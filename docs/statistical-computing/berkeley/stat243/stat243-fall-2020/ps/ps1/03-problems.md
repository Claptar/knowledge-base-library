---
title: Problems
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. As preparation for the next few units, please read the sections titled “Memory hierarchy” and “Cache in depth” in the following brief piece that talks about the difference between the CPU cache, main memory (RAM), and disk. You don’t need to follow all the technical details in the “Cache in depth”

1

section - just try to get the big picture of what the cache is and a bit about how it works. You don’t need to turn anything in for this problem.

(Side note: the reference to floppy disks and CDROM indicates that webpage was written a while ago, but of the various documents online that talk about this topic, I thought this was the best quick summary I could find.)

2. This problem explores file sizes in light of understanding storage in ASCII plain text versus binary formats and the fact that numbers are (generally) stored as 8 bytes per number in binary format.

   - (a) Explain the sizes of the two files created below. In discussing the CSV text file, how many characters do you expect to be in the file (i.e., you should be able to estimate this very accurately without using _wc_ or any explicit program that counts characters). Hint: what do we know about numbers drawn from a standard normal distribution?

n <- 1e7 a <- **matrix** ( **rnorm** (n), ncol = 100) a <- **round** (a, 10) **write.table** (a, file = '/tmp/tmp.csv', quote=FALSE, row.names=FALSE, col.names = FALSE, sep=',') **save** (a, file = '/tmp/tmp.Rda', compress = FALSE) **file.size** ('/tmp/tmp.csv') ## [1] 133888193 **file.size** ('/tmp/tmp.Rda') ## [1] 80000096

- (b) Now consider saving out the numbers one row per number. Given we no longer have to save all the commas, why is the file size unchanged?

b <- a **dim** (b) <- **c** (1e7, 1) _## change to one column by adjusting attribute_ **write.table** (b, file = '/tmp/tmp-onecolumn.csv', quote=FALSE, row.names=FALSE, col.names = FALSE, sep=',') **file.size** ('/tmp/tmp-onecolumn.csv') ## [1] 133888193

- (c) Consider the following ways of reading the data into R (though similar results would be obtained in other languages). Explain the difference in speed between the three situations. Side note: in this case _readr::read_csv()_ is rather faster than _read.csv()_ .

_## First comparison_ **system.time** (a1 <- **read.csv** ('/tmp/tmp.csv', header = FALSE)) ## user system elapsed ## 23.446 0.328 23.775

2

**system.time** (a2 <- **read.csv** ('/tmp/tmp.csv',header = FALSE, colClasses = 'numeric')) ## user system elapsed ## 2.938 0.052 2.990 **system.time** (a3 <- **scan** ('/tmp/tmp.csv', sep = ',')) ## user system elapsed ## 3.026 0.020 3.046

- (d) Explain why _tmp.Rda_ is so much bigger than _tmp2.Rda_ given they both contain the same number of numeric values.

**save** (a, file = '/tmp/tmp1.Rda') **file.size** ('/tmp/tmp1.Rda') ## [1] 76778172 b <- **rep** ( **rnorm** (1), 1e7) **save** (b, file = '/tmp/tmp2.Rda') **file.size** ('/tmp/tmp2.Rda') ## [1] 116508

3. Please read Unit 4 on good programming/project practices and incorporate what you’ve learned from that reading into your solution for Problem 4. As your response to this question, briefly (a few sentences) note what you did in your code that reflects the material in Sections 1.2 and 1.3 of Unit 4. Please also note anything in Unit 4 that you disagree with, if you have a different stylistic perspective.

4. Go to Google Scholar and enter the name (including first name to help with disambiguation) for a researcher whose work interests you. (If you want to do the one that will match the problem set solutions, you can use “Jennifer Chayes”, who is Berkeley’s new dean for data science.) If you’ve entered the name of a researcher that Google Scholar recognizes as having a Google Scholar profile, you should see that the first item returned is a “User profile”. Next, if you click on the hyperlink for the researcher under “User profiles for <researcher name>”, you’ll see that brings you to a page that provides the citations for all of the researcher’s papers.

