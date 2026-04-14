# Project Lessons

- 2026-04-15: When validating file-lane policies, avoid `str.lstrip("./")` for path normalization because it strips leading dots from valid folders like `.github`; only remove an exact `"./"` prefix.
