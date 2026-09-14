---
title: HandwrittenNotesLectureFour153248Fall2026
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/HandwrittenNotesLectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# HandwrittenNotesLectureFour153248Fall2026

**Source:** [`HandwrittenNotesLectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Lecture 4 153 248<br>Multiple Linear Regression<br>Response<br>y<br>Covariates<br>ldotsm x 1<br>Data<br>ldotsrightleftm12y ix<br>ldotsni1<br>timesn1<br>Response vector<br>vdots matrix begineleft n 1d<br>right y<br>matrix<br>Covariate<br>matrix begin vdo timeldots right e leftm X 1x2n d s<br>Time Series<br>ldotsny1 t<br>right matrix vdotsbegineleft n 1d<br>y<br>Use functions of time to construct X<br>beta 01 2 error<br>y t<br>t t2<br><!-- End of picture text -->


<!-- Start of picture text -->
matrixbeginvdorighte frac cosleft sinpiX nt12 x ds<br>Use lagged values of y as covariates<br>matrix begin vdo ldotsrightelefmX n0yt12 d ts<br>m2<br>matrixbeginvdo ldots righteleft X n2 3 y1ds<br>n2<br>molleft s<br>X rightyx<br>y 1<br><!-- End of picture text -->

Frequentist Inference ldots **beta** m0y0y **1xi**

varepsiloni im ldots **beta** m0y0y **1xi** y **i** error Unknown parmeters varepsiloni iid sigmarightleftN02 ldots **beta** m012 mean 0 sigma varepsiloni independence Construct<sup>estimatesfor</sup> finite<sup>variance</sup> MLE least the parameters squares out the distribution of<sup>the</sup> estimate Figure exact<sup>or</sup> approximate Use the distribution to construct confidence intervals Estimate Least Squares end **beta** beginrightvdots **matrix** leftmk0 ldots **beta** m0 ldo **bleftm** S2 **ta** s sum_ **right** ny0 **xi1** minimize bl **e** Stftta vdots **matrix** right get right **beta** beginend **hat** lefm0 in closed form Solve<sup>hat</sup> f **rightbleft** yX2S **ta eleft** X **n1** xij **yd** vdots **beginrightmatrix rightbleftyXTxta**


<!-- Start of picture text -->
ldotsrightleft a1kx fi<br>nablafa<br>matrix vdonabl b fracend left m0 Staa s l<br>par beg righti n<br>forallright b l e S xTy 2ft ta check<br>nablaright b l eTx ft ta<br>if A is symmetric<br>nablaright b l eA T2ft ta<br>nablaright b l e y0S 2xT ft ta<br>beta XT<br>y Least<br>Squares<br>rightbhal eXT 1yfta t<br>Estimator<br>Maximum Likelihood<br>varepsiloni iid sigmarightleftN02<br>independentrightarrowsigldotsright b sil em N02y 1xim ft ta a<br>Assume<br>m<br>Data<br>ldotsy ix s arefixed<br>xij<br>ms2<br>sigma prod_ldots beta sqrt frac mpi0 2 nety xi1<br>Likelihood<br>sigmaright bfracexp left piS 2n ta<br><!-- End of picture text -->


<!-- Start of picture text -->
dog likelihood<br>sigma rightb frac l e piS n2los ftta<br>nabla b hl e 0Sf tat betaLeastSquares<br>Rightright a rrow MLE hat<br>bfracleft 30 Snta<br>Rightarrow sigmaright sqrt<br>hatsigma<br>hbfrl e Sn a ftac t<br>MLE rightsqrt<br>beta bl exT fta<br>beta<br>Remember hat right1y<br>least ha t<br>MLE hat<br>square<br>bfr hat l e MLESnftac<br>sigmarightsqrt<br>distribution<br>2<br>Calculate the<br>Step<br>i nd<br>sptilde ldots beta N0xi 1 beta<br>mx im<br>Yi<br>rightbhal eXT 1xyfta t sigma2<br>matrix beginvdotsesimleft n 1d<br>Recall right y<br>Sig NX r frac s demu leftqrt N2A p i 1mhta<br><!-- End of picture text -->


<!-- Start of picture text -->
times1<br>p Rightarrow SigrsimmuleftNAX T hta<br>bhal eXT fta t sigrightbsil e NX2Iy m fttaa<br>right1y<br>ind<br>matrixsigbeginvdoldotsbrightesimleftmN2n01xyitadsa<br>sigma2In<br>y<br>beta siha l NT2 x 1 mft a<br>sig right<br>beta siha l N XxT 2I1 mft a<br>DETAILS<br>sig righty<br>A<br>SKIPPED<br>beta siha l N X T21 mft a<br>sig right<br>hatsigma bfrhl e Sn a ftac t<br>MLE rightsqrt<br>2<br>sigmaRightarrowhat<br>M LE b frac sihlchi e m1S 2nm fta t a<br>sigright<br>Sldots rightbhaleftm 0S2y 1xi ma ta<br><!-- End of picture text -->


<!-- Start of picture text -->
sigmahat2<br>fracsiXm1 2nm a<br>M LE<br>sig<br>hatsigma2<br>I<br>M LE t mesfracleftm12 n<br>sright i gma<br>sigma2<br>sigmahat2<br>is NOT unbiased for<br>M LE 2<br>beta<br>hatsigma2 M LE frac righthalefSn t<br>leftrightarrowbfr h l e nm1S a ftac t<br>unbiased sigmaright<br>Recap beta siha l N fxT 2 mt a<br>sig right y 1<br>hatsigma2 fracsiXm1 2nm a<br>M LE<br>sig<br>2<br>sigmahat2<br>LE<br>unbiased frhm1 na ct<br>sigma M<br>beta si l N X T2 1mf a<br>sig right ha j t<br>ov matrixsigma b arig b sqrtfr end haleftephaXT1jZ2 brlgta cint e<br>betafr hat 2c overline left<br>sigmaalphajz matrix fre leftX1 Zr2bu n dc used right sqrtpi x1j<br>unbiaseda pbeginsigma right sqrt jha P a<br><!-- End of picture text -->


<!-- Start of picture text -->
betapsi52<br>distribution<br>t<br>quantile alphafractnm12<br>rightbhal exT 1yfta t sigrightbsil e NX2Iy m fttaa<br>alphanicefrac2 nicefrac<br>alpha2<br>alphanicefrac<br>2z<br>alphafractnm12<br>BayesianApproach<br>Model<br>varepsilonmi<br>ldots beta m0y 1xi sigmarightleftN02<br>variables<br>m1n<br>ldotsni1<br>c<br>iid Unot rightleft<br>rightarrowldots beta m0<br>unit left c<br>right<br>sigsilog m a<br>data<br>data α<br>ldots b l e m0ft ta ldotsleftn<br>right ldotsn right y 1<br>y 1<br><!-- End of picture text -->


<!-- Start of picture text -->
e<br>beta data<br>f<br>sigmarightbl e ftta<br>ldotsbetan 1 f<br>sigma y<br>sigma aldots rigbetal pn y1ffth a t<br>sigmaldotsbetan y1<br>prior<br>Likelihood<br>bfrac left S 2 nta<br>sigmaright exp b fracIleft m1los C2 ta<br>sigmaright j<br>overline sigma a rig bfracexp left pI0S 2 n1 h taa t<br>data<br>β<br>overline b frac ileft nt_0S 2 dn1 fta<br>propto sright inexp gma y<br>β data<br>propto<br>right betafrac left 1Sn2<br>distribution<br>t<br>s<br>beta frac right ha leftS n2<br><!-- End of picture text -->

---

[Up: contents](index.md)
