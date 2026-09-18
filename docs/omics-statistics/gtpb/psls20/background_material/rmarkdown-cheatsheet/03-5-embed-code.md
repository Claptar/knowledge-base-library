---
title: 5. Embed Code
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/rmarkdown-cheatsheet.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`background_material/rmarkdown-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5. Embed Code

Use knitr syntax to embed R code into your report. R will run the code and include the results
when you render your report.

**inline code**

Surround code with back ticks and r. R replaces inline code with its results.

Example: `` Two plus two equals `r 2 + 2`. `` becomes "Two plus two equals 4."

**code chunks**

Start a chunk with ```` ```{r} ````. End a chunk with ```` ``` ````.

Example:

````
Here's some code
```{r}
dim(iris)
```
````

becomes "Here's some code" followed by the printed chunk:

```
dim(iris)

## [1] 150  5
```

**display options**

Use knitr options to style the output of a chunk. Place options in brackets above the chunk.

Example with `eval=FALSE`:

````
Here's some code
```{r eval=FALSE}
dim(iris)
```
````

becomes "Here's some code" followed by just the (unevaluated) code shown:

```
dim(iris)
```

Example with `echo=FALSE`:

````
Here's some code
```{r echo=FALSE}
dim(iris)
```
````

becomes "Here's some code" followed by just the result:

```
## [1] 150  5
```

| option | default | effect |
| --- | --- | --- |
| `eval` | `TRUE` | Whether to evaluate the code and include its results |
| `echo` | `TRUE` | Whether to display code along with its results |
| `warning` | `TRUE` | Whether to display warnings |
| `error` | `FALSE` | Whether to display errors |
| `message` | `TRUE` | Whether to display messages |
| `tidy` | `FALSE` | Whether to reformat code in a tidy way when displaying it |
| `results` | `"markup"` | `"markup"`, `"asis"`, `"hold"`, or `"hide"` |
| `cache` | `FALSE` | Whether to cache results for future renders |
| `comment` | `"##"` | Comment character to preface results with |
| `fig.width` | `7` | Width in inches for plots created in chunk |
| `fig.height` | `7` | Height in inches for plots created in chunk |

For more details visit yihui.name/knitr/

## 6. Render

Use your .Rmd file as a blueprint to build a finished report.

Render your report in one of two ways

1. Run `rmarkdown::render("<file path>")`
2. Click the **knit HTML** button at the top of the RStudio scripts pane

When you render, R will

- execute each embedded code chunk and insert the results into your report
- build a new version of your report in the output file type
- open a preview of the output file in the viewer pane
- save the output file in your working directory

A screenshot shows an RStudio script editor tab "Untitled2*" with a YAML header beginning `---`,
`title: "Un...`, `author: "A...`, `date: "Jul...`, `output: ht...`, `---` (partly hidden behind the
dropdown in the mockup), and the **Knit HTML** split button open, showing menu items **Knit HTML**
(checked), **Knit PDF**, **Knit Word**, a separator, then **View in Pane** (checked) and **View in
Window**.

## 7. Interactive Docs

Turn your report into an interactive Shiny document in 3 steps

**1.** Add **runtime: shiny** to the YAML header

```yaml
---
title: "Line graph"
output: html_document
runtime: shiny
---
```

**2.** In the code chunks, add Shiny **input** functions to embed widgets. Add Shiny **render**
functions to embed reactive output

````
---
title: "Line graph"
output: html_document
runtime: shiny
---

Choose a time series:
```{r echo = FALSE}
selectInput("data", "",
  c("co2", "lh"))
```

See a plot:
```{r echo = FALSE}
renderPlot({
  d <- get(input\$data)
  plot(d)
})
```
````

**3.** Render with **rmarkdown::run** or click **Run Document** in RStudio

The resulting app is shown titled "Line graph", with a "Choose a time series:" label above a
dropdown showing "co2", and a "See a plot:" label above a line graph (y-axis `d` from about 310 to
370, x-axis `Time` from 1960 to 1990) showing a rising, oscillating series.

*Note: your report will be a Shiny app, which means you must choose an html output format, like
**html_document** (for an interactive report) or **ioslides_presentation** (for an interactive
slideshow).*

## 8. Publish

Share your report where users can visit it online

**Rpubs.com**

Share non-interactive documents on RStudio's free R Markdown publishing site www.rpubs.com

**ShinyApps.io**

Host an interactive document on RStudio's server. Free and paid options www.shinyapps.io

Click the "Publish" button in the RStudio preview window to publish to rpubs.com with one click.

A screenshot shows the RStudio pane tabs Files / Plots / Packages / Help / Viewer, with a
**Publish** button (globe icon) circled beneath the Viewer tab.

## 9. Learn More

Documentation and examples - rmarkdown.rstudio.com

Further Articles - shiny.rstudio.com/articles

- blog.rstudio.com
- @rstudio

---

[← 3. Markdown](02-3-markdown.md) · [Up: contents](index.md)
