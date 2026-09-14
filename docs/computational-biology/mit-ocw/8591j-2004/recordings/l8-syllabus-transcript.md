---
title: L8 syllabus transcript
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l8-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# L8 syllabus transcript

**Source:** `recordings/l8-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **VI Modeling** **_Escherichia coli_ chemotaxis**

In this lecture we will discuss and contrast two models that model bacterial chemotaxis:

1. P. A. Spiro, J. S. Parkinson, and H. G. Othmer. A model of excitation and adaptation in bacterial chemotaxis. _PNAS_ **94** , 7263-7268 (1997).

2. N. Barkai and S. Leibler. Robustness in simple biochemical networks. _Nature_ **387** , 913-917 (1997).

In Spiro’s model the Tar receptor always forms a complex with CheA and CheW. CheW functions as an adapter (scaffolding) protein and has no enzymatic function.  The complex has two phosphorylation states (due to CheA), three methylation states, and ligand bound or unbound state. These 12 different states are summarized in Fig. 2 of Spiro’s paper. The ligand (un)binding reactions are the fast reactions (millisecond) whereas the methylation reaction are slow (minutes). The phosphorylation reactions span the intermediate time scales. Below we will explore Spiro’s model and try to pinpoint why this model has to be fine-tuned in order to reproduce perfect adaptation. This is in contrast to Barkai’s model (see below) that does not need fine-tuning to obtain perfect adaptation.

First, let us assume that we only have to consider two methylation states (2 and 3 methyl groups). Including more methylation states does not fundamentally change the properties of the model. We can always assume that we operate at low concentrations of external ligand so that only the low methylation states will be relevant. Remember that the number of methylated sites increases with increasing ligand concentration.

With this assumption the 12 different receptor states reduce to 8 states.

Secondly, the time scale of ligand binding and unbinding is almost three orders of magnitude faster than the phosphorylation and methylation times. We can therefore treat the ligand (un)binding reactions as equilibria. This reduces the possible receptor states to 4 (Fig. 7, Matlab code 3).

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

27


<!-- Start of picture text -->
keff4(L)<br>T2p T3p<br>LT2p  LT3p<br>keff3(L)<br>kpt  kpt<br>keff1(L)  keff2(L)<br>keff4(L)<br>T2  T3<br>LT2  LT3<br>Figure 7.  Reduced version of Spiro’s<br>keff3(L)  model.<br><!-- End of picture text -->

The fraction of receptors that are bound to a ligand fb can be written as (analogous to [II.12], n = 1):


where L is the ligand concentration and Kb is the association constant for ligand binding:


The effective rates are weighted averages of the rates given by Spiro:


The rates on the right hand side are the rates defined in Spiro’s paper. The effective methylation rate can not be written down by a single effective rate constant as

methylation is assumed to obey Michaelis-Menten kinetics. The methylation rates of the non-phosphorylated and phosphorylated receptors are, respectively:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

28


where [2] and [2p] are the total concentrations of non-phosphorylated and phosphorylated receptors with two methylation sites. The maximum turnover rates are Vmax1=k1cR and Vmax3=k3cR, where R is the total amount of CheR. KR is the Michaelis constant for receptor-CheR binding (1.7 µM). Note that the phosphotransfer rate is independent of L.


What is needed for perfect adaptation? Can we write a general relation that tells us how to fine-tune the rate constants?

Suppose the methylation rates [VI.4] would obey ordinary first order kinetics, in this case we can write simple ratios between the different receptor states:


This system is over-determined (4 unknowns, 5 equations) since the total amount of receptor is fixed. In other words no steady state solution exists. By assuming MichaelisMenten kinetics [VI.4] you can introduce one additional variable that ‘solves’ this issue.

Let’s go back to the perfect adaptation. Perfect adaptation means that in steady state the number of phosphorylated receptors is independent of the ligand concentration: the effective phosphorylation rate is independent of ligand concentration. On long time scale the network (Fig. 7) will equilibrate having a fraction (1-α) in state [2] and a fraction α in state [3]. The net phosphorylation rate will then be:


To obtain perfect adaptation α should be:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

29

The main point is that it is very difficult to obtain perfect adaptation in this model. It works for a very specific set of constants, but small variations from this set will lead to non-perfect adaptation.

Barkai’s model uses a similar approach but differs in a subtle way by making crucial different assumptions. The main difference is that CheB only demethylates phosphorylated (‘active’) receptors. As in Spiro’s model, Barkai’s model can reduced to four states (Fig. 8).


<!-- Start of picture text -->
keff3(L)<br>T T<br>2p 3p<br>LT LT<br>2p  3p<br>keff4(L)<br>kpt  kpt<br>keff1(L)  keff2(L)<br>T2  keff3(L) T3<br>LT2 LT3<br><!-- End of picture text -->

**Figure 8.** Stripped down version of Barkai’s model.

A second important assumption is that the methylation rates operate at saturation since [CheR] is much smaller than the concentration of receptors. This means that methylation rate is constant and is independent of [2] and [2p]. The final crucial assumption is that demethylation is independent of ligand binding. This leads to the reduce scheme depicted in Fig. 9.


<!-- Start of picture text -->
rin<br>T3p<br>LT3p<br>keff4<br>kpt<br>keff2(L)<br>rin<br>T3<br>LT3<br><!-- End of picture text -->

**Figure 9.** Even more stripped down version of Barkai’s model.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

30

Where rin is the saturated methylation rate that is independent of [2] and [2p]. The kinetic equations for these reactions are:


The total amount of receptor evolves according to:


In steady state this means that the concentration of [3p] is:


independent of the properties of the phosphorylation reaction and external ligand concentration. This system will therefore obey perfect adaptation, for any change in ligand concentration.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

31


**Figure 10.** Upper panel: perfect adaptation is observed for certain values of the net phoshorylation rate if k11>k9. Perfect adaptation is not observed if k11<k9 (lower panel). See equation [VI.3] for definition of rate constants.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

32

**Matlab code 4:** Spiro model

% filename spiro.m clear; close; To=8e-6; Yo=20e-6; Bo=1.7e-6; options = odeset('RelTol',1e-9,'AbsTol',[1e-9 1e-9 1e-9 1e-9 1e-9]); [t y]=ode23('spirofunc',[0 80],[4e-6 4e-6 0e-6 0.5e-6 10e-6],options); Ptot=To-y(:,1)-y(:,2); Bp=y(:,4); Yp=y(:,5); metlevel=1-(y(:,1)+y(:,3))/To; phoslevel=1-(y(:,1)+y(:,2))/To; subplot(2,2,1) plot(t,phoslevel,'bx'); axis([10 80 0 0.1]); title('Phosphorylation Level'); subplot(2,2,2) plot(t,metlevel,'rx'); title('Methylation Level'); axis([10 80 0 1]); subplot(2,2,3) plot(t,Bp/Bo,'gx'); axis([10 80 0 1]); title('Bp/Btot'); subplot(2,2,4) plot(t,Yp/Yo,'yx'); axis([10 80 0 1]); title('Yp/Ytot');

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

33

%filename spirofunc.m function dydt = f(t,y,flag)

% constants from Table 3 (Spiro et al.)

k1c=0.17; % 1/s k3c=30*k1c; % 1/s ratiok1bk1a=1.7e-6; % M ratiok3ck3a=1.7e-6; % M k_1=4e5; % 1/(Ms) k_3=k_1; % 1/(Ms) k8=15; % 1/s k9=3*k8; % 1/s k11=0; % 1/s %k12=1.1*k8; % 1/s k12=30; kb=8e5; % 1/(Ms) ky=3e7; % 1/(Ms) k_b=0.35; % 1/s k_y=5e5; % 1/(Ms) Kbind=1e6; % 1/M Yo=20e-6; % M Bo=1.7e-6; % M To=8e-6; % M Ro=0.3e-6; % M Zo=40e-6; % M % [T2]+[LT2] = y(1) % [T3]+[LT3] = y(2) % [T2p]+[LT2p] = y(3) % [Bp] = y(4) % [Yp] = y(5) cligand=1e-6; if t>20 cligand=1e-3; end; if t>50 cligand=1e-6; end; Vmaxunbound=k1c*Ro; % maximum turnover rate (MM kinetics) for unbound receptors Vmaxbound=k3c*Ro; % maximum turnover rate (MM kinetics) for bound receptors KR=ratiok1bk1a; % Michaelis constant fb=Kbind*cligand/(1+Kbind*cligand); % fraction receptors bound to ligand fu=1-fb; % fraction receptors not bound to ligand kpt=ky*(Yo-y(5))+kb*(Bo-y(4)); ydot1=(-k8*fu-k11*fb)*y(1)+kpt*y(3)+(k_1*fu+k_3*fb)*y(2)*y(4)Vmaxunbound*y(1)*fu/(KR+y(1)*fu)-Vmaxbound*y(1)*fb/(KR+y(1)*fb); ydot2=(-k9*fu-k12*fb)*y(2)+kpt*(To-y(1)-y(2)-y(3))(k_1*fu+k_3*fb)*y(2)*y(4)+Vmaxunbound*y(1)*fu/(KR+y(1)*fu)+Vmaxbound*y(1)*f b/(KR+y(1)*fb); ydot3=(k8*fu+k11*fb)*y(1)-kpt*y(3)+(k_1*fu+k_3*fb)*(To-y(1)-y(2)y(3))*y(4)-Vmaxunbound*y(3)*fu/(KR+y(3)*fu)+Vmaxbound*y(3)*fb/(KR+y(3)*fb); ydot4=kb*(To-y(1)-y(2))*(Bo-y(4))-k_b*y(4); ydot5=ky*(To-y(1)-y(2))*(Yo-y(5))-k_y*y(5)*Zo; dydt=[ydot1; ydot2; ydot3; ydot4; ydot5];

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

34

---

[Up: contents](../index.md)
