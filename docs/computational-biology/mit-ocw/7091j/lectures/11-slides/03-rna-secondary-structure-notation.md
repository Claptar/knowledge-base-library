---
title: RNA Secondary Structure Notation
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# RNA Secondary Structure Notation

**Source:** `lectures/11-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Parentheses notation ..(((…..)))……((((……..............)).))…

Arc (‘rainbow’) notation


………………………………………….

What do these structures look like? What is the difference between these two structures?

13


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Cate, Jamie H., Marat M. Yusupov, et al. "X-ray Crystal Structures of 70S Ribosome Functional Complexes." _Science_ 285, no. 5436 (1999): 2095-104.

14

## **Ribosome at 7 Å with tRNAs**


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Cate, Jamie H., Marat M. Yusupov, et al. "X-ray Crystal Structures of 70S Ribosome Functional Complexes." _Science_ 285, no. 5436 (1999): 2095-104.

Slide courtesy of Rachel Green

15

###### **Can build useful structures out of RNA**

###### **The exit channel for the growing polypeptide**

Slide courtesy of Rachel Green

© American Association for the Advancement of Science. All rights reserved. This content is excluded<sup>from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.</sup> Source: Ban, Nenad, Poul Nissen, et al. "The Complete Atomic Structure of the Large Ribosomal Subunit at 2.4 Å Resolution." _Science_ 289, no. 5481 (2000): 905-20.

16

###### RNA/protein distribution on the 50S ribosome

###### linguini = protein


<!-- Start of picture text -->
fettucini  = RNA<br><!-- End of picture text -->

- © American Association for the Advancement of Science. All rights reserved. This content is excluded<sup>from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.</sup> Source: Ban, Nenad, Poul Nissen, et al. "The Complete Atomic Structure of the Large Ribosomal Subunit at 2.4 Å Resolution." _Science_ 289, no. 5481 (2000): 905-20.

17

### **The ribosome is a ribozyme**

Nearest proteins and distances to active site (Å)

###### Slide courtesy of Rachel Green

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Nissen, Poul, Jeffrey Hansen, et al. "The Structural Basis of Ribosome Activity in Peptide Bond Synthesis." _Science_ 289, no. 5481 (2000): 920-30.

18

## What are the practical applications of knowing the ribosome structure?


<!-- Start of picture text -->
Antibiotics!<br><!-- End of picture text -->

© sources unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

19

##### ncRNAs: Challenges for Computational Biology

- Prediction of ncRNA structure

- Identification of ncRNA genes

- Prediction of ncRNA functions

20

RNA 2<sup>o</sup> structure by covariation / compensatory changes


```
Seq1:  A C G A A A G U
Seq2:  U A G U A A U A
Seq3:  A G G U G A C U
Seq4:  C G G C A A U G
Seq5:  G U G G G A A C
```


Mutual information statistic for pair of columns in a multiple alignment


<!-- Start of picture text -->
( i ,  j  )<br>( i ,  j  )  f<br>x , y<br>= ( i  ) (  j  )<br>x ,  y<br>M ij ∑ f x ,  y log 2  f<br>x f y<br><!-- End of picture text -->

( _i_ , _j_ ) _f x_ , _y_ = fraction of seqs w/ nt. _x_ in col. _i_ , nt. _y_ in col. _j_ ( _i_ ) _f x_ = fraction of seqs w/ nt. _x_ in col. _i_

sum over _x_ , _y_ = A, C, G, U

_M ij_<sup>is maximal (2 bits) if</sup><sup>_x_and</sup><sup>_y_individually appear</sup> at random (A,C,G,U equally likely), but perfectly covary (e.g., always complementary)

**Could use other measure of dependence (e.g., chi-square statistic)**

22

###### Inferring 2<sup>o</sup> structure from covariation


© sources unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

23

What is needed for accurate inference of RNA secondary structure by covariation?

- Secondary structure more highly conserved than primary sequence

- Sufficient divergence between homologs for many variations to have occurred, but not so much that can’t be aligned

- Sufficient number of homologs sequenced

24

---

[← Architecture of TMHMM](02-architecture-of-tmhmm.md) · [Up: contents](index.md) · [Classes of Non-coding RNAs →](04-classes-of-non-coding-rnas.md)
