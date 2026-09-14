---
title: create dummy test files without any spaces
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit3-bash.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# create dummy test files without any spaces

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

touch ~/Downloads/test{1..4}
ls -rt ~/Downloads | tail -n 5

## sometimes the ~ behaves weirdly in scripting, so let's use full path
mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
   /accounts/vis/paciorek/Downloads | tail -n 1)" ~/Desktop

function mvlast() {
    mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
       /accounts/vis/paciorek/Downloads | tail -n 1)" $1
}
```

Note that the quotes deal with cases where a file has a space in its name.

If we wanted to handle multiple files, we could do it with a loop:

```bash
#| eval: false
function mvlast() {
    for ((i=1; i<=${1}; i++)); do
        mv "/accounts/vis/paciorek/Downloads/$(ls -rt \
           /accounts/vis/paciorek/Downloads | tail -n 1)" ${2}
    done
}
```

Side note: if we were just moving files from the current working directory and with files without spaces in their names, it should be possible to use `tail -n ${1}` without the loop.

**Our fifth mission**: automate the process of determining what Python
packages are used in all of the qmd code chunks here and install those packages
on a new machine.

```bash
#| eval: false
grep import *.qmd
grep --no-filename import *.qmd
grep --no-filename "^import" *.qmd
grep --no-filename "^import " *.qmd
grep --no-filename "^import " *.qmd | sort | uniq
grep --no-filename "^import " *.qmd | cut -d'#' -f1
grep --no-filename "^import " *.qmd | cut -d'#' -f1 | sed  "s/as .*//"
grep --no-filename "^import " *.qmd | cut -d'#' -f1 | \
                   sed  "s/as .*//" | sed "s/import //" > tmp.txt
sed "s/,/\n/g" tmp.txt | sed "s/ //g" | sort | uniq | tee requirements.txt

## note: on a Mac, use 's/,/\\\n/g'
## See https://superuser.com/questions/307165/newlines-in-sed-on-mac-os-x

echo "There are $(wc -l requirements.txt | cut -d' ' -f1) \
unique packages we will install."
## note: on Linux, wc -l puts the number as the first characters of the output
## on a Mac, there may be a bunch of spaces preceding the number, so try this:
## echo "There are $(wc -l libs.txt | tr -s ' ' | cut -d' ' -f2) \
## unique packages we will install."

pip install -r requirements.txt

---

[← 3. bash shell examples](03-3-bash-shell-examples.md) · [Up: contents](index.md) · [or use Mamba/Conda →](05-or-use-mamba-conda.md)
