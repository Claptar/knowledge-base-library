---
title: "13. Using Git for Collaboration"
course: "Berkeley Stat 243 Fall 2024"
chapter: 13
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. Using Git for Collaboration

## What this covers

This section assumes the `git add` / `git commit` / `git push` workflow from the first meeting of
the course and asks the next question: how do you work with a repository's history, and how do two
or more people work on the *same* repository without overwriting each other? It covers reading a
repository's history, undoing a mistake at three different depths (`checkout`, `revert`, `reset`),
creating and merging branches, resolving the conflicts that a shared repository eventually produces,
and a handful of everyday commands (`git status`, `git diff --cached`, `git commit -a`,
`git commit --amend`) that make the day-to-day cycle less error-prone.

## Git tracks content, not files

Many revision-control systems give you an `add` command that means "start tracking this file."
Git's `add` does something more general: it is used for both brand-new files and files you have
just edited, and in either case what it does is the same — it takes a snapshot of the given files
and stages that content in the *index*, ready to go into the next commit. The index is a staging
area, not a log of which files exist; that is why `git add` is the command you reach for both the
first time you track a file and every time afterwards.

## Reading the project's history

At any point you can look back over the commits that produced the current state of the repository.
The manual page for any command is available locally, e.g. `man git-log` or `git help log`.

```bash
git log                                        # the commit history
git log -p                                     # ... with the full diff at each step
git log --stat --summary                       # ... with just a summary of what changed
git log --oneline --decorate --graph --all     # a compact graph across all branches
```

The last of these is the one worth keeping at hand once branches are in play: it draws the actual
shape of the history, rather than a flat list, which is what you need once two branches have
diverged and been merged back together.

## Undoing a mistake: checkout, revert, reset

Git gives you three different tools for undoing something, and they undo different amounts of
damage in different ways. Knowing which one you want *before* you run it matters, because `reset
--hard` genuinely discards work.

### `checkout`: look at, without changing, the past

`git checkout` moves you to a previous commit (it is also how you switch branches, below).

```bash
git checkout HEAD~1          # move back 1 commit
git checkout HEAD~2          # move back 2 commits
git checkout <commit-hash>   # move to a specific commit
```

Commit hashes come from `git log`, from `git reflog`, or from GitHub's own history view. Once you
have looked around, return to the branch tip with:

```bash
git checkout master   # or whatever branch you were on
```

### `revert`: undo a commit by adding a new one

`git revert` is for when you want to undo the *changes* a past commit made, without erasing the
fact that it happened. It does this by creating a new commit whose diff is the inverse of the one
you're reverting — so the history keeps growing forward, it just grows the mistake back out again.

```bash
git revert HEAD~1
git revert HEAD~2
git revert <commit-hash>
```

This is the safe option for anything that has already been pushed and that other people may have
built on: nobody's history gets rewritten, a new commit just cancels the old one.

### `reset`: move the branch tip itself

If you committed something you shouldn't have, or want the repository to look exactly as it did at
an earlier point, `git reset` moves the tip of your branch back to a specified commit.

```bash
git reset --soft HEAD~1   # undo the commit, keep the file changes
git reset --hard HEAD~1   # undo the commit and discard the file changes
```

The `--soft` flag undoes only the *commit* — your edits are still sitting there, staged, ready to be
recommitted differently. `--hard` throws the file changes away as well, back to how things looked
at the target commit. Unlike `revert`, `reset` rewrites where the branch pointer is, which is why it
is the right tool for cleaning up local, not-yet-shared history, and the wrong one for undoing
something everyone else has already pulled.

For a mistake that is more structural — for instance, a large file that got committed and pushed by
accident and now needs to be gone from the *history*, not just the tip — the tool is
`filter-branch`:

```bash
git filter-branch --index-filter \
  'git rm -r --cached --ignore-unmatch <PATH/TO/FILE>' HEAD
```

This rewrites every commit that touched the file, which is a heavier operation than any of the
three above: it changes history that other collaborators may already have.

## Managing branches

A single repository can hold several parallel lines of development. Create one with:

```bash
git branch experimental
```

`git branch` on its own lists the branches you have; an asterisk marks the one you're currently on.
The `master` branch is the one Git creates automatically; `experimental` is the one you just made.
Switch to it with:

```bash
git checkout experimental
```

Now edit a file and commit on this branch as usual:

```bash
git add file
git commit -m "edited file"
```

If instead you want to set changes aside without committing them — to switch branches cleanly, or
to come back to the edit later — `git stash` saves the working-tree changes and reverts the tree to
the last commit, so you can keep working with a clean tree. `git stash pop` brings the stashed
changes back and removes them from the stash; `git stash apply` brings them back but leaves a copy
in the stash, which is useful if you want to apply the same stashed change to more than one branch.

Switching back:

```bash
git checkout master
```

