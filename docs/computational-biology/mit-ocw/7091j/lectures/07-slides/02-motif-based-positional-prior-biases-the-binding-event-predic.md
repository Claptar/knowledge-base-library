---
title: Motif-based positional prior biases the binding event prediction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Motif-based positional prior biases the binding event prediction

**Source:** `lectures/07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Mixture model<br>1 2<br>M  Possible<br>events<br>b<br>m<br>N  Observed rn<br>reads<br>N M M<br>π  m ( n m = 1<br>p ( R  | π) = ∏∑ p r |  m ), ∑π<br>n =1 m =1 m =1<br><!-- End of picture text -->

###### **<mark>Position</mark> -** **<mark>specific</mark> priors**

- **Events are sparse**


<!-- Start of picture text -->
• Events occurs more likely at motif<br>positions<br>M<br>( ) (π  m )−α s  +α m<br>p π ∝ ∏<br>m =1<br><!-- End of picture text -->

- **_αs_ : uniform sparse prior parameter governing**

- **the degree of sparseness,** **_αs_ >0;** **_αm_ : position specific motif-based prior**

33

##### GEM improves in resolving joint binding events


###### **(Human GABP Data : Valouev et al., 2008)**

###### **TF A TF A**


Courtesy of PLoS Computational Biology. License: CC-BY. Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." _PLoS Computational Biology_ 8, no. 8 (2012): e1002638.

34

#### GEM improves spatial accuracy in binding event prediction


<!-- Start of picture text -->
100 100<br>80 80 GEM<br>GPS<br>GEM SISSRS<br>60 60<br>GPS MACS<br>SISSRS cisGenome<br>40 40<br>MACS QuEST<br>cisGenome FindPeaks<br>20 20<br>QuEST spp_wtd<br>PeakRanger spp_mtc<br>0 0<br>0 20 40 60 80 100 0 20 40 60 80 100<br>Spatial resolution (distance from GABP motif, bp) Spatial resolution (distance from CTCF motif, bp)<br>) )<br>% %<br> (  (<br>n n<br>o o<br>ti ti<br>c c<br>a a<br> fr  fr<br>e e<br>v v<br>ti ti<br>alu alu<br>m m<br>u u<br>C C<br><!-- End of picture text -->

**(Human GABP Data Valouev et al., 2008)**

**(Mouse CTCF data Chen , et. al. 2008)**


###### **Motif**

###### **Event call**

Courtesy of PLoS Computational Biology. License: CC-BY. Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." _PLoS Computational Biology_ 8, no. 8 (2012): e1002638.

35

#### GEM improves the spatial resolution of ChIP-exo data event prediction


<!-- Start of picture text -->
0.015 GEM initial distribution<br>GEM learned distribution<br>CTCF empirical distribution<br>0.01<br>0.005<br>0<br>-300 -200 -100 0 100 200 300<br>Stranded location with respect to binding site (bp)<br>Read density<br><!-- End of picture text -->


<!-- Start of picture text -->
Motif  Event call<br><!-- End of picture text -->

###### **(Rhee and Pugh, 2011)**

Courtesy of PLoS Computational Biology. License: CC-BY. Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." _PLoS Computational Biology_ 8, no. 8 (2012): e1002638.

36

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [GEM reveals transcription factor spatial binding constraints →](03-gem-reveals-transcription-factor-spatial-binding-constraints.md)
