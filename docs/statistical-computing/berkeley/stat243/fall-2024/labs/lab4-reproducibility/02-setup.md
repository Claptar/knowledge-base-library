---
title: Setup
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab4-reproducibility.qmd
source_file: sources/berkeley-stat243/fall-2024/labs/lab4-reproducibility.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Setup

**Source:** [`labs/lab4-reproducibility.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab4-reproducibility.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

- Find a link to "Replication Package" on the paper's page and click on "Download this project". Authentication is required; we recommend to "access through your institution" and fall back to the other options in case this fails. By the end of this step, you should have a file named `202185-V1.zip` on your machine. If that also does not work, you may try `wget www.stat.berkeley.edu/~paciorek/transfer/202185-V1.zip`.

- Unzip `202185-V1.zip` and enter `Rad_AI_Longtail/`.

- Investigate which files are likely to contain reproducibility instructions and give it a quick read.

- We now need to use the specific python version mentioned by the authors (3.11) to install the packages necessary to reproduce the results, which should be straightforward given the `requirements.txt`. But there are several caveats here. Try installing those packages and document your experience. Creating a conda environment using the provided `requirements.txt` file may be a reasonable attempt: `conda create --name lab4 python=3.11 --file requirements.txt`. If it fails on your system, try to identify why.

- As an alternative, you may try the following command to generate an adjusted requirements file to be then to install packages:
```
grep -rh import . |
    sed -e 's/"//g; s/,//g; s/\\n//g; s/^ *//g; s/ *$//g; /^$import \|from $/!d' |
    cut -d ' ' -f 2 |
    cut -d '.' -f 1 |
    sort |
    uniq |
    grep -f - requirements.txt |
    grep -v '^#' |
    cut -d '=' -f 1,2 |
    sed 's/=/==/g' |
    grep -v '_' |
    grep -v '\-base' >
    requirements_adjusted.txt
```

- Running the command above incrementally might be useful to better understand what each step does if it is not immediately clear. Installing the packages should then be less prone to error by using this `requirements_adjusted.txt` file. You will also need `nbformat==5.9.2` and `jinja2==3.1.2` to be installed. Think in particular about the following modification `sed 's/=/==/g'` and what are the implications.

---

[← Reproducibility](01-reproducibility.md) · [Up: contents](index.md) · [Replicating the results in the paper →](03-replicating-the-results-in-the-paper.md)
