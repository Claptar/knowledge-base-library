---
title: '[1] "paging" "loans" class (data$loans) # nice! ## [1] "data.frame"'
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "paging" "loans" class (data$loans) # nice! ## [1] "data.frame"

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**head** (data$loans)

|##|id|n|ame|langua|ges<br>status|
|---|---|---|---|---|---|
|##|1 1364518|Solomboahir|ana|fr,|en fundraising|
|##|2 1363041|Gulrukh|sor|ru,|en fundraising|
|##|3 1364504|Elisab|eth|fr,|en fundraising|
|##|4 1364508|Papa Sa|mba|fr,|en fundraising|
|##|5 1365895 Maria|Auxiliadora Gr|oup|es,|en fundraising|
|##|6 1365892|Luis Alfr|edo|es,|en fundraising|
|##|funded_amount|basket_amount|imag|e.id||
|##|1<br>0|25|261|8711||
|##|2<br>0|0|261|6908||
|##|3<br>0|0|261|8683||
|##|4<br>0|0|261|8693||
|##|5<br>0|0|262|0475||
|##|6<br>0|0|262|0465||
|##|image.templat|e_id|act|ivity|sector|
|##|1|1||Pigs|Agriculture|
|##|2|1||Cafe|Food|
|##|3|1 Fruits & V|eget|ables|Food|
|##|4|1<br>Cleaning|Ser|vices|Services|
|##|5|1<br>Cloth|ing|Sales|Clothing|
|##|6|1|C|attle|Agriculture|
|##||||||
|##|1||||to purchase|
|##|2||||to buy a toaster oven and exp|
|##|3|to purc|hase|fruit|s and vegetables to be resold at|


21

|##|4|to purchase an automobile pressure washer, mats,|
|---|---|---|
|##|5|to buy assorted clot|
|##|6 purchase cattle to ra|ise and to provide another source of income when h|
|##|location.country_code|location.country|
|##|1<br>MG|Madagascar|
|##|2<br>TJ|Tajikistan|
|##|3<br>SN|Senegal|
|##|4<br>SN|Senegal|
|##|5<br>PY|Paraguay|
|##|6<br>SV|El Salvador|
|##|location.town loc|ation.geo.level|
|##|1<br>Talata|town|
|##|2<br>Vahdat|town|
|##|3<br><NA>|country|
|##|4<br><NA>|country|
|##|5<br>Coronel Oviedo|town|
|##|6 Ciudad El Triunfo|town|
|##|location.geo.pairs|location.geo.type partner_id|
|##|1<br>-20 47|point<br>359|
|##|2<br>39 71|point<br>63|
|##|3<br>14 -14|point<br>108|
|##|4<br>14 -14|point<br>108|
|##|5<br>-25.416667 -56.45|point<br>58|
|##|6 13.833333 -88.916667|point<br>199|
|##|posted_date|planned_expiration_date|
|##|1 2017-09-01T15:30:05Z|2017-10-01T15:30:05Z|
|##|2 2017-09-01T15:30:02Z|2017-10-01T15:30:02Z|
|##|3 2017-09-01T15:20:03Z|2017-10-01T15:20:03Z|
|##|4 2017-09-01T15:20:03Z|2017-10-01T15:20:03Z|
|##|5 2017-09-01T15:20:03Z|2017-10-01T15:20:02Z|
|##|6 2017-09-01T15:10:06Z|2017-10-01T15:10:05Z|
|##|loan_amount borrower_|count lender_count|
|##|1<br>150|1<br>0|
|##|2<br>575|1<br>0|
|##|3<br>200|1<br>0|
|##|4<br>200|1<br>0|


22

|##|5|4025|||20<br>0|
|---|---|---|---|---|---|
|##|6|1000|||1<br>0|
|##||bonus_credit|_eligib|ility|tags|
|##|1|||FALSE|#Animals, #Parent|
|##|2|||FALSE|user_favorite|
|##|3|||FALSE|NULL|
|##|4|||FALSE|NULL|
|##|5|||TRUE|#Woman Owned Biz|
|##|6|||TRUE|#Animals|
|##|||themes|||
|##|1||NULL|||
|##|2||NULL|||
|##|3||NULL|||
|##|4||NULL|||
|##|5|Vulnerable|Groups|||
|##|6|Earth Day Ca|mpaign|||


