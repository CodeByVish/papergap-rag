"""Unify Torch/FAISS OpenMP inside the dedicated macOS virtual environment.

Both bundled libraries advertise ABI compatibility 5. The original FAISS copy
is preserved beside the symlink; no system or other virtualenv files are edited.
Run once after installing requirements-p6-local.txt on Apple Silicon.
"""

import hashlib
import json
import os
import platform
import sys
import sysconfig
from pathlib import Path


def main():
    if sys.platform != "darwin" or platform.machine() != "arm64":
        print("No macOS Apple Silicon OpenMP repair needed.")
        return
    if sys.prefix == sys.base_prefix or Path(sys.prefix).name != ".venv-p6":
        raise RuntimeError("Run this only with .venv-p6/bin/python")
    packages = Path(sysconfig.get_paths()["purelib"])
    faiss = packages / "faiss/.dylibs/libomp.dylib"
    torch = packages / "torch/lib/libomp.dylib"
    if not faiss.exists() or not torch.is_file():
        raise RuntimeError("Install Torch and faiss-cpu in .venv-p6 first")
    if faiss.resolve() == torch.resolve():
        print("Torch and FAISS already share the same OpenMP runtime.")
        return
    original = faiss.read_bytes()
    backup = faiss.with_name(
        "libomp.original-" + hashlib.sha256(original).hexdigest()[:12] + ".dylib"
    )
    if backup.exists():
        if backup.read_bytes() != original:
            raise RuntimeError("Unexpected OpenMP backup; inspect before changing it")
        faiss.unlink()
    else:
        faiss.rename(backup)
    faiss.symlink_to(os.path.relpath(torch, faiss.parent))
    evidence = (
        Path(__file__).resolve().parents[1] / "results/p6-local/native-runtime.json"
    )
    evidence.parent.mkdir(parents=True, exist_ok=True)
    evidence.write_text(
        json.dumps(
            {
                "faiss_library": str(faiss),
                "shared_library": str(torch),
                "original_backup": str(backup),
                "shared_sha256": hashlib.sha256(torch.read_bytes()).hexdigest(),
            },
            indent=2,
        )
        + "\n"
    )
    print("FAISS now shares Torch OpenMP; original library preserved:", backup)


if __name__ == "__main__":
    main()
