---
title: Nussinov Algorithm -­‐traceback
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Nussinov Algorithm -­‐traceback

**Source:** `recitations/2014-03-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

||||**_j_**||||||
|---|---|---|---|---|---|---|---|---|
|||A|A<br>|G|U|U|C|G|
||A|0|0|0|1|**2**|2|**3**|
|**_i_**|A|0|0|0|**1**|1|1|1|
|<br>|G||0|0|0|0|1|1|
||U|||0|0|0|0|1|
||U||||0|0|0|1|
||C|||||0|0|**1**|
||G||||||0|0|


start   here

Can   you   draw   this   folded   RNA?


G

U A A U C   G


- -­‐   note   that   in   reality,   stems   can’t form   if   the   loop   is   less   than   3bp due   to   restric'ons   on   backbone angles

- Improvements   on   Nussinov   algorithm

- • Nussinov   is   the   “core”   of   most   RNA   folding   programs,   but they   all   have   bells   &   whistles

   - Take   into   account   that   loop   must   be   3   or   more   nucleo'des

   - Not   all   base   pairs   are   equal   in   reality   (we   treated   them   all   at   +1   in   Nussinov)

   - Base   stacking   interac'ons

      - base **pairing** :


<!-- Start of picture text -->
G     A     G<br>> ><br>C     U     U<br><!-- End of picture text -->

- base **stacking** :


<!-- Start of picture text -->
G p A<br>| |<br>C p U<br><!-- End of picture text -->

#### Base stacking contributes more


© source unknown. All rights reserved. This content is excluded from our Creaative to free energy than base pairing Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

35

- Improvements   on   Nussinov   algorithm

- • Nussinov   is   the   “core”   of   most   RNA   folding   programs,   but they   all   have   bells   &   whistles

   - Take   into   account   that   loop   must   be   3   or   more   nucleo'des

   - Not   all   base   pairs   are   equal   in   reality   (we   treated   them   all   at   +1   in   Nussinov)

   - Base   stacking   interac'ons

   - Penalizes   interior   bulges

   - Extra   terms   at   terminal   ends   of   RNA   exposed   to   solvent

   - -­‐Nussinov   algorithm   cannot   detect   pseudoknots,   since   these   do   not   sa'sfy   the   recursive assump'on   that   each   structure   can   be   split   into   smaller   self-­‐contained   sub-­‐structures   -­‐ more   advanced   algorithms

   - With   all   these   addi'ons,   mfold   gets   ~70%   of   bases   correctly   folded;   preYy   good   on average   but   would   likely   want   to   do _in   vivo_ structure   profiling   of   your   RNA   if   you   really want   to   know   its   structure

36

---

[← Nussinov Algorithm -­‐traceback](29-nussinov-algorithm---traceback.md) · [Up: contents](index.md) · [Happy Spring Break! →](31-happy-spring-break.md)
