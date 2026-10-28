"""Reproducible QASPER source acquisition and data-contract helpers.

The Hub and source-archive boundaries in this module are deliberately small so
tests can replace them without making network requests.  The Hub's Python
dataset script is treated as ordinary bytes and is never imported or executed.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.metadata
import json
import os
import re
import shutil
import sys
import tarfile
import tempfile
import urllib.request
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from huggingface_hub import HfApi, hf_hub_download

QASPER_DATASET_ID = "allenai/qasper"
QASPER_CONFIG_NAME = "qasper"
DEFAULT_QASPER_REVISION = "fdc9d8214fbab5dd782958601db4d678e6934a54"
SUPPORTED_SOURCE_VERSION = "0.3.0"
LOCAL_PARSER_VERSION = 1
MANIFEST_SCHEMA_VERSION = 1
HASH_ALGORITHM = "sha256-relative-path-and-file-digest-v1"
SOURCE_VERIFICATION = "sha256-and-required-members"

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_SUPPORTED_SPLITS = ("train", "validation", "test")
_DOWNLOAD_BLOCK_SIZE = 1024 * 1024
_DOWNLOAD_TIMEOUT_SECONDS = 60
_MAX_SOURCE_MEMBER_BYTES = 128 * 1024 * 1024


@dataclass(frozen=True)
class RepositoryFileSpec:
    """Expected fingerprint for a file in the pinned Hub repository."""

    file: str
    bytes: int
    sha256: str


@dataclass(frozen=True)
class SourceArchiveSpec:
    """Expected source archive and its safe member-to-split mapping."""

    url: str
    declared_bytes: int
    declared_sha256: str
    members: tuple[str, ...]
    member_splits: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class SupportedSourceProfile:
    """Immutable source contract accepted by the local parser."""

    source_version: str
    repository_files: tuple[RepositoryFileSpec, ...]
    archives: tuple[SourceArchiveSpec, ...]
    split_rows: tuple[tuple[str, int], ...]
    source_license: str


@dataclass(frozen=True)
class FileDigest:
    """Byte count and SHA-256 digest for one local file."""

    bytes: int
    sha256: str


@dataclass(frozen=True)
class ValidatedSourceMetadata:
    """Relevant, validated values extracted from ``dataset_infos.json``."""

    config_name: str
    source_version: str
    source_license: str
    split_rows: tuple[tuple[str, int], ...]
    archives: tuple[SourceArchiveSpec, ...]


@dataclass(frozen=True)
class ObservedArchive:
    """An archive specification together with its locally observed digest."""

    spec: SourceArchiveSpec
    digest: FileDigest


@dataclass(frozen=True)
class SplitDigest:
    """Digest information for one deterministic output JSONL split."""

    name: str
    file: str
    rows: int
    digest: FileDigest


@dataclass(frozen=True)
class RepositoryProvenance:
    """Revision information returned by the Hub metadata boundary."""

    requested_revision: str
    resolved_revision: str
    hub_card_licenses: tuple[str, ...] = ()


@dataclass(frozen=True)
class ObservedRepositoryFile:
    """A verified repository file downloaded from one resolved revision."""

    spec: RepositoryFileSpec
    path: Path
    digest: FileDigest


@dataclass(frozen=True)
class QasperAcquisitionResult:
    """Metadata returned after a QASPER acquisition is published."""

    output_dir: Path
    requested_revision: str
    resolved_revision: str
    split_rows: tuple[tuple[str, int], ...]
    aggregate_sha256: str


def _path_exists(path: Path) -> bool:
    """Return whether a path exists, including a dangling symlink."""

    return os.path.lexists(os.fspath(path))


def _remove_directory(path: Path) -> None:
    """Remove one known staging or backup directory without following links."""

    path = Path(path)
    if not _path_exists(path):
        return
    if path.is_symlink():
        path.unlink()
        return
    if not path.is_dir():
        raise ValueError(f"Expected a directory to remove: {path}")
    shutil.rmtree(path)


def _rename_directory(source: Path, destination: Path) -> None:
    """Rename one directory on the same filesystem."""

    Path(source).rename(Path(destination))


def _validate_publishable_staging(staging_dir: Path) -> None:
    """Require a staging directory to contain exactly the published files."""

    staging_dir = Path(staging_dir)
    if not staging_dir.is_dir() or staging_dir.is_symlink():
        raise ValueError(f"Staging path is not a regular directory: {staging_dir}")

    expected_names = {"train.jsonl", "validation.jsonl", "test.jsonl", "manifest.json"}
    entries = list(staging_dir.iterdir())
    if {entry.name for entry in entries} != expected_names:
        raise ValueError("Staging directory contains unexpected acquisition files")
    if any(not entry.is_file() or entry.is_symlink() for entry in entries):
        raise ValueError("Staging directory contains a non-regular published file")


def _publish_staging_directory(
    staging_dir: Path,
    output_dir: Path,
    *,
    force: bool,
) -> None:
    """Publish a validated staging directory with replacement rollback."""

    staging_dir = Path(staging_dir)
    output_dir = Path(output_dir)
    _validate_publishable_staging(staging_dir)

    target_exists = _path_exists(output_dir)
    if target_exists and not force:
        raise FileExistsError(f"Output directory already exists: {output_dir}")
    if target_exists and (output_dir.is_symlink() or not output_dir.is_dir()):
        raise ValueError(f"Output path is not a regular directory: {output_dir}")

    backup_dir: Path | None = None
    if target_exists:
        while True:
            candidate = output_dir.parent / f"tmp_qasper_backup_{os.urandom(8).hex()}"
            if not _path_exists(candidate):
                backup_dir = candidate
                break
        _rename_directory(output_dir, backup_dir)

    try:
        _rename_directory(staging_dir, output_dir)
    except OSError:
        if backup_dir is None:
            raise
        try:
            _rename_directory(backup_dir, output_dir)
        except OSError as rollback_error:
            raise RuntimeError(
                "Could not publish the new QASPER acquisition and could not restore "
                f"the previous output directory; backup remains at {backup_dir}"
            ) from rollback_error
        raise

    if backup_dir is not None:
        try:
            _remove_directory(backup_dir)
        except OSError as cleanup_error:
            raise RuntimeError(
                "New QASPER acquisition was published, but the previous output "
                f"backup could not be removed: {backup_dir}"
            ) from cleanup_error


SUPPORTED_SOURCE_PROFILE = SupportedSourceProfile(
    source_version=SUPPORTED_SOURCE_VERSION,
    repository_files=(
        RepositoryFileSpec(
            file="qasper.py",
            bytes=5950,
            sha256="381d623d4992118738c0a17b9c8219136f493eda381125716ab32b814d0b3c0a",
        ),
        RepositoryFileSpec(
            file="dataset_infos.json",
            bytes=8145,
            sha256="c5a5b7abb6a0a91b2d9b173cdf1224d3d6e400b3d658d322acb67e12305dd5bf",
        ),
    ),
    archives=(
        SourceArchiveSpec(
            url="https://qasper-dataset.s3.us-west-2.amazonaws.com/qasper-train-dev-v0.3.tgz",
            declared_bytes=10835856,
            declared_sha256="a28fdf966db827bcee3d873107d6b6669864fb7ca8fbf73a192f5e39191bdb5a",
            members=("qasper-train-v0.3.json", "qasper-dev-v0.3.json"),
            member_splits=(
                ("qasper-train-v0.3.json", "train"),
                ("qasper-dev-v0.3.json", "validation"),
            ),
        ),
        SourceArchiveSpec(
            url="https://qasper-dataset.s3.us-west-2.amazonaws.com/qasper-test-and-evaluator-v0.3.tgz",
            declared_bytes=3865061,
            declared_sha256="72a52a41193e2838b8074f80ac074b94f956b84886c36a61c58a7df4171bdd72",
            members=("qasper-test-v0.3.json",),
            member_splits=(("qasper-test-v0.3.json", "test"),),
        ),
    ),
    split_rows=(("train", 888), ("validation", 281), ("test", 416)),
    source_license="CC BY 4.0",
)


def _extract_hub_card_licenses(dataset_info: object) -> tuple[str, ...]:
    """Read dataset-card licenses without depending on a Hub model version."""

    card_data = getattr(dataset_info, "cardData", None)
    if card_data is None:
        card_data = getattr(dataset_info, "card_data", None)

    if isinstance(card_data, Mapping):
        license_value = card_data.get("license")
    else:
        license_value = getattr(card_data, "license", None)
    if license_value is None:
        license_value = getattr(dataset_info, "license", None)
    if license_value is None:
        return ()

    if isinstance(license_value, str):
        licenses = (license_value,)
    elif isinstance(license_value, Sequence) and not isinstance(
        license_value, (str, bytes, bytearray)
    ):
        licenses = tuple(license_value)
    else:
        raise TypeError("Hub dataset-card license must be a string or sequence")

    if any(
        not isinstance(license_name, str) or not license_name
        for license_name in licenses
    ):
        raise ValueError("Hub dataset-card licenses must be non-empty strings")
    return licenses


def resolve_qasper_revision(requested_revision: str) -> RepositoryProvenance:
    """Resolve a Hub branch, tag, or SHA to an immutable commit SHA.

    The request is limited to the fixed QASPER repository and explicitly
    disables authentication so public-data access has no hidden credential
    dependency.
    """

    if not isinstance(requested_revision, str) or not requested_revision.strip():
        raise ValueError("requested_revision must be a non-empty string")

    dataset_info = HfApi().dataset_info(
        QASPER_DATASET_ID,
        revision=requested_revision,
        files_metadata=True,
        token=False,
    )
    resolved_revision = getattr(dataset_info, "sha", None)
    if not isinstance(resolved_revision, str) or not _COMMIT_SHA_RE.fullmatch(
        resolved_revision
    ):
        raise ValueError("Hub did not return a full lowercase commit SHA")

    return RepositoryProvenance(
        requested_revision=requested_revision,
        resolved_revision=resolved_revision,
        hub_card_licenses=_extract_hub_card_licenses(dataset_info),
    )


def _download_repository_file(
    spec: RepositoryFileSpec,
    resolved_revision: str,
    cache_dir: Path,
) -> ObservedRepositoryFile:
    """Download and fingerprint one fixed repository file from the Hub."""

    if not _COMMIT_SHA_RE.fullmatch(resolved_revision):
        raise ValueError("resolved_revision must be a full lowercase commit SHA")
    cache_dir.mkdir(parents=True, exist_ok=True)
    downloaded_path = Path(
        hf_hub_download(
            repo_id=QASPER_DATASET_ID,
            filename=spec.file,
            repo_type="dataset",
            revision=resolved_revision,
            cache_dir=str(cache_dir),
            token=False,
        )
    )
    if not downloaded_path.is_file():
        raise FileNotFoundError(
            f"Hub file was not downloaded as a regular file: {spec.file}"
        )

    digest = _file_digest(downloaded_path)
    if digest.bytes != spec.bytes or digest.sha256 != spec.sha256:
        raise ValueError(
            f"Repository file fingerprint changed for {spec.file}: "
            f"observed {digest.bytes} bytes/{digest.sha256}, "
            f"expected {spec.bytes} bytes/{spec.sha256}"
        )
    return ObservedRepositoryFile(spec=spec, path=downloaded_path, digest=digest)


def _download_and_verify_repository_files(
    resolved_revision: str,
    cache_dir: Path,
    profile: SupportedSourceProfile = SUPPORTED_SOURCE_PROFILE,
) -> tuple[ObservedRepositoryFile, ...]:
    """Download and verify all repository files in the supported source profile."""

    return tuple(
        _download_repository_file(spec, resolved_revision, cache_dir)
        for spec in profile.repository_files
    )


def _open_source_archive(url: str) -> object:
    """Open one public source archive through a replaceable network boundary."""

    return urllib.request.urlopen(url, timeout=_DOWNLOAD_TIMEOUT_SECONDS)


def _download_and_verify_archive(
    spec: SourceArchiveSpec,
    destination: Path,
) -> ObservedArchive:
    """Stream one official archive to disk and verify its bytes and SHA-256."""

    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        with (
            _open_source_archive(spec.url) as response,
            destination.open("wb") as handle,
        ):
            while True:
                block = response.read(_DOWNLOAD_BLOCK_SIZE)  # type: ignore[attr-defined]
                if not block:
                    break
                handle.write(block)
    except BaseException:
        if destination.is_file():
            destination.unlink()
        raise

    digest = _file_digest(destination)
    if digest.bytes != spec.declared_bytes or digest.sha256 != spec.declared_sha256:
        try:
            destination.unlink()
        except OSError:
            pass
        raise ValueError(
            f"Source archive fingerprint mismatch for {spec.url}: "
            f"observed {digest.bytes} bytes/{digest.sha256}, "
            f"expected {spec.declared_bytes} bytes/{spec.declared_sha256}"
        )
    return ObservedArchive(spec=spec, digest=digest)


def _validate_archive_member_spec(spec: SourceArchiveSpec) -> dict[str, str]:
    """Validate a source archive's root-member and output-split contract."""

    if not spec.members:
        raise ValueError(f"Source archive {spec.url} has no required members")

    member_names = list(spec.members)
    if len(set(member_names)) != len(member_names):
        raise ValueError(f"Source archive {spec.url} declares duplicate members")
    for member_name in member_names:
        if (
            not isinstance(member_name, str)
            or not member_name
            or "\x00" in member_name
            or "\\" in member_name
            or PurePosixPath(member_name).parts != (member_name,)
        ):
            raise ValueError(
                f"Source archive member is not a safe root filename: {member_name!r}"
            )

    member_to_split: dict[str, str] = {}
    for member_name, split_name in spec.member_splits:
        if not isinstance(member_name, str) or not isinstance(split_name, str):
            raise TypeError("Source archive member mappings must contain strings")
        if member_name in member_to_split:
            raise ValueError(f"Source archive {spec.url} maps a member more than once")
        if split_name not in _SUPPORTED_SPLITS:
            raise ValueError(f"Unsupported QASPER output split: {split_name!r}")
        member_to_split[member_name] = split_name

    if set(member_to_split) != set(member_names):
        raise ValueError(
            f"Source archive {spec.url} member mappings do not cover its required members"
        )
    if len(set(member_to_split.values())) != len(member_to_split):
        raise ValueError(
            f"Source archive {spec.url} maps multiple members to one split"
        )
    return member_to_split


