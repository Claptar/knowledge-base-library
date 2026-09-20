---
title: 2. Rosetta (Statistician's Approach)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-02-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-04-02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. Rosetta (Statistician's Approach)

- Assigns energy values for many of the same forces as CHARMM, but does so by comparing the protein's conformation with those of other observed structures instead of from first principles (e.g. modeling forces as harmonic oscillators, etc.)

$$\text{Energy} = w_1*\text{term}_1 + w_2*\text{term}_2 + \dots$$

### Rosetta energy terms (Pset 3 Q3)

| Rosetta Full-atom Scoring Functions | | |
| :--- | :--- | :--- |
| Van der Waals net attractive energy | FA | fa_atr |
| Van der Waals net repulsive energy | FA | fa_rep |
| Hydrogen bonds, short and long-range, (backbone) | FA/CEN | hbond_sr_bb, hbond_lr_bb |
| Hydrogen bonds, short and long-range, (side-chain) | FA | hbond_sc, hbond_bb_sc |
| Solvation (Lazaridis-Karplus) | FA | fa_sol |
| Dunbrack rotamer probability | FA | fa_dun |
| Statistical residue-residue pair potential | FA | fa_pair |
| Intra-residue repulsive Van der Waals | FA | fa_intra_rep |
| Electrostatic potential | FA | hack_elec |
| Disulfide statistical energies (S-S distance, etc.) | FA | dslf_ss_dst, dslf_cs_ang, dslf_ss_dih, dslf_ca_dih |
| Amino acid reference energy (chemical potential) | FA/CEN | ref |
| Statistical backbone torsion potential | FA/CEN | rama |
| Van der Waals "bumps" | CEN | vdw |
| Statistical environment potential | CEN | env |
| Statistical residue-residue pair potential (centroid) | CEN | pair |
| Cb | | cbeta |

---

## Methods for Refining Structures

- Once we have a starting structures, how can we refine it? Lower potential energy by:
  - Changing protein backbone phi/psi angles
  - Side-chain "packing" of amino acid R groups
- 3 approaches to refine structures:
  - 1. Energy Minimization
  - 2. Molecular Dynamics
  - 3. Simulated Annealing

---

## 1. Energy Minimization

- Deterministic process of going downward on potential energy surface
- Perform gradient (multidimensional analog of derivative) descent along potential energy surface
- Downward on potential energy surface is going in the direction of the force field since
$$F(\vec{x}) = -\nabla U(\vec{x})$$
for atomic positions $\vec{x}$
- Local search since you only go immediately downward to local minimum, which may or may not be global minimum

Courtesy of the National Academy of Sciences. Used with permission.
Source: Summa, Christopher M., and Michael Levitt. "Near-native Structure Refinement using in Vacuo Energy Minimization." *Proceedings of the National Academy of Sciences* 104, no. 9 (2007): 3177-82.

http://www.pnas.org/content/104/9/3177

---

## 2. Molecular Dynamics

- Calculate force field between all atoms in protein and surrounding environment (solvent, lipid bilayer, etc.)
- From force field, can calculate velocity, and use this to update positions over very small timescale ($t_i - t_{i-1} \sim\text{femtoseconds}$):

$$x(t_i) = x(t_{i-1}) + v(t_{i-1}) \times (t_i - t_{i-1})$$

$$v(t_i) = v(t_{i-1}) - \frac{\nabla U(t_{i-1})}{m} \times (t_i - t_{i-1})$$

- Then recalculate force field based on new atomic positions, repeat...
- Very computationally expensive since pairwise interactions between thousands of atoms at each timestep $\times$ billions or more timesteps

Courtesy of Elmar Krieger, Yasara. Used with permission.

http://www.yasara.org/dhfr.gif

---

## 3. Simulated Annealing

- Stochastic search of protein conformations
- Metropolis-Hastings algorithm is an implementation of Simulating Annealing that generates sample states of a thermodynamic system
  - Monte-Carlo method (as was Gibbs Sampler)
