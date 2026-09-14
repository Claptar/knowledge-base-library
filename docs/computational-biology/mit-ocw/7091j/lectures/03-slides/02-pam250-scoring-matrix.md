---
title: PAM250 Scoring Matrix
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PAM250 Scoring Matrix

**Source:** `lectures/03-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

27

###### **Dynamic Programming: filling in matrix**


<!-- Start of picture text -->
i =0  1  2  3  4  5<br>Gap  V  D  S  C  Y<br>j =  4<br>0  -8  -16  -24  -32  -40<br>0  Gap  4<br>-8<br>-8<br>1  V<br>-8  sij<br>-16<br>2 E<br>3  S  -24   Sij  = max of:  Si-1, j-1 +  σ (xi, yj)  (diagonal)<br>4  L  -32<br>Si-1, j + A  (from left to right)<br>5  C  -40<br>Si, j-1 + A  (from top to bottom)<br>6  Y  -48<br><!-- End of picture text -->

28


<!-- Start of picture text -->
Sequence 1<br>i =0  1  2  3  4  5<br>Sequence 2<br>Gap  V  D  S  C  Y<br>j =<br>0  -8  -16  -24  -32  -40<br>0  Gap  4<br>-8<br>1  V  -8<br>4<br>-8<br>2  E  -16<br>3  S  -24<br>-32<br>4  L<br>-40<br>5  C<br>6  Y  -48<br><!-- End of picture text -->

29

|||**Sequ**|**ence 1**|||
|---|---|---|---|---|---|
|**Sequenc**|**e 2**|**i =0**|**1**<br>**2**|**3**|**4**<br>**5**|
|**j =**||**Gap**|**V**<br>**D**|**S**|<br>**C**<br>**Y**|
|**0**<br>**1**|**Gap**<br>**V**|**0**<br>**4**<br>**-8**|**-8**<br>**-16**<br>**-2**<br>**-8**<br>**-8**<sup>**sij**</sup><br>**4**|**-24**|**-32**<br>**-40**|
|**2**|**E**|**-16**||||
|**3**|**S**|**-24**|**Sij= ma**|**x of:**|**Si-1, j-1 +**σ**(xi, yj) **(diagonal)|
|**4**<br>**5**|**L**<br>**C**|**-32**<br>**-40**|||**Si-1, j+ A**(from left to right)|
|**6**|**Y**|**-48**|||**Si, j-1 + A**(from top to bottom)|


30


<!-- Start of picture text -->
Sequence 1<br>Sequence 2  i =0  1  2  3  4  5<br>Gap  V  D  S  C  Y<br>j =<br>0  Gap  0  -8  -16  -24  -32  -40<br>4  -2  -8<br>1  V  -8  4 -8  -4<br>2  E<br>3  S<br>4  L<br>5  C<br>6  Y<br><!-- End of picture text -->

31


<!-- Start of picture text -->
Completed Dynamic Programming Matrix<br>i =0  1  2  3  4  5<br>Gap  V  D  S  C  Y<br>j =<br>0  -8  -16  -24  -32  -40<br>0  Gap  4<br>-8<br>1 V  -8  -8 -4 -12  -20  -28<br>4<br>3<br>2  E  -16  -6 7  -9  -17<br>2  -1<br>3  S  -24 -14  -6  9  1  -7<br>-8<br>4  L  -32  -22  -14  1  3  0<br>12<br>5  C  -40  -30  -22  -7   13   3<br>10<br>6  Y  -48  -38  -30  -15  5  23<br><!-- End of picture text -->

**Keep track of scores AND how we got them** . **“traceback matrix”**

32

###### **<u>The Traceback:</u>**


<!-- Start of picture text -->
After the alignment square is finished, start at the lower right and<br>work backwards following the arrows to see how you got there.<br>i =0  1  2  3  4  5<br>Gap  V  D  S  C  Y<br>j =<br>0  Gap  0  4  -8  -16  -24  -32  -40<br>-3  -8<br>-8<br>1  V  -8  4 -4  -12  -20  -28<br>3<br>2  E  -16  -6  7  -9  -17<br>2  -1<br>3  S  -24  -14  -6  9  1  -7<br>4  L  -32  -22  -14  1  3<br>0<br>5  C  -40  -30  -22  -7  13  3<br>6  Y  -48  -38  -30  -15  5<br>23<br><!-- End of picture text -->

33


<!-- Start of picture text -->
V D S – C Y<br>The Traceback<br>V E S L C Y<br>gives the alignment:<br>i =0  1  2  3  4  5<br>Gap  V  D  S  C  Y<br>j =<br>0  Gap  0  4  -8  -16  -24  -32  -40<br>-3  -8<br>1  V  -8  4 -8  -4  -12  -20  -28<br>3<br>2  E  -16  -6  7  -1  -9  -17<br>2<br>3  S  -24  -14  -6  9  1  -7<br>4  L<br>-32  -22  -14  1  3<br>0<br>5  C  -40  -30  -22  -7  13  3<br>6  Y<br>-48  -38  -30  -15  5<br>23<br>“Life must be lived forwards and understood backwards.”<br>- Søren Kierkegaard<br><!-- End of picture text -->

34

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Semiglobal Alignment →](03-semiglobal-alignment.md)
