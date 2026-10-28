import copy
import hashlib
import io
import json
import tarfile
from collections.abc import Mapping
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from typing import Self

import pytest

from src.data import qasper
from src.data.qasper import (
    DEFAULT_QASPER_REVISION,
    QASPER_DATASET_ID,
    SUPPORTED_SOURCE_PROFILE,
    FileDigest,
    ObservedArchive,
    ObservedRepositoryFile,
    RepositoryFileSpec,
    RepositoryProvenance,
    SourceArchiveSpec,
    SplitDigest,
    SupportedSourceProfile,
    ValidatedSourceMetadata,
    _aggregate_sha256,
    _build_manifest,
    _download_and_verify_archive,
    _download_and_verify_repository_files,
    _dump_manifest,
    _load_qasper_splits,
    _normalize_qasper_record,
    _publish_staging_directory,
    _read_archive_splits,
    _validate_source_metadata,
    _write_split_jsonl,
    acquire_qasper,
)


def _value_feature(dtype: str) -> dict[str, object]:
    return {"dtype": dtype, "id": None, "_type": "Value"}


def _sequence_feature(feature: object) -> dict[str, object]:
    return {"feature": feature, "length": -1, "id": None, "_type": "Sequence"}


def _metadata() -> dict[str, object]:
    answer_feature = {
        "unanswerable": _value_feature("bool"),
        "extractive_spans": _sequence_feature(_value_feature("string")),
        "yes_no": _value_feature("bool"),
        "free_form_answer": _value_feature("string"),
        "evidence": _sequence_feature(_value_feature("string")),
        "highlighted_evidence": _sequence_feature(_value_feature("string")),
    }
    qas_feature = {
        "question": _value_feature("string"),
        "question_id": _value_feature("string"),
        "nlp_background": _value_feature("string"),
        "topic_background": _value_feature("string"),
        "paper_read": _value_feature("string"),
        "search_query": _value_feature("string"),
        "question_writer": _value_feature("string"),
        "answers": _sequence_feature(
            {
                "answer": {**answer_feature},
                "annotation_id": _value_feature("string"),
                "worker_id": _value_feature("string"),
            }
        ),
    }
    features = {
        "id": _value_feature("string"),
        "title": _value_feature("string"),
        "abstract": _value_feature("string"),
        "full_text": _sequence_feature(
            {
                "section_name": _value_feature("string"),
                "paragraphs": [_value_feature("string")],
            }
        ),
        "qas": _sequence_feature(qas_feature),
        "figures_and_tables": _sequence_feature(
            {"caption": _value_feature("string"), "file": _value_feature("string")}
        ),
    }
    archives = {
        archive.url: {
            "num_bytes": archive.declared_bytes,
            "checksum": archive.declared_sha256,
        }
        for archive in SUPPORTED_SOURCE_PROFILE.archives
    }
    splits = {
        name: {"name": name, "num_examples": rows, "dataset_name": "qasper"}
        for name, rows in SUPPORTED_SOURCE_PROFILE.split_rows
    }
    return {
        "qasper": {
            "config_name": "qasper",
            "version": {"version_str": "0.3.0"},
            "license": "CC BY 4.0",
            "features": features,
            "splits": splits,
            "download_checksums": archives,
        }
    }


def _digest(seed: str, byte_count: int = 10) -> FileDigest:
    return FileDigest(
        bytes=byte_count, sha256=hashlib.sha256(seed.encode()).hexdigest()
    )


def _write_tmp_tgz(
    destination: Path,
    entries: list[tuple[str, bytes, str]],
) -> None:
    with tarfile.open(destination, mode="w:gz") as archive:
        for name, payload, entry_type in entries:
            info = tarfile.TarInfo(name)
            if entry_type == "file":
                info.size = len(payload)
                archive.addfile(info, io.BytesIO(payload))
            elif entry_type == "symlink":
                info.type = tarfile.SYMTYPE
                info.linkname = "tmp_target"
                archive.addfile(info)
            else:
                raise AssertionError(
                    f"Unsupported test archive entry type: {entry_type}"
                )


def _small_source_metadata(
    archives: tuple[SourceArchiveSpec, ...],
    split_rows: tuple[tuple[str, int], ...],
) -> ValidatedSourceMetadata:
    validated = _validate_source_metadata(_metadata())
    return replace(
        validated,
        archives=archives,
        split_rows=split_rows,
    )


