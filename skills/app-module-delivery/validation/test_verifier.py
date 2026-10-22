#!/usr/bin/env python3
"""Exercise package verification in temporary copies; never edit the source."""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1]
RECORDS = []


def write_manifest(root):
    entries = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != "MANIFEST.json":
            data = path.read_bytes()
            entries.append({"path": path.relative_to(root).as_posix(),
                            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    manifest = {"name": "app-module-delivery",
                "version": (root / "VERSION").read_text().strip(), "files": entries}
    (root / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def write_zip(root, archive, altered=None, extra=None):
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as package:
        for path in sorted(root.rglob("*")):
            if path.is_file():
                name = root.name + "/" + path.relative_to(root).as_posix()
                data = path.read_bytes()
                if altered and path.relative_to(root).as_posix() == altered:
                    data = bytes([data[0] ^ 1]) + data[1:]
                package.writestr(name, data)
        if extra:
            package.writestr(extra, b"unexpected member")


class VerifierTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="app-module-verifier-test-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / "app-module-delivery"
        shutil.copytree(SOURCE, self.root)
        write_manifest(self.root)

    def check_result(self, expected, args=(), root=None):
        selected = root or self.root
        command = [sys.executable, "-B", str(selected / "scripts/verify_package.py"), *args]
        result = subprocess.run(command, cwd=self.base, capture_output=True, text=True)
        RECORDS.append({"case": self.id().split(".")[-1], "argv": command,
                        "cwd": str(self.base), "exit_code": result.returncode,
                        "stdout": result.stdout, "stderr": result.stderr})
        self.assertEqual(result.returncode, 0 if expected == "PASS" else 1, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data["status"], expected)
        self.assertEqual(bool(data.get("errors")), expected == "FAIL")
        return data

    def test_valid_structure(self):
        data = self.check_result("PASS", ["--structure-only"])
        self.assertEqual(data["counts"]["questions"], 72)

    def test_valid_manifest(self):
        self.check_result("PASS")

    def test_valid_archive(self):
        archive = self.base / "release.zip"
        write_zip(self.root, archive)
        self.check_result("PASS", ["--archive", str(archive)])

    def test_relocated_archive(self):
        archive = self.base / "release.zip"
        write_zip(self.root, archive)
        destination = self.base / "relocated"
        destination.mkdir()
        with zipfile.ZipFile(archive) as package:
            package.extractall(destination)
        self.check_result("PASS", ["--archive", str(archive)],
                          root=destination / "app-module-delivery")

    def test_missing_required_resource(self):
        (self.root / "templates/module-design.md").unlink()
        self.check_result("FAIL", ["--structure-only"])

    def test_broken_relative_link(self):
        with (self.root / "README.md").open("a") as output:
            output.write("\n[Missing resource](missing-reference.md)\n")
        self.check_result("FAIL", ["--structure-only"])

    def test_unclosed_fence(self):
        with (self.root / "README.md").open("a") as output:
            output.write("\n~~~text\nunclosed example\n")
        self.check_result("FAIL", ["--structure-only"])

    def test_duplicate_question(self):
        with (self.root / "references/discovery.md").open("a") as output:
            output.write("\n73. Q72 Duplicate candidate\n")
        self.check_result("FAIL", ["--structure-only"])

    def test_manifest_content_drift(self):
        with (self.root / "VERSION").open("a") as output:
            output.write("changed\n")
        self.check_result("FAIL")

    def test_invalid_manifest_shape(self):
        (self.root / "MANIFEST.json").write_text("[]\n")
        self.check_result("FAIL")

    def test_missing_manifest(self):
        (self.root / "MANIFEST.json").unlink()
        self.check_result("FAIL")

    def test_invalid_manifest_entries(self):
        invalid = {"name": "app-module-delivery",
                   "version": (self.root / "VERSION").read_text(encoding="utf-8").strip(),
                   "files": [None]}
        (self.root / "MANIFEST.json").write_text(json.dumps(invalid), encoding="utf-8")
        self.check_result("FAIL")

    def test_archive_content_drift(self):
        archive = self.base / "release.zip"
        write_zip(self.root, archive, altered="SKILL.md")
        self.check_result("FAIL", ["--archive", str(archive)])

    def test_unsafe_archive_member(self):
        archive = self.base / "release.zip"
        write_zip(self.root, archive, extra="../outside.txt")
        self.check_result("FAIL", ["--archive", str(archive)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(VerifierTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if args.report:
        args.report.write_text(json.dumps({
            "scope": "package verifier behavior in isolated temporary copies",
            "status": "PASS" if result.wasSuccessful() else "FAIL",
            "tests_run": result.testsRun,
            "failures": len(result.failures),
            "errors": len(result.errors),
            "records": RECORDS,
            "excluded_scope": "agent decisions, platform loading, application behavior",
        }, ensure_ascii=False, indent=2) + "\n")
    sys.exit(0 if result.wasSuccessful() else 1)
