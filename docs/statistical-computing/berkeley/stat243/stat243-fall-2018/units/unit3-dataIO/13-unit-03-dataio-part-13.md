---
title: Unit 03 — dataIO Part 13 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 13 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

17

_## suppose we only want the country locations of the loans (using XPath)_ **xml_find_all** (loansNode, '//location//country') %>% **xml_text** ()

|##|[1]|"Guatemala"|"Kenya"|"Kenya"|"Kenya"|
|---|---|---|---|---|---|
|##|[5]|"Kenya"|"Kenya"|"Guatemala"|"Kenya"|
|##|[9]|"Kenya"|"Ecuador"|"Kenya"|"Tajikistan"|
|##|[13]|"Pakistan"|"Kenya"|"Kenya"|"Kenya"|
|##|[17]|"Kenya"|"Lebanon"|"Colombia"|"Kenya"|
|_## _|_or ex_|_tract the ge_|_ographic coo_|_rdinates_||
|**xml**|**_find**|**_all**(loansNo|de, '//locat|ion//geo/pairs'|)|


|##|{xml_nodeset (20)}|
|---|---|
|##|[1] <pairs>15.483483 -91.03707</pairs>|
|##|[2] <pairs>0.566667 34.566667</pairs>|
|##|[3] <pairs>-0.499328 37.278484</pairs>|
|##|[4] <pairs>-0.368897 35.286286</pairs>|
|##|[5] <pairs>-0.283333 36.066667</pairs>|
|##|[6] <pairs>-0.368897 35.286286</pairs>|
|##|[7] <pairs>15.055357 -91.228958</pairs>|
|##|[8] <pairs>0.232555 37.941375</pairs>|
|##|[9] <pairs>0.232555 37.941375</pairs>|
|##|[10] <pairs>0.815069 -77.716593</pairs>|
|##|[11] <pairs>0.232555 37.941375</pairs>|
|##|[12] <pairs>39 71</pairs>|
|##|[13] <pairs>31.549722 74.343611</pairs>|
|##|[14] <pairs>-0.1 34.75</pairs>|
|##|[15] <pairs>0.103073 35.176372</pairs>|
|##|[16] <pairs>-0.333333 37.65</pairs>|
|##|[17] <pairs>-0.1 34.75</pairs>|
|##|[18] <pairs>33.557069 35.372948</pairs>|
|##|[19] <pairs>6.477755 -74.4088</pairs>|
|##|[20] <pairs>-0.368897 35.286286</pairs>|


18

### **3.3 Reading JSON**

JSON files are structured as “attribute-value” pairs (aka “key-value” pairs), often with a hierarchical structure. Here’s a brief example:

{ "firstName": "John", "lastName": "Smith", "isAlive": true, "age": 25, "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" } ], "children": [], "spouse": null }