def test_source_metadata_validation_is_strict_and_returns_fixed_values() -> None:
    validated = _validate_source_metadata(_metadata())

    assert validated.source_version == "0.3.0"
    assert validated.source_license == "CC BY 4.0"
    assert validated.split_rows == SUPPORTED_SOURCE_PROFILE.split_rows
    assert validated.archives == SUPPORTED_SOURCE_PROFILE.archives

    changed = copy.deepcopy(_metadata())
    changed["qasper"]["version"]["version_str"] = "0.4.0"  # type: ignore[index]
    with pytest.raises(ValueError, match="Unsupported QASPER source version"):
        _validate_source_metadata(changed)

    changed = copy.deepcopy(_metadata())
    changed["qasper"]["download_checksums"][SUPPORTED_SOURCE_PROFILE.archives[0].url][  # type: ignore[index]
        "checksum"
    ] = "0" * 64
    with pytest.raises(ValueError, match="Archive checksum declaration changed"):
        _validate_source_metadata(changed)


def test_normalize_qasper_record_preserves_values_and_converts_nested_sequences() -> (
    None
):
    source_record = {
        "title": "A paper",
        "abstract": "非 ASCII abstract",
        "full_text": {
            "section_name": ["Introduction", ""],
            "paragraphs": [["First paragraph", "第二段"], ["Last paragraph"]],
        },
        "qas": {
            "question": ["Is it useful?"],
            "question_id": ["q-1"],
            "answers": [
                {
                    "answer": [
                        {
                            "unanswerable": False,
                            "extractive_spans": ["answer"],
                            "yes_no": None,
                            "free_form_answer": "",
                            "evidence": ["First paragraph"],
                            "highlighted_evidence": ["answer"],
                        }
                    ],
                    "annotation_id": ["ann-1"],
                    "worker_id": ["worker-1"],
                }
            ],
        },
        "figures_and_tables": {"caption": ["A figure"], "file": ["fig-1"]},
        "extra": {"nested": [True, "保留"]},
    }
    original = copy.deepcopy(source_record)

    normalized = _normalize_qasper_record("paper-1", source_record)

    assert source_record == original
    assert normalized["id"] == "paper-1"
    assert normalized["full_text"] == [
        {"section_name": "Introduction", "paragraphs": ["First paragraph", "第二段"]},
        {"section_name": "", "paragraphs": ["Last paragraph"]},
    ]
    assert normalized["qas"] == [
        {
            "question": "Is it useful?",
            "question_id": "q-1",
            "answers": [
                {
                    "answer": {
                        "unanswerable": False,
                        "extractive_spans": ["answer"],
                        "yes_no": None,
                        "free_form_answer": "",
                        "evidence": ["First paragraph"],
                        "highlighted_evidence": ["answer"],
                    },
                    "annotation_id": "ann-1",
                    "worker_id": "worker-1",
                }
            ],
        }
    ]
    assert normalized["figures_and_tables"] == [
        {"caption": "A figure", "file": "fig-1"}
    ]
    assert normalized["extra"] == {"nested": [True, "保留"]}

    with pytest.raises(ValueError, match="conflicts"):
        _normalize_qasper_record("paper-1", {"id": "paper-2"})


def test_write_split_jsonl_is_utf8_sorted_compact_and_lf(tmp_path: Path) -> None:
    destination = tmp_path / "tmp_train.jsonl"
    rows, digest = _write_split_jsonl(
        [{"z": "非 ASCII", "a": [True, ""]}, {"b": 2, "a": 1}], destination
    )

    expected_bytes = (
        '{"a":[true,""] ,"z":"非 ASCII"}\n'.replace("] ,", "],") + '{"a":1,"b":2}\n'
    ).encode()
    assert destination.read_bytes() == expected_bytes
    assert b"\r" not in destination.read_bytes()
    assert rows == 2
    assert digest.bytes == len(expected_bytes)
    assert digest.sha256 == hashlib.sha256(expected_bytes).hexdigest()


def test_aggregate_hash_uses_sorted_path_digest_lines() -> None:
    train_digest = "a" * 64
    test_digest = "b" * 64
    validation_digest = "c" * 64
    expected_input = (
        f"test.jsonl\0{test_digest}\n"
        f"train.jsonl\0{train_digest}\n"
        f"validation.jsonl\0{validation_digest}\n"
    ).encode()

    actual = _aggregate_sha256(
        {
            "validation.jsonl": validation_digest,
            "train.jsonl": train_digest,
            "test.jsonl": test_digest,
        }
    )

    assert actual == hashlib.sha256(expected_input).hexdigest()


