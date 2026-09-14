---
title: Historical heritability example
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Historical heritability example

**Source:** `lectures/19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Figure is in the public domain.

Galton,   “Regression   towards   mediocrity   in   hereditary   stature”   (1886)

Computa(onal   Analysis   of   QTLs

23

##### **h**<sup>**2**</sup> **-­‐   Narrow   Sense   heritability**

- Frac(on   of   phenotypic   variance   explained   by   an   addi(ve model   of   markers

- fa(gi)   is   addi(ve   model   of   genotypic   components   in   gi

- Difference   between   heritability   explained   by   addi(ve   model and   general   model   is   one   source   of   “missing   heritability”   in current   studies

Computa(onal   Analysis   of   QTLs

24

##### **h**<sup>**2**</sup> **-­‐   Narrow   Sense   heritability**

- Frac(on   of   phenotypic   variance   explained   by   an   addi(ve model   of   markers

- fa(gi)   is   addi(ve   model   of   genotypic   components   in   gi

- Difference   between   heritability   explained   by   addi(ve   model and   general   model   is   one   source   of   “missing   heritability”   in current   studies


<!-- Start of picture text -->
N 2<br>2 2<br>σ a = σ p − 1 ∑<br>pi  = f a ( gi ) + ei i − f  a ( g i ))<br>N i =1 ( p<br>2<br>2 σ a<br>=<br>h<br>2<br>σ p<br><!-- End of picture text -->

Computa(onal   Analysis   of   QTLs

25

**Example   trait   heritabili%es   –   h**<sup>**2**</sup> Morphological   Traits Human   height   ~   .8 CaAle   Yearling   Weight   ~   .35 Fitness   Traits Drosophila   life   history   ~   .2 Wild   animal   life   history   ~   .3

_h_<sup>2</sup> from   Visscher   et   al.   2008

Computa(onal   Analysis   of   QTLs

26

##### **Example   trait   heritabili%es**

_h_<sup>2</sup> from   Visscher   et   al.   2008

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Visscher, Peter M., William G. Hill, et al. "Heritability in the Genomics Era—Concepts

and Misconceptions." _Nature Reviews Genetics_ 9, no. 4 (2008): 255-66.

Computa(onal   Analysis   of   QTLs

27

##### **Today’s   Narra%ve   Arc**

1. Usually,   you   are   more   like   your   rela(ves   than   random   people   on the   planet.

2. The   heritability   of   a   trait   is   the   frac(on   of   phenotypic   variance   that can   be   explained   by   genotype

**3. Computa%onal   models   that   predict   phenotype   from   genotype   are key   for   understanding   disease   related   genomic   variants   and   the most   effec%ve   therapy   for   a   disease   (pharmacogenomics)**

4. We   will   computa(onally   predict   quan(ta(ve   phenotypes   by

   - adding   the   contribu(on   of   individual   loci   (QTLs)

5. Typically   our   models   can   only   predict   a   small   frac(on   of phenotypic   variance   –   the   so   called   “missing   heritability”   problem

28

##### Computa(onal   Analysis   of   QTLs **Can   we   predict   phenotype   in   a   haploid   yeast system?**


Computa(onal   Analysis   of   QTLs

29

##### **Study   heritability   of   46   traits   in   ~1000   segregants**


Key   advance:   large   panel (~1000   segregants),   many phenotypes   (46) BY   and   RM   parents


Bloom   et   al.   2013

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Computa(onal   Analysis   of   QTLs

30

##### **Certain   phenotypes   are   related**

Bloom   et   al.   2013

Ethanol   (2%) Sugars,   etc.


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Computa(onal   Analysis   of   QTLs

31

##### **Today’s   Narra%ve   Arc**

1. Usually,   you   are   more   like   your   rela(ves   than   random   people   on the   planet.

2. The   heritability   of   a   trait   is   the   frac(on   of   phenotypic   variance   that can   be   explained   by   genotype

3. Computa(onal   models   that   predict   phenotype   from   genotype   are key   for   understanding   disease   related   genomic   variants   and   the most   effec(ve   therapy   for   a   disease   (pharmacogenomics)

**4. We   will   computa%onally   predict   quan%ta%ve   phenotypes   by adding   the   contribu%on   of   individual   loci   (QTLs)**

5. Typically   our   models   can   only   predict   a   small   frac(on   of phenotypic   variance   –   the   so   called   “missing   heritability”   problem

Computa(onal   Analysis   of   QTLs

32

##### **LOD   scores   to   discover   QTLs**


<!-- Start of picture text -->
N P<br>p i | g ,µ0,µ ,1 σ<br>( ij )<br>LOD  = log10∏<br>i =1 P<br>( p i | µ,σ )<br><!-- End of picture text -->

- Use   trait   means   condi(oned   on   marker   j   in   individual   vs. uncondi(oned   mean   for   trait   to   test   if   marker   j   is   a   QTL

- • Permute   genotypes   1000   (mes   and   each   (me   compute   LOD   scores to   es(mate   null   LOD   distribu(on

- • Determine   null   LOD   score   that   describes   FDR   =   0.05 • Use   this   threshold   on   unpermuted   LOD   scores   to   find   QTLs   for   each gene

- • Fit   linear   model   to   discovered   QTLs • Repeat   finding   QTLs   predic(ng   residuals   from   exis(ng   model   (3 (mes)

Computa(onal   Analysis   of   QTLs

33

###### **1005   segregants   detect   more   QTLs   than   100   segregants**

Bloom   et   al.   2013

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Computa(onal   Analysis   of   QTLs

34

##### **Phenotype   predic%on   works   well   with iden%fied   QTLs**


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Bloom   et   al.   2013

Computa(onal   Analysis   of   QTLs

35

#### **Most   iden%fied   QTLs   have   small   effects**

5-­‐29   QTLs   per   trait (median   of   12), reported   at   5%   FDR

Bloom   et   al.   2013

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Computa(onal   Analysis   of   QTLs

36

##### **Iden%fied   QTLs   explain   most   addi%ve   heritability**

QTLs   explain 72-­‐100%   of narrow-­‐sense heritability


Bloom   et   al.   2013

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Computa(onal   Analysis   of   QTLs

37

##### **“Missing   Heritability”   exists   with   our   linear   model**

Ver(cal   gap represents non-­‐addi(ve gene(c contribu(ons


Bloom   et   al.   2013


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Computa(onal   Analysis   of   QTLs

38

##### **Today’s   Narra%ve   Arc**

1. Usually,   you   are   more   like   your   rela(ves   than   random   people   on the   planet.

2. The   heritability   of   a   trait   is   the   frac(on   of   phenotypic   variance   that

   - can   be   explained   by   genotype

3. Computa(onal   models   that   predict   phenotype   from   genotype   are key   for   understanding   disease   related   genomic   variants   and   the most   effec(ve   therapy   for   a   disease   (pharmacogenomics)

4. We   will   computa(onally   predict   quan(ta(ve   phenotypes   by

   - adding   the   contribu(on   of   individual   loci   (QTLs)

**5. Typically   our   models   can   only   predict   a   small   frac%on   of phenotypic   variance   –   the   so   called   “missing   heritability” problem**

Computa(onal   Analysis   of   QTLs

39

**What   causes   missing   heritability?** Possible   explana(ons   (non-­‐exclusive):

- Incorrect   heritability   es(mates

- Non-­‐chromosomal   elements

- Rare   variants

- Structural   variants

- Many   common   variants   of   low   effect

- Epistasis

Computa(onal   Analysis   of   QTLs

40

##### **What   causes   missing   heritability?**

###### • Consider

   - f(ab)   =   0

   - f(aB)   =   f(Ab)   =   1

   - f(AB)   =   0

- A   and   B   will   not   be   detected   as   QTLs   as   individually   they   have   no effect   on   phenotype

- Assuming   no   environmental   noise   H<sup>2</sup> =1   and   h<sup>2</sup> =0.

- Non-­‐addi(ve   interac(ons   can   result   from   gene-­‐gene   interac(ons (epistasis)

   - Can   be   more   than   pairwise!

   - Considering   all   combina(ons   of   markers   is   in   general   not   tractable because   of   mul(-­‐hypothesis   limits

- Broad   sense   heritability   includes   addi(ve   gene(c   factors, dominance   effects,   gene-­‐gene   interac(ons,   gene-­‐environment interac(ons,   non   genomic   inheritance

Computa(onal   Analysis   of   QTLs

41

##### **Remaining   sources   of   heritability**

- Gap   between narrow-­‐   and   broad-­‐ sense   heritability implies   gene(c interac(ons

- For   most   traits,   gaps not   explained   by found   pairwise interac(ons

- Excep(on:   maltose (71%   of   gap explained   by   one pairwise   interac(on)


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

Computa(onal   Analysis   of   QTLs

42

Non-­‐linear   models   reveal   missing   heritability   from   the interac(on   of   chromosomal   and   non-­‐chromosomal   elements


Courtesy of Edwards et al. Used with permission. Source: Edwards, Matthew D., Anna Symbor-Nagrabska, et al. "Interactions Between Chromosomal and Nonchromosomal Elements Reveal Missing Heritability." _Proceedings of the National Academy of Sciences_ 111, no. 21 (2014): 7719-22.

Computa(onal   Analysis   of   QTLs

43

##### **Recent   context**

**Problem** :   missing   heritability   for   human   diseases   auer hundreds   of   GWAS   studies

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Manolio, Teri A., Francis S. Collins, et al. "Finding the Missing Heritability of Complex Diseases." _Nature_ 461, no. 7265 (2009): 747-53.

“Found” _h_<sup>2</sup> from   Manolio   et   al.   2009

Computa(onal   Analysis   of   QTLs

44

##### **Discovering   what   is   missing**

- Use   other   data   to   determine   relevance   of markers   (SNPs   in   enhancers,   non-­‐sense muta(ons,   etc.)   to   reduce   marker   search   space

- • When   relevant   marker   space   is   simplified   can consider   non-­‐linear   interac(ons

- Consider   non-­‐chromosomal   gene(c   elements

- • Use   complementary   data   to   determine   marker interac(ons   (protein-­‐protein   interac(on   data, etc.)

- Your   research   goes   here!

Computa(onal   Analysis   of   QTLs

45

# **FIN**

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← H2 -­‐ Broad Sense heritability](09-h2---broad-sense-heritability.md) · [Up: contents](index.md)
