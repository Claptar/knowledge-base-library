---
title: Energy of Metropolis Algorithm, kT=53782
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Energy of Metropolis Algorithm, kT=53782

**Source:** `psets/04-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
350000<br>300000<br>250000<br>200000<br>150000<br>100000<br>50000<br>0<br>0 5000 10000 15000 20000<br>Iteration<br>Energy<br><!-- End of picture text -->

**(D – 2 points)** Finally, let’s implement an annealing schedule to make the Simulated Annealing algorithm more realistic:

1. Start at the temperature calculated in part (B).

2. Perform 100*number_of_residues iterations with this kT.

3. Cut kT in half. Repeat step 2.

4. Continue halving until kT is less than 1. You should perform

100*number_of_residues iterations for the first kT value less than 1, and then stop.

Using the temperature calculated in part (B), how many kT halvings should you perform?

- 16 (53,782/2<sup>16</sup> �O.82)

In the code, change number_of_kT_halvings = 1 to this value. Then complete the part_d() function to implement the above annealing schedule (see the code for more specific details). If your implementation is correct,

energy_plot_metropolis_part_d.pdf will be produced, showing the energy of the structure at each of the 100*number_of_residues*(number_of_kT_halvings+1) iterations with the kT at the end of each iteration set labeled on the x-axis. Upload this plot to the Stellar dropbox or include a printout of it with your writeup. In no more than two sentences, compare/contrast this Simulated Annealing plot with the Energy Minimization plot from part (A). (Note: performing the algorithm with the computed number_of_kT_halvings could take up to an hour, so it’s recommended that you test your code with

12

number_of_kT_halvings=1 first to make sure there are no errors, and then change number_of_kT_halvings to your calculated value to run the Simulated Annealing to completion).


<!-- Start of picture text -->
Energy of Metropolis Algorithm, initial kT=53782; 16 halvings of kT<br>300000<br>250000<br>200000<br>150000<br>100000<br>50000<br>0<br>82.091.045.522.861.4 80.740.320.2 10.1 05.052.526.313.1 6.6 3.3 1.6 0.8<br>537 268 134 67 33 16 8 4 2 1<br>Energy<br><!-- End of picture text -->

The Energy Minimization algorithm from part (A) is deterministic, constantly lowering the energy and requiring fewer iterations since a change in the structure is always performed at each iteration. The Simulated Annealing algorithm from part (D) is stochastic and sometimes moves to higher energy states, requiring more iterations since many conformations are sampled but only a small percentage are accepted by the Metropolis criterion.

13

**(E – 1 point)** Finally, let’s evaluate the structures you’ve produced using two criteria: (1) a simple count of the number of phi and psi angles that differ by more than 1 degree.

(2) the root-mean-square deviation (RMSD).

To calculate (1), you should complete the part_e_num_angles_different() function. A PyRosetta function can be called to easily calculate (2) (hint: see the Appendix of the linked PyRosetta Documentation).

Then fill out the table below. Which approach (Energy Minimization or Simulated Annealing) appears to have done better here? Can you think of a scenario in which the other approach would do better?

|Differe|nce between1EK8.clean.pd<br>Number of phi and psi<br>angles that differ by>1°|b and:<br>RMSD|
|---|---|---|
|`1EK8.rotated.pdb`|4|5.39|
|Energy Minimization<br>structurefrompart(A)|22|3.04|
|Simulated Annealing<br>structure from part (D)|361 (will vary since<br>Simulated Annealing is<br>stochastic)|36.23 (will vary)|


It appears that Energy Minimization resulted in a structure that is closer to 1EK8.clean.pdb as measured by both the number of angles that differ by >1° as well as the RMSD. Since only 4 phi/psi angles were rotated in the 1EK8.rotated.pdb structure (and these were only off by 10° each), it’s not surprising that the deterministic energy minimization approach did well because the nearest local minimum found by Energy Minimization is similar to the original 1EK8.clean.pdb structure. In contrast, the Simulated Annealing approach perturbed almost all angles during random sampling, even most of the angles which were not initially different between 1EK8.rotated.pdb and 1EK8.clean.pdb.

The Simulated Annealing approach would perform better than Energy Minimization when there is a large conformational change with an energy barrier between the starting structure and the globally lowest energy structure. In Energy Minimization, this barrier could not be surmounted since only downward moves on the energy surface are made and the algorithm would return a locally optimal structure that didn’t make the large conformational change to get to the globally lowest energy structure. In contrast, it’s possible that the random sampling in Simulated Annealing could sample something close to the globally lowest energy structure and/or temporarily move to structures with higher energy on the path to overcome the barrier and eventually settle in the globally lowest energy structure.

14

---

[← P2 – Refining Protein Structures in PyRosetta (7 points)](06-p2-refining-protein-structures-in-pyrosetta-7-points.md) · [Up: contents](index.md) · [P3. Mutual information of protein residues (7 points). →](08-p3-mutual-information-of-protein-residues-7-points.md)
