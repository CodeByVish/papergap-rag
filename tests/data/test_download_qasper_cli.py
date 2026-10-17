import subprocess
import sys
from pathlib import Path

import pytest

from scripts import download_qasper
from src.data.qasper import (
    DEFAULT_QASPER_REVISION,
    QasperAcquisitionResult,
)


def _result(output_dir: Path) -> QasperAcquisitionResult:
    return QasperAcquisitionResult(
        output_dir=output_dir.resolve(),
        requested_revision="release-candidate",
        resolved_revision="a" * 40,
        split_rows=(("train", 2), ("validation", 1), ("test", 3)),
        aggregate_sha256="b" * 64,
    )


def test_main_requires_output_dir(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as error:
        download_qasper.main([])

    assert error.value.code == 2
    captured = capsys.readouterr()
    assert "--output-dir" in captured.err
    assert "required" in captured.err


def test_main_forwards_default_arguments_and_prints_success_summary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_dir = tmp_path / "qasper"
    calls: list[tuple[Path, str, bool]] = []

    def fake_acquire(
        output_dir: Path,
        revision: str,
        force: bool,
    ) -> QasperAcquisitionResult:
        calls.append((output_dir, revision, force))
        return _result(output_dir)

    monkeypatch.setattr(download_qasper, "acquire_qasper", fake_acquire)

    exit_code = download_qasper.main(["--output-dir", str(output_dir)])

    assert exit_code == 0
    assert calls == [(output_dir, DEFAULT_QASPER_REVISION, False)]
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == (
        f"Output directory: {output_dir.resolve()}\n"
        f"Resolved revision: {'a' * 40}\n"
        "Split rows: train=2, validation=1, test=3\n"
        f"Aggregate SHA-256: {'b' * 64}\n"
    )


def test_main_forwards_explicit_revision_and_force(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    output_dir = tmp_path / "qasper"
    calls: list[tuple[Path, str, bool]] = []

    def fake_acquire(
        output_dir: Path,
        revision: str,
        force: bool,
    ) -> QasperAcquisitionResult:
        calls.append((output_dir, revision, force))
        return _result(output_dir)

    monkeypatch.setattr(download_qasper, "acquire_qasper", fake_acquire)

    assert (
        download_qasper.main(
            [
                "--output-dir",
                str(output_dir),
                "--revision",
                "release-candidate",
                "--force",
            ]
        )
        == 0
    )
    assert calls == [(output_dir, "release-candidate", True)]


def test_main_returns_one_for_existing_output_without_traceback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_dir = tmp_path / "qasper"

    def fake_acquire(
        output_dir: Path,
        revision: str,
        force: bool,
    ) -> QasperAcquisitionResult:
        del revision, force
        raise FileExistsError(f"Output directory already exists: {output_dir}")

    monkeypatch.setattr(download_qasper, "acquire_qasper", fake_acquire)

    assert download_qasper.main(["--output-dir", str(output_dir)]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == (
        f"error: Output directory already exists: {output_dir}\n"
    )
    assert "Traceback" not in captured.err


def test_main_propagates_unexpected_errors(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_acquire(
        output_dir: Path,
        revision: str,
        force: bool,
    ) -> QasperAcquisitionResult:
        del output_dir, revision, force
        raise ValueError("unsupported source metadata")

    monkeypatch.setattr(download_qasper, "acquire_qasper", fake_acquire)

    with pytest.raises(ValueError, match="unsupported source metadata"):
        download_qasper.main(["--output-dir", str(tmp_path / "qasper")])


def test_module_help_is_offline_and_executable() -> None:
    project_root = Path(__file__).resolve().parents[2]
    completed = subprocess.run(
        [sys.executable, "-m", "scripts.download_qasper", "--help"],
        cwd=project_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0
    assert completed.stderr == ""
    assert "--output-dir" in completed.stdout
    assert "--revision" in completed.stdout
    assert "--force" in completed.stdout
