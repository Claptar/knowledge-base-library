---
title: This test will fail.
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit4-goodPractices.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit4-goodPractices.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# This test will fail.

**Source:** [`units/unit4-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit4-goodPractices.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

def test_numpy_array():
    assert np.all(np.equal(dummy.add_one(np.array([3,4])), np.array([4,5])))

def test_bad_input():
    with pytest.raises(TypeError):
        dummy.add_one('hello')

def test_warning():
    with pytest.warns(UserWarning, match='complex'):
        dummy.add_one(1+3j)
```


We can then run the tests via `pytest` like this:

```bash
pytest mytestfile.py
```

```
====================================== test session starts ======================================
platform linux -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0
rootdir: /accounts/vis/paciorek/teaching/243fall24/fall-2024/units
plugins: anyio-4.3.0
collected 4 items

test_dummy.py .F..                                                                        [100%]

=========================================== FAILURES ============================================
_______________________________________ test_numpy_array ________________________________________

    def test_numpy_array():
>       assert np.all(np.equal(dummy.add_one(np.array([3,4])), np.array([4,5])))

test_dummy.py:11:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

x = array([3, 4])

    def add_one(x):
        if not isinstance(x, (float, int, complex)):
>           raise TypeError(f"`{x}` should be numeric")
E           TypeError: `[3 4]` should be numeric

dummy.py:5: TypeError
==================================== short test summary info ====================================
FAILED test_dummy.py::test_numpy_array - TypeError: `[3 4]` should be numeric
================================== 1 failed, 3 passed in 0.84s ==================================
```

In lab, we'll go over assertions, exceptions, and testing in
detail.

### Automated testing

*Continuous integration* (CI) is the term for carrying out actions automatically as your code changes. The most common kind of CI is automated testing - running your tests on your code when you make changes to the code. This enforces the discipline of running tests regularly and avoids the common problem that testing passes locally on your own machine, but fails for various reasons when done elsewhere.

A standard way to do this is via GitHub Actions (GHA).

To set up a GitHub Actions workflow, one

- specifies when the workflow will run (e.g., when a push or pull request is made, or only manually)
- provides instructions for how to set up the environment for the workflow
- provides the operations that the workflow should run.

The workflow is specified using a YAML file placed in the `.github/workflows` directory of the repository.

With GHA, you specify the operating system and then the steps to run in the YAML file. Some steps will  customize the environment as the initial steps and then additional step(s) will run shell or other code to run your workflow. You use pre-specified operations (called *actions*) to do common things (such as checking out a GitHub repository and installing commonly used software).

When triggered, GitHub will run the steps in a virtual machine, which is called the *runner*.

Here's an example YAML file for testing [an example package called `mytoy`](https://github.com/fperez/mytoy):

```
on:
  push:
    branches:
    - main

jobs:
  CI:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    # Install package and dependencies
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: 3.12

    - name: Install mytoy and pytest
      run: |
        pip install pytest
        pip install --user .

    - name: Run tests
      run: |
        cd mytoy
        pytest
```

You'll use GitHub Actions to automate testing during your projects. Unfortunately, GitHub Actions is not available via `github.berkeley.edu` so we
can't use it with your class repositories for your problem set work.

## Version control

- Use it! Even for projects that only you are working on. It's the closest thing you'll get to having a time machine!
- Use an issues tracker (e.g., the GitHub issues tracker is quite
    nice), or at least a simple to-do file, noting changes you'd like to
    make in the future.
- In addition to good commit messages, it's a good idea to keep good
    running notes documenting your projects.

We'll be discussing Git a lot separately.

---

[← 1. Good coding practices](02-1-good-coding-practices.md) · [Up: contents](index.md) · [2. Debugging and recommendations for avoiding bugs →](04-2-debugging-and-recommendations-for-avoiding-bugs.md)
