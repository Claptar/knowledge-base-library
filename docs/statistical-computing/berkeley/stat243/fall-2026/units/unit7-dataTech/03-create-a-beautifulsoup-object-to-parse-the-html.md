---
title: Create a BeautifulSoup object to parse the HTML
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit7-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit7-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Create a BeautifulSoup object to parse the HTML

**Source:** [`units/unit7-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit7-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

soup = bs(html, 'html.parser')

html_tables = soup.find_all('table')

## Pandas `read_html` doesn't want `str` input directly.
pd_tables = [pd.read_html(io.StringIO(str(tbl)))[0] for tbl in html_tables]

[x.shape for x in pd_tables]

pd_tables[0]
```


Beautiful Soup works by reading in the HTML as text and then parsing it
to build up a tree containing the HTML elements. Then one can [search by
HTML tag or attribute](https://beautiful-soup-4.readthedocs.io/en/latest/#searching-the-tree)
for information you want using `find_all`.

As another example, it's often useful to be able to extract the hyperlinks in an HTML document.

```python
URL = "http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year"
response = requests.get(URL)
soup = bs(response.content, 'html.parser')

## Approach 1: search for HTML 'a' tags.
a_elements = soup.find_all('a')
links1 = [x.get('href') for x in a_elements]
## Approach 2: search for 'a' elements with 'href' attribute
href_elements = soup.find_all('a', href = True)
links2 = [x.get('href') for x in href_elements]
## In either case, then use `get` to retrieve the `href` attribute value.

links2[0:9]

---

[← 1. Working with information on the web](02-1-working-with-information-on-the-web.md) · [Up: contents](index.md) · [help(bs.findall) →](04-help-bs-findall.md)
