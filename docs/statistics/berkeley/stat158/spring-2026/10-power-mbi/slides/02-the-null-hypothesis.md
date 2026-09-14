---
title: The Null Hypothesis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/10-power-mbi/slides.html
source_file: sources/berkeley-stat158/spring-2026/10-power-mbi/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# The Null Hypothesis

**Source:** [`10-power-mbi/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/10-power-mbi/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Recall the data

<style>#ilhhlftndu table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ilhhlftndu thead, #ilhhlftndu tbody, #ilhhlftndu tfoot, #ilhhlftndu tr, #ilhhlftndu td, #ilhhlftndu th {
  border-style: none;
}

#ilhhlftndu p {
  margin: 0;
  padding: 0;
}

#ilhhlftndu .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#ilhhlftndu .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ilhhlftndu .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#ilhhlftndu .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#ilhhlftndu .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#ilhhlftndu .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ilhhlftndu .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#ilhhlftndu .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#ilhhlftndu .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#ilhhlftndu .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ilhhlftndu .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ilhhlftndu .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#ilhhlftndu .gt_spanner_row {
  border-bottom-style: hidden;
}

#ilhhlftndu .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}

#ilhhlftndu .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#ilhhlftndu .gt_from_md > :first-child {
  margin-top: 0;
}

#ilhhlftndu .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ilhhlftndu .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#ilhhlftndu .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#ilhhlftndu .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#ilhhlftndu .gt_row_group_first td {
  border-top-width: 2px;
}

#ilhhlftndu .gt_row_group_first th {
  border-top-width: 2px;
}

#ilhhlftndu .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ilhhlftndu .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ilhhlftndu .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ilhhlftndu .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ilhhlftndu .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ilhhlftndu .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ilhhlftndu .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ilhhlftndu .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ilhhlftndu .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ilhhlftndu .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#ilhhlftndu .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ilhhlftndu .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#ilhhlftndu .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ilhhlftndu .gt_left {
  text-align: left;
}

#ilhhlftndu .gt_center {
  text-align: center;
}

#ilhhlftndu .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ilhhlftndu .gt_font_normal {
  font-weight: normal;
}

#ilhhlftndu .gt_font_bold {
  font-weight: bold;
}

#ilhhlftndu .gt_font_italic {
  font-style: italic;
}

#ilhhlftndu .gt_super {
  font-size: 65%;
}

#ilhhlftndu .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ilhhlftndu .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ilhhlftndu .gt_indent_1 {
  text-indent: 5px;
}

#ilhhlftndu .gt_indent_2 {
  text-indent: 10px;
}

#ilhhlftndu .gt_indent_3 {
  text-indent: 15px;
}

#ilhhlftndu .gt_indent_4 {
  text-indent: 20px;
}

#ilhhlftndu .gt_indent_5 {
  text-indent: 25px;
}

#ilhhlftndu .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ilhhlftndu div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Data</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="d_i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">d_i</th>
<th id="y_i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">y_i</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-0.50</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-1.40</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">0.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">1.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.50</td>
</tr>
</tbody>
</table>

Summary Statistics:

<span class="math display">\\$$ n\_1, n\_0, s\_1, s\_0, \\hat{\\bar{Y}}\_1, \\hat{\\bar{Y}}\_1 \\$$</span>

## The Null Distribution

If:

1.  <span class="math inline">\$Y\_i \\sim N(\\mu\_j, \\sigma^2)\$</span>
2.  <span class="math inline">\$H\_0: \\mu\_1 - \\mu\_0 = 0\$</span>
3.  <span class="math inline">\$T = \\frac{\\hat{\\bar{Y}}\_1 - \\hat{\\bar{Y}}\_0}{\\hat{SE}}\$</span>

Then:

<span class="math display">\\$$ T\_{H\_0} \\sim t(df = n\_1 + n\_0 - 2) \\$$</span>

## R toolkit

<span class="math display">\\$$ T\_{H\_0} \\sim t(df = n\_1 + n\_0 - 2) \\$$</span>

Quantiles

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
qt(quantile, df)
```

CDF (Distribution function)

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
pt(x)
```

## From data to schedule {data-id="quarto-animate-title"}

<style>#vyjishoxub table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#vyjishoxub thead, #vyjishoxub tbody, #vyjishoxub tfoot, #vyjishoxub tr, #vyjishoxub td, #vyjishoxub th {
  border-style: none;
}

#vyjishoxub p {
  margin: 0;
  padding: 0;
}

#vyjishoxub .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#vyjishoxub .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#vyjishoxub .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#vyjishoxub .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#vyjishoxub .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#vyjishoxub .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vyjishoxub .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#vyjishoxub .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#vyjishoxub .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#vyjishoxub .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#vyjishoxub .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#vyjishoxub .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#vyjishoxub .gt_spanner_row {
  border-bottom-style: hidden;
}

#vyjishoxub .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}

#vyjishoxub .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#vyjishoxub .gt_from_md > :first-child {
  margin-top: 0;
}

#vyjishoxub .gt_from_md > :last-child {
  margin-bottom: 0;
}

#vyjishoxub .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#vyjishoxub .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#vyjishoxub .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#vyjishoxub .gt_row_group_first td {
  border-top-width: 2px;
}

#vyjishoxub .gt_row_group_first th {
  border-top-width: 2px;
}

#vyjishoxub .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#vyjishoxub .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#vyjishoxub .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#vyjishoxub .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vyjishoxub .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#vyjishoxub .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#vyjishoxub .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#vyjishoxub .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#vyjishoxub .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vyjishoxub .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#vyjishoxub .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#vyjishoxub .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#vyjishoxub .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#vyjishoxub .gt_left {
  text-align: left;
}

#vyjishoxub .gt_center {
  text-align: center;
}

#vyjishoxub .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#vyjishoxub .gt_font_normal {
  font-weight: normal;
}

#vyjishoxub .gt_font_bold {
  font-weight: bold;
}

#vyjishoxub .gt_font_italic {
  font-style: italic;
}

#vyjishoxub .gt_super {
  font-size: 65%;
}

#vyjishoxub .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#vyjishoxub .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#vyjishoxub .gt_indent_1 {
  text-indent: 5px;
}

#vyjishoxub .gt_indent_2 {
  text-indent: 10px;
}

#vyjishoxub .gt_indent_3 {
  text-indent: 15px;
}

#vyjishoxub .gt_indent_4 {
  text-indent: 20px;
}

#vyjishoxub .gt_indent_5 {
  text-indent: 25px;
}

#vyjishoxub .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#vyjishoxub div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Data</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="d_i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">d_i</th>
<th id="y_i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">y_i</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-0.50</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-1.40</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">0.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">1.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.50</td>
</tr>
</tbody>
</table>

<style>#ccbznxyodm table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ccbznxyodm thead, #ccbznxyodm tbody, #ccbznxyodm tfoot, #ccbznxyodm tr, #ccbznxyodm td, #ccbznxyodm th {
  border-style: none;
}

#ccbznxyodm p {
  margin: 0;
  padding: 0;
}

#ccbznxyodm .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#ccbznxyodm .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ccbznxyodm .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#ccbznxyodm .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#ccbznxyodm .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#ccbznxyodm .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ccbznxyodm .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#ccbznxyodm .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#ccbznxyodm .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#ccbznxyodm .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ccbznxyodm .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ccbznxyodm .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#ccbznxyodm .gt_spanner_row {
  border-bottom-style: hidden;
}

#ccbznxyodm .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}

#ccbznxyodm .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#ccbznxyodm .gt_from_md > :first-child {
  margin-top: 0;
}

#ccbznxyodm .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ccbznxyodm .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#ccbznxyodm .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#ccbznxyodm .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#ccbznxyodm .gt_row_group_first td {
  border-top-width: 2px;
}

#ccbznxyodm .gt_row_group_first th {
  border-top-width: 2px;
}

#ccbznxyodm .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ccbznxyodm .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ccbznxyodm .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ccbznxyodm .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ccbznxyodm .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ccbznxyodm .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ccbznxyodm .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ccbznxyodm .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ccbznxyodm .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ccbznxyodm .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#ccbznxyodm .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ccbznxyodm .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#ccbznxyodm .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ccbznxyodm .gt_left {
  text-align: left;
}

#ccbznxyodm .gt_center {
  text-align: center;
}

#ccbznxyodm .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ccbznxyodm .gt_font_normal {
  font-weight: normal;
}

#ccbznxyodm .gt_font_bold {
  font-weight: bold;
}

#ccbznxyodm .gt_font_italic {
  font-style: italic;
}

#ccbznxyodm .gt_super {
  font-size: 65%;
}

#ccbznxyodm .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ccbznxyodm .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ccbznxyodm .gt_indent_1 {
  text-indent: 5px;
}

#ccbznxyodm .gt_indent_2 {
  text-indent: 10px;
}

#ccbznxyodm .gt_indent_3 {
  text-indent: 15px;
}

#ccbznxyodm .gt_indent_4 {
  text-indent: 20px;
}

#ccbznxyodm .gt_indent_5 {
  text-indent: 25px;
}

#ccbznxyodm .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ccbznxyodm div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Observed Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="Y_0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_0</th>
<th id="Y_1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_1</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="Y_0">-0.5</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="Y_0">-1.4</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="Y_0">0.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="Y_0">-1.0</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="Y_0">1.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.50</td>
</tr>
</tbody>
</table>

## From data to schedule {data-id="quarto-animate-title"}

<style>#tdibymlvit table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#tdibymlvit thead, #tdibymlvit tbody, #tdibymlvit tfoot, #tdibymlvit tr, #tdibymlvit td, #tdibymlvit th {
  border-style: none;
}

#tdibymlvit p {
  margin: 0;
  padding: 0;
}

#tdibymlvit .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#tdibymlvit .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#tdibymlvit .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#tdibymlvit .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#tdibymlvit .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#tdibymlvit .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#tdibymlvit .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#tdibymlvit .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#tdibymlvit .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#tdibymlvit .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#tdibymlvit .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#tdibymlvit .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#tdibymlvit .gt_spanner_row {
  border-bottom-style: hidden;
}

#tdibymlvit .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}

#tdibymlvit .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#tdibymlvit .gt_from_md > :first-child {
  margin-top: 0;
}

#tdibymlvit .gt_from_md > :last-child {
  margin-bottom: 0;
}

#tdibymlvit .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#tdibymlvit .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#tdibymlvit .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#tdibymlvit .gt_row_group_first td {
  border-top-width: 2px;
}

#tdibymlvit .gt_row_group_first th {
  border-top-width: 2px;
}

#tdibymlvit .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#tdibymlvit .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#tdibymlvit .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#tdibymlvit .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#tdibymlvit .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#tdibymlvit .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#tdibymlvit .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#tdibymlvit .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#tdibymlvit .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#tdibymlvit .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#tdibymlvit .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#tdibymlvit .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#tdibymlvit .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#tdibymlvit .gt_left {
  text-align: left;
}

#tdibymlvit .gt_center {
  text-align: center;
}

#tdibymlvit .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#tdibymlvit .gt_font_normal {
  font-weight: normal;
}

#tdibymlvit .gt_font_bold {
  font-weight: bold;
}

#tdibymlvit .gt_font_italic {
  font-style: italic;
}

#tdibymlvit .gt_super {
  font-size: 65%;
}

#tdibymlvit .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#tdibymlvit .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#tdibymlvit .gt_indent_1 {
  text-indent: 5px;
}

#tdibymlvit .gt_indent_2 {
  text-indent: 10px;
}

#tdibymlvit .gt_indent_3 {
  text-indent: 15px;
}

#tdibymlvit .gt_indent_4 {
  text-indent: 20px;
}

#tdibymlvit .gt_indent_5 {
  text-indent: 25px;
}

#tdibymlvit .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#tdibymlvit div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Observed Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="Y_0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_0</th>
<th id="Y_1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_1</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="Y_0">-0.5</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="Y_0">-1.4</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="Y_0">0.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="Y_0">-1.0</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="Y_0">1.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.50</td>
</tr>
</tbody>
</table>

<style>#altelotrub table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#altelotrub thead, #altelotrub tbody, #altelotrub tfoot, #altelotrub tr, #altelotrub td, #altelotrub th {
  border-style: none;
}

#altelotrub p {
  margin: 0;
  padding: 0;
}

#altelotrub .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#altelotrub .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#altelotrub .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#altelotrub .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#altelotrub .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#altelotrub .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#altelotrub .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#altelotrub .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#altelotrub .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#altelotrub .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#altelotrub .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#altelotrub .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#altelotrub .gt_spanner_row {
  border-bottom-style: hidden;
}

#altelotrub .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}

#altelotrub .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#altelotrub .gt_from_md > :first-child {
  margin-top: 0;
}

#altelotrub .gt_from_md > :last-child {
  margin-bottom: 0;
}

#altelotrub .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#altelotrub .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#altelotrub .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#altelotrub .gt_row_group_first td {
  border-top-width: 2px;
}

#altelotrub .gt_row_group_first th {
  border-top-width: 2px;
}

#altelotrub .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#altelotrub .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#altelotrub .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#altelotrub .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#altelotrub .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#altelotrub .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#altelotrub .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#altelotrub .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#altelotrub .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#altelotrub .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#altelotrub .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#altelotrub .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#altelotrub .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#altelotrub .gt_left {
  text-align: left;
}

#altelotrub .gt_center {
  text-align: center;
}

#altelotrub .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#altelotrub .gt_font_normal {
  font-weight: normal;
}

#altelotrub .gt_font_bold {
  font-weight: bold;
}

#altelotrub .gt_font_italic {
  font-style: italic;
}

#altelotrub .gt_super {
  font-size: 65%;
}

#altelotrub .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#altelotrub .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#altelotrub .gt_indent_1 {
  text-indent: 5px;
}

#altelotrub .gt_indent_2 {
  text-indent: 10px;
}

#altelotrub .gt_indent_3 {
  text-indent: 15px;
}

#altelotrub .gt_indent_4 {
  text-indent: 20px;
}

#altelotrub .gt_indent_5 {
  text-indent: 25px;
}

#altelotrub .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#altelotrub div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Null Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="Y_0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_0</th>
<th id="Y_1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_1</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="Y_0">0.90</td>
<td class="gt_row gt_right" headers="Y_1">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="Y_0">-0.50</td>
<td class="gt_row gt_right" headers="Y_1">-0.50</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="Y_0">2.20</td>
<td class="gt_row gt_right" headers="Y_1">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="Y_0">-1.40</td>
<td class="gt_row gt_right" headers="Y_1">-1.40</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="Y_0">0.10</td>
<td class="gt_row gt_right" headers="Y_1">0.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="Y_0">-1.00</td>
<td class="gt_row gt_right" headers="Y_1">-1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="Y_0">1.10</td>
<td class="gt_row gt_right" headers="Y_1">1.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="Y_0">1.00</td>
<td class="gt_row gt_right" headers="Y_1">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="Y_0">1.02</td>
<td class="gt_row gt_right" headers="Y_1">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="Y_0">1.50</td>
<td class="gt_row gt_right" headers="Y_1">1.50</td>
</tr>
</tbody>
</table>

## Estimate Dist under H0

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
rand_stats <- function(schedule, d_i, stat = "diff in means", reps = 1000) {
  # store treatment vector separately
  d_i_vec <- d_i

  # replicate the schedule reps times and stack them on top of one another
  randomized_exp_df <- map_dfr(1:reps, ~ schedule, .id = "experiment") |>
    mutate(experiment = factor(experiment, levels = as.character(1:reps), ordered = TRUE),
           d_i = c(replicate(n = reps, sample(d_i_vec))),  # create random assignments
           y_i = Y_1 * d_i +  Y_0 * (1 - d_i)) |>    # find observed responses
    arrange(experiment)

  # calculate test statistic for every random assignment
  if (stat == "diff in means") {
    stats <- randomized_exp_df |>
      group_by(experiment, d_i) |>
      summarize(ybar = mean(y_i),     # average within each group within each experiment
                .groups = "drop_last") |>
      summarize(ATE_hat = diff(ybar),
                .groups = "drop") |>   # take the difference between the two groups mean
      pull()
  } else {
    stop("Statistic not implemented")
  }

  return(stats)
}
```

## Estimate Dist under H0 {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
H_0 <- rand_stats(schedule = my_null_sched, d_i = my_data$d_i, reps = 5000)
H_0
```

       [1]  0.144  0.064 -0.216 -0.904  0.144  0.784 -0.576 -0.824  0.864  0.136
      [11]  0.376 -0.224  0.584  0.056  0.504 -0.104 -0.064  0.136  1.696 -0.336
      [21]  0.824  0.264 -0.944 -0.216 -0.496  0.424  0.216  0.224 -0.904 -0.224
      [31]  0.056  0.416  0.904 -0.256 -0.584 -0.144 -0.224  0.336  0.496  0.416
      [41] -0.744  0.704 -0.304 -0.056 -1.344  0.176  1.096 -0.584  1.664  0.856
      [51] -0.304 -1.056 -1.144  0.176  0.696  0.856  0.064 -0.944 -0.424 -0.096
      [61]  0.464 -0.496 -0.264 -0.176 -1.104 -0.096 -0.376 -1.136 -0.536  0.296
      [71]  0.144 -1.104  0.176 -0.384 -0.064  0.216  1.136  0.864 -0.504 -0.344
      [81] -0.696 -0.544 -0.664 -0.776  1.104  0.104  0.664  0.544  0.304  1.104
      [91] -1.144  0.056  0.056  0.056  0.544 -0.056 -0.104 -0.144 -0.256 -0.736
     [101] -0.064  1.384 -1.104 -0.464 -0.296  1.224 -0.144  0.344  0.744  0.944
     [111] -1.104  1.104 -1.224  0.376 -0.384 -1.104 -1.096  0.224  0.296 -0.264
     [121] -1.744  0.104 -0.856  0.024 -0.384 -0.336 -0.136  0.864 -0.056 -0.704
     [131] -1.376 -0.944 -1.056 -0.336 -0.416 -0.136 -1.344 -0.544 -1.136 -0.336
     [141]  0.376 -0.056  1.144  0.696 -0.784 -1.376  0.176 -0.264 -0.536  0.224
     [151]  0.104  0.176  0.584 -0.304 -0.184 -0.664 -0.736  0.536  0.704 -1.104
     [161]  1.376 -0.384 -1.224 -0.104  0.864  0.016 -0.864  0.544 -0.304 -0.176
     [171]  0.104 -0.336  0.496 -0.736 -0.824  0.064  0.864  0.464 -0.704  0.384
     [181] -0.216 -0.384 -0.864 -0.904 -0.696 -1.104  1.504  1.056  1.296  0.896
     [191] -1.104  0.856  0.304 -0.176  0.664 -0.344 -0.544 -1.744 -0.584  0.056
     [201]  0.736 -0.664  0.736  0.136 -0.136  0.136 -0.064 -1.224 -0.496  0.784
     [211]  0.256  0.536 -1.136 -0.384 -0.424 -0.224  0.584  0.176 -0.504 -0.584
     [221] -0.224  0.176  0.224 -0.056 -0.016 -0.344 -0.336 -0.776  0.624 -0.584
     [231] -0.056  0.056 -0.496 -0.384  0.304  0.496  0.144 -1.144  1.136  0.064
     [241]  0.376 -0.736 -0.136 -0.664  0.504 -0.704 -0.064  0.544  0.784  0.624
     [251]  0.944  0.464 -1.704 -1.136  0.504  0.504  0.904  0.016 -0.696  0.056
     [261]  0.696  0.224  0.904  1.296 -0.584 -0.504  0.776  0.064 -0.696  0.336
     [271]  0.664 -0.464  0.384 -1.504  0.384  0.504 -0.744 -1.696 -0.584 -0.216
     [281]  0.576  0.216 -0.664 -0.544  0.104  0.256  1.104  0.864  0.224 -0.824
     [291]  1.136  1.104 -0.664  0.256  0.904  0.424 -0.144  0.264 -0.104 -0.416
     [301] -0.304 -0.264 -1.064 -0.896  0.144 -0.344 -1.224  0.896  0.336  0.384
     [311] -0.536  1.696  1.744  0.536 -0.736  0.336  0.424  0.136 -0.224  0.256
     [321]  0.256 -0.664 -1.376  1.664  0.224 -0.384  0.736 -1.296 -0.336 -0.616
     [331]  0.256 -0.216  1.696 -0.704 -1.136 -0.904  0.136 -0.544  0.256  0.096
     [341]  1.064  1.376  0.776 -0.704  1.504  0.704  0.144 -0.504 -0.864  0.696
     [351]  0.904 -1.144 -0.176 -0.904  0.904  0.416 -0.864 -0.224 -0.736  0.584
     [361]  0.864  0.264  0.464  0.944 -0.584 -0.544 -0.936  0.304  0.904  0.864
     [371]  1.104 -0.904  0.784  1.384 -0.536 -1.104 -0.504 -0.104 -0.304  0.104
     [381]  0.216  0.184 -0.336 -0.216 -0.176  1.744 -0.776 -0.496 -0.024 -0.904
     [391] -0.224  0.104 -1.304 -0.704  1.096 -0.264 -0.304 -0.576  0.784 -1.304
     [401] -0.056  0.824 -0.664  0.496  1.696 -0.904  0.024  0.224  0.136 -0.584
     [411]  0.464 -0.664  0.224 -1.336  0.216 -0.584 -1.336  0.056 -0.336 -0.104
     [421]  0.936 -1.224  0.664 -0.136 -0.944 -0.856 -1.096  1.696 -0.576 -0.584
     [431] -0.264 -0.304 -0.536 -1.376  0.576 -0.264  0.904  0.216 -0.096  0.024
     [441]  0.584  0.296  1.144 -0.584  0.176 -0.024 -0.584 -0.296 -1.104 -1.704
     [451] -1.184 -0.184 -0.776 -1.144  0.176 -0.344 -0.256  0.336 -0.896 -0.136
     [461] -0.144 -0.144  0.144 -0.056 -0.704  0.544 -1.296  0.896 -1.296  0.216
     [471]  0.384 -0.256  0.064 -0.384 -1.096 -1.104  1.296  0.336 -0.216  0.224
     [481] -0.224  0.824  0.304  0.216 -0.544 -0.496  0.664  0.144 -0.264  0.584
     [491]  0.496  1.384 -0.616  0.744  0.296 -0.744 -1.704  0.856  0.856  0.096
     [501] -1.664  0.424 -0.376  0.544 -0.296  0.576 -0.216  1.696  0.536  0.544
     [511]  0.384  0.496  0.576  1.664 -1.184 -0.024  0.904  1.064  0.856  1.096
     [521]  0.744 -0.024 -1.296  0.376  0.256  0.904 -0.256  1.144  0.064 -0.584
     [531] -0.544  0.424  0.496 -0.216 -0.944 -0.016 -0.544  0.176  0.736 -0.576
     [541]  0.776 -0.064  1.224  0.536 -0.136  0.056 -0.304 -0.736 -0.896 -0.696
     [551]  0.904 -0.024  1.336 -0.904  0.864 -0.496 -0.384  0.704  0.384 -0.864
     [561] -0.176  1.744  0.944  0.704  1.504  0.704 -1.344 -0.496  0.784 -0.216
     [571]  0.464  0.096  0.496 -0.064 -0.096 -0.856  0.584 -0.904 -0.224  1.056
     [581] -0.184 -0.504 -0.016  0.696 -0.344  0.384 -0.024  0.176 -0.144 -1.344
     [591]  0.144  0.024 -0.384  0.504  1.144  0.064 -0.136  0.224  0.584  0.696
     [601] -0.944 -1.296  0.104 -0.064 -0.304 -0.864  0.264  0.216 -0.056  0.904
     [611]  1.064  0.664  0.256 -0.536  0.296  0.576 -0.064 -1.344  0.536  0.296
     [621]  0.664 -0.224  0.304  0.136  0.144  0.384 -0.944  1.144  0.336 -1.504
     [631] -0.664  0.144  0.304  0.664 -0.296  0.496 -0.104  0.056 -0.024 -0.744
     [641]  0.384 -1.104 -1.224 -0.176 -0.376 -0.264  0.896  0.264  0.824  0.096
     [651]  0.936  0.096  0.464  0.776 -0.736 -0.904 -0.376 -0.056 -1.104  1.744
     [661] -1.344  1.104 -0.704 -1.056 -0.264 -0.704  0.544 -0.744 -0.056  0.856
     [671]  1.144  0.104 -1.224 -0.224 -0.136  0.584 -0.264  0.416  0.224 -1.096
     [681]  0.544 -0.104 -0.304  1.096 -0.144  0.296  0.384 -0.224 -0.216 -0.064
     [691]  1.224 -0.096 -0.616 -0.904 -0.576 -0.096  0.696  0.056  0.416  1.336
     [701] -1.704 -0.696 -0.744  0.696  0.224  0.856 -1.184 -0.576  1.336  0.264
     [711] -0.424  0.176  0.536  1.184 -0.896  0.496  0.744 -0.904  0.664 -0.296
     [721]  1.144 -0.256  0.576  0.296  1.304  0.104  0.904  0.536 -0.896  0.296
     [731] -0.904  0.064  1.376 -0.416 -0.304  0.736 -0.696 -0.224 -0.216 -0.616
     [741]  0.424 -1.224  0.944  0.056 -0.256  0.256 -0.296  0.256  1.504 -0.096
     [751]  0.416  0.096  0.376 -0.536  0.224 -0.704 -1.184  0.184 -0.376  0.864
     [761] -0.216  0.904  1.384 -0.824  0.304  0.144  1.136 -0.296  0.736  0.936
     [771]  0.096  0.344  0.856 -0.064  0.256 -0.384 -0.056 -0.096  0.136  0.944
     [781] -0.744  0.744  0.936 -1.664 -0.064  0.784  0.176 -0.224 -0.064 -1.136
     [791] -0.296  0.904 -1.104 -0.704  0.544  0.256  0.544 -0.496  0.256  1.376
     [801] -0.216 -0.696  0.496  0.664  1.184  0.536 -1.704 -1.136 -1.056  0.384
     [811] -0.336  0.464 -0.224 -0.304  0.136  0.424 -0.224  0.256 -0.024 -0.936
     [821] -0.856 -0.856 -0.056  0.944 -0.856  1.504  0.904  0.096  0.536 -0.136
     [831] -0.144  0.856 -1.376  0.944  0.304 -1.696 -0.536  0.904 -1.136  0.704
     [841]  0.856 -0.744 -0.176  0.864 -0.304  1.344 -0.064  1.144  0.344 -0.384
     [851]  0.584  0.304 -1.104 -1.184 -0.104 -0.184 -0.944  1.664 -0.624  1.664
     [861]  0.064  0.664 -0.104 -1.144 -0.664  1.064  1.136  0.856 -0.296  0.384
     [871] -0.064 -1.224  0.064 -0.696  0.224  0.664  0.776  1.104  1.504 -0.776
     [881]  0.144 -0.544  0.336 -0.776  1.344  1.136  0.224  0.744 -1.744  0.496
     [891] -1.696 -0.296 -0.256 -0.384 -0.416  0.936 -0.096  0.736 -0.576  1.296
     [901]  0.544  0.624  1.384 -0.136 -0.696 -1.184  0.064 -0.704 -0.424  0.096
     [911]  0.856  0.864  0.496 -0.416  1.744  0.224  0.224 -0.304  1.336  0.144
     [921]  1.184 -0.576 -1.104  0.296  1.344  1.336  0.096 -0.384 -0.584 -1.384
     [931] -0.016 -0.136  0.904 -0.776 -0.744 -0.104  1.744  0.336  0.936 -0.296
     [941] -1.064 -1.376  0.224  0.464 -0.256 -0.464 -0.696  0.136  0.096  1.696
     [951] -0.696 -0.336 -0.216 -0.416  0.864 -0.416 -0.016  0.136 -0.136  0.344
     [961]  1.104  0.344 -0.096  0.936 -0.336 -1.184 -0.944 -1.304  0.464  0.136
     [971]  1.504  0.424  0.336  0.776 -0.344 -0.416 -0.504 -0.256  0.864 -0.136
     [981]  0.624  0.536  0.144  1.696 -0.064 -0.024  1.064  1.504  0.424 -0.904
     [991]  0.136  0.904 -0.304  0.296  0.616  0.864  0.096 -0.576  0.856 -0.496
    [1001]  0.584  0.136 -0.696 -0.584  0.064  0.704 -0.096  0.464 -0.216  0.904
    [1011] -0.096  0.224 -0.776  0.304 -0.616 -0.376 -0.064  0.336 -0.144 -1.384
    [1021]  0.664 -0.296  0.736 -0.136  0.896  0.256 -1.064 -0.176  0.144  0.296
    [1031]  0.896  0.664 -0.696  0.224 -1.136  0.064  0.584  0.904  0.336 -0.056
    [1041]  0.664 -0.696  0.544 -1.296  0.096 -0.696  0.096  0.336 -0.864  0.784
    [1051] -0.864 -0.224  0.176  0.864 -0.296 -0.544 -1.064  0.624  0.624  0.384
    [1061]  0.224  0.104  1.056  0.016 -0.096  0.784  0.544  1.384  0.136 -1.296
    [1071] -1.104 -0.256 -0.864 -0.304 -0.224  0.104 -0.304 -0.096  0.216 -0.744
    [1081] -0.504 -0.104 -0.104  0.704 -0.944 -0.424  0.904 -1.104 -0.064  0.224
    [1091] -0.224  0.096  0.536  0.256  0.064  0.256 -0.136 -0.496 -0.296  0.256
    [1101]  1.504 -0.584  0.104 -0.664  0.224 -0.024 -1.184 -0.256 -0.136 -0.064
    [1111]  0.256 -0.576  0.704  0.664  1.056 -0.504  0.144  0.744 -0.536 -0.096
    [1121]  0.064 -0.024  0.664 -0.056  0.296 -0.304  0.696  1.384 -0.096 -0.544
    [1131]  0.776 -0.424  0.176 -0.584  0.424 -1.696 -0.224  0.864  0.144  0.536
    [1141] -0.024  1.296  0.696  1.344  0.104 -0.056  0.104  0.176  0.096 -0.664
    [1151]  0.136  0.376  1.696 -0.864  0.664  1.696  1.344  0.904 -0.224  0.704
    [1161]  0.024  0.384 -0.576  1.136  0.664 -0.736  0.904  0.696 -0.784  0.144
    [1171]  1.336 -0.144  0.936  0.184 -1.304  0.696  1.136 -1.336 -0.616  0.216
    [1181]  0.336 -0.304  1.104 -0.696  0.384  0.024  0.776  0.696  0.304 -0.536
    [1191]  0.704 -1.296  0.696  0.416  0.896  1.296  0.176  0.664 -0.056 -0.224
    [1201] -0.216  0.464  0.024  0.336 -0.584  0.616 -1.704 -0.224 -1.376 -0.056
    [1211]  0.264  0.536  0.904 -1.696 -0.776 -1.136  0.616  0.056 -0.904 -1.224
    [1221]  0.744 -1.224 -0.576  0.064  0.344  0.264  0.904  0.344 -0.896 -0.936
    [1231]  0.664 -0.184 -0.224  0.544 -0.664 -0.384 -0.256 -0.856  0.136 -0.104
    [1241] -0.904  0.264 -0.776  0.496 -0.104  0.536 -0.536  0.496 -0.744  0.864
    [1251]  0.464  0.224  0.224  0.424 -0.304  0.096 -0.336  0.104  0.424  0.096
    [1261]  0.104  0.224 -0.096 -0.736  0.096 -0.336 -0.704  0.696 -0.224 -0.424
    [1271]  0.776 -0.584 -1.136  1.664 -0.256 -0.304 -1.064  1.336  0.856 -1.144
    [1281] -0.104 -0.024  0.024  0.384 -0.664 -0.376  1.136 -0.336  1.064  0.296
    [1291]  0.264  0.304  0.224  0.624 -0.896  1.504  0.544 -0.904 -0.464  0.216
    [1301] -0.096 -0.504  0.104 -0.144 -0.696  0.024 -0.176 -0.416 -0.136  0.384
    [1311] -0.224 -0.344 -0.336  0.584  0.296  1.664  0.424  0.904  0.944 -0.176
    [1321]  0.496  0.096 -1.144  0.696  0.416  0.664 -0.104 -0.544 -0.784  1.296
    [1331] -0.896 -0.264 -1.184 -0.336 -0.304 -0.144 -0.224  0.184 -0.304  0.336
    [1341] -0.544  0.896 -1.376 -1.144 -0.824 -0.624  0.304 -0.416 -0.536 -0.904
    [1351] -0.904  0.256  1.504 -0.544  1.184  0.704  0.896  0.464  0.496  0.864
    [1361]  0.664 -0.336 -0.216  1.136 -0.224  0.304 -0.904 -0.104 -0.544 -0.344
    [1371]  1.304  0.304 -0.864 -0.576  0.936 -0.776  0.056 -1.136 -0.504 -0.864
    [1381] -0.504  0.024  0.544 -0.464  0.944  1.296 -0.096  0.664  0.296 -0.744
    [1391] -0.184 -0.056 -0.224  0.576 -0.304  0.864  0.664  0.664  0.064 -0.696
    [1401]  0.856  0.096  0.904 -1.136 -0.296  0.416  0.176 -0.216  0.856 -0.336
    [1411] -0.544  0.384  0.536  0.464 -0.424 -0.856  0.184 -1.704 -0.744 -1.184
    [1421]  0.504  0.064  1.144  0.024  0.144 -0.536 -0.544  0.256 -1.304  0.744
    [1431] -0.024  0.544 -0.704  0.544  0.864  0.664  0.216 -0.304 -0.944 -0.256
    [1441]  1.504  0.904  0.144 -0.624 -0.696  0.544 -0.664  0.424 -0.536  0.544
    [1451] -1.664 -0.416 -0.904 -0.216  0.256 -0.224 -0.384 -0.064 -0.224 -0.144
    [1461]  0.064  0.424 -0.064 -0.224 -0.096  0.296 -0.104  0.544  0.056  0.664
    [1471] -0.144  1.104 -0.224 -0.744  1.344  0.336  0.064  0.384  0.696  0.864
    [1481] -0.136 -1.296 -0.256 -1.056  0.736  0.664  1.104  0.696 -1.224  0.096
    [1491]  0.304  0.584  0.784  0.624  0.064 -0.744 -0.224  0.616  0.224 -0.944
    [1501]  0.824  0.136  0.544  0.296  0.104 -0.544  1.744  0.136  0.696 -0.856
    [1511]  0.256 -0.256 -1.336  0.104  0.856 -0.904  1.064 -0.296 -0.096 -0.664
    [1521]  1.704 -0.344 -0.024  1.144  1.056  0.744 -0.256  0.704 -1.704  0.696
    [1531]  0.576  0.144  0.104  0.096  0.696  0.304 -0.024 -0.464 -0.296  0.144
    [1541]  0.344 -1.376  0.504 -0.256  0.216  0.824  0.384 -0.664 -0.064  0.576
    [1551] -0.944 -0.504  0.104  1.504  0.024 -0.776 -0.216  1.136  0.224 -0.056
    [1561] -0.376 -1.296  0.056 -0.464  1.104 -0.864 -0.016  0.496 -0.856  0.464
    [1571]  0.664  0.696  0.224  0.736 -0.064 -0.856 -0.696  0.056  0.864  0.616
    [1581]  0.304  0.144  1.384 -0.144  0.544  0.064 -0.304 -0.696  0.696 -0.904
    [1591]  0.224 -0.344  0.264  0.384 -0.056 -0.104 -0.864  0.536  0.864  0.496
    [1601]  0.336  0.904 -0.056 -0.536  0.216 -0.944 -0.144 -0.416  0.616  1.384
    [1611]  1.664 -0.056 -0.176 -0.304 -0.104 -0.064 -0.184 -0.576 -0.016  0.064
    [1621]  0.416 -0.856 -0.544  0.024 -0.224  0.056  0.744  0.336  0.904 -0.176
    [1631]  0.056  0.144 -1.744  0.264  0.944 -0.504  0.744 -0.184 -1.064 -1.304
    [1641]  0.096  0.584  1.104  0.224  1.744  0.336 -0.584 -0.296 -1.136  0.144
    [1651]  0.856 -0.336 -1.336  0.696 -0.376 -1.304 -0.056 -1.664 -0.024  0.704
    [1661]  0.104 -0.216  0.824 -0.136 -1.224 -0.384 -0.256 -0.336  0.256 -0.856
    [1671]  0.104 -1.056  0.464  0.216 -0.704 -0.376  0.224  0.744 -0.736  0.864
    [1681] -1.056  0.176  0.864  1.296  1.744  0.104 -1.344  0.504 -0.064  0.544
    [1691] -0.696  0.696  0.736  0.056 -0.864  0.624 -0.664  0.864 -0.736  0.736
    [1701]  0.096  0.744 -0.864 -1.056  0.264 -0.536 -0.736 -0.256  1.336 -0.096
    [1711]  0.904  0.064 -0.336 -0.904 -0.256  0.344  0.096  0.376  0.736  0.704
    [1721]  0.904 -0.616  1.136 -0.496 -0.744  0.896  0.384 -0.664 -0.344  0.104
    [1731]  0.536  0.096  1.664  0.864 -0.904  0.424 -0.024  0.624  0.224  0.096
    [1741]  0.704 -0.736  0.544 -0.776  0.576  0.136 -0.056  0.736 -0.584  1.336
    [1751] -0.024 -0.864  0.576 -0.904  0.856  0.384 -0.736  0.264  0.744 -0.384
    [1761]  0.424  1.336 -0.096 -0.096 -0.856 -1.104  0.696 -0.584  0.304 -0.096
    [1771]  0.256 -0.176 -0.696 -0.024  0.496 -0.056 -1.136  0.664  0.704  0.536
    [1781] -0.384 -0.424  0.144 -1.664 -1.384  0.576  0.536  1.304  0.096 -0.664
    [1791] -0.144  0.864 -0.424  0.616 -0.744 -0.256 -0.864  1.304  0.264  0.024
    [1801]  1.384 -1.304 -0.144  0.496  1.504  0.464 -1.696 -1.144  0.416  1.504
    [1811] -0.304  1.104 -0.056  0.304  0.936 -0.576  0.864 -0.256 -0.536 -0.104
    [1821]  1.504 -1.224  0.696 -1.104 -0.776 -0.176 -0.336  1.704 -0.304 -0.064
    [1831]  1.376 -0.224  0.824  0.384 -1.704  0.304 -0.576 -1.144  0.104 -0.576
    [1841] -0.416  0.864  0.904 -0.904 -0.344  0.504 -0.296  0.224  0.176  0.536
    [1851] -1.664  0.536 -0.304 -0.584 -0.304 -0.856 -0.304  0.496 -0.136 -0.424
    [1861]  0.224 -0.424  0.416  0.496  0.136  0.664  0.496 -0.496 -0.376 -1.224
    [1871]  0.024  0.704  0.784  1.504 -0.704 -0.584 -0.504  0.176  0.184 -0.736
    [1881]  1.064 -0.024  0.224 -0.104  0.904 -1.064  0.496  1.144 -1.136  0.256
    [1891] -0.144 -0.416  0.176  1.344 -0.304  0.216 -0.504 -1.704 -0.664  0.384
    [1901]  1.704 -0.544 -0.224 -0.256  1.096 -1.504 -0.064 -1.336  1.096 -0.856
    [1911] -1.296 -0.616  0.264  0.464 -0.864  0.256 -1.184  0.184  0.096  0.504
    [1921] -0.104 -1.296  0.224  0.056  1.704 -0.704  0.136  0.136 -1.504 -0.056
    [1931]  1.096 -1.384 -0.064 -0.016 -0.224  0.584 -1.104 -0.536 -0.784 -0.856
    [1941] -0.336  0.936 -0.864 -1.336  0.496 -0.704  0.056 -0.904 -0.336 -0.864
    [1951] -0.376 -0.696  0.104  0.696  0.064 -0.336  0.744  0.904 -0.576 -0.144
    [1961]  0.144 -1.704  0.256 -0.536 -0.384  0.224 -0.064 -0.064 -0.696 -1.504
    [1971]  0.384  0.704  0.544  0.384  1.096 -0.784  0.576 -0.504 -0.696  0.736
    [1981]  0.584 -0.256  0.304 -1.136  0.224 -1.136  1.296 -0.216  0.936 -0.544
    [1991]  1.384  0.304  0.096  0.424 -0.096 -1.184  0.096  0.176 -0.904 -0.464
    [2001]  0.704  0.064 -1.664 -0.544  0.576  0.304  0.904  0.304  0.224 -0.096
    [2011]  0.184 -0.424 -0.864 -0.544 -0.776 -0.064  1.696  0.224 -0.304  0.584
    [2021] -0.264  0.864 -1.064  0.144 -0.824  0.864  0.544 -0.376 -0.696  0.904
    [2031] -1.224 -0.584  0.384  1.704 -0.944  0.904  0.136 -0.304 -0.904 -1.224
    [2041]  0.064  0.104  1.504 -1.664 -0.576 -0.336  0.416 -0.576  1.136 -0.584
    [2051]  0.896 -1.144 -0.824  0.864 -0.264 -0.664 -1.136  0.576  0.936 -0.864
    [2061] -1.664  0.704 -0.336 -0.544 -0.384  0.576  1.224 -0.624  0.904 -0.904
    [2071] -0.096  0.576  1.136 -0.144 -0.584  0.176  0.144  1.096  0.776  0.616
    [2081]  0.336  0.384 -0.904  0.096  0.104  0.896  1.344  1.696  1.136 -0.256
    [2091]  0.264  1.336  1.376 -0.744  0.864  0.024 -0.776 -0.224 -0.856  0.704
    [2101] -0.584 -1.136 -1.144  0.904 -0.184  0.064  0.176  1.096  0.536  1.064
    [2111]  0.384 -0.784 -0.864  0.536  0.536  0.064 -0.424  0.704  0.256  0.304
    [2121]  1.144  0.384 -0.536 -0.176  1.344  0.576  0.256  0.904  0.224  0.176
    [2131] -1.696  0.424  0.424  1.184 -1.664 -0.256 -0.584  0.584  1.104 -1.064
    [2141] -0.216  1.144 -0.056 -0.304  1.696  0.504 -0.544 -0.664  0.416 -0.904
    [2151] -0.936  0.064 -0.424  1.344 -0.376 -0.784 -1.704 -0.864  0.304 -0.664
    [2161]  0.536 -0.496 -0.776  0.616 -1.144  0.416  1.104 -0.584 -0.544 -0.136
    [2171] -0.096  0.016 -1.136 -0.056 -0.344 -1.336  0.424  0.424  0.536  0.064
    [2181]  0.104  0.264 -0.264  0.576  1.384 -0.944 -0.144 -0.904  0.184  0.744
    [2191]  1.184  1.336 -0.216  0.904 -0.216  0.384 -0.744 -0.144  0.224  0.904
    [2201]  0.056  0.136  1.224  0.136 -0.176 -0.096  1.184  1.104  0.056  1.744
    [2211] -0.784  0.944  1.504 -0.376 -0.496 -0.776 -0.336  0.864  0.256  0.264
    [2221] -0.464  0.864 -0.536  0.224 -0.336 -0.496  0.136 -0.896  0.896 -0.856
    [2231] -0.576 -0.224 -0.024 -0.064 -0.096 -0.776  1.056 -0.496 -1.344  0.136
    [2241] -0.896  0.144 -0.544  0.856 -1.696  0.224  1.384  0.136  0.304  0.264
    [2251]  0.576  0.136 -0.904  0.504  0.256 -0.864  0.064  0.296  0.104 -0.736
    [2261]  0.064 -0.744  1.096  1.336  0.264 -0.664 -0.336 -0.376  0.696 -0.664
    [2271]  0.136 -0.256  0.424 -0.024 -0.096  1.096 -0.056 -0.624  1.696  1.696
    [2281] -0.824 -0.416 -0.944 -0.504  0.664  0.584  0.024 -0.144 -0.536  0.376
    [2291] -0.024  0.544 -0.736 -0.736  0.416 -1.336 -0.304 -0.184  0.264  0.864
    [2301] -0.184 -0.336  0.024  0.424  0.424 -0.904 -0.824  0.056  0.864  0.304
    [2311]  0.544 -0.056 -0.664 -0.424  0.384  0.616  0.216  0.056  0.856 -0.536
    [2321]  0.536 -0.256 -1.144  0.104  0.464  0.096  1.304  1.096  1.664  0.224
    [2331]  0.016  0.336  0.024  0.936  0.224 -0.416  0.896 -1.504 -0.664  0.576
    [2341]  0.336 -0.416  0.544  0.544  0.024 -0.536  1.376 -0.024 -0.544 -0.384
    [2351]  0.496 -0.016 -0.144  1.064 -0.016  0.296 -0.224 -0.336 -0.056 -0.216
    [2361] -0.056  0.224 -0.064 -0.224  1.696  0.224 -0.664  0.864 -0.304  0.416
    [2371]  1.376  0.416  0.224 -0.384  0.736 -0.904  0.376 -0.384 -0.616 -1.056
    [2381] -0.896 -0.936  0.496 -0.864 -0.664 -1.704 -0.224  0.944  0.464 -0.744
    [2391] -0.584 -0.904  0.296 -0.376  1.104 -0.664  0.464  0.424  0.216 -1.296
    [2401] -0.224 -0.576 -0.896 -0.544  0.176 -0.424 -0.104  0.216  1.504  0.056
    [2411]  0.264 -0.744 -0.736  0.256  1.224  0.136  0.264 -0.664 -0.256 -0.136
    [2421]  0.216  1.104 -0.536  0.336 -0.104 -0.664  0.336  0.536  0.336 -0.736
    [2431] -0.936 -0.416 -0.536  0.496  0.416  0.864 -0.376  0.904  0.016 -0.704
    [2441]  0.624  0.424 -0.776  1.224  0.416 -0.296 -0.304 -0.264  0.856  0.696
    [2451]  0.576 -1.056 -0.376  1.384 -1.056  1.304  0.224  0.016 -0.864  0.144
    [2461]  1.136  0.584 -0.824  0.056  0.136 -1.744  1.504 -0.336  1.336 -0.384
    [2471] -0.856  0.856 -0.536  0.344 -0.304 -1.104 -0.736  0.704 -0.096 -0.584
    [2481] -0.056 -0.056  0.856  0.224 -0.944 -1.336 -0.416  0.664 -0.024  0.376
    [2491] -0.704 -0.696  1.296 -0.696  0.056  1.336 -0.264  0.296 -0.376  0.776
    [2501] -0.296 -1.696  0.864  0.544 -1.144 -1.504 -1.304 -1.064 -0.216  0.864
    [2511]  1.104  0.024  0.824 -0.936  0.944 -0.504 -0.496 -0.304  0.416 -1.136
    [2521] -1.344  1.104  1.504 -0.024  0.264 -0.176 -0.256 -0.424 -1.056  0.544
    [2531] -0.416 -1.696 -0.016 -0.496 -1.064 -0.664 -1.104 -1.056  0.144  0.064
    [2541] -0.384  0.136  0.856 -0.904 -0.896 -0.744 -0.696  0.544  0.664 -0.584
    [2551]  0.536  0.744 -0.896  0.576  0.624 -0.104 -0.184  1.664 -0.224 -1.336
    [2561] -0.304  1.744  0.216 -0.384  0.504 -0.864  1.344  0.096 -0.024 -0.304
    [2571] -0.264 -0.584 -0.256 -0.264 -0.864  0.736 -0.944 -0.896 -0.304 -0.616
    [2581]  0.776 -0.536  0.864 -0.024  0.024  0.056 -0.576 -1.344 -0.664 -0.824
    [2591] -0.264 -1.344  0.256  0.504  0.096  0.704  0.416 -0.104 -0.184  1.104
    [2601] -1.144  1.064  0.904 -1.136  1.224  0.056 -0.584  1.664 -0.864  0.384
    [2611] -0.096  0.296 -0.256  0.104 -0.744 -0.704  0.096 -0.904  0.224 -1.664
    [2621]  0.504  1.296 -1.504 -0.064  0.536 -1.144 -0.056 -1.704 -1.704  1.064
    [2631]  1.504 -0.496  0.504  1.136  0.104  0.144 -0.944 -0.624  1.096 -1.704
    [2641]  0.024 -0.256 -1.304 -0.304 -0.696 -0.856  0.576  0.776  0.256 -0.104
    [2651]  0.304 -0.176 -0.664 -0.504  0.144  0.584 -1.664 -0.504  0.264 -0.024
    [2661]  0.304 -0.424 -1.304  0.696  0.136 -0.064  0.504  0.216 -0.944  1.384
    [2671] -1.664 -1.144  0.576  0.024 -0.856  0.584 -0.504 -0.096 -0.896  0.824
    [2681] -0.264 -0.064  0.296  0.264  0.296  0.784 -0.696  0.096  0.216  0.864
    [2691] -0.544  0.304  0.104 -0.024 -1.504  0.304  0.104  0.544 -0.776  0.776
    [2701]  0.496  0.336  0.136  0.064  0.584 -0.864 -0.536  0.544 -0.936 -0.744
    [2711]  1.224  0.424 -0.336 -1.696 -0.376 -1.504 -0.336  0.856  1.144  0.336
    [2721]  0.504 -0.256 -0.016  0.024  0.856  0.904 -0.704  0.416  0.424  0.024
    [2731] -0.544  0.056  0.944 -0.664 -0.416  1.136  0.936  0.944  1.704 -0.896
    [2741] -1.224  0.904 -0.824 -0.384 -0.096 -1.504  0.864  0.264  1.696  0.056
    [2751] -1.224 -0.384 -0.104 -0.536  0.296  0.336  0.784 -0.744  1.136  0.096
    [2761] -0.256 -1.224 -1.056 -1.384  0.424 -0.264 -0.176 -0.664  1.104  0.464
    [2771] -0.696 -0.944 -0.304 -1.664 -0.056  0.216  0.384  0.536  1.336 -0.064
    [2781]  0.304 -0.776 -0.256  0.784 -1.096 -0.736  1.504  1.144 -0.176 -0.704
    [2791]  0.864 -0.944  0.584 -0.344 -0.536  0.096  0.216  0.736  0.896  0.136
    [2801]  1.224  0.184 -0.336 -0.064  0.776 -0.176 -1.144 -1.056  0.104 -0.064
    [2811] -0.064 -0.904 -0.144 -0.744  0.904 -0.064 -1.304  0.664  0.264 -0.776
    [2821]  0.136  0.264  0.504  1.344  1.184  0.544 -0.024 -0.264 -0.424 -0.616
    [2831] -0.256 -0.504 -0.304  1.304  0.424 -0.944  0.736 -0.576  1.296  0.216
    [2841] -0.856  0.144 -0.944 -0.864  0.896 -0.504 -1.376  0.184 -0.104  0.696
    [2851]  1.376  0.024 -0.696  1.224 -0.904  0.104  0.544  1.144  0.584  0.056
    [2861]  0.704  0.064  0.224  0.536  0.296  0.896  0.496 -1.376  0.184 -0.384
    [2871] -0.664 -1.136  0.064 -0.224 -0.864 -0.496 -1.224  1.056 -0.216  0.856
    [2881]  0.664 -0.944  1.704  0.696 -0.736  0.576  0.056 -1.376  0.056 -0.584
    [2891]  0.096  1.096  0.536  0.136 -0.336 -1.096 -0.744 -0.344  0.664  1.744
    [2901]  0.304  0.224 -1.144  0.616  0.544  0.904 -0.224  0.064  0.704 -0.864
    [2911]  0.584 -1.144  0.944 -0.184  0.496 -0.296 -0.064 -0.064  0.584 -0.584
    [2921] -0.424  0.704 -0.864  0.344  0.416 -0.424  1.144  0.496  1.136 -0.104
    [2931]  0.096 -0.336  1.696 -0.096 -0.184 -0.904 -0.336  0.696  1.184  0.736
    [2941] -0.296 -1.696 -0.184 -1.224  1.744 -0.336  0.704  0.544  0.384  0.696
    [2951] -1.704 -0.056 -0.336  0.344  0.416 -0.696  0.584  0.936 -0.384  0.896
    [2961] -1.096  0.344  0.184  0.696  0.064 -1.224 -0.496 -0.024 -0.224  0.776
    [2971] -0.096  0.136  1.664 -0.536  0.304  0.784  0.264 -0.696 -0.856 -0.544
    [2981]  0.584  0.024 -1.344  0.736  1.184 -0.256  0.704 -1.136  1.136  0.256
    [2991] -1.344  1.144 -0.744  0.144  0.136 -0.544  0.416  0.304  0.064  1.104
    [3001]  0.224 -0.016  0.704  0.696 -0.536 -0.896 -1.056  1.304  0.176 -0.256
    [3011] -0.096  1.304  0.696  0.776  0.064 -1.104 -0.304 -0.064  1.064 -1.336
    [3021]  0.856  0.896  1.296 -0.296  1.664 -1.064  0.744 -0.904  0.296 -0.096
    [3031] -0.064  0.104  0.296 -0.064  0.584  0.064 -0.744  0.744 -0.496  0.136
    [3041]  0.624  0.944 -0.184 -0.696 -0.536 -1.136 -0.224 -0.424  0.336  0.056
    [3051] -0.176  0.296  0.616 -1.224 -0.336  0.296 -0.096 -0.104  1.384  0.384
    [3061]  0.296 -0.064 -0.496  0.496 -1.704 -0.336 -0.736 -0.584  0.304 -0.224
    [3071] -0.064  0.744 -0.336 -1.184 -0.704 -0.584  0.664  0.176 -0.104 -0.736
    [3081] -1.696 -0.064 -0.144 -0.424  1.376 -0.696 -0.056  0.296  1.064 -0.736
    [3091]  0.664  0.216  0.824  0.696 -1.704  1.336  1.696 -0.896  0.536 -0.416
    [3101] -1.064  0.296  0.696 -0.344  0.704  0.376 -0.184  1.336 -0.024  0.536
    [3111] -0.256 -0.336  1.104  1.704 -1.136  1.744 -0.104 -1.504  0.664  0.296
    [3121]  0.376  1.136  0.136  0.216 -0.264 -0.224  0.536  1.744 -0.544 -0.136
    [3131]  0.504  0.096  0.104  1.104  0.016  0.376  0.336  0.696  1.136 -0.504
    [3141]  0.064 -0.416  0.744  0.064 -0.104 -0.144 -0.784 -1.744 -1.696 -0.864
    [3151] -0.856  0.904 -0.776 -0.056  1.096  0.576 -0.024 -0.136 -0.664 -0.784
    [3161] -1.144  0.024 -0.904 -0.056  0.064 -1.344  0.576  0.736 -0.256  1.336
    [3171] -0.224 -1.296  1.096  0.856  0.496 -0.016  0.064 -0.664  0.736 -0.144
    [3181] -0.296  0.336  0.744  0.216  0.744 -0.336 -0.304  0.704  0.176  0.424
    [3191]  0.824  0.224 -0.856 -1.184  0.536 -1.144  0.296 -0.824  0.664  0.056
    [3201]  0.264 -0.424  0.384 -1.224  0.664 -0.736  0.264 -0.264 -1.144  0.256
    [3211] -0.104  1.056 -0.896  0.064 -0.936 -0.384  0.696 -1.224 -1.344 -0.504
    [3221] -0.776 -0.336 -0.064 -0.104  0.216 -1.336  0.064  0.224  0.504 -0.536
    [3231]  0.896 -0.504 -0.744  1.296  1.344 -0.384  1.104 -0.056 -0.544 -0.344
    [3241] -0.776  0.424  0.376  0.904  0.296 -0.056 -0.256 -0.384  0.024 -0.776
    [3251]  0.424 -0.744  0.064 -1.144  0.616 -0.416  0.624  0.744  0.856  0.904
    [3261]  0.744  0.016  0.296  0.256  0.864  1.104  0.024  1.136  0.224 -0.736
    [3271] -0.824  0.864  1.336 -0.136  0.176  0.344  1.296  0.184 -0.776 -0.136
    [3281]  1.104 -1.336  0.336  1.056 -1.224  0.024 -0.544 -0.744 -0.584  0.136
    [3291] -0.176  1.344 -0.576 -0.104 -0.856 -1.664  0.536  1.224  0.896 -0.504
    [3301]  0.104  0.904 -0.184  0.744  0.016  0.864  0.784  0.536  1.104 -0.536
    [3311]  0.344 -0.104 -0.376 -0.536 -0.864  1.224  0.216 -0.544  1.504 -0.064
    [3321] -1.104 -0.064 -1.664  0.376  0.224 -0.376  0.264 -1.336  0.776 -0.024
    [3331]  0.256  0.744  0.176  1.096  0.696  1.504 -0.944 -1.184  0.344 -0.544
    [3341]  1.224 -1.096  0.784  0.296 -1.664  0.744 -0.136  0.776 -0.624 -0.744
    [3351]  0.576  0.576 -0.896 -1.144  0.824 -0.544  0.216 -0.144 -0.624  0.064
    [3361]  0.736  0.664 -0.384  0.744 -0.896  0.176  0.544  0.744 -0.504 -0.704
    [3371] -0.536  0.616 -1.064 -0.696 -0.744  0.296  0.144 -1.064 -1.336  1.144
    [3381]  0.736  0.256  0.584 -0.576 -0.544  0.104 -0.704  0.704  0.224 -0.544
    [3391]  1.224 -1.336  0.536 -0.744  0.664  1.376 -0.536 -0.944 -1.504  1.744
    [3401]  0.144 -0.856  0.384 -1.136  0.576 -0.064 -0.544  0.904 -0.864  0.144
    [3411]  1.224  0.304  0.384  0.576 -0.416  1.664  1.064  0.096  0.296  0.304
    [3421]  0.696 -0.096  0.016 -0.864 -1.056 -0.384 -1.664 -0.856 -1.064 -0.016
    [3431] -0.784 -0.296  0.776  1.504  0.256 -0.536  0.904  0.064  0.024  0.856
    [3441]  0.424  0.056 -0.904 -0.256  0.096  0.176  1.664 -0.864 -0.064 -0.304
    [3451]  0.176  0.496  0.696 -0.296 -0.096  0.064 -0.256  0.064 -0.024 -0.056
    [3461]  1.104 -0.336  0.776 -0.704  0.016 -0.824  0.904  0.296  0.224 -1.304
    [3471] -0.296 -0.384 -0.216  0.184  0.744  0.736 -0.904  0.304  0.304  0.416
    [3481]  0.904 -0.464 -0.056 -1.184  0.096  0.696  1.184  0.184 -0.304  0.136
    [3491] -0.224 -0.864 -0.304  0.376  0.064  0.736  0.944 -0.864  0.864  0.384
    [3501] -0.296 -0.064  0.064 -1.744 -0.296  0.536  1.136  0.584  0.736  0.696
    [3511] -0.944  1.136 -0.904 -0.416  0.336  0.336  0.536  0.424 -0.184 -0.896
    [3521] -0.336 -0.864 -0.536 -0.256 -0.104  0.384  0.136  0.184  0.104 -0.336
    [3531] -1.344  0.224  0.384 -0.376  0.056 -1.144  1.696 -0.256 -0.696  0.136
    [3541] -1.104  0.064 -0.096  0.896  0.136 -0.176 -0.304 -0.296  0.216 -1.144
    [3551]  0.744 -0.904  1.136  0.224 -0.904  0.384  0.136 -0.256  0.576 -0.304
    [3561]  0.376 -0.336 -0.944  0.384 -0.104 -0.256  1.144  0.104 -0.504 -0.104
    [3571]  0.224 -0.064  0.104  0.136 -0.824 -0.104  0.224 -0.176 -0.144  1.704
    [3581]  0.696  0.264  0.504  0.544  0.104 -0.304  1.104 -0.464  0.256  0.424
    [3591] -0.464  0.536 -0.536  1.056  1.104 -0.216 -1.136 -0.944  0.904  1.104
    [3601]  0.216 -0.736  0.584 -0.336  0.144  0.376  1.744  0.216  0.096 -0.304
    [3611] -0.016 -0.584 -0.504 -0.544 -0.096 -0.336 -0.864 -1.136  0.096  0.016
    [3621]  0.904  0.544  1.224  0.024 -1.064 -0.056  0.784 -0.336  1.336 -0.696
    [3631] -0.776  0.896 -0.296  0.416 -1.184  0.704 -0.904 -0.176  0.424  0.056
    [3641]  0.296 -0.344  0.336  0.376 -0.736 -1.184  0.264  0.776  0.104 -0.144
    [3651]  1.704  1.184 -0.736 -0.136 -0.584  1.056  1.056  0.496  0.056 -0.176
    [3661] -0.536 -0.936  0.544  0.104 -0.904 -1.184  0.896 -1.504  1.664  0.536
    [3671] -0.584 -1.304  0.696 -0.064  0.144  0.776  0.296  0.904  0.944  0.104
    [3681] -0.704  0.536  0.664 -0.904  0.904 -0.536  0.224  0.336 -0.504 -1.664
    [3691]  0.424 -0.104  0.336 -0.944  0.224  0.016  1.296 -0.704 -1.376  0.936
    [3701]  1.224  0.664  0.264  0.424 -0.296  0.624 -0.944  0.704 -0.504 -0.904
    [3711] -0.256 -0.096 -0.904  0.104  0.176  0.384 -0.496  0.856  0.064 -1.376
    [3721]  0.256  0.944  1.664 -0.064 -0.256 -0.856  0.064 -0.616 -0.256 -0.304
    [3731]  0.224  1.104 -0.096 -0.256 -0.384  0.416  1.144  0.024 -0.104 -0.944
    [3741]  0.904 -0.104 -0.304 -0.176  0.664  0.216  0.784  0.904 -0.696  0.264
    [3751] -1.304  0.584 -0.264  0.616  0.696  0.264 -0.704 -0.896 -0.104 -0.224
    [3761] -0.744  0.784  0.536  1.336  0.864  1.304 -1.144  0.776 -0.336  0.224
    [3771]  0.144  0.264 -0.904 -1.144 -0.024 -0.536 -0.744  0.856 -0.224  0.496
    [3781]  0.024 -0.944  0.664 -0.384  0.904  0.896 -0.224  0.304 -0.256  1.376
    [3791]  1.136 -0.264 -1.336 -0.864  1.296 -0.256 -0.424 -0.704  0.024 -1.664
    [3801]  0.344  0.616 -0.896  0.736 -0.344 -0.696  0.056 -0.144  0.296 -0.296
    [3811]  0.144 -0.056 -0.744  1.144 -0.664  1.344 -0.696 -1.144 -0.224 -0.704
    [3821]  1.336 -0.576 -0.336 -0.176  0.176  0.944 -0.064  0.384 -1.184 -0.744
    [3831] -0.384 -1.384 -1.664  0.344  0.584 -1.136 -0.704  0.704  1.664 -0.896
    [3841]  0.624  0.624 -0.144 -0.424  0.536  0.864  0.184 -0.336  1.064  0.224
    [3851] -1.376  0.296  0.736 -0.496  0.536 -0.264 -0.056  0.064 -0.544 -0.944
    [3861]  0.064  0.536  0.616  0.304  0.056 -0.576 -1.504 -0.576 -1.376 -0.104
    [3871] -0.024  0.304  0.776 -1.704 -0.304 -0.024  0.616  1.104 -1.664 -0.544
    [3881] -0.104  0.584 -0.504 -0.496 -0.736  0.864  0.936  0.664  0.776 -0.024
    [3891]  1.136  0.424 -0.416  0.744  0.056 -0.864 -0.936 -1.296  1.056  1.336
    [3901]  0.744 -0.224 -0.096  0.944 -0.056  0.744 -1.144 -0.144  0.224  0.824
    [3911] -1.336  0.704  0.864  0.344  0.624 -0.896 -0.304  1.296  0.504 -0.304
    [3921] -0.256 -0.736  0.616  0.784 -0.016  0.096 -0.864  1.104 -0.144  0.864
    [3931]  0.384 -0.864 -0.096  0.064  0.904 -0.536 -0.264 -0.176 -1.376 -0.744
    [3941]  0.744  1.376  0.144 -0.416  0.104 -0.336  0.536 -0.584  0.296 -0.336
    [3951] -0.896 -0.264  1.184  0.296  0.176 -0.304 -0.064 -0.536  0.744 -0.544
    [3961]  0.896 -0.416 -0.504 -1.696 -0.704  0.824 -0.344  0.496  0.776 -0.376
    [3971]  0.144  0.944  0.496 -1.136 -0.024  0.264  0.896 -0.496 -1.744  0.664
    [3981]  0.256 -0.896  0.496  0.536  1.664  0.416 -0.376 -0.696  1.664 -0.664
    [3991] -0.704 -0.064  0.136  0.664 -1.096 -0.896 -0.216  0.544 -1.056  1.136
    [4001] -0.864  0.224  1.504  0.416  0.064 -1.384 -0.744  0.576  0.576 -0.224
    [4011]  0.856  0.544  0.256  1.744 -0.904  0.704 -0.384 -0.664  0.176 -0.664
    [4021]  0.696  0.944 -0.424  0.896  0.744 -1.144  0.096 -0.296 -0.104 -0.864
    [4031] -0.856 -0.056 -0.104  0.224  0.696  0.704 -1.296 -0.696  0.584  0.224
    [4041] -0.056 -0.256  0.856  0.264  1.336  0.376 -0.304  0.864 -0.256  0.424
    [4051]  0.336  0.944  0.544 -0.344  0.104  0.296 -0.744 -1.664  0.624 -0.176
    [4061] -0.056 -0.616  0.544  0.096  0.744 -0.064 -0.696 -0.464 -0.664 -0.024
    [4071] -0.336  0.504  0.216  0.296 -0.304 -0.384  0.296 -0.104 -0.064  0.664
    [4081] -0.144 -0.224  0.224  1.144 -0.424  0.784 -0.096  0.176  0.024  0.536
    [4091]  0.704 -0.064  0.776  0.096  0.504 -0.576 -0.056  1.104  0.464  0.336
    [4101]  1.384  0.544 -0.256  0.864  0.304 -0.904 -0.016 -1.144 -0.096  1.224
    [4111]  0.096  0.904  0.064  0.376 -0.704 -0.056  0.176  0.624  0.256 -0.616
    [4121] -0.576  0.504 -1.104 -0.136  1.064 -0.296 -0.144 -0.224  1.744 -0.136
    [4131]  0.064 -0.376 -0.944 -0.384 -0.296 -0.376  0.104 -1.696 -0.824 -0.376
    [4141] -0.464  0.616 -0.864  0.744 -0.336 -0.904 -0.864 -0.256 -0.104  1.704
    [4151]  0.384  0.864 -1.144 -1.376  0.776 -0.864  0.264  0.304  0.056  0.504
    [4161] -0.136  0.864  0.416 -0.424  0.104  0.576  0.664 -0.864  0.064 -0.256
    [4171] -0.336 -0.144 -0.264 -1.184  1.336 -0.904  0.304  0.896 -0.696  0.536
    [4181]  0.544  0.056 -0.784  0.336  0.896 -0.296 -0.024 -0.384 -1.296  0.224
    [4191]  1.696  1.144 -1.096 -0.904 -0.376 -0.496  0.224  1.296 -0.264  0.304
    [4201]  1.144  0.576 -0.824  0.224 -0.736  0.376 -0.696 -0.136 -0.584 -0.784
    [4211]  0.304  0.376 -0.544 -1.376 -0.224  0.264 -0.576 -0.184 -0.696 -0.584
    [4221] -0.824  0.584  0.504  0.144 -0.224 -0.136 -0.904  0.064 -0.056 -0.544
    [4231] -0.624  0.176  0.776  0.576  1.664  0.696  0.416  0.184 -0.704 -0.536
    [4241]  0.696  0.536  0.824 -1.304 -0.304 -0.376  0.704  0.864 -0.336  0.584
    [4251] -0.056  0.744 -1.104 -0.896  0.176 -0.136 -0.496  0.296  0.304 -1.704
    [4261]  0.584 -0.176 -0.136 -1.064  0.944 -1.224 -1.064 -0.904 -1.104 -0.896
    [4271] -0.104  1.344  0.264  1.184 -0.224  0.104 -1.096 -0.784 -1.096 -0.304
    [4281] -0.056 -0.064  0.496 -0.064  1.344 -0.096  0.304  0.536  0.296 -1.104
    [4291]  0.696 -1.144  1.296 -1.696 -0.544 -0.256 -0.376  1.184 -1.144 -0.496
    [4301]  0.256 -0.504 -0.824  1.104 -0.104 -0.896 -0.136 -0.936  1.336  0.504
    [4311] -0.856  0.416  1.224  0.096 -1.104  0.224 -1.384 -0.664  0.376 -0.136
    [4321]  1.664 -1.104 -0.144 -0.856 -0.504 -0.904 -1.344  0.224  0.336 -0.376
    [4331]  0.256 -1.184 -0.376 -0.184  1.064 -1.104  0.616 -0.664  0.064 -0.896
    [4341] -0.536  0.064  0.904  0.056  0.304  0.536 -0.304 -0.896 -0.496 -0.296
    [4351]  0.776  0.544  1.696 -0.224  0.744  0.336 -0.296 -0.424  0.256 -0.176
    [4361]  0.616  0.624 -0.736  0.064  0.304 -0.864 -0.304  0.496  0.104  1.744
    [4371]  1.144 -1.064  0.096  1.064  0.664  0.216  0.504 -0.864 -0.176  0.504
    [4381] -0.776 -0.664 -0.696 -0.504 -0.736 -1.144 -0.544  0.664  0.384  0.624
    [4391]  0.224 -0.304 -0.776 -0.736 -0.504 -0.384 -0.424  0.496  0.024  0.136
    [4401]  0.256 -0.856 -0.056 -0.824 -0.176 -0.096  1.136 -0.496  0.016 -0.696
    [4411]  0.296 -1.664  0.384  0.824  0.296 -0.616 -1.296 -0.024  0.544 -0.344
    [4421]  0.864 -1.696 -0.384 -0.896  0.336 -0.376  0.584  1.144 -0.144  0.536
    [4431]  0.096  0.136  0.144 -0.136 -1.136  0.904  0.384 -0.384  0.776 -0.304
    [4441] -1.136 -0.416 -0.624 -0.296  0.536  1.384  0.304  0.224  0.696 -1.704
    [4451]  0.664 -0.496 -0.776  0.944  0.616 -1.384 -0.336  0.696  0.824 -0.384
    [4461] -0.376 -1.184 -0.056  0.136 -0.416  1.336 -0.304 -0.864 -0.496  0.904
    [4471]  0.296 -0.896 -0.504  1.224 -0.056  0.744 -0.936  0.864  0.424 -0.544
    [4481]  1.664 -0.416  0.256  0.144 -0.056 -0.376 -0.576  0.744  0.496 -0.384
    [4491]  0.944  0.864 -0.296 -0.576 -0.936 -0.584 -0.784 -0.624  0.376  0.424
    [4501]  1.104 -0.096 -1.144 -0.376 -0.144  0.096  0.944 -0.384  0.696  0.384
    [4511]  0.264 -0.264  1.336 -0.904  1.104  0.416  0.136 -0.064 -0.904 -0.064
    [4521]  0.264 -1.096 -0.904 -0.464  0.104 -0.536  0.744 -0.264 -0.136  0.696
    [4531]  0.056  0.696 -1.136 -0.016 -0.504 -0.864 -0.104 -0.944  0.416  0.056
    [4541] -1.144  0.416 -0.096  1.104 -0.496 -0.056 -1.056 -0.944 -0.336 -0.296
    [4551] -0.744 -0.064 -0.424  0.624  0.136 -0.104  1.376 -0.536  0.304  0.384
    [4561] -0.584 -0.424  0.704  0.736  0.496  0.776  0.776  0.304  0.496  0.256
    [4571]  1.696 -0.944 -0.016  1.056  0.336 -0.256 -0.584  0.664 -0.904 -0.176
    [4581]  0.296 -0.136 -0.664 -0.424  0.264 -0.696 -0.304 -1.664 -0.224  1.136
    [4591]  0.104  0.344 -1.104 -0.304 -0.136 -0.856 -0.576  1.336  0.216 -0.176
    [4601]  0.176  1.136  0.056  0.064 -1.384  0.664 -0.336  0.096 -0.344  1.376
    [4611]  0.904  0.304 -0.256 -0.256  0.304  0.664  0.264 -0.296  1.144  0.184
    [4621]  0.856  1.296  0.184  1.184 -0.536 -0.304 -0.264  0.416 -1.056  0.016
    [4631]  1.296 -0.696  1.344  0.064 -0.664  1.064  1.144 -1.096 -0.384  0.344
    [4641] -1.104  0.304  0.736  0.304 -0.784  0.296 -1.696  0.184 -1.664 -0.584
    [4651]  0.464  0.904 -0.936  0.496 -0.064 -0.256  0.776  0.224  0.544  0.104
    [4661]  0.496 -0.056 -0.104 -0.624  1.184  0.864  0.336 -0.944  0.136  0.216
    [4671] -0.696 -0.776  0.144 -0.024 -0.744 -0.304 -1.664 -0.064 -0.544  1.304
    [4681]  0.224  0.864  0.304  0.664  0.904  0.696 -0.176 -0.744  0.264  0.544
    [4691] -0.904  0.304 -0.616 -0.896  0.336 -0.584  0.304  0.424  0.304 -0.384
    [4701]  1.304  1.184 -0.064 -0.336 -0.064 -1.096 -1.296 -0.944  0.624 -0.664
    [4711] -0.216  0.904 -0.536 -0.744  0.424  1.304 -0.256  0.144  0.664 -0.576
    [4721] -0.584  0.944 -0.896 -0.336  1.504  0.264  0.056 -0.376  0.336  0.704
    [4731]  0.344 -0.504 -0.384  0.704  0.264 -0.224  0.296  0.744 -0.544  0.424
    [4741]  0.896  0.256 -0.176  1.384 -0.544 -0.696  0.944 -0.264  0.064 -1.744
    [4751]  0.696 -0.856 -0.696  0.904 -0.264  1.376 -1.224  0.904 -0.256  0.704
    [4761]  0.536 -0.336 -0.144 -0.304  0.256  0.064 -0.304  0.096 -0.096  0.264
    [4771]  0.864 -0.504 -0.224 -0.664  0.064 -1.664 -0.144  0.504 -1.704 -1.096
    [4781]  0.744 -0.064 -1.064 -0.296 -0.136  0.136  0.336  0.336 -0.624 -0.224
    [4791]  0.344  0.256 -0.296 -0.784 -0.664  0.256 -0.624  0.776 -0.416 -0.856
    [4801] -0.744  0.504 -0.896  0.536  1.184  0.096  1.104 -1.064 -0.096 -1.384
    [4811]  0.776  1.504 -0.224  0.216 -0.944  0.296 -0.864 -0.016  0.224  0.056
    [4821] -0.496  0.296 -0.384 -0.216  1.384 -0.176 -1.064 -0.864  0.904 -0.104
    [4831]  0.864  0.224  0.856  0.744 -0.864 -1.104  0.264  0.264 -0.584  0.176
    [4841]  0.176 -0.616  0.336 -0.256 -0.256 -0.296  0.064  0.136  0.664 -0.344
    [4851] -1.336  0.096  0.584 -0.496  1.104 -0.224 -1.136  0.384 -0.056 -0.096
    [4861] -0.104 -1.504  0.336  0.664  0.376  0.864  0.144 -0.304 -0.296  0.584
    [4871]  0.256  1.344 -0.536  1.144 -1.144  0.224 -0.144 -0.216 -0.256 -1.304
    [4881]  0.384 -0.336  0.416  0.064 -0.256 -0.064 -0.296  0.256 -0.584 -0.336
    [4891]  0.504 -0.664  0.576 -0.864  0.056  0.664  0.096 -0.104 -0.376  0.264
    [4901]  0.304 -0.864 -1.336 -1.096  0.784  0.136  0.696  0.304  0.136  0.064
    [4911]  0.904 -0.704  1.376 -0.056  1.704 -0.056 -0.144  1.696  0.216  0.264
    [4921]  0.096  0.104  0.544 -0.736 -0.536  0.336  0.376 -0.144 -0.904  0.376
    [4931]  1.304 -0.664 -0.064 -0.024  0.296 -0.224  0.376  0.864  1.136 -0.576
    [4941] -1.504  0.264 -1.504 -0.416  0.904  0.544 -0.256 -0.944 -0.224  1.696
    [4951]  0.304  0.216  0.584  0.096 -0.776 -1.104 -1.144  0.416 -0.664 -0.744
    [4961] -0.624 -0.304  0.256 -0.424  0.864 -0.144 -0.504 -0.336 -0.144 -0.576
    [4971]  0.504  0.776  0.424 -0.464 -0.544  0.856 -0.496 -1.504  0.104 -0.296
    [4981] -0.224 -0.344  0.736  0.104  1.136  1.104  0.584 -0.224  0.136  0.496
    [4991] -0.224 -0.776  0.496 -0.784  0.216  0.384  0.136 -0.424  0.944 -0.104

## Estimate Dist under H0 {data-id="quarto-animate-title"}

## Find Reject Region

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
left_threshold <- quantile(H_0, .025)
right_threshold <- quantile(H_0, .975)
```

## Estimate Dist under H0 {data-id="quarto-animate-title"}

---

[← Power](01-power.md) · [Up: contents](index.md) · [An Alternative Hypothesis →](03-an-alternative-hypothesis.md)
