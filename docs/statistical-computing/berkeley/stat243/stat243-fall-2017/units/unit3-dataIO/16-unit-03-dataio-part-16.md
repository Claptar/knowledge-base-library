---
title: Unit 03 — dataIO Part 16 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 16 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_## this fails because node is not a standard list:_ countries <- **sapply** ( **xmlChildren** (loansNode), **function** (node) **xmlValue** (node$location$country))

**## Error in node$location: object of type ’externalptr’ is not subsettable**

XML documents have a tree structure with information at nodes. As above with HTML, one can use the _XPath_ language for navigating the tree and finding and extracting information from the node(s) of interest.

_xml2_ is a new package from RStudio for reading XML and HTML.

19

### **3.3 Reading JSON**

JSON files are structured as “attribute-value” pairs (aka “key-value” pairs), often with a hierarchical structure. Here’s a brief example:

{ "firstName": "John", "lastName": "Smith", "isAlive": true, "age": 25, "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" } ], "children": [], "spouse": null }

A set of key-value pairs is a named array and is placed inside braces (squiggly brackets). Note the nestedness of arrays within arrays (e.g., address within the overarching person array and the use of square brackets for unnamed arrays (i.e., vectors of information), as well as the use of different types: character strings, numbers, null, and (not shown) boolean/logical values. JSON and XML can be used in similar ways, but JSON is less verbose than XML.

We can read JSON into R using _fromJSON()_ in the _jsonlite_ package. Let’s play again with the Kiva data. The same data that we had worked with in XML format is also available in JSON format: http://api.kivaws.org/v1/loans/newest.json.

20

**library** (jsonlite) data <- **fromJSON** ("http://api.kivaws.org/v1/loans/newest.json") **names** (data)

---

[← Unit 03 — dataIO Part 15 —](15-unit-03-dataio-part-15.md) · [Up: contents](index.md) · [[1] "paging" "loans" class (data$loans) # nice! ## [1] "data.frame" →](17-1-paging-loans-class-data-loans-nice-1-data-frame.md)
