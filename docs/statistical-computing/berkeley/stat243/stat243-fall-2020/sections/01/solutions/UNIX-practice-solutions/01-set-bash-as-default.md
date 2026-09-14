---
title: set bash as default
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/UNIX-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/01/solutions/UNIX-practice-solutions.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# set bash as default

**Source:** [`sections/01/solutions/UNIX-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/UNIX-practice-solutions.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

knitr::opts_chunk$set(engine='bash')
```


## 1.

```r
mkdir -p projects/drought
```

## 2.
```r
ls -lrS
```

## 3.
First we need to clone the repository, then we can adjust the permissions on the file.
```r
git clone https://github.com/berkeley-stat243/stat243-fall-2018
cd stat243-fall-2018/units
ls -l unit2-bash.sh
```

Note, the file is already readable by the user and the group.  We remove the readability for other. The file is already writable by the user.  We add excuting permission for all.
```r
cd stat243-fall-2018/units
chmod o-r unit2-bash.sh
chmod ugo+x unit2-bash.sh
ls -l unit2-bash.sh
```

## 4.
.zip file is larger
```r
zip -r stat243-fall-2018.zip stat243-fall-2018
tar -cvzf stat243-fall-2018.tar stat243-fall-2018
```

```r

---

[Up: contents](index.md) · [removing 2018 folder →](02-removing-2018-folder.md)
