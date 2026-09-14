---
title: Set up authentication and headers
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit7-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit7-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Set up authentication and headers

**Source:** [`units/unit7-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit7-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

headers = {
    "Authorization": f"token {ghtoken}",
    "Accept": "application/vnd.github+json"
}

response = requests.post(url, json=issue, headers=headers)

if response.status_code == 201:
    print(f"Successfully created Issue! {response.json()['html_url']}")
else:
    print("Could not create Issue")
    print(response.status_code, response.text)
```

Note that for security, I created a [GitHub fine-grained personal access token](https://github.com/settings/personal-access-tokens) that is limited in *scope* to
only be able to handle issues in my test repository. And I've put the token into a file that is not committed to the GitHub repository containing these materials. (When doing this sort of thing with GitHub Actions, one would generally [store the token as a "secret" in the repository](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets.)


I could also have done this from the command line with `curl`, along the following lines:

```bash
#| eval: false
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GH_PERSONAL_ACCESS_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -H "User-Agent: My-Issue-Creator" \
  https://api.github.com/repos/paciorek/test/issues \
  -d '{"title":"New issue from API","body":"This issue was created using the GitHub API.","labels":["bug"]}'
```

where `${GH_PERSONAL_ACCESS_TOKEN}` is an environment variable containing the token.


`requests` can handle other kinds of HTTP requests such as PUT
and DELETE. Finally, some websites use cookies to keep track of users,
and you may need to download a cookie in the first interaction with the
HTTP server and then send that cookie with later interactions. More
details are available in the Nolan and Temple Lang book.

### Packaged access to an API

For popular websites/data sources, a developer may have packaged up the
API calls in a user-friendly fashion as functions for use from Python, R, or other
software.

For example there are various Python and R packages for interacting with GitHub
via its API.

Here's some example code for the `PyGitHub` package. We'll repeat the exercise of
programmatically creating a GitHub issue in my `paciorek/test` repository.

```python
#| eval: true
from github import Github

with open(".github-access-token.txt", "r") as file:
  ghtoken = file.read().strip()

g = Github(ghtoken)
repo_name = "paciorek/test"
repo = g.get_repo(repo_name)

---

[← Information about the issue in dict/json format.](08-information-about-the-issue-in-dict-json-format.md) · [Up: contents](index.md) · [Issue details →](10-issue-details.md)
