---
title: Contrasting Python and R
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit10-python.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit10-python.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Contrasting Python and R

**Source:** [`units/unit10-python.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit10-python.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

October 14, 2013

References:

Berkeley Python bootcamp (2010 version), organized by Josh Bloom

## **1 Programming concepts**

We’ve covered a lot of topics in R. Part of the purpose was to learn a single language really well. But by learning a language we’ve also seen a lot of the core concepts that come up in other programming languages. Here are some of the topics that we’ve discussed:

- variable types

- passing by reference and by value

- variable scope

- the call stack

- flow control

- object-oriented programming

- matrix storage concepts

- parsing

The goals of this unit are two-fold: (1) give you a basic introduction to Python, which some of you will be using intensively in the Statistics Master’s capstone course in the spring and (2) further develop understanding of programming concepts by seeing the concepts we’ve encountered with R in a different context.

1

I will note here that I am by no means a Python expert. I’ve picked up a bit here and there but am still learning. So, as is always the case, please do contribute your own knowledge in class, on the course Wiki on Github, and on Piazza.

Also a note on the formatting of this document. _knitr_ doesn’t do what I want in terms of showing the Python output (or indentation of the original code), so you’ll just see the Python syntax here and we’ll see the results in class.

## **2 Introduction to Python**

Python is an interpreted language that often serves as a glue to tie together different types of code/operations in a project. It’s particularly good at string manipulation and interacting with the operating system. Like R, you can run Python in a variety of ways: interactively from the command line, as a script, as a background job, and using a GUI (the _iPython notebook_ ). In the demos in class, we’ll use the _iPython_ interface, which has nice functionality including tab completion, command recall, and enhanced help information.

Like R, Python is an interpreted language and in some ways the syntax is similar.

print("Hi there") print(2 + 2) 2.1 * 5 # type casting/coercion # indentation matters 2.1 * 5 dist = 7 dist < 6 type(2) type(2.0) type(2*5.0) isinstance(dist, int)

Python is particularly good at string operations.

intro = "My name is" name = "sam" endLine = ".\n" intro + name.capitalize() + endLine intro.split(' ') 'abcdefghijkl'[0:10:2] # Python indexing starts with 0

2

The _name.capitalize()_ business involves object oriented programming, which is more elegant in Python than in R.

We can do flow control in Python in similar fashion to R. Here’s an _if-else_ block.

hi = 7 if name == "samuel": print(intro + name.capitalize() + endLine) elif name == "sam": print("My nickname is" + name.capitalize() + endLine) else: print("My name is something else.\n")

And here’s a _for_ loop.

x = 0 for i in range(10): x += i

---

[Up: contents](index.md) · [on the command line, we need the blank line above to end the loop print("x is " + str(x)) →](02-on-the-command-line-we-need-the-blank-line-above-to-end-the.md)
