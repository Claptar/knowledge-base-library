---
title: Predicting Protein Structure
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/13-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/13-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Predicting Protein Structure

- L12 - Introduction to Protein Structure; Structure Comparison & Classification
- **L13 - Predicting protein structure**
- **L14 - Predicting protein interactions**
- **L15 - Gene Regulatory Networks**
- **L16 - Protein Interaction Networks**
- **L17 - Computable Network Models**

---

secondary structure

IQVFLSARPPAPEVSKIY
DNLILQYSPSKSLQMILR
RALGDFENMLADGSFR
AAPKSYPIPHTAFEKSIIV
QTSRMFPVSLIEAARNH
FDPLGLETARAFGHKLA
TAALACFFAREKATNS

domain structure

novel 3D structure

---

## Statisticians vs. Physicists

"Data don't make any sense, we will have to resort to statistics."

Institut für Quantenphysik
Sie befinden sich
HIER oder HIER

---

## What were the key simplifications of the statistical approach?

"Data don't make any sense, we will have to resort to statistics."

Institut für Quantenphysik
Sie befinden sich
HIER oder HIER

---

## Threading (fold recognition)

IQVFLSARPPAPEVSKIY
DNLILQYSPSKSLQMILR
RALGDFENMLADGSFR
AAPKSYPIPHTAFEKSIIV
QTSRMFPVSLIEAARNH
FDPLGLETARAFGHKLA
TAALACFFAREKATNS

**?**

**How could we use the potential energy function to recognize the correct fold?**

---

## Methods for Refining Structures

1. Energy minimization
2. Molecular dynamics
3. Simulated Annealing

---

## 1. Energy Minimization

THERMODYNAMIC CONTROL

KINETIC CONTROL

FIGURE 1: Schematic diagram of one-dimensional cross sections through the free energy surfaces of protein folding reactions contrasting two extremes: thermodynamic vs kinetic control. A simple folding surface with a single free energy minimum is shown in panel a. Such a molecule would fold under thermodynamic control, seeking out the most stable state. This is to be contrasted with the considerably more convoluted energy surface in panel b. Because of the high barriers, starting at different locations could lead to different final conformations.

Source: Baker, David, and David A. Agard. "Kinetics Versus Thermodynamics in Protein Folding." *Biochemistry* 33, no. 24 (1994): 7505-9.

---

## Consider a small error in a structure

- True structure
- Misplaced side chain

cannot make h-bonds

Examples from this good tutorial

---

## Can we restore the side chain?

Energy vs Angle

---

## Minimization

- We have equations for U(x,y,z).
- Find nearby values of x,y,z that minimize U.

Energy vs Angle

---

## Gradient Descent

$f(x) = x^3 - 2x^2 + 2$

$$f'(x) = 0$$

http://mathworld.wolfram.com/MethodofSteepestDescent.html

---

## Gradient Descent

$f(x) = x^3 - 2x^2 + 2$

$$x_i = x_{i-1} - \varepsilon f'(x_{i-1})$$

http://mathworld.wolfram.com/MethodofSteepestDescent.html

---

## Gradient Descent

$f(x) = x^3 - 2x^2 + 2$

$$x_i = x_{i-1} - \varepsilon f'(x_{i-1})$$

**Can require many iterations**

$x_0 = 2$

$x_0 = 0.01$

http://mathworld.wolfram.com/MethodofSteepestDescent.html

---

One dimension
$$x_i = x_{i-1} - \varepsilon f'(x_{i-1})$$

N dimensions
$$\vec{x}_1 = \vec{x}_0 - \varepsilon \nabla U_0(\vec{x}_0)$$

Where gradient is defined as
$$\nabla U = \left( \frac{\partial U}{\partial x_1}, \dots, \frac{\partial U}{\partial x_n} \right)$$

Since Force is $F = -\nabla U$
$$\vec{x}_1 = \vec{x}_0 + \varepsilon F_0(\vec{x}_0)$$

each step is moving in the direction of the force

---

## Minimization

- Convergence can be a problem on some surfaces. More sophisticated approaches are available
- Our example used a continuous energy function, but can be define for discrete optimization too.

---

## Can we restore the side chain?

Starting conformation
Unsuccessful minimization

Always limited to local search

Good tutorial

---

## 2. Molecular Dynamics

- Seeks to simulate the motion of molecules
- Can escape local minima

$$x(t_i) = x(t_{i-1}) + v(t_{i-1}) \times (t_i - t_{i-1})$$

$$v(t_i) = v(t_{i-1}) + \frac{F(t_{i-1})}{m} \times (t_i - t_{i-1})$$

