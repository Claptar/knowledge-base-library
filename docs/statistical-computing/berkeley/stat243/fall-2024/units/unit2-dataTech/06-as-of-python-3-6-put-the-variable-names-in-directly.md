---
title: As of Python 3.6, put the variable names in directly.
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# As of Python 3.6, put the variable names in directly.

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit2-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

[← 3. Output from Python](05-3-output-from-python.md) · [Up: contents](index.md) · [4. Webscraping and working with HTML, XML, JSON, and YAML →](07-4-webscraping-and-working-with-html-xml-json-and-yaml.md)
