# git-dojo

A safe playground for practising Git and GitHub team workflows: branching, commits,
pull requests, code review, merge conflicts, rebasing, cherry-picking, branch protection
and CI.

The code (`src/dojo/todo.py`) is intentionally tiny. The point is the **workflow**, not the code.

## How to use this repo

1. Exercises live as [GitHub Issues](../../issues?q=label%3Aexercise) labelled `exercise`.
   Do them in number order.
2. Labels tell you who does what:
   - `person-a` / `person-b`: one person does it alone.
   - `pair`: both people do part of it, often clashing on purpose.
3. Read [CONTRIBUTING.md](CONTRIBUTING.md) once before you start.

**Practising alone?** Make a second clone that plays "Person B":

```powershell
git clone https://github.com/JonBoules/git-dojo.git git-dojo-b
cd git-dojo-b
git config user.name "Person B (practice)"
```

## Local setup

```powershell
git clone https://github.com/JonBoules/git-dojo.git
cd git-dojo
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python -m pytest     # pytest.exe may be blocked on managed laptops
ruff check .
```

## Cheat sheet

### Daily loop

```powershell
git switch main
git pull                                   # get latest main
git switch -c feature/12-short-name        # new branch for issue #12
# ...edit...
git status
git diff                                   # unstaged changes
git add -p                                 # stage hunk by hunk
git commit -m "feat: add priority to tasks"
git push -u origin HEAD                    # first push of the branch
gh pr create --fill                        # open a PR from the CLI
```

### Keeping your branch up to date

| Goal | Command |
|---|---|
| Merge main into my branch | `git fetch; git merge origin/main` |
| Rebase my branch onto main | `git fetch; git rebase origin/main` |
| Push after a rebase | `git push --force-with-lease` (never plain `--force`) |
| Abort a merge/rebase in progress | `git merge --abort` / `git rebase --abort` |

### Resolving conflicts

```powershell
git status                     # lists conflicted files
# edit files: keep what you want, delete <<<<<<< ======= >>>>>>> markers
git add <file>
git commit                     # if merging
git rebase --continue          # if rebasing
```

### Rewriting your own (unpushed or unshared) history

```powershell
git commit --amend                       # fix the last commit
git commit --fixup <sha>                 # mark a commit as a fix for <sha>
git rebase -i --autosquash origin/main   # squash/reword/reorder interactively
```

### Moving individual commits

```powershell
git cherry-pick -x <sha>       # copy a commit onto the current branch (-x records origin)
```

### Looking around

```powershell
git log --oneline --graph --all --decorate
git show <sha>
git blame src/dojo/todo.py
git reflog                     # your safety net: every HEAD position, even "lost" ones
```

### GitHub CLI

```powershell
gh issue list --label exercise
gh issue view 5
gh pr create --fill --base main
gh pr checkout 7               # check out someone else's PR locally
gh pr review 7 --approve
gh pr merge 7 --squash --delete-branch
gh pr checks 7
```
