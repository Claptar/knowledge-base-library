---
title: R Markdown Cheat Sheet
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/rmarkdown-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# R Markdown Cheat Sheet

**Source:** [`background_material/rmarkdown-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

learn more at <u>rmarkdown.rstudio.com</u>

rmarkdown  0.2.50 Updated: 8/14


**1. Workflow** R Markdown is a format for writing reproducible, dynamic reports with R. Use it to embed R code and results into slideshows, pdfs, html documents, Word files and more. To make a report:

**i. Open** - Open a file that **ii. Write** - Write content with the **iii. Embed** - Embed R code that **iv. Render** - Replace R code with its output and transform uses the .Rmd extension. easy to use R Markdown syntax creates output to include in the report the report into a slideshow, pdf, html or ms Word file.


<!-- Start of picture text -->
A report.   A report.   A report.   A report.<br>A plot:  A plot:  A plot:  A plot: Microsoft<br>.Rmd = = Word<br>```{r}  ```{r}  ```{r}<br>hist(co2) ``` hist(co2) ``` hist(co2) ``` Reveal.js<br>ioslides, Beamer<br><!-- End of picture text -->

**2. Open File** Start by saving a text file with the extension .Rmd, or open an RStudio Rmd template

#### **3. Markdown** Next, write your report in plain text. Use markdown syntax to describe how to format text in the final report.

- In the menu bar, click **File ▶ New File ▶ R Markdown…**

- A window will open. Select the class of output you would like to make with your .Rmd file

- Select the specific type of output to make with the radio buttons (you can change this later)

- Click OK


#### **4. Choose Output** Write a YAML header that explains what type of document to build from your R Markdown file.

**YAML** **`--- title: "Untitled" author: "Anonymous"`** The RStudio A YAML header is a set of key: **`output: html_document`** value pairs at the start of your **`---`** template writes the YAML header file. Begin and end the header `This is the start of my` with a line of three dashes (- - -) `report. The above is metadata saved in a YAML header.` for you

The output value determines which type of file R will build from your .Rmd file (in Step 6)


**output: html_document** html file (web page) **output: pdf_document** pdf document **output: word_document** Microsoft Word .docx **output: beamer_presentation** beamer slideshow (pdf) **output: ioslides_presentation** ioslides slideshow (html)


###### **becomes**

###### **syntax**


Plain text End a line with two spaces to start a new paragraph. *italics* and _italics_ **bold** and __bold__ superscript^2^ ~~strikethrough~~ $$link$$(www.rstudio.com)

---

[Up: contents](index.md) · [Header 1 →](02-header-1.md)
