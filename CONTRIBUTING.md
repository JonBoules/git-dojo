# Contributing

## Branches

- `main` is protected. Every change goes through a pull request.
- Branch names: `<type>/<issue-number>-<short-description>`
  - `feature/5-checkbox-format`
  - `fix/9-complete-task-index`
  - `chore/4-coverage`
- One branch per issue. Delete the branch after merging (GitHub does this automatically).

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <short summary in imperative mood>

Optional body explaining *why*, wrapped at ~72 chars.
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`.

Good: `feat: add priority field to Task`
Bad: `stuff`, `wip`, `fixed it`, `asdf`

Keep commits small and focused. Each one should leave the tests passing.

## Pull requests

- Fill in the PR template. Put `Closes #<issue>` in the description so the issue closes when the PR merges.
- CI (`ruff check` + `pytest`) must be green.
- At least one approving review is required.
- Reviewers: comment on *what* and *why*. Use GitHub's "suggestion" blocks for small fixes.
- Authors: reply to every comment, then resolve the conversation. Don't force-push during review
  unless you've told the reviewer.

## Merge strategy

All three are enabled so you can practise them (exercise 08). Default: **squash merge** for
feature branches.
