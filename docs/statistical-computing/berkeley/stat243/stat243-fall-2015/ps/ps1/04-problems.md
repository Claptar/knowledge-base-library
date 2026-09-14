---
title: Problems
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Hint: a simple piece of regular expression syntax standing for “any number of arbitrary characters” is “.*”. To refer to an actual period or an actual quote, you need to ‘escape’ it: “\.” and “\””.

1. This problem provides practice in downloading and manipulating data using shell scripting. We’ll use United Nations Food and Agriculture Organization (FAO) data on agricultural production. If you go to http://data.un.org/Explorer.aspx?d=FAO and click on “Crops”, you’ll see a bunch of agricultural products with “View data” links. Click on “apricots” as an example and you’ll see a “Download” button that allows you to download a CSV of the data. I’ve inspected the HTTP requests that the site handles and found out that you can download a file directly via URL in the following format: http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode: 526&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&s=countryName:asc, elementCode:asc,year:desc

That downloads the data for Item 526 (apricots). Note that you may need to put the http address inside double quotes when using a UNIX shell command to download it. Also make sure there are no carriage returns in the http address (I had to break the address above to fit on the page). You can see the item ID for other products by hovering over “View Data” link for the relevant product.

   - (a) Download the data for apricots. Extract the data for individual countries into one file and for regions of the world into another file. Then subset the country-level data to the year 2005. Based on the “area harvested” determine the five countries using the most land to produce apricots. You’ll need to look carefully at arguments to the _sort_ utility, in particular the “key” will allow you to sort on a field that is not the first field. Now automate your analysis and examine the top five countries for 1965, 1975, 1985, 1995, and 2005. Have the rankings changed?

   - (b) Write a bash function that takes as input a single item code (e.g., 526 for apricots, 572 for avocados) and prints out to the screen the data stored in the CSV file, such that the information could be piped on to UNIX another operation.

   - (c) (Extra credit) Find the FAO metadata online that relate item codes to names of agricultural products. Modify your function in (b) so that the user can pass the name of the product instead of the code. Your function would then presumably query a file (i.e., a file that you have created in a separate step) that relates the codes to the names.

2. Your task here is to automatically download all the files ending in _.txt_ from this National Climate Data Center website: http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/. Your shell script should provide a status message to the user, telling you the name of the file as it downloads each file. You should be able to use UNIX utilities to extract the individual file names from the HTML index file linked to above. Alternatively you may use tools from Unit 3, but an use of R should be done directly from the command line and should only involve a line or two of R code. Do not hard code the names of the .txt files into your code.

3. As preparation for future problem sets, this problem explores embedding R code and output in a PDF or HTML document.

Here is some R code that creates a plot and prints some output to the screen.

**hist** (LakeHuron)

lowHi <- **c** ( **which.min** (LakeHuron), **which.max** (LakeHuron))

2

yearExtrema <- **attributes** (LakeHuron)$tsp[1]-1 + lowHi

Your task in this problem is to produce a single-page of PDF that looks like the last page of this assignment, using either the knitr package in R with L<sup>A</sup> TEX or R Markdown. If you are a Statistics student you should use L<sup>A</sup> TEX.

Requirements for your solution:

- (a) Your solution should consist of the L<sup>A</sup> TEX+knitr or R Markdown syntax that produces the PDF, where the syntax embeds the necessary R code.

- (b) Your resulting PDF output should look like the last page of the PDF of this assignment (it does not have to be exactly the same in terms of formatting and the actual prefacing text), which I created using L<sup>A</sup> TEX+knitr.

- (c) Your resulting PDF document should be less than a page and your figure should be small enough that it only takes up half the width of the page (the _fig.width_ argument may be helpful).

- (d) In your solution, you should NOT manually type ‘1875’ or ‘1972’ in your document, rather embed an R expression that returns ’1875’ and ’1972’ using _\rinline_ or the equivalent for R Markdown.

The tutorial on dynamic documents provides information and example/template files that you can make use of to create your L<sup>A</sup> TEX/knitr or R Markdown file. Ask us questions if you get stuck - this question is just intended to ensure that you are up to speed on how to deal with formatting for future problem sets.

3

#### **The result of your solution to Problem 3 should look like this page**

The height of the water level in Lake Huron fluctuates over time. Here I ’analyze’ the variation using R. I show a histogram of the lake levels for the period 1875 to 1972.

**<mark>hist</mark>** <mark>(LakeHuron)</mark>

---

[← Technical requirements for your solutions to Problems 1 and 2](03-technical-requirements-for-your-solutions-to-problems-1-and.md) · [Up: contents](index.md) · [Histogram of LakeHuron →](05-histogram-of-lakehuron.md)
