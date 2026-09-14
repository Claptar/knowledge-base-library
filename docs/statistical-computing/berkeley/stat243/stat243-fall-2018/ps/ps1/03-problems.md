---
title: Problems
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. This question is the class survey that you already filled out.

2. As preparation for the next couple units, please read the sections titled “Memory hierarchy” and “Cache in depth” in the following brief piece that talks about the difference between the CPU cache, main memory (RAM) and disk. You don’t need to follow all the technical details in the “Cache in depth” section.

3. A friend of mine is planning to get married in Death Valley National Park in March. She wants to hold it as late in March as possible but without having a high chance of a very hot day. This problem will automate the task of generating information about what day to hold the wedding on using data from https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/.

   - (a) Download yearly climate data for a set of years of interest into a new (temporary) subdirectory within your working directory. Do not download all the years and feel free to focus on a small number of years to reduce the amount of data you need to download. Note that data for Death Valley is only present in the last few decades. As you are processing the files, report the number of observations in each year by printing the information to the screen, including if there are no observations for that year.

   - (b) Subset to the station corresponding to Death Valley, to TMAX (maximum daily temperature), and to March, and put all the data into a single file. In subsetting to Death Valley, get the information programmatically from the _ghcnd-stations.txt_ file one level up in the website. Do NOT type in the station ID code when you retrieve the Death Valley data from the yearly files.

   - (c) Create an R chunk that makes a single plot of side-by-side boxplots containing the maximum daily temperature on each day in March.

   - (d) Now generalize your code from parts (a) and (b). Write a shell function that takes as arguments a string for identifying the location, the weather variable of interest, and the time period (i.e., the years of interest and the month of interest), and returns the results. Your function should detect if the user provides the wrong number of arguments or a string that doesn’t allow one to identify a single weather station and return a useful error message. It should also give useful help information if the user invokes the function as: “get_weather -h”. Finally the function should remove the raw downloaded data files.

Hint: to check for equality in an if statement, you generally need syntax like: if [ "var" == "7" ].

4. Your task here is to automatically download all the files ending in _.txt_ from this National Climate Data Center website: https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/. Your shell script should provide a status message to the user, telling the name of the file as it downloads each file. You should be able to use UNIX utilities to extract the individual file names from the HTML index file linked to above. Alternatively you may use tools from Unit 3, but any use of R should be done directly from the command line and should only involve a line or two of R code. Do not hard code the names of the .txt files into your code.

2

Note that when we work on webscraping in Unit 3, we’ll see more elegant ways to process HTML than we are using here, but doing it “manually” here is good for practicing with the shell commands and allows us to do quick-and-dirty processing.

5. This problem is actually just the formatting of this document.

   - (a) Have the document be correct formatted according to the requirements above. You don’t need to explicitly answer this sub-problem.

   - (b) (extra credit) The _reticulate_ package and R Markdown allow you now to have Python and R chunks in a document that interact with each other. Demonstrate the ability to use this functionality, in particular sending data from R to Python and back to R, with some processing done in Python (it doesn’t have to be complicated processing). There’s a blog post here to get you started: http://feedproxy.google.com/ _∼_ r/RBloggers/ _∼_ 3/76l-uQEOoiU/?utm_source=feedburner&utm_medium=email

3

---

[← Formatting requirements](02-formatting-requirements.md) · [Up: contents](index.md)
