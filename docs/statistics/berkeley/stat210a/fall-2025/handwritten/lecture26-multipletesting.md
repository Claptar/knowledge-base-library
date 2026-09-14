---
title: Lecture 26 — multipletesting
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture26-multipletesting.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture26-multipletesting.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 26 — multipletesting

**Source:** [`handwritten/lecture26-multipletesting.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture26-multipletesting.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Outline

> 1 Multiple Testing 2 Family<sup>wise</sup> error rate control 3 Step<sup>down</sup> multiple testing 4 Simultaneous intervals Ideduced<sup>inference</sup>

> 5 False Discovery<sup>Rate</sup> control 6 Benjamin Procedure Hochberg


### Familywiseerrorrates


<!-- Start of picture text -->
have<br>Problems Even if all Hoi true might<br>IP Hoi rejected<br>any<br>I<br>Ex X N Oi 1 i b m Hoi 0 0<br>Po 1 1 a 1<br>any Ho rejected<br>Is this a problem Yes if all attention<br>will be focused on the false<br>rejections<br>and none on the correct<br>non rejections<br>Classical solution is to control the<br>EWER<br>familywiseerrotrae<br>FWERO IPO<br>false<br>any rejections<br>Po Rn<br>24 0<br>Want<br>31 FWERO α<br>correcting marginal<br>Typically achieved by<br>x X U 0,1<br>values<br>pm<br>p p p<br>filx 2 1 Ixil for Gaussian<br>e g<br><!-- End of picture text -->


<!-- Start of picture text -->
Bonferronicorrection<br>Ho Hom<br>are<br>Assumef.si pm p values for<br>with U under Hoi<br>0,1<br>pi<br>can<br>For guarantee control<br>general dependence<br>Hoi iff<br>by rejecting pi<br>Po<br>rejections<br>any false<br>Ho rejected<br>Po<br>Hoi rejected<br>Eg Po<br>α<br>Mo<br>If independent can to<br>improve<br>p values<br>m correction<br>In 1 1 d Sidal<br>Then no<br>Po false rejections<br>id.to Po a<br>pi<br>1 1 d<br>m<br>For small α 1 am 1 a I<br>I<br>Sidal doesn't much on<br>Bonferroni<br>improve<br><!-- End of picture text -->


<!-- Start of picture text -->
dircty.tt tr.onis<br>we can e<br>a<br>using stepdownprocedure<br>First order<br>p values pa fee fam<br>Order to match Has Ham<br>hyp Has<br>Holm's<br>step down procedure<br>1 If reject Her and continue<br>pa<br>Else __ Hcm halt<br>accept Has and<br>2 If and continue<br>pea i reject His<br>Else accept Ha Him and halt<br>i<br>m If reject Him<br>pen Else accept Him<br>More compactly R max r poi It Vier<br>PCR<br>Reject pass<br>his<br>_Fit<br><!-- End of picture text -->


<!-- Start of picture text -->
age<br><!-- End of picture text -->


<!-- Start of picture text -->
I<br><!-- End of picture text -->

Prof Holm's procedure level α

controls FWER at


<!-- Start of picture text -->
Profo Let min ie Hoi<br>pi<br>p<br>union bound<br>IP pot α<br>G by<br>Suppose pot Tmo want to show no false rejections<br>Let k<br>m<br>mott<br>i pispo<br>Note<br>for<br>pot<br>It<br>So R<br>4k pox No false rejs<br>pea<br><!-- End of picture text -->


There is a framework general for such making improvements called the Jeprinciple


<!-- Start of picture text -->
Closueprinciples<br>Assume we can construct a<br>marginal<br>level α test for intersection<br>every<br>Ill for S 1 __ m<br>hypothesis<br>Hos O<br>i<br>Is<br>e g reject Hos if<br>9s<br>zig pi<br>1<br>Provisionally reject Hos if the<br>marginal test<br>rejects<br>Ho if<br>Stef Reject Hos<br>rejected<br>for all Sai<br>Prof This controls FWER<br>two step procedure<br>Proof P<br>any false rejections<br>IP Ho rejected in Step 1<br>α<br><!-- End of picture text -->


<!-- Start of picture text -->
Deducedinf erence<br>CCX<br>confidence<br>Given<br>joint region<br>any<br>for OE we assume<br>may freely<br>0 c Cx deduce and all<br>and<br>any<br>FWER inflate<br>implied conclusions without<br>any<br>IPO<br>deduced inference<br>is<br>any<br>wrong<br>Can ed<br>a Polo<br>Deduction is often a for<br>good paradigm<br>deriving simultaneous intervals<br>We C CX are<br>Cmlx<br>say<br>simultaneous 1 a confidence intervals<br>for O<br>O if<br>g<br>gm<br>IPO m Il o<br>gilo C Cicx Vi I<br><!-- End of picture text -->


<!-- Start of picture text -->
EI Simultaneous intervals for multivar Gaussic<br>Assume<br>X Nd O Ʃ Ʃ known Eii 1<br>Let<br>to o of AX Ollas<br>quantile<br>upper<br>Cx 0<br>10 X co<br>X to x X x<br>to Xatt<br>CX x<br>Cd Xd<br>C x Oi i Po O CX α<br>any<br>Q<br>1 2 E<br>It<br>Cz<br>p<br>C 0<br>Note we could have instead constructed<br>an conf but then the<br>elliptical region<br>intervals would be conservative<br>p<br>z p IPC 1 d<br>f IPCO EG 0sec<br>f<br>P a t d<br>so<br>c<br><!-- End of picture text -->


<!-- Start of picture text -->
I<br>El linear n obs d variables<br>regression<br>XJ<br>EIR Nd β<br>design<br>β<br>Estimate RSSa d I<br>β<br>The BEE<br>Eg<br>where<br>Z x<br>B B to Naco<br>V RSSG X d<br>z IV Distr<br>of FEI fully known<br>Assume<br>w og X'x I<br>Let to denote<br>upper quantile of BE ls<br>Then Cj B It are simultaneous CIs<br>bed<br>j<br>for Bj<br>Compute to by simulation<br>IP EC<br>β P B β Eto α<br><!-- End of picture text -->


<!-- Start of picture text -->
cnn.si I IE<br>with test statistics all<br>independent<br>at level α 0.001 We expect 10<br>chance What if we<br>rejections just by<br>of them<br>50 20<br>get Probably only<br>are false rejections<br>as<br>Can we 10 false rejections<br>accept<br>most are valid<br>as<br>rejections<br>long<br>95 a more<br>Benjamini proposed<br>Hochberg<br>liberal error control criterion called FDR<br>R X R X rejections discoverie<br>X O 0<br>R x nH false discoveries<br>the<br>EDP is<br>0<br>K<br>The FDR<br>is<br>IEo FDP Eol<br><!-- End of picture text -->


<!-- Start of picture text -->
Benjamini Hochberg Procedure<br>B H also a method to control<br>proposed FDR<br>ordered<br>given p pea pen<br>p values<br>RIX max r called<br>par stepy<br>Procedure<br>Reject Has r<br>Pci<br>α<br>BIT<br>R 6<br>Bonferron<br>This<br>is much more liberal than Borf<br>procedure<br>when I a Ream BH<br>rejects at least<br>r p values if<br>for<br>per<br><!-- End of picture text -->

BHasempiri.ca Bayes


<!-- Start of picture text -->
Equivalent formulation for Rt fi et<br>p<br>let falsedisc<br>estimate of Vt<br>fDpt<br>9<br>I<br>if<br>BH rejects Hi E THX<br>max ft<br>pi FDI Ea<br>Wh<br>is<br>FFpt<br>continuously in t<br>increasing<br>except at values where it<br>fu<br>mt jumps down<br>IRWIN<br>O<br>a<br>0<br>M<br>O<br>y<br>fI l l l l l<br>t<br>Risks Pcs Ky Pcs t<br>Only values of t that maker for the algorithm<br>t m<br>are<br>where<br>p FDI<br>me<br>e a ai e<br><!-- End of picture text -->


<!-- Start of picture text -->
FDRcontrot<br>Elegant but fragile proof due to storey<br>2002<br>Taylor Sigmund<br>Assume<br>f indep U 0,17 c EH<br>pi<br>Let<br>Ve et<br>ie Ho p<br>It<br>FDR<br>Rtu l<br>FDTt m<br>Then FDR E FDP<br>E F5Pt<br>Y<br>d E Vt o<br>FIE<br>t<br><!-- End of picture text -->


<!-- Start of picture text -->
Note<br>Qt is a<br>when t runs<br>martingale<br>backwardse from t l to t 0<br>set<br>IE<br>Vs<br>Vt D<br>ii<br>Ef I et v<br>pies<br>fi p<br>E<br>v<br>t<br>1<br>El<br>E<br>q Es Gmt E<br>And H<br>is<br>a time Wrt the<br>stopping<br>filtration<br>vt<br>Ft<br>off<br>Pmut<br>filtration with<br>again e i t o<br>For set<br>Why Rs i<br>pies<br>Ei e s<br>peut<br>FDTs<br>Rs<br><!-- End of picture text -->


<!-- Start of picture text -->
I<br>D<br>a<br>o<br>e<br>t<br>O O O 0 O 0<br>07<br>I<br>l l l l l l<br>l<br>on<br>FDR V<br>d E<br>a ELY<br>a Mohn<br><!-- End of picture text -->

## Reinas


<!-- Start of picture text -->
Proof works if indef<br>only f Values<br>hull uniform<br>ones exactly<br>More shows FDR<br>controlled<br>robust proof<br>when<br>conservative<br>null f values<br>can be extended to positive defender<br><!-- End of picture text -->


<!-- Start of picture text -->
FDR<br>dependence<br>controlled under general<br>if we use corrected level<br>m<br>Lm T<br>E<br>login<br><!-- End of picture text -->

---

[Up: contents](../index.md)