One disadvantage of JSON is that it is not set up to deal with missing values, infinity, etc.

### **3.4 Using web APIs to get data**

Here we’ll see briefly some examples of making requests over the Web to get data. We’ll see simple http requests, as well as use APIs to systematically query a website for information based on a documented interface. The packages _RCurl_ and _httr_ are useful for a wide variety of such functionality. Note that much of the functionality I describe below is also possible within bash using either _wget_ or _curl_ .

We’ve already seen some basic downloading of html from webpages, which uses the HTTP request GET.

#### **3.4.1 HTTP requests**

Here _getURLContent()_ makes an HTTP GET request.

URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" **library** (RCurl) _## Loading required package: bitops_

23

html <- **getURLContent** (URL) tbls <- **readHTMLTable** (html)

Sometime specific information can be downloaded simply by constructing a static URL. Let’s return to the agricultural crop data that is involved in problem set 1. By going to http://data.un.org/Explorer.aspx?d=FAO, and clicking on “Crops”, we’ll see a bunch of agricultural products with “View data” links. Click on “apricots” as an example and you’ll see a “Download” button that allows you to download a CSV of the data. Let’s select a range of years and then try to download “by hand”. Sometimes we can right-click on the link that will download the data and directly see the URL that is being accessed and then one can deconstruct it so that you can create URLs programmatically to download the data you want.

In this case, we can’t see the full URL that is being used. More generally, rather than looking at the URL associated with a link we may need to view the actual HTTP request sent by our browser to the server. We can do this using features of the browser (e.g., More -> Developer -> Network in Firefox or More Tools -> Developer Tools -> Network in Chrome). Based on this we can see that an HTTP GET request is being used with a URL such as: http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526;year:2003,2004,2005,2006,2007&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc The stuff at the end of the URL specifies inputs passed to the server separated by ‘&’, in this case relating to the itemCode, dates, output format, etc. So we could more easily download the data using that URL, which we can fairly easily construct using string processing in bash, R, or Python, such as this:

_## example URL: ##"http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter= ##itemCode:526;year:2003,2004,2005,2006,2007&DataMartId=FAO& ##Format=csv&c=2,3,4,5,6,7&s=countryName:asc"_ itemCode <- 526 baseURL <- "http://data.un.org/Handlers/DownloadHandler.ashx" yrs <- **paste** ( **as.character** (2003:2007), collapse = ",") filter <- **paste0** ("?DataFilter=itemCode:", itemCode, ";year:", yrs) args1 <- "&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&" args2 <- "s=countryName:asc,elementCode:asc,year:desc" url <- **paste0** (baseURL, filter, args1, args2) _## if the website provided a CSV we could just do this: ## apricots <- read.csv(url) ## but it zips the file_

24

temp <- **tempfile** () _## give name for a temporary file_ **download.file** (url, temp) dat <- **read.csv** ( **unzip** (temp))

**head** (dat)

|##|Country.or.Area|Element.Code|Element Year|
|---|---|---|---|
|## 1|Afghanistan|31 Area|Harvested 2007|
|## 2|Afghanistan|31 Area|Harvested 2006|
|## 3|Afghanistan|31 Area|Harvested 2005|
|## 4|Afghanistan|31 Area|Harvested 2004|
|## 5|Afghanistan|31 Area|Harvested 2003|
|## 6|Afghanistan|41|Yield 2007|
|##|Unit Value Val|ue.Footnotes||
|## 1|Ha<br>3400|F||
|## 2|Ha<br>8030|||
|## 3|Ha<br>5200|F||
|## 4|Ha<br>5200|F||
|## 5|Ha<br>7007|||
|## 6|Hg/Ha 72891|Fc||


A more sophisticated way to do the download is to pass the request in a structured way with named input parameters. This request is easier to construct programmatically. Here what is returned is a zip file, which is represented in R as a sequence of “raw” bytes. I’m having trouble getting the output of _getForm()_ sent to a file, but we can use httr’s _GET()_ , followed by writing to disk and reading back in:

