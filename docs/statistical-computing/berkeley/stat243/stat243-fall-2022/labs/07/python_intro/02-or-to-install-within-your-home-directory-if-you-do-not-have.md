---
title: or to install within your home directory if you do not have admin control of
  the computer
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/07/python_intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# or to install within your home directory if you do not have admin control of the computer

**Source:** [`labs/07/python_intro.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

pip install --user numpy
```

For additional help with installation, please see the [IPython installation page](http://ipython.org/install.html).

## Resources

Useful written references and tutorials:

-   <https://docs.python.org/3/index.html>
-   <https://docs.python.org/3/library/index.html>
-   <https://scipy-lectures.github.io/>

Some introductory video lectures:

-   <https://www.youtube.com/watch?v=a_Z_6brm9ZQ>

While working through this tutorial, you should type the example code
snippets at an interactive Python terminal. I recommend using either the
IPython shell or a Jupyter IPython notebook. To start an IPython shell, type
the following at a bash prompt:

```bash
ipython
```

To start an Jupyter IPython notebook, type this:

```bash
jupyter notebook
```

A notebook should open in your browser.

Alternatively you can access Jupyter notebooks through a service called [Jupyterhub on the SCF](https://jupyter.stat.berkeley.edu).

Side note: to have all output (not just the last result) printed in the Jupyter notebook, you can run this in a cell in your notebook.

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

## Python 2 vs. 3

Python 3 is the current version of Python. For many years the old version
(Python 2) has co-existed with Python 3 and Python 2 has been used by many
people despite the existence of Python 3. Python 2 is now being phased out, so don't use it.

---

[← Background](01-background.md) · [Up: contents](index.md) · [Introduction →](03-introduction.md)
