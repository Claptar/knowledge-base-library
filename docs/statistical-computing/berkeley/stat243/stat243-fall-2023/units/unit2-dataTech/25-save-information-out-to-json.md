---
title: save information out to JSON
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit2-dataTech.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# save information out to JSON

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

with open("senators-list.json", "w") as f:
    json.dump(senators, f, indent=4, sort_keys=True)
with open("timelines.json", "w") as f:
    json.dump(timelines, f, indent=4, sort_keys=True)
```


### Accessing dynamic pages

Some websites dynamically change in reaction to the user behavior. In
these cases you need a tool that can mimic the behavior of a human
interacting with a site. Some options are:

- `selenium` is a popular tool for doing this, and there is a Python package of the same name.
- Using `scrapy` plus `splash`  is another approach.

---

[← get all the senators' timelines](24-get-all-the-senators-timelines.md) · [Up: contents](index.md) · [5. File and string encodings →](26-5-file-and-string-encodings.md)