output1 <- **getForm** (baseURL, DataFilter = **paste0** ("itemCode:", itemCode, ";year:", yrs), DataMartID = "FAO", Format = "csv", c = "2,3,4,5,6,7", s = "countryName:asc,elementCode:asc,year:desc") **class** (output1) ## [1] "raw" _## not sure how to get output1 into a file_ **library** (httr)

25

|_##_|
|---|
|_## Attaching package:_<br>_’httr’_|
|_## The following object is masked from ’package:curl’:_|
|_##_|
|_##_<br>_handle_reset_<br>|
|output2 <- **GET**(baseURL, query = **list**(|
|DataFilter = **paste0**("itemCode:", itemCode, ";year:", yrs),|
|DataMartID = "FAO", Format = "csv", c = "2,3,4,5,6,7",|
|s = "countryName:asc,elementCode:asc,year:desc"))<br><br>|
|temp <- **tempfile**()<br>_## give name for a temporary file_|
|**writeBin**(**content**(output2, 'raw'), temp)<br>_## write out as zip file_|
|dat <- **read.csv**(**unzip**(temp))|
|**head**(dat)<br><br><br>|
|##<br>Country.or.Area Element.Code<br>Element Year|
|## 1<br>Afghanistan<br>31 Area Harvested 2007|
|## 2<br>Afghanistan<br>31 Area Harvested 2006|
|## 3<br>Afghanistan<br>31 Area Harvested 2005|
|## 4<br>Afghanistan<br>31 Area Harvested 2004|
|## 5<br>Afghanistan<br>31 Area Harvested 2003|
|## 6<br>Afghanistan<br>41<br>Yield 2007|
|##<br>Unit Value Value.Footnotes|
|## 1<br>Ha<br>3400<br>F|
|## 2<br>Ha<br>8030|
|## 3<br>Ha<br>5200<br>F|
|## 4<br>Ha<br>5200<br>F|
|## 5<br>Ha<br>7007|
|## 6 Hg/Ha 72891<br>Fc|


In some cases we may need to send a lot of information as part of the URL in a GET request. If it gets to be too long (e.g„ more than 2048 characters) many web servers will reject the request. Instead we may need to use an HTTP POST request. A typical request would have syntax like this, supposing that the inputs were named _start-year_ and _end-year._

26

URL <- "http://somewhere.com" txt <- **postForm** (URL, "start-year" = "1995", "end-year" = "2005", style = "post")

result <- **readHTMLTable** (txt, header = TRUE)

RCurl can handle other kinds of HTTP requests such as PUT and DELETE. Finally, some websites use cookies to keep track of users and you may need to download a cookie in the first interaction with the HTTP server and then send that cookie with later interactions. More details are available in the Nolan and Temple Lang book.

Finally, an alternative to RCurl is the _httr_ package, which has a separate function for each type of HTTP request, e.g., GET, POST, PUT, DELETE.

#### **3.4.2 APIs: REST- and SOAP-based web services**

While webscraping with requests such as just described can work well, it was a bit convoluted. We basically needed to deconstruct the queries a browser makes and then mimic that behavior, in some cases having to parse HTML output to get at data. If the webpage changes even a little bit, our carefully constructed query syntax may fail. An alternative is to use a web service specifically designed to serve data or allow other interactions via an Applications Programming Interface (API). Both REST and SOAP use HTTP requests; we’ll focus on REST as it is more common and simpler.

When using REST, we access _resources_ , which might be a Facebook account or a database of stock quotes. The resource may return information in the form of an HTML file or JSON, CSV or something else. REST generally uses XML or JSON as the format for the request and what is returned.

Let’s see an example of accessing climate model output data from the World Bank. The API is documented here: http://data.worldbank.org/developers/climate-data-api. Following that documentation we can download monthly average precipitation predictions for 2080-2099 for the US (ISO3 code ‘USA’) based on global climate model simulations. In this case what the World Bank refers to as the REST-based query is simply constructing a straightforward URL, but one can also construct a query based on arguments passed as part of the URL, in similar fashion to as seen in the previous section.

times <- **c** (2080, 2099) countryCode <- 'USA'

baseURL <- "http://climatedataapi.worldbank.org/climateweb/rest/v1/country" type <- "mavg"

27

var <- "pr"

