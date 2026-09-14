---
title: '"Philippines" "Philippines"'
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# "Philippines" "Philippines"

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

countries <- **sapply** ( **xmlChildren** (loansNode), **function** (node)

**xmlValue** (node$location$country)) _# node is not a standard list..._

**## Error in node$location: object of type ’externalptr’ is not subsettable**

XML documents have a tree structure with information at nodes. As above with HTML, one can use the _XPath_ language for navigating the tree and finding and extracting information from the node(s) of interest.

_xml2_ is a new package from RStudio for reading XML and HTML.

18

### **3.3 Reading JSON**

JSON files are structured as “attribute-value” pairs (aka “key-value” pairs), often with a hierarchical structure. Here’s a brief example:

{ "firstName": "John", "lastName": "Smith", "isAlive": true, "age": 25, "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" } ], "children": [], "spouse": null }

A set of key-value pairs is a named array and is placed inside braces (squiggly brackets). Note the nestedness of arrays within arrays (e.g., address within the overarching person array and the use of square brackets for unnamed arrays (i.e., vectors of information), as well as the use of different types: character strings, numbers, null, and (not shown) boolean/logical values. JSON and XML can be used in similar ways, but JSON is less verbose than XML.

We can read JSON into R using _fromJSON()_ in the _jsonlite_ package. Let’s play again with the Kiva data. The same data that we had worked with in XML format is also available in JSON format: http://api.kivaws.org/v1/loans/newest.json.

19

**library** (jsonlite) _## ## Attaching package: ’jsonlite’ ## ## The following object is masked from ’package:utils’: ## ## View_ data <- **fromJSON** ("http://api.kivaws.org/v1/loans/newest.json") **names** (data) ## [1] "paging" "loans" **class** (data$loans) _# nice!_ ## [1] "data.frame" **head** (data$loans)

|##|id||name langua|ges|status|
|---|---|---|---|---|---|
|## 1|941854||Nzara|en|fundraising|
|## 2|941853||Alice|en|fundraising|
|## 3|941852||Zeqirja|en|fundraising|
|## 4|941922|Regina|Lisbeth<br>es,|en|fundraising|
|## 5|942082|Mw|anamisi|en|fundraising|
|## 6|942114|Fe|lismina|en|fundraising|
|##|funded|_amount|basket_amount|imag|e.id|
|## 1||0|0|196|9681|
|## 2||0|0|196|6858|
|## 3||0|0|196|8299|
|## 4||0|0|196|9839|
|## 5||0|0|197|0081|
|## 6||0|0|195|9349|
|##|image.|template|_id|act|ivity<br>sector|
|## 1|||1<br>But|cher|Shop<br>Food|
|## 2|||1|Fa|rming Agriculture|
|## 3|||1||Dairy Agriculture|


20

|##|4|1|Retail|Retail|
|---|---|---|---|---|
|##|5|1 Fruits|& Vegetables|Food|
|##|6|1|Agriculture Agr|iculture|
|##|||||
|##|1||||
|##|2|to buy certified fertili|zers for top dres|sing her nappier grass in orde|
|##|3||||
|##|4|||to invest|
|##|5||||
|##|6||||
|##||location.country_code lo|cation.country lo|cation.town|
|##|1|KE|Kenya|Tiribe|
|##|2|KE|Kenya|Kisii|
|##|3|XK|Kosovo|<NA>|
|##|4|SV|El Salvador|<NA>|
|##|5|KE|Kenya|Tiribe|
|##|6|TL|Timor-Leste|Oe-cusse|
|##||location.geo.level<br>loc|ation.geo.pairs||
|##|1|town|1 38||
|##|2|town<br>-0.6|83333 34.766667||
|##|3|country|42.583333 21||
|##|4|country 13.83|3333 -88.916667||
|##|5|town|1 38||
|##|6|town<br>-|8.833333 125.75||
|##||location.geo.type partne|r_id<br>pos|ted_date|
|##|1|point|164 2015-09-04T0|1:30:03Z|
|##|2|point|133 2015-09-04T0|1:30:02Z|
|##|3|point|240 2015-09-04T0|1:20:05Z|
|##|4|point|81 2015-09-04T0|1:20:03Z|
|##|5|point|164 2015-09-04T0|1:10:05Z|
|##|6|point|243 2015-09-04T0|1:10:05Z|
|##||planned_expiration_date|loan_amount borro|wer_count|
|##|1|2015-10-04T01:30:03Z|200|1|
|##|2|2015-10-04T01:30:02Z|250|1|
|##|3|2015-10-04T01:20:04Z|2050|1|
|##|4|2015-10-04T01:20:03Z|500|1|


21

|##|5|2015-10-04T01:10:05Z<br>200|1|
|---|---|---|---|
|##|6|2015-10-04T01:10:05Z<br>600|1|
|##||lender_count bonus_credit_eligibility||
|##|1|0<br>TRUE||
|##|2|0<br>FALSE||
|##|3|0<br>TRUE||
|##|4|0<br>TRUE||
|##|5|0<br>TRUE||
|##|6|0<br>TRUE||
|##|||tags|
|##|1||NULL|
|##|2||NULL|
|##|3|#FirstLoan, #Animals, #Parent, #IncomeProdu|cingDurableAsset|
|##|4||NULL|
|##|5||NULL|
|##|6||NULL|
|##||themes||
|##|1|NULL||
|##|2|NULL||
|##|3|NULL||
|##|4|Conflict Zones||
|##|5|NULL||
|##|6|Underfunded Areas||


One disadvantage of JSON is that it is not set up to deal with missing values, infinity, etc.

### **3.4 Using web APIs to get data**

Here we’ll see briefly some examples of making requests over the Web to get data. We’ll see simple http requests, as well as use of RESTful and SOAP APIs. The package _RCurl_ is the main package useful for a wide variety of such functionality. Note that all of the functionality I describe below is also possible within bash using either _wget_ or _curl_ .

We’ve already seen some basic downloading of html from webpages, which uses the HTTP request GET.

22

#### **3.4.1 HTTP requests**

First as was noted as a sidenote earlier, we can use _RCurl_ to access secure http pages (i.e., pages that use https). This may not be possible or may be more difficult when using base R functionality. Here _getURLContent()_ makes an HTTP GET request.

URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" **library** (RCurl)

_## Loading required package: bitops_ html <- **getURLContent** (URL) tbls <- **readHTMLTable** (html)

Sometime specific information can be downloaded simply by constructing a static URL. Suppose we want to get data off of Yahoo Finance. By going to

http://finance.yahoo.com/q/hp?s=DATA+Historical+Prices, we can enter a date range and a company and see the HTML output, which we could download and extract the data from using tools seen in this Unit. But often we’ll see a download link, and if we look at the URL associated with that link, we can see it looks like this:

http://real-chart.finance.yahoo.com/table.csv?s=AAPL&d=7&e=30&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv where the stuff at the end specifies inputs passed to the server separated by ‘&’, in this case the date range information. So we could more easily download the data using that URL, which we can fairly easily construct using string processing in bash, R, or Python (more in Unit 4). A more sophisticated way to do the download is to pass the request in a structured way with named input parameters. This request is easier to construct programmatically.

txt <- **getForm** ("http://ichart.finance.yahoo.com/table.csv", s = "AAPL", a = 2, b = 27, c = 2014, d = 7, e = 30, f = 2015, g = "d", ignore = ".csv") aapl <- **read.csv** ( **textConnection** (txt)) **head** (aapl)

---

[← Unit 03 — Rinput Part 16 —](16-unit-03-rinput-part-16.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 18 — →](18-unit-03-rinput-part-18.md)
