---
title: Some review of key commands you should already know
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/09/collab_with_git.md
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/09/collab_with_git.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Some review of key commands you should already know

**Source:** [`labs/09/collab_with_git.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/09/collab_with_git.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

When using Git for collaboration, you will often find that much of your workflow
remains similar to how you used Git when working alone. That is, you will still
use the following **four key commands** (click to expand):

!!! tip "Tip"
### Key command #1: `git status`

`git status` is the most fundamental way to understand what is going on in your
repo. You should use it often to remind yourself of the current state of things.

**When to use**: when starting or resuming work on a repo; prior to using `git
add` to remind yourself what files have been modified or already staged; prior
to using `git commit` to ensure you have staged all the files you want to
include in your next snapshot.

:::

!!! tip "Tip"
### Key command #2: `git diff`

The output from `git diff` demonstrates just how powerful Git really is. It can
also be incredibly useful when editing existing code, because it shows both the
state of the code before you made modifications alongside the modifications
themselves. There have been many times where I've caught bugs in my code by
inspecting `git diff` prior to committing my changes.

Note that because `git diff` shows _changes_ to tracked files, it only becomes
useful after modifying a file that you've already staged at some prior point.

Sometimes you will want to see the diff from a file is in the staged state,
prior to committing; to do so, you can use `git diff --staged`.

**When to use**: after modifying a file that was staged at some previous point;
before using `git commit` to do a quick spot check of your changes; when you
want to see what changes were made in a particular commit.

:::

!!! tip "Tip"
### Key command #1: `git add`

To this point, we've already said a good deal about `git add`. It stages changes
in your for the next commit.

**When to use**: after making changes to a particular file or set of files;
after making additional changes to a staged file or set of files; to prepare for
the next commit.

:::

!!! tip "Tip"
### Key command #1: `git commit`

We've already alluded to this command many times above as well. Use it to move
staged changes into the repo's commit history. Be sure to include a _succinct_
and _informative_ commit message so that your collaborators and your future self
have a quick hint to understand the changes you made.

It is better to make small commits for contained changes rather than a mega
commit with a diverse set of functional modifications that touch a large portion
of the code. For example, if you work linearly through your problem sets then it
is better to commit after completing each individual problem or even
sub-problem, rather than making a single commit when the full problem set is
complete.


**When to use**: after finishing work on a particular task; incrementally, when
some contained change is complete; as often as needed so that you can create
succinct but informative commit messages.

:::

If you have any doubts about these four key commands at this point, please check
in with your partner or raise your hand and I will do my best to clear things up
before you continue on to the following sections.

## Manual pages

Git's built-in documentation is a good resource when in doubt about a particular
command or to deepen your knowledge. There are many useful options to Git's
commands, so taking a skim through the manual pages for the commands you use
most often is not a bad idea.

To see the docs for a command such as `git log`, you can do:

```bash
man git-log
```
or:

```bash
git help log
```

Alternatively, you can access these manual pages on the web at
https://git-scm.com/docs. From the `git log` manual, we can find information on
a number of options that greatly increase the usefulness of the output. We'll
see some examples later on in the next section.

---

[← Some terminology](02-some-terminology.md) · [Up: contents](index.md) · [Advanced Git features for collaboration →](04-advanced-git-features-for-collaboration.md)