def _read_archive_splits(
    archive_path: Path,
    spec: SourceArchiveSpec,
    *,
    max_member_bytes: int = _MAX_SOURCE_MEMBER_BYTES,
) -> dict[str, list[dict[str, object]]]:
    """Read and normalize the explicitly required JSON members of one archive."""

    if max_member_bytes <= 0:
        raise ValueError("max_member_bytes must be positive")
    member_to_split = _validate_archive_member_spec(spec)
    archive_path = Path(archive_path)
    if not archive_path.is_file():
        raise FileNotFoundError(f"Source archive is not a regular file: {archive_path}")

    try:
        with tarfile.open(archive_path, mode="r:gz") as archive:
            required_names = set(member_to_split)
            occurrences: dict[str, list[tarfile.TarInfo]] = {
                member_name: [] for member_name in spec.members
            }
            for member in archive.getmembers():
                if member.name in required_names:
                    occurrences[member.name].append(member)

            for member_name in spec.members:
                matching_members = occurrences[member_name]
                if not matching_members:
                    raise ValueError(
                        f"Source archive {spec.url} is missing required member {member_name!r}"
                    )
                if len(matching_members) != 1:
                    raise ValueError(
                        f"Source archive {spec.url} contains duplicate member {member_name!r}"
                    )

            split_records: dict[str, list[dict[str, object]]] = {}
            for member_name in spec.members:
                member = occurrences[member_name][0]
                if not member.isfile():
                    raise ValueError(
                        f"Required source archive member is not a regular file: {member_name!r}"
                    )
                if member.size < 0 or member.size > max_member_bytes:
                    raise ValueError(
                        f"Source archive member {member_name!r} exceeds the allowed size"
                    )

                extracted = archive.extractfile(member)
                if extracted is None:
                    raise ValueError(
                        f"Could not read source archive member {member_name!r}"
                    )
                with extracted:
                    payload = extracted.read(max_member_bytes + 1)
                if len(payload) != member.size:
                    raise ValueError(
                        f"Source archive member {member_name!r} has an unexpected byte count"
                    )
                if len(payload) > max_member_bytes:
                    raise ValueError(
                        f"Source archive member {member_name!r} exceeds the allowed size"
                    )

                try:
                    parsed = json.loads(payload.decode("utf-8"))
                except (UnicodeDecodeError, json.JSONDecodeError) as error:
                    raise ValueError(
                        f"Source archive member {member_name!r} is not valid UTF-8 JSON"
                    ) from error
                if not isinstance(parsed, Mapping):
                    raise TypeError(
                        f"Source archive member {member_name!r} must contain a JSON object"
                    )

                records: list[dict[str, object]] = []
                for paper_id, source_record in parsed.items():
                    if not isinstance(paper_id, str) or not paper_id:
                        raise ValueError(
                            f"Source archive member {member_name!r} contains an empty paper ID"
                        )
                    if not isinstance(source_record, Mapping):
                        raise TypeError(
                            f"QASPER paper {paper_id!r} in {member_name!r} is not an object"
                        )
                    records.append(_normalize_qasper_record(paper_id, source_record))

                split_records[member_to_split[member_name]] = records
            return split_records
    except tarfile.TarError as error:
        raise ValueError(f"Could not read source archive {archive_path}") from error


