---
title: 4. Webscraping and working with HTML, XML, and JSON
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit2-dataTech.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Webscraping and working with HTML, XML, and JSON

**Source:** [`units/unit2-dataTech.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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
directly in the browser (e.g., in Firefox under the 3-lines "open menu"
symbol, see `Web Developer (or More Tools) -> Page Source` and in Chrome
`View -> Developer -> View Source`), or by downloading the webpage and
looking at it in an editor, although in some cases (such as the
nytimes.com case), what we might see is a lot of JavaScript.

One lesson here is not to write a lot of your own code to do something
that someone else has probably already written a package for. We'll use
the *rvest* package.

```r
library(rvest, quietly = TRUE)  # uses xml2
URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
html <- read_html(URL)
tbls <- html_table(html_elements(html, "table"))
sapply(tbls, nrow)
pop <- tbls[[1]]
head(pop)
```

(Caution here -- notice what format the columns are stored in...)

*read_html()* works by reading in the HTML as text and then parsing it
to build up a tree containing the HTML elements. Then *html_elements()*
finds the HTML tables and *html_table()* converts them to data frames.
rvest is part of the tidyverse, so it's often used with piping, e.g.,

```r
## Turns out that html_table can take the entire html doc as input
tbls <- URL |> read_html() |> html_table()
```

It's often useful to be able to extract the hyperlinks in an HTML
document. We'll find the link using [CSS
selectors](https://www.w3schools.com/cssref/css_selectors.asp), which
allow you to search for elements within HTML:

```r
URL <- "http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year"
## approach 1: search for elements with 'href' attribute
links <- read_html(URL) %>% html_elements("[href]") %>% html_attr('href')
## approach 2: search for HTML 'a' tags
links <- read_html(URL) %>% html_elements("a") %>% html_attr('href')
head(links, n = 10)
```

More generally, we may want to read an HTML document, parse it into its
components (i.e., the HTML elements), and navigate through the tree
structure of the HTML. Here we use the *XPath* language to specify
elements rather than CSS selectors. XPath can also be used for
navigating through XML documents.

```r
## find all 'a' elements that have attribute 'href'; then
## extract the 'href' attribute
links <- read_html(URL) %>% html_elements(xpath = "//a[@href]") %>%
    html_attr('href')
head(links)

## we can extract various information
listOfANodes <- read_html(URL) %>% html_elements(xpath = "//a[@href]")
listOfANodes %>% html_attr('href') %>% head(n = 10)
listOfANodes %>% html_name() %>% head(n = 10)
listOfANodes %>% html_text()  %>% head(n = 10)
```

Here's another example of extracting specific components of information
from a webpage (results not shown, since headlines will vary from day to
day).

```r
URL <- "https://www.nytimes.com"
headlines2 <- read_html(URL) %>% html_elements("h2") %>% html_text()
head(headlines2)
headlines3 <- read_html(URL) %>% html_elements("h3") %>% html_text()
head(headlines3)
```

## XML

XML is a markup language used to store data in self-describing (no
metadata needed) format, often with a hierarchical structure. It
consists of sets of elements (also known as nodes because they generally
occur in a hierarchical structure and therefore have parents, children,
etc.) with tags that identify/name the elements, with some similarity to
HTML. Some examples of the use of XML include serving as the underlying
format for Microsoft Office and Google Docs documents and for the KML
language used for spatial information in Google Earth.

Here's a brief example. The book with id attribute *bk101* is an
element; the author of the book is also an element that is a child
element of the book. The id attribute allows us to uniquely identify the
element.

```
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

We can read XML documents into R using `xml2::read_xml()` and then
manipulate it using other functions from the *xml2* package. Here's an
example of working with lending data from the Kiva lending non-profit.
You can see the XML format in a browser at

<http://api.kivaws.org/v1/loans/newest.xml>.

XML documents have a tree structure with information at nodes. As above
with HTML, one can use the *XPath* language for navigating the tree and
finding and extracting information from the node(s) of interest.

Here is some example code for extracting loan info from the Kiva data.
We'll first show the 'brute force' approach of working with the data as a
list and then the better approach of using XPath.

```r
library(xml2)
doc <- read_xml("https://api.kivaws.org/v1/loans/newest.xml")
data <- as_list(doc)
names(data)
names(data$response)
length(data$response$loans)
data$response$loans[[2]][c('name', 'activity',
                           'sector', 'location', 'loan_amount')]

## alternatively, extract only the 'loans' info (and use pipes)
loansNode <- doc %>% html_elements('loans')
loanInfo <- loansNode %>% xml_children() %>% as_list()
length(loanInfo)
names(loanInfo[[1]])
names(loanInfo[[1]]$location)

## suppose we only want the country locations of the loans (using XPath)
xml_find_all(loansNode, '//location//country')
xml_find_all(loansNode, '//location//country') %>% xml_text()

## or extract the geographic coordinates
xml_find_all(loansNode, '//location//geo/pairs')
```

## JSON

JSON files are structured as "attribute-value" pairs (aka "key-value"
pairs), often with a hierarchical structure. Here's a brief example:

```
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

A set of key-value pairs is a named array and is placed inside braces
(squiggly brackets). Note the nestedness of arrays within arrays (e.g.,
address within the overarching person array and the use of square
brackets for unnamed arrays (i.e., vectors of information), as well as
the use of different types: character strings, numbers, null, and (not
shown) boolean/logical values. JSON and XML can be used in similar ways,
but JSON is less *verbose* than XML.

We can read JSON into R using *fromJSON()* in the *jsonlite* package.
Let's play again with the Kiva data. The same data that we had worked
with in XML format is also available in JSON format:
<http://api.kivaws.org/v1/loans/newest.json>.

```r
library(jsonlite)
data <- fromJSON("http://api.kivaws.org/v1/loans/newest.json")
class(data)
names(data)
class(data$loans) # nice!
head(data$loans)

data$loans[1, 'location.geo.pairs'] # hmmm...
data$loans[1, 'location']
```

One disadvantage of JSON is that it is not set up to deal with missing
values, infinity, etc.

## Webscraping and web APIs

Here we'll see some examples of making requests over the Web to get
data. We'll use APIs to systematically query a website for information.
Ideally, but not always, the API will be documented. In many cases that
simply amounts to making an HTTP GET request, which is done by
constructing a URL.

The packages *RCurl* and *httr* are useful for a wide variety of such
functionality. Note that much of the functionality I describe below is
also possible within the shell using either *wget* or *curl*.

### Webscraping ethics and best practices

Webscraping is the process of extracting data from the web, either
directly from a website or using a web API (application programming
interface).

1.  **Should you webscrape?** In general, if we can avoid webscraping
    (particularly if there is not an API) and instead directly download
    a data file from a website, that is greatly preferred.

2.  **May you webscrape?** Before you set up any automated downloading
    of materials/data from the web you should make sure that what you
    are about to do is consistent with the rules provided by the
    website.

Some places to look for information on what the website allows are:

-   legal pages such as Terms of Service or Terms and Conditions on the
    website.

-   check the robots.txt file (e.g.,
    <https://scholar.google.com/robots.txt>) to see what a web crawler
    is allowed to do, and whether the site requires a particular delay
    between requests to the sites

-   potentially contact the site owner if you plan to scrape a large
    amount of data

Here are some links with useful information:

-   [A blog post overview on webscraping and
    robots.txt](http://feedproxy.google.com/~r/RBloggers/~3/RZGJ8Trv5Xw/?utm_source=feedburner&utm_medium=email)

-   [Blog post on webscraping
    ethics](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)

-   [Some information on how to understand a robots.txt
    file](https://www.promptcloud.com/blog/how-to-read-and-respect-robots-file)

Tips for when you make automated requests:

- When debugging code that processes the result of such a request, just run the request once, save (i.e., cache) the result, and then work on the processing code applied to the result. Don't make the same request over and over again.
- In many cases you will want to include a time delay between your
automated requests to a site, including if you are not actually crawling
a site but just want to automate a small number of queries.

### What is HTTP?

HTTP (hypertext transfer protocol) is a system for communicating
information from a server (i.e., the website of interest) to a client
(e.g., your laptop). The client sends a request and the server sends a
response.

When you go to a website in a browser, your browser makes an HTTP GET
request to the website. Similarly, when we did some downloading of html
from webpages above, we used an HTTP GET request.

Anytime the URL you enter includes parameter information after a question mark
(`www.somewebsite.com?param1=arg1&param2=arg2`), you are using an API.

The response to an HTTP request will include a status code, which can be
interpreted based on [this
information](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

The response will generally contain content in the form of text (e.g.,
HTML, XML, JSON) or raw bytes.

### APIs: REST- and SOAP-based web services

Ideally a web service documents their API (Applications Programming
Interface) that serves data or allows other interactions. REST and SOAP
are popular API standards/styles. Both REST and SOAP use HTTP requests;
we'll focus on REST as it is more common and simpler. When using REST, we access *resources*, which might be a Facebook
account or a database of stock quotes. The API will
(hopefully) document what information it expects from the user and will
return the result in a standard format (often a particular file format
rather than producing a webpage).

Often the format of the request is a URL (aka an endpoint) plus a query
string, passed as a GET request. Let's search for plumbers near
Berkeley, and we'll see the GET request, in the form:

<https://www.yelp.com/search?find_desc=plumbers&find_loc=Berkeley+CA&ns=1>

-   the query string begins with ?

-   there are one or more `Parameter=Argument` pairs

-   pairs are separated by &

-   \+ is used in place of each space


Let's see an example of accessing economic data from the
World Bank, using the [documentation for their API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information). Following the [API call structure](https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures), we can download (for example), data on various countries. The documentation indicates that our REST-based query can use either a URL structure or an argument-based structure.

```r
## Queries based on the documentation
api_url <- "http://api.worldbank.org/V2/incomeLevel/LIC/country"
api_args <- "http://api.worldbank.org/V2/country?incomeLevel=LIC"

## Generalizing a bit
req <- "http://api.worldbank.org/V2/country?incomeLevel=MIC&format=json"
data <- fromJSON(req)
## Be careful of data truncation/pagination
req <- "http://api.worldbank.org/V2/country?incomeLevel=MIC&format=json&per_page=1000"
data <- fromJSON(req)

## Programmatic control
baseURL <- "http://api.worldbank.org/V2/country"
group <- 'MIC'
format <- 'json'
args <- c(incomeLevel = group, format = format, per_page = 1000)
url <- paste0(baseURL, "?",
    paste(  paste(names(args), args, sep = "="),  collapse = "&"))

data <- fromJSON(url)
class(data)
length(data)
names(data)
head(data[[2]])
```

APIs can change and disappear. Last year the example above involved the World Bank's Climate Data API, which I can no longer find!


As another example, here we can see the [US Treasury Department API](https://fiscaldata.treasury.gov/api-documentation/), which allows us to construct queries for federal financial data.

The Nolan and Temple Lang book provides a number of examples of
different ways of authenticating with web services that control access
to the service.

Finally, some web services allow us to pass information to the service
in addition to just getting data or information. E.g., you can
programmatically interact with your Facebook, Dropbox, and Google Drive
accounts using REST based on HTTP POST, PUT, and DELETE requests.
Authentication is of course important in these contexts and some times
you would first authenticate with your login and password and receive a
"token". This token would then be used in subsequent interactions in the
same session.

I created your *github.berkeley.edu* accounts from Python by interacting
with the [GitHub API](https://docs.github.com/en/rest/reference/repos)
using the *requests* package.

### HTTP requests by deconstructing an (undocumented) API

In some cases an API may not be documented or we might be lazy and not
use the documentation. Instead we might deconstruct the queries a
browser makes and then mimic that behavior, in some cases having to
parse HTML output to get at data. Note that if the webpage changes even
a little bit, our carefully constructed query syntax may fail.

Let's look at some UN data (agricultural crop data). By going to\
<http://data.un.org/Explorer.aspx?d=FAO>, and clicking on "Crops", we'll
see a bunch of agricultural products with "View data" links. Click on
"apricots" as an example and you'll see a "Download" button that allows
you to download a CSV of the data. Let's select a range of years and
then try to download "by hand". Sometimes we can right-click on the link
that will download the data and directly see the URL that is being
accessed and then one can deconstruct it so that you can create URLs
programmatically to download the data you want.

In this case, we can't see the full URL that is being used because
there's some Javascript involved. Therefore, rather than looking at the
URL associated with a link we need to view the actual HTTP request sent
by our browser to the server. We can do this using features of the
browser (e.g., in Firefox see `Web Developer -> Network` and in Chrome
`View -> Developer -> Developer tools` and choose the `Network` tab) (or right-click on the
webpage and select `Inspect` and then `Network`). Based on this we can
see that an HTTP GET request is being used with a URL such as:\
<http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526;year:2012,2013,2014,2015,2016,2017&DataMartId=FAO&Format=csv&c=2,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc>.

We'e now able to easily download the data using that URL, which we can
fairly easily construct using string processing in bash, R, or Python,
such as this (here I just paste it together directly, but using more structured syntax
such as I used for the World Bank example would be better):

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
temp <- tempfile()  ## give name for a temporary file
download.file(url, temp)
dat <- read.csv(unzip(temp))  ## using a connection (see Section 2)

head(dat)
```

So, what have we achieved?

1. We have a reproducible workflow we can share with others (perhaps ourself in the future).

2. We can automate the process of downloading many such files.


### More details on HTTP requests

A more sophisticated way to do the download is to pass the request in a structured way with named input parameters. This request is easier to construct programmatically. Here what is returned is a zip file, which is represented in R as a sequence of “raw” bytes. We can use httr's GET(), followed by writing to disk and reading back in, as follows (for some reason knitr won't print the output...):

