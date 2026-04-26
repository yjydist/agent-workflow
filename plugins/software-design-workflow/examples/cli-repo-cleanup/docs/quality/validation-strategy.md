# Validation Strategy

## Primary checks

- Verify `scan` and `plan` work on fixture repositories.
- Confirm commands never mutate fixture contents.
- Confirm unsafe symlink escapes are skipped and reported.

## Evidence expectations

Implementation work should include golden output fixtures, exit-code tests, and a post-run diff showing no filesystem mutation.
