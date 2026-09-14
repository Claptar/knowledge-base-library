---
title: As of Python 3.6, put the variable names in directly.
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit2-dataTech.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# As of Python 3.6, put the variable names in directly.

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

print(f"Let's add {val1} and {val2}.")
num1 = 1/3
print("Let's add the %s numbers %.5f and %15.7f."
       %('floating point', num1 ,32+1/7))
```

Or to insert into a file:
```python
#| eval: false
file_path = os.path.join('/tmp', 'tmp.txt')
with open(file_path, 'a') as file:
     file.write("Let's add the %s numbers %.5f and %15.7f."
                %('floating point', num1 ,32+1/7))

```

`round` is another option, but it's often better to directly control the printing format.

---

[← 3. Output from Python](05-3-output-from-python.md) · [Up: contents](index.md) · [4. Webscraping and working with HTML, XML, and JSON →](07-4-webscraping-and-working-with-html-xml-and-json.md)
