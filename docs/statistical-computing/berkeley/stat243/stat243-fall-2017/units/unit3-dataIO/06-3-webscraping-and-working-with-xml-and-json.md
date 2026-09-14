---
title: 3 Webscraping and working with XML and JSON
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Webscraping and working with XML and JSON

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The new (well, as of 2015) book _XML and Web Technologies for Data Sciences with R_ by Deb Nolan (UCB Stats faculty) and Duncan Temple Lang (UCB Stats PhD alumnus and UC Davis Stats faculty) provides extensive information about getting and processing data off of the web, including interacting with web services such as REST and SOAP and programmatically handling authentication.

Here are some UNIX command-line tools to help in webscraping and working with files in formats such as JSON, XML, and HTML: http://jeroenjanssens.com/2013/09/19/seven-commandline-tools-for-data-science.html.

10

We’ll cover a few basic examples in this section, but HTML and XML formatting and navigating the structure of such pages is beyond the scope of what we can cover in detail. The key thing is to know that the tools exist so that you can learn how to use them if faced with such formats.

### **3.1 Reading HTML**

Let’s see a brief example of reading in HTML tables. One lesson here is not to write a lot of your own code to do something that someone else has probably already written a package for. Unfortunately, there are some issues with dealing with https-based websites that we need to work around, rather than directly using _readHTMLTable()_ as can be done with http-based websites. So we need to use _url()_ to get the HTML via https and then use the XML package functionality for parsing the HTML.

**library** (XML) _## Loading required package: methods_ **library** (curl) URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" html <- **readLines** (URL) _## alternative ## library(RCurl); html <- getURLContent(URL)_ tbls <- **readHTMLTable** (html) **sapply** (tbls, nrow) ## NULL NULL ## 243 12 pop <- **readHTMLTable** (html, which = 1) **head** (pop) ## Rank Country\n(or dependent territory) Population ## 1 1 China[Note 2] 1,385,170,000 ## 2 2 India 1,320,660,000 ## 3 3 United States[Note 3] 325,686,000 ## 4 4 Indonesia 261,890,900 ## 5 5 Pakistan 208,760,000 ## 6 6 Brazil 207,950,000

11

---

[← Unit 03 — dataIO Part 05 —](05-unit-03-dataio-part-05.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 07 — →](07-unit-03-dataio-part-07.md)