$$v(t_i) = v(t_{i-1}) - \frac{\nabla U(t_{i-1})}{m} \times (t_i - t_{i-1})$$

Movie: Simulation of protein folding

---

## Notes

- Short simulations take tremendous computing resources
- Length of simulation and protocol determine **radius of convergence**

---

## 3. Simulated Annealing

- Physical annealing - high temperature is used to avoid metal defects (local minima).
- Simulated annealing is analogous, and can be applied to many optimization problems

Simulated Annealing can escape local minima with chaotic jumps

---

## 3. Simulated Annealing

- At low temperature we cannot escape local minima
- At high temperature the kinetic energy exceeds the potential energy barrier

---

## 3. Simulated Annealing

- Atoms find equilibrium distribution at higher temperatures
- How can we find the equilibrium distribution of a complicated potential function?

Simulated Annealing can escape local minima with chaotic jumps

http://homesteadingsurvival.myshopify.com/products/115-blacksmithing-forging-welding-metallurgy-sword-books-on-dvd-rom

http://www.stanford.edu/~hwang41/mcmc.png

---

## 3. Simulated Annealing

- Start at high temperature
- Find most probable states
- Reduce temperature to trap these states

Simulated Annealing can escape local minima with chaotic jumps

http://homesteadingsurvival.myshopify.com/products/115-blacksmithing-forging-welding-metallurgy-sword-books-on-dvd-rom

http://www.stanford.edu/~hwang41/mcmc.png

---

## Metropolis Algorithm

- Goal: efficiently search a large conformation space.
- Can be understood in terms of physical processes, but much more general
- Note the difference from molecular dynamics:
  - Molecules move under physical forces but temperatures are far outside of normal range
  - **A sampling method not a simulation!**

---

## Acceptance Criteria

- Randomly choose neighboring state:
  - Always accept moves that reduce potential
  - Go uphill (higher potential) based on odds ratio

$$\frac{P(S_{\text{test}})}{P(S_n)} = \frac{e^{-E_{\text{test}} / kT}}{Z(T)} \Bigg/ \frac{e^{-E_n / kT}}{Z(T)} = e^{-(E_{\text{test}} - E_n) / kT}$$

---

## 3. Metropolis sampling

Iterate for a fixed number of cycles or until convergence:

1. Start with a system in state $S_n$ with energy $E_n$
2. Choose a neighboring state at random; we will call it the proposed state : $S_{\text{test}}$ with energy $E_{\text{test}}$
3. If $E_{\text{test}} < E_n : S_{n+1} = S_{\text{test}}$
4. Else set $S_{n+1} = S_{\text{test}}$ with probability $P = e^{-(E_{\text{test}} - E_n)/kT}$
   - otherwise $S_{n+1} = S_n$

---

Minimization vs. simulated annealing

---

$1 \xrightarrow{P=1} 2$
$2 \xrightarrow{P=e^{-\Delta G/kT}} 3$
$3 \xrightarrow{P=e^{-\Delta G/kT}} 4$
$4 \xrightarrow{P=1} 5$

---

## Acceptance Criteria

- Always go down-hill
- Go uphill based on odds ratio

$$\frac{P(S_{\text{test}})}{P(S_n)} = \frac{e^{-E_{\text{test}} / kT}}{Z(T)} \Bigg/ \frac{e^{-E_n / kT}}{Z(T)} = e^{-(E_{\text{test}} - E_n) / kT}$$

How does T alter outcome?

---

## Acceptance Criteria

- Always go down-hill
- Go uphill based on odds ratio

$$\frac{P(S_{\text{test}})}{P(S_n)} = \frac{e^{-E_{\text{test}} / kT}}{Z(T)} \Bigg/ \frac{e^{-E_n / kT}}{Z(T)} = e^{-(E_{\text{test}} - E_n) / kT}$$

Annealing schedule:
- Start at High T
- Lower slowly

---

## 3. Metropolis sampling – prob. version

To identify minima given a probability function: $P(S)$
1. Start with a system in state $S_n$
2. Choose a neighboring state at random : $S_{\text{test}}$
3. Compute acceptance ratio $a = \frac{P(S_{\text{test}})}{P(S_N)}$
4. If $a > 1 : S_{n+1} = S_{\text{test}}$
5. Else set $S_{n+1} = S_{\text{test}}$ with probability $a$ and $S_{n+1} = S_n$ with probability $1 - a$

*Not specific to protein structure. Used to sample diverse probability distributions*

---

## Review: Methods for Refining Structures

