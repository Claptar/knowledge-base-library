---
title: Haploid,%unlinked%gene,c%model%
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-30-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Haploid,%unlinked%gene,c%model%

**Source:** `recitations/2014-04-30-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- N%loci%that%each%contribute%equally%(1/N)%to%the%trait%

- Haploid%=%organism%has%1%copy%of%each%allele%

- Unlinked%=%loci%are%on%different%chromosomes%or%far%enough%apart%on%the%same% chromosome%so%crossing%over%(recombina,on)%can%always%occur%

   - Each%locus%is%therefore%inherited%independently%

- Child%randomly%inherit <mark>s%maternal%or%p</mark> aternal%c <mark>opy%</mark>


<!-- Start of picture text -->
1+ 2+ N+ 1+ 2+ N+<br>X+<br>Effect+ 0+ 0+ 0+ 1/ N+ 1 /N+ 1/N+<br>Size+<br>Example+Ph<br>1+ 2+ N+<br>+Grow<br>! $<br>Binomial%model%of%#%of%black%<br>p ( x ,  N ) = N<br>alleles%x%inherited:%<br>x<br>" # % &(1−.5) N − x .5 x<br>Here%x%is%the%phenotypic%<br>E [ x ] = .5<br>value%from%0%(no%alleles)%<br>© cflm on wikipedia. Some rights reserved. License:cflm on wikipedia. Some rights reserved. License: on wikipedia. Some rights reserved. License:<br>CC-BY-SA. This content is excluded from our Creative<br>to%1%(all%black%alleles)% 2 = .25 /  N<br>σ  x Commons license. For more information, see<br><!-- End of picture text -->

Binomial%model%of%#%of%black% alleles%x%inherited:% Here%x%is%the%phenotypic% value%from%0%(no%alleles)% to%1%(all%black%alleles)%

- © cflm on wikipedia. Some rights reserved. License:cflm on wikipedia. Some rights reserved. License: on wikipedia. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

5

## Situa,on%is%more%complex%if%loci%are%linked%

Gene(c+linkage+causes+marker+correla(on+


<!-- Start of picture text -->
1+ 1+ N\1+ 1+ 1+ N\1+<br>X+<br>Proximal+<br>1+ 1+ N\1+<br>genomic+<br>loca(ons+makes+<br>crossing+over+<br>unlikely+during+<br>meiosis+<br><!-- End of picture text -->

"%Assump,on%that%each%allele%is%inherited%independently%no%longer% holds%–%models%more%complex%than%binomial%needed%to%capture%this% dependence%

6

## Genotype%–%Phenotype%interac,ons%

- i+–+individual+in+[1+..+N]+

- gi+–+genotype+of+individual+i+

• pi+–+quan(ta(ve+phenotype+of+individual+i+(single+trait)+ • ei+–+environmental+contribu(on+to+pi

_ei_<sup>_~~p~~_</sup> _i_<sup>=</sup><sup>_f_(</sup><sup>_g_</sup> _i_<sup>)+</sup>

Phenotype%is%a%func,on%of%genotype%plus% an%environmental%component%

2 _E E e_ 2 σ _e_ [ _ei_ ]<sup>= 0</sup> !" #$=

Environmental%component%is%unbiased%but% introduces%noise%from%genotype%to%phenotype%

2 2 2 2 2 2 2 σ _p_<sup>=</sup> σ _g_<sup>+</sup> σ _e_<sup>+ 2</sup> σ _ge_ ! σ _p_<sup>=</sup> σ _g_<sup>+</sup> σ _e_

Assume%environment%affects%all%genotypes%equally%">%g% and%e%are%independent%and%their%covariance%is%0%

7

All%phenotypic%varia,on% Environmental% Heritable%gene,c%varia,on% varia,on% (Broad"sense%heritability%H<sup>2</sup> )%

Addi,ve%gene,c% varia,on% Non"addi,ve% (Narrow"sense% gene,c%varia,on% heritability%h<sup>2</sup> )% Gene" Dominance% Gene"gene% environment% interac,ons% effects% interac,ons%

8

---

[← Genotype%to%Phenotype%](04-genotype-to-phenotype.md) · [Up: contents](index.md) · [2%types%of%heritability% →](06-2-types-of-heritability.md)