A set of key-value pairs is a named array and is placed inside braces (squiggly brackets). Note the nestedness of arrays within arrays (e.g., address within the overarching person array and the use of square brackets for unnamed arrays (i.e., vectors of information), as well as the use of different types: character strings, numbers, null, and (not shown) boolean/logical values. JSON and XML can be used in similar ways, but JSON is less verbose than XML.

We can read JSON into R using _fromJSON()_ in the _jsonlite_ package. Let’s play again with the Kiva data. The same data that we had worked with in XML format is also available in JSON format: http://api.kivaws.org/v1/loans/newest.json.

19

**library** (jsonlite) _## Loading required package: methods_ data <- **fromJSON** ("http://api.kivaws.org/v1/loans/newest.json") **names** (data) ## [1] "paging" "loans" **class** (data$loans) _# nice!_ ## [1] "data.frame" **head** (data$loans)

|##|id||name|languages|status|
|---|---|---|---|---|---|
|## 1|1597053 Florec|itas|3 Group|en|fundraising|
|## 2|1600198||Lilian|en|fundraising|
|## 3|1600199||Poline|en|fundraising|
|## 4|1600194||Sally|en|fundraising|
|## 5|1600195||Joyce|en|fundraising|
|## 6|1600197||Nancy|en|fundraising|
|##|funded_amount|bask|et_amount|image.id||
|## 1|0||0|2941081||
|## 2|0||0|2940126||
|## 3|0||0|2940128||
|## 4|0||0|2940122||
|## 5|0||0|2940124||
|## 6|0||0|2940125||
|##|image.template|_id|activity|secto|r|
|## 1||1|Farming|Agricultur|e|
|## 2||1|Cereals|Foo|d|
|## 3||1|Farming|Agricultur|e|
|## 4||1|Dairy|Agricultur|e|
|## 5||1|Farming|Agricultur|e|
|## 6||1|Farming|Agricultur|e|
|##|the|mes||||
|## 1|Vulnerable Gro|ups||||


20

|##|2<br>Rural|Exclusion||
|---|---|---|---|
|##|3<br>Rural|Exclusion||
|##|4<br>Rural|Exclusion||
|##|5<br>Rural|Exclusion||
|##|6<br>Rural|Exclusion||
|##||||
|##|1|||
|##|2||to bu|
|##|3|to buy see|ds and start a horticultural farm and impro|
|##|4 to buy|an additional dairy c|ow to improve her milk-vending business, ge|
|##|5||to buy farm inputs such as hybrid seeds|
|##|6||to buy farming input|
|##|locatio|n.country_code locati|on.country location.town|
|##|1|GT|Guatemala<br>Chajul|
|##|2|KE|Kenya<br>Bungoma|
|##|3|KE|Kenya<br>Kerugoya|
|##|4|KE|Kenya<br>Kericho|
|##|5|KE|Kenya<br>Nakuru|
|##|6|KE|Kenya<br>Kericho|
|##|locatio|n.geo.level<br>location|.geo.pairs|
|##|1|town 15.483483|-91.03707|
|##|2|town<br>0.566667|34.566667|
|##|3|town -0.499328|37.278484|
|##|4|town -0.368897|35.286286|
|##|5|town -0.283333|36.066667|
|##|6|town -0.368897|35.286286|
|##|locatio|n.geo.type partner_id|posted_date|
|##|1|point<br>369|2018-09-05T17:10:05Z|
|##|2|point<br>156|2018-09-05T17:10:05Z|
|##|3|point<br>156|2018-09-05T17:10:05Z|
|##|4|point<br>156|2018-09-05T17:10:04Z|
|##|5|point<br>156|2018-09-05T17:10:04Z|
|##|6|point<br>156|2018-09-05T17:10:04Z|
|##|planned|_expiration_date loan|_amount borrower_count|
|##|1<br>2018|-10-05T17:10:05Z|4150<br>6|
|##|2<br>2018|-10-05T17:10:04Z|100<br>1|


21

|##|3<br>2018-10-05T17:10:05Z<br>300||1|
|---|---|---|---|
|##|4<br>2018-10-05T17:10:04Z<br>300||1|
|##|5<br>2018-10-05T17:10:04Z<br>300||1|
|##|6<br>2018-10-05T17:10:04Z<br>300||1|
|##|lender_count bonus_credit_eligibility|tags||
|##|1<br>0<br>FALSE|NULL||
|##|2<br>0<br>TRUE|NULL||
|##|3<br>0<br>TRUE|NULL||
|##|4<br>0<br>TRUE|NULL||
|##|5<br>0<br>TRUE|NULL||
|##|6<br>0<br>TRUE|NULL||


One disadvantage of JSON is that it is not set up to deal with missing values, infinity, etc.

### **3.4 Webscraping ethics and best practices**

Before you set up any automated downloading of materials/data from the web you should make sure that what you are about to do is consistent with the rules provided by the website. Some places to look for information on what the website allows are:

- legal pages such as Terms of Service or Terms and Conditions on the website.

- check the robots.txt file (e.g., https://scholar.google.com/robots.txt) to see what a web crawler is allowed to do, and whether the site requires a particular delay between requests to the sites

- potentially contact the site owner if you plan to scrape a large amount of data

Here are some links with useful information:

- A blog post overview on webscraping and robots.txt

- Blog post on webscraping ethics

- Some information on how to understand a robots.txt file

In many cases you will want to include a time delay between your automated requests to a site, including if you are not actually crawling a site but just want to automate a small number of queries.

22

### **3.5 Using web APIs to get data**

Here we’ll see briefly some examples of making requests over the Web to get data. We’ll see simple HTTP requests, as well as use APIs to systematically query a website for information based on a documented interface. The packages _RCurl_ and _httr_ are useful for a wide variety of such functionality. Note that much of the functionality I describe below is also possible within bash using either _wget_ or _curl_ .

We’ve already seen some basic downloading of html from webpages, which use the HTTP request GET.

#### **3.5.1 HTTP requests**

Sometime specific information can be downloaded simply by constructing a static URL. Let’s look at some UN data (agricultural crop data). By going to

http://data.un.org/Explorer.aspx?d=FAO, and clicking on “Crops”, we’ll see a bunch of agricultural products with “View data” links. Click on “apricots” as an example and you’ll see a “Download” button that allows you to download a CSV of the data. Let’s select a range of years and then try to download “by hand”. Sometimes we can right-click on the link that will download the data and directly see the URL that is being accessed and then one can deconstruct it so that you can create URLs programmatically to download the data you want.

In this case, we can’t see the full URL that is being used. More generally, rather than looking at the URL associated with a link we may need to view the actual HTTP request sent by our browser to the server. We can do this using features of the browser (e.g., in Firefox see Web Developer -> Network and in Chrome More tools -> Developer tools -> Network). Based on this we can see that an HTTP GET request is being used with a URL such as: http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526;year:2003,2004,2005,2006,2007&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc

The stuff at the end of the URL specifies inputs passed to the server separated by ‘&’, in this case relating to the itemCode, dates, output format, etc. So we could more easily download the data using that URL, which we can fairly easily construct using string processing in bash, R, or Python, such as this:

_## example URL: ##"http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter= ##itemCode:526;year:2003,2004,2005,2006,2007&DataMartId=FAO& ##Format=csv&c=2,3,4,5,6,7&s=countryName:asc"_ itemCode <- 526 baseURL <- "http://data.un.org/Handlers/DownloadHandler.ashx"

23

yrs <- **paste** ( **as.character** (2003:2007), collapse = ",") filter <- **paste0** ("?DataFilter=itemCode:", itemCode, ";year:", yrs) args1 <- "&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&" args2 <- "s=countryName:asc,elementCode:asc,year:desc" url <- **paste0** (baseURL, filter, args1, args2) _## if the website provided a CSV we could just do this: ## apricots <- read.csv(url) ## but it zips the file_ temp <- **tempfile** () _## give name for a temporary file_ **download.file** (url, temp) dat <- **read.csv** ( **unzip** (temp)) _## using a connection (see Section 2)_ **head** (dat)

|##|Country.or.Area|Element.Code|Element Year|
|---|---|---|---|
|## 1|Afghanistan|5312 Area|harvested 2007|
|## 2|Afghanistan|5312 Area|harvested 2006|
|## 3|Afghanistan|5312 Area|harvested 2005|
|## 4|Afghanistan|5312 Area|harvested 2004|
|## 5|Afghanistan|5312 Area|harvested 2003|
|## 6|Afghanistan|5419|Yield 2007|
|##|Unit Value Val|ue.Footnotes||
|## 1|ha<br>8000|F||
|## 2|ha<br>8030|||
|## 3|ha<br>6749|Im||
|## 4|ha<br>5200|F||
|## 5|ha<br>7007|||
|## 6|hg/ha 72500|Fc||


A more sophisticated way to do the download is to pass the request in a structured way with named input parameters. This request is easier to construct programmatically. Here what is returned is a zip file, which is represented in R as a sequence of “raw” bytes. We can use httr’s _GET()_ , followed by writing to disk and reading back in, as follows (for some reason knitr won’t print the output...):

24

**library** (httr) _## ## Attaching package: ’httr’ ## The following object is masked from ’package:curl’: ## ## handle_reset_ output2 <- **GET** (baseURL, query = **list** ( DataFilter = **paste0** ("itemCode:", itemCode, ";year:", yrs), DataMartID = "FAO", Format = "csv", c = "2,3,4,5,6,7", s = "countryName:asc,elementCode:asc,year:desc")) temp <- **tempfile** () _## give name for a temporary file_ **writeBin** ( **content** (output2, 'raw'), temp) _## write out as zip file_ dat <- **read.csv** ( **unzip** (temp)) **head** (dat) ## Country.or.Area Element.Code Element Year ## 1 Afghanistan 5312 Area harvested 2007 ## 2 Afghanistan 5312 Area harvested 2006 ## 3 Afghanistan 5312 Area harvested 2005 ## 4 Afghanistan 5312 Area harvested 2004 ## 5 Afghanistan 5312 Area harvested 2003 ## 6 Afghanistan 5419 Yield 2007 ## Unit Value Value.Footnotes ## 1 ha 8000 F ## 2 ha 8030 ## 3 ha 6749 Im ## 4 ha 5200 F ## 5 ha 7007 ## 6 hg/ha 72500 Fc

In some cases we may need to send a lot of information as part of the URL in a GET request. If it gets to be too long (e.g„ more than 2048 characters) many web servers will reject the request. Instead we may need to use an HTTP POST request. A typical request would have syntax like this (using _RCurl_ ), supposing that the inputs were named _start-year_ and _end-year._

25

**if** ( **url.exists** ('http://www.wormbase.org/db/searches/advanced/dumper')) { x = **postForm** ('http://www.wormbase.org/db/searches/advanced/dumper', species="briggsae", list="", flank3="0", flank5="0", feature="Gene Models", dump = "Plain TEXT", orientation = "Relative to feature", relative = "Chromsome", DNA ="flanking sequences only", .cgifields = **paste** ( **c** ("feature", "orientation", "DNA", "dump","relative"), collapse=", "))

_httr_ and _RCurl_ can handle other kinds of HTTP requests such as PUT and DELETE. Finally, some websites use cookies to keep track of users and you may need to download a cookie in the first interaction with the HTTP server and then send that cookie with later interactions. More details are available in the Nolan and Temple Lang book.

#### **3.5.2 APIs: REST- and SOAP-based web services**

While webscraping with requests such as just described can work well, it was a bit convoluted. We basically needed to deconstruct the queries a browser makes and then mimic that behavior, in some cases having to parse HTML output to get at data. If the webpage changes even a little bit, our carefully constructed query syntax may fail. An alternative is to use a web service specifically designed to serve data or allow other interactions via an Applications Programming Interface (API). REST and SOAP are popular API standards/styles. Both REST and SOAP use HTTP requests; we’ll focus on REST as it is more common and simpler.

When using REST, we access _resources_ , which might be a Facebook account or a database of stock quotes. The resource may return information in the form of an HTML file or JSON, CSV or something else. REST generally uses XML or JSON as the format for the request (if not a simple GET request) and what is returned.

Let’s see an example of accessing climate model output data from the World Bank. The API is documented here: http://data.worldbank.org/developers/climate-data-api. Following that documentation we can download monthly average precipitation predictions for 2080-2099 for the US (ISO3 code ‘USA’) based on global climate model simulations. In this case what the World Bank refers to as the REST-based query is simply constructing a straightforward URL.

26

|times <- **c**(2080, 2099)<br>countryCode <- 'USA'<br>baseURL <- "http://clim<br>_##" http://climatedataa_<br>type <- "mavg"<br>var <- "pr"|atedataa<br>_pi.world_|pi.worldba<br>_bank.org/c_|nk.org/c<br>_limatewe_|limateweb/rest/v1/country"<br>_b/rest/v1/country"_|
|---|---|---|---|---|
|data <- **read.csv**(**paste**(|baseURL,|type, var|, times[|1], times[2],|
||**paste0**(c|ountryCode|, '.csv'|), sep = '/'))|
|**head**(data)<br><br>|||||
|##<br>GCM var|scenario|from_year|to_year|Jan|
|## 1<br>bccr_bcm2_0<br>pr|a2|2080|2099|67.03573|
|## 2<br>bccr_bcm2_0<br>pr|b1|2080|2099|62.36411|
|## 3 cccma_cgcm3_1<br>pr|a2|2080|2099|73.05678|
|## 4 cccma_cgcm3_1<br>pr|b1|2080|2099|68.13736|
|## 5<br>cnrm_cm3<br>pr|a2|2080|2099|72.18374|
|## 6<br>cnrm_cm3<br>pr|b1|2080|2099|69.87911|
|##<br>Feb<br>Mar|Apr|May|Jun|Jul|
|## 1 60.34472 68.55613|69.73249|70.75057|68.87670|75.50839|
|## 2 57.25621 65.37839|66.83145|71.42986|66.70454|76.21705|
|## 3 65.88258 69.07827|70.52308|71.27610|71.40891|71.73378|
|## 4 56.80470 64.87122|64.26042|65.26155|65.63476|68.85459|
|## 5 64.47102 76.22999|79.40222|94.16236|93.20071|92.61398|
|## 6 59.47017 70.12903|80.61524|92.51666|92.54483|96.00988|
|##<br>Aug<br>Sep|Oct|Nov|Dec||
|## 1 79.16541 76.60718|79.72601|72.12957|71.83717||
|## 2 76.50563 81.48503|73.44661|67.69188|62.61851||
|## 3 71.16824 72.37070|72.17842|85.11507|77.58228||
|## 4 68.02093 66.02112|70.71792|77.58472|77.31110||
|## 5 87.12436 87.24258|86.20070|77.22606|78.49393||
|## 6 91.05730 88.87449|82.81388|70.25031|71.83962||


Often what distinguishes an API from what we’ve discussed in previous sections is that the API documents what information it expects from the user and returns the result in a standard format (e.g., a particular file format rather than producing a webpage). Here we can see the Kiva API, which allows us to construct queries on the Kiva data that we saw some of earlier.

The Nolan and Temple Lang book provides a number of examples of different ways of authen-

27

ticating with web services that control access to the service.

Finally, some web services allow us to pass information to the service in addition to just getting data or information. E.g., you can programmatically interact with your Facebook, Dropbox, and Google Drive accounts using REST based on HTTP POST, PUT, and DELETE. Authentication is of course important in these contexts and some times you would first authenticate with your login and password and receive a “token”. This token would then be used in subsequent interactions in the same session.

#### **3.5.3 Packaged access to an API**

For popular websites/data sources, a developer may have packaged up the API calls in a userfriendly fashion for use from R, Python or other software. For example there are Python (twitter) and R (twitteR) packages for interfacing with Twitter via its API.

Here’s some example code for Python (the Python package seems to be more fully-featured than the R package). This looks up the US senators’ Twitter names and then downloads a portion of each of their timelines, i.e., the time series of their tweets. Note that Twitter has limits on how much one can download at once.

**import** json **import** twitter _# You will need to set the following variables with your # personal information. To do this you will need to create # a personal account on Twitter (if you don’t already have # one). Once you’ve created an account, create a new # application here: # https://dev.twitter.com/apps # # You can manage your applications here: # https://apps.twitter.com/ # # Select your application and then under the section labeled # "Key and Access Tokens", you will find the information needed # below. Keep this information private._ CONSUMER_KEY = "" CONSUMER_SECRET = "" OAUTH_TOKEN = "" OAUTH_TOKEN_SECRET = ""

28

auth = twitter.oauth. **OAuth** (OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) api = twitter. **Twitter** (auth=auth) _# get the list of senators_ senators = api.lists. **members** (owner_screen_name="gov", slug="us-senate", count=100) with open("senators-list.json", "w") **as** f: json. **dump** (senators, f, indent=4, sort_keys= **True** ) _# get all the senators’ timelines_ names = [d["screen_name"] **for** d **in** senators["users"]] timelines = [api.statuses. **user_timeline** (screen_name=name, count = 500) **for** name **in** names] with open("timelines.json", "w") **as** f: json. **dump** (timelines, f, indent=4, sort_keys= **True** )

### **3.6 Accessing dynamic pages**

Some websites dynamically change in reaction to the user behavior. In these cases you need a tool that can mimic the behavior of a human interacting with a site. _selenium_ (and the _RSelenium_ wrapper for R) is a popular tool for doing this.

---

[← Unit 03 — dataIO Part 12 —](12-unit-03-dataio-part-12.md) · [Up: contents](index.md) · [4 Output from R →](14-4-output-from-r.md)
