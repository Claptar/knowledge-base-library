---
title: This test will fail.
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit3-goodPractices.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit3-goodPractices.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# This test will fail.

**Source:** [`units/unit3-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit3-goodPractices.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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
#| error: true
pytest test_dummy.py
```

You can run `pytest` on individual files or on directories or simply in the current working directory. In the latter cases, it will look for test files (those with the letters "test" in the file name) in the directory and all subdirectories.

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
    - uses: actions/checkout@v7

    # Install package and dependencies
    - name: Set up Python
      uses: actions/setup-python@v7
      with:
        python-version: 3.14

    - name: Install mytoy and pytest
      run: |
        pip install pytest
        pip install --user .

    - name: Run tests
      run: |
        cd mytoy
        pytest
```

Unfortunately, GitHub Actions is not available via `github.berkeley.edu` so we
can't use it with your class repositories for your problem set work.

## Version control

- Use it! Even for projects that only you are working on. It's the closest thing you'll get to having a time machine!
- Use an issues tracker (e.g., the GitHub issues tracker is quite
    nice), or at least a simple to-do file, noting changes you'd like to
    make in the future.

We'll be discussing Git a lot separately.

## AI-assisted coding tools

There is now a large variety of AI-assisted coding tools that are available within integrated development environments (IDEs) and allow you to easily work with AI while you are coding. This makes for an easier workflow than copy-pasting from a ChatBot.

!!! warning "Warning"
The arena of AI-assisted coding tools is evolving very quickly.
:::

Some common features of many tools include:

- AI-assisted code completion (extended tab completion)
- AI-assisted code suggestions (accept/reject, similar to grammar suggestions in text editing)
- Built-in Chat window providing interaction with an agent that can write and edit code.
- Ability to give files/directories as context.

Many of the tools are available through VS Code (as extensions, such as GitHub Copilot and Gemini Code Assist) or built on top of VS Code (e.g., Cursor). Other tools provide command line interfaces (e.g., Claude Code, Codex and Antigravity)

Beware of generating chunks of code (particularly large chunks) that you don't understand, particularly as you are learning. Think of the tools as helping you brainstorm.

A potential hierarchy of uses:

 - For straightforward syntax where checking the outcome is sufficient (e.g., code for formatting plots).
 - For (possibly complicated) small pieces of code where extensive testing may be sufficient (e.g., regular expressions).
 - For more extensive analysis or algorithm code, where you should check and understand the code fully.

---

[← 1. Good coding practices](02-1-good-coding-practices.md) · [Up: contents](index.md) · [2. Debugging and recommendations for avoiding bugs →](04-2-debugging-and-recommendations-for-avoiding-bugs.md)
