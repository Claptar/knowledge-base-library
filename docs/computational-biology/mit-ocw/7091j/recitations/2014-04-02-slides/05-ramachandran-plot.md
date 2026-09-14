---
title: Ramachandran Plot
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ramachandran Plot

**Source:** `recitations/2014-04-02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Shows   which   values   of   Ψ   and   Φ   are   possible   for   one   type   (or   more generally,   all)   amino   acids   in   a   protein   –   most   combina'ons   of   Ψ   and Φ   are   forbidden   due   to   steric   hindrance


( **le?** )   Plot   for glycine   –   gly   side group   is   just   -­‐H,   so has   less   restricted conforma'ons   due to   less   steric hindrance


( **right** )   Proline   has an   unusual structure   (amine N   bound   to   2,   not 1   C)   that   restricts its   possible conforma'ons

**General   case   plot** :   uses   data   from   nearly 100,000   residues   from   500   structures (excluding   Gly,   Pro,   and   a.a.   before   Pro)

Courtesy of Jane S. Richardson. License: CC-BY.

8

## Secondary   structure: α-­‐helices   and   β-­‐sheets

Form   due   to   favorable   interac'ons   (hydrogen   bonding)   between molecules   of   the   pep'de   backbone   (not   the   side   chains)


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

9

## Secondary   structure: α-­‐helices   and   β-­‐sheets

Form   due   to   favorable   interac'ons   (hydrogen   bonding)   between molecules   of   the   pep'de   backbone   (not   the   side   chains)


<!-- Start of picture text -->
α-­‐helix<br><!-- End of picture text -->

**β-­‐sheet**


<!-- Start of picture text -->
Hemoglobin<br><!-- End of picture text -->


Courtesy of Jason Koval & Kevin Cartwright. Images in the public domain. Courtesy of Isabella Daidone. Image in the public domain. hRp://en.wikipedia.org/wiki/Beta-­‐sheet

hRp://en.wikipedia.org/wiki/Beta-­‐sheet


© Richard Wheeler. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


<!-- Start of picture text -->
Rhodopsin<br><!-- End of picture text -->

© Andrei Lomize. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/ help/faq-fair-use/.

GFP:   β-­‐barrel

hRp://en.wikipedia.org/wiki/Alpha-­‐helix

hRp://en.wikipedia.org/wiki/Beta_barrel

Courtesy of Christopher King. License: CC-BY.

10

Secondary   structure: α-­‐helices   and   β-­‐sheets

Form   due   to   favorable   interac'ons   (hydrogen   bonding)   between molecules   of   the   pep'de   backbone   (not   the   side   chains) **α-­‐helix**

-­‐If   one   side   of   helix faces   interior   of protein   and   one   faces aqueous   exterior,   the helix   will   likely   be amphipathic (=possesses   both hydrophilic   and hydrophobic proper'es)

Image of helical wheel representation of an amino acid sequence removed due to copyright restrictions.

hRp://lectures.molgen.mpg.de

Ter'ary   structure: side-­‐chain   interac'ons • Helices,   sheets   and   other   secondary   structure   elements   are combined   to   produce   the   complete   structure,   largely through   side   chain   interac'ons   between   amino   acids   that   are far   apart   along   the   pep'de   chain:


- **Disulfide   bridge   (bond)** :   strong covalent   bonds   that   form   between   2 Cysteine   residues   (S-­‐S   bond)

- **Hydrophobic   interac8ons** : hydrophobic   side   chains   tend   to   be packed   away   inside   the   protein, hydrophilic   side   chains   on   the   outside so   H2O   can   form   H-­‐bonds   with   them

- **Interac8ons   between   charged residues** (ionic   bonds)

- **Hydrogen   bonding** between   side chains

© Pearson Education, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

12

.

## Quaternary   Structure:   assembling mul'ple   pep'de   subunits

- Many   proteins   contain   more   than   one   polypep'de   chain (subunits)   which   interact   to   form   the   func'onal   protein – Maintained   by   interchain   interac'ons


© Albion E. Baucom. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

From   Biochemistry.   5th   edi'on.

The   ribosome   consists   of   a   large (orange)   and   small   (green)   protein subunit   (also   contains   RNA)

© W. H. Freeman and Company. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

13

## Protein   structure   computa'onally inferred   through   2   methods


- 1.   X-­‐ray   crystallography   (most common)

   - Crystalline   atoms   cause   a   beam   of incident   X-­‐rays   to   diffract   into   many

      - specific   direc'on

   - Crystallizing   a   protein   is   difficult!

Courtesy of Thomas Splettstößer. Used with Permission.

14

hRp://en.wikipedia.org/wiki/X-­‐ray_crystallography

## Protein   structure   computa'onally inferred   through   2   methods

- 2.   NMR   (nuclear   magne'c   resonance)   spectroscopy:   exploits the   magne'c   proper'es   of   atomic   nuclei

   - Intramolecular   magne'c   field   around   an   atom   in   a   molecule   changes the   resonance   frequency,   giving   access   to   details   of   the   electronic structure   of   a   molecule

   - Usually   limited   to   small   (<35   kDa)   proteins   (more   common   for   small, organic   molecules)

   - Used   for   intrinsically   disordered

   - proteins   or   others   that   can’t   be crystallized

hRp://en.wikipedia.org/wiki/NMR_spectroscopy

> © T.vanschaik. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

15

## Proteins   usually   assume   structures that   minimize   poten'al   energy


####


If   we   could   map   all   possible conforma'ons   of   a   protein onto   2-­‐dimensions   with Poten'al   energy   as   the   3<sup>rd</sup> (z-­‐) dimension,   the   protein   would fold   downward   along   the poten'al   energy   surface   to   the global   minimum

Courtesy of Nature Publishing Group. Used with permission. Source: Dill, Ken A., and Hue Sun Chan. "From Levinthal to Pathways to Funnels." _Nature Structural  Biology_ 4, no. 1 (1997): 10-9.

For   a   par'cular   structure,   how   do   we   compute   its   poten'al   energy?   2   main   approaches: 1.   Physical   explana'on   for   forces   (CHARMM) 2.   Sta's'cal   comparison   of   structure’s   components   to   those   observed   in   other proteins   (RoseRa)

16

---

[← Pep'de chain](04-pep-de-chain.md) · [Up: contents](index.md) · [1. CHARMM (Physicist’s Approach) →](06-1-charmm-physicist-s-approach.md)
