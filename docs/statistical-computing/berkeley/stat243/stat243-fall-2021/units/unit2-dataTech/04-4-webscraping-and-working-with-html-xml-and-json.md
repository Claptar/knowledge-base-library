---
title: 4 Webscraping and working with HTML, XML, and JSON
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit2-dataTech.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit2-dataTech.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Webscraping and working with HTML, XML, and JSON

The book *XML and Web Technologies for Data Sciences with R* by Deb Nolan (UCB Stats faculty)
and Duncan Temple Lang (UCB Stats PhD alumnus and UC Davis Stats faculty) provides extensive information about getting and processing data off of the web, including interacting with web
services such as REST and SOAP and programmatically handling authentication.

Here are some UNIX command-line tools to help in webscraping and working with files in
formats such as JSON, XML, and HTML: http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html.

We’ll cover a few basic examples in this section, but HTML and XML formatting and navigating the structure of such pages in great detail is beyond the scope of what we can cover. The key
thing is to see the main concepts and know that the tools exist so that you can learn how to use
them if faced with such formats.

## 4.1 Reading HTML

HTML (Hypertext Markup Language) is the standard markup language used for displaying content in a web browser. In simple webpages (ignoring the more complicated pages that involve
Javascript), what you see in your browser is simply a rendering of a text file containing HTML.
However, instead of rendering the HTML in a browser, we might want to use code to extract
information from the HTML.

Let’s see a brief example of reading in HTML tables.

Note that before doing any coding, it can be helpful to look at the raw HTML source code for a
given page. We can explore the underlying HTML source in advance of writing our code by looking at the page source directly in the browser (e.g., in Firefox under the 3-lines “open menu” symbol, see Web Developer (or More Tools) -> Page Source and in Chrome View
-> Developer -> View Source), or by downloading the webpage and looking at it in an
editor, although in some cases (such as the nytimes.com case), what we might see is a lot of
JavaScript.

One lesson here is not to write a lot of your own code to do something that someone else has
probably already written a package for. We’ll use the *rvest* package.

