---
title: Concepts in Computing with Data {#concepts-in-computing-with-data .title}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/01-components-design-1/slides.html
source_file: sources/berkeley-stat158/spring-2026/01-components-design-1/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Concepts in Computing with Data {#concepts-in-computing-with-data .title}

**Source:** [`01-components-design-1/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/01-components-design-1/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

STAT 133

## Welcome to STAT 133!

We will begin at ten past. By that time, please

- silence phones and put into your bag
- close and stow your laptops

## Making Data

On one side of your card write answers to the following questions (borrow a pen from a neighbor if needed):

1.  What is your lab number? (integer)
2.  How many years have you been at Cal? (integer)
3.  Are you a Statistics major? (true / false)

On the other side of the card write answers to the following questions:

1.  What was your “song of the summer”? (character string)
2.  What is the farthest that you were from Cal this summer in miles? (numeric)

## With the people around you…

Take a few minutes to share your **name** and the answers to the questions that you wrote down.

−

\+

<span class="countdown-digits minutes">`03`</span><span class="countdown-digits colon">`:`</span><span class="countdown-digits seconds">`00`</span>

##

# What this class is about

In preparation for the next case study, ask “Raise your hand if you have ever voted by mail. Did you enjoy it? Would you rather have gone to a polling place?”.

The way elections are conducted has become contentious. Those in support of vote by mail say it increases the franchise: gets more people to vote. Those in support of-in person voting say it increasing civic participation and is less subject to fraud. The current administration is pushing to eliminate vote by mail in favor of in-person voting.

The reason why we vote by mail in California is because of how they vote in Oregon.

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

##

- 1998 Oregon 1st state to conduct elections by mail.
- Voters mailed a ballot a month before.
- They return it at their leisure.

What are the dynamics of this form of voting?
What is “turnout” over time?

In 1998, Oregon became the first state to conduct its elections exclusively by mail. Every election, all registered voters are automatically mailed ballots to their home address roughly a month before the election. Voters then vote at their leisure and mail back or drop off their ballot sometime before the election closes. Due to concerns about the Covid-19 pandemic, many other states have implemented some version of Oregon’s voting system in preparation for the November 3rd, 2020 election next Tuesday.

At the end, before switching slides, ask: “What data would be useful to answer this question? Where could I find it?”

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

##

##

##

##

Ask: “What appears to be stored in each cell?”

Answer: the number of ballots received since last recorded date in that county.

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

## Analysis workflow

1.  Access and store data
2.  Perform Optical Character Recognition (OCR): PDF &gt; .xls, .csv

##

What is “turnout” over time?

##

Boardwork

##

What is “turnout” over time?

## Analysis workflow

1.  Access and store data
2.  Perform Optical Character Recognition (OCR): PDF &gt; .xls, .csv
3.  Isolate data from Deschutes County
4.  Convert day from words to numbers
5.  Create new column of cumulative returns
6.  Create line plot

##

Boardwork

##

---

[Up: contents](index.md) · [How this class works →](02-how-this-class-works.md)
