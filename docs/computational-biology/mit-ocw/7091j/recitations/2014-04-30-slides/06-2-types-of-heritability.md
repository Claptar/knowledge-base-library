---
title: 2%types%of%heritability%
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-30-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2%types%of%heritability%

**Source:** `recitations/2014-04-30-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Broad"sense%(H<sup>2</sup> )%and%narrow"sense%(h<sup>2</sup> )%

- Broad"sense%

– Frac,on%of%phenotypic%variance%explained%by%gene,c% components% 2 2 2 Can%be%es,mated%from% 2 σ _<u>g</u>_ σ _<u>p</u>_<sup>−</sup> σ _e_ iden,cal%twins%or%clones% = _H_<sup>=</sup> 2 2 Can%be%observed%from%all% σ σ _p p_ individuals%in%popula,on%

   - The%upper%bound%for%phenotypic%predic,on%by%op,mal% arbitrary%(not%necessarily%linear)%model%

- Narrow"sense%

   - The%upper%bound%for%phenotypic%predic,on%by% _linear_ model%(=%frac,on%of%total%phenotypic%variance%that%is% caused%by%the%addi,ve%effects%of%genes)%

   - Determines%the%resemblance%of%offspring%to%their%parents% and%the%popula,on’s%evolu,onary%response%to%selec,on%

9

## Narrow"sense%heritability%(h<sup>2</sup> )%is%the% regression%(slope)%of%offspring%on%parents%


<!-- Start of picture text -->
h 2 ��� h 2 ��� h 2 ���<br>offspring  offspring  offspring<br>parents  parents  parents<br><!-- End of picture text -->

   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- " Regression%slope%is:%Cov(x,y)/Variance(x)%or%Cov(parents,%offspring)/Variance(parents)% " x%is%the%“mid"parent”%

- " The%higher%the%slope,%the%bener%the%offspring%resemble%their%parents.%

- " In%other%words,%the%higher%the%heritability,%the%bener%the%offspring%trait%values%are%predicted% by%parental%trait%values.%

hnp://content.csbs.utah.edu/~rogers/ant5221/lecture/QTs2.pdf%

10

## Narrow"sense%heritability:% addi,ve%model%of%phenotype%

- gi,j%is%a%binary%{0,1}%variable%of%QTL%j%in%individual%i%

- Each%QTL%in%the%genotype%contributes%independently%&% linearly%to%the%phenotype:%

> <sup>_f_</sup> _a_<sup>(</sup><sup>_g_</sup> _i_<sup>) =</sup> ∑ β _jgij_ + β0 _j_ ∈ _QTL_

- βj%is%the%effect%of%QTL%j%on%the%phenotype%(higher%">%QTL% has%greater%impact)%


<!-- Start of picture text -->
• For%addi,ve%markers,%chil dren%are %e xpected %to%be%the%<br>midpoint%of%their%parents%since%they%get%an%average%of%½%<br>loci%from%each%parent:%<br>f a ( p 1) f a ( p 2)<br>E +<br>!" f a ( g i ) #$=<br>2 2<br><!-- End of picture text -->

11

## Narrow"sense%heritability:% addi,ve%model%of%phenotype%

> <sup>_f_</sup> _a_<sup>(</sup><sup>_g_</sup> _i_<sup>) =</sup> ∑ β _jgij_ + β0 _j_ ∈ _QTL N_ 2 2 2

> <sup>_p_</sup> _i_<sup>=</sup><sup>_f_</sup> _a ei_ σ _a_<sup>=</sup> σ _p_<sup>−1</sup> ~~<u>∑(</u>~~<sup>_<u>p</u>_−</sup> _i f a_<sup>(</sup><sup>_g_</sup> _i_<sup>)</sup> )

> <sup>(</sup><sup>_g_</sup> _i_<sup>)+</sup> _~~N~~ i_ =1 Addi,ve%gene,c% variance% 2 ~~2~~ <u>σ</u> _a_ Total%phenotypic% Variance%that%remains% Narrow"sense% _<u>h</u>_<sup>~~=~~</sup> variance% aVer%linear%model%–%one% 2 heritabilit ~~y:%~~ source%of%“missing”% σ _p_ heritability%in%studies%

12

Using%LOD%scores%to%discover%QTLs%for% a%trait%(e.g.%gene%expression)% _N P_<sup>_p_</sup> _i_<sup>|</sup> _g_ ,µ0,µ ,1 σ _ij_ <u>( )</u> _LOD_ = log10∏ LOD%=%Logarithm%of%the%ODds _i_ =1 _P_<sup>_p_</sup> _i_<sup>| µ,σ</sup> ( )

LOD%=%Logarithm%of%the%ODds _i_ %=%individual%


“Null”%model:%locus%does%not%affect%gene’s%expression,%and%the%probability%of%expression%value%pi simply%follows%a%Normal(μ,σ<sup>2</sup> )%distribu,on%

“Alterna,ve”%model:%locus%affects%a%gene’s%expression%(is%a%QTL),%and%there%are%different%mean% expression%values%μ0%and%μ1%depending%on%which%genotype%is%present%at%the%locus%(if%gij=0%or%1)%

- " If%the%alterna,ve%model%(that%the%locus%is%a%QTL%for%the%gene)%doesn’t%explain%the%expression% values%any%bener%than%the%null%model,%the%probability%ra,os%are%1%and%the%LOD%score%is%0% " If%alterna,ve%model%bener%explains%the%data,%LOD%score%>%0%

- " If%the%locus%is%a%QTL,%the%LOD%score%will%get%higher%with%increasing%number%of%individuals%( _N_ )%–% with%larger%sample%samples%we%have%greater%power%to%detect%loci%as%being%sta,s,cally% significant%QTLs.%This%is%referred%to%as%“power”%–%a%study%with%too%few%people%to%determine% sta,s,cal%significance%at%some%loci%is%“underpowered”.%

13

Using%LOD%scores%to%discover%QTLs%for% a%trait%(e.g.%gene%expression)% _N P_<sup>_p_</sup> _i_<sup>|</sup> _g_ ,µ0,µ ,1 σ _ij_ <u>( )</u> _LOD_ = log10∏ _i_ =1 _P_<sup>_p_</sup> _i_<sup>| µ,σ</sup> ( )

- How%to%determine%if%a%LOD%score%is%significant?% " Permute%genotypes%(so%the%marker%gij%and%expression%values%are%mixed%up)%1000% ,mes%and%compute%LOD%scores%to%get%empirical%null%distribu,on%

   - " Determine%the%null%LOD%score%that%corresponds%to%FDR%=%0.05%

   - " Use%this%threshold%on%unpermuted%LOD%scores%to%find%QTLs%for%each%gene%

   - " Since%all%loci%are%included%in%the%permuted%null%distribu,on,%no%mul,ple%hypothesis% correc,on%needed%

- Fit%a%linear%model%to%discovered%QTLs%to%determine%each%QTL’s%contribu,on%(βj)%

- " Once%this%has%been%done%to%find%the%set%of%sta,s,cally%significant%QTLs%from%the%first% pass,%you%can%repeat%to%find%QTLs%in%the%residuals%from%the%exis,ng%model%that%may%have% been%below%the%threshold%in%the%first%pass%(3%,mes)%

14

#### Bloom%et%al.%2013:%“Finding%the%sources%of%missing% heritability%in%a%yeast%cross”%

##### • 5"29%QTLs%per%trait%(median%of%12),%although%most%QTLs%have% small%effect%size%


Absolute%value%of%normalized% difference%in%means%between% genotypes%

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

15

#### Bloom%et%al.%2013:%“Finding%the%sources%of%missing% heritability%in%a%yeast%cross”%

##### • Good%news:%most%addi,ve%heritability%(narrow"sense)%is% explained%by%detected%QTLs%


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

16

#### Bloom%et%al.%2013:%“Finding%the%sources%of%missing% heritability%in%a%yeast%cross”%

##### • Bad%news:%There%is%s,ll%much%heritability%missing%from%our% addi,ve%linear%model%


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bloom, Joshua S., Ian M. Ehrenreich, et al. "Finding the Sources of Missing Heritability in a Yeast Cross." _Nature_ 494, no. 7436 (2013): 234-7.

17

#### Bloom%et%al.%2013:%“Finding%the%sources%of%missing% heritability%in%a%yeast%cross”%

- What%could%cause%the%missing%heritability?%

   - Incorrect%heritability%es,mates%

   - Rare%variants%that%the%study%is%underpowered%to%detect%

   - Structural%variants%(inser,ons%or%dele,ons%–%these%studies%typically%only% measure%SNPs)%

   - Epigene,c%interac,ons%

   - Epista,c%effects%

      - When%the%effect%of%a%gene%depends%on%the%presence%of%one%or%more%modifier%genes%(the% gene,c%background)%

      - Example:%locus%A%and%locus%B%each%only%cause%a%5%%decrease%if%one%of%the%variants%is% present,%but%a%50%%decrease%if%both%are%present%

      - Since%all%pairwise%interac,ons%is%too%large%of%a%search%space%(100,000%x%100,000),%can%only% consider%all%interac,ons%that%involve%at%least%of%the%detected%QTLs%(20%x%100,000)%

18

### Human%Gene,cs%

   - We%want%to%find%human%variants%(SNPs,%etc.)%that%are% associated%with%a%par,cular%phenotype%(e.g.%a%disease)%

- “Manhanan%plot”%

hnp://www.nature.com/ng/journal/v44/n4/ images/ng.1109"F1.jpg


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Tanikawa, Chizu, Yuji Urabe, et al. "A Genome-wide Association Study Identifies Two Susceptibility Loci for Duodenal Ulcer in the Japanese Population." _Nature Genetics_ 44, no. 4 (2012): 430-4.

- We%need%a%way%to%test%whether%a%SNP%is%significantly% associated%with%a%phenotype:%

   - Chi"squared%test%

      - Asympto,c%approxima,on,%so%not%appropriate%if%counts%are%small%(should%be%at% least%5%counts%per%category)%

   - Fisher's%exact%test%

      - An%“exact”%calcula,on%(not%asympto,c%approxima,on),%but%involved%factorials% so%computa,onally%difficult%when%counts%become%large%(but%this%is%exactly% when%the%Chi"square%test%is%appropriate)%

19

### Tes,ng%for%SNP/phenotype%associa,on%

- Tes,ng%for%associa,on%between%a%SNP%and%a%disease%(or% some%other%trait)%–%we%are%given%the%following%counts:%

|Allele%|**Cases,**|**Controls,**|Total%Counts%|
|---|---|---|---|
|**C,**|62%|80%|142%|
|**A,**|108%|250%|358%|
|Total%Counts%|170%|330%|500%|


- Calculate%expected%counts%under%null%hypothesis%that%the%propor,on/ ra,o%of%cases%to%controls%is%the%same%regardless%of%whether%an% individual%is% **C** %or% **A** :%

   - 1)%%calculate%total%propor,on%of% **cases** %regardless%of%A/C%=%170/500%=%0.34%

   - 2)%%calculate%what%propor,on%of%the%142% **C** s%should%be% **cases** %according%to%the%total% propor,on%of% **cases** %=%142(0.34)%=%48.28,% **controls,** =%142(1"0.34)%=%93.72%

   - 3)%%same%for%the% **A** s:%%what%propor,on%of%the%358% **A** s%should%be%cases/controls% according%to%null%model?%

for% **A** %individuals,%expected% **cases** %=%358(0.34)%=%121.72,% **controls,** =%358(1"0.34)=236.28%%

20

### Tes,ng%for%SNP/phenotype%associa,on%

- Tes,ng%for%associa,on%between%a%SNP%and%a%disease%(or% some%other%trait)%–%we%are%given%the%following%counts:%

###### **Observed,**

|Allele%|**Cases,**|**Controls,**|Total%Counts%|
|---|---|---|---|
|**C,**|62%|80%|142%|
|**A,**|108%|250%|358%|
|Total%Counts%|170%|330%|500%|


###### **Expected,**

Allele% **Cases, Controls,** Total%Counts% **C,** 48.28% 93.72% 142% Using%a% **A,** 121.72% 236.28% 358% Chi"squared% Total%Counts% 170% 330% 500% test:% _n_ <u>(</u> _Oi_ − _Ei_ <u>)</u><sup>2</sup> _X_<sup>2</sup> = =<sup><u>(62 −</u>48.28)2</sup> +<sup><u>(80 −</u>93.72)2</sup> +<sup><u>(108</u>−121.72)2</sup> +<sup><u>(250 −</u>236.28)2</sup> = 8.25 ∑ _i_ =1 _Ei_ 48.28 93.72 121.72 236.28 _df_ %=%(#%rows%"1)(#%cols%–%1)%=%1

21

### Tes,ng%for%SNP/phenotype%associa,on%

Chi-Square Distribution Table

hnp://sites.stat.psu.edu/~mga/401/ tables/Chi"square"table.pdf%

|q.p%|%||Th<br>|0<br>e shaded ar<br>|2<br>χ<br>ea is equal <br>|to _Æ_ for _¬_<br>|<sup>2 </sup>=_¬_<sup>2</sup><br>_Æ_<sup>.</sup><br>||Since%%%%%<br>high%%%f%%<br>P%=%0%%%%<br>less%t%%|%our%sta,s,c%(8.25)%is%<br>er%than%the%cut"off%for%<br>%%.005,%the%P"value%is%<br>%han%0.005%|
|---|---|---|---|---|---|---|---|---|---|---|
|_df_|_¬_<sup>2</sup><br>_._995|_¬_<sup>2</sup><br>_._990|_¬_<sup>2</sup><br>_._975|_¬_<sup>2</sup><br>_._950|_¬_<sup>2</sup><br>_._900|_¬_<sup>2</sup><br>_._100|_¬_<sup>2</sup><br>_._050|_¬_<sup>2</sup><br>_._025|_¬_<sup>2</sup><br>_._010|_¬_<sup>2</sup><br>_._005|
|1|0.000|0.000|0.001|0.004|0.016|2.706|3.841|5.024|6.635|7.879|
|2|0.010|0.020|0.051|0.103|0.211|4.605|5.991|7.378|9.210|10.597|
|3|0.072|0.115|0.216|0.352|0.584|6.251|7.815|9.348|11.345|12.838|
|4|0.207|0.297|0.484|0.711|1.064|7.779|9.488|11.143|13.277|14.860|
|5|0.412|0.554|0.831|1.145|1.610|9.236|11.070|12.833|15.086|16.750|
|6|0.676|0.872|1.237|1.635|2.204|10.645|12.592|14.449|16.812|18.548|
|7|0.989|1.239|1.690|2.167|2.833|12.017|14.067|16.013|18.475|20.278|
|8|1.344|1.646|2.180|2.733|3.490|13.362|15.507|17.535|20.090|21.955|
|%%<br>9|1.735|2.088|2.700|3.325|4.168|14.684|16.919|19.023|21.666|23.589|
|Using%a%<br>10|2.156|2.558|3.247|3.940|4.865|15.987|18.307|20.483|23.209|25.188|
|Chi"squared%|||||||||||
|test:%|||||||||||
|_X_ <sup>2 </sup><br>(_Oi_ −_~~E~~i_~~)~~<sup>~~2~~</sup><br>_n_<br>|<sup>~~(62~~</sup>|<sup>~~−48.~~</sup>|<sup>~~28)2~~</sup><br>|<sup>~~(80 −~~</sup>|<sup>~~93.72)2~~</sup>|<sup>~~(10~~</sup>|<sup>~~8−12~~</sup>|<sup>~~1.72)2~~</sup>|<sup>~~(25~~</sup>|<sup>~~0 −236~~.28)2</sup><br>825|
|=<br>_Ei_<br>_i_=1<br>∑|=|48.28||<br>93|.72|+|121.7|2|+|236.28<br>=.|
|_df_%=%(#%rows%"1)(#%%%%%|%%%%%cols%–%%%|%%%%%%%1)%=%1<br>,%%|%and%|_P_(_X_1<br>~~2 ~~≥|8.25)|=0.00|%so%%%<br>41|%%we%rej%|%%%ect%H0%|%(=>SNP%is%associated)|


22

### Tes,ng%for%SNP/phenotype%associa,on%

- Tes,ng%for%associa,on%between%a%SNP%and%a%disease%(or% some%other%trait)%–%we%are%given%the%following%counts:%

###### **Observed,**

|Allele%|**Cases,**|**Controls,**|Total%Counts%|
|---|---|---|---|
|**C,**|62%|80%|142%|
|**A,**|108%|250%|358%|
|Total%Counts%|170%|330%|500%|


142 <u>�142</u> _a_ <u>��170358</u> _−a_ <u>�</u> _⇡ ._ 003 Upper"tail%one"sided%P"value:% X _a_ =62 ~~�~~ 500170 ~~�~~

##### ~~Fisher~~ ’ ~~s%Exact%Test:%~~


<!-- Start of picture text -->
! $! $<br>a  + b c +  d<br>## &&## &&<br>" a %" c %<br>p  =<br>! $<br>a  + b + c +  d<br>## &&<br>" a  + c %<br><!-- End of picture text -->

_a_ Since%the%expected%count%of%%%%%(=%Cases%with%C)% was%~48,%since%62%=%48%+%14,%the%lower%tail%goes% up%to%48%"%14%=%34.%The%two"sided%P"value%is:%

Sum+all+probabili(es+for+observed+and+all+more+extreme+values+with+same+ marginal+totals+to+compute+probability+of+null+hypothesis++

Let%our%1%degree%of%freedom%be%%%%%,% _a_ the%number%of%cases%with%“C”%

34 <u>�142</u> _a_ <u>��170358</u> _−a_ <u>�</u> 142 <u>�142</u> _a_ <u>��170358</u> _−a_ <u>�</u> + _⇡ ._ 0047 X X _a_ =0 ~~�~~ 500170 ~~�~~ _a_ =62 ~~�~~ 500170 ~~�~~

23

### Human%Gene,cs%

AVer%doing%a%Chi"square%test%and%seeing%that%a%SNP%is%significantly%enriched%in%a% disease%popula,on,%we%might%believe%that%the%SNP%is%linked%to%the%disease.%%But% <u>popula,on%structure%can%confound%these%results%(methods%for%correc,ng%for%</u> this%are%beyond%the%scope%of%this%class)% Test%control%SNPs%(known%to%


<!-- Start of picture text -->
this%are%beyond%the%scope%of%this%class)% Test%control%SNPs%(known%to%<br>be%unrelated%to%the%disease)%<br>=%normal% =%disease% A%or%T%=%SNP%at% for%high%X 2 %distribu,on%<br>Locus%1% between%cases%and%controls,%<br>A%<br>which%would%indicate%<br>popula,on%stra,fica,on%<br>muta,on%<br>A% A% A% benign% A%<br>causing%disease% muta,on%<br>at%locus%2% A%">%T%at%<br>locus%1%<br>A% A% A% A% A% T% A% A%<br>A% A% A% A% A% A% A% A% T% T% T% T% A% A%<br><!-- End of picture text -->

In%4<sup>th</sup> %genera,on,%frac,on%of%Ts%in%popula,on%=%4/14,%but%in%diseased%group%=%4/6% But%once%we%see%the%family%tree,%we%see%that%the%SNP%at%locus%1%is%unrelated%to%the%disease%

24

### Linkage%Disequilibrium%

- Recombina,on%during%meiosis%"shuffles"%alleles%between%the% homologous%maternal%and%paternal%chromosomes%


Over%,me%and%aVer%many%crossover%events%have%occurred,%loci%that%are%physically%close% together%on%the%chromosome%will%tend%to%remain%together,%so%the%probability%of%two% loci%occurring%together%is%a%func,on%of%their%distance%along%the%chromosome%


If%a%crossover%event%is%equally%likely%to%occur%at% any%posi,on%along%the%chromosome,%the% probability%that%it%will%separate%loci%A%and%B%is% much%smaller%than%A%and%C%or%B%and%C% AB C

We%have%so%far%generally%assumed%that%inheri,ng%a%par,cular%allele%at%one%locus%won't%affect% the%probability%of%inheri,ng%an%allele%at%a%different%locus.%%Such%loci%are%in%linkage <u>. equilibrium</u>

Loci%are%considered%in%linkage%disequilibrium%if%genotypes%at%two%loci%are%not%independent%of% one%another%(e.g.%inheri,ng%A%at%locus%1%influences%probability%of%inheri,ng%B%at%locus%2)%

25

### Linkage%Disequilibrium%

- Measuring%linkage%disequilibrium:%%consider%two%loci%A% and%B,%where%locus%A%has%two%possible%alleles%A%and%a,% and%locus%B%has%two%alleles%B%and%b:%

   - then%gametes%can%have%one%of%four%possible%combina,ons:%


<!-- Start of picture text -->
Gamete% Frequency Allele% Frequency<br>AB% A%<br>pAB pA=pAB+pAb<br>Ab% pAb a% pa=paB+pab<br>aB% B%<br>paB pB=paB+pAB<br>ab% b%<br>pab pb=pab+pAb<br><!-- End of picture text -->

- Then%if%alleles%are%randomly%associated%w/%one%another,%the% frequencies%of%the%four% ~~gametes%should%be%the%product%of%the%~~ allele%frequencies:% Equilibrium **AB**


<!-- Start of picture text -->
Equilibrium<br>AB<br>ab<br>aBAbAbab aBABabAb ABAb hnp://www.nature.com/nrg/journal/v2/n1/pdf/<br>AB aB nrg0101_011a.pdf%<br>aB ab<br><!-- End of picture text -->

- ex.%pAB%=%pApB%=%(pAB+pAb)(paB+pAB)

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Mackay, Trudy FC. "Quantitative Trait Loci in Drosophila." _Nature Reviews Genetics_ 2, no. 1 (2001): 11-20.

26

### Linkage%Disequilibrium%

|Gamete%|Frequency|
|---|---|
|AB%|pAB|
|Ab%|pAb|
|aB%|paB|
|ab%|pab|


|Allele%|Frequency|
|---|---|
|A%|pA=pAB+pAb|
|a%|pa=paB+pab|
|B%|pB=paB+pAB|
|b%|pb=pab+pAb|


- If%they% ~~are%not%randomly%associated%(and%therefore%in%linkage%~~ disequilibrium)%then%there%will%be%a%devia,on%(D)%in%the%expected% frequencies:% Disequilibrium

   - pAB%=%pApB%+D%

   - pAb%=%pApb%"%D%

   - paB%=%papB%"%D%

   - pab%=%papb%+%D

- Where%D%is%given%by:%


<!-- Start of picture text -->
ab hnp://www.nature.com/nrg/<br>AB ab<br>AB journal/v2/n1/pdf/<br>ab AB ab ab AB nrg0101_011a.pdf%<br>AB<br>AB ab ab<br>AB<br>AB ab<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Mackay, Trudy FC. "Quantitative Trait Loci in Drosophila." _Nature Reviews Genetics_ 2, no. 1 (2001): 11-20.

   - D%=%pABpab%–%pAbpaB%%(D%=%0 <mark>%</mark> => <mark>%no%disequilibrium)%</mark>

- AB%and%ab%are%the%"coupling"%gametes%(AB%on%one%parental% chromosome,%ab%on%the <mark>%other),%Ab%and%aB%are%th</mark> e%"repulsion"% gametes%(crossing%over% <mark>event%must%occur%betwe</mark> en%the%loci)%–%D%is% the%difference%between%these%types.%

27

### Variant%Phasing%

- To%determine%which%genes%are%linked%together%(and%therefore%likely%to%be%inherited% together%in%the%next%genera,on),%you%need%to%figure%out%which%alleles%(which% variant%SNPs)%are%on%the%same%chromosome%=%"phasing"%%

   - Why%does%this%maner?%

   - %"%If%you%have%2%different%muta,ons%in%the%same%copy%of%a%gene%(phased),%the%2<sup>nd</sup> %copy%(no%

   - muta,ons)%may%be%enough%for%normal%ac,vity%

- %"%If%there’s%one%muta,on%in%each%(unphased),%both%copies%of%the%gene%may%be%nonfunc,onal%

- • OVen%rely%on%family%data%(e.g.%parents)%to%determine%which%"parental"% chromosome%segments%were%inherited%together%in%the%child%

- Can%be%used%to%iden,fy%haplotypes%=%combina,ons%of%alleles%at%adjacent%loca,ons% in%a%chromosome%that%are%inherited%together%over%many%genera,ons%

hnp://www.uic.edu/classes/bios/bios100/lecturesf04am/ crossingover01.jpg

X,%Y,%and%Z%are% “in%phase”%on%this% x,%y,%and%z%are%“in%phase”%on% Due%to%crossing%over,%the% chromosome% this%chromosome% phasing%has%changed%

> © The McGraw Hill Corportation, Inc.. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

28

---

[← Haploid,%unlinked%gene,c%model%](05-haploid-unlinked-gene-c-model.md) · [Up: contents](index.md) · [Variant%Phasing% →](07-variant-phasing.md)
