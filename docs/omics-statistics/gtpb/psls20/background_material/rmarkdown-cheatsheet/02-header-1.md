---
title: Header 1
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/rmarkdown-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Header 1

**Source:** [`background_material/rmarkdown-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## Header 2

### Header 3 #### Header 4 ##### Header 5 ###### Header 6

endash: -- emdash: --ellipsis: ... inline equation: $A = \pi*r^{2}$ image: ![](https://raw.githubusercontent.com/GTPB/PSLS20/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/path/to/smallorb.png) horizontal rule (or slide break):


***

> block quote

- unordered list * item 2 + sub-item 1 + sub-item 2

1. ordered list

2. item 2

- + sub-item 1

- + sub-item 2

Table Header  | Second Header ------------- | ------------Table Cell    | Cell 2 Cell 3        | Cell 4

RStudio® is a trademark of RStudio, Inc.  • <u>CC BY RStudio •  info@rstudio.com  •  844-448-1212 • rstudio.com</u>

**5. Embed Code** Use knitr syntax to embed R code into your report. R will run the code and include the results when you render your report.

### **6. Render** Use your .Rmd file as a blueprint to build a finished report.

##### **inline code**

##### **code chunks**

Start a chunk with ```{r}. End a chunk with ```

Surround code with back ticks and r. R replaces inline code with its results.


```
Here’s some code
```{r}
dim(iris)
```
```


```
Two plus two
equals `r 2 + 2`.
```

##### **display options**

Use knitr options to style the output of a chunk. Place options in brackets above the chunk.


Render your report in one of two ways

1. Run **rmarkdown::render("<file path>")**

2. Click the **knit HTML** button at the top of the RStudio scripts pane

When you render, R will

- execute each embedded code chunk and insert the results into your report

- build a new version of your report in the output file type

- open a preview of the output file in the viewer pane

- save the output file in your working directory


```
Here’s some code
```{r eval=FALSE}
dim(iris)
```
```

```
Here’s some code
```{r echo=FALSE}
dim(iris)
```
```

|**option**|**default**|**effect**|
|---|---|---|
|`eval`|TRUE|Whether to evaluate the code and include its results|
|`echo`|TRUE|Whether to display code along with its results|
|`warning`|TRUE|Whether to display warnings|
|`error`|FALSE|Whether to display errors|
|`message`|TRUE|Whether to display messages|
|`tidy`|FALSE|Whether to reformat code in a tidy way when displaying it|
|`results`|"markup"|"markup", "asis", "hold", or "hide"|
|`cache`|FALSE|Whether to cache results for future renders|
|`comment`|"##"|Comment character to preface results with|
|`fig.width`|7|Width in inches for plots created in chunk|
|`fig.height`|7|Height in inches for plots created in chunk|


For more details visit <u>yihui.name/knitr/</u>

**7. Interactive Docs** Turn your report into an interactive Shiny document in 3 steps


<!-- Start of picture text -->
1 Add  runtime: shiny 2 In the code chunks,  add Shiny  3 Render with<br>to the YAML header input  functions to embed widgets.  rmarkdown::run   or<br>Add Shiny  render  functions to  click  Run Document<br>embed reactive output in RStudio<br>---  ---<br>title: "Line graph"  title: "Line graph"<br>output: html_document  output: html_document<br>runtime: shiny  runtime: shiny<br>---  ---<br>Choose a time series:  Choose a time series:<br>```{r echo = FALSE}  ```{r echo = FALSE}<br>selectInput("data", "",   selectInput("data", "",<br>  c("co2", "lh"))    c("co2", "lh"))<br>```  ```<br>See a plot:  See a plot:<br>```{r echo = FALSE}  ```{r echo = FALSE}<br>renderPlot({  renderPlot({<br>  d <- get(input$data)    d <- get(input$data)<br>  plot(d)    plot(d)<br>}) ``` })  ```<br><!-- End of picture text -->

***** _Note: your report will be a Shiny app, which means you must choose an html output format, like_ **_html_document_** _(for an interactive report) or_ **_ioslides_presentation_** _(for an interactive slideshow)._

## **8. Publish** Share your report where users can visit it online

## **9. Learn More**

#### **Rpubs.com**

Share non-interactive documents on RStudio’s free  R Markdown publishing site **<u>www.rpubs.com</u>**

#### **ShinyApps.io**

Host an interactive document on RStudio’s server. Free and paid options **<u>www.shinyapps.io</u>**

Click the "Publish" button in the RStudio preview window to publish to rpubs.com with one click.zzzz


**Documentation and examples** - rmarkdown.rstudio.com **Further Articles** - shiny.rstudio.com/articles

- - blog.rstudio.com

- - @rstudio


RStudio® and Shiny™ are trademarks of RStudio, Inc. <u>CC BY RStudio  info@rstudio.com</u> 844-448-1212 rstudio.com

---

[← R Markdown Cheat Sheet](01-r-markdown-cheat-sheet.md) · [Up: contents](index.md)
