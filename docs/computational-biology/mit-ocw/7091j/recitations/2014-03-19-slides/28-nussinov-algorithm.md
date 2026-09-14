---
title: Nussinov Algorithm
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Nussinov Algorithm

**Source:** `recitations/2014-03-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

||||<br>**_j_**||||||
|---|---|---|---|---|---|---|---|---|
|||A|A<br>|G|U|U|C|G|
||A|0|0|0|1|2|2|3|
|**_i_**|A|0|0|0|1|1|1|1|
|<br>|G||0|0|0|0|1|1|
||U|||0|0|0|0|1|
||U||||0|0|0|1|
|in<br>|C|||||0|0|1|
|<br>hlighted<br>uare:|G||||||0|0|
|_S_(_i_,_j_) = max<br>(i   =   1,j   =   7)|_S_(_i_+<br>_S_(_i_+<br>S(_i_,_j_–<br>max**_i_<**|1,_j_– 1)<br>1,_j_)<br>1)<br>**_k_<****_j_**_S_(_i_,_k_|+1 [if_i_,_j_<br>) +_S_(_k_+|base pai<br>1,_j_)|r]<br>A-­‐G<br>=   1<br>=   2<br>k   =   3:<br>k   =   4:<br>k   =   2:|­‐   don’t   b<br>S(1,3)   +<br>S(1,4)   +<br>S(1,2)   +|­‐      ase   pair<br>S(4,7)   =<br>S(5,7)   =<br>S(3,7)   =|­‐<br>0+1   =   1<br>1+1   =   2<br>0+1   =   1|


Fill   in highlighted square:

k   =   5:   S(1,5)   + S(6,7)   =   2+1   =   3 k   =   6:   S(1,6)   + S(7,7)   =   2+0   =   2

---

[← Nussinov Algorithm](27-nussinov-algorithm.md) · [Up: contents](index.md) · [Nussinov Algorithm -­‐traceback →](29-nussinov-algorithm---traceback.md)
