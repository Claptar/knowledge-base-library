---
title: A Study of Diet and Milk
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/21-two-blocking-factors/slides.html
source_file: sources/berkeley-stat158/spring-2026/21-two-blocking-factors/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# A Study of Diet and Milk

**Source:** [`21-two-blocking-factors/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/21-two-blocking-factors/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Study: Diet and Milk

A study was conducted to compare the effect that three diets had on milk production in cows: full grain, partial grain, and roughage. A cohort of cows was recruited after giving birth, when milk production is highest. Once their new diet began, they would sustain it for 6 weeks and then measure milk production. The farm can only offer a single diet at any given time.

**4 Components of the Experiment**

- response is the milk production (measured in pounds per day)
- factor of interest is the diet (full grain, partial grain, roughage)
- experimental unit: cow?

Ask: Let’s think through difference designs we could use / methods of allocation.

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

## Diet and Milk: CR

**CR**: units assigned to treatments completely at random

Say we have nine cows. Draw data frame with cols for cow id and diet.

- cows are randomly assigned to one of the three diets
  - neg: variability time block to time block (production is highest at the first time block)
  - neg: high cow-cow variability

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

## Diet and Milk: CB {data-id="quarto-animate-title"}

**CB**: units assigned to treatments at random within blocks (each treatment assigned exactly once per block).

Redraw the same DF as the previous slide, but add a third column to the data frame with week: 1-6, 7-12, and 13-18. Each week is a block.

- cows are randomly assigned to one of the three diets within time period block (week)
  - pro: variability due to time is controlled
  - neg: cow to cow variability is still high

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

## Diet and Milk: CB {data-id="quarto-animate-title"}

**CB**: units assigned to treatments at random within blocks (each treatment assigned exactly once per block). There are be more than one blocking factor.

Change the cow id column to being highlighted as a blocking factor alongside week. Redo the cow id’s so that it’s only three cows total that are studied instead of nine.

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

---

[← Two Blocking Factors](01-two-blocking-factors.md) · [Up: contents](index.md)
