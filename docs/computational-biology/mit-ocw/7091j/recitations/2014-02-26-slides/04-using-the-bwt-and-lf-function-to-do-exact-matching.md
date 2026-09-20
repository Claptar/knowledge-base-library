---
title: Using the BWT and LF function to do exact matching
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Using the BWT and LF function to do exact matching

find occurrences of ANA in BANANA
query = "ANA", bwt = "ANNB$AA"
top = 0
bot = len(bwt) # len(bwt) = 7 (yes, this is valid)
for qc in reverse(query): # need to match from end to start of query
top = LF(top, qc) # LF(i,qc) = occ(qc) + count(i,qc)
bot = LF(bot, qc)

**iter 0:**
top = 0
bot = 7

| idx | F | L |
| :---: | :---: | :---: |
| 0 | $ | A |
| 1 | A | N |
| 2 | A | N |
| 3 | A | B |
| 4 | B | $ |
| 5 | N | A |
| 6 | N | A |
| 7 | | |

(0 $\rightarrow$ 1, 7 $\rightarrow$ 4)

**iter 1:**
top=LF(0,'A')= 1
bot=LF(7,'A')= 4

| idx | F | L |
| :---: | :---: | :---: |
| 0 | $ | A |
| 1 | A | N |
| 2 | A | N |
| 3 | A | B |
| 4 | B | $ |
| 5 | N | A |
| 6 | N | A |

(1 $\rightarrow$ 5, 4 $\rightarrow$ 7)

**iter 2:**
top=LF(1,'N')= 5
bot=LF(4,'N')= 7

| idx | F | L |
| :---: | :---: | :---: |
| 0 | $ | A |
| 1 | A | N |
| 2 | A | N |
| 3 | A | B |
| 4 | B | $ |
| 5 | N | A |
| 6 | N | A |

(5 $\rightarrow$ 2, 7 $\rightarrow$ 4)

**iter 3:**
top=LF(5,'A')= 2
bot=LF(7,'A')= 4

| idx | F | L |
| :---: | :---: | :---: |
| 0 | $ | A |
| 1 | A | N |
| 2 | A | N |
| 3 | A | B |
| 4 | B | $ |
| 5 | N | A |
| 6 | N | A |

OK, now what?

---

end:
top=LF(5,'A')= 2
bot=LF(7,'A')= 4

| idx | F | L |
| :---: | :---: | :---: |
| 0 | $ | A |
| 1 | A | N |
| 2 | A | N |
| 3 | A | B |
| 4 | B | $ |
| 5 | N | A |
| 6 | N | A |
| 7 | | |

1) at end of loop, calculate **range** = bot – top
- if range == 1:
  exactly one match at top
- if range = $n > 1$:
  $n$ matches of query at top to bot-1
- if range == 0:
  query does not exist in genome

in our case, there are exactly two occurrences of "ANA" in "BANANA"

2) how can we find the location of our matches in the original string?
- use LF function to walk back to the beginning of the string, starting at the beginning of the identified match (= top)
- count # of times we "walk left" until hitting the end of string char ($) to get the hit offset

---

## Find location of our match

- let's find the location of one of the two matches we found, corresponding to location **2** in the BWT:
- use LF to "walk back" from the beginning the match ("top") until we see the end-of-string character "\$"

pseudocode:
```python
i = top      # final value of 'top' after matching
offset = 0
while BWT[i] != "$":
    offset += 1
    i = LF(i, BWT[i])
```

---

---

[← Why use the BWT?](03-why-use-the-bwt.md) · [Up: contents](index.md) · Find location of our match →
