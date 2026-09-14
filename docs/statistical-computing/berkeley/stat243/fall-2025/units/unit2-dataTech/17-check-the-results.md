---
title: Check the results.
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Check the results.

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

print(f"Successfully created issue #{issue.number}")
print(f"URL: {issue.html_url}")
g.close()
```


### Accessing dynamic pages

Many websites dynamically change in reaction to the user behavior. In
these cases you need a tool that can mimic the behavior of a human
interacting with a site. Some options are:

- `selenium` is a popular tool for doing this, and there is a Python package of the same name.
- Using `scrapy` plus `splash`  is another approach.

---

[← Create the issue](16-create-the-issue.md) · [Up: contents](index.md) · [5. File and string encodings →](18-5-file-and-string-encodings.md)
