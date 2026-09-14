---
title: Slcausal
source: https://vanderlaan-lab.org/teach-files/slcausal.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/slcausal.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Slcausal

**Source:** [`slcausal.pdf`](https://vanderlaan-lab.org/teach-files/slcausal.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
+<br>CAUSAL INFERENCE IN<br>POINT-TREATMENT AND<br>LONGITUDINAL STUDIES<br>LECTURE I:<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
INTRODUCTORY STATEMENTS AND<br>OVERVIEW OF COURSE<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>POINT TREATMENT<br>Causal inference distinguishes b etween a study<br>with treatment b eing time-indep endent and<br>longitudinal studies with time-dep endent treat-<br>ment.<br>One is often concerned with estimation of a<br>causal e�ect (a parameter with a causal inter-<br>pretation) of a variable which can b e manip-<br>ulated (Exp osure or Treatment) on an out-<br>come of interest, p ossibly adjusted for other<br>variables.<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


Example: Estimate the (adjusted) causal effect of b eing a current cigarette smoker on the level of forced expiratory volume in one second (FEV) in a cohort of adult white male former and current cigarette smokers from cross-sectional data collected in the Harvard Six Cities Study (Do ckery et al.,  ). See table that includes variables on past smoking history, past respiratory symptoms, age, height and co existent heart disease.


<!-- Start of picture text -->
+ +<br>A CAUSAL MODEL<br>Data Generating Exp eriment : Randomly draw<br>subject from p opulation, measure baseline co-<br>variates  W , assign/measure treatment/exp osure<br>variable A and measure the outcome of inter-<br>est. The data on a randomly selected subject<br>is ( Y, A, W ).<br>Let Ya b e the random variable Y one would<br>have observed, if, p ossibly contrary to the<br>fact, one would have \assigned" A = a . One<br>refers to Ya as a counterfactual variable. The<br>counterfactual distribution/treatment sp eci�c<br>distribution of Ya is the distribution one would<br>observe in the hyp othetical exp eriment in which<br>we set A = a for each subject in the p opula-<br>tion we draw from.<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


Linking counterfactuals to the observed data: Each subject has an underlying vector of counterfactuals ( _Ya,i, a ∈A_ ). If subject _i_ has b een assigned exp osure/treatment _Ai_ in the actual study, then his/her observed _Yi_ equals _YAi_ . The other _Ya,i_ , _a_ = _Ai_ , are all missing. Thus one observes ( _Ai, Yi_ = _YAi, Wi_ ) on each subject. A causal mo del involves mo delling of the effect of _a_ on _Ya_ , p ossibly adjusted for _V ⊂ W_ . An example of a causal mo del: _E_ ( _Ya | V_ ) = _β_ 0 + _β_<sup>_a_</sup> + _β_<sup>_V_</sup> . In this causal linear regression mo del _⃗β_ is a causal parameter.


<!-- Start of picture text -->
+ +<br>ASSOCIATION VERSUS CAUSALITY<br>Regression mo del for observed data:<br>E ( Y | A  ) = α 0 +  α A.<br>Causal regression mo del: For all treatment<br>outcomes a<br>E ( Ya ) = β 0 +  β a.<br>If ⃗α = ⃗β , i.e. if<br>E ( Y | A =  a ) =  E ( Ya ) ,<br>then the regression parameters ⃗β are causal<br>parameters and we say that there is no con-<br>founding.<br>If E ( Y | A = a ) = E ( Ya ), then we say that<br>the e�ect of A on Y is confounded.<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->

- Confounding in terms of prop ensity score: We de�ne _P_ ( _A_ = _a |_ subjects characteristics )

- as the prop ensity score. Formally, the subjects characteristics are de�ned by _{Ya_ : _a ∈ A}_ and the measured covariates. In words, it equals the probability on a particular treatment, given the subject. In a study where one collects ( _Y, A_ ) on each subject, but no additional covariates, we say that _A_ is randomized if _P_ ( _A_ = _a |_ subjects characteristics ) = _P_ ( _A_ = _a_ ) _._

- In a study where one collects ( _Y, A, W_ ) on each subject we say that _A_ is randomized if _P_ ( _A_ = _a |_ subjects characteristics ) = _P_ ( _A_ = _a | W_ ) _._

In words: the treatment variable is randomized if the probability on a particular treatment outcome is a function of the observed covariates only. One also refers to this assumption as the assumption of no unmeasured confounders. If _A_ is randomized in a study collecting data ( _Y, A_ ), then _E_ ( _Y | A_ = _a_ ) = _E_ ( _Ya_ ) _._ If _A_ is randomized in a study collecting data ( _Y, A, W_ ), then _E_ ( _Y | A_ = _a, W_ ) = _E_ ( _Ya | W_ ) _._ Classic example of confounding: \Carrying matches" is asso ciated with lung cancer, but \carrying matches" do es not cause lung


<!-- Start of picture text -->
cancer.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>OBSERVATIONAL VERSUS RANDOMIZED.<br>In a randomized study (e.g. clinical trial) the<br>assignment of treatment is under control of<br>the exp erimenter. In this case the prop ensity<br>score is known.<br>In an observational study the prop ensity score<br>is unknown, but one can still hop e/arrange<br>that the assumption of no unmeasured con-<br>founder holds by collecting as many p otential<br>confounders as p ossible.<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>EXAMPLE<br>Consider a study involving pregnant women<br>and let the outcome Y of interest b e the in-<br>dicator of a birth defect.<br>Data: On n subjects we observe Y and sev-<br>eral variables of interest such as the level A<br>of alcohol consumption and smoking.<br><!-- End of picture text -->


<!-- Start of picture text -->
Question: Do es smoking/alcohol consump-<br>tion have a causal e�ect on the presence of a<br>birth defect? In other words, if we would force<br>each women in the p opulation to stop smok-<br>ing and drinking during pregnancy, would that<br>decrease the numb er of birth defects?<br>Linear regression approach: Assume<br><!-- End of picture text -->

_Y_ = _α_ 0 + _α_<sup>_A_</sup> + error _._ Estimate _α_ with linear regression of _Y_ on _A_ .


<!-- Start of picture text -->
+<br><!-- End of picture text -->


Confounding: Large p ercentage of woman who smoke and drink have stressful jobs and bad eating habits. Thus even when there is no causal e�ect of smoking/drinking one might �nd that _α >_ ^ 0. Adding confounders to the linear regression mo del? This is not solving the question! Key to solution: Use causal linear regression mo del: For each smoking/drinking level _a_ let _Ya_ b e a random variable whose distribution equals the p opulation distribution of _Y_ if each subject would smoke/drink at level _a_ . Mo del dep endence of _Ya_ on _a_ : For example, assume _Ya_ = _β_ 0 + _β_<sup>_a_</sup> + error and estimate _β_ .

+ + EXAMPLE Breast Cancer Data A clinic in Germany collected data on women with breast cancer. At the time of detection, the tumor was surgically removed and variables were recorded that are b elieved to re�ect the progression and severity of disease (for example, tumor size, tumor typ e and the numb er of lymph no des involved). After surgery, each woman either received chemotherapy or not. The time until tumor recurrence is the outcome of interest and it is subject to right-censoring. Question: Do es chemotherapy have a causal e�ect on time till tumor recurrence? Would the time till recurrence distribution improve if each woman would receive chemotherapy? Asso ciation metho d: Compare survival (KaplanMeier) estimate in treatment group with sur+

vival estimate in non-treatment group. Confounding: Women with a p o orer prognosis were more likely to receive aggressive treatment, i.e. chemotherapy. Causal metho d: Estimate treatment sp eci�c p opulation distributions.


<!-- Start of picture text -->
+ +<br>TOPICS RELEVANT FOR THIS COURSE<br>• Graphical conditions for identifying a causal<br>e�ect. Confounding de�ned by graphical<br>criteria.<br>• Nonparametric structural equation mo del<br>for a graphical mo del.<br>• Direct and indirect e�ects (Robins and<br>cowork<br>ers)<br>• Non compliance in randomized studies (Robins<br>and cowork<br>ers).<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
• Marginal Structural Mo dels: Estimation<br>and Inference (Robins).<br>Pap ers:<br>) \Causal diagrams in epidemiologic research"<br>by Greenland, Pearl and Robins (  ).<br>) \Causal diagrams in empirical research" by<br>Pearl (  ) with discussions.<br>) \Why there is no statistical test for con-<br>founding, why many think there is, and why<br>they are almost right" (Pearl,  ).<br>) \Statistics, Causality and Graphs" (Pearl,<br> ).<br>) \Marginal Structural Mo dels" (Robins,  )<br>) \Estimating Exp osure E�ects by mo delling<br>the exp ectation of exp osure conditional on<br>confounders" (Robins, Mark,  ).<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>Longitudinal Studies.<br>In a longitudinal study one collects data on a<br>subject over time. Let A  ( · ) b e a treatment<br>pro cess, where A  ( k ) denotes the treatment<br>the subject receives at time k ∈{ , , , , . . .} .<br>Let Y ( · ) b e an outcome pro cess where Y ( k )<br>denotes the outcome measured b etween time<br>A  ( k− ) and  A  ( k ), preceding  A  ( k ). Let  L  ( · ) b e<br>a covariate pro cess, where L  ( k ) represents the<br>covariates measured b etween<br>time A  ( k − )<br>and A  ( k ), preceding A  ( k ).<br>The data generation pro cess can b e thought<br>of as a sequence of exp eriments over time,<br>where the exp eriment at time k is conditional<br>on the observed past. Treatment is now seqe-<br>untially randomized if the treatment assign-<br>ment A  ( k ) in exp eriment k , conditional on<br>the past, is randomized (de�ned as in the<br>+<br><!-- End of picture text -->

p oint exp osure study). In other words, the treatment assignment _A_ ( _k_ ) is only based on the data available at that p oint in time: i.e. _A_ () _, . . . , A_ ( _k−_ ), _L_ () _, . . . , L_ ( _k_ ), _Y_ () _, . . . , Y_ ( _k_ ). Causal Inference in longitudinal studies is very delicate if there exist time-dep endent covariates which predict future treatment (i.e. are a p otential confounder) and are on the causal pathway from treatment to the outcome: Make a picture: ) treatment() e�ects covariate(), ) covariate() e�ects treatment() and future outcome etc. Give example (treatment, cholesterol and heart disease) of p oint-exp osure study where one uses the _G_ -computation formula adjusting for a variable on the causal pathway from _A_ to _Y_ , showing that the _G_ -computation formula gives a useless answer.

Example I: Consider a study of the e�ect of p ost-menopausal o estrogen on cardiac mortality in which one collects as time-dep endent covariate the cholesterol level. Cholesterol level predicts cardiac mortality. Cholesterol level also predicts future treatment since physicians withdraw women from o estrogens at the time they develop an elevated cholesterol level. Being on o estrogens might e�ect the future cholesterol level. Example I I: Consider an observational study of the e�cacy of breast cancer screening (treatment/exp osure) on mortality in which one collects also the time-dep endent covariate \operative removal". Op erative removal predicts mortality. After op erative removal the screening (treatment) stops. \Op erative removal" is on the causal pathway

from \Being screened" to death. Example I I I: Consider an observational study of the e�ect of AZT-treatment on times to AIDS in HIV-infected subjects in which CDcount is a measured time-dep endent covariate. CD predicts death and treatment and is on the causal pathway from AZT to time till AIDS.


<!-- Start of picture text -->
+ +<br>QUESTIONS OF INTEREST.<br><!-- End of picture text -->

- The di�erence b etween (parameters of ) the treatment sp eci�c outcome distributions corresp onding with \never treat" and \always treat", p ossibly adjusted for baseline covariates.

- _•_ Estimation of the treatment sp eci�c outcome distributions corresp onding with a given set of p ossible treatment stategies, p ossibly dynamic treatment stategies, p ossibly adjusted for baseline covariates.

- Optimal treatment strategy.


<!-- Start of picture text -->
+<br><!-- End of picture text -->

- Given a subject made it up till p oint _t_ and given its covariate and treatment history 0

up till p oint _t_ , what is the di�erence b e- tween the treatment sp eci�c outcome distributions corresp onding with \treating at p oint _t_ and never after" and \not treating at p oint _t_ and never after".


<!-- Start of picture text -->
+ +<br>TOPICS ADDRESSED IN THIS COURSE<br>• Marginal Structural Mo dels.<br>• Structural Nested Mo dels.<br>Pap ers:<br>) The control of confounding by intermedi-<br>ate variables (Robins,  ).<br>) Estimation of e�ects of sequential treat-<br>ments by reparametrizing directed acyclic graphs<br>(Robins, Wasserman,  ). ) Marginal struc-<br>tural mo dels and causal inference in epidemi-<br>ology (Robins,    ).<br>) Structural nested failure time mo dels (Robins,<br>Estimation of the causal e�ect of a<br> ). )<br>time-varying exp osure on the marginal mean<br>of a rep eated binary outcome (Robins, Hu,<br>+<br><!-- End of picture text -->

  ). ) Estimation of the time-dep endent accelerated failure time mo del in the presence of confounding factors. ) G-estimation of causal e�ects: Isolated Systolic Hyp ertension and cardiovascular death in the Framingham study (Witteman et al.   ). ) Adjusting for di�erential rates of prophylaxis therapy for PCP in high versus low-dose AZT treatment arms in an AIDS randomized trial (Robins, Greenland,   ). ) G-estimation of the e�ect of prophylaxis therapy for pneumo cystis carinii pneumonia on the survival of AIDS patients (Robins et al.,   ). 0) Correcting for non-compliance in randomized trials using rank preserving structural nested failure time mo dels (Robins,   ). ) Correction for non-compliance in equiva-


<!-- Start of picture text -->
lence trials (Robins,   ).<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
PART I I: CAUSAL GRAPHS<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>CAUSAL GRAPH RESEARCH<br>Pearl (  ) develop es a formal theory for<br>evaluating and identifying causal e�ects of<br>single treatment variables using the language<br>of causal graphs.<br>Robins (many pap ers) provides an actual for-<br>mula for the counterfactual distributions in<br>terms of the observed data distribution in lon-<br>gitudinal studies under the assumption of se-<br>quential randomization. This formula is called<br>the G -computation formula which is very sim-<br>ple in the single treatment case.<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


The following lectures are concerned with showing how diagrams can serve as a visual yet logically rigorous aid for ) summarizing assumptions ab out a problem, ) identifying variables that must b e measured and controlled to obtain unconfounded e�ect estimates.


