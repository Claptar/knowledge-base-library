---
title: Generalized Complete Block Design \$GCB$$1$$\$
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/20-blocking-and-variance/slides.html
source_file: sources/berkeley-stat158/spring-2026/20-blocking-and-variance/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Generalized Complete Block Design \$GCB$$1$$\$

**Source:** [`20-blocking-and-variance/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/20-blocking-and-variance/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

##

<style>#oectiqqili table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#oectiqqili thead, #oectiqqili tbody, #oectiqqili tfoot, #oectiqqili tr, #oectiqqili td, #oectiqqili th {
  border-style: none;
}

#oectiqqili p {
  margin: 0;
  padding: 0;
}

#oectiqqili .gt_table {
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

#oectiqqili .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#oectiqqili .gt_title {
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

#oectiqqili .gt_subtitle {
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

#oectiqqili .gt_heading {
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

#oectiqqili .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#oectiqqili .gt_col_headings {
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

#oectiqqili .gt_col_heading {
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

#oectiqqili .gt_column_spanner_outer {
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

#oectiqqili .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#oectiqqili .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#oectiqqili .gt_column_spanner {
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

#oectiqqili .gt_spanner_row {
  border-bottom-style: hidden;
}

#oectiqqili .gt_group_heading {
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

#oectiqqili .gt_empty_group_heading {
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

#oectiqqili .gt_from_md > :first-child {
  margin-top: 0;
}

#oectiqqili .gt_from_md > :last-child {
  margin-bottom: 0;
}

#oectiqqili .gt_row {
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

#oectiqqili .gt_stub {
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

#oectiqqili .gt_stub_row_group {
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

#oectiqqili .gt_row_group_first td {
  border-top-width: 2px;
}

#oectiqqili .gt_row_group_first th {
  border-top-width: 2px;
}

#oectiqqili .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#oectiqqili .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#oectiqqili .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#oectiqqili .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#oectiqqili .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#oectiqqili .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#oectiqqili .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#oectiqqili .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#oectiqqili .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#oectiqqili .gt_footnotes {
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

#oectiqqili .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#oectiqqili .gt_sourcenotes {
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

#oectiqqili .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#oectiqqili .gt_left {
  text-align: left;
}

#oectiqqili .gt_center {
  text-align: center;
}

#oectiqqili .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#oectiqqili .gt_font_normal {
  font-weight: normal;
}

#oectiqqili .gt_font_bold {
  font-weight: bold;
}

#oectiqqili .gt_font_italic {
  font-style: italic;
}

#oectiqqili .gt_super {
  font-size: 65%;
}

#oectiqqili .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#oectiqqili .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#oectiqqili .gt_indent_1 {
  text-indent: 5px;
}

#oectiqqili .gt_indent_2 {
  text-indent: 10px;
}

#oectiqqili .gt_indent_3 {
  text-indent: 15px;
}

#oectiqqili .gt_indent_4 {
  text-indent: 20px;
}

#oectiqqili .gt_indent_5 {
  text-indent: 25px;
}

#oectiqqili .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#oectiqqili div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Full Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
</tbody>
</table>

##

<style>#jmepbpjbae table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#jmepbpjbae thead, #jmepbpjbae tbody, #jmepbpjbae tfoot, #jmepbpjbae tr, #jmepbpjbae td, #jmepbpjbae th {
  border-style: none;
}

#jmepbpjbae p {
  margin: 0;
  padding: 0;
}

#jmepbpjbae .gt_table {
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

#jmepbpjbae .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#jmepbpjbae .gt_title {
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

#jmepbpjbae .gt_subtitle {
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

#jmepbpjbae .gt_heading {
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

#jmepbpjbae .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#jmepbpjbae .gt_col_headings {
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

#jmepbpjbae .gt_col_heading {
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

#jmepbpjbae .gt_column_spanner_outer {
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

#jmepbpjbae .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#jmepbpjbae .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#jmepbpjbae .gt_column_spanner {
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

#jmepbpjbae .gt_spanner_row {
  border-bottom-style: hidden;
}

#jmepbpjbae .gt_group_heading {
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

#jmepbpjbae .gt_empty_group_heading {
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

#jmepbpjbae .gt_from_md > :first-child {
  margin-top: 0;
}

#jmepbpjbae .gt_from_md > :last-child {
  margin-bottom: 0;
}

#jmepbpjbae .gt_row {
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

#jmepbpjbae .gt_stub {
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

#jmepbpjbae .gt_stub_row_group {
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

#jmepbpjbae .gt_row_group_first td {
  border-top-width: 2px;
}

#jmepbpjbae .gt_row_group_first th {
  border-top-width: 2px;
}

#jmepbpjbae .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#jmepbpjbae .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#jmepbpjbae .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#jmepbpjbae .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#jmepbpjbae .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#jmepbpjbae .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#jmepbpjbae .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#jmepbpjbae .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#jmepbpjbae .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#jmepbpjbae .gt_footnotes {
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

#jmepbpjbae .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#jmepbpjbae .gt_sourcenotes {
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

#jmepbpjbae .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#jmepbpjbae .gt_left {
  text-align: left;
}

#jmepbpjbae .gt_center {
  text-align: center;
}

#jmepbpjbae .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#jmepbpjbae .gt_font_normal {
  font-weight: normal;
}

#jmepbpjbae .gt_font_bold {
  font-weight: bold;
}

#jmepbpjbae .gt_font_italic {
  font-style: italic;
}

#jmepbpjbae .gt_super {
  font-size: 65%;
}

#jmepbpjbae .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#jmepbpjbae .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#jmepbpjbae .gt_indent_1 {
  text-indent: 5px;
}

#jmepbpjbae .gt_indent_2 {
  text-indent: 10px;
}

#jmepbpjbae .gt_indent_3 {
  text-indent: 15px;
}

#jmepbpjbae .gt_indent_4 {
  text-indent: 20px;
}

#jmepbpjbae .gt_indent_5 {
  text-indent: 25px;
}

#jmepbpjbae .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#jmepbpjbae div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Experiment 1</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)" style="background-color: #EEE9BF">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)" style="background-color: #EEE9BF">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)" style="background-color: #EEE9BF">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)" style="background-color: #EEE9BF">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black; background-color: #EEE9BF">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #5CACEE">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)" style="background-color: #5CACEE">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #5CACEE">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">8.83</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">6.17</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#oytyqazuxh table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#oytyqazuxh thead, #oytyqazuxh tbody, #oytyqazuxh tfoot, #oytyqazuxh tr, #oytyqazuxh td, #oytyqazuxh th {
  border-style: none;
}

#oytyqazuxh p {
  margin: 0;
  padding: 0;
}

#oytyqazuxh .gt_table {
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

#oytyqazuxh .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#oytyqazuxh .gt_title {
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

#oytyqazuxh .gt_subtitle {
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

#oytyqazuxh .gt_heading {
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

#oytyqazuxh .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#oytyqazuxh .gt_col_headings {
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

#oytyqazuxh .gt_col_heading {
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

#oytyqazuxh .gt_column_spanner_outer {
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

#oytyqazuxh .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#oytyqazuxh .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#oytyqazuxh .gt_column_spanner {
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

#oytyqazuxh .gt_spanner_row {
  border-bottom-style: hidden;
}

#oytyqazuxh .gt_group_heading {
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

#oytyqazuxh .gt_empty_group_heading {
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

#oytyqazuxh .gt_from_md > :first-child {
  margin-top: 0;
}

#oytyqazuxh .gt_from_md > :last-child {
  margin-bottom: 0;
}

#oytyqazuxh .gt_row {
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

#oytyqazuxh .gt_stub {
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

#oytyqazuxh .gt_stub_row_group {
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

#oytyqazuxh .gt_row_group_first td {
  border-top-width: 2px;
}

#oytyqazuxh .gt_row_group_first th {
  border-top-width: 2px;
}

#oytyqazuxh .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#oytyqazuxh .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#oytyqazuxh .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#oytyqazuxh .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#oytyqazuxh .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#oytyqazuxh .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#oytyqazuxh .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#oytyqazuxh .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#oytyqazuxh .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#oytyqazuxh .gt_footnotes {
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

#oytyqazuxh .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#oytyqazuxh .gt_sourcenotes {
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

#oytyqazuxh .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#oytyqazuxh .gt_left {
  text-align: left;
}

#oytyqazuxh .gt_center {
  text-align: center;
}

#oytyqazuxh .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#oytyqazuxh .gt_font_normal {
  font-weight: normal;
}

#oytyqazuxh .gt_font_bold {
  font-weight: bold;
}

#oytyqazuxh .gt_font_italic {
  font-style: italic;
}

#oytyqazuxh .gt_super {
  font-size: 65%;
}

#oytyqazuxh .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#oytyqazuxh .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#oytyqazuxh .gt_indent_1 {
  text-indent: 5px;
}

#oytyqazuxh .gt_indent_2 {
  text-indent: 10px;
}

#oytyqazuxh .gt_indent_3 {
  text-indent: 15px;
}

#oytyqazuxh .gt_indent_4 {
  text-indent: 20px;
}

#oytyqazuxh .gt_indent_5 {
  text-indent: 25px;
}

#oytyqazuxh .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#oytyqazuxh div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 8.83 | 6.17 | −2.67 |

##

<style>#drkayfmpqa table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#drkayfmpqa thead, #drkayfmpqa tbody, #drkayfmpqa tfoot, #drkayfmpqa tr, #drkayfmpqa td, #drkayfmpqa th {
  border-style: none;
}

#drkayfmpqa p {
  margin: 0;
  padding: 0;
}

#drkayfmpqa .gt_table {
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

#drkayfmpqa .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#drkayfmpqa .gt_title {
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

#drkayfmpqa .gt_subtitle {
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

#drkayfmpqa .gt_heading {
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

#drkayfmpqa .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#drkayfmpqa .gt_col_headings {
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

#drkayfmpqa .gt_col_heading {
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

#drkayfmpqa .gt_column_spanner_outer {
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

#drkayfmpqa .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#drkayfmpqa .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#drkayfmpqa .gt_column_spanner {
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

#drkayfmpqa .gt_spanner_row {
  border-bottom-style: hidden;
}

#drkayfmpqa .gt_group_heading {
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

#drkayfmpqa .gt_empty_group_heading {
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

#drkayfmpqa .gt_from_md > :first-child {
  margin-top: 0;
}

#drkayfmpqa .gt_from_md > :last-child {
  margin-bottom: 0;
}

#drkayfmpqa .gt_row {
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

#drkayfmpqa .gt_stub {
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

#drkayfmpqa .gt_stub_row_group {
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

#drkayfmpqa .gt_row_group_first td {
  border-top-width: 2px;
}

#drkayfmpqa .gt_row_group_first th {
  border-top-width: 2px;
}

#drkayfmpqa .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#drkayfmpqa .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#drkayfmpqa .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#drkayfmpqa .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#drkayfmpqa .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#drkayfmpqa .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#drkayfmpqa .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#drkayfmpqa .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#drkayfmpqa .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#drkayfmpqa .gt_footnotes {
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

#drkayfmpqa .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#drkayfmpqa .gt_sourcenotes {
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

#drkayfmpqa .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#drkayfmpqa .gt_left {
  text-align: left;
}

#drkayfmpqa .gt_center {
  text-align: center;
}

#drkayfmpqa .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#drkayfmpqa .gt_font_normal {
  font-weight: normal;
}

#drkayfmpqa .gt_font_bold {
  font-weight: bold;
}

#drkayfmpqa .gt_font_italic {
  font-style: italic;
}

#drkayfmpqa .gt_super {
  font-size: 65%;
}

#drkayfmpqa .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#drkayfmpqa .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#drkayfmpqa .gt_indent_1 {
  text-indent: 5px;
}

#drkayfmpqa .gt_indent_2 {
  text-indent: 10px;
}

#drkayfmpqa .gt_indent_3 {
  text-indent: 15px;
}

#drkayfmpqa .gt_indent_4 {
  text-indent: 20px;
}

#drkayfmpqa .gt_indent_5 {
  text-indent: 25px;
}

#drkayfmpqa .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#drkayfmpqa div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Experiment 2</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)" style="background-color: #EEE9BF">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #EEE9BF">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black; background-color: #EEE9BF">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #5CACEE">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)" style="background-color: #5CACEE">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #5CACEE">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">9.83</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">4.83</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#qumffiuwdr table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#qumffiuwdr thead, #qumffiuwdr tbody, #qumffiuwdr tfoot, #qumffiuwdr tr, #qumffiuwdr td, #qumffiuwdr th {
  border-style: none;
}

#qumffiuwdr p {
  margin: 0;
  padding: 0;
}

#qumffiuwdr .gt_table {
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

#qumffiuwdr .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#qumffiuwdr .gt_title {
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

#qumffiuwdr .gt_subtitle {
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

#qumffiuwdr .gt_heading {
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

#qumffiuwdr .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#qumffiuwdr .gt_col_headings {
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

#qumffiuwdr .gt_col_heading {
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

#qumffiuwdr .gt_column_spanner_outer {
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

#qumffiuwdr .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#qumffiuwdr .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#qumffiuwdr .gt_column_spanner {
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

#qumffiuwdr .gt_spanner_row {
  border-bottom-style: hidden;
}

#qumffiuwdr .gt_group_heading {
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

#qumffiuwdr .gt_empty_group_heading {
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

#qumffiuwdr .gt_from_md > :first-child {
  margin-top: 0;
}

#qumffiuwdr .gt_from_md > :last-child {
  margin-bottom: 0;
}

#qumffiuwdr .gt_row {
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

#qumffiuwdr .gt_stub {
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

#qumffiuwdr .gt_stub_row_group {
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

#qumffiuwdr .gt_row_group_first td {
  border-top-width: 2px;
}

#qumffiuwdr .gt_row_group_first th {
  border-top-width: 2px;
}

#qumffiuwdr .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#qumffiuwdr .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#qumffiuwdr .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#qumffiuwdr .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#qumffiuwdr .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#qumffiuwdr .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#qumffiuwdr .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#qumffiuwdr .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#qumffiuwdr .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#qumffiuwdr .gt_footnotes {
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

#qumffiuwdr .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#qumffiuwdr .gt_sourcenotes {
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

#qumffiuwdr .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#qumffiuwdr .gt_left {
  text-align: left;
}

#qumffiuwdr .gt_center {
  text-align: center;
}

#qumffiuwdr .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#qumffiuwdr .gt_font_normal {
  font-weight: normal;
}

#qumffiuwdr .gt_font_bold {
  font-weight: bold;
}

#qumffiuwdr .gt_font_italic {
  font-style: italic;
}

#qumffiuwdr .gt_super {
  font-size: 65%;
}

#qumffiuwdr .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#qumffiuwdr .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#qumffiuwdr .gt_indent_1 {
  text-indent: 5px;
}

#qumffiuwdr .gt_indent_2 {
  text-indent: 10px;
}

#qumffiuwdr .gt_indent_3 {
  text-indent: 15px;
}

#qumffiuwdr .gt_indent_4 {
  text-indent: 20px;
}

#qumffiuwdr .gt_indent_5 {
  text-indent: 25px;
}

#qumffiuwdr .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#qumffiuwdr div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 8.83 | 6.17 | −2.67 |
| 9.83 | 4.83 | −5.00 |

##

<style>#iqgrqoxvkz table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#iqgrqoxvkz thead, #iqgrqoxvkz tbody, #iqgrqoxvkz tfoot, #iqgrqoxvkz tr, #iqgrqoxvkz td, #iqgrqoxvkz th {
  border-style: none;
}

#iqgrqoxvkz p {
  margin: 0;
  padding: 0;
}

#iqgrqoxvkz .gt_table {
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

#iqgrqoxvkz .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#iqgrqoxvkz .gt_title {
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

#iqgrqoxvkz .gt_subtitle {
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

#iqgrqoxvkz .gt_heading {
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

#iqgrqoxvkz .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#iqgrqoxvkz .gt_col_headings {
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

#iqgrqoxvkz .gt_col_heading {
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

#iqgrqoxvkz .gt_column_spanner_outer {
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

#iqgrqoxvkz .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#iqgrqoxvkz .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#iqgrqoxvkz .gt_column_spanner {
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

#iqgrqoxvkz .gt_spanner_row {
  border-bottom-style: hidden;
}

#iqgrqoxvkz .gt_group_heading {
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

#iqgrqoxvkz .gt_empty_group_heading {
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

#iqgrqoxvkz .gt_from_md > :first-child {
  margin-top: 0;
}

#iqgrqoxvkz .gt_from_md > :last-child {
  margin-bottom: 0;
}

#iqgrqoxvkz .gt_row {
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

#iqgrqoxvkz .gt_stub {
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

#iqgrqoxvkz .gt_stub_row_group {
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

#iqgrqoxvkz .gt_row_group_first td {
  border-top-width: 2px;
}

#iqgrqoxvkz .gt_row_group_first th {
  border-top-width: 2px;
}

#iqgrqoxvkz .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#iqgrqoxvkz .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#iqgrqoxvkz .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#iqgrqoxvkz .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#iqgrqoxvkz .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#iqgrqoxvkz .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#iqgrqoxvkz .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#iqgrqoxvkz .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#iqgrqoxvkz .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#iqgrqoxvkz .gt_footnotes {
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

#iqgrqoxvkz .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#iqgrqoxvkz .gt_sourcenotes {
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

#iqgrqoxvkz .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#iqgrqoxvkz .gt_left {
  text-align: left;
}

#iqgrqoxvkz .gt_center {
  text-align: center;
}

#iqgrqoxvkz .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#iqgrqoxvkz .gt_font_normal {
  font-weight: normal;
}

#iqgrqoxvkz .gt_font_bold {
  font-weight: bold;
}

#iqgrqoxvkz .gt_font_italic {
  font-style: italic;
}

#iqgrqoxvkz .gt_super {
  font-size: 65%;
}

#iqgrqoxvkz .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#iqgrqoxvkz .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#iqgrqoxvkz .gt_indent_1 {
  text-indent: 5px;
}

#iqgrqoxvkz .gt_indent_2 {
  text-indent: 10px;
}

#iqgrqoxvkz .gt_indent_3 {
  text-indent: 15px;
}

#iqgrqoxvkz .gt_indent_4 {
  text-indent: 20px;
}

#iqgrqoxvkz .gt_indent_5 {
  text-indent: 25px;
}

#iqgrqoxvkz .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#iqgrqoxvkz div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Experiment 3</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)" style="background-color: #EEE9BF">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)" style="background-color: #EEE9BF">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #EEE9BF">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black; background-color: #EEE9BF">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #5CACEE">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)" style="background-color: #5CACEE">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)" style="background-color: #5CACEE">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">8.83</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">5.00</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#vukfpiktbd table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#vukfpiktbd thead, #vukfpiktbd tbody, #vukfpiktbd tfoot, #vukfpiktbd tr, #vukfpiktbd td, #vukfpiktbd th {
  border-style: none;
}

#vukfpiktbd p {
  margin: 0;
  padding: 0;
}

#vukfpiktbd .gt_table {
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

#vukfpiktbd .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#vukfpiktbd .gt_title {
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

#vukfpiktbd .gt_subtitle {
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

#vukfpiktbd .gt_heading {
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

#vukfpiktbd .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vukfpiktbd .gt_col_headings {
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

#vukfpiktbd .gt_col_heading {
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

#vukfpiktbd .gt_column_spanner_outer {
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

#vukfpiktbd .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#vukfpiktbd .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#vukfpiktbd .gt_column_spanner {
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

#vukfpiktbd .gt_spanner_row {
  border-bottom-style: hidden;
}

#vukfpiktbd .gt_group_heading {
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

#vukfpiktbd .gt_empty_group_heading {
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

#vukfpiktbd .gt_from_md > :first-child {
  margin-top: 0;
}

#vukfpiktbd .gt_from_md > :last-child {
  margin-bottom: 0;
}

#vukfpiktbd .gt_row {
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

#vukfpiktbd .gt_stub {
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

#vukfpiktbd .gt_stub_row_group {
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

#vukfpiktbd .gt_row_group_first td {
  border-top-width: 2px;
}

#vukfpiktbd .gt_row_group_first th {
  border-top-width: 2px;
}

#vukfpiktbd .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#vukfpiktbd .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#vukfpiktbd .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#vukfpiktbd .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vukfpiktbd .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#vukfpiktbd .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#vukfpiktbd .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#vukfpiktbd .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#vukfpiktbd .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#vukfpiktbd .gt_footnotes {
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

#vukfpiktbd .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#vukfpiktbd .gt_sourcenotes {
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

#vukfpiktbd .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#vukfpiktbd .gt_left {
  text-align: left;
}

#vukfpiktbd .gt_center {
  text-align: center;
}

#vukfpiktbd .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#vukfpiktbd .gt_font_normal {
  font-weight: normal;
}

#vukfpiktbd .gt_font_bold {
  font-weight: bold;
}

#vukfpiktbd .gt_font_italic {
  font-style: italic;
}

#vukfpiktbd .gt_super {
  font-size: 65%;
}

#vukfpiktbd .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#vukfpiktbd .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#vukfpiktbd .gt_indent_1 {
  text-indent: 5px;
}

#vukfpiktbd .gt_indent_2 {
  text-indent: 10px;
}

#vukfpiktbd .gt_indent_3 {
  text-indent: 15px;
}

#vukfpiktbd .gt_indent_4 {
  text-indent: 20px;
}

#vukfpiktbd .gt_indent_5 {
  text-indent: 25px;
}

#vukfpiktbd .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#vukfpiktbd div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 8.83 | 6.17 | −2.67 |
| 9.83 | 4.83 | −5.00 |
| 8.83 | 5.00 | −3.83 |

##

<style>#xcihyxfkcz table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#xcihyxfkcz thead, #xcihyxfkcz tbody, #xcihyxfkcz tfoot, #xcihyxfkcz tr, #xcihyxfkcz td, #xcihyxfkcz th {
  border-style: none;
}

#xcihyxfkcz p {
  margin: 0;
  padding: 0;
}

#xcihyxfkcz .gt_table {
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

#xcihyxfkcz .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#xcihyxfkcz .gt_title {
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

#xcihyxfkcz .gt_subtitle {
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

#xcihyxfkcz .gt_heading {
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

#xcihyxfkcz .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#xcihyxfkcz .gt_col_headings {
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

#xcihyxfkcz .gt_col_heading {
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

#xcihyxfkcz .gt_column_spanner_outer {
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

#xcihyxfkcz .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#xcihyxfkcz .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#xcihyxfkcz .gt_column_spanner {
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

#xcihyxfkcz .gt_spanner_row {
  border-bottom-style: hidden;
}

#xcihyxfkcz .gt_group_heading {
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

#xcihyxfkcz .gt_empty_group_heading {
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

#xcihyxfkcz .gt_from_md > :first-child {
  margin-top: 0;
}

#xcihyxfkcz .gt_from_md > :last-child {
  margin-bottom: 0;
}

#xcihyxfkcz .gt_row {
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

#xcihyxfkcz .gt_stub {
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

#xcihyxfkcz .gt_stub_row_group {
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

#xcihyxfkcz .gt_row_group_first td {
  border-top-width: 2px;
}

#xcihyxfkcz .gt_row_group_first th {
  border-top-width: 2px;
}

#xcihyxfkcz .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#xcihyxfkcz .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#xcihyxfkcz .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#xcihyxfkcz .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#xcihyxfkcz .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#xcihyxfkcz .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#xcihyxfkcz .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#xcihyxfkcz .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#xcihyxfkcz .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#xcihyxfkcz .gt_footnotes {
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

#xcihyxfkcz .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#xcihyxfkcz .gt_sourcenotes {
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

#xcihyxfkcz .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#xcihyxfkcz .gt_left {
  text-align: left;
}

#xcihyxfkcz .gt_center {
  text-align: center;
}

#xcihyxfkcz .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#xcihyxfkcz .gt_font_normal {
  font-weight: normal;
}

#xcihyxfkcz .gt_font_bold {
  font-weight: bold;
}

#xcihyxfkcz .gt_font_italic {
  font-style: italic;
}

#xcihyxfkcz .gt_super {
  font-size: 65%;
}

#xcihyxfkcz .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#xcihyxfkcz .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#xcihyxfkcz .gt_indent_1 {
  text-indent: 5px;
}

#xcihyxfkcz .gt_indent_2 {
  text-indent: 10px;
}

#xcihyxfkcz .gt_indent_3 {
  text-indent: 15px;
}

#xcihyxfkcz .gt_indent_4 {
  text-indent: 20px;
}

#xcihyxfkcz .gt_indent_5 {
  text-indent: 25px;
}

#xcihyxfkcz .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#xcihyxfkcz div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Experiment 4</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)" style="background-color: #EEE9BF">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #EEE9BF">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black; background-color: #EEE9BF">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #5CACEE">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)" style="background-color: #5CACEE">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)" style="background-color: #5CACEE">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">9.83</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">3.67</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#loumgvrhdl table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#loumgvrhdl thead, #loumgvrhdl tbody, #loumgvrhdl tfoot, #loumgvrhdl tr, #loumgvrhdl td, #loumgvrhdl th {
  border-style: none;
}

#loumgvrhdl p {
  margin: 0;
  padding: 0;
}

#loumgvrhdl .gt_table {
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

#loumgvrhdl .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#loumgvrhdl .gt_title {
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

#loumgvrhdl .gt_subtitle {
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

#loumgvrhdl .gt_heading {
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

#loumgvrhdl .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#loumgvrhdl .gt_col_headings {
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

#loumgvrhdl .gt_col_heading {
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

#loumgvrhdl .gt_column_spanner_outer {
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

#loumgvrhdl .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#loumgvrhdl .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#loumgvrhdl .gt_column_spanner {
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

#loumgvrhdl .gt_spanner_row {
  border-bottom-style: hidden;
}

#loumgvrhdl .gt_group_heading {
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

#loumgvrhdl .gt_empty_group_heading {
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

#loumgvrhdl .gt_from_md > :first-child {
  margin-top: 0;
}

#loumgvrhdl .gt_from_md > :last-child {
  margin-bottom: 0;
}

#loumgvrhdl .gt_row {
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

#loumgvrhdl .gt_stub {
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

#loumgvrhdl .gt_stub_row_group {
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

#loumgvrhdl .gt_row_group_first td {
  border-top-width: 2px;
}

#loumgvrhdl .gt_row_group_first th {
  border-top-width: 2px;
}

#loumgvrhdl .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#loumgvrhdl .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#loumgvrhdl .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#loumgvrhdl .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#loumgvrhdl .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#loumgvrhdl .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#loumgvrhdl .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#loumgvrhdl .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#loumgvrhdl .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#loumgvrhdl .gt_footnotes {
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

#loumgvrhdl .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#loumgvrhdl .gt_sourcenotes {
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

#loumgvrhdl .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#loumgvrhdl .gt_left {
  text-align: left;
}

#loumgvrhdl .gt_center {
  text-align: center;
}

#loumgvrhdl .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#loumgvrhdl .gt_font_normal {
  font-weight: normal;
}

#loumgvrhdl .gt_font_bold {
  font-weight: bold;
}

#loumgvrhdl .gt_font_italic {
  font-style: italic;
}

#loumgvrhdl .gt_super {
  font-size: 65%;
}

#loumgvrhdl .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#loumgvrhdl .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#loumgvrhdl .gt_indent_1 {
  text-indent: 5px;
}

#loumgvrhdl .gt_indent_2 {
  text-indent: 10px;
}

#loumgvrhdl .gt_indent_3 {
  text-indent: 15px;
}

#loumgvrhdl .gt_indent_4 {
  text-indent: 20px;
}

#loumgvrhdl .gt_indent_5 {
  text-indent: 25px;
}

#loumgvrhdl .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#loumgvrhdl div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 8.83 | 6.17 | −2.67 |
| 9.83 | 4.83 | −5.00 |
| 8.83 | 5.00 | −3.83 |
| 9.83 | 3.67 | −6.17 |

##

<style>#ierxtfmapm table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ierxtfmapm thead, #ierxtfmapm tbody, #ierxtfmapm tfoot, #ierxtfmapm tr, #ierxtfmapm td, #ierxtfmapm th {
  border-style: none;
}

#ierxtfmapm p {
  margin: 0;
  padding: 0;
}

#ierxtfmapm .gt_table {
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

#ierxtfmapm .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ierxtfmapm .gt_title {
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

#ierxtfmapm .gt_subtitle {
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

#ierxtfmapm .gt_heading {
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

#ierxtfmapm .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ierxtfmapm .gt_col_headings {
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

#ierxtfmapm .gt_col_heading {
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

#ierxtfmapm .gt_column_spanner_outer {
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

#ierxtfmapm .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ierxtfmapm .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ierxtfmapm .gt_column_spanner {
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

#ierxtfmapm .gt_spanner_row {
  border-bottom-style: hidden;
}

#ierxtfmapm .gt_group_heading {
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

#ierxtfmapm .gt_empty_group_heading {
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

#ierxtfmapm .gt_from_md > :first-child {
  margin-top: 0;
}

#ierxtfmapm .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ierxtfmapm .gt_row {
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

#ierxtfmapm .gt_stub {
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

#ierxtfmapm .gt_stub_row_group {
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

#ierxtfmapm .gt_row_group_first td {
  border-top-width: 2px;
}

#ierxtfmapm .gt_row_group_first th {
  border-top-width: 2px;
}

#ierxtfmapm .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ierxtfmapm .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ierxtfmapm .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ierxtfmapm .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ierxtfmapm .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ierxtfmapm .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ierxtfmapm .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ierxtfmapm .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ierxtfmapm .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ierxtfmapm .gt_footnotes {
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

#ierxtfmapm .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ierxtfmapm .gt_sourcenotes {
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

#ierxtfmapm .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ierxtfmapm .gt_left {
  text-align: left;
}

#ierxtfmapm .gt_center {
  text-align: center;
}

#ierxtfmapm .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ierxtfmapm .gt_font_normal {
  font-weight: normal;
}

#ierxtfmapm .gt_font_bold {
  font-weight: bold;
}

#ierxtfmapm .gt_font_italic {
  font-style: italic;
}

#ierxtfmapm .gt_super {
  font-size: 65%;
}

#ierxtfmapm .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ierxtfmapm .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ierxtfmapm .gt_indent_1 {
  text-indent: 5px;
}

#ierxtfmapm .gt_indent_2 {
  text-indent: 10px;
}

#ierxtfmapm .gt_indent_3 {
  text-indent: 15px;
}

#ierxtfmapm .gt_indent_4 {
  text-indent: 20px;
}

#ierxtfmapm .gt_indent_5 {
  text-indent: 25px;
}

#ierxtfmapm .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ierxtfmapm div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Experiment 5</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)" style="background-color: #EEE9BF">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #EEE9BF">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black; background-color: #EEE9BF">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)" style="background-color: #5CACEE">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)" style="background-color: #5CACEE">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)" style="background-color: #5CACEE">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #5CACEE">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">9.83</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">4.83</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#ceeuferzei table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ceeuferzei thead, #ceeuferzei tbody, #ceeuferzei tfoot, #ceeuferzei tr, #ceeuferzei td, #ceeuferzei th {
  border-style: none;
}

#ceeuferzei p {
  margin: 0;
  padding: 0;
}

#ceeuferzei .gt_table {
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

#ceeuferzei .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ceeuferzei .gt_title {
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

#ceeuferzei .gt_subtitle {
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

#ceeuferzei .gt_heading {
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

#ceeuferzei .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ceeuferzei .gt_col_headings {
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

#ceeuferzei .gt_col_heading {
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

#ceeuferzei .gt_column_spanner_outer {
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

#ceeuferzei .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ceeuferzei .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ceeuferzei .gt_column_spanner {
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

#ceeuferzei .gt_spanner_row {
  border-bottom-style: hidden;
}

#ceeuferzei .gt_group_heading {
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

#ceeuferzei .gt_empty_group_heading {
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

#ceeuferzei .gt_from_md > :first-child {
  margin-top: 0;
}

#ceeuferzei .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ceeuferzei .gt_row {
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

#ceeuferzei .gt_stub {
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

#ceeuferzei .gt_stub_row_group {
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

#ceeuferzei .gt_row_group_first td {
  border-top-width: 2px;
}

#ceeuferzei .gt_row_group_first th {
  border-top-width: 2px;
}

#ceeuferzei .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ceeuferzei .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ceeuferzei .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ceeuferzei .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ceeuferzei .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ceeuferzei .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ceeuferzei .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ceeuferzei .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ceeuferzei .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ceeuferzei .gt_footnotes {
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

#ceeuferzei .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ceeuferzei .gt_sourcenotes {
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

#ceeuferzei .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ceeuferzei .gt_left {
  text-align: left;
}

#ceeuferzei .gt_center {
  text-align: center;
}

#ceeuferzei .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ceeuferzei .gt_font_normal {
  font-weight: normal;
}

#ceeuferzei .gt_font_bold {
  font-weight: bold;
}

#ceeuferzei .gt_font_italic {
  font-style: italic;
}

#ceeuferzei .gt_super {
  font-size: 65%;
}

#ceeuferzei .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ceeuferzei .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ceeuferzei .gt_indent_1 {
  text-indent: 5px;
}

#ceeuferzei .gt_indent_2 {
  text-indent: 10px;
}

#ceeuferzei .gt_indent_3 {
  text-indent: 15px;
}

#ceeuferzei .gt_indent_4 {
  text-indent: 20px;
}

#ceeuferzei .gt_indent_5 {
  text-indent: 25px;
}

#ceeuferzei .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ceeuferzei div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 8.83 | 6.17 | −2.67 |
| 9.83 | 4.83 | −5.00 |
| 8.83 | 5.00 | −3.83 |
| 9.83 | 3.67 | −6.17 |
| 9.83 | 4.83 | −5.00 |

##

<style>#xanigenvce table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#xanigenvce thead, #xanigenvce tbody, #xanigenvce tfoot, #xanigenvce tr, #xanigenvce td, #xanigenvce th {
  border-style: none;
}

#xanigenvce p {
  margin: 0;
  padding: 0;
}

#xanigenvce .gt_table {
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

#xanigenvce .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#xanigenvce .gt_title {
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

#xanigenvce .gt_subtitle {
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

#xanigenvce .gt_heading {
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

#xanigenvce .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#xanigenvce .gt_col_headings {
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

#xanigenvce .gt_col_heading {
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

#xanigenvce .gt_column_spanner_outer {
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

#xanigenvce .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#xanigenvce .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#xanigenvce .gt_column_spanner {
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

#xanigenvce .gt_spanner_row {
  border-bottom-style: hidden;
}

#xanigenvce .gt_group_heading {
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

#xanigenvce .gt_empty_group_heading {
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

#xanigenvce .gt_from_md > :first-child {
  margin-top: 0;
}

#xanigenvce .gt_from_md > :last-child {
  margin-bottom: 0;
}

#xanigenvce .gt_row {
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

#xanigenvce .gt_stub {
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

#xanigenvce .gt_stub_row_group {
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

#xanigenvce .gt_row_group_first td {
  border-top-width: 2px;
}

#xanigenvce .gt_row_group_first th {
  border-top-width: 2px;
}

#xanigenvce .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#xanigenvce .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#xanigenvce .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#xanigenvce .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#xanigenvce .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#xanigenvce .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#xanigenvce .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#xanigenvce .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#xanigenvce .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#xanigenvce .gt_footnotes {
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

#xanigenvce .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#xanigenvce .gt_sourcenotes {
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

#xanigenvce .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#xanigenvce .gt_left {
  text-align: left;
}

#xanigenvce .gt_center {
  text-align: center;
}

#xanigenvce .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#xanigenvce .gt_font_normal {
  font-weight: normal;
}

#xanigenvce .gt_font_bold {
  font-weight: bold;
}

#xanigenvce .gt_font_italic {
  font-style: italic;
}

#xanigenvce .gt_super {
  font-size: 65%;
}

#xanigenvce .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#xanigenvce .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#xanigenvce .gt_indent_1 {
  text-indent: 5px;
}

#xanigenvce .gt_indent_2 {
  text-indent: 10px;
}

#xanigenvce .gt_indent_3 {
  text-indent: 15px;
}

#xanigenvce .gt_indent_4 {
  text-indent: 20px;
}

#xanigenvce .gt_indent_5 {
  text-indent: 25px;
}

#xanigenvce .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#xanigenvce div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Experiment 100</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)" style="background-color: #EEE9BF">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #EEE9BF">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black; background-color: #EEE9BF">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)" style="background-color: #5CACEE">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)" style="background-color: #5CACEE">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)" style="background-color: #5CACEE">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #5CACEE">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">10.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">4.33</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#kxvjlgsaxk table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#kxvjlgsaxk thead, #kxvjlgsaxk tbody, #kxvjlgsaxk tfoot, #kxvjlgsaxk tr, #kxvjlgsaxk td, #kxvjlgsaxk th {
  border-style: none;
}

#kxvjlgsaxk p {
  margin: 0;
  padding: 0;
}

#kxvjlgsaxk .gt_table {
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

#kxvjlgsaxk .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#kxvjlgsaxk .gt_title {
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

#kxvjlgsaxk .gt_subtitle {
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

#kxvjlgsaxk .gt_heading {
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

#kxvjlgsaxk .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#kxvjlgsaxk .gt_col_headings {
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

#kxvjlgsaxk .gt_col_heading {
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

#kxvjlgsaxk .gt_column_spanner_outer {
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

#kxvjlgsaxk .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#kxvjlgsaxk .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#kxvjlgsaxk .gt_column_spanner {
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

#kxvjlgsaxk .gt_spanner_row {
  border-bottom-style: hidden;
}

#kxvjlgsaxk .gt_group_heading {
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

#kxvjlgsaxk .gt_empty_group_heading {
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

#kxvjlgsaxk .gt_from_md > :first-child {
  margin-top: 0;
}

#kxvjlgsaxk .gt_from_md > :last-child {
  margin-bottom: 0;
}

#kxvjlgsaxk .gt_row {
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

#kxvjlgsaxk .gt_stub {
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

#kxvjlgsaxk .gt_stub_row_group {
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

#kxvjlgsaxk .gt_row_group_first td {
  border-top-width: 2px;
}

#kxvjlgsaxk .gt_row_group_first th {
  border-top-width: 2px;
}

#kxvjlgsaxk .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#kxvjlgsaxk .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#kxvjlgsaxk .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#kxvjlgsaxk .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#kxvjlgsaxk .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#kxvjlgsaxk .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#kxvjlgsaxk .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#kxvjlgsaxk .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#kxvjlgsaxk .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#kxvjlgsaxk .gt_footnotes {
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

#kxvjlgsaxk .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#kxvjlgsaxk .gt_sourcenotes {
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

#kxvjlgsaxk .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#kxvjlgsaxk .gt_left {
  text-align: left;
}

#kxvjlgsaxk .gt_center {
  text-align: center;
}

#kxvjlgsaxk .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#kxvjlgsaxk .gt_font_normal {
  font-weight: normal;
}

#kxvjlgsaxk .gt_font_bold {
  font-weight: bold;
}

#kxvjlgsaxk .gt_font_italic {
  font-style: italic;
}

#kxvjlgsaxk .gt_super {
  font-size: 65%;
}

#kxvjlgsaxk .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#kxvjlgsaxk .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#kxvjlgsaxk .gt_indent_1 {
  text-indent: 5px;
}

#kxvjlgsaxk .gt_indent_2 {
  text-indent: 10px;
}

#kxvjlgsaxk .gt_indent_3 {
  text-indent: 15px;
}

#kxvjlgsaxk .gt_indent_4 {
  text-indent: 20px;
}

#kxvjlgsaxk .gt_indent_5 {
  text-indent: 25px;
}

#kxvjlgsaxk .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#kxvjlgsaxk div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 8.83 | 6.17 | −2.67 |
| 9.83 | 4.83 | −5.00 |
| 8.83 | 5.00 | −3.83 |
| 9.83 | 3.67 | −6.17 |
| 9.83 | 4.83 | −5.00 |

##

<style>#rxdtcldjsh table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#rxdtcldjsh thead, #rxdtcldjsh tbody, #rxdtcldjsh tfoot, #rxdtcldjsh tr, #rxdtcldjsh td, #rxdtcldjsh th {
  border-style: none;
}

#rxdtcldjsh p {
  margin: 0;
  padding: 0;
}

#rxdtcldjsh .gt_table {
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

#rxdtcldjsh .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#rxdtcldjsh .gt_title {
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

#rxdtcldjsh .gt_subtitle {
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

#rxdtcldjsh .gt_heading {
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

#rxdtcldjsh .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rxdtcldjsh .gt_col_headings {
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

#rxdtcldjsh .gt_col_heading {
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

#rxdtcldjsh .gt_column_spanner_outer {
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

#rxdtcldjsh .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#rxdtcldjsh .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#rxdtcldjsh .gt_column_spanner {
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

#rxdtcldjsh .gt_spanner_row {
  border-bottom-style: hidden;
}

#rxdtcldjsh .gt_group_heading {
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

#rxdtcldjsh .gt_empty_group_heading {
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

#rxdtcldjsh .gt_from_md > :first-child {
  margin-top: 0;
}

#rxdtcldjsh .gt_from_md > :last-child {
  margin-bottom: 0;
}

#rxdtcldjsh .gt_row {
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

#rxdtcldjsh .gt_stub {
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

#rxdtcldjsh .gt_stub_row_group {
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

#rxdtcldjsh .gt_row_group_first td {
  border-top-width: 2px;
}

#rxdtcldjsh .gt_row_group_first th {
  border-top-width: 2px;
}

#rxdtcldjsh .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#rxdtcldjsh .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#rxdtcldjsh .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#rxdtcldjsh .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rxdtcldjsh .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#rxdtcldjsh .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#rxdtcldjsh .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#rxdtcldjsh .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#rxdtcldjsh .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rxdtcldjsh .gt_footnotes {
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

#rxdtcldjsh .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#rxdtcldjsh .gt_sourcenotes {
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

#rxdtcldjsh .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#rxdtcldjsh .gt_left {
  text-align: left;
}

#rxdtcldjsh .gt_center {
  text-align: center;
}

#rxdtcldjsh .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#rxdtcldjsh .gt_font_normal {
  font-weight: normal;
}

#rxdtcldjsh .gt_font_bold {
  font-weight: bold;
}

#rxdtcldjsh .gt_font_italic {
  font-style: italic;
}

#rxdtcldjsh .gt_super {
  font-size: 65%;
}

#rxdtcldjsh .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#rxdtcldjsh .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#rxdtcldjsh .gt_indent_1 {
  text-indent: 5px;
}

#rxdtcldjsh .gt_indent_2 {
  text-indent: 10px;
}

#rxdtcldjsh .gt_indent_3 {
  text-indent: 15px;
}

#rxdtcldjsh .gt_indent_4 {
  text-indent: 20px;
}

#rxdtcldjsh .gt_indent_5 {
  text-indent: 25px;
}

#rxdtcldjsh .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#rxdtcldjsh div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="5" class="gt_heading gt_title gt_font_normal gt_bottom_border">GCB[1]: Experiment 100</th>
</tr>
<tr class="gt_col_headings even">
<th id="a::stub" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="Project" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Project</th>
<th id="Region" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Region</th>
<th id="Y(0)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(0)</th>
<th id="Y(1)" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Y(1)</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<th id="stub_1_1" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_1 Project">1</td>
<td class="gt_row gt_center" headers="stub_1_1 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_1 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="even">
<th id="stub_1_2" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_2 Project">2</td>
<td class="gt_row gt_center" headers="stub_1_2 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(0)">0</td>
<td class="gt_row gt_center" headers="stub_1_2 Y(1)" style="background-color: #EEE9BF">0</td>
</tr>
<tr class="odd">
<th id="stub_1_3" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_3 Project">3</td>
<td class="gt_row gt_center" headers="stub_1_3 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(0)">2</td>
<td class="gt_row gt_center" headers="stub_1_3 Y(1)" style="background-color: #EEE9BF">4</td>
</tr>
<tr class="even">
<th id="stub_1_4" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_4 Project">4</td>
<td class="gt_row gt_center" headers="stub_1_4 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(0)" style="background-color: #EEE9BF">2</td>
<td class="gt_row gt_center" headers="stub_1_4 Y(1)">4</td>
</tr>
<tr class="odd">
<th id="stub_1_5" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_5 Project">5</td>
<td class="gt_row gt_center" headers="stub_1_5 Region">A</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(0)" style="background-color: #EEE9BF">4</td>
<td class="gt_row gt_center" headers="stub_1_5 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_6" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_6 Project" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Region" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">A</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(0)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black; background-color: #EEE9BF">6</td>
<td class="gt_row gt_center" headers="stub_1_6 Y(1)" style="border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: black">8</td>
</tr>
<tr class="odd">
<th id="stub_1_7" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_7 Project">7</td>
<td class="gt_row gt_center" headers="stub_1_7 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(0)">14</td>
<td class="gt_row gt_center" headers="stub_1_7 Y(1)" style="background-color: #5CACEE">12</td>
</tr>
<tr class="even">
<th id="stub_1_8" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_8 Project">8</td>
<td class="gt_row gt_center" headers="stub_1_8 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(0)" style="background-color: #5CACEE">16</td>
<td class="gt_row gt_center" headers="stub_1_8 Y(1)">8</td>
</tr>
<tr class="odd">
<th id="stub_1_9" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_9 Project">9</td>
<td class="gt_row gt_center" headers="stub_1_9 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(0)" style="background-color: #5CACEE">16</td>
<td class="gt_row gt_center" headers="stub_1_9 Y(1)">8</td>
</tr>
<tr class="even">
<th id="stub_1_10" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_10 Project">10</td>
<td class="gt_row gt_center" headers="stub_1_10 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_10 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="odd">
<th id="stub_1_11" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_11 Project">11</td>
<td class="gt_row gt_center" headers="stub_1_11 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(0)">17</td>
<td class="gt_row gt_center" headers="stub_1_11 Y(1)" style="background-color: #5CACEE">5</td>
</tr>
<tr class="even">
<th id="stub_1_12" class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" scope="row"></th>
<td class="gt_row gt_center" headers="stub_1_12 Project">12</td>
<td class="gt_row gt_center" headers="stub_1_12 Region">B</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(0)" style="background-color: #5CACEE">18</td>
<td class="gt_row gt_center" headers="stub_1_12 Y(1)">5</td>
</tr>
<tr class="odd">
<th id="grand_summary_stub_1" class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\bar{Y}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(0)">9.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_first_grand_summary_row" headers="grand_summary_stub_1 Y(1)">5.58</td>
</tr>
<tr class="even">
<th id="grand_summary_stub_2" class="gt_row gt_left gt_stub gt_grand_summary_row gt_last_summary_row" data-quarto-table-cell-role="th" scope="row"><span class="math inline">$\hat{\bar{Y}}$</span></th>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Project">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Region">—</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(0)">10.33</td>
<td class="gt_row gt_center gt_grand_summary_row gt_last_summary_row" headers="grand_summary_stub_2 Y(1)">4.33</td>
</tr>
</tbody>
</table>

<figure>

</figure>

<style>#hlpbxfqluz table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#hlpbxfqluz thead, #hlpbxfqluz tbody, #hlpbxfqluz tfoot, #hlpbxfqluz tr, #hlpbxfqluz td, #hlpbxfqluz th {
  border-style: none;
}

#hlpbxfqluz p {
  margin: 0;
  padding: 0;
}

#hlpbxfqluz .gt_table {
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

#hlpbxfqluz .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#hlpbxfqluz .gt_title {
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

#hlpbxfqluz .gt_subtitle {
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

#hlpbxfqluz .gt_heading {
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

#hlpbxfqluz .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#hlpbxfqluz .gt_col_headings {
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

#hlpbxfqluz .gt_col_heading {
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

#hlpbxfqluz .gt_column_spanner_outer {
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

#hlpbxfqluz .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#hlpbxfqluz .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#hlpbxfqluz .gt_column_spanner {
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

#hlpbxfqluz .gt_spanner_row {
  border-bottom-style: hidden;
}

#hlpbxfqluz .gt_group_heading {
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

#hlpbxfqluz .gt_empty_group_heading {
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

#hlpbxfqluz .gt_from_md > :first-child {
  margin-top: 0;
}

#hlpbxfqluz .gt_from_md > :last-child {
  margin-bottom: 0;
}

#hlpbxfqluz .gt_row {
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

#hlpbxfqluz .gt_stub {
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

#hlpbxfqluz .gt_stub_row_group {
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

#hlpbxfqluz .gt_row_group_first td {
  border-top-width: 2px;
}

#hlpbxfqluz .gt_row_group_first th {
  border-top-width: 2px;
}

#hlpbxfqluz .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#hlpbxfqluz .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#hlpbxfqluz .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#hlpbxfqluz .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#hlpbxfqluz .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#hlpbxfqluz .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#hlpbxfqluz .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#hlpbxfqluz .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#hlpbxfqluz .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#hlpbxfqluz .gt_footnotes {
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

#hlpbxfqluz .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#hlpbxfqluz .gt_sourcenotes {
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

#hlpbxfqluz .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#hlpbxfqluz .gt_left {
  text-align: left;
}

#hlpbxfqluz .gt_center {
  text-align: center;
}

#hlpbxfqluz .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#hlpbxfqluz .gt_font_normal {
  font-weight: normal;
}

#hlpbxfqluz .gt_font_bold {
  font-weight: bold;
}

#hlpbxfqluz .gt_font_italic {
  font-style: italic;
}

#hlpbxfqluz .gt_super {
  font-size: 65%;
}

#hlpbxfqluz .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#hlpbxfqluz .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#hlpbxfqluz .gt_indent_1 {
  text-indent: 5px;
}

#hlpbxfqluz .gt_indent_2 {
  text-indent: 10px;
}

#hlpbxfqluz .gt_indent_3 {
  text-indent: 15px;
}

#hlpbxfqluz .gt_indent_4 {
  text-indent: 20px;
}

#hlpbxfqluz .gt_indent_5 {
  text-indent: 25px;
}

#hlpbxfqluz .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#hlpbxfqluz div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| <span class="math inline">\$\\hat{\\bar{Y}}\_0\$</span> | <span class="math inline">\$\\hat{\\bar{Y}}\_1\$</span> | <span class="math display">\\$$\\widehat{ATE}\\$$</span> |
|----|----|----|
| 8.83 | 6.17 | −2.67 |
| 9.83 | 4.83 | −5.00 |
| 8.83 | 5.00 | −3.83 |
| 9.83 | 3.67 | −6.17 |
| 9.83 | 4.83 | −5.00 |

##

Let <span class="math inline">\$A\$</span> and <span class="math inline">\$B\$</span> be a (non-random) partition of the units <span class="math inline">\$\\{1, \\ldots, n\\}\$</span> into blocks and let be <span class="math inline">\$n\_A\$</span> and <span class="math inline">\$n\_B\$</span> their sizes.

<span class="math display">\\$$\\begin{equation} \\begin{aligned} ATE &= \\frac{1}{n}(Y\_1(1) - Y\_1(0)) + \\frac{1}{n}(Y\_2(1) - Y\_2(0)) + \\ldots + \\frac{1}{n}(Y\_n(1) - Y\_n(0)) \\\\ &= \\sum\_{i \\in A} \\frac{1}{n} Y\_i(1) - Y\_i(0) + \\sum\_{i \\in B} \\frac{1}{n} Y\_i(1) - Y\_i(0) \\\\ &= \\frac{1}{n} \\frac{n\_A}{1} \\frac{1}{n\_A} \\sum\_{i \\in A} Y\_i(1) - Y\_i(0) + \\frac{1}{n} \\frac{n\_B}{1} \\frac{1}{n\_B} \\sum\_{i \\in B} Y\_i(1) - Y\_i(0) \\\\ &= \\frac{n\_A}{n} ATE\_A + \\frac{n\_B}{n} ATE\_B \\\\ \\end{aligned} \\end{equation}\\$$</span>

##

<span class="math display">\\$$\\begin{equation} \\begin{aligned} Var(\\widehat{ATE}) &= Var(\\frac{n\_A}{n} \\widehat{ATE}\_A + \\frac{n\_B}{n} \\widehat{ATE}\_B) \\\\ &= \\frac{n\_A^2}{n^2} Var(\\widehat{ATE}\_A) + \\frac{n\_B^2}{n^2} Var(\\widehat{ATE}\_B) \\\\ \\end{aligned} \\end{equation}\\$$</span>

<span class="math display">\\$$\\begin{equation} \\begin{aligned} SE(\\widehat{ATE}) &= \\sqrt{ \\frac{n\_A^2}{n^2} (SE(\\widehat{ATE}\_A)^2) + \\frac{n\_B^2}{n^2} (SE(\\widehat{ATE}\_B)^2)} \\\\ \\end{aligned} \\end{equation}\\$$</span>

Recall for <span class="math inline">\$CR{1}\$</span>,

<span class="math display">\\$$ SE(\\widehat{ATE}) = \\sqrt{ \\frac{1}{n - 1} \\left( \\frac{n\_0 \\sigma\_1^2}{n\_1} + \\frac{n\_1 \\sigma\_0^2}{n\_0} + 2 Cov(Y\_i(1), Y\_i(0)) \\right) } \\$$</span>

##  {data-id="quarto-animate-title"}

Exact block SEs:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
n_A <- 6

a_sigsq_1 <- mean((indo_cb$`Y(1)`[ind_a] - mean(indo_cb$`Y(1)`[ind_a]))^2)
a_sigsq_0 <- mean((indo_cb$`Y(0)`[ind_a] - mean(indo_cb$`Y(0)`[ind_a]))^2)
a_cov_01 <- mean((indo_cb$`Y(1)`[ind_a] - mean(indo_cb$`Y(1)`[ind_a])) *
               (indo_cb$`Y(0)`[ind_a] - mean(indo_cb$`Y(0)`[ind_a])))
a_var_ATE <- 1 / (n_A - 1) * (a_sigsq_0 + a_sigsq_1 + 2 * a_cov_01)
a_se_ATE <- sqrt(a_var_ATE)
```



``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
a_se_ATE
```

    [1] 2.389793

##  {data-id="quarto-animate-title"}

Exact block SEs:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
a_se_ATE
```

    [1] 2.389793

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
n_B <- 6
b_sigsq_1 <- mean((indo_cb$`Y(1)`[ind_b] - mean(indo_cb$`Y(1)`[ind_b]))^2)
b_sigsq_0 <- mean((indo_cb$`Y(0)`[ind_b] - mean(indo_cb$`Y(0)`[ind_b]))^2)
b_cov_01 <- mean((indo_cb$`Y(1)`[ind_b] - mean(indo_cb$`Y(1)`[ind_b])) *
               (indo_cb$`Y(0)`[ind_b] - mean(indo_cb$`Y(0)`[ind_b])))
b_var_ATE <- 1 / (n_B - 1) * (b_sigsq_0 + b_sigsq_1 + 2 * b_cov_01)
b_se_ATE <- sqrt(b_var_ATE)
```

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
b_se_ATE
```

    [1] 0.6191392

##

Exact SE:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
ab_se_ate <- sqrt(n_A^2 / n^2 * a_se_ATE^2  + n_B^2 / n^2 * b_se_ATE^2)
ab_se_ate
```

    [1] 1.234346

<figure>

</figure>

---

[← Completely Randomized Design \$CR$$1$$\$](02-completely-randomized-design.md) · [Up: contents](index.md)
