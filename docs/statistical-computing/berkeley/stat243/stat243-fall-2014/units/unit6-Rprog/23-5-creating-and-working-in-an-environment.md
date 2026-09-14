---
title: 5 Creating and working in an environment
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Creating and working in an environment

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We’ve already talked extensively about the environments that R creates. Occasionally you may want to create an environment in which to store objects.

e <- **new.env** () **assign** ("x", 3, envir = e) _# same as e$x <- 3_ e$x ## [1] 3 **get** ("x", envir = e, inherits = FALSE) ## [1] 3

_# the FALSE avoids looking for x in the enclosing environments_ e$y <- 5 **ls** (e)

51

---

[← Slots: ## ## Name: name age birthday ## Class: character numeric Date](22-slots-name-name-age-birthday-class-character-numeric-date.md) · [Up: contents](index.md) · [[1] "x" "y" rm ("x", envir = e) parent.env (e) ## →](24-1-x-y-rm-x-envir-e-parent-env-e.md)