1. Energy minimization
2. Molecular dynamics
3. Simulated annealing

---

## Methods for Predicting Structure

IQVFLSARPPAPEVSKIY
DNLILQYSPSKSLQMILR
RALGDFENMLADGSFR
AAPKSYPIPHTAFEKSIIV
QTSRMFPVSLIEAARNH
FDPLGLETARAFGHKLA
TAALACFFAREKATNS

$\longrightarrow$ novel 3D structure

---

## What actually works for structure prediction?

**CASP1**

*(First meeting on Critical Assessment of techniques for protein Structure Prediction)*

**A Large-Scale Experiment to Assess Protein Structure Prediction Methods**

*PROTEINS: Structure, Function, and Genetics* 23:ii–iv (1995)

**COLLECTING PREDICTION TARGETS**

Information was solicited from X-ray crystallographers and NMR spectroscopists about structures that were either expected to be solved shortly or that had been solved already but not discussed in public. Targets were identified through personal contacts, blanket emailing, and appeals at scientific meetings. The collecting and management of prediction targets proved to be a difficult undertaking. In all, information on 33 different proteins was obtained. Some of these were not solved in time for the prediction experiment and some were made public without sufficient notice to the predictors. Finally, one or more predictions were received on 24 of these targets.

---

## Rosetta

Raman et al. Proteins 2009; 77(Suppl 9):89–99.
http://onlinelibrary.wiley.com/doi/10.1002/prot.22540/full

- Two types of models:
  - Homology
  - *de novo*

---

## Homology

- Align query to sequences in PDB
- Use several alignment methods
- Three categories of queries:
  1. High sequence similarity template(s) (>50% sequence similarity).
  2. Medium sequence similarity template(s) (20–50% sequence similarity).
  3. Low sequence similarity template(s) (<20% sequence similarity).

---

## Homology

- Align query to sequences in PDB } tools you have seen earlier in the course
- Use several alignment methods }
- Refine models

---

## General Refinement Procedure

- Random changes to backbone torsion angles
- Rotamer optimization of side chains
- Energy minimization of torsion angles (bond lengths and angles kept fixed)

---

## Homology

High sequence similarity template(s) (>50% sequence similarity).
- Minimal refinement, focused on regions where alignment is poor.

---

## Homology

Medium sequence similarity template(s) (20–50% sequence similarity).
- Proceed with several alignments
- Refine structures
- Choose best model by final energy

---

## Homology

Medium sequence similarity template(s) (20–50% sequence similarity).
- Refinement focuses on regions near gaps and insertions, loops in the starting model, and sequence segments with low conservation
- Replaces torsion angles with those from peptides of known structure
- Minimize local structure
- Refine global structure

## Native structure

Best model

Best template

© Wiley-Liss. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Raman, Srivatsan, Robert Vernon, et al. "Structure Prediction for CASP8 with All-atom Refinement using Rosetta." *Proteins: Structure, Function, and Bioinformatics* 77, no. S9 (2009): 89-99.

---

## Accurate side chains in core

© Wiley-Liss. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Raman, Srivatsan, Robert Vernon, et al. "Structure Prediction for CASP8 with All-atom Refinement using Rosetta." *Proteins: Structure, Function, and Bioinformatics* 77, no. S9 (2009): 89-99.

---

## Homology

Low sequence similarity template(s) (<20% sequence similarity).

- Use many more starting models
- More aggressive refinement strategy
  - Rebuild secondary structure elements in addition to regions refined in medium homology:
    - gaps and insertions
    - loops in the starting model
    - regions with low conservation

---

Native | Best Model | Native | Best Model

© Wiley-Liss. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Raman, Srivatsan, Robert Vernon, et al. "Structure Prediction for CASP8 with All-atom Refinement using Rosetta." *Proteins: Structure, Function, and Bioinformatics* 77, no. S9 (2009): 89-99.

---

## de novo

- When there is no suitable homology model:
  - Monte Carlo search for backbone angles
    - Choose a short region (3-9 amino acids) of backbone
    - Set torsion angles to those of a similar peptide in PDB
    - Accept with metropolis criteria
  - 36,000 MC steps
  - Repeat entire process to get 2,000 final structures
  - Cluster structures
  - Refine clusters

---

## How has modeling changed during the CASP challenges?

### CASP1

*(First meeting on Critical Assessment of techniques for protein Structure Prediction)*

### A Large-Scale Experiment to Assess Protein Structure Prediction Methods

PROTEINS: Structure, Function, and Genetics 23:ii-iv (1995)

#### COLLECTING PREDICTION TARGETS

