---
title: Last to First (LF) function
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Last to First (LF) function

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**LF(** **_i_ ,** **_qc_ ) = occ(** **_qc_ ) + count(** **_i_ ,** **_qc_ )** returns the index of the char in the First column that is lexically <u>equivalent to the instance of</u> _qc_ in position _i_ of the BWT, using the fact that rank is same in First and Last columns

<u>idx BWT</u> 0 $ B A N A N A 1 A $ B A N A N 2 A N A $ B A N 3 A N A N A $ B 4 B A N A N A $ 5 N A $ B A N A 6 N A N A $ B A

**occ(** **_qc_ )** = # characters lexically smaller than _qc_ in the BWT (e.g. rank in **First** column of matrix) **count(** **_i_ ,** **_qc_ )** = # of _qc_ characters before position _i_ in the BWT (e.g. rank of _qc_ character at position _i_ , minus 1)

In other words, since the first column is alphabetical, we first find the row where our character starts in the First column (e.g. Ns begin at index 5), then use the fact that rank is same in first and last column to find the specific char in First col that is the same lexical occurrences as our query in the BWT

11

## **Using the BWT and LF function to do exact matching**

- **say we have the following sequence:  $ABBABA, and we want to find occurrences of BBA**

- **using the BW-matrix, we can start by finding all rows beginning with "A"**

**but, we're only interested in rows where the A is preceded by a B** and now, we only want suffixes where the B is preceded by another B Once we know where our matches to our query begin in the BWT, use LF to get these locations in original string


To make this clearer, we showed the entire BW matrix. But how to do this if we only have the BWT? - use the LF function!

http://www.cs.jhu.edu/~langmea/resources/lecture_notes/bwt_and_fm_index.pdf

12


13

#### **Using the BWT and LF function to do exact matching**


<!-- Start of picture text -->
2<br>4<br><!-- End of picture text -->

1) at end of loop, calculate **range** = bot – top - if **range** == 1:

exactly one match at **top**

- if **range** = _n_ > 1:

   - _n_ matches of query at **top** to **bot** -1

- if **range** == 0:

   - query does not exist in genome

in our case, there are exactly two occurrences of "ANA" in "BANANA"

- 2) how can we find the location of our matches in the original string? - use LF function to walk back to the beginning of the string, starting at the beginning of the identified match (= **top** ) - count # of times we "walk left" until hitting the end of string

- char ($) to get the hit offset

14

#### Find location of our match

- let's find the location of one of the two matches we found, corresponding to location **2** in the BWT: - use LF to "walk back" from the beginning the match ("top") until we see the end-of-string character "$"

pseudocode:

i = top # final value of 'top' after matching offset = 0 while BWT[i] != "$": offset += 1

i = LF(i, BWT[i])

15

#### Find location of our match

let's find the location of one of the two matches we found, corresponding to location _i=_ **_2_** in the BWT:

- use LF to "walk back" until we see the end-of-string char "$" - obtain hit offset = 3 B A N A N A


16


17

## Regenerating your string from its BWT

same as using LF to walk-back to the beginning of the string and get the hit offset, except you start from the end - by definition, BWT[0] is the last character of original string i = 0 str = ""

while bwt[i] != "$": str = bwt[i] + str i = LF(i, bwt[i])

**<u>iter 0: iter 1: iter 2: iter 3:</u>** 0 A i = 0 str = BWT[0] + str str = BWT[1] + str str = BWT[5] + str str = "" = "A" = "NA" = "ANA" 1 N 2 N i = LF(0, "A") = **1** i = LF(1, "N") = **5** i = LF(5, "A") = **2**

3 B **<u>iter 4: iter 5: iter 6:</u>** 4 $ BWT[ **4** ] str = BWT[2] + str str = BWT[6] + str str = BWT[3] + str 5 A == "$" = "NANA" = "ANANA" = "BANANA" 6 A **DONE** i = LF(2, "N") = **6** i = LF(6, "A") = **3** i = LF(3, "B") = **4** 7

18

---

[← BWT and character rank](06-bwt-and-character-rank.md) · [Up: contents](index.md) · [Some caveats →](08-some-caveats.md)
