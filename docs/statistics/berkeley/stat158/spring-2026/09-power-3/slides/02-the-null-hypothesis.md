---
title: The Null Hypothesis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/09-power-3/slides.html
source_file: sources/berkeley-stat158/spring-2026/09-power-3/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# The Null Hypothesis

**Source:** [`09-power-3/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/09-power-3/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Recall the data

<style>#fbeymqavkm table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#fbeymqavkm thead, #fbeymqavkm tbody, #fbeymqavkm tfoot, #fbeymqavkm tr, #fbeymqavkm td, #fbeymqavkm th {
  border-style: none;
}

#fbeymqavkm p {
  margin: 0;
  padding: 0;
}

#fbeymqavkm .gt_table {
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

#fbeymqavkm .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#fbeymqavkm .gt_title {
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

#fbeymqavkm .gt_subtitle {
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

#fbeymqavkm .gt_heading {
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

#fbeymqavkm .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fbeymqavkm .gt_col_headings {
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

#fbeymqavkm .gt_col_heading {
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

#fbeymqavkm .gt_column_spanner_outer {
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

#fbeymqavkm .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#fbeymqavkm .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#fbeymqavkm .gt_column_spanner {
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

#fbeymqavkm .gt_spanner_row {
  border-bottom-style: hidden;
}

#fbeymqavkm .gt_group_heading {
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

#fbeymqavkm .gt_empty_group_heading {
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

#fbeymqavkm .gt_from_md > :first-child {
  margin-top: 0;
}

#fbeymqavkm .gt_from_md > :last-child {
  margin-bottom: 0;
}

#fbeymqavkm .gt_row {
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

#fbeymqavkm .gt_stub {
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

#fbeymqavkm .gt_stub_row_group {
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

#fbeymqavkm .gt_row_group_first td {
  border-top-width: 2px;
}

#fbeymqavkm .gt_row_group_first th {
  border-top-width: 2px;
}

#fbeymqavkm .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#fbeymqavkm .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#fbeymqavkm .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#fbeymqavkm .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fbeymqavkm .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#fbeymqavkm .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#fbeymqavkm .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#fbeymqavkm .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#fbeymqavkm .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fbeymqavkm .gt_footnotes {
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

#fbeymqavkm .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#fbeymqavkm .gt_sourcenotes {
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

#fbeymqavkm .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#fbeymqavkm .gt_left {
  text-align: left;
}

#fbeymqavkm .gt_center {
  text-align: center;
}

#fbeymqavkm .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#fbeymqavkm .gt_font_normal {
  font-weight: normal;
}

#fbeymqavkm .gt_font_bold {
  font-weight: bold;
}

#fbeymqavkm .gt_font_italic {
  font-style: italic;
}

#fbeymqavkm .gt_super {
  font-size: 65%;
}

#fbeymqavkm .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#fbeymqavkm .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#fbeymqavkm .gt_indent_1 {
  text-indent: 5px;
}

#fbeymqavkm .gt_indent_2 {
  text-indent: 10px;
}

#fbeymqavkm .gt_indent_3 {
  text-indent: 15px;
}

#fbeymqavkm .gt_indent_4 {
  text-indent: 20px;
}

#fbeymqavkm .gt_indent_5 {
  text-indent: 25px;
}

#fbeymqavkm .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#fbeymqavkm div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

<style>#rswqbqrluy table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#rswqbqrluy thead, #rswqbqrluy tbody, #rswqbqrluy tfoot, #rswqbqrluy tr, #rswqbqrluy td, #rswqbqrluy th {
  border-style: none;
}

#rswqbqrluy p {
  margin: 0;
  padding: 0;
}

#rswqbqrluy .gt_table {
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

#rswqbqrluy .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#rswqbqrluy .gt_title {
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

#rswqbqrluy .gt_subtitle {
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

#rswqbqrluy .gt_heading {
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

#rswqbqrluy .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rswqbqrluy .gt_col_headings {
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

#rswqbqrluy .gt_col_heading {
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

#rswqbqrluy .gt_column_spanner_outer {
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

#rswqbqrluy .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#rswqbqrluy .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#rswqbqrluy .gt_column_spanner {
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

#rswqbqrluy .gt_spanner_row {
  border-bottom-style: hidden;
}

#rswqbqrluy .gt_group_heading {
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

#rswqbqrluy .gt_empty_group_heading {
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

#rswqbqrluy .gt_from_md > :first-child {
  margin-top: 0;
}

#rswqbqrluy .gt_from_md > :last-child {
  margin-bottom: 0;
}

#rswqbqrluy .gt_row {
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

#rswqbqrluy .gt_stub {
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

#rswqbqrluy .gt_stub_row_group {
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

#rswqbqrluy .gt_row_group_first td {
  border-top-width: 2px;
}

#rswqbqrluy .gt_row_group_first th {
  border-top-width: 2px;
}

#rswqbqrluy .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#rswqbqrluy .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#rswqbqrluy .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#rswqbqrluy .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rswqbqrluy .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#rswqbqrluy .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#rswqbqrluy .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#rswqbqrluy .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#rswqbqrluy .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rswqbqrluy .gt_footnotes {
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

#rswqbqrluy .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#rswqbqrluy .gt_sourcenotes {
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

#rswqbqrluy .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#rswqbqrluy .gt_left {
  text-align: left;
}

#rswqbqrluy .gt_center {
  text-align: center;
}

#rswqbqrluy .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#rswqbqrluy .gt_font_normal {
  font-weight: normal;
}

#rswqbqrluy .gt_font_bold {
  font-weight: bold;
}

#rswqbqrluy .gt_font_italic {
  font-style: italic;
}

#rswqbqrluy .gt_super {
  font-size: 65%;
}

#rswqbqrluy .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#rswqbqrluy .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#rswqbqrluy .gt_indent_1 {
  text-indent: 5px;
}

#rswqbqrluy .gt_indent_2 {
  text-indent: 10px;
}

#rswqbqrluy .gt_indent_3 {
  text-indent: 15px;
}

#rswqbqrluy .gt_indent_4 {
  text-indent: 20px;
}

#rswqbqrluy .gt_indent_5 {
  text-indent: 25px;
}

#rswqbqrluy .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#rswqbqrluy div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

<style>#crtfmmjokc table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#crtfmmjokc thead, #crtfmmjokc tbody, #crtfmmjokc tfoot, #crtfmmjokc tr, #crtfmmjokc td, #crtfmmjokc th {
  border-style: none;
}

#crtfmmjokc p {
  margin: 0;
  padding: 0;
}

#crtfmmjokc .gt_table {
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

#crtfmmjokc .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#crtfmmjokc .gt_title {
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

#crtfmmjokc .gt_subtitle {
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

#crtfmmjokc .gt_heading {
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

#crtfmmjokc .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#crtfmmjokc .gt_col_headings {
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

#crtfmmjokc .gt_col_heading {
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

#crtfmmjokc .gt_column_spanner_outer {
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

#crtfmmjokc .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#crtfmmjokc .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#crtfmmjokc .gt_column_spanner {
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

#crtfmmjokc .gt_spanner_row {
  border-bottom-style: hidden;
}

#crtfmmjokc .gt_group_heading {
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

#crtfmmjokc .gt_empty_group_heading {
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

#crtfmmjokc .gt_from_md > :first-child {
  margin-top: 0;
}

#crtfmmjokc .gt_from_md > :last-child {
  margin-bottom: 0;
}

#crtfmmjokc .gt_row {
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

#crtfmmjokc .gt_stub {
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

#crtfmmjokc .gt_stub_row_group {
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

#crtfmmjokc .gt_row_group_first td {
  border-top-width: 2px;
}

#crtfmmjokc .gt_row_group_first th {
  border-top-width: 2px;
}

#crtfmmjokc .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#crtfmmjokc .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#crtfmmjokc .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#crtfmmjokc .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#crtfmmjokc .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#crtfmmjokc .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#crtfmmjokc .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#crtfmmjokc .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#crtfmmjokc .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#crtfmmjokc .gt_footnotes {
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

#crtfmmjokc .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#crtfmmjokc .gt_sourcenotes {
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

#crtfmmjokc .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#crtfmmjokc .gt_left {
  text-align: left;
}

#crtfmmjokc .gt_center {
  text-align: center;
}

#crtfmmjokc .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#crtfmmjokc .gt_font_normal {
  font-weight: normal;
}

#crtfmmjokc .gt_font_bold {
  font-weight: bold;
}

#crtfmmjokc .gt_font_italic {
  font-style: italic;
}

#crtfmmjokc .gt_super {
  font-size: 65%;
}

#crtfmmjokc .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#crtfmmjokc .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#crtfmmjokc .gt_indent_1 {
  text-indent: 5px;
}

#crtfmmjokc .gt_indent_2 {
  text-indent: 10px;
}

#crtfmmjokc .gt_indent_3 {
  text-indent: 15px;
}

#crtfmmjokc .gt_indent_4 {
  text-indent: 20px;
}

#crtfmmjokc .gt_indent_5 {
  text-indent: 25px;
}

#crtfmmjokc .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#crtfmmjokc div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

<style>#fanxqlsxrx table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#fanxqlsxrx thead, #fanxqlsxrx tbody, #fanxqlsxrx tfoot, #fanxqlsxrx tr, #fanxqlsxrx td, #fanxqlsxrx th {
  border-style: none;
}

#fanxqlsxrx p {
  margin: 0;
  padding: 0;
}

#fanxqlsxrx .gt_table {
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

#fanxqlsxrx .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#fanxqlsxrx .gt_title {
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

#fanxqlsxrx .gt_subtitle {
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

#fanxqlsxrx .gt_heading {
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

#fanxqlsxrx .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fanxqlsxrx .gt_col_headings {
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

#fanxqlsxrx .gt_col_heading {
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

#fanxqlsxrx .gt_column_spanner_outer {
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

#fanxqlsxrx .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#fanxqlsxrx .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#fanxqlsxrx .gt_column_spanner {
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

#fanxqlsxrx .gt_spanner_row {
  border-bottom-style: hidden;
}

#fanxqlsxrx .gt_group_heading {
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

#fanxqlsxrx .gt_empty_group_heading {
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

#fanxqlsxrx .gt_from_md > :first-child {
  margin-top: 0;
}

#fanxqlsxrx .gt_from_md > :last-child {
  margin-bottom: 0;
}

#fanxqlsxrx .gt_row {
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

#fanxqlsxrx .gt_stub {
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

#fanxqlsxrx .gt_stub_row_group {
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

#fanxqlsxrx .gt_row_group_first td {
  border-top-width: 2px;
}

#fanxqlsxrx .gt_row_group_first th {
  border-top-width: 2px;
}

#fanxqlsxrx .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#fanxqlsxrx .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#fanxqlsxrx .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#fanxqlsxrx .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fanxqlsxrx .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#fanxqlsxrx .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#fanxqlsxrx .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#fanxqlsxrx .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#fanxqlsxrx .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fanxqlsxrx .gt_footnotes {
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

#fanxqlsxrx .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#fanxqlsxrx .gt_sourcenotes {
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

#fanxqlsxrx .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#fanxqlsxrx .gt_left {
  text-align: left;
}

#fanxqlsxrx .gt_center {
  text-align: center;
}

#fanxqlsxrx .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#fanxqlsxrx .gt_font_normal {
  font-weight: normal;
}

#fanxqlsxrx .gt_font_bold {
  font-weight: bold;
}

#fanxqlsxrx .gt_font_italic {
  font-style: italic;
}

#fanxqlsxrx .gt_super {
  font-size: 65%;
}

#fanxqlsxrx .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#fanxqlsxrx .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#fanxqlsxrx .gt_indent_1 {
  text-indent: 5px;
}

#fanxqlsxrx .gt_indent_2 {
  text-indent: 10px;
}

#fanxqlsxrx .gt_indent_3 {
  text-indent: 15px;
}

#fanxqlsxrx .gt_indent_4 {
  text-indent: 20px;
}

#fanxqlsxrx .gt_indent_5 {
  text-indent: 25px;
}

#fanxqlsxrx .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#fanxqlsxrx div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

<style>#ttmawillqq table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ttmawillqq thead, #ttmawillqq tbody, #ttmawillqq tfoot, #ttmawillqq tr, #ttmawillqq td, #ttmawillqq th {
  border-style: none;
}

#ttmawillqq p {
  margin: 0;
  padding: 0;
}

#ttmawillqq .gt_table {
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

#ttmawillqq .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ttmawillqq .gt_title {
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

#ttmawillqq .gt_subtitle {
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

#ttmawillqq .gt_heading {
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

#ttmawillqq .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ttmawillqq .gt_col_headings {
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

#ttmawillqq .gt_col_heading {
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

#ttmawillqq .gt_column_spanner_outer {
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

#ttmawillqq .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ttmawillqq .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ttmawillqq .gt_column_spanner {
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

#ttmawillqq .gt_spanner_row {
  border-bottom-style: hidden;
}

#ttmawillqq .gt_group_heading {
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

#ttmawillqq .gt_empty_group_heading {
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

#ttmawillqq .gt_from_md > :first-child {
  margin-top: 0;
}

#ttmawillqq .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ttmawillqq .gt_row {
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

#ttmawillqq .gt_stub {
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

#ttmawillqq .gt_stub_row_group {
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

#ttmawillqq .gt_row_group_first td {
  border-top-width: 2px;
}

#ttmawillqq .gt_row_group_first th {
  border-top-width: 2px;
}

#ttmawillqq .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ttmawillqq .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ttmawillqq .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ttmawillqq .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ttmawillqq .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ttmawillqq .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ttmawillqq .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ttmawillqq .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ttmawillqq .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ttmawillqq .gt_footnotes {
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

#ttmawillqq .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ttmawillqq .gt_sourcenotes {
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

#ttmawillqq .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ttmawillqq .gt_left {
  text-align: left;
}

#ttmawillqq .gt_center {
  text-align: center;
}

#ttmawillqq .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ttmawillqq .gt_font_normal {
  font-weight: normal;
}

#ttmawillqq .gt_font_bold {
  font-weight: bold;
}

#ttmawillqq .gt_font_italic {
  font-style: italic;
}

#ttmawillqq .gt_super {
  font-size: 65%;
}

#ttmawillqq .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ttmawillqq .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ttmawillqq .gt_indent_1 {
  text-indent: 5px;
}

#ttmawillqq .gt_indent_2 {
  text-indent: 10px;
}

#ttmawillqq .gt_indent_3 {
  text-indent: 15px;
}

#ttmawillqq .gt_indent_4 {
  text-indent: 20px;
}

#ttmawillqq .gt_indent_5 {
  text-indent: 25px;
}

#ttmawillqq .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ttmawillqq div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

       [1]  1.104 -0.424 -0.936  1.696  0.136  0.584  0.904  0.136 -1.056  0.264
      [11] -1.136  0.616  0.824  0.776 -0.624 -0.424 -0.216  0.416 -0.536 -0.304
      [21] -0.856 -0.144 -0.504 -1.064  0.376  0.224  0.744 -0.744 -0.176 -0.416
      [31] -0.624 -0.744 -0.304  0.384  1.704 -0.696 -0.744  0.056  0.424  0.896
      [41]  1.664 -0.576  1.136 -1.704 -0.096  0.624 -0.864 -0.144 -0.264 -0.224
      [51] -0.296  0.184 -0.496  0.296 -0.104 -0.224  1.504 -1.136 -1.504 -0.776
      [61]  0.704  0.104 -0.904 -1.136 -1.136 -0.336  0.496  1.744  0.624 -0.544
      [71]  0.144  0.576  1.296 -0.624 -0.104  0.224  1.224 -1.344  0.056  0.416
      [81] -0.176 -0.256  1.104 -0.024 -1.696 -0.664  0.856  0.064  0.544 -0.864
      [91] -1.304 -1.664  0.536 -0.096  0.104 -1.104  0.144 -0.704  0.704 -0.864
     [101] -0.224 -0.024  0.064 -0.064 -0.064  0.904 -1.304  0.216  1.104 -0.744
     [111]  0.536 -0.704  0.776 -1.064  0.256  0.704  0.104  0.416 -0.904  1.664
     [121]  0.296 -0.856  0.064 -0.904 -0.896  1.296  0.744  0.304 -0.176 -1.744
     [131]  0.304  0.664  0.904  0.304  0.216  0.704  0.744  0.536 -0.136  0.944
     [141] -0.504  1.384 -0.824 -0.856  1.144 -0.224  0.616  0.096 -0.944  0.384
     [151] -0.856  0.696  0.144  0.856  1.304  1.064  0.256 -1.144  0.176 -0.064
     [161]  1.336 -0.464 -0.144 -0.416 -1.184  0.504 -0.936 -0.544 -0.664  1.144
     [171] -0.344  0.296  0.424 -0.696  1.344  0.544 -1.344 -1.064  0.696 -0.856
     [181]  0.304  0.744 -0.744 -0.584  0.616 -0.224  0.224 -0.856 -0.664  0.504
     [191] -0.664  0.576 -0.104 -0.184  0.936  0.304  0.496 -0.736 -0.416 -0.736
     [201] -0.216  0.096 -1.336  0.224 -0.024 -0.544 -0.024  0.176  0.144  0.224
     [211]  0.584 -0.056 -0.096  0.584 -0.056  0.896 -0.224  0.624  1.704  0.024
     [221]  0.056  0.776 -0.664 -0.144  1.144 -0.696 -1.144  0.496  0.464  1.096
     [231] -1.056  0.224  0.576  0.584  0.256  0.664 -0.056  0.896 -0.376 -0.024
     [241]  0.496 -0.224  0.864  0.544 -0.616 -0.664 -0.944  0.864  0.304 -0.576
     [251]  0.704  0.216  0.856  0.776 -0.664 -0.216  0.616  1.704  0.464  1.056
     [261]  0.536  0.176 -0.904 -0.704 -0.304  0.056  0.384  1.344  0.584  0.176
     [271] -0.224  0.104  0.304  1.144 -0.304  0.024 -0.136 -0.336  0.896 -0.376
     [281]  0.664  0.584 -0.064  1.504 -0.304 -0.584  0.624 -0.144  0.136 -0.736
     [291]  0.256  0.504  1.136  0.224  0.664 -0.584 -0.176 -0.864 -0.136 -0.904
     [301] -1.704 -0.224  0.904  0.744 -0.064  0.896 -1.304 -0.864 -0.544 -1.344
     [311]  0.696 -0.864 -1.504  0.256  0.056  0.776  0.464 -0.296 -0.496 -0.904
     [321]  0.216 -0.664  1.096 -0.304 -1.744  0.776  0.736 -0.904 -0.744  0.904
     [331] -1.056 -1.384  0.056 -0.536  0.416 -1.504  0.904 -0.904  0.304  0.344
     [341] -0.496  0.736 -1.144 -0.056 -0.384 -0.576 -0.224  0.536 -0.544  0.336
     [351] -0.296  1.304  0.896 -0.696  0.024 -0.304 -1.296 -1.344  0.256 -0.056
     [361] -0.424  0.576  0.024 -0.024  1.344  0.016 -0.416 -0.576 -0.304  0.224
     [371] -1.376  0.584 -0.704 -0.056 -0.896 -0.904  0.376  0.584  0.304 -0.664
     [381] -1.136  0.224 -0.416  0.176  1.664 -1.224  0.144  0.464  0.304 -1.104
     [391]  0.784  0.856 -0.024  0.744 -0.296  0.064  1.136  0.496  0.416 -0.144
     [401]  1.336 -0.056 -0.256 -0.584 -1.744  1.104  1.104  0.776  0.056 -0.584
     [411]  0.144  0.496  0.776  0.544 -0.856 -0.256 -0.864 -0.224  0.024  0.296
     [421]  0.776 -0.584  0.504  1.104 -0.464  0.664  0.664  0.224 -0.264 -0.176
     [431] -1.504  0.024  0.704  0.136  0.216  1.376  1.376 -0.304  0.424 -0.304
     [441] -0.784  0.336  0.696  1.064  0.336 -0.304 -0.056  0.464 -0.064 -0.336
     [451]  0.304  0.856  0.576  0.496  0.544  0.904  0.496 -0.096 -0.576 -0.776
     [461] -0.384  0.384 -1.664 -0.064  0.664  0.176 -0.896 -0.784  1.136 -0.104
     [471]  0.904 -0.376 -0.496  0.336  0.064  0.744  0.736  1.144  0.104  1.056
     [481]  1.384  0.896  1.336 -0.024 -0.896 -0.464 -0.016  0.144 -0.304  0.224
     [491] -0.704  0.664 -1.144 -0.744 -0.104 -1.296  0.256 -0.296  0.144 -0.496
     [501]  0.304  0.424  1.064  0.376  0.904  0.736  0.496 -0.056  0.064 -0.376
     [511]  0.096 -0.176 -0.824  0.664 -0.304 -0.336  0.544 -0.384  1.144  0.544
     [521]  0.744  1.104  1.224 -0.536 -1.136  0.064  1.096  0.096 -0.424  0.056
     [531]  0.136 -0.144  0.504  0.336 -1.296  1.384  0.664 -1.224 -0.664  0.336
     [541]  0.216  0.424 -0.056  0.096  0.744  0.384  0.936 -0.224 -0.296 -0.616
     [551]  0.224 -1.384  0.064  0.176 -0.856  0.384  0.504 -0.336  0.904 -0.904
     [561] -0.144  0.504  0.064  1.064  0.744  0.536  0.224  0.224  0.224  0.904
     [571]  0.296  0.936  0.056 -0.264 -1.504  0.136  0.584  0.304  0.384 -1.096
     [581] -0.704  0.664  0.344 -0.736  0.176 -0.224  0.544 -0.576  0.336  0.544
     [591] -0.584  1.136 -0.136  0.064  0.904 -1.744 -0.776 -1.104 -0.584 -0.064
     [601]  1.104  0.696 -0.424 -1.184  0.896  0.704 -0.776 -0.704 -0.056  0.864
     [611] -1.064 -1.144 -0.096 -0.464 -0.904  0.224  0.776  0.496 -0.136  0.464
     [621]  0.256  0.736 -0.896 -0.576  1.304 -0.136 -0.616 -1.344 -0.736 -0.296
     [631]  0.224  0.664  0.176  0.936  0.616 -0.424  0.256 -0.696  1.336 -0.536
     [641]  0.744 -0.616 -0.864 -0.744 -0.384  1.304 -0.944  0.296 -1.184 -0.064
     [651] -0.584  0.336  0.096  0.496 -0.904 -0.296  0.376  0.736  1.296  0.304
     [661]  0.696  0.696 -1.384 -0.736  1.064 -0.256  0.256  0.104  0.296  1.744
     [671] -0.664 -0.504 -0.224  0.696 -0.056 -0.336  0.864  0.856 -0.056  0.304
     [681]  0.664  0.536 -0.584  0.424 -0.256  0.304 -0.896 -0.744  0.176 -0.504
     [691]  0.056  0.064 -0.104 -0.544  0.704 -0.064 -0.544 -0.944  0.536 -0.064
     [701]  0.104  0.224 -0.904 -0.136  0.136  1.104  0.744  0.424  0.664 -0.896
     [711]  0.704  0.296 -0.304 -0.376  0.584 -0.664 -1.096 -1.104 -0.376  0.056
     [721]  1.136  1.184  0.064  0.776  0.744 -0.736  0.424 -0.104 -0.096 -0.416
     [731]  0.104 -0.544 -0.744  0.896  0.064 -0.544  0.536  0.744 -0.936 -0.104
     [741]  0.264 -0.296  0.864 -0.184  0.376  0.824  1.376 -1.136 -1.304 -1.056
     [751]  0.904  1.136 -0.904  0.304  0.864  1.064  0.464 -1.376  0.944  0.144
     [761] -0.464  0.064 -0.096  0.704  0.096 -0.536 -0.904 -0.744  0.544 -0.904
     [771]  0.536  0.016 -1.144 -0.896 -1.144  0.744 -0.104 -0.224 -0.624  0.864
     [781]  1.144  0.856  0.296  0.776 -1.344  0.136  1.696  0.936  0.424  0.824
     [791] -0.544 -0.584  0.776 -0.104  1.376  1.104  0.064  0.944  0.144 -0.304
     [801] -0.384  0.736 -0.904  0.544 -1.144 -0.104 -0.376 -0.904 -0.776 -0.384
     [811]  0.744  0.256  1.744 -0.096 -0.536  0.064 -1.296  0.144  0.504 -0.104
     [821]  0.224 -0.744 -0.776 -0.896 -0.544 -0.576 -0.176 -0.176  1.104  0.904
     [831] -0.624 -0.776  0.896  0.904  0.144 -0.824 -0.784 -0.544  1.696 -0.144
     [841]  0.664 -0.376  0.184 -1.136 -0.144  0.536  0.256 -0.896  0.144  0.384
     [851]  0.064 -1.224 -0.176  0.504  0.296 -0.216 -0.184  0.664  0.744 -0.416
     [861] -0.744  0.056 -0.336  1.096 -0.096  0.304  0.576  0.056  0.384  0.664
     [871]  0.304 -0.496  0.536  0.704 -1.136 -0.856 -0.904  0.104  0.336  0.376
     [881] -0.576  0.336  0.744  0.584  0.384  0.056  1.136 -0.304 -1.384 -0.184
     [891] -0.584 -0.216  1.184 -0.056 -0.856 -0.336 -0.064  1.104  0.224 -0.776
     [901] -0.224 -0.376 -0.864 -0.096 -0.144 -0.616 -0.944  0.144 -0.224  1.136
     [911]  0.536 -0.544  0.104 -0.744  0.216  0.744 -0.696 -0.136  0.864 -0.544
     [921] -0.856 -0.384  0.616 -0.176 -0.376  0.736  0.056 -0.616 -0.504  0.624
     [931] -0.464 -0.096 -0.864  1.704  0.736 -0.896  0.296  0.304 -0.736  1.704
     [941] -0.904  0.736  0.616 -0.296  0.056 -0.536 -1.096  0.864 -0.264 -0.384
     [951] -0.904  1.184  0.184 -0.856 -0.696 -0.336  0.584  0.064 -0.904  0.696
     [961] -1.344 -0.136 -0.264 -1.744 -0.904  0.064 -0.904 -1.144 -0.864  1.064
     [971]  0.056 -0.696  1.384 -0.536  0.296 -0.664  0.256  0.904  0.176  0.904
     [981]  0.936  0.144 -0.144  0.944 -0.664 -1.344  1.696 -1.144  0.184  0.496
     [991]  0.864  1.344 -0.696 -0.696 -0.784  1.664 -1.104  0.704 -0.056  0.216
    [1001] -1.696 -0.544  0.424 -0.144  0.336  0.504 -0.144  0.744 -0.144 -0.904
    [1011]  0.304  0.064 -0.544  1.376 -0.536 -0.744 -0.904  0.576 -0.296 -0.384
    [1021]  0.296  0.336 -0.424  0.136  0.536 -0.136 -0.464 -1.184  0.424 -0.016
    [1031]  0.176 -0.384 -0.504 -0.464  0.384  0.584  0.424 -0.504  0.216 -0.056
    [1041]  0.344  0.104  0.776 -0.896 -0.536  0.776 -1.096 -0.256 -0.384  0.384
    [1051]  0.616 -1.064  0.216 -0.064 -0.216 -0.424 -0.256  0.744 -1.104  1.296
    [1061] -0.376  1.376 -0.696 -0.064  1.744 -1.344 -0.296  0.896 -1.136  0.864
    [1071]  1.096  0.176  0.896  0.696  0.384 -0.584  1.304  0.064  0.536  0.096
    [1081] -0.264 -1.336 -0.256 -0.184  1.664 -0.784 -1.104  1.696 -0.944 -0.096
    [1091]  0.136 -0.056 -0.064  0.136 -0.776  0.264 -0.256  0.016  0.744  0.904
    [1101] -1.104 -0.416  0.504 -1.064  0.144  0.536 -1.136  0.944  0.704 -0.256
    [1111]  0.616  0.736 -0.024  0.856 -0.944 -0.024 -0.336  1.056 -1.104  0.016
    [1121]  0.384  0.064 -0.544 -0.744 -0.256 -0.384 -0.584 -0.336 -0.504  0.104
    [1131] -0.904 -0.496  0.896  1.384 -0.616 -0.944  0.176  0.896 -0.704  0.064
    [1141]  0.736  0.384  1.104  0.896  1.296  0.056 -0.856  0.736 -0.904 -0.144
    [1151]  0.696  0.776  0.944  0.136  0.584  0.056 -1.104  1.096 -1.224  0.856
    [1161] -0.664 -0.176 -0.744  0.864 -0.224  1.104  0.224  0.256  0.744 -0.944
    [1171]  0.304  0.096 -0.616 -0.496  0.064 -0.256 -0.744  0.464  0.864 -0.256
    [1181]  1.376 -0.624 -0.864  0.224 -0.944 -0.384  0.904 -0.784 -0.904  0.296
    [1191] -0.056 -0.096 -1.136 -0.104 -1.224 -0.264 -0.064  0.904  0.616  0.864
    [1201]  0.136  1.064 -0.144 -0.064 -0.304 -0.136  1.296 -0.064 -0.184 -0.104
    [1211]  1.104  0.104 -0.144  0.224  0.304 -0.384  0.744 -1.104  1.144  0.144
    [1221] -0.896 -0.144 -0.016  0.536  0.304  0.624 -0.576 -0.304 -0.584  0.624
    [1231] -1.144 -0.384  0.744  0.864 -0.224  0.384  0.616  0.536  0.064  0.024
    [1241] -1.144 -0.584 -0.544  0.184 -0.064  0.496 -0.664  1.376 -0.424 -0.864
    [1251]  0.096 -0.384 -0.336  0.336  0.584 -0.056 -0.736  0.016  0.784 -0.216
    [1261]  0.136  0.896  0.496  0.896 -0.216 -0.056 -0.304 -0.024  0.424  0.144
    [1271]  0.896 -1.144  0.144  0.824 -0.744  0.216  0.616 -0.376 -1.064  1.504
    [1281]  0.664  0.096 -0.176 -0.504  0.896  0.504 -0.304 -1.144 -1.696  0.584
    [1291] -0.096  1.184 -0.216  0.896  1.384  0.744  0.496 -0.584 -0.296 -1.136
    [1301]  0.824  0.864  0.064 -0.736  0.016 -1.104 -0.824  0.176  1.104  1.096
    [1311]  1.664 -0.424  1.064 -0.224 -0.064 -0.904  0.384 -0.576  0.736  0.304
    [1321] -0.736 -0.664 -0.304  0.784  0.584 -0.216  0.104 -0.744  0.024 -0.216
    [1331] -0.744  0.584 -0.176 -0.104  0.264 -0.144  0.696  0.696  0.856  0.344
    [1341] -0.256 -0.616  0.336 -0.904 -0.784  0.416 -0.144 -0.256  0.056 -0.024
    [1351] -1.696 -1.384 -0.136  1.744  0.544 -1.344 -0.096 -0.096  1.136 -0.784
    [1361] -0.176 -0.584  0.296  1.224  0.016 -0.304  1.704  0.736  0.304  0.776
    [1371] -1.704 -0.904  1.056 -1.224 -0.584 -0.424  0.104 -0.504 -0.744  0.104
    [1381] -0.664 -0.384  0.304  0.864 -0.584  0.536 -0.896  0.136  0.056  0.104
    [1391] -0.256  0.904 -0.696  0.056 -0.544  0.864 -0.064  0.216 -0.504  1.384
    [1401] -0.776  0.384  0.536  0.384  0.744 -0.384  0.904 -0.344 -0.064 -0.424
    [1411]  0.616  0.296 -0.136 -0.136 -1.696 -1.224  0.216 -0.336 -0.224  0.384
    [1421] -0.416  0.856 -0.504  0.344 -0.224 -0.904  0.184  1.296  0.056 -0.104
    [1431]  0.296  0.064 -0.064 -1.296 -1.056 -0.704  1.344 -0.224  0.384 -0.016
    [1441] -0.304  0.704  0.264  0.904  0.336  1.704  0.504  0.864  0.224 -0.856
    [1451]  0.696  0.096 -0.056 -0.576 -0.496 -0.256  0.384  0.896 -0.064 -0.216
    [1461] -0.416  0.064  0.744  0.176  0.464 -0.896  0.104  0.584 -0.336  0.064
    [1471]  0.224 -1.336  0.336 -1.384 -0.696  0.536 -0.776 -0.776  0.424 -0.864
    [1481] -1.704 -0.096 -1.376  0.296  1.344  0.296 -1.224 -0.064 -1.504 -0.664
    [1491]  0.784  0.784 -0.696 -0.144  0.824 -1.696 -0.536 -0.744  0.736  0.104
    [1501]  0.224 -0.544 -0.256 -0.064 -0.136  0.784 -1.504  1.696 -1.384 -0.224
    [1511] -0.216  0.736 -0.704  0.296  0.056 -0.304  0.664 -1.304  0.304 -0.144
    [1521]  0.864  0.696 -0.304  1.296 -0.264  1.096 -0.336 -0.224  1.336 -0.424
    [1531] -0.544 -1.344  0.736 -0.904 -0.536 -0.696 -1.504 -0.576  0.464  0.064
    [1541]  0.176  0.856  0.384 -0.576  0.544  0.496 -0.744  0.384  0.376  0.336
    [1551] -0.536  1.744  0.544 -0.824  1.144  0.064 -0.904  0.944  0.264  0.336
    [1561] -0.096 -0.304  0.536 -0.216  0.856  0.544 -0.864  0.104  0.304 -0.096
    [1571] -1.096  0.904 -0.256  0.264 -0.736  0.024 -0.584  0.744 -0.384 -0.256
    [1581]  0.336  0.464  0.104  1.144  1.104 -0.704  0.224 -0.216 -0.376  1.664
    [1591]  0.264 -0.496 -0.584 -0.944 -0.024 -0.336 -0.696 -0.696  0.736 -0.536
    [1601] -0.224  0.856  0.544  0.056 -0.704 -0.144 -0.544  0.224 -0.384 -0.864
    [1611]  0.864 -0.216 -0.304  0.296 -0.504 -0.544  0.304 -0.744 -0.136  0.584
    [1621]  1.304 -1.344  0.264  1.744 -0.744 -0.696  0.544  0.536  0.584  0.264
    [1631]  1.744  0.944 -0.664 -0.744  0.424 -0.184 -0.024  0.384  0.696 -0.024
    [1641]  0.336 -0.584 -0.224 -0.064  0.304  1.104 -0.056  0.336 -0.224 -0.056
    [1651]  0.856  0.144 -0.264  0.336  0.544 -0.856 -0.096  0.424  1.504  0.056
    [1661]  0.264  0.864 -1.696  0.944 -1.344  0.864  0.224  0.736 -0.304  1.376
    [1671]  0.416  0.744  0.376 -0.904 -0.144  0.336 -0.096 -0.064 -0.384 -0.744
    [1681] -0.216 -0.576  1.704  0.896  0.256  0.464 -0.944 -0.144  0.864  0.464
    [1691] -1.104 -0.256 -1.664  0.336 -0.424 -0.304 -0.944 -0.096 -0.696  0.384
    [1701]  0.584  0.056  0.136 -1.104 -0.104  0.144  1.104  1.744  0.376 -0.736
    [1711]  0.696 -0.896 -0.304  0.744  1.704  0.664 -1.104  0.344 -0.944  0.496
    [1721]  0.304  0.336 -1.744  0.304 -0.504 -0.704 -0.736 -0.576 -1.136 -0.016
    [1731]  0.256 -0.256 -0.624  0.784 -1.376  0.304  0.144 -0.544  0.256  0.144
    [1741]  0.584  0.544  0.056 -0.536 -0.256  0.416  0.376  0.144  0.784 -0.176
    [1751]  0.104 -0.224 -0.864 -1.056 -1.704  0.104  0.784  0.096  0.864  0.096
    [1761] -0.224  0.336  0.136  0.064  0.144 -1.064 -0.104 -0.664 -1.336 -0.256
    [1771]  1.696  0.264  0.736  0.176  0.576  0.416  0.776  0.664 -0.904  0.584
    [1781] -0.384  0.216  0.176 -0.736 -0.904 -0.304  0.096 -0.064  0.384  1.136
    [1791] -1.336  0.584 -0.376  0.416  1.136  1.096  0.496  0.736 -0.304  0.864
    [1801] -0.024  0.856  0.616  0.584  0.016  0.944  0.176  0.104 -1.336 -0.544
    [1811] -0.056  0.136 -0.904 -0.904 -0.824 -0.504 -0.096  1.376  0.104  0.144
    [1821] -0.144  0.064 -0.496 -0.536  0.056  0.384  0.024  1.344 -1.184 -0.064
    [1831]  0.896  0.896 -0.024  0.184 -0.056  0.584  0.336  0.336 -0.224  0.024
    [1841] -0.424  0.616  0.896  0.136 -1.056  0.216 -0.504 -0.136 -0.544  0.416
    [1851]  0.016 -0.056  0.904 -0.216 -0.344  0.736  1.184 -0.304 -0.064  0.736
    [1861] -0.736 -0.336  0.664  1.096 -0.056  0.536 -0.856 -0.904  0.064 -0.104
    [1871] -0.736 -0.416  1.184  0.136  0.296  1.136  0.256 -0.344  0.384  1.104
    [1881] -1.136 -0.664 -0.696  1.376  0.416  0.096  0.184 -1.144  0.704 -0.864
    [1891] -0.584 -0.256 -1.296 -0.384  1.104  1.056  0.864  0.416  0.064  0.384
    [1901] -0.776 -0.096 -0.264 -0.184  1.696  1.064  0.864 -0.664  0.504  0.104
    [1911] -0.704  0.744 -0.256  0.416  0.936 -0.776  0.536 -1.696  0.384 -0.576
    [1921] -0.704 -0.696 -0.024 -0.896  0.136  0.616 -0.104  0.864 -0.336  0.856
    [1931]  0.896 -0.544  0.536  0.744  0.176  0.464  0.224  0.264  0.144 -0.784
    [1941] -1.296 -0.016 -0.896  0.304 -1.136 -1.504 -0.216 -0.064 -0.584 -0.784
    [1951] -0.696 -0.144 -0.344 -0.176  0.424 -0.384 -0.696  1.704 -0.056 -0.584
    [1961]  0.424  0.696  0.424 -0.536  0.544 -0.144  0.184 -0.064  1.296 -0.064
    [1971] -0.144  1.104 -0.784 -0.536  0.144 -0.336  0.576  0.296 -0.184  1.136
    [1981]  0.544  0.384 -0.544  0.216 -0.136  0.504 -0.696 -0.584  1.376 -0.296
    [1991]  0.384  0.304  0.304 -0.616  0.736 -0.864  0.304  0.944 -0.744 -1.304
    [2001] -0.336 -1.096 -0.256  0.744 -0.584  0.616  0.696 -0.464 -0.424  0.824
    [2011]  0.744 -0.296 -1.136 -0.184 -0.416 -0.256  1.384 -1.136 -0.144  1.704
    [2021]  0.384 -0.576 -0.416 -0.504 -0.736  0.896  0.464 -0.224  0.696 -0.576
    [2031]  0.584 -0.584 -0.336  0.296  0.344  0.336 -0.704  0.544  0.536 -0.424
    [2041] -0.176  0.496 -0.224  0.256  0.264 -0.016  1.704 -0.864  0.584 -0.776
    [2051] -0.176  1.664 -0.216  1.104  1.136 -0.904 -0.904  0.336 -0.696  0.736
    [2061] -0.256 -0.056  0.744 -0.664 -0.096  0.264 -1.296 -0.904  0.024  1.136
    [2071]  0.384 -0.416  0.144  0.664  0.224 -0.584 -0.776 -0.944 -1.376 -0.376
    [2081] -0.504 -0.896  0.176 -0.136  0.216  1.224  1.336  1.184 -0.416  0.296
    [2091]  0.376  0.704  0.256  1.664 -0.256  0.216  0.704  1.104 -0.096  0.224
    [2101]  0.296  0.056  0.296  0.184  0.704 -0.304  0.784  1.664 -1.704 -0.136
    [2111] -0.896  0.224  1.704 -0.184  0.144 -0.136  1.704 -0.416 -0.776  1.144
    [2121] -0.864 -0.896  0.664 -0.104 -0.504  0.104  0.536  0.304  0.856  0.064
    [2131]  0.856  0.176  0.336 -1.136 -0.864  0.056  0.304  0.584 -0.096 -0.264
    [2141]  0.864 -0.896 -1.056  0.224  0.904 -0.304  0.856 -0.864 -0.424 -1.304
    [2151]  0.624 -0.584 -1.504 -0.304 -0.224  0.104  0.584 -1.096 -1.704  1.304
    [2161]  1.704 -0.104  0.696 -0.944 -0.744  0.696  0.056 -0.336  0.296 -0.584
    [2171] -0.736  0.944  0.704  0.944 -0.904  0.736  0.824 -0.304 -0.184  0.864
    [2181]  0.384 -0.576 -1.664 -1.064 -0.064 -1.064 -0.056 -0.696 -0.896 -0.904
    [2191] -0.616 -1.704  0.704 -0.016  0.304  0.304 -0.256 -0.936  1.504  0.176
    [2201] -0.256  1.704 -0.536 -1.136 -0.064 -0.504 -0.304 -0.776 -0.696  0.856
    [2211]  0.136 -0.016 -0.544 -0.744  0.624 -1.696  0.664  0.216 -0.704  0.176
    [2221] -0.304  0.064 -1.144  0.064  0.496  0.256  0.304  0.424  1.064  1.104
    [2231]  0.864 -0.224 -0.136  0.624 -0.936 -0.304 -0.304 -0.416  0.424  0.136
    [2241]  0.144 -0.136 -0.384  0.096 -0.864  0.136  1.104 -0.864 -0.304 -0.664
    [2251]  0.536 -0.824  0.344 -1.096  0.744  0.696  1.184  0.136  0.744  0.536
    [2261]  0.064  1.096 -1.136  1.376 -0.016  0.304  0.584 -0.424  1.304  0.376
    [2271]  0.064 -0.144 -0.144 -0.744  0.064  0.584  0.056  0.144 -0.104  1.096
    [2281]  0.136 -1.104 -0.376 -0.384  0.536  0.176  1.096 -0.144 -1.136  0.136
    [2291] -0.096  0.256 -1.104 -0.104  0.096 -0.104  0.304  0.504 -0.256  0.264
    [2301] -0.144 -0.896  0.224  0.376  0.744  0.096 -0.336  1.704 -0.496 -0.424
    [2311]  0.784  0.464 -0.696  0.544 -0.744  1.096  1.096  0.496  0.664  0.504
    [2321]  0.896  0.024 -0.784  0.136  0.664 -0.584 -0.304  1.696 -0.776  0.296
    [2331]  0.944  0.024 -0.744 -0.496 -0.224  0.776 -0.744 -0.856  1.224  0.096
    [2341] -0.544  0.776  0.856  0.136 -1.144  0.064 -0.664  0.744 -0.904  0.056
    [2351] -0.944 -1.104  0.336  1.104 -0.736 -0.336  0.096 -1.296 -0.184 -0.136
    [2361] -0.664  0.504  0.144  1.144  0.664 -0.336 -1.296  0.336  0.224  0.064
    [2371] -0.504  0.536  0.864 -0.896  0.576 -1.304  0.144  0.264  0.256  0.664
    [2381] -1.224  0.264  0.024 -0.704  0.264 -0.504  0.024  0.496 -0.576 -0.304
    [2391] -0.144 -0.056 -0.056 -0.896  0.784 -0.016 -0.936  0.544 -0.944  1.296
    [2401] -1.744 -1.136 -1.696 -1.384  0.424 -0.096 -0.616 -0.336 -0.056 -0.056
    [2411] -0.824  0.064 -0.896  0.144 -0.104 -0.664 -0.064  0.776 -1.296 -0.264
    [2421]  1.136  0.424  0.264  0.744  0.256  0.384 -1.384  0.736 -0.136 -0.496
    [2431]  0.096  0.536 -0.784 -0.664  1.376 -0.744 -0.136  0.264 -0.336  0.056
    [2441]  0.576 -0.184  1.336  0.496  1.064 -0.264  0.336 -1.104 -0.024  0.336
    [2451]  1.224  0.864 -0.536 -0.696  1.336  0.216  0.304 -0.864  0.664  0.256
    [2461] -0.696  0.504 -0.624  0.784 -0.536  0.864  0.536 -0.944  0.544 -0.424
    [2471] -0.064  0.144  0.024 -0.056  0.576 -1.104 -1.744 -0.304  0.384 -0.296
    [2481] -0.744  0.296 -0.736  0.104 -1.304 -0.104  1.344 -0.704  0.184  1.064
    [2491]  0.744 -0.376 -0.136  1.184  0.336 -0.696  0.336  0.824  0.224  0.736
    [2501] -0.104 -0.704  0.056 -0.696 -0.496  0.384 -0.024  0.296  1.664  0.904
    [2511]  0.304 -0.056 -0.224 -0.616  1.296  0.336  0.736 -0.504  0.584 -0.416
    [2521] -1.056  0.296 -0.504  0.056 -0.064  0.184 -0.864 -0.704  0.064  0.496
    [2531]  1.104  1.136 -1.384 -0.536  0.064 -0.864  0.856  1.096  0.224  0.784
    [2541]  0.504 -0.104 -0.736 -0.296  0.904  0.936 -0.744  0.176  1.744  1.344
    [2551]  0.424  0.864 -0.264 -0.496 -0.696 -0.704 -0.016 -0.624  0.776  1.744
    [2561] -0.704 -0.904  1.144 -0.144  0.264 -0.536  0.136  1.696 -0.904 -0.296
    [2571]  0.504 -0.024 -1.504 -0.904  0.104 -0.104 -0.344  0.864  0.544  1.504
    [2581] -0.144 -0.904 -0.064  0.104 -0.784 -0.224 -0.576  0.944  0.136 -0.744
    [2591]  0.904  0.064 -1.664 -0.224  1.696  1.144  0.224 -0.224  0.744  0.784
    [2601]  1.744  0.744 -0.224  0.136 -0.536  0.256  0.064  1.384 -1.704 -0.136
    [2611]  0.544 -1.136  1.336  0.096  0.704 -0.176  0.696 -0.504  0.864  0.384
    [2621] -0.664  0.584 -0.856 -0.224  0.304  1.144 -0.376 -0.064  1.744 -0.464
    [2631] -1.664  0.304 -0.704  0.536  0.144  0.104  0.824  0.104 -0.584  0.504
    [2641] -0.344 -0.224 -0.256  0.824  0.944 -0.344  0.136  0.344  0.384  0.536
    [2651]  0.496 -0.496  1.184 -0.224 -0.536 -1.504 -0.304  0.824 -0.824  0.296
    [2661] -0.744 -1.104 -0.936 -0.224 -0.664 -0.056  0.904  1.704  0.224  0.584
    [2671]  0.504 -0.864  0.184  0.064 -0.184  1.704  0.056 -0.896 -0.104 -0.496
    [2681]  1.184  0.024 -0.096  0.056 -0.304  0.216 -0.304  0.736  0.336  1.744
    [2691] -0.384 -0.056  0.376  1.376 -0.144 -0.184 -0.056 -0.256 -1.224 -0.224
    [2701]  0.536  0.504 -0.064  0.376 -0.696 -0.016  0.536  0.896  0.416  0.056
    [2711] -0.336 -0.056  0.664  0.376  1.064  1.064 -1.184 -0.176 -0.256 -1.104
    [2721]  0.736 -0.144  0.936  0.584  0.016  0.944  1.144 -0.064 -1.344  0.264
    [2731] -1.376  0.264  0.064  0.536  0.776 -0.856 -0.304 -0.536 -0.936  0.624
    [2741]  0.864  0.216  0.496 -1.104 -0.696 -0.376  0.824  0.144  1.144  0.384
    [2751] -0.416 -0.376  0.904  0.304  0.136 -1.144  0.216  0.424  1.704  0.256
    [2761] -0.416  0.136  1.336 -0.584 -0.136  0.224  0.064  0.344  0.824  0.576
    [2771]  0.744  0.096  0.536 -1.056  0.304 -0.096  0.496  1.344 -0.536  0.056
    [2781] -0.856 -0.096 -0.744  1.504 -1.064  0.176 -0.584 -1.096  1.384  0.944
    [2791]  0.064 -0.104  0.416 -0.664 -0.024 -1.664 -0.744  1.344  0.144 -0.856
    [2801]  0.704 -0.056 -0.264 -0.024  0.544  0.136  0.536 -0.416  1.744 -0.056
    [2811]  0.376 -0.824 -0.064  0.224 -1.664 -0.056  1.056 -0.584 -1.104 -0.536
    [2821]  0.616 -0.096  0.304  0.096 -0.056 -0.304 -1.696  0.376 -0.144  1.104
    [2831]  1.184  0.304  0.584  0.256 -0.216 -0.336  0.736 -1.296 -0.296  0.264
    [2841]  0.296  0.944  1.144 -0.736 -1.104 -1.144 -1.064  0.136  0.584 -0.304
    [2851] -0.296  0.536  0.296 -0.336  1.384 -0.256  0.224 -0.296  0.304 -0.496
    [2861]  0.776  1.344  0.224 -0.584  0.736 -0.576  1.184  0.056 -0.664  0.376
    [2871]  0.576  0.536 -0.704  0.664 -1.136 -0.584 -0.944  0.416 -0.496 -0.584
    [2881] -0.176  0.304 -0.864 -0.944 -0.136  0.224  0.856 -0.544 -0.256 -0.744
    [2891]  1.376  0.216  0.064  0.144 -0.424  1.504 -1.104 -0.704 -0.904  0.864
    [2901]  1.096 -0.256 -0.024  0.736 -0.424  0.064  0.944 -0.664  0.496  0.704
    [2911] -1.144  0.224  0.496 -0.544 -0.064 -0.704 -0.424  0.824  0.296 -0.304
    [2921] -0.536  1.136 -0.336 -0.856  0.904 -0.336  0.584  0.096  1.096  0.224
    [2931]  0.256 -0.064 -0.424  0.064  0.304  0.504 -0.224 -0.664  0.896  0.384
    [2941] -0.504  1.504 -1.144  1.136  0.544  0.944 -1.336  0.936  0.056  1.056
    [2951]  0.504  1.096  0.224 -0.864 -0.856  0.864 -0.056 -1.144 -0.624  0.104
    [2961] -0.896  1.104  0.536  0.864 -0.776 -0.496  1.144  1.056  0.624 -0.944
    [2971]  0.704  0.696  1.384 -0.296 -0.944  0.904  0.384 -0.504  0.576  0.136
    [2981]  1.384 -0.944 -0.864 -0.224 -0.696  0.864 -0.744  1.304 -0.184  0.744
    [2991]  0.296 -0.384  0.704 -0.664 -0.496 -0.416 -0.576 -0.064 -0.784  1.224
    [3001]  0.144 -0.776  0.096 -0.544 -0.664 -0.584 -1.144  0.384 -0.176 -0.024
    [3011]  0.696 -0.776 -0.616 -0.496  0.176 -1.064  0.416  0.496  0.736 -0.136
    [3021] -1.144  0.384 -0.904  0.616  0.136  0.744 -0.096  0.176 -0.256  0.104
    [3031]  0.864  0.536 -0.784  1.056  0.224  0.584  0.896  0.064 -0.504  0.776
    [3041]  0.424  0.256  0.216  0.064 -0.496 -0.224 -1.376  1.144  0.336  0.064
    [3051]  0.496  0.464 -0.584 -0.296  1.184  0.576 -0.024  0.504 -0.384  1.104
    [3061] -0.104 -1.344  0.824 -0.096  0.544 -0.296  0.336 -0.224  0.296 -0.264
    [3071]  1.136  0.264 -0.216  0.336 -1.064  0.336 -0.904  0.136  1.664 -0.936
    [3081] -1.136 -1.104 -1.744  1.336 -0.584 -0.264 -0.864 -0.704  0.256  0.536
    [3091] -0.384  1.344 -0.056 -0.216  1.056 -1.696  0.344  0.696 -0.224 -0.544
    [3101] -0.464  0.224 -0.696  0.256 -0.696  0.896 -0.424  0.024 -0.224 -1.744
    [3111]  0.664  0.744  1.224 -0.536 -1.144  0.016 -1.336 -0.064 -0.296  0.776
    [3121]  0.064 -0.736  0.056  1.304  0.416  0.256 -0.224  0.416  0.296  0.616
    [3131] -0.744 -0.904 -0.216  0.136  0.024  0.496 -0.704  0.304  0.536  0.176
    [3141]  0.856  0.296  1.336  0.296 -0.056 -1.064  0.424 -0.464 -0.696 -0.744
    [3151]  0.296  0.536  0.904 -0.256  0.216  0.104  0.176  0.856 -0.064  0.384
    [3161]  0.624 -0.296  1.144  1.336 -0.384 -0.336 -0.536  1.704  0.064 -0.416
    [3171] -0.904 -0.416  0.296  1.144  0.096  0.864  0.944 -0.296  0.024  1.696
    [3181] -0.304  0.736 -1.104  0.576 -0.856 -1.376 -0.264  1.056  0.424 -1.304
    [3191]  0.024 -0.584 -0.664  1.336  0.544  0.904  0.256  0.376  0.584  0.744
    [3201] -0.936 -1.144 -0.504 -0.824  1.096  0.576  0.824 -0.144  1.136  1.104
    [3211] -0.296 -0.536 -0.864 -0.576 -0.304 -0.416  0.424 -0.096  0.176  0.744
    [3221] -0.424 -0.304  0.024 -0.696  0.296 -0.096 -0.264  0.664  0.904  0.424
    [3231]  0.264 -0.496  0.336  0.584 -0.216 -0.384 -0.664  0.064  1.096  0.304
    [3241]  0.856 -0.464  0.384 -0.376 -0.704  0.024  0.704 -0.576 -0.856  0.736
    [3251]  0.304 -0.624  0.296 -0.664 -0.584 -1.376  0.224 -1.136  0.536  1.224
    [3261] -1.704  0.264 -0.776  0.736 -0.744  0.256  0.496 -1.336  0.096 -0.696
    [3271]  1.056  0.904 -0.104 -0.384  0.704 -0.256  1.096  0.104  0.136  0.304
    [3281]  0.696  0.744 -1.344  0.336  0.864  0.744 -0.144 -0.224 -0.144  0.544
    [3291] -0.496  0.136  0.064 -1.704 -0.024  0.584  0.904 -0.504 -1.744  0.504
    [3301] -0.416 -0.664 -1.304  0.776  1.304  0.224  0.864 -0.896  0.344 -0.376
    [3311]  1.704  0.944 -0.704  0.384  1.224  1.304  0.944  0.064 -0.856 -0.304
    [3321] -0.024 -0.064  0.096 -0.064  0.224  0.136 -0.896  0.264 -0.536  1.336
    [3331]  0.064  0.144 -0.384 -0.776 -0.224  0.376  0.544  0.944 -0.264  0.584
    [3341]  0.064  0.376  0.544  0.696  1.344  0.544 -1.336 -1.696 -0.896  0.224
    [3351]  0.224  0.064  0.416  1.184  1.144  0.144 -1.144  1.184 -1.744 -0.024
    [3361] -1.224 -0.056  0.616  0.536 -0.216  0.664  0.496  1.304 -0.784 -0.384
    [3371]  0.536 -0.624  1.056  0.696  0.576  0.304  1.296 -0.024 -0.624 -0.024
    [3381]  0.416 -0.256 -0.696 -0.496  0.144 -0.664 -0.296 -0.304 -0.784  1.056
    [3391]  1.376 -0.544 -0.384  0.584  0.064  0.464  0.376 -0.696 -0.864  0.464
    [3401] -1.064  0.144  1.056  0.744  0.296  1.144 -0.096 -0.936 -0.416 -0.576
    [3411] -0.064 -0.104  1.136  0.464 -0.424 -1.696 -0.424  0.864  0.736 -0.504
    [3421]  0.744  0.304  0.184 -0.576 -0.136 -0.864 -1.704  0.224 -0.056  0.584
    [3431] -0.824 -0.104 -0.216 -0.416 -1.304  0.384  0.696  0.744 -0.224 -1.336
    [3441]  0.296  0.944 -0.056 -0.576  0.056 -0.256  0.104  0.376  0.744 -0.376
    [3451] -0.384  0.896 -0.336  0.464  0.024  1.056  0.864  0.856 -0.664 -1.136
    [3461]  0.056 -0.896  0.664  0.664 -0.624 -0.144 -0.056 -0.136 -0.184  1.136
    [3471]  0.856 -0.736  0.096 -1.336  0.544  0.224  0.584  0.384  1.104 -1.696
    [3481] -0.224 -1.696 -0.224 -0.576  1.184  1.744  0.224  0.736  0.424  0.464
    [3491] -0.696 -1.704 -1.184 -0.064 -0.856  0.864 -1.296 -1.304  1.104 -0.784
    [3501] -0.664  0.096 -1.056 -0.536 -0.384 -0.424  0.096 -0.176 -1.296 -0.176
    [3511] -0.344 -0.696  0.224 -0.056 -0.544  0.664  0.336 -1.104  0.136  0.056
    [3521]  0.624  0.736  0.056  1.376  0.024  0.144  0.496  0.944 -0.384  1.296
    [3531]  0.064 -1.344  0.864 -0.064 -0.696 -0.224 -0.064 -1.096 -0.296 -0.624
    [3541]  0.744 -0.176 -0.424  0.384 -0.024 -0.024  0.744  0.304  0.744 -0.056
    [3551] -0.824 -1.744  0.136  0.184  0.064 -0.504  0.104  1.104 -0.544 -0.944
    [3561]  0.904 -0.744 -0.304  1.384  0.416  1.376  0.024 -0.504 -0.176 -0.384
    [3571]  0.536  1.504  0.224 -1.224  0.856  1.064 -0.776 -0.664  0.176 -0.776
    [3581]  0.544 -0.144 -0.096  0.696 -0.624  0.544 -1.304 -0.704  0.864  0.184
    [3591] -0.136 -0.304 -0.224  0.056 -1.704 -0.224 -0.584 -0.904 -0.184 -0.416
    [3601] -1.696  1.104 -0.584  1.064  0.776 -0.744  1.344  1.096 -0.224 -0.064
    [3611]  0.384  0.496  0.784  0.744  0.176  1.104  0.784 -0.864 -1.504 -0.744
    [3621] -0.224 -1.704 -0.224 -0.104 -0.424  0.736  0.016 -1.104  0.776 -1.704
    [3631] -0.544 -0.256  0.584 -0.304  0.504 -0.744 -0.104 -0.544 -0.144  0.384
    [3641] -0.216 -0.304 -0.264  0.056  0.224 -0.664  0.376  0.864 -1.704 -0.704
    [3651] -0.344  1.184  0.104 -0.864 -0.256  1.304 -0.064  0.424 -0.096 -0.296
    [3661]  0.736  0.576  0.104 -0.144 -0.936  0.576 -0.496 -0.896  0.184 -0.744
    [3671] -0.224 -0.736  0.224  0.704  0.904  0.376 -0.144 -0.304 -0.224  0.536
    [3681] -0.496 -0.616  0.344 -1.376  0.536  0.544 -1.744  0.744 -0.136 -0.576
    [3691] -0.136  0.944 -0.136  1.144 -0.664  0.664  0.064  0.856 -0.864  1.096
    [3701]  0.424 -0.776  0.536 -0.064  0.384  0.744 -1.224  0.416 -0.736  0.136
    [3711] -0.296 -0.424 -0.904  0.384  0.264  0.584 -0.376 -0.704  0.576 -0.824
    [3721]  0.904 -0.784  0.216  0.416 -0.056  0.136  0.576 -0.184  0.216  1.296
    [3731] -0.344  0.264  0.104  1.376 -0.304 -0.904 -0.776  0.136 -0.584  1.056
    [3741]  0.376  0.776 -0.184  1.056 -0.424  0.624 -0.384  0.224 -0.104  0.616
    [3751]  1.096  0.224 -0.584  0.464 -0.536  0.616 -1.104  1.224  0.376 -0.504
    [3761]  0.584  0.864 -0.216 -0.144  1.104 -0.224 -0.096  0.504 -0.744 -1.144
    [3771] -0.136  0.744 -0.536 -0.696  0.384  0.224  0.096  0.064  0.144 -0.904
    [3781]  0.024  0.696 -0.896  0.144  0.256  0.064 -1.336 -0.536  0.576  0.536
    [3791]  0.016 -0.464  0.176 -0.584 -0.176 -1.664 -0.864 -0.584  1.304  1.144
    [3801] -0.144 -0.896  0.024  0.664  0.144  0.416  0.336  1.136 -1.064 -0.256
    [3811] -0.304 -0.944 -0.216 -0.864 -0.896 -0.136  0.096 -1.104 -0.664 -0.144
    [3821] -0.096  0.904  0.296 -0.856  0.304  1.136  0.576 -1.184 -0.544  0.744
    [3831]  0.264  0.864 -1.224 -1.304 -0.696  0.256  0.896  0.776  1.696 -0.744
    [3841] -0.104  0.664 -0.144  1.744  0.376 -0.176  0.496  0.144  0.136  1.096
    [3851] -0.896 -0.384 -0.384  0.904 -0.776  0.704 -0.736  1.664 -0.224  1.104
    [3861]  0.104  0.936 -0.584  0.896 -0.104 -0.896  0.144  1.136  0.744  1.224
    [3871]  0.944 -0.704 -1.096 -0.064 -1.504  1.384 -0.496  0.464  0.016  0.304
    [3881]  0.384  1.096 -0.176 -0.856  0.384  0.776 -0.304 -0.344  0.504 -0.256
    [3891]  1.104 -0.944 -1.104 -0.056  1.336 -0.696 -1.184 -0.224  0.256 -0.944
    [3901]  0.504 -0.616  0.544 -0.104 -1.376  0.536 -0.024  0.224  0.216 -0.096
    [3911] -0.416  0.936  0.144 -0.136  0.856  0.016  0.096 -0.096  0.744  0.696
    [3921] -1.744 -0.664 -0.936 -0.584  1.304  0.336  0.184  0.336  0.184 -0.576
    [3931] -0.376 -0.496  0.664 -0.104 -1.104  0.584 -0.744 -0.664  0.336 -0.064
    [3941] -0.496 -0.856  0.096  0.064  0.736  0.624 -1.136 -0.024  0.864  0.616
    [3951]  1.664  0.864 -0.304 -0.136  0.136  0.176 -0.096 -0.144  0.704 -0.176
    [3961]  0.584 -0.584  0.296  0.904 -1.064  0.224  0.864 -0.064 -0.464  0.224
    [3971] -0.256 -0.504 -0.336 -0.856  0.296 -0.104  0.216  0.056 -0.336 -0.824
    [3981] -0.504  1.224  0.744 -0.616 -0.336 -0.216  0.856  0.936  0.096  0.624
    [3991] -1.136 -0.856 -0.184 -1.144 -0.064 -0.376  0.096  1.296 -0.304  0.696
    [4001] -0.704 -0.424 -1.104  0.616  0.776 -0.416 -0.696  0.224 -0.496  0.304
    [4011] -0.904  0.744 -1.184  1.064  1.144 -0.944 -1.344  0.136  0.496  0.736
    [4021]  1.696 -1.696 -0.576  0.064 -0.064 -0.136  0.296 -0.776 -0.104 -1.184
    [4031] -0.376  0.696 -0.896 -1.144  0.224 -0.136 -0.896 -1.384  0.504 -0.256
    [4041] -0.224  1.376  0.224 -0.544 -1.104  1.704 -0.584  1.304  0.256  0.344
    [4051] -0.856 -0.664  0.104 -0.696 -0.376  1.136  1.336 -0.216 -0.584  0.864
    [4061]  1.064 -1.696  0.544 -0.504  0.264 -0.744  0.896  0.576  0.176 -0.136
    [4071] -0.544  0.064 -0.336  0.584 -0.664 -0.664 -1.104 -0.936  0.664  0.664
    [4081] -0.536  0.336  1.664 -0.416 -0.704 -0.216 -0.224 -0.776 -0.216  0.704
    [4091] -1.704  1.224  0.144  0.784 -0.904  0.496 -0.856  1.744  0.104  0.576
    [4101]  0.464  0.584 -0.384  0.504 -0.944 -0.936  0.096 -0.864  0.096  0.704
    [4111] -0.664  0.616 -0.904  1.296 -0.304  0.496  0.904 -1.104  0.584 -0.856
    [4121] -1.136  0.256  0.104 -1.664  0.696  0.896 -0.144 -0.904  1.104 -0.544
    [4131]  0.584  0.264 -1.384  0.264 -1.384  0.104 -0.224 -0.576 -0.784 -0.664
    [4141] -1.384  0.136  0.384 -0.944 -0.184 -0.576  0.536 -1.376  0.496 -0.304
    [4151]  0.104 -0.704  0.056 -0.336 -1.144 -0.216  0.624 -0.264 -0.504 -0.344
    [4161]  0.736 -0.376  0.016  0.064 -0.424 -0.344  0.904  0.504  0.536 -1.104
    [4171]  0.256  0.696  0.304  0.584  1.304 -1.184 -0.256 -0.416  0.224  0.056
    [4181] -1.144  0.264 -0.096 -0.064 -0.184  0.296 -0.936 -1.336 -0.704  1.136
    [4191] -0.584  0.056  0.904  0.544  0.856 -0.056  0.144 -0.376  0.544  0.096
    [4201] -0.384  0.584  1.096  0.704 -0.504 -0.544 -0.336  0.384 -1.744 -0.864
    [4211] -0.104  0.904  0.944  0.776  0.096  0.024 -0.584 -0.136  1.336 -1.504
    [4221]  0.096 -0.024 -0.376  0.544  0.256 -0.664  0.144  0.144  0.776 -0.416
    [4231] -0.096  0.144 -0.304  0.016  0.344 -1.344 -0.776  0.736  0.336  0.536
    [4241] -0.936 -0.296  0.336 -0.384  0.544  0.304  0.696  0.384 -0.144 -0.256
    [4251] -0.144 -0.864  0.664 -1.136 -0.744 -1.056  0.936 -1.224  0.136  0.296
    [4261] -0.584  0.376 -0.464 -1.224  0.216 -1.376  0.064  0.536 -0.216  0.696
    [4271] -0.056 -0.216 -1.504 -1.104 -0.696  0.176 -0.944 -0.176 -0.576  1.376
    [4281]  1.376  0.544 -1.344 -0.416  1.136 -0.864  0.304 -0.864 -1.696  1.336
    [4291]  0.144 -0.256  0.544  0.216  0.536  0.136 -0.024  0.224 -0.744 -0.296
    [4301] -0.704 -0.016  0.136 -0.176 -0.264  0.336 -0.136  1.664  0.704 -1.144
    [4311]  1.384  0.144  0.544  0.256 -0.824 -0.336 -0.424 -0.904  0.216  0.096
    [4321]  1.336  0.736 -0.704 -0.144 -0.536  1.504  0.216 -0.384  0.704  0.664
    [4331]  1.344 -0.536  0.296 -0.096  0.544 -0.736 -1.136  0.504 -1.384 -0.424
    [4341]  0.936 -0.784 -0.576 -1.136 -0.384  0.736  0.336  0.224  0.416  0.664
    [4351]  0.056 -0.584  0.296  1.096 -0.664 -1.136  0.744  0.744  0.024 -1.304
    [4361] -1.224 -0.544  0.144 -0.624 -0.776  0.176  0.584 -0.224 -0.056 -0.664
    [4371] -0.104  0.544 -0.784  0.064  0.176 -0.864 -0.776 -1.064 -0.176  1.744
    [4381] -0.904  0.664  1.696 -0.504  0.616 -0.776  0.616  0.296  0.584  1.144
    [4391] -0.256  0.224  1.096 -0.416 -0.256  0.944 -0.136 -1.104 -1.144 -0.224
    [4401] -0.544 -0.736 -0.736  1.504 -0.184  0.616  0.616 -1.104  1.744 -0.784
    [4411]  0.496 -0.024 -0.224  0.064 -1.064 -0.904  0.056  0.096 -0.696  0.056
    [4421] -0.664 -0.256  0.104 -0.016 -0.064 -0.824 -0.296 -0.784  0.576 -0.704
    [4431] -0.384  0.896 -0.336  0.136  0.576  0.224  0.296 -1.056 -0.136 -0.376
    [4441]  0.896  1.664  1.296 -0.904 -0.736 -0.424 -0.144 -0.224  1.384  0.944
    [4451] -1.304  0.896 -1.384  0.176  0.544 -1.224 -0.296  0.544 -0.904  0.736
    [4461]  0.264  0.536  0.304 -0.224 -1.296 -0.936  0.576  0.696 -0.304  0.104
    [4471] -1.384 -0.624 -0.624 -0.616  0.296 -0.216  0.704 -0.504 -1.336  1.144
    [4481] -1.696  0.384  0.776 -0.064  0.696 -1.144  0.904 -0.624 -0.264  0.424
    [4491]  0.064  0.296 -0.536 -0.256 -0.296  0.224  0.904 -0.296  0.704  1.224
    [4501]  0.496  0.736  0.376 -0.336 -0.736  1.136 -0.104 -0.904  0.296  1.144
    [4511]  1.344 -0.576 -0.384  1.136 -0.016  0.384 -0.056 -0.056  0.416 -0.096
    [4521]  0.696 -1.224  0.136  0.176 -0.496  0.384 -0.216  0.256 -0.416  0.304
    [4531]  0.216 -0.096 -1.296  0.464  0.384  0.144 -0.744  1.344 -0.776 -0.224
    [4541]  1.224  1.376  0.896 -0.224 -0.176  0.176  0.616  0.176  0.824  0.144
    [4551] -0.304 -0.864 -1.296  0.216  0.224 -1.064 -0.496 -0.224  0.304 -0.584
    [4561]  0.296  1.224 -1.136 -0.216  1.704 -0.144  0.904 -1.344 -0.584  1.104
    [4571]  0.104 -0.504  0.144  0.696  0.856 -0.096  0.864  0.256 -0.856 -0.944
    [4581] -0.664  0.224 -0.936 -1.376  0.504  0.104 -0.256  0.224 -1.296 -0.304
    [4591]  0.824  0.496  0.904  1.336  0.544  0.104 -0.256  0.224 -0.584  0.024
    [4601]  0.424  0.384  0.776 -0.064  0.296  0.256 -1.184 -0.864 -0.416 -0.256
    [4611] -1.056 -0.264  0.056 -0.296  0.224 -1.144 -1.744 -0.256  0.144  0.864
    [4621]  1.136  0.064 -1.744 -0.896  0.216  0.256 -0.896  0.304  0.856  1.224
    [4631]  0.704 -0.104  0.304 -0.184 -1.184  1.344 -0.104 -0.744  0.864 -0.384
    [4641]  1.104  1.224 -0.056 -0.056 -0.736 -0.304  0.904  0.544  0.544  0.904
    [4651]  0.264  0.136  0.744 -1.144  1.056  0.296  1.296  0.824  0.536 -0.424
    [4661] -0.136 -0.536 -0.544 -0.704  0.216  0.304 -0.936  0.296 -0.856  0.544
    [4671] -1.296 -0.384 -0.184  0.176 -0.104 -0.296 -1.056  0.296  0.696  0.536
    [4681]  0.064  0.184  0.064 -0.296  0.696 -0.504 -0.056  1.184  0.056  0.544
    [4691] -0.776  0.336 -0.544 -0.664  1.664  0.424  0.776 -0.056  0.856  1.744
    [4701]  0.896  0.744  0.264 -0.384  1.144  0.144 -0.416 -0.336  1.104 -1.504
    [4711]  1.296 -0.304  1.136 -0.584  0.744 -0.696 -1.304  0.256 -0.776  0.064
    [4721] -0.216  0.864 -0.936 -1.144 -0.104  1.104  0.056  0.376  0.584 -0.344
    [4731] -0.024 -0.064  0.376  0.824 -0.056 -0.744 -0.504  0.336  0.336  0.056
    [4741] -1.664 -1.144  0.144  0.384 -0.864 -0.416 -0.304 -0.224  0.304  0.864
    [4751] -1.336 -0.536  0.504 -0.776  1.304  0.224 -0.016  0.864 -0.344  0.304
    [4761] -0.264 -0.096  0.384 -0.304 -0.344 -1.344 -0.536 -0.064 -0.056  0.056
    [4771]  0.576  0.264 -1.144  0.664  0.384 -0.304 -1.744 -0.536 -0.536 -0.384
    [4781] -0.384  0.024  0.216 -0.136 -0.944 -1.704 -0.664  1.664  0.144  0.384
    [4791]  0.784 -0.384 -0.176  0.304 -0.856 -0.024 -0.344  0.856  0.416  0.904
    [4801] -0.544  0.224 -0.856  0.616  0.304 -0.144  0.584 -1.136 -0.544 -0.536
    [4811]  0.296 -1.344  0.296 -0.264 -0.144  0.384 -0.184  0.176 -0.864  0.744
    [4821] -0.504  0.304  0.176  0.576  0.744  0.896  0.664 -0.096  0.104 -0.384
    [4831] -1.704 -1.144  0.584 -0.624  0.304 -0.024  1.504 -1.136  0.256  0.424
    [4841] -0.664  0.064  0.136 -1.304 -1.136 -1.136 -1.184  0.304 -1.104 -1.384
    [4851]  0.216  0.064 -0.664  0.224  0.856  1.184  0.584 -0.376  0.864 -0.904
    [4861]  0.224  0.936  0.096 -0.584  0.384 -0.496  0.056 -0.584  0.104  0.664
    [4871] -0.696 -0.016 -0.624  0.136 -1.296 -0.904 -1.144  0.216  0.944 -0.024
    [4881] -1.384  0.536 -1.184 -0.424 -0.864 -0.136 -0.224 -0.264  0.856  0.536
    [4891] -0.256 -0.336 -1.376  0.296  0.584 -1.336 -0.216 -0.224  1.064 -0.104
    [4901] -0.296 -0.864 -0.144  0.256  0.584 -0.296 -0.064  0.736  0.664  0.904
    [4911]  1.384  0.224  0.664  0.296 -0.736 -0.696  1.744 -0.384  0.144 -0.224
    [4921] -0.776 -1.064 -0.144  0.256 -0.384  1.336  0.224  0.416 -0.856  0.304
    [4931] -1.304  0.216  0.264  0.184 -0.864 -0.304  0.536  1.344  0.576  0.576
    [4941] -0.704 -0.384 -0.096  0.144 -1.056  0.224 -0.104  1.304  0.696 -0.104
    [4951]  0.384 -0.664 -0.824  0.736 -0.904  0.144  0.704  1.136 -1.744 -0.416
    [4961]  1.096 -1.096  0.224 -0.376 -0.696 -0.944  0.544 -0.584 -0.224 -0.096
    [4971] -0.776 -0.496 -1.144  0.944  1.296  0.104 -0.616 -0.064  0.496  1.344
    [4981]  1.136  0.056 -1.696  0.696  0.144  0.184  0.464  1.376 -1.376  0.304
    [4991] -0.664 -0.256 -0.336 -0.224 -0.264  0.496 -0.304  1.376 -1.096  0.264

## Estimate Dist under H0 {data-id="quarto-animate-title"}

## Find Reject Region

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
left_threshold <- quantile(H_0, .025)
right_threshold <- quantile(H_0, .975)
```

## Estimate Dist under H0 {data-id="quarto-animate-title"}

---

[← Power (THIS SLIDE DECK IS NOT FINAL) {#power-this-slide-deck-is-not-final .title}](01-power-this-slide-deck-is-not-final-power-this-slide-deck-is.md) · [Up: contents](index.md) · [An Alternative Hypothesis →](03-an-alternative-hypothesis.md)
