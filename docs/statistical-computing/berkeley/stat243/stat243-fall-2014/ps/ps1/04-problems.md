---
title: Problems
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. (Due Sep. 3) Please fill out the class entry survey:

   - https://docs.google.com/a/berkeley.edu/forms/d/1Yr33EgFwcgtIgJ8FmhyugarGkGNmhnpS3QztknsK_Cs/viewform?c=0&w=1&usp=mail_form_link

2. Virtual machine practice: Install VirtualBox on your computer and import the BCE virtual machine (VM), following these instructions: http://collaboratool.berkeley.edu/using-virtualbox.html. Then clone the class Git repository onto the virtual machine.

   - (a) How many (virtual) processors are there on the virtual machine?

   - (b) What is reported (from within the VM) in terms of how much RAM there is?

3. This problem provides practice in downloading and manipulating data using shell scripting. We’ll use data from the US Federal Election Commission (FEC) on campaign expenditures and contributions about contributions to candidates for the US Senate. Not all of you will be familiar with the US election system or how candidates for office raise money, so if you’re confused about the context, do ask me. Basically, individuals who are campaigning to be elected raise money as contributions from other people and organizations. The contributions must be reported to the FEC and the resulting data are available to the public.

   - (a) This website, http://www.fec.gov/data/CandidateSummary.do?format=html, contains information on the total contributions and expenditures by each candidate for the 2014 elections. At the top of the page you’ll see links to a CSV file and to metadata for all of the candidates running for federal office.

      - i. Using the CSV file extract the data for Republican and Democratic candidates for Senate into two files (one for Republicans and one for Democrats). Be careful because S and REP and DEM can appear in fields other than the relevant fields.

      - ii. At this stage, we want to be able to split into fields based on commas, but some of the fields themselves have commas in them. Here’s how we can use a UNIX program called _sed_ to do some useful replacement of certain patterns. You don’t have to understand the syntax as working with regular expressions in _sed_ is more than I want to cover in the course.

         - sed ’s/$[^",]$,/\1/g’ file.csv # this removes any comma that is NOT preceded by a “ (double quote) or another comma

2

- sed ’s/[$"]//g’ file.csv # this removes the $ and “ (double quote) from the file

Now extract the total contributions to each candidate and some basic information about each candidate and sort on the total contributions. You’ll need to look carefully at arguments to the _sort_ utility, in particular the “key” will allow you to sort on a field that is not the first field. For each party find the five candidates with the largest total contributions and print the amount of contributions and some information about the candidate to the screen.

- (b) For this part of the problem, we’ll use FEC data on individual contributions to candidates from ftp://ftp.fec.gov/FEC/2014. The data are described at the website: http://www.fec.gov/finance/disclosure/ftpdet.shtml#a2013_2014. Basically the Candidate Master file contains a record for each candidate, which includes their “principal committee ID” for their campaign finance committee. Write shell code that takes a candidate’s last name and returns their principal committee ID based on the _cn.txt_ file (from the _cn14.zip_ file), assigning the result to a shell variable. Now write shell code that uses that variable to extract the individual contributions to that candidate (from the individual contributions file, _itcont.txt_ contained in the _indiv14.zip_ file) and finds out the number of contributions above $200, both nationwide and restricted to California. Compare the two candidates for the Kentucky Senate seat, Mitch McConnell and Alison Lundergan Grimes.

- (c) Extra credit: Take your code from part (b) and make it into a function that finds the number of contributions for a candidate, returning the result in a nicely formatted way. Now use a loop to loop through multiple predefined candidates and call the function, reporting the number of contributions for each candidate.

The goal here is to practice writing shell code to download files, extract fields and subset datasets, and summarize information in those fields. If you’d like to use different fields or different data available online to answer a question of your choice, that’s fine. Just run the data source and question(s) by me in advance.

4. More shell practice: Your task here is to automatically download all the files ending in _txt_ from this National Climate Data Center website: http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/. Your shell script should provide a status message to the user, telling you the name of the file as it downloads each file. You should be able to use the UNIX tools in Table 2 of Unit 2 to extract the individual file names from the HTML index file linked to above. Do not hard code the names of the txt files into your code.

5. As preparation for future problem sets, this problem explores embedding R code and output in a PDF or HTML document. Here is some R code that creates a plot and prints some output to the screen.

**hist** (LakeHuron)

lowHi <- **c** ( **which.min** (LakeHuron), **which.max** (LakeHuron))

yearExtrema <- **attributes** (LakeHuron)$tsp[1] - 1 + lowHi

You should produce a PDF (using the knitr package in R with Latex) or an HTML file (using R Markdown). If you are a Statistics student you should use Latex. Requirements for your solution:

3

- (a) Your solution should consist of the Latex+knitr or R Markdown syntax that produces the PDF, where the syntax embeds the necessary R code.

- (b) Your resulting PDF or HTML output should look like the last page of the PDF of this assignment (it does not have to be exactly the same in terms of formatting and the actual prefacing text), which I created using Latex+knitr.

- (c) Your resulting PDF or HTML document should be less than a page and your figure should be small enough that it only takes up half the width of the page (the _fig.width_ argument may be helpful).

- (d) In your solution, you should NOT manually type ’1875’ or ’1972’ in your document, rather embed an R expression that returns ’1875’ and ’1972’ using _\rinline_ or the equivalent for R Markdown.

#### Hints:

- (a) Using Latex with knitr: The following should work on the VM or an SCF Linux machine. However, on the VM, at the command line, you’ll first need to run the following to install some necessary software:

sudo apt-get install texinfo

See the example Latex file with embedded R code at the knitr demo page: 005-latex.Rtex. Rename the file, e.g., _knitrTest.Rtex_ (for some reason, when I tried to use the _knit()_ function below with the original file name, it failed). Start R and run the following to produce a PDF: library(knitr)

knit2pdf(’knitrTest.Rtex’) # this should produce knitrTest.pdf On the VM, you can use the program _evince_ to view the PDF.

- (b) To use R Markdown, see the demo file _module1_basics.Rmd_ in the _berkeley-scf/r-bootcamp2014_ repository. You can create HTML from this file from within R as: library(knitr)

knit2html(’module1_basics.Rmd’) # this should produce module1_basics.html

4

#### **Solution to Problem 5**

The height of the water level in Lake Huron fluctuates over time. Here I ’analyze’ the variation using R. I show a histogram of the lake levels for the period 1875 to 1972.

**<mark>hist</mark>** <mark>(LakeHuron)</mark>

---

[← Technical requirements for your solutions to Problems 3 and 4](03-technical-requirements-for-your-solutions-to-problems-3-and.md) · [Up: contents](index.md) · [Histogram of LakeHuron →](05-histogram-of-lakehuron.md)
