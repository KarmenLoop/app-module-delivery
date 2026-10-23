# App Module Delivery v1.1.0 host tutorial

The adapter is included under `scripts/host.py` in this skill.

1. Download and extract the versioned skill ZIP. Use Python 3.11+. Keep its files intact under the published license. In the repository, the script below is at `skills/app-module-delivery/scripts/host.py`; in the ZIP it is `app-module-delivery/scripts/host.py`.
2. In the application workspace, create `.app-delivery-checks.json` with the commands the owner authorizes. Each named entry needs an exact `argv` array; optional fields are `cwd`, `timeout_seconds` (1–60), `expected_exit`, and workspace-relative `artifacts` and `inputs`. List the source/configuration files whose changes should invalidate the result in `inputs`. Only those declared inputs and artifacts are checked for later drift. Use a meaningful application check that writes a real result, not an echo standing in for a feature.
3. Install the adapter in each host workspace. Substitute the actual script, private storage, and workspace paths:

```sh
python /path/to/host.py --root /private/app-acceptance --workspace /path/to/application --install-host codex install
python /path/to/host.py --root /private/app-acceptance --workspace /path/to/application --install-host cursor install
```

4. Reload, approve this specific server, and verify `app_init`, `app_run_check`, `app_status`, and `app_export` are listed. Use `app_init` to map requirement IDs/titles to registered `check_id` values and set a project ID and goal.
5. Read the current revision. Call `app_run_check` with the project, check ID, and `expected_revision`. Inspect the real exit, logs, artifact hashes, and requirement results. Repair the application after a failure and run the same approved check again using the new revision. The adapter does not repair applications itself.
6. `app_status` rechecks hashes. Changed/missing evidence becomes `STALE`; changing registered commands requires a newly reviewed plan. Export the current acceptance record with `app_export`.

The same tools can be called without an agent: `python /path/to/host.py --root /private/app-acceptance --workspace /path/to/application call app_status --input request.json`, where the JSON contains `project_id`.

If a host exits during a running check, wait for that check's bounded timeout and read `app_status` again. A separate owned runner writes a durable terminal receipt; a new host reconciles it once. If the runner or computer itself is killed before a receipt is written, the state remains running/unknown and blocks a duplicate run. Inspect the saved run manually; no missing receipt is treated as a pass. Check output is limited to 8 MiB per log with polling enforcement.

This adapter is a local acceptance ledger and registered-command runner. It does not create device evidence, a schedule, or execution permission beyond the registered checks. Codex live reading and local subprocess execution were accepted on macOS; Cursor protocol discovery passed, while its model conversation and native Windows/Linux use remain outstanding.
