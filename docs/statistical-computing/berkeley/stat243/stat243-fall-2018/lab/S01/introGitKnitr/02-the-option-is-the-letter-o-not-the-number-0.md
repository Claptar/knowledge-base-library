---
title: the option is the letter O (Not the number 0)
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S01/introGitKnitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S01/introGitKnitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# the option is the letter O (Not the number 0)

**Source:** [`lab/S01/introGitKnitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S01/introGitKnitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

curl -O http://textfiles.com/food/bread.txt
```

- Use the command `ls` to list the contents in your current directory
- Use the command `curl` to download these other text files:
	- http://textfiles.com/food/btaco.txt
	- http://textfiles.com/food/1st_aid.txt
	- http://textfiles.com/food/beesherb.txt
- Use the command `curl` to download the following csv files:
	- http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv
	- http://www.math.uah.edu/stat/data/Fisher.csv
	- http://web.pdx.edu/~gerbing/data/cars.csv
- Now try `ls -l` to list the contents in your current directory in long format
- Look at the `man` documentation of `ls` to find out how to list the contents in reverse order
- How would you list the contents in long format and by time?
- Inside `stat243-S01` create a directory `data`
- Change to the directory `data`
- Create a directory `txt-files`
- Create a directory `csv-files`
- Use the command `mv` to move the `bread.txt` file to the folder `txt-files`
- Use the wildcard `*` to move all the text files to the directory `txt-files`
- Use the wildcard `*` to move all the `.csv` files to the directory `csv-files`
- Go back to the parent directory `stat243-S01`
- Create a directory `copies`
- Use the command `cp` to copy the `bread.txt` file (the one inside the folder
`txt-files`) to the `copies` directory
- Use the wildcard `*` to copy all the `.txt` files in the directory `copies`
- Use the wildcard `*` to copy all the `.csv` files in the directory `copies`
- Change to the directory `copies`
- Use the command `mv` to rename the file `bread.txt` as `bread-recipe.txt`
- Rename the file `Fisher.csv` as `iris.csv`
- Rename the file `btaco.txt` as `breakfast-taco.txt`
- Change to the parent directory (i.e. `stat243-S01`)
- Rename the directory `copies` as `copy-files`
- Find out how to use the `rm` command to delete the directory `copy-files`
- List the contents of the directory `txt-files` displaying the results in reverse (alphabetical) order

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Git and GitHub Practice →](03-git-and-github-practice.md)
