---
title: Exploratory Data Analysis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Exploratory Data Analysis

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Making Paper

<style>#akuosphquk table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#akuosphquk thead, #akuosphquk tbody, #akuosphquk tfoot, #akuosphquk tr, #akuosphquk td, #akuosphquk th {
  border-style: none;
}

#akuosphquk p {
  margin: 0;
  padding: 0;
}

#akuosphquk .gt_table {
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

#akuosphquk .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#akuosphquk .gt_title {
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

#akuosphquk .gt_subtitle {
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

#akuosphquk .gt_heading {
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

#akuosphquk .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#akuosphquk .gt_col_headings {
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

#akuosphquk .gt_col_heading {
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

#akuosphquk .gt_column_spanner_outer {
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

#akuosphquk .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#akuosphquk .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#akuosphquk .gt_column_spanner {
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

#akuosphquk .gt_spanner_row {
  border-bottom-style: hidden;
}

#akuosphquk .gt_group_heading {
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

#akuosphquk .gt_empty_group_heading {
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

#akuosphquk .gt_from_md > :first-child {
  margin-top: 0;
}

#akuosphquk .gt_from_md > :last-child {
  margin-bottom: 0;
}

#akuosphquk .gt_row {
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

#akuosphquk .gt_stub {
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

#akuosphquk .gt_stub_row_group {
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

#akuosphquk .gt_row_group_first td {
  border-top-width: 2px;
}

#akuosphquk .gt_row_group_first th {
  border-top-width: 2px;
}

#akuosphquk .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#akuosphquk .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#akuosphquk .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#akuosphquk .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#akuosphquk .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#akuosphquk .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#akuosphquk .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#akuosphquk .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#akuosphquk .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#akuosphquk .gt_footnotes {
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

#akuosphquk .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#akuosphquk .gt_sourcenotes {
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

#akuosphquk .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#akuosphquk .gt_left {
  text-align: left;
}

#akuosphquk .gt_center {
  text-align: center;
}

#akuosphquk .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#akuosphquk .gt_font_normal {
  font-weight: normal;
}

#akuosphquk .gt_font_bold {
  font-weight: bold;
}

#akuosphquk .gt_font_italic {
  font-style: italic;
}

#akuosphquk .gt_super {
  font-size: 65%;
}

#akuosphquk .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#akuosphquk .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#akuosphquk .gt_indent_1 {
  text-indent: 5px;
}

#akuosphquk .gt_indent_2 {
  text-indent: 10px;
}

#akuosphquk .gt_indent_3 {
  text-indent: 15px;
}

#akuosphquk .gt_indent_4 {
  text-indent: 20px;
}

#akuosphquk .gt_indent_5 {
  text-indent: 25px;
}

#akuosphquk .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#akuosphquk div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| strength | hard | time | pressure |
|----------|------|------|----------|
| 196.6    | 2    | 3hrs | 400      |
| 196.0    | 2    | 3hrs | 400      |
| 198.5    | 4    | 3hrs | 400      |
| 197.2    | 4    | 3hrs | 400      |
| 197.5    | 8    | 3hrs | 400      |
| 196.6    | 8    | 3hrs | 400      |
| 197.7    | 2    | 3hrs | 500      |
| 196.0    | 2    | 3hrs | 500      |
| 196.0    | 4    | 3hrs | 500      |
| 196.9    | 4    | 3hrs | 500      |
| 195.6    | 8    | 3hrs | 500      |
| 196.2    | 8    | 3hrs | 500      |
| 199.8    | 2    | 3hrs | 650      |
| 199.4    | 2    | 3hrs | 650      |
| 198.4    | 4    | 3hrs | 650      |
| 197.6    | 4    | 3hrs | 650      |
| 197.4    | 8    | 3hrs | 650      |
| 198.1    | 8    | 3hrs | 650      |
| 198.4    | 2    | 4hrs | 400      |
| 198.6    | 2    | 4hrs | 400      |
| 197.5    | 4    | 4hrs | 400      |
| 198.1    | 4    | 4hrs | 400      |
| 197.6    | 8    | 4hrs | 400      |
| 198.4    | 8    | 4hrs | 400      |
| 199.6    | 2    | 4hrs | 500      |
| 200.4    | 2    | 4hrs | 500      |
| 198.7    | 4    | 4hrs | 500      |
| 198.0    | 4    | 4hrs | 500      |
| 197.0    | 8    | 4hrs | 500      |
| 197.8    | 8    | 4hrs | 500      |
| 200.6    | 2    | 4hrs | 650      |
| 200.9    | 2    | 4hrs | 650      |
| 199.6    | 4    | 4hrs | 650      |
| 199.0    | 4    | 4hrs | 650      |
| 198.5    | 8    | 4hrs | 650      |
| 199.8    | 8    | 4hrs | 650      |

##

## Main Effects Plot

---

[← Higher Order Factorial Designs](01-higher-order-factorial-designs.md) · [Up: contents](index.md) · [Interaction Plots →](03-interaction-plots.md)
