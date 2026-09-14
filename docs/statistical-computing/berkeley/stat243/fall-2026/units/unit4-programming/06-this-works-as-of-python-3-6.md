---
title: This works as of Python 3.6.
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# This works as of Python 3.6.

**Source:** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

[← 3. Output from Python](05-3-output-from-python.md) · [Up: contents](index.md) · [4. Interacting with the operating system and external code and configuring Python →](07-4-interacting-with-the-operating-system-and-external-code-an.md)