|data|<- **read.**|**csv**(**paste**|(baseURL,|type, var|, times[|1], times[2],|
|---|---|---|---|---|---|---|
||||**paste0**(c|ountryCode|, '.csv'|), sep = '/'))|
|**head**(|data)||||||
|##||GCM var|scenario|from_year|to_year|Jan|
|## 1|bccr_b|cm2_0<br>pr|a2|2080|2099|67.03573|
|## 2|bccr_b|cm2_0<br>pr|b1|2080|2099|62.36411|
|## 3|cccma_cg|cm3_1<br>pr|a2|2080|2099|73.05678|
|## 4|cccma_cg|cm3_1<br>pr|b1|2080|2099|68.13736|
|## 5|cnr|m_cm3<br>pr|a2|2080|2099|72.18374|
|## 6|cnr|m_cm3<br>pr|b1|2080|2099|69.87911|
|##|Feb|Mar|Apr|May|Jun|Jul|
|## 1|60.34472|68.55613|69.73249|70.75057|68.87670|75.50839|
|## 2|57.25621|65.37839|66.83145|71.42986|66.70454|76.21705|
|## 3|65.88258|69.07827|70.52308|71.27610|71.40891|71.73378|
|## 4|56.80470|64.87122|64.26042|65.26155|65.63476|68.85459|
|## 5|64.47102|76.22999|79.40222|94.16236|93.20071|92.61398|
|## 6|59.47017|70.12903|80.61524|92.51666|92.54483|96.00988|
|##|Aug|Sep|Oct|Nov|Dec||
|## 1|79.16541|76.60718|79.72601|72.12957|71.83717||
|## 2|76.50563|81.48503|73.44661|67.69188|62.61851||
|## 3|71.16824|72.37070|72.17842|85.11507|77.58228||
|## 4|68.02093|66.02112|70.71792|77.58472|77.31110||
|## 5|87.12436|87.24258|86.20070|77.22606|78.49393||
|## 6|91.05730|88.87449|82.81388|70.25031|71.83962||


The Nolan and Temple Lang book provides a number of examples of different ways of authenticating with web services that control access to the service.

Finally, some web services allow us to pass information to the service in addition to just getting data or information. E.g., you can programmatically interact with your Facebook, Dropbox, and Google Drive accounts using REST based on HTTP POST, PUT, and DELETE. Authentication is of course important in these contexts and some times you would first authenticate with your login and password and receive a “token”. This token would then be used in subsequent interactions in the same session.

28

#### **3.4.3 Packaged access to an API**

For popular websites/data sources, a developer may have packaged up the API calls in a userfriendly fashion for use from R, Python or other software. For example there are Python (twitter) and R (twitteR) packages for interfacing with Twitter via its API.

Here’s some example code for Python (the Python package seems to be more fully-featured than the R package). This looks up the US senators’ Twitter names and then downloads a portion of each of their timelines, i.e., the time series of their tweets. Note that Twitter has limits on how much one can download at once.

**import** json **import** twitter _# You will need to set the following variables with your # personal information. To do this you will need to create # a personal account on Twitter (if you don’t already have # one). Once you’ve created an account, create a new # application here: # https://dev.twitter.com/apps # # You can manage your applications here: # https://apps.twitter.com/ # # Select your application and then under the section labeled # "Key and Access Tokens", you will find the information needed # below. Keep this information private._ CONSUMER_KEY = "" CONSUMER_SECRET = "" OAUTH_TOKEN = "" OAUTH_TOKEN_SECRET = "" auth = twitter.oauth. **OAuth** (OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) api = twitter. **Twitter** (auth=auth) _# get the list of senators_ senators = api.lists. **members** (owner_screen_name="gov", slug="us-senate",

29

count=100) with open("senators-list.json", "w") **as** f: json. **dump** (senators, f, indent=4, sort_keys= **True** ) _# get all the senators’ timelines_ names = [d["screen_name"] **for** d **in** senators["users"]] timelines = [api.statuses. **user_timeline** (screen_name=name, count = 500) **for** name **in** names] with open("timelines.json", "w") **as** f: json. **dump** (timelines, f, indent=4, sort_keys= **True** )

---

[← Unit 03 — dataIO Part 16 —](16-unit-03-dataio-part-16.md) · [Up: contents](index.md) · [4 Output from R →](18-4-output-from-r.md)
