---
title: Unit 03 — Rinput Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 19 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

More generally, rather than looking at the URL associated with a link we may need to view the actual HTTP request sent by our browser to the server. We can do this using features of the browser (e.g., Ctrl-Shift-q in Firefox or More Tools -> Developer Tools -> Network in Chrome)

In some cases we may need to send a lot of information as part of the URL in a GET request. If it gets to be too long (e.g„ more than 2048 characters) many web servers will reject the request. Instead we may need to use an HTTP POST request. A typical request would have syntax like this, supposing that the inputs were named _start-year_ and _end-year._

URL <- "http://somewhere.com" txt <- **postForm** (URL, "start-year" = "1995", "end-year" = "2005", style = "post")

result <- **readHTMLTable** (txt, header = TRUE)

RCurl can handle other kinds of HTTP requests such as PUT and DELETE. Finally, some websites use cookies to keep track of users and you may need to download a cookie in the first interaction with the HTTP server and then send that cookie with later interactions. More details are available in the Nolan and Temple Lang book.

Finally, an alternative to RCurl is the _httr_ package, which has a separate function for each type of HTTP request, e.g., GET, POST, PUT, DELETE.

#### **3.4.2 REST- and SOAP-based web services**

While webscraping with requests such as just described can work well, it was a bit convoluted. We basically needed to deconstruct the queries a browser makes and then mimic that behavior, in some cases having to parse HTML output to get at data. If the webpage changes even a little bit, our carefully constructed query syntax may fail. An alternative is to use a web service specifically designed to serve data or allow other interactions via an Applications Programming Interface

24

(API). Both REST and SOAP use HTTP requests; we’ll focus on REST as it is more common and simpler.

When using REST, we access _resources_ , which might be a Facebook account or a database of stock quotes. The resource may return information in the form of an HTML file or JSON, CSV or something else. REST generally uses XML or JSON as the format for the request and what is returned.

Let’s see an example of accessing climate model output data from the World Bank. The API is documented here: http://data.worldbank.org/developers/climate-data-api. Following that documentation we can download monthly average precipitation data for 1980-1999 for the US (ISO3 code ‘USA’).

times <- **c** (1980, 1999) countryCode <- 'USA'

baseURL <- "http://climatedataapi.worldbank.org/climateweb/rest/v1/country" type <- "mavg" var <- "pr"

data <- **read.csv** ( **paste** (baseURL, type, var, times[1], times[2], **paste0** (countryCode, '.csv'), sep = '/')) **head** (data)

---

[← Unit 03 — Rinput Part 18 —](18-unit-03-rinput-part-18.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 20 — →](20-unit-03-rinput-part-20.md)
