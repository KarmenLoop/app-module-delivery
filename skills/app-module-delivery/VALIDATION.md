# Validation record

Version 1.0.1, English public edition. Release date: October 22, 2026.

## Executed checks

The following checks passed on macOS for the English public edition:

| Check | Actual result | Evidence |
| --- | --- | --- |
| Skill authoring metadata | Official skill-creator validator exited 0: `Skill is valid!` | [Authoring record](validation/authoring-checks.json) |
| Verifier regressions | 14 tests, 0 failures, 0 errors; process exited 0 | [Regression record](validation/verifier-tests-final.json) |
| Package structure and references | Required resources, Markdown references, ordered Q01-Q72; exited 0 | Release package receipt and reproducible verifier |
| Manifest and archive | Exact inventory, byte counts, SHA-256, ZIP members/content and CRC; exited 0 | Release `package-receipt.json` and `SHA256SUMS` |
| Public repository | English text, local references, SVG structure, version/license consistency, bounded private-path and credential checks; exited 0 | `scripts/check_repository.py` |

The public regression receipt redacts machine-specific paths and retains actual outcomes and verifier output. Its counts describe isolated test copies before final publication evidence was added. The final release receipt describes the released archive. No checksum is embedded into a file that it would need to hash recursively.

## Reproduce

From the repository root, install `requirements-dev.txt`, then run:

~~~sh
python -B scripts/check_repository.py
python -B skills/app-module-delivery/validation/test_verifier.py
python -B scripts/package_skill.py --output-dir dist
~~~

From an extracted installable skill, run `python -B scripts/verify_package.py`. CI repeats the repository, regression, and package checks on Linux, macOS, and Windows; inspect the actual run conclusion rather than assuming success from this document.

## Limits and preserved history

The original Chinese 1.0.0 package remains separate and unchanged. Its verifier's initial malformed-manifest failure is preserved in [the historical receipt](validation/verifier-tests-first.json), with local paths redacted. This is historical tool evidence, not an application failure; the corrected malformed-manifest regression passes.

Native loading in all seven hosts, E01-E12 agent trials, actual application/device/performance/recovery tests, and independent acceptance remain NOT_RUN. Package integrity and passing tool checks do not establish those results. The [self-review](validation/SELF_REVIEW.md) is a document review, not independent behavioral acceptance.