def test_manifest_is_stable_and_contains_only_reproducible_metadata(
    tmp_path: Path,
) -> None:
    validated = _validate_source_metadata(_metadata())
    repository_files = {
        spec.file: FileDigest(bytes=spec.bytes, sha256=spec.sha256)
        for spec in SUPPORTED_SOURCE_PROFILE.repository_files
    }
    archives = [
        ObservedArchive(
            spec=spec, digest=FileDigest(spec.declared_bytes, spec.declared_sha256)
        )
        for spec in SUPPORTED_SOURCE_PROFILE.archives
    ]
    splits = [
        SplitDigest(
            name=name,
            file=f"{name}.jsonl",
            rows=rows,
            digest=_digest(name, byte_count=rows),
        )
        for name, rows in SUPPORTED_SOURCE_PROFILE.split_rows
    ]

    manifest = _build_manifest(
        requested_revision=DEFAULT_QASPER_REVISION,
        resolved_revision=DEFAULT_QASPER_REVISION,
        source_metadata=validated,
        repository_files=repository_files,
        source_archives=archives,
        splits=splits,
        hub_card_licenses=("cc-by-4.0",),
        huggingface_hub_version="0.30.0",
        python_version="3.11.0",
    )
    destination = tmp_path / "tmp_manifest.json"
    manifest_digest = _dump_manifest(manifest, destination)
    reloaded = json.loads(destination.read_text(encoding="utf-8"))

    assert reloaded == manifest
    assert manifest_digest.bytes == destination.stat().st_size
    assert manifest["source_verification"] == "sha256-and-required-members"
    assert (
        manifest["output"]["hash_algorithm"]
        == "sha256-relative-path-and-file-digest-v1"
    )  # type: ignore[index]
    assert str(tmp_path) not in destination.read_text(encoding="utf-8")
    assert "generated_at" not in manifest
    assert "absolute_path" not in destination.read_text(encoding="utf-8")


