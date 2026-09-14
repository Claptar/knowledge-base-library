---
title: Role of ligand binding
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/07-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Role of ligand binding

**Source:** `lectures/07-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Image removed due to copyright considerations.

The rate of CheA phosphorylation is stimulated by unoccupied receptors


Image by MIT OCW. After figure 4 in Falke, J. J., R. B. Bass, S. L. Butler, S. A. Chervitz, and M. A. Danielson. "The

```
why is this all so complex ?
```


<!-- Start of picture text -->
add  add more remove<br>attractant attractant  attractant<br>1 2 3 4<br>tumbling<br>methylation<br><!-- End of picture text -->

Correlation of Receptor Methylation with Behavioral Response

###### Image by MIT OCW.

methylation is important for adaptation (~ background subtraction)

_E. coli_ can sense aspartate from 10 nM - 1 mM and sense changes as small as 0.1%

Before starting with the modeling, first let’s look at some recent experiments

Alon et al. Nature **397** ,168 (1999) Cluzel et al. Science **287** , 1652 (2000) Sourjik et al., PNAS **99,** 123 (2002) PNAS **99** , 12669 (2002) Nature **428** , 439 (2004)

Remember scientists have been working on _E. coli_ chemotaxis for about 100 years now

Image removed due to copyright considerations. See figure 1 in Cluzel, P., M. Surette, and S. Liebler. "An ultrasensitive bacterial motor revealed by monitoring signaling proteins in single cells." _Science_ 287, no. 5458 (Mar 3, 2000): 1652-5.

```
Single cell chemotacticanalysis
```

##### **correlation CW bias & CheY-P gene expression**

cells have plasmids with CheY-GFP under inducible promoter assumption: all CheY is phosphorylated

strain: CheY-, CheZ-, CheB-

##### Hill #: ~10

Image removed due to copyright considerations. See figure 1 in Cluzel, P., M. Surette, and S. Liebler. "An ultrasensitive bacterial motor revealed by monitoring signaling proteins in single cells." _Science_ 287, no. 5458 (Mar 3, 2000): 1652-5.


low YFP/CFP: unbound high YFP/CFP: bound

FRET (fluorescence resonant transfer)

Figures 1A, 1B in Sourjik, V., and H. C. Berg. "Binding of the Escherichia coli response regulator CheY to its target measured in vivo by fluorescence resonance energy transfer." _Proc Natl Acad Sci U S A_ 99, no. 20 (Oct 1, 2002): 12669-74.

CheY-YFP (yellow) CheZ-CFP (blue

CheZ binds only to CheYp !!

adding attractant leads to immediate lower concentration of CheYp-CheZ complex, lower [CheYp], less tumbling


Figures 1A and 1B in Sourjik, V., and Berg HC. "Receptor sensitivity in bacterial chemotaxis." _Proc Natl Acad Sci U S A_ 99, no. 1 (Jan 8, 2002): 123-7.


Figure 2 in Sourjik, V., and Berg HC. "Receptor sensitivity in bacterial chemotaxis." _Proc Natl Acad Sci U S A_ 99, no. 1 (Jan 8, 2002): 123-7.

Hill # ~ 1


Figure 2 in Sourjik, V., and Berg HC. "Receptor sensitivity in bacterial chemotaxis." _Proc Natl Acad Sci U S A_ 99, no. 1 (Jan 8, 2002): 123-7. Copyright (2002) National Academy of Sciences, U. S. A.

amplification between receptors and CheYp: ~35 amplification between CheYp and motor: ~10 total amplification ~ 350 our models should reproduce this (hint: receptor clustering)

```
perfect
adaptation
```

###### **`excitation(fast)`**

**`adaptation slow`** Figures 1a and 1 b in Sourjik, V., and Berg HC. "Receptor sensitivity in bacterial chemotaxis." _Proc Natl Acad Sci U S A_ 99, no. 1 (Jan 8, 2002): 123-7.

Copyright (2002) National Academy of Sciences, U. S. A.

Models should also reproduce

qualitative properties such as perfect adaptation

Images removed due to copyright considerations. See Figure 1 in Alon, U., M. G. Surette, N. Barkai, and S. Leibler. "Robustness in bacterial chemotaxis." _Nature_ 397, no. 6715 (Jan 14, 1999): 168-71.

Perfect adaptation is robust against changes in Che-protein concentrations

Images removed due to copyright considerations. See Figure 2 in Alon, U., M. G. Surette, N. Barkai, and S. Leibler. "Robustness in bacterial chemotaxis." _Nature_ 397, no. 6715 (Jan 14, 1999): 168-71.

Goal of next lecture is develop models that qualitatively and quantitative reproduce these phenomena, such as:

huge gain sensitivity perfect adaptation

All these effects are ubiquitous in signal transduction pathways in general.

‘Fine tuned model for perfect adaptation’

Spiro et al. PNAS **94** , 7263-7268 (1997) A model of excitation and adaptation in bacterial chemotaxis


Figure 1 of Spiro P. A., J. S. Parkinson, and H. G. Othmer. "A model of excitation and adaptation in bacterial chemotaxis." _Proc Natl Acad Sci U S A_ 94, no. 14 (Jul 8, 1997): 7263-8. Copyright (1997) National Academy of Sciences, U. S. A.

key player: Tar-CheA-CheW complex

---

[← Methylation - Phosphorylation coupling](13-methylation---phosphorylation-coupling.md) · [Up: contents](index.md) · [assumptions →](15-assumptions.md)
