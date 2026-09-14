---
title: 4. Working with information on the web
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Working with information on the web

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit2-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In this section, we'll see some ways to programmatically interact
with information on the web, focusing on downloading information, but also showing how we can upload as well. As part of this we'll see some details about file formats commonly used in this
context.

The main theme of this section is using tools to make it easy to interact with the web
and with information in formats such as HTML, XML, JSON, and YAML.

## Reading HTML

We'll cover a few basic examples in this section, but HTML and XML
formatting and navigating the structure of such pages in great detail is
beyond the scope of what we can cover. The key thing is to see the main
concepts and know that the tools exist so that you can learn how to use
them if faced with such formats.

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
import io
import requests
from bs4 import BeautifulSoup as bs

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

## Wikipedia requires information about the bot/program making an automated request.
user_agent = "stat243_educational_bot/0.1 (paciorek@berkeley.edu)"
headers = {'User-Agent': user_agent}
response = requests.get(URL, headers=headers)
html = response.content

---

[← This works as of Python 3.6.](06-this-works-as-of-python-3-6.md) · [Up: contents](index.md) · [Create a BeautifulSoup object to parse the HTML →](08-create-a-beautifulsoup-object-to-parse-the-html.md)
