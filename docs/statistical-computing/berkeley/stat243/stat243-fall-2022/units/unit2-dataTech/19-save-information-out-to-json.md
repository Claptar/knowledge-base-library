---
title: save information out to JSON
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit2-dataTech.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# save information out to JSON

**Source:** [`units/unit2-dataTech.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

with open("senators-list.json", "w") as f:
    json.dump(senators, f, indent=4, sort_keys=True)
with open("timelines.json", "w") as f:
    json.dump(timelines, f, indent=4, sort_keys=True)
```


### Accessing dynamic pages

Some websites dynamically change in reaction to the user behavior. In
these cases you need a tool that can mimic the behavior of a human
interacting with a site. Some options are:

-   *selenium* (and the *RSelenium* wrapper for R) is a popular tool for
    doing this.

-   *splash* (and the *splashr* wrapper for R) is another approach.

-   *htmlunit* is another tool for this.

---

[← get all the senators' timelines](18-get-all-the-senators-timelines.md) · [Up: contents](index.md) · [5. File and string encodings →](20-5-file-and-string-encodings.md)
