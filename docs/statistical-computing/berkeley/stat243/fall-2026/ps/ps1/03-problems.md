---
title: Problems
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/ps/ps1.qmd
source_file: sources/berkeley-stat243/fall-2026/ps/ps1.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps1.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/ps/ps1.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

1. Please read [these lecture notes](https://36-750.github.io/tools/computer-architecture) about how computers work, used in a class on statistical computing at CMU. Briefly (a few sentences) describe the difference between disk and memory based on that reference and/or other resources you find. If you're doing an data analysis, you should have an understanding of what situations might lead to running out of disk space and what situations might lead to running out of memory.

2. A friend of mine is planning to get married in Death Valley National
    Park in March (this problem is based on real events...). She
    wants to hold it as late in March as possible but without having a
    high chance of a very hot day. This problem will automate the task
    of generating information about what day of March to hold the wedding
    using data from the [Global Historical Climatology Network](https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_year).
    All of your operations should be done using the bash shell except
    part (c). Also, ALL of your work should be done using shell commands
    that you save in your solution file. So you can't say "I downloaded
    the data from such-and-such website" or "I unzipped the file"; you
    need to provide the bash code that someone else could run to repeat what you
    did. This is partly for practice in writing shell code and partly to
    enforce the idea that your work should be reproducible and
    documented.

    a.  Download yearly climate data from the location above for a set of years of interest into
        a temporary directory. Do
        not download all the years and feel free to focus on a small
        number of years to reduce the amount of data you need to
        download (unzipped, some of the yearly files are as big as ~1 GB). Note that data for Death Valley is only present in the
        last few decades. As you are processing the files, report the
        number of observations in each year by printing the information
        to the screen (i.e., `stdout`), including if there are no observations for that
        year. Try to avoid printing anything else out (e.g., the progress of the downloading).

    b.  Subset to the station corresponding to Death Valley, to the TMAX
        (maximum daily temperature) variable, and to March, and put all the data
        into a single file. In subsetting to Death Valley, get the
        information programmatically from the `ghcnd-stations.txt` file
        one level up on the website. Do NOT type (hard code) in the station ID code
        when you retrieve the Death Valley data from the yearly files.

    c.  Write a small Python script (or R would be fine too) that takes as input your single file from (b)
        and makes a single plot showing side-by-side boxplots containing the
        maximum daily temperatures on each calendar day in March. Note that by creating a script and calling that from the shell you should avoid the challenges of mixing bash and Python chunks discussed in the Quarto references above.

    d.  Now generalize your code from parts (a) and (b). Write a shell
        function whose arguments allow the user to specify (1) a string for identifying the
        location (this string should not be the station ID), (2) the weather variable of interest, and (3) the time period
        (i.e., the years of interest and the month of interest), and
        returns the results (and in this case don't print out the information about the number of rows). Your function should detect if the user
        provides the wrong number of arguments or a string that doesn't
        allow one to identify a single weather station and return a
        useful error message. It should also give useful help
        information if the user invokes the function as: `get_weather -h`. Finally the function should remove the raw downloaded data
        files (alternatively, you should download such files into your operating system's temporary file location).

---

[← Formatting requirements](02-formatting-requirements.md) · [Up: contents](index.md)