<!-- Start of picture text -->
+<br>GRAPH TERMINOLOGY<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
Consider the graph in Figure . In this exam-<br>ple, A is air-p ollution level, B is sex (b oy or<br>girl), C is bronchial activity, E is antihistamine<br>treatment, D is astma.<br>ARC, EDGE: line or arrow connecting two<br>variables.<br>ADJACENT: A and C are adjacent.<br>Single headed arrows represent direct links from<br>causes to e�ects.<br>NODES.<br>PATH is any unbroken route traced out along<br>or against arrows or lines connecting adjacent<br>no des: e.g. E-C-D is a path.<br>DIRECTED PATH/ CAUSAL PATH<br>no de INTERCEPTS the path.<br>X is an ANCESTOR or CAUSE of Y if there<br>is a directed path from X to Y .<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
Then Y is a DESCENDANT of X or AF-<br>FECTED by X .<br>X PARENT of Y.<br>Y CHILD of X, X is DIRECTLY AFFECTED<br>by Y .<br>Unsp eci�ed common ancestors are denoted<br>with U , with dashed arrows to the variables<br>it a�ects.<br>DIRECTED GRAPH: all arcs b etween vari-<br>ables are arrows (single or double headed).<br>ACYCLIC GRAPH: no directed path forms a<br>closed lo op.<br>Abbreviation for directed acyclic graph: DAG.<br>A path that connects X to Y is a BACK<br>DOOR PATH from X to Y if it has an ar-<br>rowhead p ointing to X . Figure : all path<br>from E to D except the direct path are back<br><!-- End of picture text -->


<!-- Start of picture text -->
do or paths.<br><!-- End of picture text -->

A path COLLIDES at a variable _X_ if the path enters and exits _X_ through arrowheads, in which case _X_ is called a collider on the path. A path is BLOCKED if it has one or more colliders, otherwise UNBLOCKED. See �gure : the back do or path EACBD is blo cked b ecause it collides at _C_ . E-A-C-D is unblo cked. CAUSE: _A_ is a cause of _C_ . De�nition: A directed acyclic graph _G_ is a CAUSAL GRAPH if for each no de _Xi_ with parents ( _PA_ ) _i_ we have _Xi_ = _fi_ (( _PA_ ) _i, ϵi_ ) with _fi_ b eing a deterministic function and _ϵi, i_ = _, . . . , m_ , are all indep endent, and _ϵi_ is also indep endent of ( _PA_ ) _i_ , _i_ = _, . . . , m_ .

Let _A, Y_ b e two no des in the causal graph, where we have an arrow going from _A_ to _Y_ . The counterfactual distribution of _Ya_ is de�ned by ) delete the equation corresp onding with _Xi_ = _A_ . ) Set _A_ = _a_ in all the other equations. Let ( _L, U_ ) represent all non-descendants of _A_ . In a causal graph we have that _P_ ( _A_ = _a |_ ( _Ya, a ∈A_ ) _, L, U_ ) = _P_ ( _A_ = _a | L, U_ ), i.e. _A_ is randomized w.r.t. observing the whole graph. DEFINITION OF CONFOUNDING: In a causal DAG we say that the e�ect of _A_ on _Y_ is confounded if there is an unblo cked back do or path from _A_ to _Y_ .


<!-- Start of picture text -->
+ +<br>STATISTICAL GRAPH<br>Let X , . . . , Xm b e m variables. Supp ose f ( xi |<br>x where is a<br>, . . . , x i− ) = f ( xi | ( pa ) i ), ( pa ) i<br>subset of ( x , . . . , x i− ). If we refer to ( x , . . . , x i− )<br>as the ancestors of xi , then this says that Xi is<br>indep endent of its ancestors, given its parents<br>( PA  ) i . In this case the density of ( X , . . . , Xm )<br>is given by:<br>m<br>=<br>p ( X , . . . , Xm ) � p ( Xi | ( PA  ) i ) .<br>i =<br>This likeliho o d of ( X , . . . , X m ) corresp onds<br>with a STATISTICAL GRAPH de�ned by the<br>no des X , . . . , X n , where no de Xi has incom-<br>ing arrows from ( PA  ) i .<br>Remark: A causal graph is also a statistical<br>graph. A statistical graph is not necessarily a<br>causal graph.<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>d-SEPARATION IN STATISTICAL GRAPH<br>d-SEPARATION: Let R , T and S b e three<br>sets of no des in the graph. We say that<br>R and T are d-separated by S if every un-<br>blo cked path, including paths generated by<br>adjustment for variables in S , from T to R<br>is intercepted by a variable in S .<br>We can also say: S blo cks every path b etween<br>R and T .<br>In a statistical graph we have that ⃗Z is in-<br>dep endent of ⃗Z , given a third vector ⃗Z (all<br>three vectors should b e distinct) if ⃗Z and ⃗Z<br>are d-SEPARATED by ⃗Z .<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
The converse is not necessarily true: Figure<br>has a direct path and four back-do or paths<br>b etween E and D . Each path transmits an as-<br>so ciation, but these asso ciations might can-<br>cel one another out. However, this always<br>involves p erfect cancellations so that for all<br>practical purp oses one is allowed to read \A<br>and B are d-separated by C " as \A and B are<br>indep endent, given C ".<br>One says that the joint distribution  p ( X , . . . , Xm )<br>is faithfull to the statistical graph if we have<br>that ⃗Z is indep endent of ⃗Z , given a third<br>vector ⃗Z IF AND ONLY IF ⃗Z and ⃗Z are<br>d-SEPARATED by ⃗Z .<br>See �gure and for a graphical illustrati on<br>for the following: Marginally A and B are not<br>asso ciated since A and B are d -separated, but<br>A and B are asso ciated within stata of C .<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>SUFFICIENT SET OF ADJUSTMENT<br><!-- End of picture text -->

Let _A, Y_ Let _L_ b


<!-- Start of picture text -->
Let A, Y b e two no des in the statistical graph.<br>Let L b e a set of other no des in the graph,<br>b eing non-descendents of A  . Denote the<br>remaining non-descendents of A with U .<br>Let b ( y | a ) b e the G -computation formula<br>(Robins):<br>=<br>b ( y | a ) p ( y | a, l, u  ) dP ( l, u  ) .<br>�<br>If A is randomized for the data ( Y, A, L, U ),<br>i.e. A is indep endent of Ya , given L, U , for<br>each a , then b ( y | a ) = P ( Ya = y ). This holds,<br>in particular, if G is a causal graph.<br>However, supp ose U is not observed. Then<br>this G -computation formula is not useful b e-<br>cause it cannot b e estimated from data. There-<br>fore it is of interest to understand under what<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
conditions we have that L is a su�cient set<br>of adjustment: i.e.<br>b ( y | a ) = b ∗ ( y | a )  ≡ p ( y | a, l ) dP ( l ) .<br>�<br>Back do or path condition: We say that<br>there is no back do or path from A to Y if<br>Y is d -separated from A in GA , where GA is<br>the graph obtained from G by deleting all out-<br>going arrows from A  .<br>.<br>Notation: A ⊥d Y<br>We say that there is no back do or path from<br>A to Y , controlling for L  , if Y and A are d-<br>separated by L in GA .<br>Notation: A ⊥d Y | L  .<br>Theorem If there is no back do or path from<br>A to Y controlling for L  , then L is su�cient<br>for adjustment: i.e.<br>b ( y | a ) =  b ∗ ( y | a ) .<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>ALTERNATIVE CRITERIA<br>Theorem U can b e split up in U , U where<br>U ⊥ d A | L in G (cho ose U maximal set) and<br>U ⊥ d Y | ( A, L, U ) in G<br>⇐⇒<br>Y ⊥d A | L in GA , i.e. there is no back do or<br>path from A to Y controlled for L  .<br>So a statistical graph can b e used to deter-<br>mine a su�cient set of variables L to adjust<br>for to compute b ( y | a ). However, then we<br>still wonder = P We know<br>if b ( y | a ) ( Ya = y )?<br>that this is true if P ( A = a | ( Ya, a ∈A ) , L  ) =<br>P ( A = a | L  ) (the randomization assumption<br>holds). This assumption holds if the statisti-<br>cal graph happ ens to b e a causal graph, but<br>if it is not, then this is still an op en question.<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>TWO APPROACHES<br>Therefore we have the following two approaches<br>for determing a correct formula for P ( Ya = y )<br>using graph theory:<br>Statistical Graph: Using the statistical graph,<br>determine a su�cient set of variables L to ad-<br>just for, i.e. such that there is not back do or<br>path from A to Y controlled for L  . This guar-<br>antees that b ( y | a ) = b ∗ ( y | a ).<br>Now, just assume/hop e/reason that the ran-<br>domization assumption holds  P ( A = a | ( Ya, a ∈<br>A ) , L  ) = P ( A = a | L  ). Then the  G -computation<br>formula b ∗ ( y | a ) only adjusting for L equals<br>P<br>( Ya = y ).<br>Causal Graph: Using a causal graph (thus<br>needing a much stronger set of assumptions<br>p ertaining a causal graph), determine a su�-<br>cient set of variables L to adjust for, i.e. such<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
that there is not back do or path from A to<br>Y controlled for L  . Then the G -computation<br>formula b ∗ ( y | a ) only adjusting for L equals<br>P<br>( Ya = y ).<br>Note that the statistical graph theory is appli-<br>cable under fewer assumptions, but if one is<br>able to assume a causal graph, then that guar-<br>antees selection of a su�cient set of variables<br>L to truly estimate P ( Ya = y ).<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>STATISTICAL CRITERIA.<br>The graphical condition \ U can b e split up in<br>U , U where U ⊥ d A | L in G and U ⊥ d Y |<br>( A, L, U ) in G " for  b ( y | a ) = b ∗ ( y | a ) is a little<br>stronger than needed since b ( y | a ) = b ∗ ( y | a )<br>is only a statement in terms of distributions.<br>The following theorem for determining if b ( y |<br>a ) =  b ∗ ( y | a ) assumes only a purely statistical<br>assumption.<br>Theorem (Statistical criteria) If U can b e<br>split up in U , U where U is indep endent of<br>A  , given L and U is indep endent of Y , given<br>( A, L, U ), then b ( y | a ) = b ∗ ( y | a ).<br>So it can happ en that L do es not d -separate<br>A and Y in GA in the causal graph G , while<br>the statistical criteria holds. In that case we<br>still have b ∗ = P for the ef-<br>( y | a ) ( Ya = y ).<br>fect of A on Y . These examples involve p er-<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
fect cancellations and are therefore not prac-<br>tically relevant. The statistical criteria for<br>= b ∗ can b e tested based on<br>b ( y | a ) ( y | a )<br><!-- End of picture text -->

data, though.


<!-- Start of picture text -->
+<br>DEFINING NON-CONFOUNDING<br>IN A CAUSAL GRAPH<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
Graphical conditions for non-confounding<br>in a causal graph. Supp ose that the graph<br>is causal. If there is no back do or path from<br>A to Y , then the e�ect of A on Y is NOT<br>confounded.<br>If there is no back do or path from A to Y<br>controlling for L (i.e. Y is d -separated from A<br>by L in GA ), then the e�ect of A on Y within<br>stata of L is unconfounded and we call L suf-<br>�cient set for adjustment.<br>Thus if L is a su�cient set for adjustment for<br>the e�ect of A on Y , then the G -computation<br>formula b ∗ ( y | a ) only adjusting for L equals<br>P ( Ya = y ). Thus in this case one can es-<br>timate the counterfactual distribution of Ya<br>+ 0<br><!-- End of picture text -->

if one measures _L_ (the other p otential confounders _U_ do not need to b e measured). Thus if one is able to provide a causal graph b efore planning a study to determine a (adjusted) causal e�ect of _A_ on _Y_ , then one can use this causal graph to determine which variables need to b e measured b eyond ( _A, Y_ ).


<!-- Start of picture text -->
+ +<br>UNNECESSARY ADJUSTMENT<br>Consider a causal graph.<br>Unnecessary adjustment and harmful ad-<br>justment: One can have that the e�ect of A<br>on Y is not confounded marginally (no back<br>do or path in GA ), but that the e�ect of A on<br>Y , within strata C , is confounded.<br>See Figure .<br>LESSON: Adjustment for variables (such as<br>C in Fig ) that are not necessary to con-<br>trol may necessitate adjustment for even more<br>variables, and there might not b e anymore<br>that would remove the bias (see Figure ).<br>As a consequence the following can happ en:<br>the marginal G -computation formula might<br>represent the causal e�ect of A on Y (i.e.<br>P ( Ya = y )) while the adjusted G -computation<br>formula do es NOT represent an adjusted causal<br>e�ect (i.e. P ( Ya =  y | C ))!<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
If one has the causal graph available, then one<br>can prevent this to happ en, but otherwise this<br>is an actual risk.<br>To give a concrete example: the data is  E, D, F<br>and the true causal graph is Fig which we<br>do not know. Our goal is to o estimate the<br>marginal causal e�ect of E on D . Supp ose<br>we worry ab out F b eing a confounder and<br>therefore we use the G -computation formula<br>adjusting for F (WRONG), while we could<br>have used the marginal G -computation for-<br>mula (CORRECT).<br>EXAMPLE of adjustment induced bias: In<br>studies of estrogen (E) and endometrical can-<br>cer (D), some researchers attempted to con-<br>trol for detection bias by stratifying on uterine<br>bleeding (F), which could b e caused by either<br><!-- End of picture text -->

estrogen or cancer, as in Figure . The association b etween estrogen and cancer withing levels of bleeding was drastically reduced by this strati�cation (likely due to bias pro duced by the adjustment). EXAMPLE (Healthy worker survivor e�ect): Unmeasured health conditions in�uence decision to leave work. Then leaving work is asso ciated with mortality, even when it has no causal e�ect on mortality. Let the exp o- sure (E) b e job-assignment, which in�uences worker decisions to leave work (L). Fig is the causal graph for this scenario. The e�ect of E on D is marginally unconfounded but within strata of _L_ the e�ect of E on D is confounded.