def test_resolve_qasper_revision_uses_fixed_public_hub_request(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[dict[str, object]] = []

    class FakeApi:
        def dataset_info(self, *args: object, **kwargs: object) -> object:
            calls.append({"args": args, **kwargs})
            return SimpleNamespace(
                sha="a" * 40,
                cardData={"license": "cc-by-4.0"},
            )

    monkeypatch.setattr(qasper, "HfApi", FakeApi)

    provenance = qasper.resolve_qasper_revision("main")

    assert provenance.requested_revision == "main"
    assert provenance.resolved_revision == "a" * 40
    assert provenance.hub_card_licenses == ("cc-by-4.0",)
    assert calls == [
        {
            "args": (QASPER_DATASET_ID,),
            "revision": "main",
            "files_metadata": True,
            "token": False,
        }
    ]


def test_repository_files_are_downloaded_at_resolved_sha_and_fingerprinted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source_path = tmp_path / "tmp_qasper.py"
    source_bytes = b"ordinary source bytes; never execute"
    source_path.write_bytes(source_bytes)
    spec = RepositoryFileSpec(
        file="qasper.py",
        bytes=len(source_bytes),
        sha256=hashlib.sha256(source_bytes).hexdigest(),
    )
    calls: list[dict[str, object]] = []

    def fake_hf_hub_download(**kwargs: object) -> str:
        calls.append(kwargs)
        return str(source_path)

    monkeypatch.setattr(qasper, "hf_hub_download", fake_hf_hub_download)

    observed = _download_and_verify_repository_files(
        "b" * 40,
        tmp_path / "tmp_hf_cache",
        profile=replace(SUPPORTED_SOURCE_PROFILE, repository_files=(spec,)),
    )

    assert observed[0].spec == spec
    assert observed[0].path == source_path
    assert observed[0].digest == FileDigest(
        bytes=len(source_bytes), sha256=hashlib.sha256(source_bytes).hexdigest()
    )
    assert calls == [
        {
            "repo_id": QASPER_DATASET_ID,
            "filename": "qasper.py",
            "repo_type": "dataset",
            "revision": "b" * 40,
            "cache_dir": str(tmp_path / "tmp_hf_cache"),
            "token": False,
        }
    ]


def test_source_archive_is_streamed_and_verified_without_extracting(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    archive_bytes = b"tmp archive bytes"
    archive_spec = replace(
        SUPPORTED_SOURCE_PROFILE.archives[0],
        declared_bytes=len(archive_bytes),
        declared_sha256=hashlib.sha256(archive_bytes).hexdigest(),
    )
    calls: list[str] = []

    class FakeResponse:
        def __init__(self, payload: bytes) -> None:
            self.remaining = payload

        def __enter__(self) -> Self:
            return self

        def __exit__(self, *args: object) -> None:
            return None

        def read(self, size: int) -> bytes:
            del size
            if self.remaining:
                value = self.remaining
                self.remaining = b""
                return value
            return b""

    def fake_open(url: str) -> FakeResponse:
        calls.append(url)
        return FakeResponse(archive_bytes)

    monkeypatch.setattr(qasper, "_open_source_archive", fake_open)
    destination = tmp_path / "tmp_downloads" / "tmp_qasper.tgz"

    observed = _download_and_verify_archive(archive_spec, destination)

    assert observed == ObservedArchive(
        spec=archive_spec,
        digest=FileDigest(
            bytes=len(archive_bytes), sha256=hashlib.sha256(archive_bytes).hexdigest()
        ),
    )
    assert destination.read_bytes() == archive_bytes
    assert calls == [archive_spec.url]

    bad_destination = tmp_path / "tmp_downloads" / "tmp_bad_qasper.tgz"
    with pytest.raises(ValueError, match="fingerprint mismatch"):
        _download_and_verify_archive(
            replace(archive_spec, declared_sha256="0" * 64), bad_destination
        )
    assert not bad_destination.exists()


def test_read_archive_splits_maps_members_in_source_order_without_extracting(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    train_spec = replace(
        SUPPORTED_SOURCE_PROFILE.archives[0],
        url="tmp://train-dev",
        members=("tmp-train.json", "tmp-dev.json"),
        member_splits=(
            ("tmp-train.json", "train"),
            ("tmp-dev.json", "validation"),
        ),
    )
    test_spec = replace(
        SUPPORTED_SOURCE_PROFILE.archives[1],
        url="tmp://test",
        members=("tmp-test.json",),
        member_splits=(("tmp-test.json", "test"),),
    )
    train_archive = tmp_path / "tmp_train_dev.tgz"
    test_archive = tmp_path / "tmp_test.tgz"
    _write_tmp_tgz(
        train_archive,
        [
            (
                "tmp-train.json",
                json.dumps(
                    {"paper-b": {"title": "B"}, "paper-a": {"title": "A"}},
                    ensure_ascii=False,
                ).encode("utf-8"),
                "file",
            ),
            (
                "tmp-dev.json",
                json.dumps({"paper-dev": {"title": "Dev"}}).encode("utf-8"),
                "file",
            ),
            ("evaluator.json", b"ignored", "file"),
            ("../tmp_evil.txt", b"ignored", "file"),
        ],
    )
    _write_tmp_tgz(
        test_archive,
        [
            (
                "tmp-test.json",
                json.dumps({"paper-test": {"title": "Test"}}).encode("utf-8"),
                "file",
            )
        ],
    )

    def forbidden_extract(*args: object, **kwargs: object) -> None:
        del args, kwargs
        raise AssertionError("archive extraction must not be used")

    monkeypatch.setattr(tarfile.TarFile, "extract", forbidden_extract)
    monkeypatch.setattr(tarfile.TarFile, "extractall", forbidden_extract)

    metadata = _small_source_metadata(
        (train_spec, test_spec),
        (("train", 2), ("validation", 1), ("test", 1)),
    )
    splits = _load_qasper_splits(
        {train_spec.url: train_archive, test_spec.url: test_archive},
        metadata,
    )

    assert list(splits) == ["train", "validation", "test"]
    assert [record["id"] for record in splits["train"]] == ["paper-b", "paper-a"]
    assert splits["validation"][0]["id"] == "paper-dev"
    assert splits["test"][0]["id"] == "paper-test"
    assert not (tmp_path / "tmp_evil.txt").exists()


def test_read_archive_splits_rejects_missing_duplicate_and_non_regular_members(
    tmp_path: Path,
) -> None:
    spec = replace(
        SUPPORTED_SOURCE_PROFILE.archives[0],
        url="tmp://single",
        members=("tmp-records.json",),
        member_splits=(("tmp-records.json", "train"),),
    )

    missing_archive = tmp_path / "tmp_missing.tgz"
    _write_tmp_tgz(missing_archive, [("other.json", b"{}", "file")])
    with pytest.raises(ValueError, match="missing required member"):
        _read_archive_splits(missing_archive, spec)

    duplicate_archive = tmp_path / "tmp_duplicate.tgz"
    _write_tmp_tgz(
        duplicate_archive,
        [
            ("tmp-records.json", b"{}", "file"),
            ("tmp-records.json", b"{}", "file"),
        ],
    )
    with pytest.raises(ValueError, match="duplicate member"):
        _read_archive_splits(duplicate_archive, spec)

    symlink_archive = tmp_path / "tmp_symlink.tgz"
    _write_tmp_tgz(symlink_archive, [("tmp-records.json", b"", "symlink")])
    with pytest.raises(ValueError, match="not a regular file"):
        _read_archive_splits(symlink_archive, spec)


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        (b"\xff", "valid UTF-8 JSON"),
        (b"{", "valid UTF-8 JSON"),
        (b"[]", "must contain a JSON object"),
        (b'{"": {}}', "empty paper ID"),
        (b'{"paper": []}', "is not an object"),
        (b'{"paper": {"id": "other"}}', "conflicts"),
    ],
)
def test_read_archive_splits_rejects_invalid_member_content(
    tmp_path: Path,
    payload: bytes,
    message: str,
) -> None:
    spec = replace(
        SUPPORTED_SOURCE_PROFILE.archives[0],
        url="tmp://invalid",
        members=("tmp-records.json",),
        member_splits=(("tmp-records.json", "train"),),
    )
    archive_path = tmp_path / "tmp_invalid.tgz"
    _write_tmp_tgz(archive_path, [("tmp-records.json", payload, "file")])

    with pytest.raises((ValueError, TypeError), match=message):
        _read_archive_splits(archive_path, spec)


def test_read_archive_splits_rejects_oversized_member(tmp_path: Path) -> None:
    spec = replace(
        SUPPORTED_SOURCE_PROFILE.archives[0],
        url="tmp://oversized",
        members=("tmp-records.json",),
        member_splits=(("tmp-records.json", "train"),),
    )
    archive_path = tmp_path / "tmp_oversized.tgz"
    _write_tmp_tgz(archive_path, [("tmp-records.json", b"{}", "file")])

    with pytest.raises(ValueError, match="exceeds the allowed size"):
        _read_archive_splits(archive_path, spec, max_member_bytes=1)


def test_load_qasper_splits_rejects_archive_set_and_row_count_mismatches(
    tmp_path: Path,
) -> None:
    spec = replace(
        SUPPORTED_SOURCE_PROFILE.archives[0],
        url="tmp://single",
        members=("tmp-records.json",),
        member_splits=(("tmp-records.json", "train"),),
    )
    archive_path = tmp_path / "tmp_records.tgz"
    _write_tmp_tgz(
        archive_path,
        [("tmp-records.json", b'{"paper": {"title": "A"}}', "file")],
    )
    metadata = _small_source_metadata((spec,), (("train", 2),))

    with pytest.raises(ValueError, match="Archive paths do not match"):
        _load_qasper_splits({}, metadata)
    with pytest.raises(ValueError, match="expected 2"):
        _load_qasper_splits({spec.url: archive_path}, metadata)


def _acquisition_fixture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> SupportedSourceProfile:
    """Install a small fully offline source profile for acquisition tests."""

    qasper_payload = b"# qasper source\n"
    infos_payload = b"{}"
    repository_specs = (
        RepositoryFileSpec(
            file="qasper.py",
            bytes=len(qasper_payload),
            sha256=hashlib.sha256(qasper_payload).hexdigest(),
        ),
        RepositoryFileSpec(
            file="dataset_infos.json",
            bytes=len(infos_payload),
            sha256=hashlib.sha256(infos_payload).hexdigest(),
        ),
    )
    archive_payload = b"tmp archive payload"
    archive_spec = SourceArchiveSpec(
        url="tmp://qasper-archive",
        declared_bytes=len(archive_payload),
        declared_sha256=hashlib.sha256(archive_payload).hexdigest(),
        members=("tmp-records.json",),
        member_splits=(("tmp-records.json", "train"),),
    )
    profile = SupportedSourceProfile(
        source_version="0.3.0",
        repository_files=repository_specs,
        archives=(archive_spec,),
        split_rows=(("train", 1), ("validation", 1), ("test", 1)),
        source_license="CC BY 4.0",
    )
    monkeypatch.setattr(qasper, "SUPPORTED_SOURCE_PROFILE", profile)

    def fake_resolve(requested_revision: str) -> RepositoryProvenance:
        return RepositoryProvenance(
            requested_revision=requested_revision,
            resolved_revision="a" * 40,
            hub_card_licenses=("cc-by-4.0",),
        )

    def fake_repository_files(
        resolved_revision: str,
        cache_dir: Path,
        *,
        profile: SupportedSourceProfile,
    ) -> tuple[ObservedRepositoryFile, ...]:
        assert resolved_revision == "a" * 40
        cache_dir.mkdir(parents=True, exist_ok=True)
        payloads = {"qasper.py": qasper_payload, "dataset_infos.json": infos_payload}
        observed: list[ObservedRepositoryFile] = []
        for spec in profile.repository_files:
            path = cache_dir / f"tmp_{spec.file}"
            path.write_bytes(payloads[spec.file])
            observed.append(
                ObservedRepositoryFile(
                    spec=spec,
                    path=path,
                    digest=FileDigest(bytes=spec.bytes, sha256=spec.sha256),
                )
            )
        return tuple(observed)

    def fake_metadata(
        value: object,
        *,
        profile: SupportedSourceProfile,
    ) -> ValidatedSourceMetadata:
        del value
        return ValidatedSourceMetadata(
            config_name="qasper",
            source_version=profile.source_version,
            source_license=profile.source_license,
            split_rows=profile.split_rows,
            archives=profile.archives,
        )

    def fake_archive(spec: SourceArchiveSpec, destination: Path) -> ObservedArchive:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(archive_payload)
        return ObservedArchive(
            spec=spec,
            digest=FileDigest(bytes=len(archive_payload), sha256=spec.declared_sha256),
        )

    def fake_load_splits(
        archive_paths: Mapping[str, Path],
        source_metadata: ValidatedSourceMetadata,
    ) -> dict[str, list[dict[str, object]]]:
        assert set(archive_paths) == {archive_spec.url}
        del source_metadata
        return {
            "train": [{"id": "paper-train", "title": "Train"}],
            "validation": [{"id": "paper-validation", "title": "Validation"}],
            "test": [{"id": "paper-test", "title": "Test"}],
        }

    monkeypatch.setattr(qasper, "resolve_qasper_revision", fake_resolve)
    monkeypatch.setattr(
        qasper, "_download_and_verify_repository_files", fake_repository_files
    )
    monkeypatch.setattr(qasper, "_validate_source_metadata", fake_metadata)
    monkeypatch.setattr(qasper, "_download_and_verify_archive", fake_archive)
    monkeypatch.setattr(qasper, "_load_qasper_splits", fake_load_splits)
    return profile


def test_acquire_qasper_publishes_only_validated_files_and_cleans_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    profile = _acquisition_fixture(tmp_path, monkeypatch)
    output_dir = tmp_path / "nested" / "qasper"

    result = acquire_qasper(output_dir, revision="release-candidate")

    assert result.output_dir == output_dir.resolve()
    assert result.requested_revision == "release-candidate"
    assert result.resolved_revision == "a" * 40
    assert result.split_rows == profile.split_rows
    assert sorted(path.name for path in output_dir.iterdir()) == [
        "manifest.json",
        "test.jsonl",
        "train.jsonl",
        "validation.jsonl",
    ]
    assert not list(output_dir.glob("tmp_*"))
    assert not [path for path in output_dir.iterdir() if path.is_dir()]
    assert not list(output_dir.parent.glob("tmp_qasper_*"))
    manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["output"]["aggregate_sha256"] == result.aggregate_sha256
    assert manifest["splits"][0]["rows"] == 1

    (output_dir / "stale.txt").write_text("stale", encoding="utf-8")
    replaced = acquire_qasper(output_dir, revision="release-candidate", force=True)
    assert replaced.aggregate_sha256 == result.aggregate_sha256
    assert not (output_dir / "stale.txt").exists()
    assert not list(output_dir.parent.glob("tmp_qasper_backup_*"))


def test_acquire_qasper_failure_removes_sibling_staging_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _acquisition_fixture(tmp_path, monkeypatch)
    output_dir = tmp_path / "qasper"

    def fail_load_splits(
        archive_paths: Mapping[str, Path],
        source_metadata: ValidatedSourceMetadata,
    ) -> dict[str, list[dict[str, object]]]:
        del archive_paths, source_metadata
        raise ValueError("simulated split failure")

    monkeypatch.setattr(qasper, "_load_qasper_splits", fail_load_splits)
    with pytest.raises(ValueError, match="simulated split failure"):
        acquire_qasper(output_dir)
    assert not output_dir.exists()
    assert not list(tmp_path.glob("tmp_qasper_*"))


def test_acquire_qasper_rejects_existing_output_before_external_calls(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    output_dir = tmp_path / "qasper"
    output_dir.mkdir()
    sentinel = output_dir / "sentinel.txt"
    sentinel.write_text("keep", encoding="utf-8")

    def forbidden_resolve(revision: str) -> RepositoryProvenance:
        del revision
        raise AssertionError("revision resolution must not run")

    monkeypatch.setattr(qasper, "resolve_qasper_revision", forbidden_resolve)
    with pytest.raises(FileExistsError):
        acquire_qasper(output_dir)
    assert sentinel.read_text(encoding="utf-8") == "keep"


def test_publish_staging_force_replaces_and_rolls_back_on_failure(
    tmp_path: Path,
) -> None:
    output_dir = tmp_path / "qasper"
    output_dir.mkdir()
    (output_dir / "old.txt").write_text("old", encoding="utf-8")
    staging_dir = tmp_path / "tmp_qasper_stage"
    staging_dir.mkdir()
    for name in ("train.jsonl", "validation.jsonl", "test.jsonl", "manifest.json"):
        (staging_dir / name).write_text(name, encoding="utf-8")

    _publish_staging_directory(staging_dir, output_dir, force=True)
    assert not staging_dir.exists()
    assert not (output_dir / "old.txt").exists()
    assert (output_dir / "manifest.json").read_text(encoding="utf-8") == "manifest.json"
    assert not list(tmp_path.glob("tmp_qasper_backup_*"))

    failing_stage = tmp_path / "tmp_qasper_failing_stage"
    failing_stage.mkdir()
    for name in ("train.jsonl", "validation.jsonl", "test.jsonl", "manifest.json"):
        (failing_stage / name).write_text(name, encoding="utf-8")
    previous = output_dir / "manifest.json"
    previous_hash = hashlib.sha256(previous.read_bytes()).hexdigest()
    original_rename = qasper._rename_directory

    def fail_new_publish(source: Path, destination: Path) -> None:
        if source == failing_stage:
            raise OSError("simulated publish failure")
        original_rename(source, destination)

    old_rename = qasper._rename_directory
    qasper._rename_directory = fail_new_publish
    try:
        with pytest.raises(OSError, match="simulated publish failure"):
            _publish_staging_directory(failing_stage, output_dir, force=True)
    finally:
        qasper._rename_directory = old_rename
    assert hashlib.sha256(previous.read_bytes()).hexdigest() == previous_hash
    assert failing_stage.exists()
    assert not list(tmp_path.glob("tmp_qasper_backup_*"))


def test_publish_staging_keeps_backup_when_rollback_fails(tmp_path: Path) -> None:
    output_dir = tmp_path / "qasper"
    output_dir.mkdir()
    (output_dir / "old.txt").write_text("old", encoding="utf-8")
    staging_dir = tmp_path / "tmp_qasper_stage"
    staging_dir.mkdir()
    for name in ("train.jsonl", "validation.jsonl", "test.jsonl", "manifest.json"):
        (staging_dir / name).write_text(name, encoding="utf-8")

    original_rename = qasper._rename_directory
    backup_source: list[Path] = []

    def fail_publish_and_rollback(source: Path, destination: Path) -> None:
        if source == staging_dir:
            raise OSError("simulated publish failure")
        if source.name.startswith("tmp_qasper_backup_"):
            backup_source.append(source)
            raise OSError("simulated rollback failure")
        original_rename(source, destination)

    old_rename = qasper._rename_directory
    qasper._rename_directory = fail_publish_and_rollback
    try:
        with pytest.raises(RuntimeError, match="backup remains"):
            _publish_staging_directory(staging_dir, output_dir, force=True)
    finally:
        qasper._rename_directory = old_rename
    assert backup_source and backup_source[0].exists()
    assert not output_dir.exists()