def _load_qasper_splits(
    archive_paths: Mapping[str, Path],
    source_metadata: ValidatedSourceMetadata,
) -> dict[str, list[dict[str, object]]]:
    """Read all supported archives and verify metadata-declared split row counts."""

    expected_archives = {archive.url: archive for archive in source_metadata.archives}
    if len(expected_archives) != len(source_metadata.archives):
        raise ValueError("Source metadata contains duplicate archive URLs")
    if set(archive_paths) != set(expected_archives):
        raise ValueError("Archive paths do not match the validated source metadata")

    split_records: dict[str, list[dict[str, object]]] = {}
    for archive_spec in source_metadata.archives:
        archive_splits = _read_archive_splits(
            Path(archive_paths[archive_spec.url]),
            archive_spec,
        )
        for split_name, records in archive_splits.items():
            if split_name in split_records:
                raise ValueError(f"Duplicate QASPER output split: {split_name}")
            split_records[split_name] = records

    expected_rows = dict(source_metadata.split_rows)
    if len(expected_rows) != len(source_metadata.split_rows):
        raise ValueError("Source metadata contains duplicate split names")
    if set(split_records) != set(expected_rows):
        raise ValueError("QASPER archive members do not produce the required splits")

    for split_name, expected_count in source_metadata.split_rows:
        observed_count = len(split_records[split_name])
        if observed_count != expected_count:
            raise ValueError(
                f"QASPER split {split_name!r} contains {observed_count} records; "
                f"expected {expected_count}"
            )
    return {
        split_name: split_records[split_name]
        for split_name, _ in source_metadata.split_rows
    }


