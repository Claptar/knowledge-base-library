---
title: Outline%
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Outline%

**Source:** `recitations/2014-04-23-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Chroma,n%Structure%

- Dynamic%Bayesian%Networks%/%Segway%

- DNAse"seq%&%Protein%Interac,on%Quan,ta,on% (PIQ)%

- ChIA"PET%reveals%3D%interac,ons%in%the%genome%

3

### Introduc,on%to%Chroma,n%

- DNA%in%one%cell%is%3%meters%long,%yet%fits%into%a%,ny%nucleus%

- To%facilitate%the%packaging,%DNA%is%wrapped%around%nucleosomes,% and%this%fiber%is%wrapped%into%higher%order%structures%up%to%the%level% of%a%chromosome%

   - “chroma,n”%refers%to%the%structure%of%DNA%+%nucleosomes%

   - Each%nucleosome%is%an%octamer%composed%of%4%pairs%of%different%histone%proteins:%H2A,% H2B,%H3,%and%H4


- © Pearson Education, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Courtesy of the Broad Institute. Used with permission. The most recent best practicesBroad Institute. Used with permission. The most recent best practices. Used with permission. The most recent best practices

Courtesy of the Broad Institute. Used with permission. The most recent best practicesBroad Institute. Used with permission. The most recent best practices. Used with permission. The most recent best practices can be found at this website: https://www.broadinstitute.org/gatk/guide/best-practices.

hbp://www.mun.ca/biology/desmid/brian/BIOL2060/ BIOL2060"18/1820.jpg%

hbps://www.broadins,tute.org/files/news/images/2010/ chroma,n_states_2a.png%

4

### Histone%modifica,ons%

###### – Par,cular%residues%on%the%tails%of%these%histones%commonly%undergo% post"transla,onal%chemical%modifica,ons%


hbp://a.sta,c"abcam.com/CmsMedia/ Media/common"histone"modifica,on"1.jpg%

© Abcam. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

– Some%of%these%modifica,ons%are%associated%with%func,ons%–%different% combina,ons%of%marks%and%their%meaning%compose%the%“histone%code”% <u>| y</u>

Most% common% in%papers%

|Histone modification<br>or variant|Signal<br>characteristics|Putative functions|
|---|---|---|
|H2A.Z|Peak|Histone protein variant (H2A.Z) associated with regulatory elements with dynamic chromatin|
|H3K4me1|Peak/region|Mark of regulatory elements associatedwithenhancersand otherdistalelements,but alsoenricheddownstream oftranscription starts|
|H3K4me2|Peak|Mark of regulatory elements associated with promoters and enhancers|
|H3K4me3|Peak|Mark of regulatory elements primarily associated with promoters/transcription starts|
|H3K9ac|Peak|Mark of active regulatory elements with preference for promoters|
|H3K9me1|Region|Preference for the 59end of genes|
|H3K9me3|Peak/region|Repressive mark associated with constitutive heterochromatin and repetitive elements|
|H3K27ac|Peak|Mark of active regulatory elements; may distinguish active enhancers and promoters from their inactive counterparts|
|H3K27me3|Region|Repressive mark established by polycomb complex activity associated with repressive domains and silent developmental genes|
|H3K36me3|Region|Elongation mark associated with transcribed portions of genes, with preference for 39regions after intron 1|
|H3K79me2|Region|Transcription-associated mark, with preference for 59end of genes|
|H4K20me1|Region|Preference for 59end of genes|


~~ENCODE%Consor,um~~<sup>~~%~~</sup> _~~Nature~~_ ~~%2012%~~

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: ENCODE Project Consortium. "An Integrated Encyclopedia of DNA Elements in the Human Genome." _Nature_ 489, no. 7414 (2012): 57-74.

5

##### Histone%code%&%DNA%methyla,on%regulate%gene%expression%

- In%addi,on%to%histone%modifica,ons,%gene% expression%can%be%affected%by%DNA%methyla,on:% the%5%carbon%of%cytosines%in%DNA%can%be% methylated.%

   - In%metazoans,%only%C’s%before%G’s%can%be%methylated% (the%C’s%of%CpG).%Hundred%or%thousands%of%base"long% stretches%rich%in%methylated%cytosines%form%“CpG% islands”%at%some%promoters%to%repress%gene%expression%

- “Epigene,c”%changes%are%changes%to%DNA%not%at% the%level%of%primary%sequence%which%are% reversible%&%heritable%

- Epigene,c%marks%are%ohen%cell"type%and/or% disease%state"specific%

   - For%example,%the%pluripotency%gene% _Nanog_ %is%% %demethylated%during%reprogramming%of%differen,ated% %cells%into%iPSCs%

- Enzymes%ac,vely%regulate%the%epigene,c%marks%

   - Chroma,n%modifiers%and%nucleosome%remodelers%are%enzymes% that%ac,vely%regulate%chroma,n%marks,%nucleosome%posi,oning%&% turnover%

   - DNA%methyltransferases%to%methylate%DNA%


Courtesy of Macmillan Publishers Limited. Used with permission.

6

---

[← Announcements%](02-announcements.md) · [Up: contents](index.md) · [Profiling%histone%modifica,ons% →](04-profiling-histone-modifica-ons.md)
