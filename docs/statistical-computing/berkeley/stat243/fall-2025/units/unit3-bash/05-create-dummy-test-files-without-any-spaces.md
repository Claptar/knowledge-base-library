---
title: Create dummy test files without any spaces.
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Create dummy test files without any spaces.

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

touch ~/Downloads/test{1..4}
ls -rt ~/Downloads | tail -n 5

## Sometimes the ~ behaves weirdly in scripting, so let's use full path.
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

**We'll work on Challenge #3 here.**

**We'll work on Challenge #4 here.**


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

## Note: on a Mac, use 's/,/\\\n/g'
## See https://superuser.com/questions/307165/newlines-in-sed-on-mac-os-x

echo "There are $(wc -l requirements.txt | cut -d' ' -f1) \
unique packages we will install."
## Note: on Linux, wc -l puts the number as the first characters of the output.
## On a Mac, there may be a bunch of spaces preceding the number, so try this:
## echo "There are $(wc -l libs.txt | tr -s ' ' | cut -d' ' -f2) \
## unique packages we will install."

pip install -r requirements.txt

---

[← 3. bash shell examples](04-3-bash-shell-examples.md) · [Up: contents](index.md) · [or use Mamba/Conda →](06-or-use-mamba-conda.md)
