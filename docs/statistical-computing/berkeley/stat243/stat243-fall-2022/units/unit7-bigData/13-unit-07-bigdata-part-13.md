---
title: Unit 07 — bigData Part 13 —
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 07 — bigData Part 13 —

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

obama = lines.filter(find)  # use this for demo in section
obama.count()  # 433k observations for full dataset
```

Now let's use the mapReduce paradigm to get the aggregate statistics we
want.

```python
### map-reduce step to sum hits across date-time-language triplets ###

def stratify(line):
    # create key-value pairs where:
    #   key = date-time-language
    #   value = number of website hits
    vals = line.split(' ')
    return(vals[0] + '-' + vals[1] + '-' + vals[2], int(vals[4]))

---

[← not clear if should repartition; will likely have small partitions if not](12-not-clear-if-should-repartition-will-likely-have-small-parti.md) · [Up: contents](index.md) · [sum number of hits for each date-time-language value →](14-sum-number-of-hits-for-each-date-time-language-value.md)
