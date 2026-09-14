---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Outline

**Source:** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture25-bootstrap.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Estimation 1 Nonparametric 2 estimator Plugin 3 errors standard Bootstrap 4 Bootstrap bias estimator correction 5 confidence intervals Bootstrap 6 Double bootstrap


## Nonparametrice<sup>stimation</sup>


<!-- Start of picture text -->
Recall<br>of X<br>the empiricist Xn is<br>t E Bn 3<br>Ei X<br>The<br>ines timator of OCP<br>plug is Bn<br>a Sample median<br>b<br>1 max sample var<br>c OLS estimator<br>d MLE for Oe<br>Po<br><!-- End of picture text -->


Want O P to be cts wrt some topology in which P then OCP OCP

Counterexamples OCP 1 P is absolutely cts Pcc Lebesgue OCP 1 co P is integrable Epix Pn always integrable never abs cts for all n


<!-- Start of picture text -->
Bootstra<br>stadarderrors<br>x is an estimator for OCP<br>Suppose<br>maybe plug in maybe not<br>What is its standard error<br>Use plug in<br>use to indicate<br>07<br>F can<br>varp.ca new sample not X<br>OnCXE<br>Varp.CO Varx Xt<br>pep<br>How to Monte Carlo<br>compute<br>For b I B sample n points<br>with<br>replacement<br>Sample Xt XY'd In<br>from original same<br>18 0<br>067 X<br>I<br>0 8<br>8<br>sie On<br>EEcom_O<br>Note this is a Monte Carlo numerical approx<br>to the idealized estimate which<br>Bootstrap<br>we could<br>over all n<br>compute by iterating<br>possible XX XY XE vectors<br><!-- End of picture text -->


<!-- Start of picture text -->
BootstrapBirection<br><!-- End of picture text -->


<!-- Start of picture text -->
What is its bias<br>n some estimator<br>OCB<br>Bias p 8 Ep Q<br>Idea plug in Bn for P<br>Biasp.co Epn Q OCPn<br>NB<br>Monte Carlo<br>For 6 1 a B<br>Xi Xn<br>sample d idk<br>b<br>XH<br>I BE b<br>B<br>6 1<br>Bias In 8 0 En<br>We can use this to correct bias<br>NBC<br>Bias En<br>Q<br>Note while n Bias Q is always better than Q<br>Bias In not be<br>Q Might be adding us<br>may<br><!-- End of picture text -->


<!-- Start of picture text -->
A<br>1<br>1<br>20<br>OCP<br>EpO Ep<br>i<br>Iii<br>Biaspo Biasp<br><!-- End of picture text -->


<!-- Start of picture text -->
World<br>Rework.ie<br>Sampling dist P A Pex the<br>Parameter OCP<br>OCP x<br>Data set x p xt x Rex<br>observed once<br>Estimator X Q ated atwill<br>Sampling dist<br>of estimate<br>t.fi fn<br><!-- End of picture text -->

Confidence Interval Bootstrap


<!-- Start of picture text -->
How do we a CI for OCP<br>get<br>what if we knew the distribution<br>idea<br>of Efx Ocp<br>Rdx p<br>r OCP Er<br>Define cdf<br>Gn p Pp 07 1<br>r<br>Lower quartile Gn f<br>I<br>r<br>Gj'p<br>Upper<br>I o r O E ra<br>Ppl E Q<br>r<br>Ppc Oe n ra Q<br>so<br>Usually we don't know Gn p bootstrap<br>r OCR er<br>Gn<br>Pq 8Cx<br>not of P<br>function of X<br>is a only<br>r<br>G f<br>En iz Q E<br>Can use Cn<br>I<br>with f Gipn Fa Gn p<br><!-- End of picture text -->


<!-- Start of picture text -->
Bootstrapat<br>For 6 1 B<br>XM Xn b dp<br>Rib cx b OCR<br>Return ecdf of Rib<br>Rnc X P Efx OCP is called a roof<br>The quantity<br>function of data dist used to make CIs<br>Other examples<br>iiTl<br>iIRnlx.P<br>T.io<br>i i iI<br>0nCxYocp<br>dist<br>so its sampling<br>Want to choose Rn<br>slowly with P so Gn p Gn p<br>Gnp changes<br>works better<br>Studentized root usually<br>E<br>than then we<br>Q O get<br>F no<br>EE En<br>Cn<br>Q<br><!-- End of picture text -->


<!-- Start of picture text -->
DoubleBootstrap<br>us<br>tells<br>have that e.g<br>We theory<br>might<br>50<br>IGn.ECCa.bz Gmp Ca D<br>say<br>still be worried about finite<br>but sample<br>coverage<br>Let 2 OCP<br>jn.pk Pp Cn<br>I L if Cn has<br>coverage<br>asy<br>But in finite samples have<br>might<br>L l a<br>pG<br>interval has 87<br>e g 90 coverage<br>Jn p O D 0.87 C 0.9<br>Solution Double Bootstrap<br>in<br>1 Estimate via<br>plug yn<br>yn.pl<br>2 Use Cn Z X where Ita I o<br>interval 08<br>estimate 92 has 90 coverages 8<br>e g<br><!-- End of picture text -->

---

[Up: contents](../index.md)
