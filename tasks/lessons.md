# Project Lessons

- 2026-04-15: When validating file-lane policies, avoid `str.lstrip("./")` for path normalization because it strips leading dots from valid folders like `.github`; only remove an exact `"./"` prefix.
- 2026-04-15: When bulk-downloading similarly named artifacts (e.g., tab pages), always run `ls` before extraction commands; filename separator mismatches (`-` vs `_`) can cause false missing-file errors and stall parsing.
