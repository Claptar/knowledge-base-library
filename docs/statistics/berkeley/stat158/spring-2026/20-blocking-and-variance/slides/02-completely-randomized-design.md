---
title: Completely Randomized Design \$CR$$1$$\$
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/20-blocking-and-variance/slides.html
source_file: sources/berkeley-stat158/spring-2026/20-blocking-and-variance/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Completely Randomized Design \$CR$$1$$\$

**Source:** [`20-blocking-and-variance/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/20-blocking-and-variance/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

##

<style>#pciixkyugb table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#pciixkyugb thead, #pciixkyugb tbody, #pciixkyugb tfoot, #pciixkyugb tr, #pciixkyugb td, #pciixkyugb th {
  border-style: none;
}

#pciixkyugb p {
  margin: 0;
  padding: 0;
}

#pciixkyugb .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: 300px;
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

#pciixkyugb .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#pciixkyugb .gt_title {
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

#pciixkyugb .gt_subtitle {
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

#pciixkyugb .gt_heading {
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

#pciixkyugb .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#pciixkyugb .gt_col_headings {
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

#pciixkyugb .gt_col_heading {
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

#pciixkyugb .gt_column_spanner_outer {
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

#pciixkyugb .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#pciixkyugb .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#pciixkyugb .gt_column_spanner {
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

#pciixkyugb .gt_spanner_row {
  border-bottom-style: hidden;
}

#pciixkyugb .gt_group_heading {
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

#pciixkyugb .gt_empty_group_heading {
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

#pciixkyugb .gt_from_md > :first-child {
  margin-top: 0;
}

#pciixkyugb .gt_from_md > :last-child {
  margin-bottom: 0;
}

#pciixkyugb .gt_row {
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

#pciixkyugb .gt_stub {
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

#pciixkyugb .gt_stub_row_group {
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

#pciixkyugb .gt_row_group_first td {
  border-top-width: 2px;
}

#pciixkyugb .gt_row_group_first th {
  border-top-width: 2px;
}

#pciixkyugb .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#pciixkyugb .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#pciixkyugb .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#pciixkyugb .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#pciixkyugb .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#pciixkyugb .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#pciixkyugb .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#pciixkyugb .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#pciixkyugb .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#pciixkyugb .gt_footnotes {
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

#pciixkyugb .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#pciixkyugb .gt_sourcenotes {
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

#pciixkyugb .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#pciixkyugb .gt_left {
  text-align: left;
}

#pciixkyugb .gt_center {
  text-align: center;
}

#pciixkyugb .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#pciixkyugb .gt_font_normal {
  font-weight: normal;
}

#pciixkyugb .gt_font_bold {
  font-weight: bold;
}

#pciixkyugb .gt_font_italic {
  font-style: italic;
}

#pciixkyugb .gt_super {
  font-size: 65%;
}

#pciixkyugb .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#pciixkyugb .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#pciixkyugb .gt_indent_1 {
  text-indent: 5px;
}

#pciixkyugb .gt_indent_2 {
  text-indent: 10px;
}

#pciixkyugb .gt_indent_3 {
  text-indent: 15px;
}

#pciixkyugb .gt_indent_4 {
  text-indent: 20px;
}

#pciixkyugb .gt_indent_5 {
  text-indent: 25px;
}

#pciixkyugb .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#pciixkyugb div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="4" class="gt_heading gt_title gt_font_normal gt_bottom_border">CR[1]: Full Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">1</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">1</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">2</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">15</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)">9</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)">15</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">17</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_1 Y(0)">9.42</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_1 Y(1)">5.75</td>
</tr>
</tbody>
</table>

##

<style>#epbpjbaeqz table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#epbpjbaeqz thead, #epbpjbaeqz tbody, #epbpjbaeqz tfoot, #epbpjbaeqz tr, #epbpjbaeqz td, #epbpjbaeqz th {
  border-style: none;
}

#epbpjbaeqz p {
  margin: 0;
  padding: 0;
}

#epbpjbaeqz .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: 300px;
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

#epbpjbaeqz .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#epbpjbaeqz .gt_title {
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

#epbpjbaeqz .gt_subtitle {
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

#epbpjbaeqz .gt_heading {
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

#epbpjbaeqz .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#epbpjbaeqz .gt_col_headings {
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

#epbpjbaeqz .gt_col_heading {
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

#epbpjbaeqz .gt_column_spanner_outer {
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

#epbpjbaeqz .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#epbpjbaeqz .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#epbpjbaeqz .gt_column_spanner {
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

#epbpjbaeqz .gt_spanner_row {
  border-bottom-style: hidden;
}

#epbpjbaeqz .gt_group_heading {
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

#epbpjbaeqz .gt_empty_group_heading {
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

#epbpjbaeqz .gt_from_md > :first-child {
  margin-top: 0;
}

#epbpjbaeqz .gt_from_md > :last-child {
  margin-bottom: 0;
}

#epbpjbaeqz .gt_row {
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

#epbpjbaeqz .gt_stub {
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

#epbpjbaeqz .gt_stub_row_group {
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

#epbpjbaeqz .gt_row_group_first td {
  border-top-width: 2px;
}

#epbpjbaeqz .gt_row_group_first th {
  border-top-width: 2px;
}

#epbpjbaeqz .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#epbpjbaeqz .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#epbpjbaeqz .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#epbpjbaeqz .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#epbpjbaeqz .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#epbpjbaeqz .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#epbpjbaeqz .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#epbpjbaeqz .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#epbpjbaeqz .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#epbpjbaeqz .gt_footnotes {
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

#epbpjbaeqz .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#epbpjbaeqz .gt_sourcenotes {
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

#epbpjbaeqz .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#epbpjbaeqz .gt_left {
  text-align: left;
}

#epbpjbaeqz .gt_center {
  text-align: center;
}

#epbpjbaeqz .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#epbpjbaeqz .gt_font_normal {
  font-weight: normal;
}

#epbpjbaeqz .gt_font_bold {
  font-weight: bold;
}

#epbpjbaeqz .gt_font_italic {
  font-style: italic;
}

#epbpjbaeqz .gt_super {
  font-size: 65%;
}

#epbpjbaeqz .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#epbpjbaeqz .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#epbpjbaeqz .gt_indent_1 {
  text-indent: 5px;
}

#epbpjbaeqz .gt_indent_2 {
  text-indent: 10px;
}

#epbpjbaeqz .gt_indent_3 {
  text-indent: 15px;
}

#epbpjbaeqz .gt_indent_4 {
  text-indent: 20px;
}

#epbpjbaeqz .gt_indent_5 {
  text-indent: 25px;
}

#epbpjbaeqz .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#epbpjbaeqz div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="4" class="gt_heading gt_title gt_font_normal gt_bottom_border">CR[1]: Experiment 1</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)" style="background-color: #90EE90">1</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)" style="background-color: #90EE90">1</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)" style="background-color: #90EE90">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">2</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)" style="background-color: #90EE90">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)" style="background-color: #90EE90">15</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)">9</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)" style="background-color: #90EE90">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #90EE90">15</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)" style="background-color: #90EE90">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #90EE90">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">17</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.42</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.75</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">11.83</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">4.67</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#tyqazuxhtd table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#tyqazuxhtd thead, #tyqazuxhtd tbody, #tyqazuxhtd tfoot, #tyqazuxhtd tr, #tyqazuxhtd td, #tyqazuxhtd th {
  border-style: none;
}

#tyqazuxhtd p {
  margin: 0;
  padding: 0;
}

#tyqazuxhtd .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
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

#tyqazuxhtd .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#tyqazuxhtd .gt_title {
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

#tyqazuxhtd .gt_subtitle {
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

#tyqazuxhtd .gt_heading {
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

#tyqazuxhtd .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#tyqazuxhtd .gt_col_headings {
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

#tyqazuxhtd .gt_col_heading {
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

#tyqazuxhtd .gt_column_spanner_outer {
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

#tyqazuxhtd .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#tyqazuxhtd .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#tyqazuxhtd .gt_column_spanner {
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

#tyqazuxhtd .gt_spanner_row {
  border-bottom-style: hidden;
}

#tyqazuxhtd .gt_group_heading {
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

#tyqazuxhtd .gt_empty_group_heading {
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

#tyqazuxhtd .gt_from_md > :first-child {
  margin-top: 0;
}

#tyqazuxhtd .gt_from_md > :last-child {
  margin-bottom: 0;
}

#tyqazuxhtd .gt_row {
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

#tyqazuxhtd .gt_stub {
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

#tyqazuxhtd .gt_stub_row_group {
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

#tyqazuxhtd .gt_row_group_first td {
  border-top-width: 2px;
}

#tyqazuxhtd .gt_row_group_first th {
  border-top-width: 2px;
}

#tyqazuxhtd .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#tyqazuxhtd .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#tyqazuxhtd .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#tyqazuxhtd .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#tyqazuxhtd .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#tyqazuxhtd .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#tyqazuxhtd .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#tyqazuxhtd .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#tyqazuxhtd .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#tyqazuxhtd .gt_footnotes {
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

#tyqazuxhtd .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#tyqazuxhtd .gt_sourcenotes {
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

#tyqazuxhtd .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#tyqazuxhtd .gt_left {
  text-align: left;
}

#tyqazuxhtd .gt_center {
  text-align: center;
}

#tyqazuxhtd .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#tyqazuxhtd .gt_font_normal {
  font-weight: normal;
}

#tyqazuxhtd .gt_font_bold {
  font-weight: bold;
}

#tyqazuxhtd .gt_font_italic {
  font-style: italic;
}

#tyqazuxhtd .gt_super {
  font-size: 65%;
}

#tyqazuxhtd .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#tyqazuxhtd .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#tyqazuxhtd .gt_indent_1 {
  text-indent: 5px;
}

#tyqazuxhtd .gt_indent_2 {
  text-indent: 10px;
}

#tyqazuxhtd .gt_indent_3 {
  text-indent: 15px;
}

#tyqazuxhtd .gt_indent_4 {
  text-indent: 20px;
}

#tyqazuxhtd .gt_indent_5 {
  text-indent: 25px;
}

#tyqazuxhtd .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#tyqazuxhtd div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 11.83 | 4.67 | −7.17 |

##

<style>#mpqaujhwtb table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#mpqaujhwtb thead, #mpqaujhwtb tbody, #mpqaujhwtb tfoot, #mpqaujhwtb tr, #mpqaujhwtb td, #mpqaujhwtb th {
  border-style: none;
}

#mpqaujhwtb p {
  margin: 0;
  padding: 0;
}

#mpqaujhwtb .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: 300px;
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

#mpqaujhwtb .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#mpqaujhwtb .gt_title {
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

#mpqaujhwtb .gt_subtitle {
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

#mpqaujhwtb .gt_heading {
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

#mpqaujhwtb .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mpqaujhwtb .gt_col_headings {
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

#mpqaujhwtb .gt_col_heading {
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

#mpqaujhwtb .gt_column_spanner_outer {
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

#mpqaujhwtb .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#mpqaujhwtb .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#mpqaujhwtb .gt_column_spanner {
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

#mpqaujhwtb .gt_spanner_row {
  border-bottom-style: hidden;
}

#mpqaujhwtb .gt_group_heading {
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

#mpqaujhwtb .gt_empty_group_heading {
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

#mpqaujhwtb .gt_from_md > :first-child {
  margin-top: 0;
}

#mpqaujhwtb .gt_from_md > :last-child {
  margin-bottom: 0;
}

#mpqaujhwtb .gt_row {
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

#mpqaujhwtb .gt_stub {
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

#mpqaujhwtb .gt_stub_row_group {
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

#mpqaujhwtb .gt_row_group_first td {
  border-top-width: 2px;
}

#mpqaujhwtb .gt_row_group_first th {
  border-top-width: 2px;
}

#mpqaujhwtb .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#mpqaujhwtb .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#mpqaujhwtb .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#mpqaujhwtb .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mpqaujhwtb .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#mpqaujhwtb .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#mpqaujhwtb .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#mpqaujhwtb .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#mpqaujhwtb .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mpqaujhwtb .gt_footnotes {
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

#mpqaujhwtb .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#mpqaujhwtb .gt_sourcenotes {
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

#mpqaujhwtb .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#mpqaujhwtb .gt_left {
  text-align: left;
}

#mpqaujhwtb .gt_center {
  text-align: center;
}

#mpqaujhwtb .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#mpqaujhwtb .gt_font_normal {
  font-weight: normal;
}

#mpqaujhwtb .gt_font_bold {
  font-weight: bold;
}

#mpqaujhwtb .gt_font_italic {
  font-style: italic;
}

#mpqaujhwtb .gt_super {
  font-size: 65%;
}

#mpqaujhwtb .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#mpqaujhwtb .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#mpqaujhwtb .gt_indent_1 {
  text-indent: 5px;
}

#mpqaujhwtb .gt_indent_2 {
  text-indent: 10px;
}

#mpqaujhwtb .gt_indent_3 {
  text-indent: 15px;
}

#mpqaujhwtb .gt_indent_4 {
  text-indent: 20px;
}

#mpqaujhwtb .gt_indent_5 {
  text-indent: 25px;
}

#mpqaujhwtb .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#mpqaujhwtb div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="4" class="gt_heading gt_title gt_font_normal gt_bottom_border">CR[1]: Experiment 2</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">1</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)" style="background-color: #90EE90">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">1</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)" style="background-color: #90EE90">2</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="background-color: #90EE90">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #90EE90">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">15</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #90EE90">9</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)" style="background-color: #90EE90">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)" style="background-color: #90EE90">16</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)">15</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)" style="background-color: #90EE90">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #90EE90">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">17</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.42</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.75</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">12.00</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">2.67</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#drpdyniwio table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#drpdyniwio thead, #drpdyniwio tbody, #drpdyniwio tfoot, #drpdyniwio tr, #drpdyniwio td, #drpdyniwio th {
  border-style: none;
}

#drpdyniwio p {
  margin: 0;
  padding: 0;
}

#drpdyniwio .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
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

#drpdyniwio .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#drpdyniwio .gt_title {
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

#drpdyniwio .gt_subtitle {
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

#drpdyniwio .gt_heading {
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

#drpdyniwio .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#drpdyniwio .gt_col_headings {
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

#drpdyniwio .gt_col_heading {
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

#drpdyniwio .gt_column_spanner_outer {
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

#drpdyniwio .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#drpdyniwio .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#drpdyniwio .gt_column_spanner {
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

#drpdyniwio .gt_spanner_row {
  border-bottom-style: hidden;
}

#drpdyniwio .gt_group_heading {
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

#drpdyniwio .gt_empty_group_heading {
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

#drpdyniwio .gt_from_md > :first-child {
  margin-top: 0;
}

#drpdyniwio .gt_from_md > :last-child {
  margin-bottom: 0;
}

#drpdyniwio .gt_row {
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

#drpdyniwio .gt_stub {
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

#drpdyniwio .gt_stub_row_group {
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

#drpdyniwio .gt_row_group_first td {
  border-top-width: 2px;
}

#drpdyniwio .gt_row_group_first th {
  border-top-width: 2px;
}

#drpdyniwio .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#drpdyniwio .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#drpdyniwio .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#drpdyniwio .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#drpdyniwio .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#drpdyniwio .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#drpdyniwio .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#drpdyniwio .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#drpdyniwio .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#drpdyniwio .gt_footnotes {
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

#drpdyniwio .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#drpdyniwio .gt_sourcenotes {
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

#drpdyniwio .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#drpdyniwio .gt_left {
  text-align: left;
}

#drpdyniwio .gt_center {
  text-align: center;
}

#drpdyniwio .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#drpdyniwio .gt_font_normal {
  font-weight: normal;
}

#drpdyniwio .gt_font_bold {
  font-weight: bold;
}

#drpdyniwio .gt_font_italic {
  font-style: italic;
}

#drpdyniwio .gt_super {
  font-size: 65%;
}

#drpdyniwio .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#drpdyniwio .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#drpdyniwio .gt_indent_1 {
  text-indent: 5px;
}

#drpdyniwio .gt_indent_2 {
  text-indent: 10px;
}

#drpdyniwio .gt_indent_3 {
  text-indent: 15px;
}

#drpdyniwio .gt_indent_4 {
  text-indent: 20px;
}

#drpdyniwio .gt_indent_5 {
  text-indent: 25px;
}

#drpdyniwio .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#drpdyniwio div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 11.83 | 4.67 | −7.17 |
| 12.00 | 2.67 | −9.33 |

##

<style>#vujdpsiavu table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#vujdpsiavu thead, #vujdpsiavu tbody, #vujdpsiavu tfoot, #vujdpsiavu tr, #vujdpsiavu td, #vujdpsiavu th {
  border-style: none;
}

#vujdpsiavu p {
  margin: 0;
  padding: 0;
}

#vujdpsiavu .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: 300px;
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

#vujdpsiavu .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#vujdpsiavu .gt_title {
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

#vujdpsiavu .gt_subtitle {
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

#vujdpsiavu .gt_heading {
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

#vujdpsiavu .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vujdpsiavu .gt_col_headings {
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

#vujdpsiavu .gt_col_heading {
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

#vujdpsiavu .gt_column_spanner_outer {
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

#vujdpsiavu .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#vujdpsiavu .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#vujdpsiavu .gt_column_spanner {
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

#vujdpsiavu .gt_spanner_row {
  border-bottom-style: hidden;
}

#vujdpsiavu .gt_group_heading {
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

#vujdpsiavu .gt_empty_group_heading {
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

#vujdpsiavu .gt_from_md > :first-child {
  margin-top: 0;
}

#vujdpsiavu .gt_from_md > :last-child {
  margin-bottom: 0;
}

#vujdpsiavu .gt_row {
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

#vujdpsiavu .gt_stub {
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

#vujdpsiavu .gt_stub_row_group {
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

#vujdpsiavu .gt_row_group_first td {
  border-top-width: 2px;
}

#vujdpsiavu .gt_row_group_first th {
  border-top-width: 2px;
}

#vujdpsiavu .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#vujdpsiavu .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#vujdpsiavu .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#vujdpsiavu .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vujdpsiavu .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#vujdpsiavu .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#vujdpsiavu .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#vujdpsiavu .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#vujdpsiavu .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vujdpsiavu .gt_footnotes {
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

#vujdpsiavu .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#vujdpsiavu .gt_sourcenotes {
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

#vujdpsiavu .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#vujdpsiavu .gt_left {
  text-align: left;
}

#vujdpsiavu .gt_center {
  text-align: center;
}

#vujdpsiavu .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#vujdpsiavu .gt_font_normal {
  font-weight: normal;
}

#vujdpsiavu .gt_font_bold {
  font-weight: bold;
}

#vujdpsiavu .gt_font_italic {
  font-style: italic;
}

#vujdpsiavu .gt_super {
  font-size: 65%;
}

#vujdpsiavu .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#vujdpsiavu .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#vujdpsiavu .gt_indent_1 {
  text-indent: 5px;
}

#vujdpsiavu .gt_indent_2 {
  text-indent: 10px;
}

#vujdpsiavu .gt_indent_3 {
  text-indent: 15px;
}

#vujdpsiavu .gt_indent_4 {
  text-indent: 20px;
}

#vujdpsiavu .gt_indent_5 {
  text-indent: 25px;
}

#vujdpsiavu .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#vujdpsiavu div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="4" class="gt_heading gt_title gt_font_normal gt_bottom_border">CR[1]: Experiment 3</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">1</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)" style="background-color: #90EE90">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">1</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)" style="background-color: #90EE90">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">2</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #90EE90">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="background-color: #90EE90">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)" style="background-color: #90EE90">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">15</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #90EE90">9</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)" style="background-color: #90EE90">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #90EE90">15</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)" style="background-color: #90EE90">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #90EE90">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">17</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.42</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.75</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">8.50</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">7.33</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#yaemypgtog table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#yaemypgtog thead, #yaemypgtog tbody, #yaemypgtog tfoot, #yaemypgtog tr, #yaemypgtog td, #yaemypgtog th {
  border-style: none;
}

#yaemypgtog p {
  margin: 0;
  padding: 0;
}

#yaemypgtog .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
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

#yaemypgtog .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#yaemypgtog .gt_title {
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

#yaemypgtog .gt_subtitle {
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

#yaemypgtog .gt_heading {
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

#yaemypgtog .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#yaemypgtog .gt_col_headings {
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

#yaemypgtog .gt_col_heading {
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

#yaemypgtog .gt_column_spanner_outer {
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

#yaemypgtog .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#yaemypgtog .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#yaemypgtog .gt_column_spanner {
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

#yaemypgtog .gt_spanner_row {
  border-bottom-style: hidden;
}

#yaemypgtog .gt_group_heading {
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

#yaemypgtog .gt_empty_group_heading {
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

#yaemypgtog .gt_from_md > :first-child {
  margin-top: 0;
}

#yaemypgtog .gt_from_md > :last-child {
  margin-bottom: 0;
}

#yaemypgtog .gt_row {
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

#yaemypgtog .gt_stub {
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

#yaemypgtog .gt_stub_row_group {
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

#yaemypgtog .gt_row_group_first td {
  border-top-width: 2px;
}

#yaemypgtog .gt_row_group_first th {
  border-top-width: 2px;
}

#yaemypgtog .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#yaemypgtog .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#yaemypgtog .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#yaemypgtog .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#yaemypgtog .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#yaemypgtog .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#yaemypgtog .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#yaemypgtog .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#yaemypgtog .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#yaemypgtog .gt_footnotes {
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

#yaemypgtog .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#yaemypgtog .gt_sourcenotes {
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

#yaemypgtog .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#yaemypgtog .gt_left {
  text-align: left;
}

#yaemypgtog .gt_center {
  text-align: center;
}

#yaemypgtog .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#yaemypgtog .gt_font_normal {
  font-weight: normal;
}

#yaemypgtog .gt_font_bold {
  font-weight: bold;
}

#yaemypgtog .gt_font_italic {
  font-style: italic;
}

#yaemypgtog .gt_super {
  font-size: 65%;
}

#yaemypgtog .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#yaemypgtog .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#yaemypgtog .gt_indent_1 {
  text-indent: 5px;
}

#yaemypgtog .gt_indent_2 {
  text-indent: 10px;
}

#yaemypgtog .gt_indent_3 {
  text-indent: 15px;
}

#yaemypgtog .gt_indent_4 {
  text-indent: 20px;
}

#yaemypgtog .gt_indent_5 {
  text-indent: 25px;
}

#yaemypgtog .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#yaemypgtog div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 11.83 | 4.67 | −7.17 |
| 12.00 | 2.67 | −9.33 |
| 8.50 | 7.33 | −1.17 |

##

<style>#jefmatjfnu table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#jefmatjfnu thead, #jefmatjfnu tbody, #jefmatjfnu tfoot, #jefmatjfnu tr, #jefmatjfnu td, #jefmatjfnu th {
  border-style: none;
}

#jefmatjfnu p {
  margin: 0;
  padding: 0;
}

#jefmatjfnu .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: 300px;
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

#jefmatjfnu .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#jefmatjfnu .gt_title {
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

#jefmatjfnu .gt_subtitle {
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

#jefmatjfnu .gt_heading {
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

#jefmatjfnu .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#jefmatjfnu .gt_col_headings {
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

#jefmatjfnu .gt_col_heading {
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

#jefmatjfnu .gt_column_spanner_outer {
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

#jefmatjfnu .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#jefmatjfnu .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#jefmatjfnu .gt_column_spanner {
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

#jefmatjfnu .gt_spanner_row {
  border-bottom-style: hidden;
}

#jefmatjfnu .gt_group_heading {
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

#jefmatjfnu .gt_empty_group_heading {
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

#jefmatjfnu .gt_from_md > :first-child {
  margin-top: 0;
}

#jefmatjfnu .gt_from_md > :last-child {
  margin-bottom: 0;
}

#jefmatjfnu .gt_row {
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

#jefmatjfnu .gt_stub {
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

#jefmatjfnu .gt_stub_row_group {
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

#jefmatjfnu .gt_row_group_first td {
  border-top-width: 2px;
}

#jefmatjfnu .gt_row_group_first th {
  border-top-width: 2px;
}

#jefmatjfnu .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#jefmatjfnu .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#jefmatjfnu .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#jefmatjfnu .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#jefmatjfnu .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#jefmatjfnu .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#jefmatjfnu .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#jefmatjfnu .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#jefmatjfnu .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#jefmatjfnu .gt_footnotes {
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

#jefmatjfnu .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#jefmatjfnu .gt_sourcenotes {
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

#jefmatjfnu .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#jefmatjfnu .gt_left {
  text-align: left;
}

#jefmatjfnu .gt_center {
  text-align: center;
}

#jefmatjfnu .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#jefmatjfnu .gt_font_normal {
  font-weight: normal;
}

#jefmatjfnu .gt_font_bold {
  font-weight: bold;
}

#jefmatjfnu .gt_font_italic {
  font-style: italic;
}

#jefmatjfnu .gt_super {
  font-size: 65%;
}

#jefmatjfnu .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#jefmatjfnu .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#jefmatjfnu .gt_indent_1 {
  text-indent: 5px;
}

#jefmatjfnu .gt_indent_2 {
  text-indent: 10px;
}

#jefmatjfnu .gt_indent_3 {
  text-indent: 15px;
}

#jefmatjfnu .gt_indent_4 {
  text-indent: 20px;
}

#jefmatjfnu .gt_indent_5 {
  text-indent: 25px;
}

#jefmatjfnu .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#jefmatjfnu div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="4" class="gt_heading gt_title gt_font_normal gt_bottom_border">CR[1]: Experiment 4</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)" style="background-color: #90EE90">1</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)" style="background-color: #90EE90">1</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)" style="background-color: #90EE90">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">2</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #90EE90">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="background-color: #90EE90">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #90EE90">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">15</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #90EE90">9</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)" style="background-color: #90EE90">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #90EE90">15</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)" style="background-color: #90EE90">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)" style="background-color: #90EE90">17</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.42</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.75</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">7.50</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">7.83</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#brkncogdaw table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#brkncogdaw thead, #brkncogdaw tbody, #brkncogdaw tfoot, #brkncogdaw tr, #brkncogdaw td, #brkncogdaw th {
  border-style: none;
}

#brkncogdaw p {
  margin: 0;
  padding: 0;
}

#brkncogdaw .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
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

#brkncogdaw .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#brkncogdaw .gt_title {
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

#brkncogdaw .gt_subtitle {
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

#brkncogdaw .gt_heading {
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

#brkncogdaw .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#brkncogdaw .gt_col_headings {
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

#brkncogdaw .gt_col_heading {
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

#brkncogdaw .gt_column_spanner_outer {
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

#brkncogdaw .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#brkncogdaw .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#brkncogdaw .gt_column_spanner {
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

#brkncogdaw .gt_spanner_row {
  border-bottom-style: hidden;
}

#brkncogdaw .gt_group_heading {
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

#brkncogdaw .gt_empty_group_heading {
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

#brkncogdaw .gt_from_md > :first-child {
  margin-top: 0;
}

#brkncogdaw .gt_from_md > :last-child {
  margin-bottom: 0;
}

#brkncogdaw .gt_row {
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

#brkncogdaw .gt_stub {
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

#brkncogdaw .gt_stub_row_group {
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

#brkncogdaw .gt_row_group_first td {
  border-top-width: 2px;
}

#brkncogdaw .gt_row_group_first th {
  border-top-width: 2px;
}

#brkncogdaw .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#brkncogdaw .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#brkncogdaw .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#brkncogdaw .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#brkncogdaw .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#brkncogdaw .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#brkncogdaw .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#brkncogdaw .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#brkncogdaw .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#brkncogdaw .gt_footnotes {
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

#brkncogdaw .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#brkncogdaw .gt_sourcenotes {
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

#brkncogdaw .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#brkncogdaw .gt_left {
  text-align: left;
}

#brkncogdaw .gt_center {
  text-align: center;
}

#brkncogdaw .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#brkncogdaw .gt_font_normal {
  font-weight: normal;
}

#brkncogdaw .gt_font_bold {
  font-weight: bold;
}

#brkncogdaw .gt_font_italic {
  font-style: italic;
}

#brkncogdaw .gt_super {
  font-size: 65%;
}

#brkncogdaw .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#brkncogdaw .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#brkncogdaw .gt_indent_1 {
  text-indent: 5px;
}

#brkncogdaw .gt_indent_2 {
  text-indent: 10px;
}

#brkncogdaw .gt_indent_3 {
  text-indent: 15px;
}

#brkncogdaw .gt_indent_4 {
  text-indent: 20px;
}

#brkncogdaw .gt_indent_5 {
  text-indent: 25px;
}

#brkncogdaw .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#brkncogdaw div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 11.83 | 4.67 | −7.17 |
| 12.00 | 2.67 | −9.33 |
| 8.50 | 7.33 | −1.17 |
| 7.50 | 7.83 | 0.33 |

##

<style>#qztzdvpboq table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#qztzdvpboq thead, #qztzdvpboq tbody, #qztzdvpboq tfoot, #qztzdvpboq tr, #qztzdvpboq td, #qztzdvpboq th {
  border-style: none;
}

#qztzdvpboq p {
  margin: 0;
  padding: 0;
}

#qztzdvpboq .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: 300px;
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

#qztzdvpboq .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#qztzdvpboq .gt_title {
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

#qztzdvpboq .gt_subtitle {
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

#qztzdvpboq .gt_heading {
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

#qztzdvpboq .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#qztzdvpboq .gt_col_headings {
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

#qztzdvpboq .gt_col_heading {
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

#qztzdvpboq .gt_column_spanner_outer {
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

#qztzdvpboq .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#qztzdvpboq .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#qztzdvpboq .gt_column_spanner {
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

#qztzdvpboq .gt_spanner_row {
  border-bottom-style: hidden;
}

#qztzdvpboq .gt_group_heading {
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

#qztzdvpboq .gt_empty_group_heading {
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

#qztzdvpboq .gt_from_md > :first-child {
  margin-top: 0;
}

#qztzdvpboq .gt_from_md > :last-child {
  margin-bottom: 0;
}

#qztzdvpboq .gt_row {
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

#qztzdvpboq .gt_stub {
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

#qztzdvpboq .gt_stub_row_group {
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

#qztzdvpboq .gt_row_group_first td {
  border-top-width: 2px;
}

#qztzdvpboq .gt_row_group_first th {
  border-top-width: 2px;
}

#qztzdvpboq .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#qztzdvpboq .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#qztzdvpboq .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#qztzdvpboq .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#qztzdvpboq .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#qztzdvpboq .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#qztzdvpboq .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#qztzdvpboq .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#qztzdvpboq .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#qztzdvpboq .gt_footnotes {
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

#qztzdvpboq .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#qztzdvpboq .gt_sourcenotes {
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

#qztzdvpboq .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#qztzdvpboq .gt_left {
  text-align: left;
}

#qztzdvpboq .gt_center {
  text-align: center;
}

#qztzdvpboq .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#qztzdvpboq .gt_font_normal {
  font-weight: normal;
}

#qztzdvpboq .gt_font_bold {
  font-weight: bold;
}

#qztzdvpboq .gt_font_italic {
  font-style: italic;
}

#qztzdvpboq .gt_super {
  font-size: 65%;
}

#qztzdvpboq .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#qztzdvpboq .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#qztzdvpboq .gt_indent_1 {
  text-indent: 5px;
}

#qztzdvpboq .gt_indent_2 {
  text-indent: 10px;
}

#qztzdvpboq .gt_indent_3 {
  text-indent: 15px;
}

#qztzdvpboq .gt_indent_4 {
  text-indent: 20px;
}

#qztzdvpboq .gt_indent_5 {
  text-indent: 25px;
}

#qztzdvpboq .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#qztzdvpboq div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="4" class="gt_heading gt_title gt_font_normal gt_bottom_border">CR[1]: Experiment 5</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)" style="background-color: #90EE90">1</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)" style="background-color: #90EE90">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">1</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)" style="background-color: #90EE90">2</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="background-color: #90EE90">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #90EE90">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">15</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #90EE90">9</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)" style="background-color: #90EE90">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #90EE90">15</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)" style="background-color: #90EE90">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #90EE90">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">17</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.42</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.75</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">9.67</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">5.67</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#mvcwlxhzjb table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#mvcwlxhzjb thead, #mvcwlxhzjb tbody, #mvcwlxhzjb tfoot, #mvcwlxhzjb tr, #mvcwlxhzjb td, #mvcwlxhzjb th {
  border-style: none;
}

#mvcwlxhzjb p {
  margin: 0;
  padding: 0;
}

#mvcwlxhzjb .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
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

#mvcwlxhzjb .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#mvcwlxhzjb .gt_title {
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

#mvcwlxhzjb .gt_subtitle {
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

#mvcwlxhzjb .gt_heading {
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

#mvcwlxhzjb .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mvcwlxhzjb .gt_col_headings {
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

#mvcwlxhzjb .gt_col_heading {
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

#mvcwlxhzjb .gt_column_spanner_outer {
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

#mvcwlxhzjb .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#mvcwlxhzjb .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#mvcwlxhzjb .gt_column_spanner {
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

#mvcwlxhzjb .gt_spanner_row {
  border-bottom-style: hidden;
}

#mvcwlxhzjb .gt_group_heading {
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

#mvcwlxhzjb .gt_empty_group_heading {
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

#mvcwlxhzjb .gt_from_md > :first-child {
  margin-top: 0;
}

#mvcwlxhzjb .gt_from_md > :last-child {
  margin-bottom: 0;
}

#mvcwlxhzjb .gt_row {
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

#mvcwlxhzjb .gt_stub {
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

#mvcwlxhzjb .gt_stub_row_group {
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

#mvcwlxhzjb .gt_row_group_first td {
  border-top-width: 2px;
}

#mvcwlxhzjb .gt_row_group_first th {
  border-top-width: 2px;
}

#mvcwlxhzjb .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#mvcwlxhzjb .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#mvcwlxhzjb .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#mvcwlxhzjb .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mvcwlxhzjb .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#mvcwlxhzjb .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#mvcwlxhzjb .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#mvcwlxhzjb .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#mvcwlxhzjb .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#mvcwlxhzjb .gt_footnotes {
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

#mvcwlxhzjb .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#mvcwlxhzjb .gt_sourcenotes {
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

#mvcwlxhzjb .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#mvcwlxhzjb .gt_left {
  text-align: left;
}

#mvcwlxhzjb .gt_center {
  text-align: center;
}

#mvcwlxhzjb .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#mvcwlxhzjb .gt_font_normal {
  font-weight: normal;
}

#mvcwlxhzjb .gt_font_bold {
  font-weight: bold;
}

#mvcwlxhzjb .gt_font_italic {
  font-style: italic;
}

#mvcwlxhzjb .gt_super {
  font-size: 65%;
}

#mvcwlxhzjb .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#mvcwlxhzjb .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#mvcwlxhzjb .gt_indent_1 {
  text-indent: 5px;
}

#mvcwlxhzjb .gt_indent_2 {
  text-indent: 10px;
}

#mvcwlxhzjb .gt_indent_3 {
  text-indent: 15px;
}

#mvcwlxhzjb .gt_indent_4 {
  text-indent: 20px;
}

#mvcwlxhzjb .gt_indent_5 {
  text-indent: 25px;
}

#mvcwlxhzjb .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#mvcwlxhzjb div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 11.83 | 4.67 | −7.17 |
| 12.00 | 2.67 | −9.33 |
| 8.50 | 7.33 | −1.17 |
| 7.50 | 7.83 | 0.33 |
| 9.67 | 5.67 | −4.00 |

##

<style>#pqfbetdrtz table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#pqfbetdrtz thead, #pqfbetdrtz tbody, #pqfbetdrtz tfoot, #pqfbetdrtz tr, #pqfbetdrtz td, #pqfbetdrtz th {
  border-style: none;
}

#pqfbetdrtz p {
  margin: 0;
  padding: 0;
}

#pqfbetdrtz .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: 300px;
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

#pqfbetdrtz .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#pqfbetdrtz .gt_title {
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

#pqfbetdrtz .gt_subtitle {
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

#pqfbetdrtz .gt_heading {
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

#pqfbetdrtz .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#pqfbetdrtz .gt_col_headings {
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

#pqfbetdrtz .gt_col_heading {
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

#pqfbetdrtz .gt_column_spanner_outer {
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

#pqfbetdrtz .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#pqfbetdrtz .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#pqfbetdrtz .gt_column_spanner {
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

#pqfbetdrtz .gt_spanner_row {
  border-bottom-style: hidden;
}

#pqfbetdrtz .gt_group_heading {
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

#pqfbetdrtz .gt_empty_group_heading {
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

#pqfbetdrtz .gt_from_md > :first-child {
  margin-top: 0;
}

#pqfbetdrtz .gt_from_md > :last-child {
  margin-bottom: 0;
}

#pqfbetdrtz .gt_row {
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

#pqfbetdrtz .gt_stub {
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

#pqfbetdrtz .gt_stub_row_group {
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

#pqfbetdrtz .gt_row_group_first td {
  border-top-width: 2px;
}

#pqfbetdrtz .gt_row_group_first th {
  border-top-width: 2px;
}

#pqfbetdrtz .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#pqfbetdrtz .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#pqfbetdrtz .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#pqfbetdrtz .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#pqfbetdrtz .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#pqfbetdrtz .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#pqfbetdrtz .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#pqfbetdrtz .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#pqfbetdrtz .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#pqfbetdrtz .gt_footnotes {
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

#pqfbetdrtz .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#pqfbetdrtz .gt_sourcenotes {
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

#pqfbetdrtz .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#pqfbetdrtz .gt_left {
  text-align: left;
}

#pqfbetdrtz .gt_center {
  text-align: center;
}

#pqfbetdrtz .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#pqfbetdrtz .gt_font_normal {
  font-weight: normal;
}

#pqfbetdrtz .gt_font_bold {
  font-weight: bold;
}

#pqfbetdrtz .gt_font_italic {
  font-style: italic;
}

#pqfbetdrtz .gt_super {
  font-size: 65%;
}

#pqfbetdrtz .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#pqfbetdrtz .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#pqfbetdrtz .gt_indent_1 {
  text-indent: 5px;
}

#pqfbetdrtz .gt_indent_2 {
  text-indent: 10px;
}

#pqfbetdrtz .gt_indent_3 {
  text-indent: 15px;
}

#pqfbetdrtz .gt_indent_4 {
  text-indent: 20px;
}

#pqfbetdrtz .gt_indent_5 {
  text-indent: 25px;
}

#pqfbetdrtz .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#pqfbetdrtz div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="4" class="gt_heading gt_title gt_font_normal gt_bottom_border">CR[1]: Experiment 100</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)" style="background-color: #90EE90">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)" style="background-color: #90EE90">1</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)" style="background-color: #90EE90">1</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)" style="background-color: #90EE90">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">2</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="background-color: #90EE90">0</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)" style="background-color: #90EE90">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">15</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #90EE90">9</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)" style="background-color: #90EE90">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)" style="background-color: #90EE90">16</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)">15</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)" style="background-color: #90EE90">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)" style="background-color: #90EE90">17</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.42</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.75</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">9.00</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">6.50</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#chmmbhlpbx table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#chmmbhlpbx thead, #chmmbhlpbx tbody, #chmmbhlpbx tfoot, #chmmbhlpbx tr, #chmmbhlpbx td, #chmmbhlpbx th {
  border-style: none;
}

#chmmbhlpbx p {
  margin: 0;
  padding: 0;
}

#chmmbhlpbx .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 22px;
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

#chmmbhlpbx .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#chmmbhlpbx .gt_title {
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

#chmmbhlpbx .gt_subtitle {
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

#chmmbhlpbx .gt_heading {
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

#chmmbhlpbx .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#chmmbhlpbx .gt_col_headings {
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

#chmmbhlpbx .gt_col_heading {
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

#chmmbhlpbx .gt_column_spanner_outer {
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

#chmmbhlpbx .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#chmmbhlpbx .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#chmmbhlpbx .gt_column_spanner {
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

#chmmbhlpbx .gt_spanner_row {
  border-bottom-style: hidden;
}

#chmmbhlpbx .gt_group_heading {
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

#chmmbhlpbx .gt_empty_group_heading {
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

#chmmbhlpbx .gt_from_md > :first-child {
  margin-top: 0;
}

#chmmbhlpbx .gt_from_md > :last-child {
  margin-bottom: 0;
}

#chmmbhlpbx .gt_row {
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

#chmmbhlpbx .gt_stub {
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

#chmmbhlpbx .gt_stub_row_group {
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

#chmmbhlpbx .gt_row_group_first td {
  border-top-width: 2px;
}

#chmmbhlpbx .gt_row_group_first th {
  border-top-width: 2px;
}

#chmmbhlpbx .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#chmmbhlpbx .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#chmmbhlpbx .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#chmmbhlpbx .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#chmmbhlpbx .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#chmmbhlpbx .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#chmmbhlpbx .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#chmmbhlpbx .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#chmmbhlpbx .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#chmmbhlpbx .gt_footnotes {
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

#chmmbhlpbx .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#chmmbhlpbx .gt_sourcenotes {
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

#chmmbhlpbx .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#chmmbhlpbx .gt_left {
  text-align: left;
}

#chmmbhlpbx .gt_center {
  text-align: center;
}

#chmmbhlpbx .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#chmmbhlpbx .gt_font_normal {
  font-weight: normal;
}

#chmmbhlpbx .gt_font_bold {
  font-weight: bold;
}

#chmmbhlpbx .gt_font_italic {
  font-style: italic;
}

#chmmbhlpbx .gt_super {
  font-size: 65%;
}

#chmmbhlpbx .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#chmmbhlpbx .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#chmmbhlpbx .gt_indent_1 {
  text-indent: 5px;
}

#chmmbhlpbx .gt_indent_2 {
  text-indent: 10px;
}

#chmmbhlpbx .gt_indent_3 {
  text-indent: 15px;
}

#chmmbhlpbx .gt_indent_4 {
  text-indent: 20px;
}

#chmmbhlpbx .gt_indent_5 {
  text-indent: 25px;
}

#chmmbhlpbx .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#chmmbhlpbx div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 11.83 | 4.67 | −7.17 |
| 12.00 | 2.67 | −9.33 |
| 8.50 | 7.33 | −1.17 |
| 7.50 | 7.83 | 0.33 |
| 9.67 | 5.67 | −4.00 |

##

<span class="math display">\\$$\\begin{equation} \\begin{aligned} Var(\\widehat{ATE}) &= Var(\\hat{\\bar{Y}}\_1 - \\hat{\\bar{Y}}\_0) \\\\ &= Var(\\hat{\\bar{Y}}\_1) + Var(\\hat{\\bar{Y}}\_0) - 2Cov(\\hat{\\bar{Y}}\_1, \\hat{\\bar{Y}}\_0) \\\\ &= \\frac{n - n\_1}{n - 1} \\frac{\\sigma\_1^2}{n\_1} + \\frac{n - n\_0}{n - 1} \\frac{\\sigma\_0^2}{n\_0} + 2 \\frac{1}{n - 1}Cov(Y\_i(1), Y\_i(0)) \\\\ &= \\frac{1}{n - 1} \\left( \\frac{n\_0 \\sigma\_1^2}{n\_1} + \\frac{n\_1 \\sigma\_0^2}{n\_0} + 2 Cov(Y\_i(1), Y\_i(0)) \\right) \\end{aligned} \\end{equation}\\$$</span>

<span class="math display">\\$$ SE(\\widehat{ATE}) = \\sqrt{ \\frac{1}{n- 1} \\left( \\frac{n\_0 \\sigma\_1^2}{n\_1} + \\frac{n\_1 \\sigma\_0^2}{n\_0} + 2 Cov(Y\_i(1), Y\_i(0)) \\right) } \\$$</span>

##

<span class="math display">\\$$ SE(\\widehat{ATE}) = \\sqrt{ \\frac{1}{n - 1} \\left( \\frac{n\_0 \\sigma\_1^2}{n\_1} + \\frac{n\_1 \\sigma\_0^2}{n\_0} + 2 Cov(Y\_i(1), Y\_i(0)) \\right) } \\$$</span>

How does <span class="math inline">\$SE(\\widehat{ATE})\$</span> relate to the following quantities? What does it suggest about how to plan your design?

1.  The total number of units under study <span class="math inline">\$n\$</span>.
2.  The variance within each set of potential outcomes <span class="math inline">\$\\sigma\_1^2\$</span>, <span class="math inline">\$\\sigma\_0^2\$</span>.
3.  The relative size of the groups <span class="math inline">\$n\_1\$</span> and <span class="math inline">\$n\_0\$</span>.
4.  The covariance in the potential outcomes <span class="math inline">\$Cov(Y\_i(1), Y\_i(0))\$</span>.

<!-- -->

1.  This is the most intuitive and straightforward of the implications: the greater the number of units under study, the smaller the SE.
2.  In general, you want these to be as low as possible. One may is to use a response that is as reliable as possible and has low measurement error. A second way is to select your units to be as uniform as possible in terms of each potential outcome. This is the intuition behind blocking.
3.  If the variances of the potential outcomes are equal, you will minimize the SE by balancing your groups. If you happen to have extra information that suggests one variance is larger than the other, the lowest SE is when more units are allocated to that treatment group.
4.  The lower (including negative!) the Cov between the potential outcomes, the lower the SE. This one is challenging to think of how you would manipulate; it’s really a characteristic of the treatments.

This is a good time to revisit the preliminary statement about the sign change between the Cov of the averages and the Cov of the potential outcomes and ask why there’s that flip. You can also revisit the CR experiments to see the sign flip.

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

##  {data-id="quarto-animate-title"}

Exact SE:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
sigsq_1 <- mean((indo_cr$`Y(1)` - mean(indo_cr$`Y(1)`))^2)
sigsq_0 <- mean((indo_cr$`Y(0)` - mean(indo_cr$`Y(0)`))^2)
cov_01 <- mean((indo_cr$`Y(1)` - mean(indo_cr$`Y(1)`)) *
               (indo_cr$`Y(0)` - mean(indo_cr$`Y(0)`)))
var_ATE <- 1 / (n - 1) * (n_0 / n_1 * sigsq_0 + n_1 / n_0 *
                          sigsq_1 + 2 * cov_01)

se_ATE <- sqrt(var_ATE)
```

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
se_ATE
```

    [1] 3.729151

##  {data-id="quarto-animate-title"}

Exact SE:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
se_ATE
```

    [1] 3.729151

<figure>

</figure>

---

[← Blocking and Variance](01-blocking-and-variance.md) · [Up: contents](index.md) · [Generalized Complete Block Design \$GCB$$1$$\$ →](03-generalized-complete-block-design.md)
