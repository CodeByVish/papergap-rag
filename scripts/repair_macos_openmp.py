"""Opt-in repair for duplicate FAISS/PyTorch OpenMP runtimes on macOS ARM64.

Run with the affected environment's Python. Inspect the plan first; --apply
backs up FAISS's runtime and links to PyTorch's existing runtime. --restore
reinstates the backup. No global library or other environment is modified.
"""

import argparse
import importlib.metadata
import platform
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--restore", action="store_true")
    args = parser.parse_args()
    if platform.system() != "Darwin" or platform.machine() != "arm64":
        parser.error("This repair applies only to macOS ARM64")
    try:
        faiss = importlib.metadata.distribution("faiss-cpu")
        torch = importlib.metadata.distribution("torch")
        source = Path(faiss.locate_file("faiss/.dylibs/libomp.dylib"))
        target = Path(torch.locate_file("torch/lib/libomp.dylib")).resolve()
        backup = (
            Path(__file__).resolve().parents[1]
            / ".cache/environment-backups"
            / f"faiss-{faiss.version}-libomp.dylib"
        )
        if not source.is_file() or not target.is_file():
            raise ValueError("Expected bundled runtime paths were not found")
        print(f"FAISS runtime: {source}\nShared runtime: {target}\nBackup: {backup}")
        if args.restore:
            if not backup.is_file():
                raise ValueError("No backup exists; nothing to restore")
            if not source.is_symlink() or source.resolve() != target:
                raise ValueError("FAISS runtime has changed; refusing to replace it")
            source.unlink()
            shutil.copy2(backup, source)
            print("Restored original FAISS runtime.")
        elif args.apply:
            if source.resolve() == target:
                print("Already using one runtime; no change needed.")
                return
            if source.is_symlink():
                raise ValueError(
                    "Unexpected FAISS symlink; inspect it before changing it"
                )
            if backup.exists() and source.read_bytes() != backup.read_bytes():
                raise ValueError("Existing backup differs; refusing to overwrite it")
            backup.parent.mkdir(parents=True, exist_ok=True)
            if not backup.exists():
                shutil.copy2(source, backup)
            source.unlink()
            source.symlink_to(target)
            print(
                "Linked FAISS to PyTorch's runtime. Run the full tests and model smoke check."
            )
        else:
            print("Plan only. Pass --apply to repair, or --restore to undo it.")
    except (OSError, ValueError, importlib.metadata.PackageNotFoundError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
