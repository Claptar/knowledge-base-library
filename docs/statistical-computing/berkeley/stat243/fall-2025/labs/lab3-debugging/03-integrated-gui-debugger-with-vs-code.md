---
title: Integrated GUI debugger (with VS Code)
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab3-debugging.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab3-debugging.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Integrated GUI debugger (with VS Code)

**Source:** [`labs/lab3-debugging.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab3-debugging.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Today we will experiment with the visual debugging tools integrated with IDEs. We will do that in VS Code (unless you have another IDE with debugger integration). We will load a piece of code, go through it to understand what it does, then try to discover the problem with it and fix it. Our main function is `get_commits`, which makes use of the GitHub API to retrieve the recent commits to a repository. The fact that there are nested functions makes debugging less straightforward, but we will see how the bug could nevertheless be uncovered. Although the focus is on visual debuggers today, the ideas apply directly to command-line debuggers.

```python
import json
import pandas as pd
import requests
import warnings

def get_login(item):
    if not isinstance(item, dict):
        raise TypeError(f"`item` argument must be a dictionary")
    return item['author']['login']

def process(data):
    if not isinstance(data, dict) or "commit" not in data.keys() or \
       not isinstance(data['commit'], dict) or \
       "author" not in data['commit'].keys() or \
       not isinstance(data['commit']['author'], dict) or \
       "name" not in data['commit']['author'].keys() or \
       "date" not in data['commit']['author'].keys():
        raise RuntimeError(f"Unexpected json structure returned for commit: {data}")
    return {"user": data['commit']['author']['name'],
            "date": data['commit']['author']['date'],
            "login": get_login(data)}

def get_commits(org, repo, extended=False):
    if not isinstance(org, str):
        raise TypeError(f"`org` argument must be a string")
    if not isinstance(org, str):
        raise TypeError(f"`repo` argument must be a string")
    main_url = 'https://api.github.com/repos'
    perpage = 100
    # Search parameters
    request = f"{main_url}/{org}/{repo}/commits?per_page={perpage}"
    try:
        response = requests.get(request)
    except Exception as err:
        print("Problem making GitHub commits API request over the internet")
        raise

    if response.status_code == 200:  # Or `response.reason == 'OK':`
        content = response.content
    else:
        raise RuntimeError(f"Error in API request: {response.status_code}.")

    data = json.loads(content)
    data_cleaned = [process(item) for item in data]
    df = pd.DataFrame(data_cleaned)
    return df
```

---

[← Advanced debugging](02-advanced-debugging.md) · [Up: contents](index.md) · [Post-mortem debugging →](04-post-mortem-debugging.md)