_EXPECTED_FEATURE_SIGNATURE = (
    "struct",
    {
        "id": ("value", "string"),
        "title": ("value", "string"),
        "abstract": ("value", "string"),
        "full_text": (
            "sequence",
            (
                "struct",
                {
                    "section_name": ("value", "string"),
                    "paragraphs": ("list", ("value", "string")),
                },
            ),
        ),
        "qas": (
            "sequence",
            (
                "struct",
                {
                    "question": ("value", "string"),
                    "question_id": ("value", "string"),
                    "nlp_background": ("value", "string"),
                    "topic_background": ("value", "string"),
                    "paper_read": ("value", "string"),
                    "search_query": ("value", "string"),
                    "question_writer": ("value", "string"),
                    "answers": (
                        "sequence",
                        (
                            "struct",
                            {
                                "answer": (
                                    "struct",
                                    {
                                        "unanswerable": ("value", "bool"),
                                        "extractive_spans": (
                                            "sequence",
                                            ("value", "string"),
                                        ),
                                        "yes_no": ("value", "bool"),
                                        "free_form_answer": ("value", "string"),
                                        "evidence": ("sequence", ("value", "string")),
                                        "highlighted_evidence": (
                                            "sequence",
                                            ("value", "string"),
                                        ),
                                    },
                                ),
                                "annotation_id": ("value", "string"),
                                "worker_id": ("value", "string"),
                            },
                        ),
                    ),
                },
            ),
        ),
        "figures_and_tables": (
            "sequence",
            (
                "struct",
                {
                    "caption": ("value", "string"),
                    "file": ("value", "string"),
                },
            ),
        ),
    },
)


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    """Calculate a file's SHA-256 digest without loading it all into memory."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _file_digest(path: Path) -> FileDigest:
    return FileDigest(bytes=path.stat().st_size, sha256=_sha256_file(path))


def _feature_signature(feature: object) -> object:
    if isinstance(feature, list):
        if len(feature) != 1:
            raise ValueError("A list feature must contain exactly one item schema")
        return ("list", _feature_signature(feature[0]))

    if not isinstance(feature, Mapping):
        raise TypeError("Feature metadata must be a mapping or one-item list")

    if feature.get("_type") == "Sequence":
        if "feature" not in feature:
            raise ValueError("Sequence feature is missing its child feature")
        return ("sequence", _feature_signature(feature["feature"]))

    if "dtype" in feature:
        return ("value", feature["dtype"])

    return (
        "struct",
        {str(key): _feature_signature(value) for key, value in feature.items()},
    )


def _as_mapping(value: object, context: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise TypeError(f"{context} must be a JSON object")
    return value


def _validate_source_metadata(
    metadata: Mapping[str, object],
    profile: SupportedSourceProfile = SUPPORTED_SOURCE_PROFILE,
) -> ValidatedSourceMetadata:
    """Validate pinned ``dataset_infos.json`` data without executing source code."""

    root = _as_mapping(metadata, "dataset_infos")
    if set(root) != {QASPER_CONFIG_NAME}:
        raise ValueError("dataset_infos contains an unsupported configuration")
    config = _as_mapping(root.get(QASPER_CONFIG_NAME), "dataset_infos.qasper")

    version = _as_mapping(config.get("version"), "dataset_infos.qasper.version")
    source_version = version.get("version_str")
    if source_version != profile.source_version:
        raise ValueError(
            f"Unsupported QASPER source version: {source_version!r}; "
            f"expected {profile.source_version!r}"
        )

    if config.get("config_name") not in (None, QASPER_CONFIG_NAME):
        raise ValueError("QASPER metadata has an unexpected config name")

    source_license = config.get("license")
    if source_license != profile.source_license:
        raise ValueError(
            f"Unsupported QASPER source license: {source_license!r}; "
            f"expected {profile.source_license!r}"
        )

    features = _as_mapping(config.get("features"), "dataset_infos.qasper.features")
    if _feature_signature(features) != _EXPECTED_FEATURE_SIGNATURE:
        raise ValueError("QASPER feature schema is not supported by the local parser")

    split_metadata = _as_mapping(config.get("splits"), "dataset_infos.qasper.splits")
    expected_split_rows = dict(profile.split_rows)
    if set(split_metadata) != set(expected_split_rows):
        raise ValueError("QASPER split metadata does not match the supported profile")

    split_rows: list[tuple[str, int]] = []
    for split_name in _SUPPORTED_SPLITS:
        split = _as_mapping(split_metadata.get(split_name), f"split {split_name}")
        if split.get("name") != split_name:
            raise ValueError(f"QASPER split {split_name!r} has an unexpected name")
        row_count = split.get("num_examples")
        if not isinstance(row_count, int) or isinstance(row_count, bool):
            raise TypeError(f"QASPER split {split_name!r} has an invalid row count")
        if row_count != expected_split_rows[split_name]:
            raise ValueError(
                f"QASPER split {split_name!r} declares {row_count} rows; "
                f"expected {expected_split_rows[split_name]}"
            )
        split_rows.append((split_name, row_count))

    checksums = _as_mapping(
        config.get("download_checksums"), "dataset_infos.qasper.download_checksums"
    )
    expected_archives = {archive.url: archive for archive in profile.archives}
    if set(checksums) != set(expected_archives):
        raise ValueError("QASPER archive metadata does not match the supported profile")

    for url, archive in expected_archives.items():
        checksum = _as_mapping(checksums.get(url), f"archive checksum {url}")
        if checksum.get("num_bytes") != archive.declared_bytes:
            raise ValueError(f"Archive byte declaration changed for {url}")
        if checksum.get("checksum") != archive.declared_sha256:
            raise ValueError(f"Archive checksum declaration changed for {url}")

    return ValidatedSourceMetadata(
        config_name=QASPER_CONFIG_NAME,
        source_version=source_version,
        source_license=source_license,
        split_rows=tuple(split_rows),
        archives=profile.archives,
    )


def _copy_sequence_records(value: object, context: str) -> list[dict[str, object]]:
    """Convert a dict-of-lists sequence to a list-of-dicts without value edits."""

    if isinstance(value, list):
        records = value
    elif isinstance(value, Mapping):
        if not value:
            return []
        field_values: dict[str, list[object]] = {}
        for field, field_value in value.items():
            if not isinstance(field_value, list):
                raise TypeError(f"{context}.{field} must be a list")
            field_values[str(field)] = field_value
        lengths = {len(items) for items in field_values.values()}
        if len(lengths) != 1:
            raise ValueError(f"{context} fields have inconsistent lengths")
        record_count = next(iter(lengths))
        records = [
            {
                field: copy.deepcopy(values[index])
                for field, values in field_values.items()
            }
            for index in range(record_count)
        ]
    else:
        raise TypeError(f"{context} must be a list or dict of lists")

    copied_records: list[dict[str, object]] = []
    for index, record in enumerate(records):
        if not isinstance(record, Mapping):
            raise TypeError(f"{context}[{index}] must be an object")
        copied_records.append(
            {str(key): copy.deepcopy(item) for key, item in record.items()}
        )
    return copied_records


def _normalize_answers(value: object) -> list[dict[str, object]]:
    answers = _copy_sequence_records(value, "qas.answers")
    for answer_record in answers:
        if "answer" in answer_record and isinstance(answer_record["answer"], Mapping):
            answer_record["answer"] = copy.deepcopy(answer_record["answer"])
    return answers


def _normalize_qasper_record(
    paper_id: str,
    source_record: Mapping[str, object],
) -> dict[str, object]:
    """Apply the old QASPER builder's nested-sequence compatibility conversion."""

    if not isinstance(paper_id, str) or not paper_id:
        raise ValueError("paper_id must be a non-empty string")
    record = _as_mapping(source_record, "QASPER paper record")
    normalized = {str(key): copy.deepcopy(value) for key, value in record.items()}

    if "id" in normalized and normalized["id"] != paper_id:
        raise ValueError(f"QASPER record id conflicts with its paper key {paper_id!r}")
    normalized["id"] = paper_id

    if "full_text" in normalized:
        sections = _copy_sequence_records(normalized["full_text"], "full_text")
        for section in sections:
            if "paragraphs" in section:
                paragraphs = section["paragraphs"]
                if not isinstance(paragraphs, list):
                    raise ValueError("full_text section paragraphs must be a list")
                section["paragraphs"] = copy.deepcopy(paragraphs)
        normalized["full_text"] = sections

    if "qas" in normalized:
        questions = _copy_sequence_records(normalized["qas"], "qas")
        for question in questions:
            if "answers" in question:
                question["answers"] = _normalize_answers(question["answers"])
        normalized["qas"] = questions

    if "figures_and_tables" in normalized:
        normalized["figures_and_tables"] = _copy_sequence_records(
            normalized["figures_and_tables"], "figures_and_tables"
        )

    return normalized


