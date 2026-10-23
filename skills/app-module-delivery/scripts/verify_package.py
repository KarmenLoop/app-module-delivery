#!/usr/bin/env python3
"""Read-only structural, manifest, and ZIP verification for this skill."""

import argparse
import hashlib
import json
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


REQUIRED = [
    "SKILL.md", "VERSION", "README.md", "VALIDATION.md", "agents/openai.yaml",
    "references/discovery.md", "references/architecture.md",
    "references/ui-ux.md", "references/development.md",
    "references/testing.md", "references/delivery-recovery.md",
    "references/platforms.md", "references/behavior-evals.md",
    "templates/application-plan.md", "templates/architecture.md",
    "templates/module-design.md", "templates/interaction-contract.md",
    "templates/acceptance.md", "templates/progress.md",
    "scripts/verify_package.py",
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def verify(root, archive=None, structure_only=False):
    root = root.resolve()
    errors = []
    counts = {"files": 0, "markdown_files": 0, "relative_links": 0,
              "questions": 0, "manifest_entries": 0, "archive_members": 0}
    if not root.is_dir():
        return {"status": "FAIL", "errors": ["Skill directory does not exist"]}

    files = {}
    for path in sorted(root.rglob("*")):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append("Symlink is not portable: " + rel)
        elif path.is_file():
            files[rel] = path
    counts["files"] = len(files)
    for rel in REQUIRED:
        if rel not in files:
            errors.append("Missing required file: " + rel)

    skill = files.get("SKILL.md")
    if skill:
        text = skill.read_text(encoding="utf-8")
        front = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not front:
            errors.append("Missing SKILL.md frontmatter")
        else:
            if not re.search(r"^name: app-module-delivery$", front.group(1), re.M):
                errors.append("Unexpected skill name")
            if not re.search(r"^description: .+", front.group(1), re.M):
                errors.append("Missing description")
        if re.search(r"^\[TODO:[^\n]*\]$", text, re.M):
            errors.append("Unfinished skill scaffold")

    # Check authored Markdown resources. Fenced example content is not a link.
    link_pattern = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
    fence_pattern = re.compile(r"^\s*([~\x60]{3,})(.*)$")
    for rel, path in files.items():
        if path.suffix != ".md":
            continue
        counts["markdown_files"] += 1
        fence = None
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = fence_pattern.match(line)
            if match and len(set(match.group(1))) == 1:
                marker = match.group(1)
                if fence is None:
                    fence = (marker[0], len(marker))
                elif marker[0] == fence[0] and len(marker) >= fence[1] and not match.group(2).strip():
                    fence = None
                continue
            if fence:
                continue
            for found in link_pattern.finditer(line):
                target = found.group(1).strip()
                target = target.split(' "', 1)[0]
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                parts = urlsplit(target)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                counts["relative_links"] += 1
                decoded = unquote(parts.path)
                if Path(decoded).is_absolute() or "\\" in decoded:
                    errors.append(f"Nonportable link: {rel}:{number}: {target}")
                    continue
                destination = (path.parent / decoded).resolve()
                if destination != root and root not in destination.parents:
                    errors.append(f"Link escapes package: {rel}:{number}: {target}")
                elif not destination.exists():
                    errors.append(f"Broken link: {rel}:{number}: {target}")
        if fence:
            errors.append("Unclosed Markdown fence: " + rel)

    discovery = files.get("references/discovery.md")
    if discovery:
        questions = re.findall(r"^\d+\.\s+(Q\d{2})\b", discovery.read_text(encoding="utf-8"), re.M)
        counts["questions"] = len(questions)
        if questions != [f"Q{i:02d}" for i in range(1, 73)]:
            errors.append("Question inventory must contain ordered, unique Q01-Q72")

    if not structure_only:
        manifest_path = files.get("MANIFEST.json")
        if not manifest_path:
            errors.append("Missing MANIFEST.json")
        else:
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                if not isinstance(manifest, dict):
                    raise ValueError("Manifest must be a JSON object")
                if manifest.get("name") != "app-module-delivery":
                    errors.append("Manifest name mismatch")
                if manifest.get("version") != (root / "VERSION").read_text().strip():
                    errors.append("Manifest version mismatch")
                entries = manifest["files"]
                if not isinstance(entries, list) or any(not isinstance(entry, dict) for entry in entries):
                    raise ValueError("Manifest files must be a list of objects")
                names = [entry["path"] for entry in entries]
                counts["manifest_entries"] = len(entries)
                if len(names) != len(set(names)):
                    errors.append("Duplicate manifest entries")
                expected = set(files) - {"MANIFEST.json"}
                if set(names) != expected:
                    errors.append("Manifest file inventory mismatch")
                for entry in entries:
                    path = files.get(entry["path"])
                    if path is None:
                        continue
                    data = path.read_bytes()
                    if len(data) != entry["bytes"] or digest(data) != entry["sha256"]:
                        errors.append("Manifest content mismatch: " + entry["path"])
            except (ValueError, KeyError, TypeError, OSError) as exc:
                errors.append("Invalid manifest: " + str(exc))

    if archive is not None:
        try:
            expected = {root.name + "/" + rel: path for rel, path in files.items()}
            with zipfile.ZipFile(archive) as package:
                info = package.infolist()
                names = [entry.filename for entry in info]
                counts["archive_members"] = len(info)
                safe = True
                for entry in info:
                    name = entry.filename
                    member = PurePosixPath(name)
                    if (member.is_absolute() or ".." in member.parts or "\\" in name
                            or stat.S_ISLNK(entry.external_attr >> 16)):
                        errors.append("Unsafe archive member: " + name)
                        safe = False
                if len(names) != len(set(names)) or set(names) != set(expected):
                    errors.append("Archive file inventory mismatch")
                    safe = False
                if safe:
                    for entry in info:
                        data = expected[entry.filename].read_bytes()
                        if entry.file_size != len(data):
                            errors.append("Archive size mismatch: " + entry.filename)
                        elif package.read(entry.filename) != data:
                            errors.append("Archive content mismatch: " + entry.filename)
                    bad = package.testzip()
                    if bad:
                        errors.append("Archive CRC failure: " + bad)
        except (OSError, ValueError, zipfile.BadZipFile, RuntimeError) as exc:
            errors.append("Archive read failure: " + str(exc))

    return {
        "status": "FAIL" if errors else "PASS",
        "scope": "package structure" if structure_only else "package structure and manifest",
        "archive_checked": archive is not None,
        "counts": counts,
        "errors": errors,
        "excluded_scope": "agent behavior, platform loading, and application runtime",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--structure-only", action="store_true",
                        help="Authoring check before the release manifest is generated")
    args = parser.parse_args()
    if args.structure_only and args.archive:
        parser.error("--archive requires a manifest check")
    try:
        result = verify(args.root, args.archive, args.structure_only)
    except (OSError, UnicodeError, ValueError) as exc:
        result = {"status": "FAIL", "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
