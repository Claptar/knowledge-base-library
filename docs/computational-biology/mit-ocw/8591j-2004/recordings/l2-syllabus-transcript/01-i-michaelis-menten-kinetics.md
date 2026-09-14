---
title: I Michaelis-Menten kinetics
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l2-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# I Michaelis-Menten kinetics

**Source:** `recordings/l2-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The goal of this chapter is to develop the mathematical techniques to quantitatively model biochemical reactions. Biochemical reactions in living cells are often catalyzed by enzymes. These enzymes are proteins that bind and subsequently react specifically with other molecules (other proteins, DNA, RNA, or small molecules) defined as substrates. A few examples:

1. The conversion of glucose (substrate) into glucose-6-phosphate (product) by the protein hexokinase (enzyme).

2. Transcription: binding of the RNA polymerase (enzyme) to the promoter region of the DNA (substrate) results in transcription of the mRNA (product).

3. The phosphorylation of a protein: the unphosphorylated protein CheY (substrate, regulating the direction of rotation of the bacterial flagella) is phosphorylated by a phosphate CheZ (enzyme) resulting in CheY-p (product).

All these reactions involve a substrate S reacting with an enzyme E to form a complex ES which then in turn is converted into product P and the enzyme:


In this scheme there are two fundamental different reactions. The first reaction depicted with the double arrow is a reversible reaction reflecting the reversible binding and unbinding of the enzyme and the substrate. The second reaction is an irreversible reaction in which the enzyme-substrate complex is irreversibly converted into product and enzyme symbolized by the single arrow. The rate of a reaction is proportional to the product of the concentrations of the reactants. The kinetics of the chemical equations above is described by the following set of coupled differential equations:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

2


Note that _k1_ and _k-1_ have different units, 1/(Ms) and 1/s respectively. The turnover rate _v_ is defined as the increase (or decrease) in product over time, which is directly proportional to the concentration of enzyme-substrate complex [ES]. For the analysis below we will assume initial conditions: [S]t=0 = So; [E]t=0 = Eo; [ES]t=0 = 0; [P]t=0 = 0.

Since the enzyme is a catalyst that facilitates the reaction but does not react itself, the total concentration of enzyme (free + bound) should be constant:


Using this conservation law the four differential equations [I.2] reduce to three coupled ordinary differential equations:


with the initial conditions [S]t=0 = So, [ES]t=0 = 0, and [P]t=0 = 0. Matlab code 1 solves these equations and calculates the time dependence of the concentrations [S], [ES] and [P] as a function of the initial concentrations [So] and [Eo] and the rate constants k1, k-1, and k2. In this case the systems can also be solved analytically. Figure 1 shows an example of the time dependence of the chemical components for k1[So] ≈ k-1 >> k2. This is often the regime of biological relevance since the substrate-enzyme binding occurs at much faster time scales than the turnover into product. The thermodynamic equilibrium or steady state (t→∞) of this system would be [S] = [ES] = 0; [E] = [Eo]; [P] = [So]. However the relevant time-scale to consider is the time range in which [ES] and [E] are

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

3

relatively constant. This state is often called the quasi-equilibrium or pseudo-steady state. Under these circumstances one expects that after an initial short transient period there will be a balance between the formation of the enzyme-substrate complex and the breaking apart of complex (either to enzyme and substrate, or to enzyme and product). In the pseudo-steady state (d[ES]/dt = d[E]/dt = 0) (I.4) reduces to:


In the case of many more substrate than enzyme molecules (So >> Eo), this pseudo-steady state will be achieved before there is perceptible transformation of substrate into product. In this case the equation [I.5] leads to the traditional Michaelis-Menten equation, which predicts the initial turnover rate of the enzymatic reaction vo as a function of initial substrate concentration So:


where the constant Km = (k-1+k2)/kl is called the Michaelis constant and vmax = k2Eo is the maximum turn-over rate. The Michaelis constant has units of concentration and reflects the affinity of the reaction. Strong affinity means small Km. At a concentration Km the turn-over rate is 0.5vmax (Fig. 2).

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

4


**Figure 1.** The time dependence of the substrate, enzyme, enzyme-substrate complex, and product concentration. This graph was generated by using Matlab code 1. The upper panel uses a logarithmic x-axis whereas the lower panel uses a linear scale.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

5


**Figure 2.** The initial turnover rate as given by the Michaelis-Menten formula [I.6].

**Matlab code 1:** Michaelis-Menten kinetics

**% filename: mm.m k1=1e3; % units 1/(Ms) k_1=1; % units 1/s k2=0.05; % units 1/s E0=0.5e-3; % units M options=[];**

**[t y]=ode23('mmfunc',[0 100],[1e-3 0 0],options,k1,k_1,k2,E0); S=y(:,1); ES=y(:,2); E=E0-ES; P=y(:,3); plot(t,S,'r',t,E,'b',t,ES,'g',t,P,'c');**

**% filename: mmfunc.m function dydt = f(t,y,flag,k1,k_1,k2,E0) % [S] = y(1), [ES] = y(2), [P] = y(3) dydt = [-k1*E0*y(1)+(k1*y(1)+k_1)*y(2); k1*E0*y(1)-(k1*y(1)+k_1+k2)*y(2); k2*y(2)];**

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

6

---

[Up: contents](index.md) · [II Equilibrium binding and cooperativity →](02-ii-equilibrium-binding-and-cooperativity.md)