_IMPORTANT: if you repeatedly query the Google Scholar site too quickly, Google will start returning “503” errors because it detects automated usage (see problem 5 below). So, if you are going to run code from a script such that multiple queries would get done in quick succession, please put something like Sys.sleep(2) in between the calls that do the HTTP requests. Also when developing your code, once you have the code in part (a) working to download the HTML, use the downloaded HTML to develop the remainder of your code and don’t keep re-downloading the HTML as you work on the remainder of the code._

- (a) Now, based on the information returned by your work above, including the various URLs that your searching and clicking generated, write R code that will programmatically return the citation page for your researcher. Specifically, write a function whose input is the character string of the name of the researcher and whose output is the HTML (as an object of class ’xml_document’) corresponding to the researcher’s citation page as well as the researcher’s Google Scholar ID.

3

Hint: you will need to use some string processing functions to extract the Scholar ID (and possibly for other things) from the output of the various _rvest_ functions. I recommend functions from the _stringr_ package (we’ll see these in Unit 5 and you can find information in Section 2.1.2 of the _string processing_ tutorial), in particular: _str_detect()_ , _str_extract()_ , _str_split()_ , and _str_replace()_ . You should NOT need to use regular expressions (which we’ll cover in Unit 5), but you can if you want/know how to. Finally if you get an error message like this “Syntax error in regexp pattern. (U_REGEX_RULE_SYNTAX)”, it means the string processing function is interpreting the characters you are looking for as a regular expression. Simply wrap the string you are looking for in the _fixed()_ function, e.g., “fixed(’sdf?=sd34’)” so the characters are simply interpreted as regular characters (i.e., interpreted literally).

- (b) Create a second function to process the resulting HTML to create an R data frame that contains the article title, authors, journal information, year of publication, and number of citations as five columns of information. Try your function on a second researcher to provide more confidence that your function is working properly.

- (c) Include checks in your code so that it fails gracefully if the user provides invalid input or Google Scholar doesn’t return a result. You don’t have to use the _assertthat_ package as we won’t cover that until Section on Sep. 18, but you can if you want.

- (d) (Extra credit) Fix your function so that you get all of the results for a researcher and not just the first 20. Hint: figure out what query is made when you click on “Show More” at the bottom of the page.

Hint: as you are trying to understand the structure of the HTML, one option is to use _write_xml()_ on the result of _read_html()_ and then view the file that is produced in a text editor.

Note: For simplicity you can either assume only one User Profile will be returned by your initial search or that you can just use the first of the profiles.

5. Look at the _robots.txt_ file for Google Scholar and the references in Unit 2 on the ethics of webscraping. Write a paragraph discussing the ethics of scraping data from Google Scholar as we do in Problem 4. Do you have any concerns in terms of whether anything we are doing in Problem 4 might violate Google’s rules or the general ethical considerations in the references? (I think what we are doing is in the spirit of ethical webscraping, or I wouldn’t have assigned it, but there is a grey zone here, and I’d like you to think about the ethical issues within a specific context.)

6. This problem is actually just the formatting of this document.

   - (a) Have the document be correctly formatted according to the requirements above. You don’t need to explicitly answer this sub-problem.

   - (b) (extra credit) The _reticulate_ package and R Markdown allow you now to have Python and R chunks in a document that interact with each other. Demonstrate the ability to use this functionality, in particular sending data from R to Python and back to R, with some processing done in Python (it doesn’t have to be complicated processing). There’s a blog post here to get you started: http://feedproxy.google.com/ _∼_ r/RBloggers/ _∼_ 3/76l-uQEOoiU/?utm_source=feedburner&utm_medium=email

4

---

[← Formatting requirements](02-formatting-requirements.md) · [Up: contents](index.md)
