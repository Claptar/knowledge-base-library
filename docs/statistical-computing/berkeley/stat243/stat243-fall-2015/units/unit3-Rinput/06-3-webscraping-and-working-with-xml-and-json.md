---
title: 3 Webscraping and working with XML and JSON
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Webscraping and working with XML and JSON

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The new book _XML and Web Technologies for Data Sciences with R_ by Deb Nolan (UCB Stats faculty) and Duncan Temple Lang (UCB Stats PhD alumnus) provides extensive information about getting and processing data off of the web, including interacting with web services such as REST and SOAP and programmatically handling authentication.

Here are some UNIX command-line tools to help in webscraping and working with files in formats such as JSON, XML, and HTML: http://jeroenjanssens.com/2013/09/19/seven-commandline-tools-for-data-science.html.

We’ll cover a few basic examples in this section, but HTML and XML formatting and navigating the structure of such pages is beyond the scope of what we can cover in detail. The key thing is to know that the tools exist so that you can learn how to use them if faced with such formats.

### **3.1 Reading HTML**

Let’s see a brief example of reading in HTML tables. One lesson here is not to write a lot of your own code to do something that someone else has probably already written a package for. Unfortunately, there are some issues with dealing with https that we need to work around, rather than directly using _readHTMLTable()_ as can be done with http. So we need to use _curl()_ to get the HTML via https and then use the XML package functionality for parsing the HTML.

**library** (XML) _## Loading required package: methods_ **library** (curl) URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" html <- **readLines** ( **curl** (URL)) _# alternative # library(RCurl); html <- getURLContent(URL)_ tbls <- **readHTMLTable** (html)

9

---

[← Unit 03 — Rinput Part 05 —](05-unit-03-rinput-part-05.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 07 — →](07-unit-03-rinput-part-07.md)