- Idea: Sample a new conformation by perturbing protein's current structure
  - If lower energy, accept new conformation
  - If higher energy, accept it with probability proportional to difference in energy between two structures
    - Unlike Energy Minimization, it is possible to move upward on the potential energy surface, which may allow us to escape a local minimum and find the global minimum

---

## 3. Simulated Annealing

- Name and idea come from **metallurgy**
  - **High temperature** – **more molecular movement**
    - Metropolis-Hastings algorithm for protein folding: more sampling of protein conformations / movement along the potential energy surface
    - High probability of jumping from local minimum to another region of the potential energy surface
  - **Lower temperature** – **less molecular movement**
    - Low probability of escaping current local minimum – used for for small refinements of protein structure
  - **Annealing schedule** specifies how temperature changes from high to low over time

---

## 3. Simulated Annealing

- Example searching for maximum instead of minimum:

Temperature: 25.0

Courtesy of Kingpin13. Image in the public domain.

http://en.wikipedia.org/wiki/File:Hill_Climbing_with_Simulated_Annealing.gif#file

---

## 3. Simulated Annealing

- Metropolis-Hastings acceptance criterion:
  - If test conformation has lower energy, always accept it
  - If test conformation has higher energy, accept it with probability:

$$\frac{P(S_{\text{test}})}{P(S_{\text{current}})} = \frac{\left(e^{-E_{\text{test}}/kT}\right)/Z(T)}{\left(e^{-E_{\text{current}}/kT}\right)/Z(T)} = e^{-(E_{\text{test}} - E_{\text{current}})/kT}$$

Probability of each conformation follows Boltzmann distribution
$Z(T)$ is a normalization constant that cancels
$k$ is Boltzmann constant; can refer to $kT$ as "temperature"

- At higher temperature, exponent is closer to 0 so acceptance probability is closer to 1 (more likely to accept higher energy conformational changes)

---

## Structure discovery using homology

- In determining a structure, if regions of your query protein are homologous (evolutionarily related) to other proteins of known structure, they likely adopt the homologous structure/fold
- Align your query protein to those in the PDB:
  - High (50%+) sequence similarity
  - Medium (20%-50%) sequence similarity
  - Low (<20%) sequence similarity

---

## Structure discovery using homology

- In determining a structure, if regions of your query protein are homologous (evolutionarily related) to other proteins of known structure, they likely adopt the homologous structure/fold
- Align your query protein to those in the PDB:
  - High (50%+) sequence similarity
    - Can be confident the structures are very similar – generally only need to refine regions where alignment is poor.
  - Medium (20%-50%) sequence similarity
  - Low (<20%) sequence similarity

---

## Structure discovery using homology

- In determining a structure, if regions of your query protein are homologous (evolutionarily related) to other proteins of known structure, they likely adopt the homologous structure/fold
- Align your query protein to those in the PDB:
  - Medium (20%-50%) sequence similarity
    - Try several alignments, and refine structure resulting from each. Choose the final based on lowest energy.

---

## Structure discovery using homology

- In determining a structure, if regions of your query protein are homologous (evolutionarily related) to other proteins of known structure, they likely adopt the homologous structure/fold
- Align your query protein to those in the PDB:
  - Low (<20%) sequence similarity
    - Lots of possible starting structures from different alignments. Need to do more aggressive refinement since final structure may be significantly different than starting structure; choose final structure based on lowest energy.

---

## Structure discovery without homology

$$\left.
\begin{aligned}
&\text{• Monte Carlo search of backbone phi/psi angles} \\
&\quad\text{– Choose small region of 3-9 a.a.s and set angles to those of} \\
&\quad\quad\text{similar peptide in PDB} \\
&\quad\text{– Calculate energy of structure with new angles of the 3-9 a.a.s} \\
&\quad\text{– Accept according to Metropolis criterion} \\
&\text{• Repeat this 36,000 times to get 1 final structure}
\end{aligned}
\right\} \quad \text{Repeat 20,000 times to get 20,000 structures}$$

- Cluster the many structures into small number of representative groups; more sophisticated refinement of groups

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802 / 6.874 / HST.506 Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Recitation 4-2](01-recitation-4-2.md) · [Up: contents](index.md)
