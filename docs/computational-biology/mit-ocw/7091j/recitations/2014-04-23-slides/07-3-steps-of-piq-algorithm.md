---
title: 3%Steps%of%PIQ%algorithm%
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3%Steps%of%PIQ%algorithm%

**Source:** `recitations/2014-04-23-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- 1.%Iden,fica,on%of%candidate%sites%using%TF%mo,fs%from%TF% databases%

- 2.%Smoothing%of%raw%reads%from%each%DNase"seq%experiment.% DNase"seq%reads%are%modeled%as%arising%from%a%Gaussian%process%to% remove%noise%by%adap,vely%smoothing%the%reads%from%neighboring% bases%

- 3.%Iden,fy%binding%sites%of%TF%by%itera,vely%combining%direct% evidence%of%binding%(DNase"seq)%with%computer"generated%model% of%DNaseI%hypersensi,vity%that%includes%that%event%(uses%TF" signature%profile%shapes%and%magnitudes%for%each%TF%to%build%a% model%of%the%expected%DNaseI%hypersensi,vity)%

- Use%log"likelihood%ra,o%to%test%each%region%for%TF%binding,%calling% those%above%1%%of%null%distribu,on%as%binary%“bound”%regions%

18

- Pioneer%Transcrip,on%Factors%

- • Region%of%“closed”%chroma,n%that’s%inaccessible%to%most% TFs%can%be%opened%by%pioneer%TF%binding%


###### Zaret)2011)

©  Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Zaret, Kenneth S., and Jason S. Carroll. "Pioneer Transcription Factors: Establishing Competence for Gene Expression." _Genes & Development_ 25, no. 21 (2011): 2227-41.

- Then%once%chroma,n%is%opened,%other%“sebler”%TFs%can% bind%

19

---

[← Transcrip,on%Factor%Binding%](06-transcrip-on-factor-binding.md) · [Up: contents](index.md) · [Iden,fica,on%of%Pioneer%TFs% →](08-iden-fica-on-of-pioneer-tfs.md)
