---
title: 1.1 Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/regexpr-Lang.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.1 Introduction

**Source:** [`units/regexpr-Lang.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Although binary files allow us to explicitly encode the type of a value, be it an integer, real number, string, etc., much of the data we deal with are given to us as plain text. We input numbers in text files, download text files from Web and FTP servers, and save spreadsheets as comma-separated values in .csv files. In these cases, the data are merely represented by their text form and are easily interpreted by applications. However, there are many examples of more complex situations where the data are not as easily interpreted, and the text must be processed to create the values of interest. A simple example of this phenomenon is when numeric values are embedded into text, but not in a regular or simple format, such as numbers in an HTML table. In this case, we must extract the elements of interest from the text content by identifying the patterns where the values occur. A different sort of example occurs when text itself makes up the data, such as a speech, an abstract, or an email message. Then we must search for the presence of certain words or phrases in particular contexts or places to uncover structure in the data, e.g. we might examine how often each word is used, the names of the author(s), the use of punctuation, etc. Finally, documents and text are sometimes treated directly as data such as in search engines, databases, and so on.

#### **1.1.1 Placing data on a map**

To make a county map of the United States (Figure **??** in Chapter **??** ) that displays election results, and possibly census data too, requires the various sources of information to be merged together. This merger uses county name, a text field, which needs to be _transformed_ into a uniform format across the three sources. The following sample lines of text demonstrate the inconsistencies in how a county’s name is represented in these three sources of data; geographic (top), census (middle) and election (bottom). Notice that there is no period after ’’St’’ in the geographic data; the election results differ from the other two sources in that there is an & rather than “and” in Lewis and Clark County; the capitalization is not consistent (e.g. “Qui” vs “qui” in Lac qui Parle County); and the use of “County” and “Parish” is not consistent.

"De Witt County",IL,40169623,-88904690 "Lac qui Parle County",MN,45000955,-96175301

"Lewis and Clark County",MT,47113693,-112377040 "St John the Baptist Parish",LA,30118238,-90501892

"St. John the Baptist Parish","43,044","52.6","44.8",...

"De Witt County","16,798","97.8","0.5", ...

1

"Lac qui Parle County","8,067","98.8","0.2", ... "Lewis and Clark County","55,716","95.2","0.2", ...

DeWitt 23 23 4,920 2,836 0 Lac Qui Parle 31 31 2,093 2,390 36 Lewis & Clark 54 54 16,432 12,655 386 St. John the Baptist 35 35 9,039 10,305 74

#### **1.1.2 Spam filtering**

In Chapter **??** we explore the problem of filtering email to try to differentiate legitimate electronic mail from unsolicited bulk email, i.e. spam. One approach considered _creates_ several variables pertaining to the email message and then uses the values of these variables for a mail message to predict whether it is spam or not. A potentially useful variable is one that indicates whether the subject line of the email message contains a “word” with punctuation or a digit in the middle of it, such as “V!agra” or “m0rtgage”.

Below are parts of the header from three email messages. The bottom two headers are from spam while the top is not.

Date: Tue, 02 Jan 2007 12:17:45 -0800 From: Duncan Temple Lang <duncan@wald.ucdavis.edu> To: Deborah Nolan <nolan@stat.Berkeley.EDU> Subject: Re: 90 days

Date: Sat, 27 Jan 2007 16:28:48 +0800 From: remade SSE <glzmeqrxr99@embarqhsd.net> To: depchairs03-04@uclink.berkeley.edu Subject: [SPAM:XXXXXXXXX]

Date: Thu, 03 Apr 2008 09:24:53 +0700 From: Faustino Britt <Faustino@sfera.umk.pl> To: Brice Frederick <nolan@stat.Berkeley.EDU> Subject: Fancy rep1!c@ted watches

Notice that the last subject line contains the “word” rep1!c@ted rather than “replicated”. These fake words are popular in spam because they are easy for us to read, but they are not likely to be found in a list of “banned” words, i.e. words that a spammer would use. Another variable that may be helpful in detecting spam is a logical that indicates whether or not the subject line of an email message begins with “Re:” Yet another is whether or not the reply-to address contains an underscore or digit.

#### **1.1.3 Weblogs**

To analyze the requests made to a Web site, we first _extract_ the relevant information from the Web log, such as the machine of requester, the time and date of the request, the name of the file requested, the return status, and the number of bytes returned. Below are two lines from a Web log. The log is a text file where each request appears on a separate line of text, and although the text has a lot of structure, the information does not appear in a simple format such as in comma separated values, nor is it placed consistently in the same columns in the file. For example, the date and time are set off in square brackets. Note that each line in the Web log is broken across four lines here for formatting purposes.

169.237.46.168 - - [26/Jan/2004:10:47:58 -0800]

- "GET /stat141/Winter04 HTTP/1.1" 301 328

- "http://anson.ucdavis.edu/courses/"

> "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)"

> 169.237.46.168 - - [26/Jan/2004:10:47:58 -0800]

2

##### **Examples of Uses of Regular Expressions on Text Data**

- EXTRACT pieces of text that appear in non-standard formats.

- CREATE variables from information found in text.

- CLEAN and TRANSFORM text into a uniform format and resolve inconsistencies in format between files.

- MINE text by treating documents directly as data.

"GET /stat141/Winter04/ HTTP/1.1" 200 2585 "http://anson.ucdavis.edu/courses/" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)"

#### **1.1.4 Mining the State of the Union addresses**

We _mine_ the text of the State of the Union Addresses, looking for similarities between presidents’ speeches. One approach to doing this would be to compare word frequencies across documents in the corpus of speeches. To do this, we build a word-vector for each speech that tallies the number of occurrences of each word used in the speech, e.g. there was one occurrence of the word “much”, the word “debt” was used twice, and the words “nation”, “national” or “nations” appeared five times in the December, 1790 inaugural speech of George Washington’s (a snippet is shown below). With these word-vectors we can look for similarities between the distribution of words in the speeches. to create the word-vector, we first stem words (i.e. reduce “running” to “run”) and remove stop words such as “and’, “the”, and “of”.

***

State of the Union Address George Washington December 8, 1790

Fellow-Citizens of the Senate and House of Representatives:

In meeting you again I feel much satisfaction in being able to repeat my congratulations on the favorable prospects which continue to distinguish our public affairs. The abundant fruits of another year have blessed our country with plenty and with the means of a flourishing commerce.

The regular expression language is essentially a programming language, and with it we can develop complicated constructs, making use of the rich set of meta characters that it employs, to analyze each of these data sets. The goal of this chapter is to demonstrate the fundamental ideas behind the language, to introduce the basic elements in the language, and show how they can be combined to express patterns. There are many tutorials and examples on the Web that cover different uses and applications of regular expressions. There are also books on the subject that provide many more examples and a greater understanding of how regular expressions work. Most important of all, practice in creating regular expressions and testing them on data is essential to gaining both understanding and experience so that when you need to use regular expressions in handling data, they will be familiar.

3

---

[Up: contents](index.md) · [1.2 Matching literal strings →](02-1-2-matching-literal-strings.md)
