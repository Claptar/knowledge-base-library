---
title: 'Study: Battery Lifetime'
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/14-two-factors/slides.html
source_file: sources/berkeley-stat158/spring-2026/14-two-factors/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Study: Battery Lifetime

**Source:** [`14-two-factors/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/14-two-factors/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Battery Lifetime Data

<style>#uljgsinblo table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#uljgsinblo thead, #uljgsinblo tbody, #uljgsinblo tfoot, #uljgsinblo tr, #uljgsinblo td, #uljgsinblo th {
  border-style: none;
}

#uljgsinblo p {
  margin: 0;
  padding: 0;
}

#uljgsinblo .gt_table {
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

#uljgsinblo .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#uljgsinblo .gt_title {
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

#uljgsinblo .gt_subtitle {
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

#uljgsinblo .gt_heading {
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

#uljgsinblo .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#uljgsinblo .gt_col_headings {
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

#uljgsinblo .gt_col_heading {
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

#uljgsinblo .gt_column_spanner_outer {
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

#uljgsinblo .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#uljgsinblo .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#uljgsinblo .gt_column_spanner {
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

#uljgsinblo .gt_spanner_row {
  border-bottom-style: hidden;
}

#uljgsinblo .gt_group_heading {
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

#uljgsinblo .gt_empty_group_heading {
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

#uljgsinblo .gt_from_md > :first-child {
  margin-top: 0;
}

#uljgsinblo .gt_from_md > :last-child {
  margin-bottom: 0;
}

#uljgsinblo .gt_row {
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

#uljgsinblo .gt_stub {
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

#uljgsinblo .gt_stub_row_group {
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

#uljgsinblo .gt_row_group_first td {
  border-top-width: 2px;
}

#uljgsinblo .gt_row_group_first th {
  border-top-width: 2px;
}

#uljgsinblo .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#uljgsinblo .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#uljgsinblo .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#uljgsinblo .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#uljgsinblo .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#uljgsinblo .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#uljgsinblo .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#uljgsinblo .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#uljgsinblo .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#uljgsinblo .gt_footnotes {
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

#uljgsinblo .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#uljgsinblo .gt_sourcenotes {
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

#uljgsinblo .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#uljgsinblo .gt_left {
  text-align: left;
}

#uljgsinblo .gt_center {
  text-align: center;
}

#uljgsinblo .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#uljgsinblo .gt_font_normal {
  font-weight: normal;
}

#uljgsinblo .gt_font_bold {
  font-weight: bold;
}

#uljgsinblo .gt_font_italic {
  font-style: italic;
}

#uljgsinblo .gt_super {
  font-size: 65%;
}

#uljgsinblo .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#uljgsinblo .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#uljgsinblo .gt_indent_1 {
  text-indent: 5px;
}

#uljgsinblo .gt_indent_2 {
  text-indent: 10px;
}

#uljgsinblo .gt_indent_3 {
  text-indent: 15px;
}

#uljgsinblo .gt_indent_4 {
  text-indent: 20px;
}

#uljgsinblo .gt_indent_5 {
  text-indent: 25px;
}

#uljgsinblo .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#uljgsinblo div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| id  | material | temp | lifetime |
|-----|----------|------|----------|
| 1   | 1        | 15   | 130      |
| 2   | 1        | 15   | 155      |
| 3   | 1        | 70   | 34       |
| 4   | 1        | 70   | 40       |
| 5   | 1        | 125  | 20       |
| 6   | 1        | 125  | 70       |
| 7   | 1        | 15   | 74       |
| 8   | 1        | 15   | 180      |
| 9   | 1        | 70   | 80       |
| 10  | 1        | 70   | 75       |
| 11  | 1        | 125  | 82       |
| 12  | 1        | 125  | 58       |
| 13  | 2        | 15   | 150      |
| 14  | 2        | 15   | 188      |
| 15  | 2        | 70   | 136      |
| 16  | 2        | 70   | 122      |
| 17  | 2        | 125  | 25       |
| 18  | 2        | 125  | 70       |
| 19  | 2        | 15   | 159      |
| 20  | 2        | 15   | 126      |
| 21  | 2        | 70   | 106      |
| 22  | 2        | 70   | 115      |
| 23  | 2        | 125  | 58       |
| 24  | 2        | 125  | 45       |
| 25  | 3        | 15   | 138      |
| 26  | 3        | 15   | 110      |
| 27  | 3        | 70   | 174      |
| 28  | 3        | 70   | 120      |
| 29  | 3        | 125  | 96       |
| 30  | 3        | 125  | 104      |
| 31  | 3        | 15   | 168      |
| 32  | 3        | 15   | 160      |
| 33  | 3        | 70   | 150      |
| 34  | 3        | 70   | 139      |
| 35  | 3        | 125  | 82       |
| 36  | 3        | 125  | 60       |

*Counts in each treatment group*

<style>#gbfqrssyhk table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#gbfqrssyhk thead, #gbfqrssyhk tbody, #gbfqrssyhk tfoot, #gbfqrssyhk tr, #gbfqrssyhk td, #gbfqrssyhk th {
  border-style: none;
}

#gbfqrssyhk p {
  margin: 0;
  padding: 0;
}

#gbfqrssyhk .gt_table {
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

#gbfqrssyhk .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#gbfqrssyhk .gt_title {
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

#gbfqrssyhk .gt_subtitle {
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

#gbfqrssyhk .gt_heading {
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

#gbfqrssyhk .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#gbfqrssyhk .gt_col_headings {
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

#gbfqrssyhk .gt_col_heading {
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

#gbfqrssyhk .gt_column_spanner_outer {
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

#gbfqrssyhk .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#gbfqrssyhk .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#gbfqrssyhk .gt_column_spanner {
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

#gbfqrssyhk .gt_spanner_row {
  border-bottom-style: hidden;
}

#gbfqrssyhk .gt_group_heading {
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

#gbfqrssyhk .gt_empty_group_heading {
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

#gbfqrssyhk .gt_from_md > :first-child {
  margin-top: 0;
}

#gbfqrssyhk .gt_from_md > :last-child {
  margin-bottom: 0;
}

#gbfqrssyhk .gt_row {
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

#gbfqrssyhk .gt_stub {
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

#gbfqrssyhk .gt_stub_row_group {
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

#gbfqrssyhk .gt_row_group_first td {
  border-top-width: 2px;
}

#gbfqrssyhk .gt_row_group_first th {
  border-top-width: 2px;
}

#gbfqrssyhk .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#gbfqrssyhk .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#gbfqrssyhk .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#gbfqrssyhk .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#gbfqrssyhk .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#gbfqrssyhk .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#gbfqrssyhk .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#gbfqrssyhk .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#gbfqrssyhk .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#gbfqrssyhk .gt_footnotes {
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

#gbfqrssyhk .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#gbfqrssyhk .gt_sourcenotes {
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

#gbfqrssyhk .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#gbfqrssyhk .gt_left {
  text-align: left;
}

#gbfqrssyhk .gt_center {
  text-align: center;
}

#gbfqrssyhk .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#gbfqrssyhk .gt_font_normal {
  font-weight: normal;
}

#gbfqrssyhk .gt_font_bold {
  font-weight: bold;
}

#gbfqrssyhk .gt_font_italic {
  font-style: italic;
}

#gbfqrssyhk .gt_super {
  font-size: 65%;
}

#gbfqrssyhk .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#gbfqrssyhk .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#gbfqrssyhk .gt_indent_1 {
  text-indent: 5px;
}

#gbfqrssyhk .gt_indent_2 {
  text-indent: 10px;
}

#gbfqrssyhk .gt_indent_3 {
  text-indent: 15px;
}

#gbfqrssyhk .gt_indent_4 {
  text-indent: 20px;
}

#gbfqrssyhk .gt_indent_5 {
  text-indent: 25px;
}

#gbfqrssyhk .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#gbfqrssyhk div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| material | temp | n   |
|----------|------|-----|
| 1        | 15   | 4   |
| 1        | 70   | 4   |
| 1        | 125  | 4   |
| 2        | 15   | 4   |
| 2        | 70   | 4   |
| 2        | 125  | 4   |
| 3        | 15   | 4   |
| 3        | 70   | 4   |
| 3        | 125  | 4   |

## EDA

---

[← A Linear Model](02-a-linear-model.md) · [Up: contents](index.md)
