---
title: Comments
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/ps4.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/ps/ps4.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Comments

**Source:** [`ps/ps4.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/ps4.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

- This covers Unit 5.
- It's due at 10 am (Pacific) on October 12, both submitted as a PDF to Gradescope as well as committed to your GitHub repository.
- Please see PS1 and the grading rubric for formatting and attribution requirements.
- I just noticed that the `pryr` package has been superseded by functionality in other packages, particularly by `lobstr` in terms of our uses of `pryr`. So I suggest you use `lobstr::obj_addr`, `lobstr::obj_size`, and `lobstr::mem_used` in place of `pryr::address`, `pryr::object_size`, and `pryr::mem_used` respectively. That said, you'll likely need `.Internal(inspect())` for your solutions for the more granular information it provides.

---

[Up: contents](index.md) · [Problems →](02-problems.md)
