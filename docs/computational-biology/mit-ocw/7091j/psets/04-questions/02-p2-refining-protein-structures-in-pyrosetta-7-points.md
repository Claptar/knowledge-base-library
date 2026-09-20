---
title: P2 – Refining Protein Structures in PyRosetta (7 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/04-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# P2 – Refining Protein Structures in PyRosetta (7 points)

In this problem, you will explore refining protein structures using two methods discussed in class: Energy Minimization and Simulated Annealing. To do this, we will use PyRosetta, an interactive Python-based interface to the powerful Rosetta molecular modeling suite.

When implementing your solutions in the skeleton code provided, we encourage you to look at the solutions from Problem Set 3 Question 3 as well as the PyRosetta documentation: http://graylab.jhu.edu/~sid/pyrosetta/downloads/documentation/PyRosetta_Manual.pdf, particularly Units 2 (Protein Structure in PyRosetta) and 3 (Calculating Energies in PyRosetta), and the Appendix.

In the following, we will provide instructions on how to complete this problem on Athena's Dialup Service, where PyRosetta has previously been installed as a module for another class.

Log onto Athena's Dialup Service, either at a workstation on campus or from a Terminal on your personal machine:

```text
ssh <your Kerberos username>@athena.dialup.mit.edu
```

Once logged on, load the PyRosetta module with the following 2 commands:

```text
cd /afs/athena/course/20/20.320/PyRosetta
source SetPyRosettaEnvironment.sh
```

If you log onto Athena to complete the problem at a future time, you will have to execute these two commands again, otherwise you will get the following error:

```text
ImportError: No module named rosetta
```

Now, head to the course's Athena directory, copy the `pyRosetta_RefiningStructures.zip` folder of files for this problem to your home directory (`~`), and then unzip it in your home directory with the following commands:

```text
cd /afs/athena/course/7/7.91/sp_2014
cp pyRosetta_RefiningStructures.zip ~
cd ~
unzip pyRosetta_RefiningStructures.zip
cd pyRosetta_RefiningStructures
```

---

You should now be able to edit any of these files. Skeleton code is provided in `pyRosetta_1EK8.py`. The `1EK8.clean.pdb` file is a cleaned PDB file of the *E. coli* ribosome recycling factor, while `1EK8.rotated.pdb` is the same structure but with some phi and/or psi angles rotated. In this problem, you will refine the `1EK8.rotated.pdb` structure using an Energy Minimization approach as well as a Simulated Annealing approach.

**(A – 1 point)** Complete the `part_a_energy_minimization()` function in `pyRosetta_1EK8.py` to carry out a simple greedy energy minimization algorithm. Rather than computing the gradient of the full energy potential, you should simply calculate the energy of the structure for each of the residue's phi and psi angles changed by $\pm 1$ degree, and accept the structure with the lowest energy, continuing until the change in energy is less than 1 (see the code for more specific details).

What are the starting and final energies of the structure? How many iterations until convergence? If implemented correctly, a plot of the energy at each iteration (`energy_minimization_plot.pdf`) will be made; upload it to the Stellar electronic dropbox or include a printout of it with your write-up. Once finished with this, to cut down on run-time for subsequent parts of the question you may want to comment out the lines between `###### PART (A) ########` and `###### END PART (A) ########`.

The starting energy is 37,278.5, and after 61 iterations the final energy is 188.9.

---

**(B – 1 point)** Now we'll refine `1EK8.rotated.pdb` through a Simulated Annealing approach. For the initial iterations, we aim for an acceptance criterion of 50% for structures that have twice the starting energy of `1EK8.rotated.pdb`. What should we initially set $kT$ (henceforth simply referred to as the temperature since $k$, the Boltzmann constant, remains the same) to be to achieve this acceptance rate?

The energy of `1EK8.rotated.pdb` is initially $E_i = 37,278.5$, so an acceptance rate of 50% corresponds to:
$$0.5 = e^{-(2E_i - E_i)/kT} \Rightarrow -\ln(0.5) = E_i/kT \Rightarrow kT = -E_i/\ln(0.5) \approx 53,782.$$

**(C – 2 points)** Now let's implement the core of the Simulating Annealing algorithm: making a number of possible changes to the structure and accepting each according to the Metropolis criterion. To do this, fill in `onesetofMetropolismoves()`, a function that is called by `part_c()`; your implementation of `onesetofMetropolismoves()` should repeatedly call `make_backbone_change_metropolis()`, which you should implement to make one phi or psi angle perturbation drawn from a Normal(0, 20) distribution and accept or reject it according to the Metropolis criterion (see the code for more specific details).

Finally, change `kT_from_part_B = 1` at the bottom of the code to your answer from part (B). If your implementation of the functions called by `part_c()` is correct, `energy_plot_metropolis.pdf` will be produced, showing the energy of the structure at each of the `100*number_of_residues` iterations with your `kT_from_part_B`. Upload it to the Stellar dropbox or include a printout of it with your writeup.

---

**(D – 2 points)** Finally, let's implement an annealing schedule to make the Simulated Annealing algorithm more realistic:
1. Start at the temperature calculated in part (B).
2. Perform `100*number_of_residues` iterations with this $kT$.
3. Cut $kT$ in half. Repeat step 2.
4. Continue halving until $kT$ is less than 1. You should perform `100*number_of_residues` iterations for the first $kT$ value less than 1, and then stop.

Using the temperature calculated in part (B), how many $kT$ halvings should you perform?

16 $(53,782/2^{16} \approx 0.82)$

In the code, change `number_of_kT_halvings = 1` to this value. Then complete the `part_d()` function to implement the above annealing schedule (see the code for more specific details). If your implementation is correct, `energy_plot_metropolis_part_d.pdf` will be produced, showing the energy of the structure at each of the `100*number_of_residues*(number_of_kT_halvings+1)` iterations with the $kT$ at the end of each iteration set labeled on the x-axis. Upload this plot to the Stellar dropbox or include a printout of it with your writeup. In no more than two sentences, compare/contrast this Simulated Annealing plot with the Energy Minimization plot from part (A). (Note: performing the algorithm with the computed `number_of_kT_halvings` could take up to an hour, so it's recommended that you test your code with

---

`number_of_kT_halvings=1` first to make sure there are no errors, and then change `number_of_kT_halvings` to your calculated value to run the Simulated Annealing to completion).

The Energy Minimization algorithm from part (A) is deterministic, constantly lowering the energy and requiring fewer iterations since a change in the structure is always performed at each iteration. The Simulated Annealing algorithm from part (D) is stochastic and sometimes moves to higher energy states, requiring more iterations since many conformations are sampled but only a small percentage are accepted by the Metropolis criterion.

---

**(E – 1 point)** Finally, let's evaluate the structures you've produced using two criteria:
(1) a simple count of the number of phi and psi angles that differ by more than 1 degree.
(2) the root-mean-square deviation (RMSD).
To calculate (1), you should complete the `part_e_num_angles_different()` function. A PyRosetta function can be called to easily calculate (2) (hint: see the Appendix of the linked PyRosetta Documentation).

Then fill out the table below. Which approach (Energy Minimization or Simulated Annealing) appears to have done better here? Can you think of a scenario in which the other approach would do better?

| Difference between `1EK8.clean.pdb` and: | Number of phi and psi angles that differ by >1° | RMSD |
| :--- | :--- | :--- |
| `1EK8.rotated.pdb` | 4 | 5.39 |
| Energy Minimization structure from part (A) | 22 | 3.04 |
| Simulated Annealing structure from part (D) | 361 (will vary since Simulated Annealing is stochastic) | 36.23 (will vary) |

It appears that Energy Minimization resulted in a structure that is closer to `1EK8.clean.pdb` as measured by both the number of angles that differ by >1° as well as the RMSD. Since only 4 phi/psi angles were rotated in the `1EK8.rotated.pdb` structure (and these were only off by 10° each), it's not surprising that the deterministic energy minimization approach did well because the nearest local minimum found by Energy Minimization is similar to the original `1EK8.clean.pdb` structure. In contrast, the Simulated Annealing approach perturbed almost all angles during random sampling, even most of the angles which were not initially different between `1EK8.rotated.pdb` and `1EK8.clean.pdb`.

The Simulated Annealing approach would perform better than Energy Minimization when there is a large conformational change with an energy barrier between the starting structure and the globally lowest energy structure. In Energy Minimization, this barrier could not be surmounted since only downward moves on the energy surface are made and the algorithm would return a locally optimal structure that didn't make the large conformational change to get to the globally lowest energy structure. In contrast, it's possible that the random sampling in Simulated Annealing could sample something close to the globally lowest energy structure and/or temporarily move to structures with higher energy on the path to overcome the barrier and eventually settle in the globally lowest energy structure.

---

---

[← P1 - Bayesian Networks (7 points)](01-p1---bayesian-networks-7-points.md) · [Up: contents](index.md) · [P3. Mutual information of protein residues (7 points). →](03-p3-mutual-information-of-protein-residues-7-points.md)
