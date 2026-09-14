---
title: help(bs.findall)
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit2-dataTech.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# help(bs.findall)

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

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
URL = "https://www.nytimes.com"
responseNYT = requests.get(URL)
soupNYT = bs(responseNYT.content, 'html.parser')
h2_elements = soupNYT.find_all("h2")
headlines2 = [x.get_text() for x in h2_elements]
h3_elements = soupNYT.find_all("h3")
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

[← Create a BeautifulSoup object to parse the HTML](08-create-a-beautifulsoup-object-to-parse-the-html.md) · [Up: contents](index.md) · [Convert the BeautifulSoup object to a lxml object →](10-convert-the-beautifulsoup-object-to-a-lxml-object.md)
