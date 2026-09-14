---
title: 2.3.4 The Random Energy Model (REM) for compact heteropolymers
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.3.4 The Random Energy Model (REM) for compact heteropolymers

**Source:** `lectures/11-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Deep in the globular phase, the states of the compact polymer can be visualized as the collection of all maximally compact configurations. In a lattice version, these are self-avoiding walks that visit all sites, leaving no empty ones, and are referred to as Hamiltonian walks. The number of Hamiltonian walks also grows exponentially with the number of steps as g<sup>′N</sup> , but is much smaller than the number of self-avoiding walks (g<sup>N</sup> ≫ g<sup>′N</sup> ). For a homopolymer all such configurations are equally likely, but in a heteropolymer the distinct interactions between different monomers leads to variations in energy. Presumably at low temperatures the lower energy states are preferred, and there can potentially be a phase transition to a specific (ground state) configuration. For biological molecules, there are non-specific attractive forces that tend to aggregate all monomers, whereas specific interactions select a particular (native) shape amongst the manifold of possible compact states.


To explore this scenario, consider all compact configurations for a multi-component heteropolymer such as a protein. The energy of a configuration α is given by


where the sum is over all non-polymeric nearest-neighbor pairs ⟨ab⟩, and Vab is the interaction energy assigned to a neighboring pair of monomers a and b. The partition function is obtained by the sum


over the g<sup>′N</sup> states. To make headway with this hard problem, we make the drastic approximation of assuming that the bond energies Vab are independent random variables. Subject to this assumption, the energies Eα are themselves random variables, and as long as the number of terms NB in Eq. (2.58) is large, taken from a Gaussian distribution. The mean and variance of the distribution are given by


where noting that NB = (z − 1)N (of the z per each site of the lattice, one is polymeric), we have folded the proportionality constant into the definitions of ε0 and σ<sup>2</sup> .

44

For large N, the probability distribution for the energy will take the Gaussian form


Since the total number of states is g<sup>′N</sup> , the density of states is Ω(E) = g<sup>′N</sup> p(E), and the entropy of this random energy model (REM) is given by


The last term is not extensive (proportional to N) and can be safely ignored.


According to Eq. (2.62), S(E) is shaped like a parabola, but thermodynamic constraints imply that only a certain portion of this curve is physical. First, the temperature T is obtained from the slope of the curve via T<sup>−1</sup> = dS/dE. Positive temperatures require the entropy to increase with temperature, and thus only the states with E < Nε0 are physically accessible. Second, the entropy cannot be negative, and S(E) should thus stick to zero for E < Ec, where Ec is easily obtained as


(Note the connection to the extreme value problem studied earlier: Ec is also the mean value of the lowest of g<sup>′N</sup> energies randomly selected from p(E).) The singularity of entropy at Ec signifies a phase transition into a glassy state, at a temperature Tc given by


There are presumably a few low energy states with energy close to Ec, and the system freezes into one of these for T ≤ Tc.

45

---

[← 2.3.3 Compact (globular) polymers in bad solvents](02-2-3-3-compact-globular-polymers-in-bad-solvents.md) · [Up: contents](index.md) · [2.3.5 Designed REM for protein folding →](04-2-3-5-designed-rem-for-protein-folding.md)