```r
library(httr)
output2 <- GET(baseURL, query = list(
               DataFilter = paste0("itemCode:", itemCode, ";year:", yrs),
               DataMartID = "FAO", Format = "csv", c = "2,3,4,5,6,7",
               s = "countryName:asc,elementCode:asc,year:desc"))
temp <- tempfile()  ## give name for a temporary file
writeBin(content(output2, 'raw'), temp)  ## write out as zip file
dat <- read.csv(unzip(temp))
head(dat)
```

In some cases we may need to send a lot of information as part of the
URL in a GET request. If it gets to be too long (e.g,, more than 2048
characters) many web servers will reject the request. Instead we may
need to use an HTTP POST request (POST requests are often used for
submitting web forms). A typical request would have syntax like this
search (using *RCurl*):

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

Unfortunately that specific search doesn't work because the server URL
and/or API seem to have changed. But it gives you an idea of what the
format would look like.

*httr* and *RCurl* can handle other kinds of HTTP requests such as PUT
and DELETE. Finally, some websites use cookies to keep track of users
and you may need to download a cookie in the first interaction with the
HTTP server and then send that cookie with later interactions. More
details are available in the Nolan and Temple Lang book.

### Packaged access to an API

For popular websites/data sources, a developer may have packaged up the
API calls in a user-friendly fashion for use from R, Python or other
software. For example there are Python (twitter) and R (twitteR)
packages for interfacing with Twitter via its API.

Here's some example code for Python (the Python package seems to be more
fully-featured than the R package). This looks up the US senators'
Twitter names and then downloads a portion of each of their timelines,
i.e., the time series of their tweets. Note that Twitter has limits on
how much one can download at once.

```python
import json
import twitter

---

[← 3. Output from R](04-3-output-from-r.md) · [Up: contents](index.md) · [You will need to set the following variables with your →](06-you-will-need-to-set-the-following-variables-with-your.md)
