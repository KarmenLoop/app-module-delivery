# Verification and evidence boundaries

The [validation record](../skills/app-module-delivery/VALIDATION.md) describes actual checks. CI runs package/tool checks on Linux, macOS, and Windows; it does not run the seven agent clients.

## Commands

Use Python 3.9 or later:

~~~sh
python -m pip install -r requirements-dev.txt
python -B scripts/check_repository.py
python -B skills/app-module-delivery/validation/test_verifier.py
python -B scripts/package_skill.py --output-dir dist
~~~

The repository check validates the skill manifest, YAML, English text, local links, SVG structure, version/license consistency, and known private-path or credential patterns. This bounded check is not a security audit.

Verifier regressions cover valid structure/inventory/ZIP, relocation, missing resources, broken links, unclosed fences, duplicate IDs, changed content, malformed or missing manifests, changed archive bytes, and unsafe members.

The builder validates source, normalizes ZIP metadata, compares archive bytes, checks CRC, and emits checksums and a receipt.

## Interpret scope

Package checks prove tested package properties. Agent behavior requires actual decisions and outputs. Native host acceptance requires loading and operation in that product/version. Application acceptance requires real business, permission, data, target, performance, and recovery results.

Missing required evidence keeps acceptance incomplete. Unit checks, mocks, screenshots, builds, sandboxes, devices, independent review, and publication retain separate scope.

## Historical failure

The original verifier failed to return structured output for an invalid top-level manifest. The corrected implementation validates manifest shape. A path-redacted historical receipt is retained as tool history.

## Maintainer builds

After an authorized change, update version and evidence, then intentionally refresh inventory:

~~~sh
python -B scripts/package_skill.py --refresh-manifest --output-dir dist
~~~

Ordinary verification is read-only. Inventory regeneration should not conceal unexplained changes.