def _write_split_jsonl(
    records: Iterable[Mapping[str, object]],
    destination: Path,
) -> tuple[int, FileDigest]:
    """Write deterministic UTF-8 JSONL and return its row count and digest."""

    destination.parent.mkdir(parents=True, exist_ok=True)
    row_count = 0
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            if not isinstance(record, Mapping):
                raise TypeError("JSONL records must be mappings")
            line = json.dumps(
                record,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
            handle.write(line)
            handle.write("\n")
            row_count += 1

    return row_count, _file_digest(destination)


def _validate_sha256(value: str, context: str) -> str:
    if not isinstance(value, str) or not _SHA256_RE.fullmatch(value):
        raise ValueError(f"{context} must be a lowercase SHA-256 digest")
    return value


def _validate_relative_path(value: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("aggregate-hash paths must be non-empty strings")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(
            f"aggregate-hash path is not a safe relative POSIX path: {value!r}"
        )
    return value


def _aggregate_sha256(file_digests: Mapping[str, FileDigest | str]) -> str:
    """Hash sorted relative paths and their already-calculated file digests."""

    aggregate_input = bytearray()
    for relative_path in sorted(file_digests):
        safe_path = _validate_relative_path(relative_path)
        digest_value = file_digests[relative_path]
        digest = (
            digest_value.sha256
            if isinstance(digest_value, FileDigest)
            else digest_value
        )
        _validate_sha256(digest, f"digest for {relative_path}")
        aggregate_input.extend(f"{safe_path}\0{digest}\n".encode())
    return _sha256_bytes(bytes(aggregate_input))


def _coerce_file_digest(
    value: FileDigest | Mapping[str, object], context: str
) -> FileDigest:
    if isinstance(value, FileDigest):
        digest = value
    elif isinstance(value, Mapping):
        byte_count = value.get("bytes")
        digest_value = value.get("sha256")
        if not isinstance(byte_count, int) or isinstance(byte_count, bool):
            raise TypeError(f"{context}.bytes must be an integer")
        digest = FileDigest(bytes=byte_count, sha256=digest_value)  # type: ignore[arg-type]
    else:
        raise TypeError(f"{context} must be a FileDigest or mapping")
    if digest.bytes < 0:
        raise ValueError(f"{context}.bytes must be non-negative")
    _validate_sha256(digest.sha256, f"{context}.sha256")
    return digest


def _build_manifest(
    *,
    requested_revision: str,
    resolved_revision: str,
    source_metadata: ValidatedSourceMetadata,
    repository_files: Mapping[str, FileDigest | Mapping[str, object]],
    source_archives: Sequence[ObservedArchive],
    splits: Sequence[SplitDigest],
    hub_card_licenses: Sequence[str],
    huggingface_hub_version: str,
    python_version: str | None = None,
    profile: SupportedSourceProfile = SUPPORTED_SOURCE_PROFILE,
) -> dict[str, object]:
    """Build the stable manifest payload for a validated acquisition."""

    if not requested_revision or not resolved_revision:
        raise ValueError("requested and resolved revisions must be non-empty")
    if not _COMMIT_SHA_RE.fullmatch(resolved_revision):
        raise ValueError("resolved_revision must be a full lowercase commit SHA")
    if (
        source_metadata.config_name != QASPER_CONFIG_NAME
        or source_metadata.source_version != profile.source_version
        or source_metadata.split_rows != profile.split_rows
        or source_metadata.archives != profile.archives
    ):
        raise ValueError("source metadata does not match the supported profile")

    expected_repository_files = {spec.file: spec for spec in profile.repository_files}
    if set(repository_files) != set(expected_repository_files):
        raise ValueError("manifest repository files do not match the supported profile")
    repository_file_entries: list[dict[str, object]] = []
    for spec in profile.repository_files:
        observed = _coerce_file_digest(
            repository_files[spec.file], f"repository file {spec.file}"
        )
        if observed.bytes != spec.bytes or observed.sha256 != spec.sha256:
            raise ValueError(f"repository file fingerprint changed for {spec.file}")
        repository_file_entries.append(
            {"file": spec.file, "bytes": observed.bytes, "sha256": observed.sha256}
        )

    if len(source_archives) != len(profile.archives):
        raise ValueError("manifest archive count does not match the supported profile")
    archive_entries: list[dict[str, object]] = []
    for expected, observed_archive in zip(
        profile.archives, source_archives, strict=True
    ):
        if observed_archive.spec != expected:
            raise ValueError(
                "manifest archive specification does not match the profile"
            )
        observed = _coerce_file_digest(
            observed_archive.digest, f"archive {expected.url}"
        )
        if (
            observed.bytes != expected.declared_bytes
            or observed.sha256 != expected.declared_sha256
        ):
            raise ValueError(
                f"archive fingerprint does not match declaration for {expected.url}"
            )
        archive_entries.append(
            {
                "url": expected.url,
                "declared_bytes": expected.declared_bytes,
                "observed_bytes": observed.bytes,
                "declared_sha256": expected.declared_sha256,
                "observed_sha256": observed.sha256,
                "members": list(expected.members),
            }
        )

    expected_rows = dict(source_metadata.split_rows)
    split_by_name: dict[str, SplitDigest] = {}
    for split in splits:
        if split.name in split_by_name:
            raise ValueError(f"duplicate split in manifest: {split.name}")
        split_by_name[split.name] = split
    if set(split_by_name) != set(_SUPPORTED_SPLITS):
        raise ValueError("manifest splits must be train, validation, and test")

    split_entries: list[dict[str, object]] = []
    split_file_digests: dict[str, FileDigest] = {}
    for split_name in _SUPPORTED_SPLITS:
        split = split_by_name[split_name]
        expected_file = f"{split_name}.jsonl"
        if split.file != expected_file:
            raise ValueError(f"unexpected output file for split {split_name}")
        if split.rows != expected_rows.get(split_name):
            raise ValueError(f"unexpected row count for split {split_name}")
        digest = _coerce_file_digest(split.digest, f"split {split_name}")
        split_file_digests[split.file] = digest
        split_entries.append(
            {
                "name": split.name,
                "rows": split.rows,
                "file": split.file,
                "bytes": digest.bytes,
                "sha256": digest.sha256,
            }
        )

    licenses = [str(license_name) for license_name in hub_card_licenses]
    if any(not license_name for license_name in licenses):
        raise ValueError("Hub card licenses must be non-empty strings")
    runtime_python_version = python_version or ".".join(
        str(part) for part in sys.version_info[:3]
    )
    if not huggingface_hub_version:
        raise ValueError("huggingface_hub_version must be non-empty")

    manifest: dict[str, object] = {
        "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
        "dataset": {
            "id": QASPER_DATASET_ID,
            "config": QASPER_CONFIG_NAME,
            "requested_revision": requested_revision,
            "resolved_revision": resolved_revision,
            "source_dataset_version": source_metadata.source_version,
            "local_parser_version": LOCAL_PARSER_VERSION,
        },
        "licenses": {
            "hub_card": licenses,
            "source_script": source_metadata.source_license,
        },
        "repository_files": repository_file_entries,
        "splits": split_entries,
        "source_verification": SOURCE_VERIFICATION,
        "source_archives": archive_entries,
        "libraries": {
            "python": runtime_python_version,
            "huggingface_hub": huggingface_hub_version,
        },
        "output": {
            "format": "jsonl",
            "encoding": "utf-8",
            "newline": "lf",
            "hash_algorithm": HASH_ALGORITHM,
            "aggregate_sha256": _aggregate_sha256(split_file_digests),
        },
    }
    return manifest


def _dump_manifest(manifest: Mapping[str, object], destination: Path) -> FileDigest:
    """Write a manifest with stable JSON formatting and LF newlines."""

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(
            manifest,
            handle,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        handle.write("\n")
    return _file_digest(destination)


def _load_json_object(path: Path, context: str) -> Mapping[str, object]:
    """Load one UTF-8 JSON object from a verified local source file."""

    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    return _as_mapping(value, context)


def _cleanup_staging_directory(path: Path) -> None:
    """Best-effort cleanup used only after an acquisition failure."""

    try:
        _remove_directory(path)
    except OSError:
        return


def acquire_qasper(
    output_dir: Path,
    revision: str = DEFAULT_QASPER_REVISION,
    force: bool = False,
) -> QasperAcquisitionResult:
    """Download QASPER and publish deterministic local JSONL files and a manifest.

    All downloads and generated files are built in a sibling staging directory.
    The destination is changed only after every source, serialization, and
    manifest check succeeds.
    """

    requested_output = Path(output_dir)
    output_path = Path(os.path.abspath(os.fspath(requested_output)))
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if _path_exists(output_path):
        if not force:
            raise FileExistsError(f"Output directory already exists: {output_path}")
        if output_path.is_symlink() or not output_path.is_dir():
            raise ValueError(f"Output path is not a regular directory: {output_path}")

    staging_path: Path | None = None
    try:
        staging_path = Path(
            tempfile.mkdtemp(prefix="tmp_qasper_", dir=os.fspath(output_path.parent))
        )
        hub_cache_dir = staging_path / "tmp_hf_cache"
        downloads_dir = staging_path / "tmp_downloads"

        provenance = resolve_qasper_revision(revision)
        profile = SUPPORTED_SOURCE_PROFILE
        repository_files = _download_and_verify_repository_files(
            provenance.resolved_revision,
            hub_cache_dir,
            profile=profile,
        )
        repository_by_name = {
            observed.spec.file: observed for observed in repository_files
        }
        if set(repository_by_name) != {spec.file for spec in profile.repository_files}:
            raise ValueError(
                "Downloaded repository files do not match the source profile"
            )

        dataset_infos = _load_json_object(
            repository_by_name["dataset_infos.json"].path,
            "dataset_infos",
        )
        source_metadata = _validate_source_metadata(dataset_infos, profile=profile)

        archive_paths: dict[str, Path] = {}
        observed_archives: list[ObservedArchive] = []
        for archive_index, archive_spec in enumerate(source_metadata.archives):
            archive_path = downloads_dir / f"tmp_archive_{archive_index}.tgz"
            observed_archive = _download_and_verify_archive(archive_spec, archive_path)
            observed_archives.append(observed_archive)
            archive_paths[archive_spec.url] = archive_path

        split_records = _load_qasper_splits(archive_paths, source_metadata)
        split_digests: list[SplitDigest] = []
        for split_name in _SUPPORTED_SPLITS:
            split_path = staging_path / f"{split_name}.jsonl"
            row_count, digest = _write_split_jsonl(
                split_records[split_name], split_path
            )
            split_digests.append(
                SplitDigest(
                    name=split_name,
                    file=split_path.name,
                    rows=row_count,
                    digest=digest,
                )
            )

        try:
            huggingface_hub_version = importlib.metadata.version("huggingface-hub")
        except importlib.metadata.PackageNotFoundError as error:
            raise RuntimeError(
                "huggingface-hub distribution metadata is unavailable"
            ) from error

        manifest = _build_manifest(
            requested_revision=provenance.requested_revision,
            resolved_revision=provenance.resolved_revision,
            source_metadata=source_metadata,
            repository_files={
                observed.spec.file: observed.digest for observed in repository_files
            },
            source_archives=observed_archives,
            splits=split_digests,
            hub_card_licenses=provenance.hub_card_licenses,
            huggingface_hub_version=huggingface_hub_version,
            profile=profile,
        )
        _dump_manifest(manifest, staging_path / "manifest.json")

        _remove_directory(hub_cache_dir)
        _remove_directory(downloads_dir)
        _validate_publishable_staging(staging_path)

        result = QasperAcquisitionResult(
            output_dir=output_path,
            requested_revision=provenance.requested_revision,
            resolved_revision=provenance.resolved_revision,
            split_rows=tuple((split.name, split.rows) for split in split_digests),
            aggregate_sha256=_aggregate_sha256(
                {split.file: split.digest for split in split_digests}
            ),
        )
        _publish_staging_directory(staging_path, output_path, force=force)
        return result
    finally:
        if staging_path is not None and _path_exists(staging_path):
            _cleanup_staging_directory(staging_path)