Information was solicited from X-ray crystallographers and NMR spectroscopists about structures that were either expected to be solved shortly or that had been solved already but not discussed in public. Targets were identified through personal contacts, blanket emailing, and appeals at scientific meetings. The collecting and management of prediction targets proved to be a difficult undertaking. In all, information on 33 different proteins was obtained. Some of these were not solved in time for the prediction experiment and some were made public without sufficient notice to the predictors. Finally, one or more predictions were received on 24 of these targets.

---

## Improvement over the last decade: Percentage of residues successfully modeled

Andriy Kryshtafovych, Krzysztof Fidelis, John Moult

Each point represents the best model for a target

CASP10 and CASP9 are similar, much better than CASP5.

Target difficulty -based on structural and sequence similarity of a target to proteins of known structure

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Kryshtafovych, Andriy, Krzysztof Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." *Proteins: Structure, Function, and Bioinformatics* 82, no. S2 (2014): 164-74.

---

## Overall Prediction Accuracy Did Not Improve

**Global distance test**
**GDT_TS**
=overall accuracy of a model

average % of $\text{C}\alpha$ atoms in the prediction close to corresponding atoms in the target structure

**Perfect model: 90-100**
**Random model: 20-30**

Target difficulty is based on structural and sequence similarity of a target to proteins of known structure

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Kryshtafovych, Andriy, Krzysztof Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." *Proteins: Structure, Function, and Bioinformatics* 82, no. S2 (2014): 164-74.

---

## Overall Prediction Accuracy Did Not Improve

Why is the trend line the same?

Are targets getting harder in other ways?
Multi-domain, multi-chain, etc.

Target difficulty is based on structural and sequence similarity of a target to proteins of known structure

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Kryshtafovych, Andriy, Krzysztof Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." *Proteins: Structure, Function, and Bioinformatics* 82, no. S2 (2014): 164-74.

---

## Free modeling results

*de novo*
(no template)

---

## Free Modeling in Flux

Andriy Kryshtafovych, Krzysztof Fidelis, John Moult

**Global distance test**
GDT_TS =overall accuracy of a model

average percentage of $\text{C}\alpha$ atoms in the prediction close to corresponding atoms in the target structure

**Perfect model: 90-100**
**Random model: 20-30**

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Kryshtafovych, Andriy, Krzysztof Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." *Proteins: Structure, Function, and Bioinformatics* 82, no. S2 (2014): 164-74.

---

## Free Modeling in Flux

Andriy Kryshtafovych, Krzysztof Fidelis, John Moult

GDT_TS
Perfect model: 90-100
Random model: 20-30

- CASP9 results for <120 AA were great. 5/11 had GDT >60.
- CASP10 were mediocre (three models >60 but four <40)
- CASP5 had only 1/5 >60

© Wiley Periodicals, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Kryshtafovych, Andriy, Krzysztof Fidelis, et al. "CASP10 Results Compared to those of Previous CASP Experiments." *Proteins: Structure, Function, and Bioinformatics* 82, no. S2 (2014): 164-74.

---

## Free Modeling in Flux

Andriy Kryshtafovych, Krzysztof Fidelis, John Moult

"Current FM [free modeling] methods perform best on single domain regular structures... The apparent lack of progress in CASP10 and ROLL compared with CASP5 probably again reflects the more difficult nature of CASP10 targets.

First, many targets which in CASP5 would have been in this category now have templates ...

CASP10 FM targets exhibit more irregularity, and more of a tendency to be domains of larger proteins that are hard to identify from sequence and that may be dependent on the rest of the structure for their conformation.

---

## Statisticians vs. Physicists

"Data don't make any sense, we will have to resort to statistics."
Courtesy of VADLO.com. Used with permission.

### Rosetta

- Leverage everything we know about existing structures of proteins and peptides to build starting models
- Refine using a knowledge-based potential

---

## Statisticians vs. Physicists

*Institut für Quantenphysik*
Sie befinden sich HIER oder HIER

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

### DE Shaw

- DON'T CHEAT!
- Only use physical forces.
- Fold proteins by simulating the *in vitro* process

---

## DE Shaw

- Lindorff-Larsen et al. (2011) *Science*
- Simulate protein folding.
- Why had no one else succeeded at this?

Courtesy of Nature Publishing Group. Used with permission.
Source: Dill, Ken A. and Hue Sun Chan. "From Levinthal to Pathways to Funnels." *Nature Structural Biology* 4, no. 1 (1997): 10-9.

---

---

[Up: contents](index.md) · [DE Shaw →](02-de-shaw.md)
