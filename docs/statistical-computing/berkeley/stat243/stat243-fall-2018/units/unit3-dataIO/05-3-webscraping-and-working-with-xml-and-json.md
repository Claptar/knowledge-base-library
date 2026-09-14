---
title: 3 Webscraping and working with XML and JSON
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Webscraping and working with XML and JSON

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The new (well, as of 2015) book _XML and Web Technologies for Data Sciences with R_ by Deb Nolan (UCB Stats faculty) and Duncan Temple Lang (UCB Stats PhD alumnus and UC Davis Stats faculty) provides extensive information about getting and processing data off of the web, including interacting with web services such as REST and SOAP and programmatically handling authentication.

Here are some UNIX command-line tools to help in webscraping and working with files in formats such as JSON, XML, and HTML: http://jeroenjanssens.com/2013/09/19/seven-commandline-tools-for-data-science.html.

We’ll cover a few basic examples in this section, but HTML and XML formatting and navigating the structure of such pages is beyond the scope of what we can cover in detail. The key thing is to know that the tools exist so that you can learn how to use them if faced with such formats.

10

### **3.1 Reading HTML**

Let’s see a brief example of reading in HTML tables. One lesson here is not to write a lot of your own code to do something that someone else has probably already written a package for. We’ll use the _rvest_ package (you can also see usage of the now-unmaintained _xml_ package in the code file for this unit).

**library** (rvest) _# uses xml2 ## Loading required package: xml2 ## ## Attaching package: ’rvest’ ## The following object is masked from ’package:readr’: ## ## guess_encoding_ URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" html <- **read_html** (URL) tbls <- **html_table** ( **html_nodes** (html, "table")) **sapply** (tbls, nrow) ## [1] 1 240 12 pop <- tbls[[2]] **head** (pop) ## Rank Country(or dependent territory) Population ## 1 1 China[Note 2] 1,393,860,000 ## 2 2 India[Note 3] 1,336,480,000 ## 3 3 United States[Note 4] 327,765,000 ## 4 4 Indonesia 265,015,300 ## 5 5 Brazil 209,533,000 ## 6 6 Pakistan 201,872,000 ## Date % of worldpopulation ## 1 September 3, 2018 18.2% ## 2 September 3, 2018 17.5% ## 3 September 3, 2018 4.29% ## 4 July 1, 2018 3.47% ## 5 September 3, 2018 2.74%

11

---

[← Unit 03 — dataIO Part 04 —](04-unit-03-dataio-part-04.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 06 — →](06-unit-03-dataio-part-06.md)
