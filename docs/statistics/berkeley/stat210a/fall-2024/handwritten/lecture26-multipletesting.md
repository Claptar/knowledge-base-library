---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture26-multipletesting.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture26-multipletesting.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Outline

**Source:** [`handwritten/lecture26-multipletesting.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture26-multipletesting.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

> 1 Multiple Testing 2 Family<sup>wise</sup> error rate control 3 Step<sup>down</sup> multiple testing 4 Simultaneous intervals Ideduced<sup>inference</sup>

> 5 False Discovery<sup>Rate</sup> control 6 Benjamin Procedure Hochberg


<!-- Start of picture text -->
FamilywiseEIorRate<br>have<br>Even if all Hoo true<br>Robley might<br>L<br>IP Hoi rejected<br>any<br>EI X int N Oi D i 1 m Hoi Oi _0<br>m<br>Po any Hoc rejected I G a 1<br>Is this a problem Yes if all attention<br>will be focused on the false<br>rejections<br>and more on the correct<br>non rejections<br>Classical solution is to control the<br>rate<br>familywiseerror fewer<br>F WER<br>IPO false<br>any rejections<br>lPoCRnH<br>0<br>Want<br>sff FWERO E 4<br>correcting marginal<br>Typically achieved by<br>U o D<br>values pmCX<br>f p.CN p Ei<br>fix 2 I oIClXiD for Gaussian<br>e g<br><!-- End of picture text -->


<!-- Start of picture text -->
Bonferronicorrection<br>Ho Hom<br>are<br>Assumef.si pm p values for<br>with U under Hoi<br>0,1<br>pi<br>can<br>For guarantee control<br>general dependence<br>Hoi iff<br>by rejecting pi<br>Po<br>rejections<br>any false<br>Ho rejected<br>Po<br>Hoi rejected<br>Eg Po<br>α<br>Mo<br>If independent can to<br>improve<br>p values<br>m correction<br>In 1 1 d Sidal<br>Then no<br>Po false rejections<br>id.to Po a<br>pi<br>1 1 d<br>m<br>For small α 1 am 1 a I<br>I<br>Sidal doesn't much on<br>Bonferroni<br>improve<br><!-- End of picture text -->


<!-- Start of picture text -->
Deducedinf erence<br>CCX<br>confidence<br>Given<br>joint region<br>any<br>for OE we assume<br>may freely<br>0 c Cx deduce and all<br>and<br>any<br>FWER inflate<br>implied conclusions without<br>any<br>IPO<br>deduced inference<br>is<br>any<br>wrong<br>Can ed<br>a Polo<br>Deduction is often a for<br>good paradigm<br>deriving simultaneous intervals<br>We C CX are<br>Cmlx<br>say<br>simultaneous 1 a confidence intervals<br>for O<br>O if<br>g<br>gm<br>IPO m Il o<br>gilo C Cicx Vi I<br><!-- End of picture text -->


<!-- Start of picture text -->
EI Simultaneous intervals for multivar Gaussia<br>Assume<br>X Nd 0 E I known Eii I<br>Let<br>to a of DX Oka<br>quantile<br>upper<br>CCD<br>90 Ioi Xi l e ca Vi<br>X to x X I x t<br>tDx<br>Xd<br>c X x x CdcXD<br>X Oi i POCO Cox a<br>PIC<br>any<br>Q<br>2<br>E<br>d<br>a<br>It<br>Cz I<br>i<br>l<br>c O<br>Note we could have instead constructed<br>an conf but then the<br>elliptical region<br>g<br>intervals would be conservative<br>IPC I d<br>pe<br>i.oieas<br>I d<br>O<br>c<br><!-- End of picture text -->


<!-- Start of picture text -->
I<br>EI nobs<br>d variables<br>Linearregression<br>XEIR design B NICE oTxX5Y<br>2 R<br>Estimate d I<br>B<br>tha BEI<br>FE<br>where<br>2 B DG Naco Cx'x5S<br>V RS XI d<br>z Iv Distr<br>of Bjp fully knows<br>Assume<br>wlog X'x<br>Hj<br>Let to denote a<br>upper quantile of B Hp<br>Then Cj Et are simultaneous CIs<br>Bj<br>j I id<br>for Bj<br>compute to by simulation<br>pieces.tt PCIB B.ie Eto t I o<br><!-- End of picture text -->


<!-- Start of picture text -->
iI<br>is<br>men<br>with test statistics all<br>independent<br>at level α 0.001 We expect 10<br>chance What if we<br>rejections just by<br>of them<br>50 20<br>get Probably only<br>are false rejections<br>as<br>Can we 10 false rejections<br>accept<br>most are valid<br>as<br>rejections<br>long<br>95 a more<br>Benjamin proposed<br>Hochberg<br>liberal error control criterion called FDR<br>R X R X rejections discoverie<br>X O O<br>RX false discoveries<br>The<br>IEP is<br>0<br>The FDR<br>is ELFDP Eo<br><!-- End of picture text -->


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
