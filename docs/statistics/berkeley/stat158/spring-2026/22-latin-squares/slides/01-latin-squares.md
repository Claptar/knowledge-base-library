---
title: Latin Squares
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/22-latin-squares/slides.html
source_file: sources/berkeley-stat158/spring-2026/22-latin-squares/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Latin Squares

**Source:** [`22-latin-squares/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/22-latin-squares/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Diet and Milk: LS

**LS**: A *Latin Square* design is a special case of a CB design with *two* blocking factors.

- Each factor has the same number of levels.
- Each treatment appears exactly once in each row and column of the Latin Square.

## While you’re waiting

The square below has each letter appearing only once in each row and column. How many such squares are there?

|     |     |     |     |
|-----|-----|-----|-----|
| A   | B   | C   | D   |
| B   | A   | D   | C   |
| C   | D   | B   | A   |
| D   | C   | A   | B   |

Correct answer of all Latin Squares of order 4 is 576 = 4 \* 4! \* 3!

Correct answer of standard Latin Squares of order 4 is 4 = 4! / 4 = 24 / 4

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

## Counting Latin Squares

|     |     |     |     |
|-----|-----|-----|-----|
| A   | B   | C   | D   |
| B   |     |     |     |
| C   |     |     |     |
| D   |     |     |     |

Say: It’s clear that it’s easy to make an alternative square simply by swapping two rows or two columns. But beyond those variants, how many squares are there? Let’s start by counting the number of squares that have a fixed row and column order. These are called *standard* Latin Squares.

Write in right col:

*Standard Latin Square*: A square with treatments in alphabetical order in the first row and column.

Say: Let’s count the number of standard squares. Which letters can go in spot (2,2)? There are three cases, A, C, and D.

Write: A, C, D

Let’s start with A in (2,2). How many squares result from that? (fill in square as you go and show that there are two squares with A in (2,2)).

Now let’s put C in (2,2). How many squares result from that? (fill in square as you go and show that there is one square with C in (2,2)).

Finally, let’s put D in (2,2). How many squares result from that? (fill in square as you go and show that there is one square with D in (2,2)).

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

## Counting Latin Squares

|     |     |     |     |
|-----|-----|-----|-----|
| A   | B   | C   | D   |
| B   | A   | D   | C   |
| C   | D   | B   | A   |
| D   | C   | A   | B   |

|     |     |     |     |
|-----|-----|-----|-----|
| D   | C   | A   | B   |
| B   | A   | D   | C   |
| C   | D   | B   | A   |
| A   | B   | C   | D   |

Say: Now, we need to count the total number of Latin Squares that one can generate from a given Standard Square.

Write: Given a standard square of g=4, how many Latin Squares can we generate from it?

4! squares from permuting the rows 4! squares from permuting the columns Only 1/4 of the squares are unique because of the symmetry of the square (swapping rows and columns can give the same square).

<span class="math display">\\$$ \\frac{4! \\times 4!}{4} = 144 \\$$</span>

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

## Counting Latin Squares

| Type     | g=2 | g=3 | g=4 | g=5    |
|----------|-----|-----|-----|--------|
| standard | 1   | 1   | 4   | 56     |
| all LS   | 2   | 12  | 576 | 161280 |

## How to do random assignment in LS

1.  Randomly select a *standard* latin square (treatments in alphabetical order in first row and column).
2.  Randomly assign levels of the first blocking factor to rows.
3.  Randomly assign levels of the second blocking factor to columns.
4.  Randomly assign treatment levels to letters.

---

[Up: contents](index.md) · [Inference →](02-inference.md)