```r
library(rvest) # uses xml2
##
## Attaching package: ’rvest’
## The following object is masked from ’package:readr’:
##
## guess_encoding
URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
html <- read_html(URL)
tbls <- html_table(html_elements(html, "table"))
sapply(tbls, nrow)
## [1] 242 12
pop <- tbls[[1]]
head(pop)
## # A tibble: 6 x 8
## Rank `Country or depe~ Region Population `% of world`
## <chr> <chr> <chr> <chr> <chr>
## 1 â World World 7,892,069~ 100%
## 2 1 China (more) Asia 1,411,778~ 17.9%
## 3 2 India (more) Asia 1,381,270~ 17.5%
## 4 3 United States (m~ Ameri~ 332,277,3~ 4.21%
## 5 4 Indonesia (more) Asia 271,350,0~ 3.44%
## 6 5 Pakistan (more) Asia 225,200,0~ 2.85%
## # ... with 3 more variables: Date <chr>, ...
```

*read_html()* works by reading in the HTML as text and then parsing it to build up a tree containing the HTML elements. Then *html_nodes()* finds the HTML tables and *html_table()* converts
them to data frames. *rvest* is part of the tidyverse, so it’s often used with piping, e.g.,

```r
library(magrittr)
## Turns out that html_table can take the entire html doc as input
tbls <- URL %>% read_html() %>% html_table()
```

It’s often useful to be able to extract the hyperlinks in an HTML document. We’ll find the link
using *CSS selectors*, which allow you to search for elements within HTML:

```r
URL <- "http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year"
## approach 1: search for elements with 'href' attribute
links <- read_html(URL) %>% html_elements("[href]") %>% html_attr('href')
## approach 2: search for HTML 'a' tags
links <- read_html(URL) %>% html_elements("a") %>% html_attr('href')
head(links, n = 10)
## [1] "?C=N;O=D" "?C=M;O=A"
## [3] "?C=S;O=A" "?C=D;O=A"
## [5] "/pub/data/ghcn/daily/" "1763.csv.gz"
## [7] "1764.csv.gz" "1765.csv.gz"
## [9] "1766.csv.gz" "1767.csv.gz"
```

More generally, we may want to read an HTML document, parse it into its components (i.e.,
the HTML elements), and navigate through the tree structure of the HTML. Here we use the *XPath*
language to specify elements rather than CSS selectors. XPath can also be used for navigating
through XML documents.

```r
## find all 'a' elements that have attribute 'href'; then
## extract the 'href' attribute
links <- read_html(URL) %>% html_elements(xpath = "//a[@href]") %>%
html_attr('href')
head(links)
## [1] "?C=N;O=D" "?C=M;O=A"
## [3] "?C=S;O=A" "?C=D;O=A"
## [5] "/pub/data/ghcn/daily/" "1763.csv.gz"
## we can extract various information
listOfANodes <- read_html(URL) %>% html_elements(xpath = "//a[@href]")
listOfANodes %>% html_attr('href') %>% head(n = 10)
## [1] "?C=N;O=D" "?C=M;O=A"
## [3] "?C=S;O=A" "?C=D;O=A"
## [5] "/pub/data/ghcn/daily/" "1763.csv.gz"
## [7] "1764.csv.gz" "1765.csv.gz"
## [9] "1766.csv.gz" "1767.csv.gz"
listOfANodes %>% html_name() %>% head(n = 10)
## [1] "a" "a" "a" "a" "a" "a" "a" "a" "a" "a"
listOfANodes %>% html_text() %>% head(n = 10)
## [1] "Name" "Last modified"
## [3] "Size" "Description"
## [5] "Parent Directory" "1763.csv.gz"
## [7] "1764.csv.gz" "1765.csv.gz"
## [9] "1766.csv.gz" "1767.csv.gz"
```

Here’s another example of extracting specific components of information from a webpage (results not shown, since headlines will vary from day to day).

```r
URL <- "https://www.nytimes.com"
headlines2 <- read_html(URL) %>% html_elements("h2") %>% html_text()
head(headlines2)
headlines3 <- read_html(URL) %>% html_elements("h3") %>% html_text()
head(headlines3)
```

## 4.2 XML

XML is a markup language used to store data in self-describing (no metadata needed) format,
often with a hierarchical structure. It consists of sets of elements (also known as nodes because
they generally occur in a hierarchical structure and therefore have parents, children, etc.) with
tags that identify/name the elements, with some similarity to HTML. Some examples of the use of
XML include serving as the underlying format for Microsoft Office and Google Docs documents
and for the KML language used for spatial information in Google Earth.

Here’s a brief example. The book with id attribute *bk101* is an element; the author of the book
is also an element that is a child element of the book. The id attribute allows us to uniquely identify
the element.

```xml
<?xml version="1.0"?>
<catalog>
<book id="bk101">
<author>Gambardella, Matthew</author>
<title>XML Developer's Guide</title>
<genre>Computer</genre>
<price>44.95</price>
<publish_date>2000-10-01</publish_date>
<description>An in-depth look at creating applications with XML.</description>
</book>
<book id="bk102">
<author>Ralls, Kim</author>
<title>Midnight Rain</title>
<genre>Fantasy</genre>
<price>5.95</price>
<publish_date>2000-12-16</publish_date>
<description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
</book>
</catalog>
```

We can read XML documents into R using `xml2::read_xml()` and then manipulate it
using other functions from the *xml2* package. Here’s an example of working with lending data
from the Kiva lending non-profit. You can see the XML format in a browser at
http://api.kivaws.org/v1/loans/newest.xml.

XML documents have a tree structure with information at nodes. As above with HTML, one
can use the XPath language for navigating the tree and finding and extracting information from the
node(s) of interest. Here is some example code for extracting loan info from the Kiva data.

```r
library(xml2)
doc <- read_xml("https://api.kivaws.org/v1/loans/newest.xml")
data <- as_list(doc)
names(data)
## [1] "response"
names(data$response)
## [1] "paging" "loans"
length(data$response$loans)
## [1] 20
data$response$loans[[2]][c('name', 'activity',
'sector', 'location', 'loan_amount')]
## $name
## $name[[1]]
## [1] "Ablaba Eva"
##
##
## $activity
## $activity[[1]]
## [1] "Sewing"
##
##
## $sector
## $sector[[1]]
## [1] "Services"
##
##
## $location
## $location$country_code
## $location$country_code[[1]]
## [1] "TG"
##
##
## $location$country
## $location$country[[1]]
## [1] "Togo"
##
##
## $location$town
## $location$town[[1]]
## [1] "baguida"
##
##
## $location$geo
## $location$geo$level
## $location$geo$level[[1]]
## [1] "town"
##
##
## $location$geo$pairs
## $location$geo$pairs[[1]]
## [1] "6.160584 1.31352"
##
##
## $location$geo$type
## $location$geo$type[[1]]
## [1] "point"
##
##
##
##
## $loan_amount
## $loan_amount[[1]]
## [1] "150"
## alternatively, extract only the 'loans' info (and use pipes)
loansNode <- doc %>% html_elements('loans')
loanInfo <- loansNode %>% xml_children() %>% as_list()
length(loanInfo)
## [1] 20
names(loanInfo[[1]])
## [1] "id"
## [2] "name"
## [3] "description"
## [4] "status"
## [5] "funded_amount"
## [6] "basket_amount"
## [7] "image"
## [8] "activity"
## [9] "sector"
## [10] "use"
## [11] "location"
## [12] "partner_id"
## [13] "posted_date"
## [14] "planned_expiration_date"
## [15] "loan_amount"
## [16] "borrower_count"
## [17] "lender_count"
## [18] "bonus_credit_eligibility"
## [19] "tags"
names(loanInfo[[1]]$location)
## [1] "country_code" "country" "town"
## [4] "geo"
## suppose we only want the country locations of the loans (using XPath)
xml_find_all(loansNode, '//location//country')
## {xml_nodeset (20)}
## [1] <country>Togo</country>
## [2] <country>Togo</country>
## [3] <country>El Salvador</country>
## [4] <country>Guatemala</country>
## [5] <country>Haiti</country>
## [6] <country>El Salvador</country>
## [7] <country>El Salvador</country>
## [8] <country>Georgia</country>
## [9] <country>El Salvador</country>
## [10] <country>El Salvador</country>
## [11] <country>El Salvador</country>
## [12] <country>El Salvador</country>
## [13] <country>Kenya</country>
## [14] <country>Indonesia</country>
## [15] <country>Kenya</country>
## [16] <country>Kenya</country>
## [17] <country>El Salvador</country>
## [18] <country>El Salvador</country>
## [19] <country>El Salvador</country>
## [20] <country>Honduras</country>
xml_find_all(loansNode, '//location//country') %>% xml_text()
## [1] "Togo" "Togo" "El Salvador"
## [4] "Guatemala" "Haiti" "El Salvador"
## [7] "El Salvador" "Georgia" "El Salvador"
## [10] "El Salvador" "El Salvador" "El Salvador"
## [13] "Kenya" "Indonesia" "Kenya"
## [16] "Kenya" "El Salvador" "El Salvador"
## [19] "El Salvador" "Honduras"
## or extract the geographic coordinates
xml_find_all(loansNode, '//location//geo/pairs')
## {xml_nodeset (20)}
## [1] <pairs>6.160584 1.31352</pairs>
## [2] <pairs>6.160584 1.31352</pairs>
## [3] <pairs>13.833333 -88.916667</pairs>
## [4] <pairs>14.944972 -91.108924</pairs>
## [5] <pairs>37.55 22.083333</pairs>
## [6] <pairs>13.833333 -88.916667</pairs>
## [7] <pairs>13.341347 -88.275314</pairs>
## [8] <pairs>42.605475 42.000951</pairs>
## [9] <pairs>13.833333 -88.916667</pairs>
## [10] <pairs>13.833333 -88.916667</pairs>
## [11] <pairs>13.833333 -88.916667</pairs>
## [12] <pairs>13.833333 -88.916667</pairs>
## [13] <pairs>-0.583333 35.183333</pairs>
## [14] <pairs>-6.178056 106.63</pairs>
## [15] <pairs>-1.307941 36.714256</pairs>
## [16] <pairs>-1.307941 36.714256</pairs>
## [17] <pairs>13.341347 -88.275314</pairs>
## [18] <pairs>13.833333 -88.916667</pairs>
## [19] <pairs>13.833333 -88.916667</pairs>
## [20] <pairs>14.033333 -86.583333</pairs>
```

## 4.3 JSON

JSON files are structured as “attribute-value” pairs (aka “key-value” pairs), often with a hierarchical structure. Here’s a brief example:

```json
{
"firstName": "John",
"lastName": "Smith",
"isAlive": true,
"age": 25,
"address": {
"streetAddress": "21 2nd Street",
"city": "New York",
"state": "NY",
"postalCode": "10021-3100"
},
"phoneNumbers": [
{
"type": "home",
"number": "212 555-1234"
},
{
"type": "office",
"number": "646 555-4567"
}
],
"children": [],
"spouse": null
}
```

A set of key-value pairs is a named array and is placed inside braces (squiggly brackets). Note
the nestedness of arrays within arrays (e.g., address within the overarching person array and the use
of square brackets for unnamed arrays (i.e., vectors of information), as well as the use of different
types: character strings, numbers, null, and (not shown) boolean/logical values. JSON and XML
can be used in similar ways, but JSON is less verbose than XML.

We can read JSON into R using *fromJSON()* in the *jsonlite* package. Let’s play again with
the Kiva data. The same data that we had worked with in XML format is also available in JSON
format: http://api.kivaws.org/v1/loans/newest.json.

```r
library(jsonlite)
data <- fromJSON("http://api.kivaws.org/v1/loans/newest.json")
class(data)
## [1] "list"
names(data)
## [1] "paging" "loans"
class(data$loans) # nice!
## [1] "data.frame"
head(data$loans)
## id name languages status
## 1 2233588 Sogninde fr, en fundraising
## 2 2233590 Ablaba Eva fr, en fundraising
## 3 2233155 Maria Consuelo es, en fundraising
## 4 2233167 Sacpulupense Group es, en fundraising
## 5 2233592 Elisemene fr, en fundraising
## 6 2233154 Ada Yessenia es, en fundraising
## funded_amount basket_amount image.id
## 1 0 0 3242990
## 2 0 0 4400807
## 3 0 0 4400045
## 4 0 0 4400078
## 5 0 0 3766325
## 6 0 0 4400042
## image.template_id activity sector
## 1 1 Used Clothing Clothing
## 2 1 Sewing Services
## 3 1 General Store Retail
## 4 1 Textiles Arts
## 5 1 Beverages Food
## 6 1 Fish Selling Food
## use
## 1 to buy 2 bundles of second-hand clothing.
## 2 to buy 10 pagnes [traditional clothes].
## 3 to buy drinks and other staple food products wholesale.
## 4 to purchase a variety of thread.
## 5 to increase her stock of soft drinks.
## 6 to buy fresh fish to distribute to her customers.
## location.country_code location.country
## 1 TG Togo
## 2 TG Togo
## 3 SV El Salvador
## 4 GT Guatemala
## 5 HT Haiti
## 6 SV El Salvador
## location.town
## 1 baguida
## 2 baguida
## 3 <NA>
## 4 Chichicastenango, Departamento El Quiche
## 5 Croix-des-Bouquets
## 6 <NA>
## location.geo.level location.geo.pairs
## 1 town 6.160584 1.31352
## 2 town 6.160584 1.31352
## 3 country 13.833333 -88.916667
## 4 town 14.944972 -91.108924
## 5 town 37.55 22.083333
## 6 country 13.833333 -88.916667
## location.geo.type partner_id posted_date
## 1 point 296 2021-08-30T15:50:58Z
## 2 point 296 2021-08-30T15:50:58Z
## 3 point 167 2021-08-30T15:50:55Z
## 4 point 55 2021-08-30T15:50:04Z
## 5 point 442 2021-08-30T15:30:15Z
## 6 point 167 2021-08-30T15:30:10Z
## planned_expiration_date loan_amount borrower_count
## 1 2021-09-29T15:50:58Z 200 1
## 2 2021-09-29T15:50:58Z 150 1
## 3 2021-09-29T15:50:55Z 500 1
## 4 2021-09-29T15:50:03Z 3000 8
## 5 2021-09-29T15:30:15Z 775 1
## 6 2021-09-29T15:30:10Z 1000 1
## lender_count bonus_credit_eligibility tags
## 1 0 FALSE NULL
## 2 0 FALSE NULL
## 3 0 TRUE NULL
## 4 0 TRUE NULL
## 5 0 FALSE NULL
## 6 0 TRUE NULL
## themes
## 1 NULL
## 2 NULL
## 3 Vulnerable Groups
## 4 NULL
## 5 NULL
## 6 NULL
data$loans[1, 'location.geo.pairs'] # hmmm...
## NULL
data$loans[1, 'location']
## country_code country town geo.level
## 1 TG Togo baguida town
## geo.pairs geo.type
## 1 6.160584 1.31352 point
```

One disadvantage of JSON is that it is not set up to deal with missing values, infinity, etc.

## 4.4 Webscraping and web APIs

Here we’ll see some examples of making requests over the Web to get data. We’ll use APIs to
systematically query a website for information. Ideally, but not always, the API will be documented. In many cases that simply amounts to making an HTTP GET request, which is done by
constructing a URL.

The packages *RCurl* and *httr* are useful for a wide variety of such functionality. Note that much
of the functionality I describe below is also possible within bash using either *wget* or *curl*.

### 4.4.1 Webscraping ethics and best practices

Webscraping is the process of extracting data from the web, either directly from a website or using
a web API (application programming interface).

1. **Should you webscrape?** In general, if we can avoid webscraping (particularly if there is not
an API) and instead directly download a data file from a website, that is greatly preferred.

2. **May you webscrape?** Before you set up any automated downloading of materials/data
from the web you should make sure that what you are about to do is consistent with the rules
provided by the website.

Some places to look for information on what the website allows are:

• legal pages such as Terms of Service or Terms and Conditions on the website.

• check the robots.txt file (e.g., https://scholar.google.com/robots.txt) to see what a web crawler
is allowed to do, and whether the site requires a particular delay between requests to the sites

• potentially contact the site owner if you plan to scrape a large amount of data

Here are some links with useful information:

• A blog post overview on webscraping and robots.txt

• Blog post on webscraping ethics

• Some information on how to understand a robots.txt file

In many cases you will want to include a time delay between your automated requests to a site,
including if you are not actually crawling a site but just want to automate a small number of queries.

### 4.4.2 What is HTTP?

HTTP (hypertext transfer protocol) is a system for communicating information from a server (i.e.,
the website of interest) to a client (e.g., your laptop). The client sends a request and the server
sends a response.

When you go to a website in a browser, your browser makes an HTTP GET request to the
website. Similarly, when we did some downloading of html from webpages above, we used an
HTTP GET request.

Anytime the URL you enter includes 'param' information (www.somewebsite.com?param=arg),
you are using an API.

The response to an HTTP request will include a status code, which can be interpreted based on
this information.

The response will generally contain content in the form of text (e.g., HTML, XML, JSON) or
raw bytes.

### 4.4.3 APIs: REST- and SOAP-based web services

Ideally a web service documents their API (Applications Programming Interface) that serves data
or allows other interactions. REST and SOAP are popular API standards/styles. Both REST and
SOAP use HTTP requests; we’ll focus on REST as it is more common and simpler. The API
will (hopefully) document what information it expects from the user and will return the result in a
standard format (e.g., a particular file format rather than producing a webpage).

When using REST, we access *resources*, which might be a Facebook account or a database of
stock quotes. The resource may return information in the form of an HTML file or JSON, CSV or
something else.

Often the format of the request is a URL (aka an endpoint) plus a query string, passed as a GET
request. Let’s search for plumbers near Berkeley, and we’ll see the GET request, in the form:
https://www.yelp.com/search?find_desc=plumbers&find_loc=Berkeley+CA&ns=1

• the query string begins with ?

• there are one or more Parameter=Argument pairs

• pairs are separated by &

• + is used in place of each space

We don’t always get HTML back - try searching for “Purple Rain” at *apple.com*. What format do
you get back?

Let’s see an example of accessing climate model output data from the World Bank. The API is
documented by following some links from here: http://datahelpdesk.worldbank.org/knowledgebase.
Following that documentation we can download monthly average precipitation predictions for
2080-2099 for the US (ISO3 code ‘USA’) based on global climate model simulations. In this
case our REST-based query is simply constructing a straightforward URL.

```r
times <- c(2080, 2099)
countryCode <- 'USA'
baseURL <- "http://climatedataapi.worldbank.org/climateweb/rest/v1/country"
##" http://climatedataapi.worldbank.org/climateweb/rest/v1/country"
type <- "mavg"
var <- "pr"
data <- read.csv(paste(baseURL, type, var, times[1], times[2],
paste0(countryCode, '.csv'), sep = '/'))
head(data)
## GCM var scenario from_year to_year Jan
## 1 bccr_bcm2_0 pr a2 2080 2099 67.03573
## 2 bccr_bcm2_0 pr b1 2080 2099 62.36411
## 3 cccma_cgcm3_1 pr a2 2080 2099 73.05678
## 4 cccma_cgcm3_1 pr b1 2080 2099 68.13736
## 5 cnrm_cm3 pr a2 2080 2099 72.18374
## 6 cnrm_cm3 pr b1 2080 2099 69.87911
## Feb Mar Apr May Jun Jul
## 1 60.34472 68.55613 69.73249 70.75057 68.87670 75.50839
## 2 57.25621 65.37839 66.83145 71.42986 66.70454 76.21705
## 3 65.88258 69.07827 70.52308 71.27610 71.40891 71.73378
## 4 56.80470 64.87122 64.26042 65.26155 65.63476 68.85459
## 5 64.47102 76.22999 79.40222 94.16236 93.20071 92.61398
## 6 59.47017 70.12903 80.61524 92.51666 92.54483 96.00988
## Aug Sep Oct Nov Dec
## 1 79.16541 76.60718 79.72601 72.12957 71.83717
## 2 76.50563 81.48503 73.44661 67.69188 62.61851
## 3 71.16824 72.37070 72.17842 85.11507 77.58228
## 4 68.02093 66.02112 70.71792 77.58472 77.31110
## 5 87.12436 87.24258 86.20070 77.22606 78.49393
## 6 91.05730 88.87449 82.81388 70.25031 71.83962
```

## 4.4.4 HTTP requests by deconstructing an (undocumented) API

As another example, here we can see the Kiva API, which allows us to construct queries on the
Kiva data that we saw some of earlier.

The Nolan and Temple Lang book provides a number of examples of different ways of authenticating with web services that control access to the service.

Finally, some web services allow us to pass information to the service in addition to just getting data or information. E.g., you can programmatically interact with your Facebook, Dropbox,
and Google Drive accounts using REST based on HTTP POST, PUT, and DELETE requests. Authentication is of course important in these contexts and some times you would first authenticate
with your login and password and receive a “token”. This token would then be used in subsequent
interactions in the same session.

I created your github.berkeley.edu accounts from Python by interacting with the Github API
using the *requests* package.

### 4.4.4 HTTP requests by deconstructing an (undocumented) API

In some cases an API may not be documented or we might be lazy and not use the documentation.
Instead we might deconstruct the queries a browser makes and then mimic that behavior, in some
cases having to parse HTML output to get at data. Note that if the webpage changes even a little
bit, our carefully constructed query syntax may fail.

Let’s look at some UN data (agricultural crop data). By going to
http://data.un.org/Explorer.aspx?d=FAO, and clicking on “Crops”, we’ll see a bunch of agricultural
products with “View data” links. Click on “apricots” as an example and you’ll see a “Download”
button that allows you to download a CSV of the data. Let’s select a range of years and then try
to download “by hand”. Sometimes we can right-click on the link that will download the data and
directly see the URL that is being accessed and then one can deconstruct it so that you can create
URLs programmatically to download the data you want.

In this case, we can’t see the full URL that is being used because there’s some Javascript involved. Therefore, rather than looking at the URL associated with a link we need to view the
actual HTTP request sent by our browser to the server. We can do this using features of the
browser (e.g., in Firefox see Web Developer -> Network and in Chrome More tools
-> Developer tools -> Network) (or right-click on the webpage and select Inspect
and then Network). Based on this we can see that an HTTP GET request is being used with a
URL such as:

http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526;year:2012,2013,2014,2015,2016,2017&DataMartId=FAO&Format=csv&c=2,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc.

We’e now able to easily download the data using that URL, which we can fairly easily construct
using string processing in bash, R, or Python, such as this:

```r
## example URL:
## http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526;
##year:2012,2013,2014,2015,2016,2017&DataMartId=FAO&Format=csv&c=2,4,5,6,7&
##s=countryName:asc,elementCode:asc,year:desc
itemCode <- 526
baseURL <- "http://data.un.org/Handlers/DownloadHandler.ashx"
yrs <- paste(as.character(2012:2017), collapse = ",")
filter <- paste0("?DataFilter=itemCode:", itemCode, ";year:", yrs)
args1 <- "&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&"
args2 <- "s=countryName:asc,elementCode:asc,year:desc"
url <- paste0(baseURL, filter, args1, args2)
## if the website provided a CSV we could just do this:
## apricots <- read.csv(url)
## but it zips the file
temp <- tempfile() ## give name for a temporary file
download.file(url, temp)
dat <- read.csv(unzip(temp)) ## using a connection (see Section 2)
head(dat)
## Country.or.Area Element.Code Element Year Unit
## 1 Afghanistan 5312 Area harvested 2017 ha
## 2 Afghanistan 5312 Area harvested 2016 ha
## 3 Afghanistan 5312 Area harvested 2015 ha
## 4 Afghanistan 5312 Area harvested 2014 ha
## 5 Afghanistan 5312 Area harvested 2013 ha
## 6 Afghanistan 5312 Area harvested 2012 ha
## Value Value.Footnotes
## 1 13413 Im
## 2 8595
## 3 9116
## 4 9005
## 5 9005
## 6 8350
```

```r
library(httr)
##
## Attaching package: ’httr’
## The following object is masked from ’package:curl’:
##
## handle_reset
output2 <- GET(baseURL, query = list(
DataFilter = paste0("itemCode:", itemCode, ";year:", yrs),
DataMartID = "FAO", Format = "csv", c = "2,3,4,5,6,7",
s = "countryName:asc,elementCode:asc,year:desc"))
temp <- tempfile() ## give name for a temporary file
writeBin(content(output2, 'raw'), temp) ## write out as zip file
dat <- read.csv(unzip(temp))
head(dat)
## Country.or.Area Element.Code Element Year Unit
## 1 Afghanistan 5312 Area harvested 2017 ha
## 2 Afghanistan 5312 Area harvested 2016 ha
## 3 Afghanistan 5312 Area harvested 2015 ha
## 4 Afghanistan 5312 Area harvested 2014 ha
## 5 Afghanistan 5312 Area harvested 2013 ha
## 6 Afghanistan 5312 Area harvested 2012 ha
## Value Value.Footnotes
## 1 13413 Im
## 2 8595
## 3 9116
## 4 9005
## 5 9005
## 6 8350
```

In some cases we may need to send a lot of information as part of the URL in a GET request.
If it gets to be too long (e.g., more than 2048 characters) many web servers will reject the request.
Instead we may need to use an HTTP POST request (POST requests are often used for submitting
web forms). A typical request would have syntax like this search (using *RCurl*):

```r
if(url.exists('http://www.wormbase.org/db/searches/advanced/dumper')) {
x = postForm('http://www.wormbase.org/db/searches/advanced/dumper',
species="briggsae",
list="",
flank3="0",
flank5="0",
feature="Gene Models",
dump = "Plain TEXT",
orientation = "Relative to feature",
relative = "Chromsome",
DNA ="flanking sequences only",
.cgifields = paste(c("feature", "orientation", "DNA",
"dump","relative"), collapse=", "))
}
```

Unfortunately that specific search doesn’t work because the server URL and/or API seem to
have changed. But it gives you an idea of what the format would look like.

*httr* and *RCurl* can handle other kinds of HTTP requests such as PUT and DELETE. Finally,
some websites use cookies to keep track of users and you may need to download a cookie in the
first interaction with the HTTP server and then send that cookie with later interactions. More
details are available in the Nolan and Temple Lang book.

### 4.4.5 Packaged access to an API

For popular websites/data sources, a developer may have packaged up the API calls in a user-friendly fashion for use from R, Python or other software. For example there are Python (*twitter*)
and R (*twitteR*) packages for interfacing with Twitter via its API.

Here’s some example code for Python (the Python package seems to be more fully-featured
than the R package). This looks up the US senators’ Twitter names and then downloads a portion
of each of their timelines, i.e., the time series of their tweets. Note that Twitter has limits on how
much one can download at once.

```python
import json
import twitter
# You will need to set the following variables with your
# personal information. To do this you will need to create
# a personal account on Twitter (if you don't already have
# one). Once you've created an account, create a new
# application here:
# https://dev.twitter.com/apps
#
# You can manage your applications here:
# https://apps.twitter.com/
#
# Select your application and then under the section labeled
# "Key and Access Tokens", you will find the information needed
# below. Keep this information private.
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)
api = twitter.Twitter(auth=auth)
# get the list of senators
senators = api.lists.members(owner_screen_name="gov", slug="us-senate", count=100)
# get all the senators' timelines
names = [d["screen_name"] for d in senators["users"]]
timelines = [api.statuses.user_timeline(screen_name=name, count = 500)
for name in names]
# save information out to JSON
with open("senators-list.json", "w") as f:
json.dump(senators, f, indent=4, sort_keys=True)
with open("timelines.json", "w") as f:
json.dump(timelines, f, indent=4, sort_keys=True)
```

### 4.4.6 Accessing dynamic pages

Some websites dynamically change in reaction to the user behavior. In these cases you need a tool
that can mimic the behavior of a human interacting with a site. Some options are:

• *selenium* (and the *RSelenium* wrapper for R) is a popular tool for doing this.

• *splash* (and the *splashr* wrapper for R) is another approach.

• *htmlunit* is another tool for this.

---

[← 3 Output from R](03-3-output-from-r.md) · [Up: contents](index.md) · [5 File and string encodings →](05-5-file-and-string-encodings.md)
