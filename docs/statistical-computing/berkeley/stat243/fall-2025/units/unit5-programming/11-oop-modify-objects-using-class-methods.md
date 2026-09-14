---
title: 'OOP: modify objects using class methods'
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# OOP: modify objects using class methods

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

y = list([1.2, 3.5, 4.2])
y.append(7.9)  # y modified in place using class method
```

Different people have different preferences, but which is better sometimes depends on what you are trying to do. If your computation is a data analysis pipeline that involves a series of transformations of some data, a functional approach might make more sense, since the focus is on a series of actions rather than the state of objects. If your computation involves various operations on fixed objects whose state needs to change, OOP might make more sense. For example, if you were writing code to keep track of student information, it would probably make sense to have each student as an object of a `Student` class with methods such as `register` and `assign_grade`.

---

[← functional, but using class methods](10-functional-but-using-class-methods.md) · [Up: contents](index.md) · [6. Object-oriented programming (OOP) →](12-6-object-oriented-programming-oop.md)
