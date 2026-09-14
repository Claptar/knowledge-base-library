---
title: Lecture 11 — bayescompute
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture11-bayescompute.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture11-bayescompute.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 11 — bayescompute

**Source:** [`handwritten/lecture11-bayescompute.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture11-bayescompute.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

rchical Bayes 2 Markov Chain Monte Carlo 3 Gibbs Sampler


<!-- Start of picture text -->
Hierarchical<br>Bayes<br>Full of Bayes is realized in large<br>power<br>with structure<br>complex problems repeat<br>allowing us to pool information across<br>observations<br>many<br>E Predict a batter's true batting average<br>from ni at bats Xi of hits Biron ni O<br>Pool info i t m via hierarchical mode<br>across players<br>a B Yolo B<br>Oils p rid Betalo B ism<br>iem<br>Mee Biron ni Oi<br>Xi Oi<br>x E ELO ix a B Ix<br>Eloi<br>sampled tho Bixt<br>ECÉÉ Ix<br>Use all Xi on Oi<br>It xm to learn good prior<br>model where we<br>Note there is always an equivalent<br>over a B and just write a more<br>marginalize<br>on O Hierarchical version may give<br>complicated prior<br>better intuition or computational strategies<br><!-- End of picture text -->

fussianHierarchicadmool


<!-- Start of picture text -->
g<br>g<br>e ied<br>ta Id NCO<br>Oi<br>o O Ed NCOi D<br>Xi<br><!-- End of picture text -->


<!-- Start of picture text -->
Define 5 t e amount of shrinkage<br>Txt I EL x Xi<br>Fred from entire data set<br>X 5 Nato IIa 121st<br>Egan E<br>511 1112<br>a Ed's<br>e<br>Conjugate prior<br>scale<br>he<br>e 5512<br>g's<br>5 X ICE<br>yi<br>kted I Is't tix 512<br>hype e<br>y g g<br>Flip Ned<br>Efflux't Old<br>SETI<br>deity<br>pseudo data Y Y with 11411 s<br>to o I<br>want to truncate<br>prior<br>might<br>if I smell<br><!-- End of picture text -->


<!-- Start of picture text -->
parametes<br>Graphicalforf<br>E hyper<br>L V<br>J<br>O Oz Om<br>X X2 I<br>These are d<br>the<br>distr ÉÉmayÉÉÉÉ with<br>in a DAG V E<br>factor for each vertex<br>II p ZilZpaci<br>plz<br>Pali i<br>i j<br>For this model<br>t Oi On Xi Xm<br>p<br>t 91 E<br>I Ipcxiloi<br>p<br><!-- End of picture text -->


GIstationarityotto


Proof


<!-- Start of picture text -->
afd valid kernel<br>In theory Pick.FI izat<br>Q 0 7101 1<br>sample long enough is<br>Do it again N more times mn N samples from Xo<br>In how do we know we've<br>practice sampled long enough<br>T Show how fast the MC mixes<br>t<br>Lumanammnthm<br>if<br>oifn.at Anne<br>ᵗ<br>GOOD<br>NOT<br>GREAT<br>Can be deceived<br>Esp for bimodal posterior<br>10 x<br>tho<br>me<br>µ<br>B<br>Estimate posterior based<br>rent<br>Burn Ethan B N<br>on 0 B<br>O<br>0 3<br>F ration<br>n<br>Ʃ 0 Efo<br>rmean<br>P.si 1 0<br><!-- End of picture text -->


<!-- Start of picture text -->
Implementation details matter<br>O O id NCO 1<br>id N O 10s 1 it on<br>Xi O<br>To nlo.LY<br>O F N NCI ECI<br>MCI 1 I<br>att Ey<br>ECI c l<br>89 1 att<br>Ii<br>2<br>I<br>a 1<br>Gibbs takes<br>a long<br>time to mix<br>1<br>Better parameterization<br>f<br>i B O to<br>B or<br>or<br>O<br>BiH B lx<br>Gibbs<br>Directly sampling<br>to<br>from posterior<br><!-- End of picture text -->


<!-- Start of picture text -->
Empirically<br>model<br>hierarchical<br>Back to Gaussian<br>MCE<br>for Itta<br>n<br>Illxll It x'd<br>is tall x<br>her 2ft<br>MCE<br>g<br>reasonable<br>a<br>For 51 7<br>prior fye<br>any<br>l 1 5 Xi<br>É Xi<br>matter much why use one<br>If prior doesn't<br>5 from data<br>estimate<br>Could just<br>it in<br>want<br>however we plug<br>estimator is 5<br>Amun<br>934<br>a<br>hybrid approach<br>Called EmpiricalBayest<br>treated as fixed<br>which<br>in hyper parameters<br>others treated as random<br><!-- End of picture text -->

---

[Up: contents](../index.md)
