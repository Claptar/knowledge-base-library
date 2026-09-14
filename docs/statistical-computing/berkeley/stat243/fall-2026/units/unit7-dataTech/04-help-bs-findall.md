---
title: help(bs.findall)
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit7-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit7-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# help(bs.findall)

**Source:** [`units/unit7-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit7-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

```

The `kwargs` keyword arguments to `find` and `find_all` allow one
to search for elements with particular characteristics, such
as having a particular attribute (seen above) or having an attribute
have a particular value (e.g., picking out an element with a particular
`id`).

Here's another example of extracting specific components of information
from a webpage (results not shown, since headlines will vary from day to
day). We'll use `get_text` to retrieve the element's value.

```python
#| eval: false
URL = "https://dailycal.org"
response_news = requests.get(URL)
soup_news = bs(response_news.content, 'html.parser')
h2_elements = soup_news.find_all("h2")
headlines2 = [x.get_text() for x in h2_elements]
h3_elements = soup_news.find_all("h3")
headlines3 = [x.get_text() for x in h3_elements]
```

More generally, we may want to read an HTML document, parse it into its
components (i.e., the HTML elements), and navigate through the tree
structure of the HTML.

We can use [CSS selectors](https://www.w3schools.com/cssref/css_selectors.asp)
 with the `select` method for more powerful extraction capabilities. Going back to the climate data, let's extract all the `th` elements nested within `tr` elements:

```python
soup.select("tr th")
```

Or we could extract  the `a` elements whose parents are `th` elements:

```python
soup.select("th > a")
```

Next let's use the *XPath* language to specify
elements rather than CSS selectors. XPath can also be used for
navigating through XML documents.

```python
import lxml.html

---

[← Create a BeautifulSoup object to parse the HTML](03-create-a-beautifulsoup-object-to-parse-the-html.md) · [Up: contents](index.md) · [Convert the BeautifulSoup object to a lxml object →](05-convert-the-beautifulsoup-object-to-a-lxml-object.md)
