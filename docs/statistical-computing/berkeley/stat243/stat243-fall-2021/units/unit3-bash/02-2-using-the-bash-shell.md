---
title: 2 Using the bash shell
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit3-bash.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Using the bash shell

Please see the tutorial on using the bash shell. For our purposes in this Unit, you should work through all of the material EXCEPT as follows:

- If you don't have access to a remote Unix-based machine (such as one of the SCF machines), then you wouldn't be able to practice with *ssh* and *scp* in Section 1.1. That's fine. Just read it over to get the main idea.
- You can skip Section 1.4.1.
- You can skip regular expressions (Section 3), but do look at Section 3.6.1 and the 'text substitution' use of *sed* in Section 3.6.2.
- Feel free to skip Section 4 for now; I'll ask you to read it more carefully later.

When we talk about string processing and regular expressions in R in Unit 5, we'll come back to the material on regular expressions.

When looking at Sections 3.6.1 and 3.6.2, note that you can use *grep* to look for and *sed* to replace simple strings in files without needing to know how to specify patterns based on regular expressions. So try to see how to do that without getting bogged down in the examples in those sections that use the complicated regular expression syntax. For example:

```bash
grep "," file.txt # look for lines with commas in file.txt
sed -i 's/,/;/g' file.txt # replace commas with semicolons in file.txt
```

---

[← Unit 3: The bash shell and UNIX utilities](01-unit-3-the-bash-shell-and-unix-utilities.md) · [Up: contents](index.md) · [3 bash shell examples →](03-3-bash-shell-examples.md)
