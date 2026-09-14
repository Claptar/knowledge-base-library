---
title: Unit 07 — bigData Part 11 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — bigData Part 11 —

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Challenge** : Create a view with one row for every question-tag pair, including questions without any tags.

**Challenge** : Write a query that would return the displaynames of all of the users who have *never* posted a question. The NULL keyword will come in handy – it’s like ‘NA‘ in R. Hint: NULLs should be produced if you do an outer join.

### **2.14 SAS**

SAS is quite good at handling large datasets, storing them on disk rather than in memory. I have used SAS in the past for subsetting and merging large datasets. Then I will generally extract the data I need for statistical modeling and do the analysis in R.

Here’s an example of some SAS code for reading in a CSV followed by some subsetting and merging and then output.

/* we can use a pipe - in this case to remove carriage returns, */

- /* presumably because the CSV file was created in Windows */

filename tmp pipe "cat ~/shared/hei/gis/100w4kmgrid.csv | tr -d '\r'";

21

/* read in one data file */ data grid; infile tmp lrecl=500 truncover dsd firstobs=2; informat gridID x y landMask dataMask; input gridID x y landMask dataMask; run ; filename tmp pipe "cat ~/shared/hei/goes/Goes_int4km.csv | tr -d '\r'"; /* read in second data file */ data match; infile tmp lrecl=500 truncover dsd firstobs=2; informat goesID gridID areaInt areaPix; input goesID gridID areaInt areaPix; run ; /* need to sort before merging */ proc sort data=grid; by gridID; run; proc sort data=match; by gridID; run; /* notice some similarity to SQL */ data merged; merge match(in=in1) grid(in=in2); by gridID; /* key field */ if in1=1; /* also do some subsetting */ /* only keep certain fields */ keep gridID goesID x y landMask dataMask areaInt areaPix; run; /* do some subsetting */

22

data PA; /* new dataset */ set merged; /* original dataset */ if x<1900000 and x>1200000 and y<2300000 and y>1900000; run;

%let filename="~/shared/hei/code/model/GOES-gridMatchPA.csv"; /* output to CSV */ PROC EXPORT DATA= WORK.PA

OUTFILE= &filename DBMS=CSV REPLACE;

RUN;

Note that SAS is oriented towards working with data in a “data frame”-style format; i.e., rows as observations and columns as fields, with different fields of possibly different types. As you can see in the syntax above, the operations concentrate on transforming one dataset into another dataset.

---

[← count(distinct tag) ## 1 41006](10-count-distinct-tag-1-41006.md) · [Up: contents](index.md) · [3 R and big data →](12-3-r-and-big-data.md)
