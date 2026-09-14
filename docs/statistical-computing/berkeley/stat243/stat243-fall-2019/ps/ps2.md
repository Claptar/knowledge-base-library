---
title: 'Stat243: Problem Set 2, Due Friday Sept. 20'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps2.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/ps/ps2.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: Problem Set 2, Due Friday Sept. 20

**Source:** [`ps/ps2.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps2.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

September 12, 2019

Comments:

- This covers material in Units 3 and 4.

- It’s due at 2 pm on September 20, **both submitted as a PDF to bCourses as well as committed to your Github repository** as documented in the _howtos/submitting-electronically.txt_ file.

- Please note my comments in the syllabus about when to ask for help and about working together. In particular, **please give the names of any other students that you worked with on the problem set and indicate in comments any ideas or code you borrowed from another student.**

Formatting requirements

1. Your electronic solution should be in the form of an R markdown file named _ps2.Rmd_ or a L<sup>A</sup> TEX+knitr file named _ps2.Rtex_ , with bash and R code chunks included in the file (or read in from separate code files). Please see the _dynamic documents_ tutorial or Lab 1 materials for more information on how to do this.

2. Your PDF submission should be the PDF produced from your Rmd/Rtex. Your Github submission should include the Rtex/Rmd file, any code files containing chunks that you read into your Rtex/Rmd file, and the final PDF, all named according to the guidelines in _howtos/submitting-electronically.txt_ .

3. For problem 2, all of your operations should be done using UNIX tools (with the possible exception mentioned in the problem). Also, ALL of your work should be done using shell commands that you save in your solution file. So you can’t say “I downloaded the data from such-and-such website” or “I unzipped the file”; you need to give us the bash code that we could run to repeat what you did. This is partly for practice in writing shell code and partly to enforce the idea that your work should be reproducible and documented.

4. You will probably need to use _sed_ in a basic way as we have used it so far in class and in the tutorial on bash. You should not need to use more advanced functionality nor should you need to use _awk_ , but you may if you want to.

5. Your solution should not just be code - you should have text describing how you approached the problem and what the various steps were.

6. Your code should have comments indicating what each function or block of code does, and for any lines of code or code constructs that may be hard to understand, a comment indicating what that code does. You do not need to show exhaustive output but in general you should show short examples of what your code does to demonstrate its functionality.

1

## **Problems**

1. Add assertions and testing for your code from Problem 4 of PS1. You may use a modified version of your PS1 solution, perhaps because you found errors in what you did.

   - (a) Add formal assertions using the _assertthat_ package. You should try to catch the various incorrect inputs a user could provide and anything else that could go wrong (e.g., what happens if one is not online?).

   - (b) Use the _testthat_ package to set up a small but thoughtful set of tests of your functions. In deciding on your tests, try to think about tricky cases that might cause problems.

2. This problem provides practice using shell scripting. We’ll use United Nations Food and Agriculture Organization (FAO) data on agricultural production that we saw in class. If you go to http://data.un.org/Explorer.aspx?d=FAO and click on “Crops”, you’ll see a bunch of agricultural products with “View data” links. Click on “apricots” as an example and you’ll see a “Download” button that allows you to download a CSV of the data. In class we inspected the HTTP requests that the site handles and found out that you can download a file directly via a URL in the following format: http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode: 526&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&s=countryName:asc, elementCode:asc,year:desc

That downloads the data for Item 526 (apricots). Note that you may need to put the http address inside double quotes when using a UNIX shell command to download it. Also make sure there are no carriage returns in the http address (I had to break the address above to fit on the page). You can see the itemCode for other products by hovering over “View Data” link for the relevant product.

- (a) Download the data for apricots. Extract the data, excluding the metadata and the global total, into another file. Then subset the data to the year 2005. Based on the “area harvested” determine the ten regions/countries using the most land to produce apricots. Now automate your analysis and examine the top five regions/countries for 1965, 1975, 1985, 1995, and 2005. (Do not just copy and paste your code one time for each of the years!)

Note: dealing with the comma separation in the file can be a problem as there are commas used inside character strings as well. You’ll probably want to convert the file to be delimited by something other than a comma - you can do this from the command line or if you would like to do it via R, you are allowed to use Rscript from the command line to run a little bit of R code to do the conversion. (Or if you know Python, feel free to do it from the command line via Python.)

   - (b) Write a bash function that takes as input a single item code (e.g., 526 for apricots, 572 for avocados), downloads the data, and prints out to the screen the data stored in the CSV file, such that the information could be piped to another UNIX command. Your function should detect if the user provides the wrong number of arguments and return a useful error message. It should also give useful help information if the user invokes the function as: “myfun -h”.

3. On Tuesday, September 24, the Lab will consist of a discussion of good practices in reproducible research and computing. In preparation, please do the following:

   - (a) Read **one** of these four items (you can read more if you want of course):

      - i. Read the Preface, the Basic Reproducible Workflow Template chapter and Lessons Learned chapters of the new-ish (Berkeley-produced) book: The Practice of Reproducible Research.

2

- ii. Gentzkow and Shapiro (http://www.brown.edu/Research/Shapiro/pdfs/CodeAndData.pdf) – this one is written from the perspective of social scientists.

- iii. Wilson et.al. (http://arxiv.org/pdf/1210.0530v3.pdf)

- iv. Millman and Perez

(https://github.com/berkeley-stat243/stat243-fall-2014/blob/master/section/millman-perez.pdf)

Based on what you read, please write down a substantive comment or question you have that is raised by this material and submit to this Google form (https://tinyurl.com/s243-repr) for our ease in collating them before section. In addition, include your comment/question here in your problem set solution.

- (b) (Nothing to turn in) When reading, please think about the following questions, which we will be discussing in section:

   - i. Are there practices suggested that seem particularly compelling to you? What about ones that don’t seem compelling to you?

   - ii. Do you currently use any of the practices described? Which ones, and why? Which ones do you not use and why (apart from just not being aware of them)?

   - iii. Why don’t researchers consistently utilize these principles/tools? Which ones might be the most/least used? Which ones might be the easiest/most difficult to implement?

   - iv. What principles and practices described apply more to analyses of data, and which apply more to software engineering? Which principles and practices apply to both?

- (c) (Nothing to turn in) Please skim through the paper _ps/clm.pdf_ **before Lab on September 24** (you don’t need to do this before you’ve turned in the problem set), focusing the Method section. In Lab, we’ll talk about the code the authors provide at https://github.com/andykrause/hhLocation and whether that code makes it easy to reproduce what they did in the paper. So you don’t need to read the paper in detail but try to get a sense for what they did in their analysis so that when you look at the code in Lab, you understand the context.

3

---

[Up: contents](../index.md)
