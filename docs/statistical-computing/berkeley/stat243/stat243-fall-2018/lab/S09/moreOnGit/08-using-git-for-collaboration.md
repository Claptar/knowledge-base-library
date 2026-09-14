---
title: Using Git For Collaboration
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S09/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Using Git For Collaboration

**Source:** [`lab/S09/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Suppose that Ugur has started a new project with a Git repository in /home/ugur/project, and that Omid, who has a home directory on the same machine, wants to contribute.

This creates a new directory "myrepo" containing a clone of Ugur's repository. The clone is on an equal footing with the original project, possessing its own copy of the original project's history. Omid then makes some changes and commits them. When he's ready, he tells Ugur to pull changes from the repository at /home/omid/myrepo. He does this with:

```bash
ugur$ cd /home/ugur/project
ugur$ git pull /home/omid/myrepo master
```

This merges the changes from Omid's "master" branch into Ugur's current branch. If Ugur has made her own changes in the meantime, then he may need to manually fix any conflicts.

The `pull` command thus performs two operations: it fetches changes from a remote branch, then merges them into the current branch.

Note that in general, Ugur would want his local changes committed before initiating this `pull`. If Omid's work conflicts with what Ugur did since their histories forked, Ugur will use his working tree and the index to resolve conflicts, and existing local changes will interfere with the conflict resolution process (Git will still perform the fetch but will refuse to merge --- Ugur will have to get rid of his local changes in some way and pull again when this happens).

Ugur can peek at what Omid did without merging first, using the "fetch" command; this allows Ugur to inspect what Omid did, using a special symbol "FETCH_HEAD", in order to determine if he has anything worth pulling, like this:

```bash
ugur$ git fetch /home/omid/myrepo master
ugur$ git log -p HEAD..FETCH_HEAD
```

This operation is safe even if Ugur has uncommitted local changes. The range notation "HEAD..FETCH_HEAD" means "show everything that is reachable from the FETCH_HEAD but exclude anything that is reachable from HEAD". Ugur already knows everything that leads to his current state (HEAD), and reviews what Omid has in his state (FETCH_HEAD) that he has not seen with this command.

If Ugur wants to visualize what Omid did since their histories forked he can issue the following command:

```bash
gitk HEAD..FETCH_HEAD
```

Ugur may want to view what both of them did since they forked. He can use three-dot form instead of the two-dot form:

```bash
gitk HEAD...FETCH_HEAD
```

This means "show everything that is reachable from either one, but exclude anything that is reachable from both of them".

Please note that these range notation can be used with both gitk and `git log`.

After inspecting what Omid did, if there is nothing urgent, Ugur may decide to continue working without pulling from Omid If Omid's history does have something Ugur would immediately need, he may choose to stash his work-in-progress first, do a `pull`, and then finally unstash his work-in-progress on top of the resulting history.

When you are working in a small closely knit group, it is not unusual to interact with the same repository over and over again. By defining remote repository shorthand, you can make it easier:

```bash
ugur$ git remote add omid /home/omid/myrepo
```

With this, Ugur can perform the first part of the `pull` operation alone using the git fetch command without merging them with his own branch, using:

```bash
ugur$ git fetch omid
```

Unlike the longhand form, when Ugur fetches from Omid using a remote repository shorthand set up with git remote, what was fetched is stored in a remote-tracking branch, in this case omid/master. So after this:

```bash
ugur$ git log -p master..omid/master
```

shows a list of all the changes that Omid made since he branched from Ugur's master branch.

After examining those changes, Ugur could merge the changes into his master branch:

```bash
ugur$ git merge omid/master
```
This merge can also be done by pulling from his own remote-tracking branch, like this:
```bash
ugur$ git pull . remotes/omid/master
```

Note that git pull always merges into the current branch, regardless of what else is given on the command line.

Later, Omid can update his repo with Ugur's latest changes using

```bash
omid$ git pull
```
Note that he doesn't need to give the path to Ugur's repository; when Omid cloned Ugur's repository, Git stored the location of his repository in the repository configuration, and that location is used for pulls:

```bash
omid$ git config --get remote.origin.url
```
/home/ugur/project

Git also keeps a pristine copy of Ugur's master branch under the name "origin/master":

```bash
omid$ git branch -r
```

```bash
ugur$ git fetch omid
```

---

[← Managing Branches](07-managing-branches.md) · [Up: contents](index.md)