<!-- Start of picture text -->
+ +<br>MINIMAL SUFFICIENT SET<br>FOR ADJUSTMENT<br>A set L is minimall y su�cient for adjustment<br>if L is su�cient for adjustment, but no prop er<br>subset of L is su�cient.<br>Fig : {A, C} and {B, C} are minimal su�-<br>cient.<br>Fig : {A, C} and {B, C} are su�cient, but<br>not minimal su�cient.<br>To �nd a minimall y su�cient set we may se-<br>quentially delete variables from a su�cient set<br>until no more variables can b e dropp ed with-<br>out the new set failing the back do or test (i.e.<br>not b eing su�cient anymore).<br>Fact: L can b e su�cient while adding vari-<br>ables to L can lead to an insu�cient set.<br>Fig : L =  {} is su�cient, but {C} is not suf-<br>�cient.<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
�cient.<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
Fact: There may exist several di�erent mini-<br>mal su�cient sets.<br>Fig : {A, B, C} and {F } are minimall y suf-<br>�cient sets of adjustment.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>IDENTIFIABILITY OF CAUSAL EFFECTS<br>IN A CAUSAL GRAPH<br>Given a causal graph, supp ose that one can-<br>not �nd observed covariates L so that A and<br>Y are d-separated, given L  . This do es not<br>imply that the causal e�ect of A on Y is not-<br>identi�ed, but there do es not exist one stan-<br>dard formula such as the G -computation for-<br>mula. The approach is the following. Let<br>( L, U ) b e a su�cient set for adjustment, i.e.<br>A ⊥d Y | ( L, U ), but the comp onents U will<br>not b e observable. Then we still have the G -<br>computation formula (using Pearl's notation):<br>P ( Y = y | ^ a ) = P ( Y =  y | A = a, L = l, U = u  ) dFL,U<br>�<br>The causal graph is a statistical graph and<br>thus we have a sp ecial structure of the den-<br>sity of all no des in the graph. Using the<br>conditional indep endence assumptions of the<br>+<br><!-- End of picture text -->

statistical graph can sometimes b e used to eliminate _U_ from the _G_ -computation formula. This is a purely algebraic excercise. If one succeeds in doing this then one has proved that _P_ ( _Y_ = _y |_ ^ _a_ ) is still identi�able. Pearl (  ) develop es a \Calculus of Intervention" for causal graphs which can b e helpful in carrying out this excercise. Theorem earl (P   ) Rule (insertion/deletion of observation): _P_ ( _Y_ = _y |_ ^ _a, Z, W_ ) = _P_ ( _Y_ = _y |_ ^ _a, W_ ) if _Y ⊥d Z |_ ( _A, W_ Rule (action/observation exchange): _P_ ( _Y_ = _y |_ ^ _a, z, W_ ^ ) = _P_ ( _Y_ = _y |_ ^ _a, Z_ = _z, W_ ) if _Y ⊥d Z_ Rule (insertion/deletion of actions): _P_ ( _Y_ = _y |_ ^ _a, z, W_ ^ ) = _P_ ( _Y_ = _y |_ ^ _a, W_ ) if _Y ⊥d Z |_ ( _A, W_ where _Z_ is the set of _Z_ -no des that are ( _W_ ) � not ancestors of any _W_ -no de in _G_ . _X_


<!-- Start of picture text -->
With the help of this calculus one can prove<br>the following theorem:<br>Theorem. (The front do or criterion) Sup-<br>p ose a set of variables Z satis�es the follow-<br>ing conditions relative to an ordered pair of<br>variables ( A, Y ).: (i) Z intercepts all directed<br>paths from A to Y , (ii) there is no back do or<br>path b etween A and Z , and (iii) every back<br>do or path b etween Z and Y is blo cked by A  .<br>Then the causal e�ect of  A on  Y is identi�able<br>and given by:<br><!-- End of picture text -->


<!-- Start of picture text -->
P ( Y = y | ^ a ) = � P ( Z = z | A =  a ) � P ( Y = y | A<br>a a ′<br><!-- End of picture text -->


<!-- Start of picture text -->
=<br><!-- End of picture text -->

Consider Figure of Pearl   .


<!-- Start of picture text -->
+ +<br>IDENTIFIABILITY OF CAUSAL EFFECTS<br>IN A CAUSAL GRAPH<br>Given a causal graph, supp ose that one can-<br>not �nd observed covariates L so that A and<br>Y are d-separated, given L  . This do es not<br>imply that the causal e�ect of A on Y is not-<br>identi�ed, but there do es not exist one stan-<br>dard formula such as the G -computation for-<br>mula. The approach is the following. Let<br>( L, U ) b e a su�cient set for adjustment, i.e.<br>A ⊥d Y | ( L, U ), but the comp onents U will<br>not b e observable. Then we still have the G -<br>computation formula (using Pearl's notation):<br>P ( Y = y | ^ a ) = P ( Y =  y | A = a, L = l, U = u  ) dFL,U<br>�<br>The causal graph is a statistical graph and<br>thus we have a sp ecial structure of the den-<br>sity of all no des in the graph. Using the<br>conditional indep endence assumptions of the<br>+<br><!-- End of picture text -->

statistical graph can sometimes b e used to eliminate _U_ from the _G_ -computation formula. This is a purely algebraic excercise. If one succeeds in doing this then one has proved that _P_ ( _Y_ = _y |_ ^ _a_ ) is still identi�able. Pearl (  ) develop es a \Calculus of Intervention" for causal graphs which can b e helpful in carrying out this excercise.


<!-- Start of picture text -->
Theorem earl<br>(P   )<br>Rule (insertion/deletion of observation):<br>P ( Y = y | ^ a, Z, W ) = P ( Y = y | ^ a, W )<br>�<br>if Y ⊥d Z | ( A, W ) in GA .<br>Rule (action/observation exchange):<br>P ( Y = y | ^ a, z, W ^ ) = P ( Y = y | ^ a, Z = z, W )<br>�<br>if Y ⊥d Z | ( A, W ) in GAZ .<br>Rule (insertion/deletion of actions):<br>P ( Y = y | ^ a, z, W ^ ) = P ( Y = y | ^ a, W )<br>�<br>if Y ⊥d Z | ( A, W ) in G , where Z ( W ) is<br>AZ ( W )<br>the set of Z -no des that are not ancestors of<br>�<br>any W -no de in G .<br>A<br><!-- End of picture text -->

With the help of this calculus one can prove the following theorem: Theorem. (The front do or criterion) Supp ose a set of variables _Z_ satis�es the following conditions relative to an ordered pair of variables ( _A, Y_ ): (i) _Z_ intercepts all directed paths from _A_ to _Y_ , (ii) there is no back do or path b etween _A_ and _Z_ , and (iii) every back do or path b etween _Z_ and _Y_ is blo cked by _A_ . Then the causal e�ect _P_ ( _Y_ = _y |_ ^ _a_ ) of _A_ on _Y_ is identi�able and given by:


<!-- Start of picture text -->
Consider Figure of Pearl   .<br>Example: This graphical criterion p ermits<br>identi�cation of causal e�ects by measuring<br>variables that are a�ected by treatment. Let<br>A b e smoking,  Y lung cancer and  Z the amount<br>of tar dep osited in subject's lungs, U are un-<br>measured confounders of the e�ect of smo ok-<br>ing.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>Pro of of front do or criterion.<br>Task : P ( Z = z | x ^) = P ( Z = z | x ) using<br>rule .<br>Task : Compute P ( Y = y | z ^).<br>P z ^ = P z ^ z ^<br>( Y = y | ) � ( Y = y | X = x, ) P ( X = x | ) .<br>x<br>By rule : P ( X = x | z ^) = P ( X = x ) (i.e.<br>manipulating Z has no e�ect on X b ecause Z<br>is a descendant of X in G .) By rule :<br>P ( Y = y | X =  x, z ^) =  P ( Y = y | X = x, Z = z )<br>if Z ⊥d Y | X in GZ . Thus we conclude:<br>P z ^ = P<br>( Y = y | ) � ( Y = y | X =  x, z ) P ( X = x )<br>x<br>= =  z<br>EXP ( Y = y | X, Z ) .<br>Task : Compute P ( Y = y | x ^). We have:<br>P = P<br>( Y =  y | x ^) � ( Y =  y | Z = z, x ^) P ( Z = z | x ^)<br>z<br>= P<br>� ( Y =  y | Z = z, x ^) P ( Z = z | X = x ) .<br>z<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
By rule<br><!-- End of picture text -->

_P_ = _P_ ( _Y_ = _y | Z_ = _z, x_ ^) ( _Y_ = _y | z,_ ^ _x_ ^) � since _Y ⊥d Z | X_ in _GXZ_ . By rule we have: _P_ ( _Y_ = _y | z,_ ^ _x_ ^) = _P_ ( _Y_ = _y | z_ ^) since _Y ⊥d X | Z_ in _GXZ_ . Thus we have: _P_ = _P z_ ^ ( _Y_ = _y | Z_ = _z, x_ ^) ( _Y_ = _y |_ ) _._ In task we already calculated _P_ ( _Y_ = _y | z_ ^). Thus we have shown _P_ ( _Y_ = _y | x_ ^) equals � _P_ ( _Z_ = _z | x_ ) � _P_ ( _Y_ = _y | x_<sup>_′_</sup> _, z_ ) _P_ ( _X_ = _x_<sup>_′_</sup> ) _. z x_<sup>_′_</sup>


<!-- Start of picture text -->
+ +<br>CAUSAL INFERENCE BY<br>SURROGATE EXPERIMENTS<br>Supp ose we wish to learn the causal e�ect of<br>A on Y when P ( y | ^ a ) is not identi�able (due<br>to unmeasured confounders) and for practi-<br>cal (ethical) reasons we cannot randomize A  .<br>Can we identify P ( y | ^ a ) by randomizing a<br>surrogate variable Z which is easier to control<br>than A  . For example, A is cholesterol level, Y<br>is heart disease and Z is diet.<br>Theorem: If (i)  A intercepts all directed paths<br>form Z to Y and (ii) P ( Y | ^ a ) is identi�able<br>in GZ � (the causal graph in which all incoming<br>arrows in Z are<br>deleted).<br>Pro of. If (i) holds, we have P ( y | ^ a ) = P ( y |<br>�<br>^ a, z ^) since Y ⊥d Z | A in GAZ � . P ( y | ^ a, z ^) is the<br>causal e�ect of A on Y in the causal graph<br>GZ � which is identi�able by (ii).<br>+<br><!-- End of picture text -->

Translated to our cholesterol example, there should b e no direct e�ect of diet on heart disease and no confouding e�ect b etween cholesterol and heart disease, unless we can measure an intermediate variable b etween the two. See �gures e and h????


<!-- Start of picture text -->
+ +<br><!-- End of picture text -->


<!-- Start of picture text -->
PART I I I: G-COMPUTATION<br>FORMULA<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>G-COMPUTATION IN LONGITUDINAL STUD<br>Let  A  ( j ) b e treatment assigned at time  j , L  ( j )<br>covariate values measured after A  ( j − ) and<br>b efore A  ( j ), j = 0 , . . . , K . Let Y = LK + b e<br>the outcome of interest. Then the temp oral<br>ordering of all measured variables is given by:<br>L  (0) , A  (0) , L  () , . . . , L ( K ) , A  ( K ) , Y = L  ( K +) .<br>Meaning of temp oral ordering: The fu-<br>ture variables cannot a�ect the past variables:<br>e.g. the is not<br>counterfactual L  (0) A  (0)= a  (0)<br>a�ected by a (0).<br>The corresp onding density representation is<br>given by:<br>f ( v ) = f ( l 0 ) f ( a 0 | l 0 ) f ( l | a 0 , l 0 )  . . . f ( lK + | � lK, � aK ) .<br>Given a treatment vector � a ∗ , the density  f � a ∗ ( v ) =<br>f � a ∗ ( y, � lK ) is de�ned by the density f ( v ) except<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
that f ( aj | � aj− , � lj ) is replaced by a degener-<br>ate distribution at a ∗ .<br>j<br>By integrating out � lK in this joint density  f � a ∗ ( v )<br>we can obtain the marginal density f � a ∗ ( y ):<br>K<br>. . . f ( y | � lK, � a ∗ K ) � f ( lj | � lj− , � a ∗ j− ) dµ  ( lj ) .<br>� �<br>j =<br>Thus the marginal distribution F � a ∗ is given by:<br>K<br>. . . P ( Y < y | � lK, � a ∗ K ) � f ( lj | � lj− , � a ∗ j− ) dµ  ( lj ) .<br>� �<br>j =<br>Robins refers to this as the G -computation<br>algorithm formula or functional for the e�ect<br>�<br>of treatment action A = � a ∗ on the outcome  Y .<br>If the statistical graph is causal or if treatment<br>assignment of A  ( j ) is sequentially randomized<br>then<br>F � a ∗ ( y ) = P ( Y � a ∗ ≤ y ) .<br><!-- End of picture text -->

Let's state this as a theorem.

Theorem. Supp ose the ordering


<!-- Start of picture text -->
L  (0) , A  (0) , L  () , . . . , L ( K ) , A  ( K ) , Y = L  ( K +)<br>is temp oral in the sense that L  ( j ) is only af-<br>�<br>fected by A ( j − ) for j = , . . . , K + . Con-<br>sider the G -computations formulas f � a ∗ ( y, � lK )<br>and f � a ∗ ( y ) corresp onding with this ordering.<br>If<br>�<br>:<br>A  ( j )  ⊥ ( Y � a , L � a � a ∈A ) | L �  ( j ) , A  ( j − ) ,<br>then the  G -computation formula  f � a ∗ ( y, � lK ) equals<br>P =<br>( Y � a ∗ = y, � a ∗ � lK ) .<br>L � K,<br>If<br><!-- End of picture text -->


<!-- Start of picture text -->
then the G -computation formula f � a ∗ ( y equals<br>P<br>( Y � a ∗ = y ) .<br>Pro of. Give the general pro of, see handout<br>(Maja).<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>JAMIE'S HYPOTHETICAL EXAMPLE<br>Let  A 0 b e a randomly assigned treatment (drugs,<br>yes or no) assigned at t 0 , L is indicator of hav-<br>ing develop ed a risk factor such as Pneumonia<br>at time t , A is treatment (AZT) indicator<br>at time t (which can b e based on values of<br>A 0 , L  ) and Y is an outcome at t such as the<br>indicator of b eing alive at t . In this example,<br>we can think of A 0 = as a drug which pre-<br>vents the development of Pneumonia ( L = ).<br>Question : Estimate causal e�ect of A 0 . In<br>other words, estimate  P ( YA = = ) −P ( YA =0 =<br>0 0<br>), where YA =0 ( YA =0 = ) is the counter-<br>0 0<br>factual outcome we would have observed on<br>everyb o dy if everyb o dy gets assigned A 0 = 0.<br>Answer: P ( Y =  | A 0 = ) − P ( Y =  | A 0 =<br>0) = / − 0 / = − / . So marginally<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
treating hurts.<br><!-- End of picture text -->


<!-- Start of picture text -->
Question : Would it have b een wrong to<br>adjust for L in Question ? In other words,<br>would<br>P ( Y =  | A 0 = , L = ) −P ( Y =  | A 0 = 0 , L = )<br>have a causal interpretation.<br>Answer: If a subject develop es Pneumonia<br>( L = ) in spite of treatment A 0 = , then<br>that says something extra ab out the subject<br>relative to a subject who develop ed Pneumo-<br>nia ( L = ) in the control treatment arm  A 0 =<br>0. Formally, since L = LA the conditioning<br>0<br>event A 0 = , L = equals A 0 = , L =<br>while the conditioning event A 0 = 0 , L =<br>= =<br>equals A 0 0 , L 0<br>Question : Supp ose that we would like to<br>know which of the two treatment regimes  A 0 =<br><!-- End of picture text -->


<!-- Start of picture text -->
0 , A = and A 0 = , A = are b est. Then<br>we want to estimate P ( Y = ) −P ( Y 0 = ).<br>How?<br>NAIVE I: P ( Y = | A 0 = 0 , A = )  − P ( Y =<br>| A 0 = , A = ). Wrong since L is a con-<br>founder of A and A a�ects L  .<br>0<br>NAIVE I I: Adjust for L  : P ( Y = | A 0 =<br>= = = = =<br>0 , A , L )  − P ( Y | A 0 , A<br>, L = ). In the example, this di�erence<br>equals / indicating treating at t 0 hurts in<br>the L = strata.<br>Wrong, cannot adjust for covariate a�ected<br>by treatment. As ab ove, having L = in<br>A 0 = group is a very di�erent statement<br>from having L = in A 0 = 0 group.<br>G-COMPUTATION FORMULA:<br><!-- End of picture text -->

_Pa_ 0<sup>_a_</sup> ( _Y_ = _, L_ = _l_ ) = _P_ ( _L_ = _l_ ) _P_ ( _Y_ = _| a_ 0<sup>_, a, l_</sup> ) _._


<!-- Start of picture text -->
P ( Y = ) = /  ∗ / + /  ∗ / = / .<br>And<br>P ( Y 0 = ) =  ∗ 0 / + 0 = / .<br>Note that P ( Y 00 = ) and P ( Y 0 = ) are not<br>identi�ed from data example.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>ALTERNATIVE REPRESENTATION OF<br>G-COMP FORMULA<br>Recall the G -comp formula:<br>K<br>f � a ∗ ( y ) = . . . f ( y | � lK, � a ∗ K ) � f ( lj | � lj− , � a ∗ j− ) dµ  ( lj<br>� �<br>j =<br>This can b e rewritten as:<br>�<br>I A = � a ∗<br>( Y = y, )<br> <br>E<br>�<br>=  a ∗ =<br>� Kj =0 P ( A  ( j ) ( j )  | Aj− � aj− , L � j− )  .<br><!-- End of picture text -->


<!-- Start of picture text -->
+ 0<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>G-COMPUTATION FORMULA<br>Consider a statistical graph for a set of no des<br>X , . . . , X m , where we will assume that these<br>are ordered temp orarily. Then the corresp ond-<br>ing representation of the density of  X , . . . , X m<br>is given by:<br><!-- End of picture text -->

_m_ = _P_ = _p_ ( _x_<sup>_, . . . , xm_</sup> ) � ( _Xi_ = _xi |_ ( _PA_ ) _i_ ( _pa_ ) _i_ ) _, i_ = where _P_ = is the con( _Xii_ = _xii |_ ( _PA_ ) _i_ ( _pa_ ) _i_ ) ditional densityy of _Xii_ , given its parentsrents ( _PA_ ) _i_ in the statistical graph.


<!-- Start of picture text -->
where P = is the con-<br>( Xii = xii | ( PA  ) i ( pa ) i )<br>ditional densityy of Xii , given its parentsrents ( PA  ) i<br>in the statistical graph.<br>Let A b e a subset of the no des ( X , . . . , Xm ).<br>Let's denote the remainder of the no des with<br>( Y, W ), where Y is an outcome variable of in-<br>terest. The G -computational formula for the<br>e�ect of A = a on Y is a functional of this<br>joint density representation: so it dep ends on<br>the ordering of the variables as well.<br>+<br><!-- End of picture text -->

How would you obtain from this joint density the density of ( _Y, W_ ) in the hyp othetical world where we set _A_ = _a_ : Supp ose that the statistical graph is even causal. Then we can represent the world of ( _X_<sup>_, . . . , Xm_</sup> ) by a system of _m_ equations _Xi_ = _φi_ (( _PA_ ) _i, ϵi_ ), _i_ = _, . . . , m_ . What is the distribution of the variables ( _Y, W_ ) if we set _A_ = _a_ in this system? Setting _A_ = _a_ just reduces the numb er of equations since all equations corresp onding with _Xi ∈ A_ are deleted and we set _A_ = _a_ in all other equations. This is just a new causal graph and thus we can write down its corresp onding density.


<!-- Start of picture text -->
If we set A = a (i.e. we intervene by setting<br>A = a , but otherwise remain things as they<br>are), then a new density p ( Y = y, W = w | ^ a )<br>of the graph is obtained by setting the condi-<br>tional densities of no des in A equal to a de-<br>generate density at A =  a :<br>=<br>� mi = P ( Xi =  xi | ( PA  ) i ( pa ) i )<br>=<br>� Xi∈A P ( Xi = xi | ( PA  ) i ( pa ) i )<br>and this object is evaluated at ( x , . . . , xm )<br>corresp onding with ( y, w, a ). This density rep-<br>resents the density of ( Y, W ) in the hyp othet-<br>ical world where we set A =  a .<br>Supp ose we want to obtain a formula for the<br>causal e�ect of setting A = a on an outcome<br>variable Y , where Y is one of the no des. Then<br>we �nd this by integrating out all other vari-<br>ables in p ( Y = y, W = w | ^ a ):<br>=<br>b ( y | a ) ( Y = y, dw | ^ a ) .<br>� w P<br><!-- End of picture text -->

This is the _G_ -computation formula of Robins. If the graph is causal, then this equals _P_ ( _Ya_ = _y_ ). More general, if the necessary (sequential) randomization assumption holds for the data ( _A, Y, W_ ) (i.e. ( _X_<sup>_, . . . , Xn_</sup> )), then this equals _P_ ( _Ya_ = _y_ ).


<!-- Start of picture text -->
+ +<br>G-COMPUTATION IN LONGITUDINAL STUD<br>Let  A  ( j ) b e treatment assigned at time  j , L  ( j )<br>covariate values measured after A  ( j − ) and<br>b efore A  ( j ), j = 0 , . . . , K . Let Y = LK + b e<br>the outcome of interest. Then the temp oral<br>ordering of all measured variables is given by:<br>L  (0) , A  (0) , L  () , . . . , L ( K ) , A  ( K ) , Y = L  ( K +) .<br>Meaning of temp oral ordering: The fu-<br>ture variables cannot a�ect the past variables:<br>e.g. the is not<br>counterfactual L  (0) A  (0)= a  (0)<br>a�ected by a (0).<br>The corresp onding density representation is<br>given by:<br>f ( v ) = f ( l 0 ) f ( a 0 | l 0 ) f ( l | a 0 , l 0 )  . . . f ( lK + | � lK, � aK ) .<br><!-- End of picture text -->


<!-- Start of picture text -->
Given a treatment vector � a ∗ , the density  f � a ∗ ( v )<br>f � a ∗ ( y, � lK ) is de�ned by the density f ( v ) except<br>+<br><!-- End of picture text -->

= )

that _f_ ( _aj |_ � _aj− ,_ � _lj_ ) is replaced by a degenerate distribution at _a_<sup>_∗_</sup> . _j_ By integrating out � _lK_ in this joint density _f_ � _a_<sup>_∗_</sup> ( _v_ ) we can obtain the marginal density _f_ � _a_<sup>_∗_</sup> ( _y_ ): _K f_ � _a_<sup>_∗_</sup> ( _y_ ) = _. . . f_ ( _y |_ � _lK,_ � _a_<sup>_∗_</sup> _K_ ) � _f_ ( _lj |_ � _lj− ,_ � _a_<sup>_∗_</sup> _j−_ ) _dµ_ ( _lj_ � � _j_ = Thus the marginal distribution _F_ � _a_<sup>_∗_</sup> is given by: _K F_ � _a_<sup>_∗_</sup> ( _y_ ) = _. . . P_ ( _Y < y |_ � _lK,_ � _a_<sup>_∗_</sup> _K_ ) � _f_ ( _lj |_ � _lj− ,_ � _a_<sup>_∗_</sup> _j−_ ) � � _j_ = Robins refers to this as the _G_ -computation algorithm formula or functional for the e�ect � of treatment action _A_ = � _a_<sup>_∗_</sup> on the outcome _Y_ . If the statistical graph is causal or if treatment assignment of _A_ ( _j_ ) is sequentially randomized then _F_ � _a_<sup>_∗_</sup> ( _y_ ) = _P_ ( _Y_ � _a_<sup>_∗≤y_</sup> ) _._

Theorem. Supp ose the ordering


<!-- Start of picture text -->
L  (0) , A  (0) , L  () , . . . , L ( K ) , A  ( K ) , Y = L  ( K +)<br>is temp oral in the sense that L  ( j ) is only af-<br>�<br>fected by A ( j − ) for j = , . . . , K + . Con-<br>sider the G -computations formulas f � a ∗ ( y, � lK )<br>and f � a ∗ ( y ) corresp onding with this ordering.<br>If<br>�<br>:<br>A  ( j )  ⊥ ( Y � a , L � a � a ∈A ) | L �  ( j ) , A  ( j − ) ,<br>then the  G -computation formula  f � a ∗ ( y, � lK ) equals<br>P =<br>( Y � a ∗ = y, � a ∗ � lK ) .<br>L � K,<br>If<br><!-- End of picture text -->


<!-- Start of picture text -->
�<br>:<br>A  ( j )  ⊥ ( Y � a � a ∈A ) | L �  ( j ) , A  ( j − ) ,<br>then the G -computation formula f � a ∗ ( y equals<br>P<br>( Y � a ∗ = y ) .<br>Pro of. For simplicity: give the pro of for<br>L .<br>0 , A 0 , L , A , Y<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>G-COMPUTATION IN SIMPLE EXAMPLE.<br><!-- End of picture text -->


<!-- Start of picture text -->
Supp ose that the data on a subject is ( A, Y, W , W ),<br>where A is treatment, Y is outcome, W , W<br>are covariates. Assume the following temp o-<br>ral ordering at which the variables are gener-<br>ated:<br>W = ( W , W ) , A, Y.<br>In other words, one �rst generates covariates,<br>then the treatment is drawn p ossibly based on<br>W and subsequently one measures the out-<br>come Y .<br>Determine the  G -computation formula for: P ( Ya ≤<br>and P<br>y ) ( Ya ≤ y | W ).<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>JAMIE'S HYPOTHETICAL EXAMPLE<br><!-- End of picture text -->


<!-- Start of picture text -->
Let A 0 b e a randomly assigned treatment (yes<br>or no) assigned at t 0 , L is indicator of having<br>develop ed a risk factor such as Anemia at time<br>t , A is treatment (AZT) indicator at time t<br>(which can b e based on values of A 0 , L ) and<br>Y is an outcome at t such as the indicator<br>of b eing alive at t . In this example, we can<br>think of  A 0 = as a treatment which prevents<br>the development of Anemia ( L = ).<br>Question : Estimate causal e�ect of A 0 . In<br>other words, estimate  P ( YA = = ) −P ( YA =0 =<br>0 0<br>), where YA =0 ( YA =0 = ) is the counter-<br>0 0<br>factual outcome we would have observed on<br>everyb o dy if everyb o dy gets assigned A 0 = 0.<br>Answer: P ( Y =  | A 0 = ) − P ( Y =  | A 0 =<br>0) = / − 0 / = − / . So marginally<br>+<br><!-- End of picture text -->

treating hurts.

Question : Would it have b een wrong to adjust for _L_ in Question ? In other words, would _P_ ( _Y_ = _| A_ 0 = _, L_ = ) _−P_ ( _Y_ = _| A_ 0 = 0 _, L_ = have a causal interpretation. Answer: If a subject develop es Anemia ( _L_ = ) in spite of treatment _A_ 0 = , then that says something extra ab out the subject relative to a subject who develop ed Anemia ( _L_ = ) in the control treatment arm _A_ = 0. So an 0 asso ciation b etween _A_ 0 and _Y_ in the group _L_ = can b e solely due to the fact that _A_ 0 = prevents _L_ = . Question : Supp ose that we would like to know which of the two treatment regimes _A_ 0 = 0 _, A_ = and _A_ 0 = _, A_ = are b est. Then


<!-- Start of picture text -->
we want to estimate P ( Y = ) −P ( Y 0 = ).<br>How?<br>NAIVE I: P ( Y = | A 0 = 0 , A = )  − P ( Y =<br> | A 0 = , A = ). Wrong since L is a con-<br>founder of A and A a�ects L .<br>0<br>NAIVE I I: Adjust for L : P ( Y = | A 0 =<br>= = = = =<br>0 , A , L )  − P ( Y | A 0 , A<br>, L = ). In the example, this di�erence<br>equals / indicating treating at t 0 hurts in<br>the L = strata.<br>Wrong, cannot adjust for covariate a�ected<br>by treatment. Having L = in A 0 =<br>group is a very di�erent statement from hav-<br>ing L = in A 0 = 0 group.<br>G-COMPUTATION FORMULA:<br>Pa 0 a ( Y = , L = l ) = P ( L = l ) P ( Y =  | A 0 =  a<br><!-- End of picture text -->

Thus _P_ ( _Ya_ 0<sup>_a_</sup> = ) is given by:


<!-- Start of picture text -->
= = = =<br>, L ) +  Pa 0 a ( Y , L 0) .<br>rmula gives:<br><!-- End of picture text -->


<!-- Start of picture text -->
P ( Y = ) = /  ∗ / + /  ∗ / = / .<br>And<br>P ( Y 0 = ) =  ∗ 0 / + 0 = / .<br>Note that P ( Y 00 = ) and P ( Y 0 = ) are not<br>identi�ed from data example.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>ALTERNATIVE REPRESENTATION OF<br>G-COMP FORMULA<br>Recall the G -comp formula:<br>K<br>f � a ∗ ( y ) = . . . f ( y | � lK, � a ∗ K ) � f ( lj | � lj− , � a ∗ j− ) dµ  ( lj<br>� �<br>j =<br>This can b e rewritten as:<br>�<br>I A = � a ∗<br>( Y = y, )<br>= E .<br>f � a ∗ ( y ) �<br>=  a ∗ =<br>� Kj =0 P ( A  ( j ) ( j )  | Aj− � aj− , L � j− )<br><!-- End of picture text -->


<!-- Start of picture text -->
yes<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br><!-- End of picture text -->


<!-- Start of picture text -->
PART I I I: MARGINAL STRUCTURAL<br>MODELS.<br>IN POINT TREATMENT STUDIES<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>REGRESSION MODELS.<br>Consider the regression mo del:<br>Y =  mα ( A, V ) +  ϵ, E ( ϵ | A, V ) = 0,<br>where  mα ( A, V ) = E ( Y | A, V ) is a given parametriza-<br>tion of the regression surface. The observed<br>data is n observations on ( Y, A, W ), where V<br>is a subset of the observed covariates W , and<br>the goal is to estimate α ∈ IR k . Here A is<br>a treatment variable, W are covariates and<br>Y is an outcome variable of interest. Let<br>ϵ ( α ) ≡ Y − mα ( A, V ).<br>EXAMPLE: If Y is Bernoulli one could as-<br>sume:<br>P ( Y =  | A, V ) = α 0 +  α A +  α V<br>P ( Y =  | A, V ) = exp( α 0 +  α A +  α V )<br>P ( Y =  | A, V ) =<br>+ exp( α 0 +  α A +  α V )<br><!-- End of picture text -->

+


<!-- Start of picture text -->
In these three mo dels the parameter α repre-<br>sents the (adjusted) Risk Di�erence, Relative<br>Risk and the Odds Ratio, resp ectively.<br><!-- End of picture text -->


<!-- Start of picture text -->
Each vector function ( A, V ) → h ( A, V ) ∈ IR k<br>implies an unbiased estimating equation for α<br>given by:<br><!-- End of picture text -->

_n_ 0 = � _h_ ( _Ai, Vi_ ) _ϵi_ ( _α_ ) _. i_ = (Note that the least squares estimator would corresp ond with _h_ ( _A, V_ ) = _d/dαmα_ ( _A, V_ ).) Under weak regularity conditions we have that the solution _αn_ is ro ot- _n_ consistent and asymptotically linear: _n √n_ ( _αn−α_ ) _≈_ � _C_<sup>_−_</sup> _h_ ( _Ai, Vi_ ) _ϵi_ ( _α_ ) + _oP_ () _, n √ i_ =


<!-- Start of picture text -->
where IC ( X | α ) is the so called in�uence<br>curve given by:<br>IC ( X | α ) ≡ C − h ( A, V ) ϵ ( α ) .<br>Global summary of Pro of: Let  X = ( Y, A, W ).<br>De�ne Sα ( X ) = h ( A, V ) ϵ ( α ), let α 0 b e the<br>true regression parameter, P 0 b e the true data<br>generating distribution and let Pn b e the em-<br>pirical distribution of the data. Assume that<br>we have shown consistency of αn by other<br>means. We have:<br>EP 0 {Sαn − Sα 0 } = −EPn−P 0 Sαn ( X ) .<br><!-- End of picture text -->


<!-- Start of picture text -->
Empirical pro cess theory shows that:<br><!-- End of picture text -->


<!-- Start of picture text -->
Applying C − to b oth sides gives the wished<br>results.<br>Thus (by central limit theorem) √ n ( αn − α )<br><!-- End of picture text -->

is asymptotically normally distrubuted. The normal limit distribution has exp ectation zero and covariance matrix given by: � = _E_ ( _IC_ ( _X | α_ ) _IC_ ( _X | α_ )<sup>_⊤_</sup> ) = _C_<sup>_−_</sup> _E{h_ ( _A, V_ ) _h_ ( _A, V_ )<sup>_⊤_</sup> _ϵ_ ( _α_ ) _}C− ._ Given an estimator _αn_ of _α_ we can estimate � with the empirical covariance matrix of _IC_ ( _Xi | αn_ ), _i_ = _, . . . , n_ . This can b e used to construct an asymptotic 0.  con�dence interval for each comp onent _αj_ of _α_ . The optimal covariance matrix (smallest variance on the diagonal) is obtained by setting _d_ ( _A, V_ ) _dα_<sup>_mα_</sup> _h_ = _hopt_ ( _A, V_ ) = _. E_ ( _ϵ_ ( _α_ ) _| A, V_ ) The solution of 0 =<sup>�</sup><sup>_n_</sup> _i_ =<sup>_hopt_</sup> ( _Ai, Vi_ ) _ϵi_ ( _α_ ) equals the following weighted least squares estima-

tor:


<!-- Start of picture text -->
This estimator is not available in practice since<br>the weights are unknown. However, it imme-<br>diately suggests an iterative weighted least<br>squares estimator: HOW, Describ e it in de-<br>tail.<br>This iterative weighted least squares estima-<br>tor (IWLSE) requires guessing a mo del for<br>the regression E ( ϵ ( α ) | A, V ). If this guessed<br>mo del is correct, then the resulting IWLSE is<br>asymptotically e�cient. If the guessed mo del<br>is wrong, then the resulting IWLSE is still con-<br>sistent and asymptotically normal. Therefore<br>we call this IWLSE estimator a lo cally e�cient<br>estimator of α at the guessed mo del.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>A CAUSAL REGRESSION MODEL<br>FOR POINT TREATMENT<br>Let A b e a treatment variable with outcome<br>space A , W b e a vector of baseline covariates<br>not a�ected by A and Y is an outcome vari-<br>able. De�ne the vector of treatment sp eci�c<br>counterfactuals ( Ya : a ∈A ). Assume that A<br>is randomized w.r.t. W :<br>P ( A =  a | ( Ya :  a ∈A ) , W ) = P ( A = a | W ) .<br>We will denote the latter prop ensity score with<br>g ( a | W ).<br>We assume the following causal regression mo del:<br>for each a ∈A<br>E ( Ya | V ) = mβ ( a, V ) +  ϵa,<br>where E ( ϵa | V ) = 0. Such a mo del is called<br>a Marginal Structural Mo del. Note that β is<br>a causally interpretable parameter.<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
EXAMPLE: If Y is Bernoulli one could as-<br>sume:<br>P ( Ya =  | V ) = β 0 +  β a +  β V<br>P ( Ya =  | V ) = exp( β 0 +  β a +  β V )<br>P ( Ya =  | V ) =<br>+ exp( β 0 +  β a +  β V )<br>In these three mo dels the parameter β rep-<br>resents the (adjusted) Causal Risk Di�erence,<br>Causal Relative Risk and the Causal Odds Ra-<br>tio, resp ectively.<br><!-- End of picture text -->

When do es _α_ equal _β_ . In other words, when do we have _E_ ( _Y | A_ = _a, V_ ) = _E_ ( _Ya | V_ )? Answer: if _A_ is randomized w.r.t. _V_ (i.e. _A_ is completely selected at random within stata of _V_ ). Formally, _g_ ( _a |_ ( _Ya_ : _a ∈A_ ) _, W_ ) == _g_ ( _a | V_ ) _._ In that case, we have that _α_ represents the causal e�ect of _A_ on _Y_ within strata of _V_ . This requires adjusting for all p otential confounders in the regression mo del. In that case we have a lo cally e�cient estimator for _α_ , as given ab ove, and thus of _β_ (since _α_ = _β_ ).

+ + ESTIMATING EQUATIONS FOR _β_ . Each vector function ( _A, V_ ) _→ h_ ( _A, V_ ) _∈_ IR<sup>_k_</sup> implies an unbiased estimating equation for _β_ given by: _n h_ ( _Ai, Vi_ ) 0 = � ( _β_ ) _. i_ = _g_ ( _Ai | Wi_ )<sup>_ϵAi_</sup> If ( _Condition_ ) for almost every _W_ and each _a h_ ( _a, V_ ) _/_ () then one can indeed show ) _E_ ( _β_ ) = 0 _._ � _gh_ (( _AA, V | W_ )<sup>_ϵA_</sup> � Give the pro of. Discuss this identi�ability condition. Firstly, we note that this condition is needed to make the causal parameter identi�able from the data. Nonparametric estimation of the G-computation +

formula _E_ ( _Ya | V_ ) = _EE_ ( _Y | A_ = _a, W_ ) _| V_ ) would require that the conditioning event ( _A_ = _a, W_ ) always has p ositive probability. Therefore this condition should not come as a surprise. Before doing an analysis it is advisable to plot empirically ( _Ai, Wi_ ), _i_ = _, . . . , n_ , in order to detect subp opulations _W_ = _w_ for = 0 for some _a_ . which _g_ ( _a | w_ ) The fact that this condition dep ends on _h_ and thus on the choice of the estimating equation is helpful. For example, it might b e p ossible to set _h_ ( _A, V_ ) = _h_ ( _A, V_ ) _I_ ( _A ∈A_<sup>_, V∈V_</sup> ) for some subset _A_ of all treatment outcomes and some subset _V_ of covariate values for which _g_ ( _a | W_ ) _>_ 0 for all _a ∈A_ , _V ∈V_ . Consider now the scenario in which subjects with a certain covariate value _W_ = _w_ always receive treatment . Then it would make

most sense to delete these subjects from the sample. One will now do causal inference for the p opulation of subjects with _W_ = _w_ , which supp osedly is the p opulation of interest since do ctors already knew the b est treatment for subjects with _W_ = _w_ . However, in case one is truly interested in doing causal inference for the total p opulation one could mo del and estimate _E_ ( _Y | A, W_ ) (which thus involves extrap olating this surface to the region of _A, W_ 's for which no data is available) and use the _G_ -computation formula _E_ ( _Ya | V_ ) = _EE_ ( _Y | A_ = _a, W_ ) _| V_ ). However, keep in mind that the consistency of the estimate relies on having guessed what the e�ect of the other treatments would have b een for subjects with _W_ = _w_ . Back to the estimating equation: Since _g_ ( _a | W_ ) is an unknown nuisance parameter in


<!-- Start of picture text -->
this estimating equation this insights results<br>in the following prop osed estimators: for each<br>and an estimato<br>h ( A, V ) r gn ( · | W ) of g ( · | W )<br>we have the following estimating equation:<br>n h ( Ai, Vi )<br>0 = � ( β ) .<br>i = gn ( Ai | Wi ) ϵAi<br>We refer to these typ e of estimators of β<br>as the Inverse of Probability of Treatment<br>Weighted (IPTW) estimator. We prop ose (Robins)<br>to cho ose<br>g ( A | V ) d ( A, V )<br>dβ mβ<br>h ( A, V ) =  h ∗ ( A, V ) ≡ .<br>E ( ϵA ( β ) | A, V )<br>The advantages of this choice of estimating<br>equation is:<br>) If A is randomized w.r.t. V , then this es-<br>timating equation corresp onds with the es-<br>timating equation 0 = � n i = hopt ( Ai, Vi ) ϵi ( β )<br>which is in this situtation the optimal esti-<br>mating equation.<br>) In general, g ( A | V ) /g ( A | W ) is much more<br><!-- End of picture text -->


<!-- Start of picture text -->
stable than /g ( A | W ).<br>To summarize: multiplyi ng with g ( A | V ) sta-<br>bilizes the estimating equation in general and<br>it makes the estimating equation even optimal<br>when all confounders are contained in V .<br><!-- End of picture text -->


<!-- Start of picture text -->
h ∗ ( Ai,Vi )<br>The solution of 0 = � n i = ( β ) equals<br>g ( Ai|Wi ) ϵAi<br>the following weighted least squares estima-<br>tor:<br><!-- End of picture text -->


<!-- Start of picture text -->
n<br>= min −<br>βn � wi � Yi − mβ ( Ai, Vi ) �  ,<br>i =<br>where<br>g ( Ai | Vi )<br>= .<br>wi<br>g ( Ai | Wi )E ( ϵ ( α ) | Ai, Vi )<br>This estimator is not available in practice since<br>g ( A | V ) , g ( A | W ) and E ( ϵ ( β ) | Ai, Vi ) are<br>unknown. However, it immediately suggests<br>an iterative weighted least squares estimator:<br>HOW, Describ e it in detail?<br>This iterative weighted least squares estima-<br>tor of β requires a choice of mo del for g ( A |<br>W ), g ( A | V ) and for the regression of  ϵ ( β ) on<br>A, V . The mo del for g ( A | W ) implies a mo del<br>for g ( A | V ): just assume that the regression<br>parameters in front of the covariates b eyond<br><!-- End of picture text -->

_V_ are equal to zero. The consistency of the estimator _βn_ only relies on consistent estimation of (i.e. the correct mo del for) _g_ ( _A | W_ ) and on the correctness of the marginal structural mo del _E_ ( _Ya | V_ ) = _mβ_ ( _a, V_ ). Choices of mo dels for the prop ensity score: Bernoulli: If _A_ is a b ernoulli random variable, one can select a logistic regression mo del for _g_ ( _A | W_ ). Discrete: If _A_ is discrete, then one can use a multinomial regression: exp( _γa_ 0 + _γ_<sup>_W_</sup> ) _P_ = _a_ = ( _A_ 0 0<sup>_| W_</sup> ) +<sup>�</sup> _a_ 0 =0 exp( _γa_ 0 + _γ_<sup>_W_</sup> ) _P_ ( _A_ 0 = 0 _| W_ ) = +<sup>�</sup> _a_ 0 =0 exp( _γa_ 0 + _γ_<sup>_W_</sup> )<sup>_._</sup> Or Poisson regression: )<sup>_a_</sup> _P_ =<sup>_λ_(</sup><sup>_W_</sup> ( _A_ = _a | W_ ) exp( _−λ_ ( _W_ )) _, a_ ! where we assume some regression mo del for

_λ_ ( _W_ ) = _E_ ( _A | W_ ). Continuous: If _A_ is a continuous variable, then ) assume that _E_ ( _A | W_ ) = _mγ_ ( _A, W_ ) for some regression mo del _mγ_ and that the error distribution follows a known family (e.g. normal error disribution) with p ossibly a few unknown parameters. The regression estimation is then standard and the residuals can then b e used to �t the parametric error distribution. ) One could also use a semiparametric mo del such as the Cox-prop ortional hazards mo del: _λ_ ( _a | W_ ) = _λ_ 0 ( _a_ ) exp( _γW_ ) _._ Or any other semiparametric mo del such as the accelerated failure time mo del, the very �exible HAAR hazard mo dels of Stone and Ko op erb erg among many others.

Imp ortant fact: If one estimates _g_ ( _A | W_ ) more nonparametrically, then the asymptotic e�ciency of the estimator _βn_ increases. Therefore one should cho ose the dimension of the mo del for _g_ ( _a | W_ ) as large as sample size allows. Compare this IPTW-estimator _βn_ with an estimator based on the _G_ -computation for-


<!-- Start of picture text -->
mula.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>PART IV:<br>MARGINAL STRUCTURAL MODELSnl<br>FOR TIME-DEPENDENT<br>TREATMENT<br>Consider a longitudinal study with data col-<br>lected in the following temp oral ordering:<br>L 0 , A 0 , L , A , . . . , L K , A K , Y.<br>Let V b e a subset of the baseline covariates<br>�<br>L 0 . Let Ak = ( A 0 , . . . , A k ) b e the treatment<br>�<br>or exp osure history up till time k and A =<br>( A 0 , . . . , A k ) is the treatment history up till<br>end of follow up. Similar l y, we de�ne L � k and<br>L � . For convenience, we will now and then use<br>the notation LK + = Y .<br>Let Y b e the counterfactual value of Y that<br>� a<br>would have b een observed had the subject re-<br>ceived treatment history � a = ( a 0 , . . . , a K ). We<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
can also de�ne counterfactuals L which de-<br>� a<br>notes the pro cess L that would have b een ob-<br>served if the subject had received treatment<br>� a . The Y � a , � a ∈A , are the counterfactuals of<br>interest.<br>We will assume that treatment is sequentially<br>randomized: for each p ossible treatment regime<br>� a (consistent with the observed history)<br>A  ( k ) ⊥ Y � a | A � ( k − ) , L �  ( k ) .<br>In other words, for each k<br>�<br>:<br>g ( a ( k ) | ( Y � a � a ∈A ) , A  ( k − ) , L �  ( k ))<br>�<br>= g ( A  ( k )  | A  ( k − ) , L �  ( k )) .<br>We de�ne:<br><!-- End of picture text -->


<!-- Start of picture text -->
K<br>�<br>g (� a | X ) = � g ( a ( k )  | A  ( k − ) , L �  ( k )) ,<br>k =0<br>which one can think of as the conditional prob-<br>ability on receiving treatment regime � a , given<br><!-- End of picture text -->

the full data _X_ = ( _Y_ � _a_<sup>_, L_</sup> � _a_ : � _a ∈A_ ).

By the curse of dimensionality it will not b e p ossible (even when _g_ (� _a | X_ ) would b e known) to estimate treatment sp eci�c distributions of _Y_ � _a_ nonparametrically. Therefore we will need to assume a MSM such as: _E_ sum ( _Y_ � _a_<sup>_| V_</sup> ) = _mβ_ ( _V,_ (� _a_ )) _,_ is some (e.g. _β_ 0 + _β_ sum(� _a_ )) where _sum_ (� _a_ ) summary measure of � _a_ which is b elieved to have an e�ect on the conditional mean of _Y_ � _a_ , within strata of _V_ . For example, if _a_ ( _k_ ) is the dose of a particular treatment received at time _k_ , then sum(� _a_ ) = � _K_ is the cumulative dose through end _k_ =0<sup>_ak_</sup> of follow up for a subject receiving treatment regime � _a_ .


<!-- Start of picture text -->
The causal parameter β is of imp ortant p ol-<br>icy interest: e.g Y = when subject has de-<br>tectable HIV-serum in blo o d at end of follow<br>up and a ( j ) = if the subject received AZT<br>at time j .<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>IPTW-ESTIMATOR IN MSM MODEL<br>FOR ONE SINGLE OUTCOME<br>Consider the regression mo del:<br>� �<br>E sum<br>( Y | A, V ) = mβ ( V, ( A  )) .<br>The estimating equations for this regression<br>mo del are:<br>{h (sum( A � ) , V ) ϵ ( β ) :  h}.<br>The estimating equations for the corresp ond-<br>ing MSM mo del E ( Y � a | V ) ( V, sum(� a ))<br>= mβ<br>are given by:<br><!-- End of picture text -->


<!-- Start of picture text -->
( A � ) , V )<br>� ϵ ( β ) :  h .<br>� h (sum g ( A | X ) �<br>These estimating equations are unbiased if<br>h (sum� a, V ) /g (� a | X ) > 0 for all � a .<br><!-- End of picture text -->


<!-- Start of picture text -->
Remark: If a subject's history up till p oint t<br>is such that certain have zero<br>treatments a ( t  )<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
probability to b e assigned, then one should ar-<br>ti�cially censor the subject at t  . In this way<br>one can arti�ciall y arrange the identi�ability<br>assumption to b e true.<br>De�ne<br>�<br>g ( A | V )<br>SW ( K ) = �<br>g ( A | X )<br>� K =0 g ( A  ( j )  | A � ( j − ) , V )<br>j<br>= .<br>� K =0 g ( A  ( j )  | A � ( j − ) , L �  ( j ))<br>j<br>In order to have a stable estimating equations<br>which is optimal in case V contains all con-<br>founders, we prop ose as estimating equation:<br>n<br>�<br>0 = � SWi ( K ) hopt (sum( Ai ) , Vi ) ϵ � ( β ) ,<br>Ai<br>i =<br>where<br>�<br>� d/dβmβ (sum( A  ) , V )<br>= .<br>hopt (sum( A  ) , V ) �<br>E ( ϵ ( β ) | A, V )<br><!-- End of picture text -->

_E_ ( _ϵ_ ( _β_ ) _| A, V_ ) This estimating equation corresp onds with �t-

ting the regression mo del _E_ � sum � ( _Y | A, V_ ) ( _V,_ ( _A_ )) = _mβ_


<!-- Start of picture text -->
using weights  SWi ( K ) for subject  i , i = , . . . , n .<br>We refer to these weighted estimators as IPTWE,<br>abbreviating \Inverse Probability of Treatment<br>Weighted Estimator".<br><!-- End of picture text -->

Recall that adjusting for time-dep endent confounders (thus a variable which is a�ected by past treatment) in the regression mo del will yield a biased estimate of the treatment effect: see example page , Robins, Hernan, Brumback (  ).


<!-- Start of picture text -->
+ +<br>ESTIMATION OF SUBJECT<br>SPECIFIC WEIGHTS<br>Consider the case that A  ( k ) is a -0 variable.<br>�<br>Then we can estimate P ( Ak = | Ak− =<br>� ak− , L � k = � lk ) using a p o oled logistic regres-<br>sion mo del that treats each p erson-day as one<br>observation, with covariates extracted from<br>past treatment and covariate history. This<br>yields then an estimate of g ( A � | X ). Note<br>that this estimate is a pro duct over time of<br>)<br>−A  ( k<br>terms (  − Pk ) ) Pk A  ( k .<br>Similarl y, one can estimate g ( A � | V ) by using<br>a p o oled logistic regression mo del that treats<br>each p erson-day as one observation, with co-<br>variate V and covariates extracted from past<br>treatment: thus not adjusting for L �  ( k ).<br>Give example: formula (), () and ()<br>of Robins, Hernan, Brumback (  ).<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>CENSORING BY LOSS TO FOLLOW UP<br>Let Ck = if the subject was lost to follow-up<br>by day k and Ck = 0 otherwise. We assume<br>that once a subject is lost to follow up, the<br>subject do es not reenter the study.<br>No new ideas are required to account for cen-<br>soring, by viewing censoring as just another<br>time-varying treatment and restricting the es-<br>timator ab ove to the uncensored subjects.<br>The data on the uncensored subjects is now:<br>L 0 , ( C 0 = 0 , A 0 ) , . . . , LK, ( CK = 0 , AK ) , Y, CK + = 0 .<br>Let � a ′ = (( c 0 , a 0 ) , ( c , a ) , . . . , ( cK, aK ) , cK + )<br>represent a treatment history: at time j the<br>subject receives joint treatment a ′ j = ( cj, aj )<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
(we de�ne a ′ K + = cK + ). As ab ove, we de-<br>�ne the counterfactuals Y � a ′ . The only coun-<br>terfactuals of interest to us are Y for � a ′ with<br>� a ′<br>c 0 = . . . = cK + = 0. Therefore we only<br>p ose a MSM mo del for these counterfactu-<br>als. Let Y b e the counterfactual Y with<br>� a � a ′<br>real treatment comp onents aj and cj = 0,<br>j = 0 , . . . , K + . We assume the MSM mo del<br>for Y :<br>� a<br>E sum<br>( Y � a | V ) ( V, (� a )) .<br>= mβ<br><!-- End of picture text -->

+ + IPTCW-ESTIMATOR IN MSM MODEL FOR ONE SINGLE OUTCOME Let � b e the indicator of b eing uncensored: i.e. � = if and only if _CK_ + = 0. The estimating equations for the MSM mo del _E_ ( _Y_ � _a_<sup>_|_</sup> _V_ ) ( _V,_ sum(� _a_ )) are given by: = _mβ_ ( _A_ � ) _, V_ ) � _ϵ_ ( _β_ )� : _h ._ � _h_ (sum _g_ ( _A_<sup>_′_</sup> _| X_ ) � De�ne � _g_ ( _A_<sup>_′_</sup> _| V_ ) _SW_<sup>_′_</sup> ( _K_ + ) = � _g_ ( � _A_<sup>_′_</sup> =0 _| X_<sup>_K_</sup> +)<sup>_g_</sup> ( _A_<sup>_′_</sup> ( _j_ ) _| A_ �<sup>_′_</sup> ( _j −_ ) _, V_ ) _j_ = � =0<sup>_K_</sup> +<sup>_g_</sup> ( _A_<sup>_′_</sup> ( _j_ ) _| A_ �<sup>_′_</sup> ( _j −_ ) _, L_ � ( _j_ )) _. j_ Since _a_<sup>_′_</sup> ( _j_ ) = ( _c_ ( _j_ ) = 0 _, a_ ( _j_ )) we can write � _a_<sup>_′_</sup> _g_ ( _a_<sup>_′_</sup> ( _j_ ) _|_ ( _j −_ ) _, L_ � ( _j_ )) = = = _g_ ( _c_ ( _j_ ) 0 _|_ � _a_ ( _j −_ ) _,_ � _c_ ( _j −_ ) 0 _, L_ � ( _j_ )) = _×g_ ( _a_ ( _j_ ) _|_ � _a_ ( _j −_ ) _,_ � _c_ ( _j_ ) 0 _, L_ � ( _j_ )) +


<!-- Start of picture text -->
and<br><!-- End of picture text -->

_g_ ( _a_<sup>_′_</sup> ( _K_ + ) _|_ � _a_<sup>_′_</sup> ( _K_ ) _, L_ � ( _K_ + )) = = = _g_ ( _c_ ( _K_ + ) 0 _|_ � _a_ ( _K_ ) _,_ � _c_ ( _K_ ) 0 _, L_ � ( _K_ + )) _._ Therefore _SW_<sup>_′_</sup> ( _K_ + ) = _SW_<sup>_c_</sup> ( _K_ + ) _SW_ ( _K_ ) _,_ where � � _C_ = � _K_ =0<sup>_g_</sup> ( _A_ ( _j_ ) _| A_ ( _j −_ ) _,_ ( _j_ ) 0 _, V_ ) _j SW_ ( _K_ ) = � � + _C_ = � _K_ =0<sup>_g_</sup> ( _A_ ( _j_ ) _| A_ ( _j −_ ) _,_ ( _j_ ) 0 _, L_ � ( _j_ )) _j_ and _SW_<sup>_c_</sup> ( _K_ + ) is given by: � � + = _C_ = � _K_ =0<sup>_g_</sup> ( _C_ ( _j_ ) 0 _| A_ ( _j −_ ) _,_ ( _j −_ ) 0 _, V_ ) _j ._ � � + = _C_ = � _K_ =0<sup>_g_</sup> ( _C_ ( _j_ ) 0 _| A_ ( _j −_ ) _,_ ( _j −_ ) 0 _, L_ � ( _j_ )) _j_


<!-- Start of picture text -->
In order to have stable estimating equations<br>which is optimal in case V contains all con-<br>founders and nob o dy is censored, we prop ose<br>as estimating equation:<br>n<br>�<br>0 = � SWi ′ ( K + ) hopt (sum( Ai ) , Vi ) ϵ � ( β ) ,<br>Ai<br>i =<br>where<br>�<br>� d/dβmβ (sum( A  ) , V )<br>hopt (sum( A  ) , V ) = � .<br>E ( ϵ ( β ) | A, V )<br>This estimating equation corresp onds with �t-<br>ting the regression mo del  E ( Y | A, V � ) ( V, sum( A �<br>= mβ<br>with using weights SWi ′ ( K + ) for subject i ,<br>i = , . . . , n . We refer to these weighted es-<br>timators as \Inverse of Probability of Treat-<br>ment and Censoring Weighted Estimator".<br>Explain that these estimators are the same<br>as solving the estimating equation we used<br>without censoring with � /P (� =  | X, A  ).<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>ESTIMATION OF SUBJECT<br>SPECIFIC WEIGHTS<br>�<br>Again, we can estimate P ( Ck = 0 | Ck− =<br>� � �<br>0 , A  ( k− ) , L � k ) and  P ( Ck = 0  | Ck− = 0 , A  ( k−<br>) , V ) using a p o oled logistic regression mo del<br>that treats each p erson-day as one observa-<br>tion. Thus by �tting four logistic regression<br>mo dels to p o oled samples one obtains an es-<br>timate of SW ′ ( K + ).<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
0<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>PART V:<br><!-- End of picture text -->


<!-- Start of picture text -->
MARGINAL STRUCTURAL MODELS<br>FOR TIME-DEPENDENT<br>TREATMENT<br>IN SURVIVAL ANALYSIS<br><!-- End of picture text -->


<!-- Start of picture text -->
+<br><!-- End of picture text -->


+ + DATA Let _A_ ( _j_ ) b e treatment the subject received at time _j_ . Let _L_ ( _j_ ) b e time-dep endent covariates collected on the subject at time _j_ , where _L_ ( _j_ ) o ccurs right b efore the treatment assignment _A_ ( _j_ ). Let the outcome of interest b e the survival time _T_ of the subject. A particular application one can keep in mind is a longitudinal study in which a HIV-infected subject is followed up till death _T_ , _A_ ( _t_ ) is a dichotomous variable indicating whether a patient is on prophylaxis treatment at day _t_ , _L_ ( _t_ ) is a vector of measured risk factors for survival such as CD count, white blo dd cell count and numb er of Pneumonia (PCP) b outs. The observed data on a subject is thus: ( _T, A_ � ( _T_ ) _, L_ � ( _T_ )) _._


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
We are concerned with estimation of causal<br>e�ects of A � on survival T . A useful alternative<br>way of representing this data structure is to<br>de�ne Y ( j ) as the indicator of failure at time<br>j and de�ne the data as:<br>( A �( T ) , Y � ( T ) , L �  ( T )) .<br>Let V b e a subset of the baseline covariates<br>Let T b e the counterfactual value of<br>L  (0). � a<br>T that would have b een observed had the sub-<br>ject received treatment history � a = ( a 0 , . . . , a K ).<br>We have T = T . We can also de�ne<br>� a � a  ( T ) , 0<br>counterfactuals L � a which denotes the pro cess<br>L that would have b een observed if the sub-<br>ject had received treatment � a . Again, L � a ( t  ) =<br>L � a ( t ) , 0 ( t  ). The Y � a , � a ∈A , are the counterfac-<br>tuals of interest.<br>We will assume that treatment is sequentially<br><!-- End of picture text -->


<!-- Start of picture text -->
randomized: for each p ossible treatment regime<br>� a (consistent with the observed history)<br>A  ( k ) ⊥ Y � a | A � ( k − ) , L �  ( k ) .<br>In other words, for each k<br>�<br>:<br>g ( a ( k ) | ( Y � a � a ∈A ) , A  ( k − ) , L �  ( k ))<br>�<br>= g ( A  ( k )  | A  ( k − ) , L �  ( k )) .<br><!-- End of picture text -->


<!-- Start of picture text -->
K<br>�<br>g (� a | X ) = � g ( a ( k )  | A  ( k − ) , L �  ( k )) ,<br>k =0<br>which one can think of as the conditional prob-<br>ability on receiving treatment regime � a , given<br>the full data X = ( Y � a , L � a : � a ∈A ).<br><!-- End of picture text -->

We de�ne:

+ + MARGINAL STRUCTURAL COX MODEL In the absence of time-dep endent confounding one could use a time-dep endent Cox-prop ortional hazards mo del: _λT_ ( _t | A_ � ( _t_ ) _, V_ ) = _λ_ 0 ( _t_ ) exp( _γ_<sup>_A_(</sup><sup>_t_)</sup> + _γ_<sup>_⊤V_</sup> ) _._ Here _λT_ ( _t | A_ � ( _t_ ) _, V_ ) is the hazard of death at time _t_ from start of follow up conditional on � treatment history _A_ ( _t_ ) and pretreatment covariates _V_ , and _λ_ 0 ( _t_ ) is an unsp eci�ed baseline hazard function. For example, _V_ could include the log of baseline CD-count, log of baseline white blo o d count. In the absence of time-dep endent confounding one can then estimate _γ_ with the solution of the partial likeliho o d score equation for _γ_ . Since the partial likeli ho o d is a pro d- uct over time from _t_ = 0 till _∞_ the score +


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
equation is an sum over time. So let's repre-<br>sent the score equation (for one subject) as<br>� t U ( A �( t  ) , Y � ( t  ) , V | γ ).<br>The corresp onding marginal structural Cox-<br>prop ortional hazards mo del is given by:<br>λT ( t | V ) = λ 0 ( t  ) exp( β a ( t  ) +  β V ) ,<br>� a<br><!-- End of picture text -->


<!-- Start of picture text -->
where λT ( t | V ) is the hazard of death at t<br>� a<br>among subjects with pretreatment covariates<br>V had, contrary to the fact, all subjects fol-<br>lowed treatment regime � a .<br>De�ne<br>�<br>g ( A ( t  ) | V )<br>SW ( t  ) = �<br>g ( � At (=0 t  ) g | X ( A ) ( j )  | A � ( j − ) , V )<br>j<br>= .<br>� K =0 g ( A  ( j )  | A � ( j − ) , L �  ( j ))<br>j<br>In order to have a stable estimating equation<br>which is optimal in case we do not have time-<br><!-- End of picture text -->

dep endent confounding, we prop ose as estimating equation: _n_ � 0 = � � _SWi_ ( _t_ ) _U_ ( _Ai_ ( _t_ ) _, Y_ � _i_ ( _t_ ) _, Vi | γ_ ) _. i_ = _t_ This corresp onds with �tting the time-dep endent Cox mo del with each subjects data line ( _Ai_ ( _t_ ) _, Yi_ ( _t_ ) _, L_ weighted with _Wi_ ( _t_ ) = _SWi_ ( _t_ ) with _t_ running from 0 till _Ti_ .

+ + MARGINAL STRUCTURAL lOGISTIC REGRESSION MODEL If time is discrete, i.e. many subjects die at the same time, then the Cox-mo del is not appropriate, but one should use a discrete survival time mo del. In this case one could mo del the discrete hazard with a logistic regression mo del: � = = logit ( _P_ ( _Y_ ( _t_ ) _| Y_ ( _t −_ ) 0 _, A_ ( _t −_ ) _, V_ ) = _β_ 0 ( _t_ ) + _β_<sup>_A_(</sup><sup>_t −_</sup> ) + _β_<sup>_V,_</sup> where _β_ 0 ( _t_ ) is an unsp eci�ed baseline function. If the time unit b ecomes �ner and �ner, then this mo del approximates the Cox prop ortional hazards mo del with exp( _β_ 0 ( _t_ )) representing the cumulative baseline hazard.


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
This mo del can b e �t with p o oled logistic re-<br>gression treating each p erson day as an ob-<br>servation: this also provides the correct con-<br>�dence intervals.<br>The corresp onding marginal structural mo del<br>is given by:<br>= =<br>logit ( P ( Y � a ( t  )  | Y � a ( t − ) 0 , V )<br>= β 0 ( t  ) +  β a ( t − ) +  β V.<br>The causal parameters  β can b e �t with weighted<br>p o oled logistic regression treating each p erson<br>day t as an observation with weights SW ( t  ).<br>To obtain conservative con�dence intervals<br>one needs to view the data as rep eated mea-<br>sures and therefore one should �t the mo del<br>with a generalized estimating equations pro-<br>gram (e.g. option 'rep eated' in SAS Pro c<br>Genmo d).<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>CENSORING BY LOSS TO FOLLOW UP<br>Let Ck = if the subject was lost to follow-up<br>by day k and Ck = 0 otherwise. We assume<br>that once a subject is lost to follow up, the<br>subject do es not reenter the study.<br>No new ideas are required to account for cen-<br>soring, by viewing censoring as just another<br>time-varying treatment and restricting the es-<br>timator ab ove to the uncensored subjects. At<br>time j the subject receives joint treatment<br>a ′ j = ( cj, aj ).<br>As ab ove, we de�ne the counterfactuals Y .<br>� a ′<br>The only counterfactuals of interest to us are<br>Y for � a ′ with c =  . . . = 0. Therefore<br>� a ′ 0 = cK +<br>we only p ose the logistic regression or Cox-<br>prop ortional hazards MSM mo del for these<br>counterfactuals.<br>+<br><!-- End of picture text -->

Let � b e the indicator of b eing uncensored: i.e. � = if and only if _CK_ + = 0. De�ne _A_ �<sup>_′_</sup> _g_ ( ( _t_ ) _| V_ ) _SW_<sup>_′_</sup> ( _t_ ) = � _A_<sup>_′_</sup> _g_ ( � _t_ =0( _t_ )<sup>_g_</sup> _|_ ( _XA_<sup>_′_</sup> )( _j_ ) _| A_ �<sup>_′_</sup> ( _j −_ ) _, V_ ) _j_ = � _t_ =0<sup>_g_</sup> ( _A_<sup>_′_</sup> ( _j_ ) _| A_ �<sup>_′_</sup> ( _j −_ ) _, L_ � ( _j_ )) _. j_ Since _a_<sup>_′_</sup> ( _j_ ) = ( _c_ ( _j_ ) = 0 _, a_ ( _j_ )) we can write � _a_<sup>_′_</sup> _g_ ( _a_<sup>_′_</sup> ( _j_ ) _|_ ( _j −_ ) _, L_ � ( _j_ )) = = = _g_ ( _c_ ( _j_ ) 0 _|_ � _a_ ( _j −_ ) _,_ � _c_ ( _j −_ ) 0 _, L_ � ( _j_ )) = _×g_ ( _a_ ( _j_ ) _|_ � _a_ ( _j −_ ) _,_ � _c_ ( _j_ ) 0 _, L_ � ( _j_ )) _._

Therefore _SW_<sup>_′_</sup> ( _t_ ) = _SW_<sup>_c_</sup> ( _t_ ) _SW_ ( _t_ ) _,_ where � � _C_ = � _t_ =0<sup>_g_</sup> ( _A_ ( _j_ ) _| A_ ( _j −_ ) _,_ ( _j_ ) 0 _, V_ ) _j SW_ ( _t_ ) = � � _C_ = � _t_ =0<sup>_g_</sup> ( _A_ ( _j_ ) _| A_ ( _j −_ ) _,_ ( _j_ ) 0 _, L_ � ( _j_ )) _j_

and _SW_<sup>_c_</sup> ( _t_ ) is given by: � � = _C_ = � _t_ =0<sup>_g_</sup> ( _C_ ( _j_ ) 0 _| A_ ( _j −_ ) _,_ ( _j −_ ) 0 _, V_ ) _j_ � � _._ = _C_ = � _t_ =0<sup>_g_</sup> ( _C_ ( _j_ ) 0 _| A_ ( _j −_ ) _,_ ( _j −_ ) 0 _, L_ � ( _j_ )) _j_ One estimates _β_ with weighted p o oled logistic regression treating each p erson day t as an observation with weights � _SW_<sup>_′_</sup> ( _t_ ).


<!-- Start of picture text -->
+ +<br>INSTRUMENTAL VARIABLES IN<br>REGRESSION<br>Supp ose that Y = m ( X | β ) + ϵ , where Eϵ = 0<br>but E ( ϵ | X ) = 0. For example, X might<br>b e the actual treatment taken by the subject,<br>Y is the outcome of interest and X might<br>b e based on unobserved variables related to<br>the error. Then the standard (naive) esti-<br>mating equation h ( X ) ϵ ( β ) might result in a<br>biased estimator. Let Z b e a variable satis-<br>fying E ( ϵ ( β ) | Z ) = E ( ϵ ( β )); for example, Z<br>is indep endent of ϵ ( β ). In our example, one<br>could think of Z b eing a randomly assigned<br>treatment arm. Then one can use as esti-<br>mating equation<br>g ( Z ) ϵ ( β ) . ()<br>If the matrix E ( g ( Z ) dβ d ϵ ( β )) is invertible, then<br>under standard regularity conditions, the cor-<br>resp onding estimator is asymptotically linear<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
with in�uence curve<br><!-- End of picture text -->


<!-- Start of picture text -->
E ( g ( Z ) d/dβm ( X | β )) = Eg ( Z ) Ed/dβm  ( X |<br>β ). In other words, this estimating equation<br>can only b e informative if Z is related to X .<br>The random variable Z is often referred to<br>as an instrumental variable. Thus in regres-<br>sion problems where one exp ects dep endence<br>b etween the residual and X one can salvage<br>estimation by �nding a variable Z which is un-<br>related to the residual but related to X .<br><!-- End of picture text -->

_{Eg_ ( _Z_ ) _d/dβm_ ( _X | β_ ) _}_<sup>_−_</sup> _g_ ( _Z_ ) _ϵ_ ( _β_ ) _._ This invertibil i ty condition requires that


<!-- Start of picture text -->
+ +<br>CAUSAL INFERENCE WITH<br>NON-COMPLIANCE<br>IN POINT TREATMENT STUDIES<br>Let R b e the treatment assigned to the sub-<br>ject and we assume that R is completely ran-<br>domized. Let A b e the treatment the sub-<br>ject actually uses. Let Y b e the outcome<br>of interest and supp ose that we also observe<br>some covariates  W . Thus the observed data is<br>( Y, R, A, W ). By non-compliance A can b e dif-<br>ferent from  R and  A can b e confounded by un-<br>measured confounders. Let X = (( Ya :  a ) , W )<br>b e the treatment sp eci�c counterfactual out-<br>comes and the covariate vector.<br>Consider the marginal structural mo del<br>Ya = β 0 +  β a +  ϵ, where E ( ϵ ) = 0.<br>Note that ϵ = Y 0 − β 0 so that β 0 = EY 0 . This<br>marginal structural mo del is equivalent with<br>+<br><!-- End of picture text -->

_E_ ( _Ya − Y_ 0 ) = _β_<sup>_a_.</sup>

It also corresp onds with the following observed data regression mo del _Y_ = _YA_ = _β_ 0 + _β_<sup>_A_</sup> + _ϵ,_ where _Eϵ_ ( _β_ ) = 0 _._ Thus estimation of _β_<sup>_, β_</sup> corresp onds with linear regression of _Y_ on _A_ but with an error term which dep ends on _A_ since the actual selected treatment _A_ might have b een based on _Y_ . 0 This suggests to use the instrumental variable metho d to estimate ( _β_<sup>_, β_</sup> ) using _R_ as instrumental variable. Notice that indeed _R_ is indep endent of _ϵ_ and (strongly) related to _A_ . Thus our estimating equations are of the typ e: for any given _φ φ_ ( _R_ ) _{Y − β_ 0<sup>_−βA}._</sup>


<!-- Start of picture text -->
The unbiasedness of this estimating equation<br>follows from the fact that at the true β R<br>is indep endent of ϵ ( β ) = Y − β 0 − β A and<br>that Eϵ ( β ) = 0. Alternatively, we could use<br>as estimating equation:<br>{φ ( R )  − Eφ ( R ) }{Y − β A}.<br>If R has only two outcomes 0 , , then there<br>exists only one estimating equation (i.e. φ )<br>and therefore one can only identify β . In<br>general, the dimension of our causal mo del<br>parameter β needs to b e restricted by the ac-<br>tual numb er of estimating equations we can<br>come up with. If R has k p ossible outcomes,<br>then we can come up k − choices of φ . If<br>covariates are available, then we have k −<br>estimating equations for each strata identi-<br>�ed by e.g. V = v . By assuming that the<br>causal mo del do es not heavily dep end on the<br>strate V = v , e.g. E ( Ya − Y 0 | V ) = β a + β V ,<br><!-- End of picture text -->


<!-- Start of picture text -->
this approach makes it p ossible to mo del the<br>e�ect of a more �exible.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>CAUSAL EFFECT AMONG COMPLIERS<br>Assume the following mo del:<br><!-- End of picture text -->

_E_ ( _Ya − Y_ 0<sup>_| R, A_</sup> = _a_ ) = _β_ 0<sup>_a_</sup> + _β_<sup>_R._</sup> Note that the unknown parameter _β_ = ( _β_ 0<sup>_, β_</sup> ) de�nes, in particular, the causal e�ect of treatment _A_ among the compliers. Let _Y_ 0 ( _β_ ) = _Y − β_ 0<sup>_A −βR_</sup> which represents the outcome _Y_ blipp ed down to _Y_ 0 . The instrumental variable metho d suggests the following estimating equation for _β_ : ( _φ_ ( _R_ ) _− Eφ_ ( _R_ )) _Y_ 0 ( _β_ ) _._ () Since _E_ ( _Y_ 0 ( _β_ ) _| R, A_ = _a_ ) = _E_ ( _Y_ 0<sup>_|R, A_</sup> = _a_ ) it follows that

= _E{_ ( _φ_ ( _R_ ) _− Eφ_ ( _R_ )) _Y_ 0 ( _β_ ) _} E{_ ( _φ_ ( _R_ ) _− Eφ_ ( _R_ )) _Y_ 0<sup>_}_</sup> = = 0 since _E_ ( _φ_ ( _R_ ) _| Y_ 0 ) = _Eφ_ ( _R_ ). +


<!-- Start of picture text -->
+<br><!-- End of picture text -->


<!-- Start of picture text -->
(We used that YRA =  YA )<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>CAUSAL INFERENCE WITH<br>NON-COMPLIANCE<br>IN LONGITUDINAL STUDIES<br>Data: On each subject we collect the follow-<br>ing data over time<br>R, L 0 , A 0 , L , A , . . . , L K , A K , Y,<br>where ( Lj, Aj ) represents covariates and treat-<br>ment at time j , j = 0 , . . . , K , and R = A− is<br>the randomly assigned treatment arm. We<br>mo del the so called blip function conditional<br>on the past:<br>�<br>E ( YA � j, 0 −Y A � j− , 0 | Aj = � aj, L � j = � lj ) = βj (� aj, � lj | β ) ,<br>where the blip is parametrized by<br>function βj<br>a �nite dimensional parameter vector β which<br>is common to each βj , j = , . . . , K . In words,<br>this blip function is the exp ected value of the<br>di�erence of two counterfactuals only di�er-<br>ing by one blip in their treatment, given the<br>+<br><!-- End of picture text -->


At the true _β E_ ( _Y_ 0 ( _β_ ) _| R_ ) = _EY_ 0 . Using _R_ as an instrumental variable suggests the following estimating equations: for any given _φ {φ_ ( _R_ ) _− Eφ_ ( _R_ ) _}{Y_ 0 ( _β_ ) _}._ If _R_ has only two outcomes 0 _,_ , then there exists only one estimating equation (i.e. _φ_ ) and therefore one can only identify _β_ . In general, the dimension of our causal mo del parameter _β_ needs to b e restricted by the actual numb er of estimating equations we can come up with. If _R_ has _k_ p ossible outcomes,


<!-- Start of picture text -->
then we can come up k − choices of φ . If<br>covariates are available, then we have k −<br>estimating equations for each strata identi-<br>�ed by e.g. V = v . By assuming that the<br>causal mo del do es not heavily dep end on the<br>strate V = v , e.g. E ( Ya − Y 0 | V ) = β a + β V ,<br>this approach makes it p ossible to mo del the<br>e�ect of a more �exible.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>STRUCTURAL NESTED MEAN MODELS<br>IN LONGITUDINAL STUDIES<br>Data: On each subject we collect the follow-<br>ing data over time<br>L 0 , A 0 , L , A , . . . , L K , A K , Y,<br>where ( Lj, Aj ) represents covariates and treat-<br>ment, resp ectively, at time j , j = 0 , . . . , K ,<br>�<br>and Y is the outcome of interest. Let Aj =<br>( A 0 , . . . , A j ) and L � j = ( L 0 , . . . , L j ), j = 0 , . . . , K .<br>For each p ossible treatment regime � a = ( a 0 , . . . , a K )<br>we de�ne L � as the counterfactual out-<br>( Y � a , � a<br>come of ( Y, L �  ) if, p ossibly contrary to the<br>fact, the subject would have received treat-<br>ment regime � a . Thus ( Y, L �  ) = ( YA � , L � A �).<br>We assume the following mo del. Firstly, we<br>assume the sequential randomization assump-<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
tion which states that Aj ⊥{Y � a , L �� a : � a} , given<br>�<br>the observed past , where � a ranges<br>Aj− , L � j<br>�<br>over treatment regimes with � aj− = Aj− . In<br>addition, we mo del the so called blip function<br>conditional on the past:<br>�<br>E ( YA � j, 0 −Y A � j− , 0 | Aj = � aj, L � j = � lj ) = βj (� aj, � lj | β ) ,<br>where the blip is parametrized by<br>function βj<br>a �nite dimensional parameter vector β which<br>is common to each βj , j = , . . . , K . In words,<br>this blip function is the exp ected value of the<br>di�erence of two counterfactuals only di�er-<br>ing by one blip in their treatment, given the<br>observed past.<br>The idea ab ove of using an instrumental vari-<br>able to obtain an unbiased estimating equa-<br>tion can b e generalized to construct unbiased<br>estimating equations of the blip function in<br>structural nested mean mo dels. We view the<br><!-- End of picture text -->


<!-- Start of picture text -->
total data generating exp eriment as a sequen-<br>tial exp eriment over time, where at time j one<br>conditions on the observed past A � ( j − ) , L �  ( j ).<br>Exp eriment j corresp onds with drawing the<br>data after Aj− and ending with generating<br>Aj , where we know that Aj is assigned com-<br>pletely at random, given the past. For each j<br>one constructs a residual which has mean zero<br>conditonal on the past and is unrelated to Aj<br>which will play the role of the instrumental<br>variable.<br>Consider the blipp ed down version of Y<br><!-- End of picture text -->


De�ne the residual:

Notice that _Aj_ is related to the covariates � _Kl_ = _j_<sup>_βl_</sup> ( _A_ � _l, L_ � _l_ ) and using ) that _Yj−_ ( _β_ ) rep� resents the counterfactual _Y_ and ) the _Aj− ,_ 0 sequential randomization assumption we will b e able to show that _E_ ( _ϵj−_ ( _β_ ) _| A_ � _j− , Aj, L_ � _j_ ) = _E_ ( _ϵj−_ ( _β_ ) _| A_ � _j− , L_ � _j_ ) _._ () Thus _Aj_ is unrelated (in the exp ectation sense) to the residual, given the observed past. This proves that we can as instrumental use _Aj_ variable and thus use as estimating equation: for each function _g_ � = = ( _β_ ) _g_ ( ) 0 _, j , . . . , K. ϵj− Aj, L_ � _j_ To see that the estimating equation is unbiased just condition on _A_ � _j, L_ � _j_ and use that _E_ ( _Yj−_ ( _β_ ) _| A_ � _j, L_ � _j_ ) = _E_ ( _Yj−_ ( _β_ ) _| A_ � _j− , L_ � _j_ ). A natural way of combining these _K_ instrumental estimating equations corresp onding with


<!-- Start of picture text -->
exp eriment j = , . . . , K to one estimating<br>equation for β is to use as estimating equation<br>K<br>�<br>� ϵj− ( β ) gj ( Aj, L � j ) = 0 .<br>j =<br>We can extend this class of estimating equa-<br>tions as follows:<br>K<br>� Yj− ( β )  − �( A � j− , L � j )<br>� �<br>j =<br>� � �<br>g ( Aj, L � j )  − E ( g ( Aj, L � j ) | Aj− , L � j ) ,<br>� �<br>where φ and g are user supplied.<br>We will now show that indeed<br>� �<br>E ( Yj− ( β ) | Aj− , L � j, Aj ) = E ( Yj− ( β ) | Aj− , L � j ) .<br><!-- End of picture text -->

We have


<!-- Start of picture text -->
+ +<br>ESTIMATING COUNTERFACTUAL<br>EXPECTATIONS<br>Ab ove we provided an estimating equation for<br>the blip function parameter β . Supp ose now<br>that we are concerned with estimating E ( Y � a )<br>for a given treatment regime � a = ( a 0 , . . . , a K ).<br>In order to derive an estimator of this param-<br>eter we will do as if β , i.e. the set of blip<br>, is known. The actual prop osed<br>functions βj<br>estimator of E ( Y � a ) is obtained by substituting<br>an estimate for β .<br>For each subject construct the following vari-<br>able<br>K<br>�<br>�<br>Y 0 ( β ) =  YA − � βl ( Al, L � l ) .<br>l =<br>The variable Y 0 ( β ) represents a substitute for<br>the variable Y one would have seen if the<br>0<br>subject had never b een treated. As ab ove<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
Thus the random variable Y has the same<br>� a ( β )<br>exp ectation as the treatment sp eci�c coun-<br><!-- End of picture text -->


<!-- Start of picture text -->
terfactual Y . Thus it remains to understand<br>� a<br>how to estimate EY<br>� a ( β ).<br><!-- End of picture text -->

Note that the exp ectation of _βl_ ( _A_ � _l, L_ � _l_ ) is taken in the world where everyb o dy get assigned � treatment _A_ = � _a_ , which comes down to integrating w.r.t. the joint distribution of the counterfactuals of _L_ and 0<sup>_, L_</sup> _a_<sup>_, L_</sup> _a_<sup>_a, . . . , Ll,_</sup> � _al_ � setting _AK_ = � _aK_ . This joint distribution is obtained with the general _G_ -computation formula which we will give now. First write down the density representation for _L_ : 0<sup>_, A_</sup> 0<sup>_, L, A, . . . , L_</sup> _l_<sup>_, A_</sup> _l f_ ( _L_ 0 ) _f_ ( _A_ 0<sup>_| L_</sup> 0 ) _f_ ( _L_<sup>_|_</sup> _A_ �0<sup>_, L_</sup> 0 ) _f_ ( _A_<sup>_|_</sup> _A_ �0<sup>_,_</sup> _L_ � ) _. . . f_ ( _Ll | L_ � _l− , A_ � _l−_ ) _f_ ( _Al | L_ � _l, A_ � _l−_ ) _._ Replacing _f_ ( _Aj | A_ � _j− , L_ � _j_ ) by a degenerate distribution at _Aj_ = _aj_ , _j_ = 0 _, . . . , l_ , results


<!-- Start of picture text -->
in the wished joint density P ( L 0 = s 0 , L a =<br>s , L a a = s , . . . , L l, � al =  sl ) given by:<br>�<br>P = ) .<br>� l ( Lj = sj | Aj− � aj− , L � j− = sj−<br>j =0<br>The latter formula is referred to as the G-<br>computation formula and indeed equals the<br>counterfactual density under the sequential<br>randomization assumption.<br>We conclude that we have the following for-<br>mula for EY :<br>� a<br>K<br>EY � a = EY 0 ( β ) + � βl (� al, � sl )<br>� s ,...,s l<br>l =<br>�<br>� l P ( Lj = sj | Aj− = � aj− , L � j− =  sj− )<br>j =0<br>This formula expresses the counterfactual ex-<br>p ectation  EY � a in terms of observed data distri-<br>butions and the blip function. Consequently,<br><!-- End of picture text -->


<!-- Start of picture text -->
we can use this formula to estimate EY . Be-<br>� a<br>yond estimation of the blip function it requires<br>estimation of the conditional distribution of<br>Lj , given the past.<br>For testing the presence of a treatment ef-<br>fect one is only concerned with estimation of<br>the blip function itself which do es not require<br>mo delling of covariate distributions. If one<br>uses the formula to estimate EY for various<br>� a<br>� a , then these estimates are protected agains<br>missp eci�cation of the covariate distributions<br>under the null-hyp othesis of no-treatment ef-<br>fect.<br><!-- End of picture text -->


<!-- Start of picture text -->
+ +<br>EXTENSION TO DYNAMIC REGIMES<br><!-- End of picture text -->


<!-- Start of picture text -->
For a given set of rules d � = ( d ( · ) , . . . , dK ( · ))<br>let Y b e the counterfactual outcome of Y if<br>d �<br>�<br>one follows the rules Aj = dj ( Aj− , L � j ). Sup-<br>p ose we want to estimate EY .<br>d �<br>We already provided estimators for the blip<br>function and we can also still de�ne Y as<br>0 ( β )<br>ab ove. De�ne<br>K<br>Yd �( β ) ≡ Y 0 ( β ) + � βl ( A � l, ) ,<br>L � l,d � l<br>l =0<br>where ( A � l, L � l,d � l ) follows the counterfactual dis-<br>tribution one would observe in the hyp othet-<br>ical world where everyb o dy follows the dy-<br>namic treatment regime d �. As ab ove one can<br>show that the exp ectation of Y ( β ) equals the<br>d �<br>exp ectation of Y . Thus it remains to esti-<br>d �<br>mate EY ( β ).<br>d �<br>+<br><!-- End of picture text -->

This counterfactual distribution of ( _A_ � _l, L_ � _l,d_ � _l_ ) is obtained with the general _G_ -computation formula. First write down the density representation for the data _L_ 0<sup>_, A_</sup> 0<sup>_, L, A, . . . , L_</sup> _l_<sup>_, A_</sup> _l_ : _f_ ( _L_ 0 ) _f_ ( _A_ 0<sup>_| L_</sup> 0 ) _f_ ( _L_<sup>_|_</sup> _A_ �0<sup>_, L_</sup> 0 ) _f_ ( _A_<sup>_|_</sup> _A_ �0<sup>_,_</sup> _L_ � ) _. . . f_ ( _Ll | L_ � Replacing _f_ ( _Aj | Aj−_ = � _aj− , L_ � _j_ = � _sj_ ) by a degenerate distribution at _dj_ (� _aj− ,_ � _sj_ ), _j_ = 0 _, . . . , l_ , results in the wished joint density _P_ ( _L_ 0 = _s_ 0<sup>_, L_</sup> _d_ = _s_<sup>_, L_</sup> _d_<sup>_d_</sup> = _s_<sup>_, . . . , L_</sup> _l,d_ � _l_ = _sl_ ) given by: � � _l P_ ( _Lj_ = _sj | Aj−_ = _dj_ (� _aj− , L_ � _j_ ) _, L_ � _j−_ = _s_ � _j−_ ) _. j_ =0 The latter formula is referred to as the G- computation formula and indeed equals the counterfactual density under the sequential randomization assumption.


<!-- Start of picture text -->
We conclude that we have the following for-<br><!-- End of picture text -->


<!-- Start of picture text -->
mula for EY :<br>d �<br>K<br>EYd � =  EY 0 ( β ) + � βl (� al, � sl )<br>� s ,...,s l<br>l =<br>�<br>� l P ( Lj =  sj | Aj− =  dj (� aj− , � sj ) , L � j− = s � j− )<br>j =0<br>Given estimates of the conditional distribu-<br>tions of Lj , given the past, for j = 0 , . . . , K ,<br>given β and thus Y 0 ( β ) one can evaluate this<br>multivariate integral by simply simulating a<br>large numb er of the variables Yd �( β ). This<br>avoids the need of numerical integration.<br><!-- End of picture text -->

---

[Up: contents](index.md)
