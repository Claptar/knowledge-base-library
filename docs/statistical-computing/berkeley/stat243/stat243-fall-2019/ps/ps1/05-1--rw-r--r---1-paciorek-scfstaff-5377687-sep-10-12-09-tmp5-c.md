---
title: '[1] "-rw-r--r-- 1 paciorek scfstaff 5377687 Sep 10 12:09 tmp5.csv"'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "-rw-r--r-- 1 paciorek scfstaff 5377687 Sep 10 12:09 tmp5.csv"

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (b) Now consider the additional results below. Can you explain what is going on and understand what R is doing when it saves an object using _save()_ ? You might experiment with options to the

2

_save()_ function to determine if your explanations are correct.

chars <- **sample** (letters, 1e6, replace = TRUE) chars <- **paste** (chars, collapse = '') **save** (chars, file = 'tmp6.Rda') **system** ('ls -l tmp6.Rda', intern = TRUE) ## [1] "-rw-r--r-- 1 paciorek scfstaff 635255 Sep 10 12:09 tmp6.Rda" chars <- **rep** ('a', 1e6) chars <- **paste** (chars, collapse = '') **save** (chars, file = 'tmp7.Rda') **system** ('ls -l tmp7.Rda', intern = TRUE) ## [1] "-rw-r--r-- 1 paciorek scfstaff 1066 Sep 10 12:09 tmp7.Rda"

4. Go to https://scholar.google.com and enter the name (including first name to help with disambiguation) for a researcher whose work interests you. (If you want to do the one that will match the problem set solutions, you can use “Robert Tibshirani”, who is a well-known statistician and machine learning researcher.) If you’ve entered the name of a researcher that Google Scholar recognizes as having a Google Scholar profile, you should see that the first item returned is a “User profile”. Next, if you click on the hyperlink for the researcher under “User profiles for <researcher name>”, you’ll see that brings you to a page that provides the citations for all of the researcher’s papers. _IMPORTANT: if you repeatedly query the Google Scholar site too quickly, Google will start returning “503” errors because it detects automated usage (see problem 5 below). So, if you are going to run code from a script such that multiple queries would get done in quick succession, please put something like Sys.sleep(2) in between the calls that do the HTTP requests. Also when developing your code, once you have the code in part (a) working to download the HTML, use the downloaded HTML to develop the remainder of your code and don’t keep re-downloading the HTML as you work on the remainder of the code._

   - (a) Now, based on the information returned by your work above, including the various URLs that your searching and clicking generated, write R code that will programmatically return the citation page for your researcher. Specifically, write a function whose input is the character string of the name of the researcher and whose output is the HTML (as an object of class ’xml_document’) corresponding to the researcher’s citation page as well as the researcher’s Google Scholar ID.

Hint: you will need to use some string processing functions to extract the Scholar ID (and possibly for other things) from the output of the various _rvest_ functions. I recommend functions from the _stringr_ package (we’ll see these in Unit 5 and you can find information in Section 2.1.2 of the _string processing_ tutorial), in particular: _str_detect()_ , _str_extract()_ , _str_split()_ , and _str_replace()_ . You should NOT need to use regular expressions (which we’ll cover in Unit 5), but you can if you want/know how to. Finally if you get an error message like this “Syntax error in regexp pattern. (U_REGEX_RULE_SYNTAX)”, it means the string processing function is interpreting the characters you are looking for as a regular expression. Simply wrap the string you are looking for in the _fixed()_ function, e.g., “fixed(’sdf?=sd34’)” so the characters are simply interpreted as regular characters (i.e., interpreted literally).

3

- (b) Create a second function to process the resulting HTML to create an R data frame that contains the article title, authors, journal information, year of publication, and number of citations as five columns of information. Try your function on a second researcher to provide more confidence that your function is working properly.

- (c) Include checks in your code so that it fails gracefully if the user provides invalid input or Google Scholar doesn’t return a result. You don’t have to use the _assertthat_ package as we won’t cover that until the Lab on Tuesday September 10, but you can if you want.

- (d) (Extra credit) Fix your function so that you get all of the results for a researcher and not just the first 20. Hint: figure out what query is made when you click on “Show More” at the bottom of the page.

Hint: as you are trying to understand the structure of the HTML, one option is to use _write_xml()_ on the result of _read_html()_ and then view the file that is produced in a text editor.

Note: For simplicity you can either assume only one User Profile will be returned by your initial search or that you can just use the first of the profiles.

5. Look at the _robots.txt_ file for Google Scholar and the references in Unit 2 on the ethics of webscraping. Write a paragraph or two discussing the ethics of scraping data from Google Scholar as we do in Problem 4. Do you have any concerns in terms of whether anything we are doing in Problem 4 might violate Google’s rules or the general ethical considerations in the references? (I think what we are doing is in the spirit of ethical webscraping, or I wouldn’t have assigned it, but there is a grey zone here, and I’d like you to think about the ethical issues within a specific context.)

6. This problem is actually just the formatting of this document.

   - (a) Have the document be correctly formatted according to the requirements above. You don’t need to explicitly answer this sub-problem.

   - (b) (extra credit) The _reticulate_ package and R Markdown allow you now to have Python and R chunks in a document that interact with each other. Demonstrate the ability to use this functionality, in particular sending data from R to Python and back to R, with some processing done in Python (it doesn’t have to be complicated processing). There’s a blog post here to get you started: http://feedproxy.google.com/ _∼_ r/RBloggers/ _∼_ 3/76l-uQEOoiU/?utm_source=feedburner&utm_medium=email

4

---

[← Ps 01 — Part 04 —](04-ps-01-part-04.md) · [Up: contents](index.md)
