---
title: Wrapping up E. coli Chemotaxis (L7 & L8)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/09-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Wrapping up E. coli Chemotaxis (L7 & L8)

**Source:** `lectures/09-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**<u>Main points of last 2 lectures:</u>**

**_L7:_** _Biological background_

**what is the function of the individual molecules ?**

**_L8:_** _modeling of all possible chemotactic reactions_

**why doesn’t this model reproduce experimentally observed perfect adaptation ?**

**_L8-9_** _: strip down full model to essentials based on assumptions that are experimentally justified (or sometimes not)_

1


Figure 1A in Mittal, N., E. O. Budrene, M. P. Brenner, and A. Van Oudenaarden. "Motility of Escherichia coli cells in clusters formed by chemotactic aggregation." _Proc Natl Acad Sci U S A_ . 100, no. 23 (Nov 11, 2003): 13259-63.

##### Images removed due to copyright considerations.

3

## Absence of chemical attractant


<!-- Start of picture text -->
Tumble<br>Run<br><!-- End of picture text -->

Image by MIT OCW.

4

# Presence of chemical attractant


<!-- Start of picture text -->
Attractant<br>Tumble<br>Run<br><!-- End of picture text -->

Chemical Gradient Sensed in a Temporal Manner

Image by MIT OCW.

5


Figure 1 of Spiro, P. A., J. S. Parkinson, and H. G. Othmer. "A model of excitation and adaptation in bacterial chemotaxis." _Proc Natl Acad Sci U S A_ 94, no. 14 (Jul 8, 1997): 7263-8.

Copyright (1997) National Academy of Sciences, U. S. A.

key player: Tar-CheA-CheW complex

6


<!-- Start of picture text -->
slow<br>fast<br>intermediate<br><!-- End of picture text -->

Figure 2 of Spiro, P. A., J. S. Parkinson, and H. G. Othmer. "A model of excitation and adaptation in bacterial chemotaxis." _Proc Natl Acad Sci U S A_ 94, no. 14 (Jul 8, 1997): 7263-8.


<!-- Start of picture text -->
First reduction<br>keff4(L)<br>T2p T3p<br>LT2p LT3p<br>keff3(L)<br>kpt<br>kpt<br>keff1(L) keff2(L)<br>keff4(L)<br>T2 T3<br>LT2 LT3<br>keff3(L)<br>1- α α<br>[3]<br>in steady state: α ≡<br>+<br>[2] [3]<br>= −<br>k (1 α)k (L) + αk (L)<br>phos eff1 eff2<br>8<br><!-- End of picture text -->

8


<!-- Start of picture text -->
perfect adaptation for small L<br>safe zone<br>perfect adaptation for large L<br>net phosphorylated rate<br><!-- End of picture text -->

fine-tune: net phoshorylation rate and keff1 and keff2 so that α falls in safe zone 9

9


<!-- Start of picture text -->
no safe zone<br>never perfect adaptation<br><!-- End of picture text -->

10

#### Second reduction


<!-- Start of picture text -->
keff3(L)<br>T2p T3p<br>LT2p LT3p<br>keff4(L)<br>kpt<br>kpt<br>keff1(L) keff2(L)<br>keff3(L)<br>T2 T3<br>LT2 LT3<br><!-- End of picture text -->

#### additional assumption:

- CheB only demetylates phosphorylated receptors

- experimental backup:

- not possible to directly measure if CheB demethylates only active receptors

- rate of methylation drops immediately after addition

11

---

[Up: contents](index.md) · [Third reduction →](02-third-reduction.md)
