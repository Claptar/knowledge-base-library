---
title: type Q to quit and return to the bash shell
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/01/intro_git_knitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/01/intro_git_knitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# type Q to quit and return to the bash shell

**Source:** [`labs/01/intro_git_knitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/01/intro_git_knitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

git log
```

Let's make a change to `README.md`, which is now tracked by Git.

```bash
echo "Nothing to see here." >> README.md
```

`git status` will show that `README.md` was modified, along with other
useful information. But it won't actually show the _differences_ between your
repo's history and the current un-committed state. To see this, there is another
extremely useful command:

```bash

---

[← this usually opens in less](04-this-usually-opens-in-less.md) · [Up: contents](index.md) · [this also typically opens in less →](06-this-also-typically-opens-in-less.md)
