---
title: Variant%Phasing%
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-30-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Variant%Phasing%

**Source:** `recitations/2014-04-30-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Longer%reads%will%help%–%<br>two%SNPs%present%in%the%<br>same%read%are%definitely%on%<br>the%same%chromosome%<br><!-- End of picture text -->

29

### Hardy"Weinberg%Equilibrium%(HWE)%

- Assume%only%two%alleles:%%A%and%a%

- If%P(A)%=%ψ%=%frequency%of%A%in%the%popula,on,% and%the%popula,on%is%in%HWE,%then:%

|– P(AA)%=%ψ<sup>2</sup>|**gamete,**|**A**%(ψ)%|**a**%(1"ψ)%|
|---|---|---|---|
|– P(Aa)%=%2ψ(1"ψ)%|**A**%(ψ)%|**AA**%(ψ<sup>2</sup>)%|**Aa**%(ψ(1"ψ))%|
|– P(aa)%=%(1"ψ)<sup>2</sup>|**a**%(1"ψ)%|**Aa**%(ψ(1"ψ))%|**aa**%((1"ψ)<sup>2</sup>)%|


- HWE%states%that%allele%and%genotype%frequencies% in%a%popula,on%will%be%constant%from%genera,on% to%genera,on%in%the%absence%of%other% evolu,onary%forces;%assuming%the%following:%

   - random%ma,ng%

   - popula,on%size%is%infinite%

   - no%migra,on,%muta,on%or%selec,on%(so%allele% frequencies%won't%change)%

30

### HWE%and%Likelihood%ra,o%tests%

- Tes,ng%whether%a%popula,on%is%in%HWE%using%a% likelihood%ra,o%test%(LRT):%

   - say%we%observe%N%=%200%individuals%with%the%following% genotypes:%% **25** %aa,% **90** %Aa,% **85** %AA%

– is%this%popula,on%in%HWE?%

• Recall%that%the%likelihood%ra,o%is%given%by:% likelihood%of%the%data%under%the%null%model% λ =<sup>_P_</sup><sup><u>(</u></sup><sup>_Data_|</sup><sup>_H_</sup><sup><u>0)</u></sup> likelihood%of%the%data%under%the%alterna,ve% _P_ ( _Data_ | _H_ 1) model%

- Then%the%following%test%sta,s,c%is%approximately%Chi" square%distributed:%

2 −2ln(λ) ~ _Xdf_ – _df_ %=%(#%free%parameters%in%H1)%–%(#%free%parameters%in%H0)%

31

### HWE%and%Likelihood%ra,o%tests%

- We%observe%n%=%200%individuals%with%the%following% genotypes:%% **25** %aa,% **55** %Aa,% **120,** AA% – is%this%popula,on%in%HWE?%

- Here,%under%the%unconstrained%model%H1,%the% parameters%are% _p_ AA,% _p_ Aa%and% _p_ aa%( _df_ %=%2)%

   - for%this%example:%%% _p_ AA%=%120/200%=%0.6,% _p_ Aa%=%55/200%=% 0.275,% _p_ aa%=%25/200%=%0.125%

- Under%the%constrained%model%H0,%we%only%need% _p_ A (frac,on%of%A%alleles%in%popula,on)%and%if%HWE%holds:% – _p_ A%=%(2nAA+nAa)/2n _#_ =%(2(120)%+%55)/400%=%295/400%=%0.7375 – _p_ AA%=%( _p_ A)<sup>2</sup> %=%(0.7375)<sup>2</sup> %=%0.5439%

   - _p_ Aa%=%2 _p_ A%(1" _p_ A)%=%0.3872%

   - – _p_ aa%=%(1" _p_ A)<sup>2%</sup> =%0.0689%


could%also%do%a%Chi"square% goodness%of%fit%test%with%these% probabili,es%*%n%as%the%expected% counts%instead%of%LRT%

32

### HWE%and%Likelihood%ra,o%tests%

- We%observe%N%=%200%individuals%with%the%following% genotypes:%% **25** %aa,% **90** %Aa,% **85** %AA% – is%this%popula,on%in%HWE?%

• Therefore,%our%test%sta,s,c%is:% 2, 2 _<u>pA</u>_ <u>(1−</u> _<u>pA</u>_ <u>),(1−</u> _<u>pA</u>_ <u>)2 )</u> −2ln(λ) = −2ln<sup>_P_</sup><sup><u>(</u></sup><sup>_Data_|</sup><sup>_<u>pA</u>_</sup> _P_ ( _Data_ | _pAA_ , _pAa_ , _paa_ ) = −2ln<sup>_P_</sup><sup><u>(</u></sup><sup>_Data_| 0.5439,0.3872,0.0689)</sup> _P_ ( _Data_ | 0.6,0.275,0.125) • Note%that%P(Data|H)%follows%a%mul,nomial%distribu,on% (generalized%binomial%for%more%than%2%categories):% Note%that%the% _n_ ! _xk_ factorials%will%drop% _P_ ( _x_ 1,..., _xk_ ; _n_ , _p_ 1,..., _pk_ ) = _p_ 1 _x_ 1... _pk x_ 1!,..., _xk_ ! out%of%LRT% So%for%example:% 200! 0.6<sup>25</sup> 0.275<sup>90</sup> 0.125<sup>85</sup> _P_ ( _Data_ | _H_ 1) = _P_ (25,90,85;200,0.6,0.275,0.125) = 25!90!85!

33

### Likelihood%Ra,o%Tests%

- Can%use%a%similar%LRT%to%determine%whether%the%data% are%bener%explained%when%treated%as%two% subpopula,ons,%like%cases%and%controls:%

   - H0:%% _p_ AA,% _p_ Aa%and% _p_ aa%are%sufficient%to%explain%the%data%

   - – H1:%%we%do%bener%by%considering%two%subpopula,ons:% • _p_<sup>_1_</sup> AA<sup>,%</sup><sup>_p1_</sup> Aa<sup>%and%</sup><sup>_p1_</sup> aa<sup>%for%subpopula,on%1%(D1)%</sup> • _p_<sup>_2_</sup> AA<sup>,%</sup><sup>_p2_</sup> Aa<sup>%and%</sup><sup>_p2_</sup> aa<sup>%for%subpopula,on%2%(D2)%</sup>

- Then%our%test%sta,s,c%T%is:%

_P_ <u>(</u> _D_ | _<u>pAA</u>_ <u>,</u> _<u>pAa</u>_ <u>,</u> _<u>paa</u>_ <u>)</u> _T_ = −2ln _P_ ( _D_<sup>1</sup> | _p_ 1 _AA_ , _p_ 1 _Aa_ , _p_ 1 _aa_ ) _P_ ( _D_ 2 | _pAA_ 2 , _pAa_ 2 , _paa_ 2 )

- approx.%Chi"square%distributed%with% _df_ %=%4%–%2%=%2%

34

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 2%types%of%heritability%](06-2-types-of-heritability.md) · [Up: contents](index.md)