The edit made on `experimental` is no longer visible — it lives only on that branch. If you now make
a *different* change on `master` and commit it, the two branches have diverged: each has a commit
the other doesn't.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="master and experimental branches diverging from a common commit and merging back together">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="70" x2="310" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="15" y="74" font-size="12" fill="currentColor">master</text>

  <line x1="120" y1="70" x2="220" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <line x1="220" y1="140" x2="280" y2="140" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="230" y="160" font-size="12" fill="currentColor">experimental</text>

  <line x1="280" y1="140" x2="310" y2="70" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>

  <circle cx="120" cy="70" r="4" fill="currentColor"/>
  <text x="112" y="55" font-size="11" fill="currentColor">branch</text>

  <circle cx="220" cy="140" r="4" fill="currentColor"/>
  <text x="200" y="128" font-size="11" fill="currentColor">commit</text>

  <circle cx="240" cy="70" r="4" fill="currentColor"/>
  <text x="228" y="55" font-size="11" fill="currentColor">commit</text>

  <circle cx="310" cy="70" r="4" fill="currentColor"/>
  <text x="290" y="55" font-size="11" fill="currentColor">merge</text>
</svg>
<figcaption>master and experimental each pick up their own commits after the branch point; git merge experimental brings experimental's changes back into master at a merge commit.</figcaption>
</figure>

To bring `experimental`'s work into `master`:

```bash
git merge experimental
```

If the two branches touched different things, the merge succeeds and you add, commit, and push as
usual. If they touched the *same* lines, Git leaves conflict markers in the affected files instead
of guessing; `git diff` will show you where. Once you have edited the files to resolve the
conflict:

```bash
git commit -a
```

records the merge. With the work safely in `master`, the branch itself can be deleted:

```bash
git branch -d experimental       # refuses unless experimental is already merged in
git branch -D experimental       # deletes it regardless, discarding any unmerged work
git push -d origin experimental  # remove the branch from the remote as well
```

`-d` is the safe form — it checks that everything on the branch is already reachable from where
you're standing before it deletes anything; `-D` does not check and will happily drop unmerged
commits.

### Pull requests

In a collaborative repository, merging straight into `master` is usually not the right move —
instead you open a *pull request*, which shows the maintainers the diff between your branch and
`master`, lets them comment, and gives everyone a chance to catch problems before the branch is
merged in. This is the normal way branches get merged in industry software development, and it is
worth the same practice as merging on the command line.

## A few more everyday commands

**Staging and committing.** With several modified files, `git add file1 file2 file3` stages them;
`git diff --cached` then shows exactly what is about to be committed (plain `git diff`, without
`--cached`, shows changes you've made but haven't staged yet), and `git status` gives a quick
overview of what's staged, unstaged, and untracked. If you only ever want to commit files Git
already knows about, `git commit -a` skips the separate `add` step and stages every modified
(but not new) file automatically as part of the commit.

**Amending a commit.** If you commit and then realise you forgot a file:

```bash
git add file1
git commit -m "adding file1"

# realise file2 should have been in that commit too
git add file2
git commit --amend -m "adding second file"
```

`--amend` folds the new staged changes into the previous commit and lets you update its message,
rather than leaving a second, separate commit that only exists to patch the first.

**Importing an existing project.** Turning a folder of existing work (say, unpacked from a tarball)
into a Git repository is a normal `git init` followed by staging everything and committing:

```bash
tar xzf project.tar.gz
cd project
git init
git add .
git commit -m "add"
```

The awkward part of this route is connecting the result to a remote afterwards. It is usually
easier to go the other way: create the (empty) repository on GitHub first, clone it locally, and
then add your files to that clone — the remote is already wired up and there is nothing to link
after the fact.

## Exercises

These are done as a partner exercise — split into pairs (a three works if numbers don't divide
evenly) and work through them together on a shared repository.

1. Create a new GitHub repository (only one partner needs to do this).
2. Add your partner as a collaborator, via the repository's Settings, then Collaborators.
3. Each partner creates their own branch (give the branches different names), adds a file or two to
   it, and merges it into `master` — either on the command line or via a pull request. If you merge
   on the command line, run `git pull` before pushing, to avoid a conflict with the remote.
4. Deliberately create a race between the two of you:
   - one partner pushes a new commit to the remote repository;
   - the other partner, without pulling first, tries to add, commit, and push their own changes,
     and observes what happens;
   - resolve the resulting conflict, either by pulling and merging, or by using `git reset --soft`
     as described above.
5. Have both partners (or the same partner from two computers) edit the *same* file and see what
   happens when those changes meet.

## Sources

- Berkeley STAT 243 (Fall 2021), Section 10, "To Do in Section: Using Git For Collaboration" and
  its three linked parts — `moreOnGit.Rmd`, converted to markdown at
  `stat243-fall-2021/sections/10/moreOnGit/01-to-do-in-section-using-git-for-collaboration.md`
  through `04-appendix-more-useful-git-functionality.md`. No slide deck or transcript accompanies
  this material; it is discussion-section handout text, used here in full.
- The handout itself points to, but does not reproduce, several external references for more depth:
  the Berkeley SCF "Git Basics" tutorial, the Software Carpentry Git lesson, the "Basic Branching
  and Merging" and "Advanced Merging" chapters of the Pro Git book, the interactive
  learngitbranching.js.org tutorial, the Pro Git "Undoing Things" chapter, and Atlassian's
  step-by-step pull-request tutorial. None of their content is included here beyond what the
  handout itself states.

---

[← 12. Version Control and Dynamic Documents](12-version-control-and-dynamic-documents.md) · [Contents](index.md) · [16. The Final Project →](16-the-final-project.md)
