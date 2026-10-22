#!/usr/bin/env python3
"""Build and verify the installable skill archive."""

import argparse
import hashlib
import io
import json
import stat
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/app-module-delivery"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_lf(path, text):
    with path.open("w", encoding="utf-8", newline="\n") as output:
        output.write(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--refresh-manifest", action="store_true")
    args = parser.parse_args()
    version = (SKILL / "VERSION").read_text(encoding="utf-8").strip()
    if args.refresh_manifest:
        files = []
        for path in sorted(SKILL.rglob("*")):
            if path.is_symlink():
                raise ValueError("Unexpected symlink")
            if path.is_file() and path.name != "MANIFEST.json":
                data = path.read_bytes()
                files.append({"path": path.relative_to(SKILL).as_posix(),
                              "bytes": len(data), "sha256": sha(data)})
        manifest = {"format_version": 1, "name": "app-module-delivery", "version": version, "files": files}
        write_lf(SKILL / "MANIFEST.json", json.dumps(manifest, indent=2) + "\n")
    check = subprocess.run([sys.executable, "-B", str(SKILL / "scripts/verify_package.py")],
                           capture_output=True, text=True)
    if check.returncode:
        print(check.stdout + check.stderr)
        return check.returncode
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive = args.output_dir / ("app-module-delivery-v" + version + ".zip")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                item = zipfile.ZipInfo(SKILL.name + "/" + path.relative_to(SKILL).as_posix(),
                                       (2026, 10, 22, 0, 0, 0))
                item.compress_type = zipfile.ZIP_DEFLATED
                item.create_system = 3
                item.external_attr = (stat.S_IFREG | 0o644) << 16
                package.writestr(item, path.read_bytes())
    data = buffer.getvalue()
    if archive.exists() and archive.read_bytes() != data:
        raise ValueError("A different artifact already exists at the destination")
    archive.write_bytes(data)
    result = subprocess.run([sys.executable, "-B", str(SKILL / "scripts/verify_package.py"),
                             "--archive", str(archive.resolve())], capture_output=True, text=True)
    if result.returncode:
        print(result.stdout + result.stderr)
        return result.returncode
    digest = sha(data)
    write_lf(args.output_dir / "SHA256SUMS", digest + "  " + archive.name + "\n")
    receipt = {"name": "app-module-delivery", "version": version, "file": archive.name,
               "bytes": len(data), "sha256": digest,
               "manifest_sha256": sha((SKILL / "MANIFEST.json").read_bytes()),
               "verification": json.loads(result.stdout),
               "excluded_scope": "agent behavior, native client loading, application runtime"}
    write_lf(args.output_dir / "package-receipt.json", json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
