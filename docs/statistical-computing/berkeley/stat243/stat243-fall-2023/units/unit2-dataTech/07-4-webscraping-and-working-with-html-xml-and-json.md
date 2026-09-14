---
title: 4. Webscraping and working with HTML, XML, and JSON
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit2-dataTech.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Webscraping and working with HTML, XML, and JSON

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit2-dataTech.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

The book *XML and Web Technologies for Data Sciences with R* by Deb
Nolan (UCB Stats faculty) and Duncan Temple Lang (UCB Stats PhD alumnus
and UC Davis Stats faculty) provides extensive information about getting
and processing data off of the web, including interacting with web
services such as REST and SOAP and programmatically handling
authentication.

Here are some UNIX command-line tools to help in webscraping and working
with files in formats such as JSON, XML, and HTML:
<http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html>.

We'll cover a few basic examples in this section, but HTML and XML
formatting and navigating the structure of such pages in great detail is
beyond the scope of what we can cover. The key thing is to see the main
concepts and know that the tools exist so that you can learn how to use
them if faced with such formats.

## Reading HTML

HTML (Hypertext Markup Language) is the standard markup language used
for displaying content in a web browser. In simple webpages (ignoring
the more complicated pages that involve Javascript), what you see in
your browser is simply a *rendering* (by the browser) of a text file containing HTML.

However, instead of rendering the HTML in a browser, we might want to
use code to extract information from the HTML.

Let's see a brief example of reading in HTML tables.

Note that before doing any coding, it can be helpful to look at the raw
HTML source code for a given page. We can explore the underlying HTML
source in advance of writing our code by looking at the page source
directly in the browser (e.g., in Firefox under the 3-lines (hamburger) "open menu"
symbol, see `Web Developer (or More Tools) -> Page Source` and in Chrome
`View -> Developer -> View Source`), or by downloading the webpage and
looking at it in an editor, although in some cases (such as the
nytimes.com case), what we might see is a lot of JavaScript.

One lesson here is not to write a lot of your own code to do something
that someone else has probably already written a package for. We'll use
the `BeautifulSoup4` package.

```python
import requests
from bs4 import BeautifulSoup as bs

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response = requests.get(URL)
html = response.content

---

[← As of Python 3.6, put the variable names in directly.](06-as-of-python-3-6-put-the-variable-names-in-directly.md) · [Up: contents](index.md) · [Create a BeautifulSoup object to parse the HTML →](08-create-a-beautifulsoup-object-to-parse-the-html.md)
