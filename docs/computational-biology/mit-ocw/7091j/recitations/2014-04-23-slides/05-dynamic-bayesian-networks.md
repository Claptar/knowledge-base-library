---
title: Dynamic%Bayesian%Networks%
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Dynamic%Bayesian%Networks%

**Source:** `recitations/2014-04-23-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- A%Bayesian%network%(directed%graphical%model%where%arcs/ edges%represent%condi,onal%dependencies)%that%models%a% dynamic%process%(sequen,al%data,%either%temporal%or%spa,al%–% e.g.%along%the%genome)%

- Similar%to%Hidden%Markov%Models,%but%include%addi,onal% random%variables%that%allow%tuning%(e.g.,%hard%limits%on% segment%lengths)%

8

## **( ( ( ( ( ( (** Segway:%Dynamic%Bayesian%Network%


<!-- Start of picture text -->
� �� ����� � ��<br>� � �� ���������� ��<br>�� ���������� ��<br>�������<br>� � �� ��<br>�����<br>� �� � � � �� � � ���������� � � �� � �<br>� � �<br>� � � � � � � � ������������ � � � � �<br>� � �<br>� � ∈ ����� � �<br><!-- End of picture text -->

Black%arcs%(edges)%=%determinis,c%condi,onal% dependence,%red%=%stochas,c%condi,onal% dependence%

Variable’s%parents%are% indicated%by%its%direct% predecessor%in%the%directed% graph%

Every%variable%is%condi,onally% independent%of%all%variables%in% the%model%given%its%parents

_n_ %observa,on%tracks% _T_ :%sequence%length%

Square:%discrete%random% variable%

Circle:%con,nuous%random% variable%

White:%hidden%variable% Black:%observed%variable%

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

9

## Segway:%Dynamic%Bayesian%Network%


<!-- Start of picture text -->
� �� ����� � ��<br>� � �� ���������� ��<br>�� ���������� ��<br>�������<br>� � �� ��<br>�����<br>� �� � � � �� � � ���������� � � �� � �<br>� � �<br>� � � � � � � � ������������ � � � � �<br>� � �<br><!-- End of picture text -->

_�_ � ∈ ����� _�_ � Observa,on%track:%assay%output%(e.g.,%density%of%H3K4me3% ChIP"seq%reads%–%one%track%for%each%of% _n_ %experiments)%

Segment%label:%The%hidden% annota,on%you’re%trying%to% infer%(e.g.%promoter).%

Indicator:%1/0%whether%or%not% the%assay%produced%any%results% for%that%region%(=0%if%assay% can’t%map%reads%to%that%region.% In%this%case,%the%edge%from%Qt to%Xt(i)%is%edited%out)%

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

10

## Segway:%Dynamic%Bayesian%Network%

Ruler%marker:%


<!-- Start of picture text -->
%=1%every%10 th %posi,on,%0%<br>� �� ����� � �� otherwise%(every%10 th %posi,on,%<br>we%update%the%countdown%<br>variable%as%to%how%long%we’ve%<br>� � �� ���������� ��<br>been%in%that%label)%<br>�� ���������� ��<br>������� Countdown:%Discrete%variable%<br>� � �� ��<br>�����<br>that%allows%the%specifica,on%of%<br>minimum%or%maximum%<br>� �� � � � �� � � ���������� � � �� � �<br>� � �<br>segment%length.%Starts%at%ini,al%<br>value%dependent%on%QT%(might%T%(might%%(might%<br>want%TSS%to%be%short%but%<br>� � � � � � � � ������������ � � � � �<br>� � � intergenic%region%to%be%long)%<br>and%decreases%where%ruler%<br>� � ∈ ����� � �<br><!-- End of picture text -->

Countdown:%Discrete%variable% that%allows%the%specifica,on%of% minimum%or%maximum% segment%length.%Starts%at%ini,al% value%dependent%on%QT%(might%T%(might%%(might% want%TSS%to%be%short%but% intergenic%region%to%be%long)% and%decreases%where%ruler% marker%MT=1.%

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

11

## Segway:%Dynamic%Bayesian%Network%


<!-- Start of picture text -->
� �� ����� � ��<br>� � �� ���������� ��<br>�� ���������� ��<br>�������<br>� � �� ��<br>�����<br>� �� � � � �� � � ���������� � � �� � �<br>� � �<br>� � � � � � � � ������������ � � � � �<br>� � �<br>� � ∈ ����� � �<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Transi,on:%binary%segment% transi,on%label%that%either% forces%the%segment%label%to% change%at%the%current%posi,on% (Jt=1)%or%prevent%it%from% changing%(Jt=0).%

Segway%generates%a% condi,onal%probability%table% P(Jt=1|Qt"1,Ct"1)%that%maps%each% (Qt"1,Ct"1)%to%one%of%three%rules% that%determine%the%value%of%Jt:% %1.%Force:%P(Jt=1)%=%1% %2.%Prevent:%P(Jt=1)%=%0% %3.%Allow:%P(Jt=1)=1/(1+L)%

“Allow”%rule%models% geometric%distribu,on%w/ expected%length%L%

12

## Segway:%Dynamic%Bayesian%Network%

- Train%on%1%%of%the%Genome%

   - Assign%equal%probability%(=1/n)%of%each%label%to%the%star,ng%posi,on,%then%use% Expecta,on"Maximiza,on%(EM)%algorithm%to%learn%model%parameters% (contribu,ons%of%each%track%(experimental%assay)%to%each%label)%%

   - Star,ng%from%different%ini,al%condi,ons%(i.e.,%contribu,ons%of%each%track%to%a% par,cular%label)%gave%similar%results%

- Then%use%these%parameters%to%segment%the%rest%of%the%genome% using%Viterbi%decoding%(similar%to%what%we%discussed%for%HMMs)%

13

#### Example%of%Segway’s%segmenta,on%for%a%gene%


<!-- Start of picture text -->
Window position Human Mar. 2006 (NCBI36/hg18) chr6:33044414-33057260 (12,847 bp)<br>Scale 5 kb<br>Chr6: 33046000 33047000 33048000 33049000 33050000 33051000 33052000 33053000 33054000 33055000 33056000 33057000<br>Segway 31-track chromatin segmentation (K562)<br>D<br>L0<br>L1<br>F0<br>F1<br>R0<br>R1<br>R2<br>R3<br>R4<br>R5<br>C0<br>C1<br>H3K9me1<br>TF0<br>TF1<br>TF2<br>TSS<br>GS<br>E/GM<br>GM0<br>GM1<br>GE0<br>GE1<br>GE2<br>ENCODE Gencode Manual Gene Annotations (level 1+2) (Oct 2009)<br>HLA-DMA BRD2<br>HLA-DMA BRD2<br>BRD2<br>BRD2 BRD2<br>BRD2 BRD2 BRD2<br>AL645941.1 BRD2 BRD2<br>BRD2<br>BRD2<br>BRD2<br><!-- End of picture text -->

      - © source unknown. All rights reserved. This content is excluded from our Creative Commons licens ~~e.~~ For more information, see htt ~~p://~~ ocw.mit.edu/help/f ~~aq-f~~ air-use/.

- "Arbitrarily%chose%there% ~~<u>to</u>~~ %be%25%labels%(so%that%they%wo ~~uld~~ %remain%int ~~er~~ pretable%by%biologists)% % ~~Th~~ e%authors%gave%n ~~<u>am</u>~~ es%to%the%resul,ng%25%labels:%

   - %D:%“dead”%–%n ~~o%a~~ c,vity%

   - %GS:%gene%start%

   - %GM:%gene%middle%

%GE:%gene%end%

~~%E:%enhancer%~~

14

---

[← Profiling%histone%modifica,ons%](04-profiling-histone-modifica-ons.md) · [Up: contents](index.md) · [Transcrip,on%Factor%Binding% →](06-transcrip-on-factor-binding.md)
