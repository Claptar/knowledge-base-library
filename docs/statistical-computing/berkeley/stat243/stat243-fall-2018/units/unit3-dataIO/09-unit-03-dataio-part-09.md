---
title: Unit 03 — dataIO Part 09 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 09 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here’s another example of extracting specific components of information from a webpage.

URL <- "https://www.nytimes.com"

headlines <- **read_html** (URL) %>% **html_nodes** ("h2") %>% **html_text** () **head** (headlines)

13

We can explore the underlying HTML source in advance of writing our code by looking at the page source directly in the browser (e.g., in Firefox see Web Developer -> Page Source and in Chrome More tools -> Developer tools), or by downloading the webpage and looking at it in an editor, although in some cases (such as the nytimes.com case), what we might see is a lot of JavaScript.

### **3.2 XML**

XML is a markup language used to store data in self-describing (no metadata needed) format, often with a hierarchical structure. It consists of sets of elements (also known as nodes because they generally occur in a hierarchical structure and therefore have parents, children, etc.) with tags that identify/name the elements, with some similarity to HTML. Some examples of the use of XML include serving as the underlying format for Microsoft Office and Google Docs documents and for the KML language used for spatial information in Google Earth.

Here’s a brief example. The book with id attribute _bk101_ is an element; the author of the book is also an element that is a child element of the book. The id attribute allows us to uniquely identify the element.

<?xml version="1.0"?> <catalog>

<book id="bk101"> <author>Gambardella, Matthew</author> <title>XML Developer's Guide</title> <genre>Computer</genre> <price>44.95</price> <publish_date>2000-10-01</publish_date> <description>An in-depth look at creating applications with XML.</description> </book> <book id="bk102"> <author>Ralls, Kim</author> <title>Midnight Rain</title> <genre>Fantasy</genre> <price>5.95</price> <publish_date>2000-12-16</publish_date>

<description>A former architect battles corporate zombies, an evil </book> </catalog>

14

We can read XML documents into R using xml2::read_xml() and then manipulate it using other functions from the _xml2_ package. Here’s an example of working with lending data from the Kiva lending non-profit. You can see the XML format in a browser at

http://api.kivaws.org/v1/loans/newest.xml.

XML documents have a tree structure with information at nodes. As above with HTML, one can use the _XPath_ language for navigating the tree and finding and extracting information from the node(s) of interest. Here is some example code for extracting loan info from the Kiva data.

**library** (xml2) doc <- **read_xml** ("https://api.kivaws.org/v1/loans/newest.xml") data <- **as_list** (doc) **names** (data) ## [1] "response" **names** (data$response) ## [1] "paging" "loans" **length** (data$response$loans) ## [1] 20 data$response$loans[[2]][ **c** ('name', 'activity', 'sector', 'location', 'loan_amount')] ## $name ## $name[[1]] ## [1] "Lilian" ## ## ## $activity ## $activity[[1]] ## [1] "Cereals" ## ## ## $sector ## $sector[[1]] ## [1] "Food"

15

---

[← Unit 03 — dataIO Part 08 —](08-unit-03-dataio-part-08.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 10 — →](10-unit-03-dataio-part-10.md)
