#!/usr/bin/env python3
"""Check the public repository without changing source files."""

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/app-module-delivery"


def main():
    errors = []
    command = [sys.executable, "-B", str(SKILL / "scripts/verify_package.py")]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        errors.append("Skill verification failed: " + result.stdout + result.stderr)
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if version != (SKILL / "VERSION").read_text(encoding="utf-8").strip():
        errors.append("Repository and skill versions differ")
    if (ROOT / "LICENSE").read_bytes() != (SKILL / "LICENSE").read_bytes():
        errors.append("Repository and installable license differ")
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---", text, re.S)
    metadata = yaml.safe_load(front.group(1)) if front else {}
    if metadata.get("name") != "app-module-delivery" or not metadata.get("description"):
        errors.append("Invalid skill metadata")
    ui = yaml.safe_load((SKILL / "agents/openai.yaml").read_text(encoding="utf-8"))["interface"]
    if not 25 <= len(ui["short_description"]) <= 64:
        errors.append("UI description length is invalid")
    if "$app-module-delivery" not in ui["default_prompt"]:
        errors.append("UI prompt does not identify the skill")

    count = 0
    links = 0
    svg_count = 0
    han = re.compile(r"[\u3400-\u9fff]")
    private = re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/|/var/folde[r]s/|/Library/Develope[r]/")
    credential = re.compile(r"gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----")
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if any(part in {".git", "dist", "__pycache__", ".venv"} for part in rel.parts):
            continue
        if not path.is_file():
            continue
        count += 1
        if path.suffix not in {".md", ".py", ".json", ".yml", ".yaml", ".svg", ".txt"} and path.name not in {"LICENSE", "VERSION"}:
            continue
        body = path.read_text(encoding="utf-8")
        if han.search(body):
            errors.append("Non-English public text: " + rel.as_posix())
        if private.search(body):
            errors.append("Private local path: " + rel.as_posix())
        if credential.search(body):
            errors.append("Credential pattern: " + rel.as_posix())
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", body):
                target = target.split(' "', 1)[0]
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                destination = (path.parent / target.split("#", 1)[0]).resolve()
                links += 1
                if destination != ROOT and ROOT not in destination.parents:
                    errors.append("Reference escapes repository: " + target)
                elif not destination.exists():
                    errors.append("Broken reference: " + rel.as_posix() + ": " + target)
        if path.suffix == ".svg":
            tree = ET.fromstring(body)
            ns = {"s": "http://www.w3.org/2000/svg"}
            if tree.find("s:title", ns) is None or tree.find("s:desc", ns) is None:
                errors.append("SVG lacks accessible text: " + rel.as_posix())
            if tree.findall(".//s:script", ns):
                errors.append("SVG contains scripts: " + rel.as_posix())
            svg_count += 1
    print(json.dumps({"status": "FAIL" if errors else "PASS", "version": version,
                     "files_checked": count, "local_references": links,
                     "svg_documents": svg_count, "errors": errors,
                     "scope": "repository and package properties, not application runtime"}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
