---
title: 04 questions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 04 questions

**Source:** `psets/04-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

8.592J–HST.452J: Statistical Physics in Biology

Assignment # 4

Coulomb Interactions

1. Flory Theory: The Coulomb energy of a ball of charge Q and dimension R in d spacial dimensions scales as


The proportionality coefficient depends on the exact shape and charge distribution; details that are not relevant to our intended scaling analysis.

(a) For a charged polymer of length N, estimate the dependence of R on Q and N, by balancing the above Coulomb energy with the entropy associated with confining the polymer to a size R. (Follow the Flory reasoning for self-avoiding polymers.)

(b) For a polyelectrolyte in which Q ∝ N, find the Flory exponent νF in the scaling relation R ∝ N<sup>νF</sup> . Identify the upper critical dimension du above which ν = 1/2 (the Coulomb interaction is irrelevant), and the lower critical dimension du<sup>Fbelow whichνF= 1 (the</sup> polymer is fully stretched).

(c) Unlike in the case of self-avoiding polymers, the Flory estimate is a rather poor description for charged polymers. In fact, it can be shown that the exact value of the swelling exponent for uniformly changed polymers is ν = 2/(d−2). Identify the correct upper and lower critical dimensions from this formula. Note that a uniformly charged polymer in three dimensions is fully stretched.

(d) A polyampholyte is a heteropolymer with charged monomers of both signs. If the charges are randomly and independently chosen to be positive or negative, we expect Q<sup>2</sup> ∝ N. What is the Flory estimate of the swelling exponent in this case?

*****

2. The Manning Transition: When ionic polymers (polyelectrolytes) such as DNA are immersed in water, the smaller charged counter-ions go into solution, leaving behind an oppositely charged polymer. Because of the electrostatic repulsion of the charges left behind, the polymer is stretched, and shall be modeled as a cylinder of radius a, as depicted in the figure. While thermal fluctuations tend to make the ions wander about in the solvent, electrostatic attractions favor their return and condensation on the polymer. The potential due to a uniform linear charge density is logarithmic, and assuming that the counterions have valence z (chrage ze), their potential energy is given by


Here, n is the linear density and ri is the radial coordinate of the i<sup>th</sup> particle. Note that the Coulomb repulsions between the counter-ions have been left out.

1


<!-- Start of picture text -->
R 2a<br>-<br>-<br>z+<br>- z+<br>h<br>z+<br>- r L<br>-<br>z+ -<br>- z+<br>-<br><!-- End of picture text -->

(a) For a cylindrical container of radius R, show that at a temperature T , the canonical partition function Z has the form


and give the value of ζ.

(b) Calculate the probability distribution function p (r) for the radial position of a counterion, and its first moment (r), the average radial position of a counter-ion.

(c) The behavior of the results calculated above in the limit of R ≫ a is very different at high and low temperatures. Identify the transition temperature, and characterize the nature of the two phases. In particular, how does (r) depend on R and a in each case?

(d) Calculate the pressure exerted by the counter-ions on the wall of the container, in the limit R ≫ a, at all temperatures.

(e) According to Manning, at low temperatures just enough counterions reattach to the polymer to reduce its charge density such that the value of ζ stays at 1. Along a fully ionized double stranded DNA, unit (negative) charges occur at a separation of b = 1.7A<sup>˚</sup> . Use the Manning reasoning to calculate the fraction of this charge that is neutralized by salt counterions in solutions of either Na Cl or Mg Cl2. (The Bjerrum length in water is ℓB = e<sup>2</sup> /(ǫkBT ) ≈ 7<sup>˚</sup> A.)

*****

3. Packaging DNA in a phage: After an infected bacterium has duplicated the DNA and coat of an infecting phage, a new phage is assembled with the aid of protein motors. In the case of bacteriophage φ29, a 20,000 base pair dsDNA has to be packaged in a capsid, which is a cylinder of radius r = 42nm and height h = 47nm. Inside the capsid the DNA is arranged like a spool, first winding in a helical shell next to the wall, and then forming successively tighter shells moving inwards. A typical separation between strands in this

2

structure is 2.3nm. Single molecule experiments have shown that the work required to pack the DNA in the capsid is approximately 10<sup>5</sup> kBT at room temperature (T = 300<sup>o</sup> K). In the following, use order of magnitude estimates to determine what sets this energy scale.

(a) Estimate the entropy of the DNA in solution, using a persistence length of ℓP ≈ 50nm. Can the loss of this entropic free energy account for the work of packaging?

(b) Estimate the energy cost of bending DNA into the helical form found in the capsid. (Express the rigidity parameter κ in terms of the persistence length ℓP .) Is bending energy a significant fraction of the overall work of packaging?

(c) Estimate the electrostatic energy of DNA in the capsid: Assume unit charges along the DNA at a spacing of b ≈ 0.17nm, which interact through a Debye–Hu¨ckel potential of screening length λ ≈ 1nm, with charges on nearby strands (separations of around 2nm). Can electrostatic energies account for the work of packaging?

Here are a couple of articles on the packaging of DNA in a phage: P. K. Purohit, M. M. Inamdar, P. D. Grayson, T. M. Squires, J. Kondev, and R. Phillips, Forces during Bac­ teriophage DNA Packaging and Ejection- Biophys. J., February1, 2005; 88(2): 851 - 866. (http://www.biophysj.org/cgi/reprint/88/2/851); and S. Tzlil, J. T. Kindt, W. M. Gelbart, and A. Ben-Shaul, Forces and Pressures in DNA Packaging and Release from Viral CapsidsBiophys. J., March1,2003; 84(3): 1616 - 1627. (http://www.biophysj.org/cgi/reprint/84/3/1616). *****

4. Charged membranes: In class, we solved the Poisson–Boltzmann for a flat membrane of uniform charge density σ, with a neutralizing background of counterions of charge e. (a) Extend the solution to counterions of charge ze, and compute their density at a distance y from the membrane.

(b) There is an overall constant of proportionality that can be fixed by examining the electric field at the charge surface. Plot the electric field as a function of y.

(c) Check the overall neutrality of the system by integrating over the density of counterions.

(d) Calculate the self-consistent potential and charge density between two uniformly charged plates. (Each plate has uniform charge density σ, the neutralizing counterions have charge ze, and the plates are separated by L.)

(Optional) (e) Solve the Poisson–Bolzmann equation around a cylinder of radius a and charge density n = e/b. (Hint: By changing variables to x = ln(r/a) and ψ = βzeφ −2x, you should be able to reduce the two dimensional problem to the already solved one dimensional case.) Can you make connections to the results in problem 2 on Manning condensation?

*****

5. Bending a charged polymer: As indicated in the figure below, bending a polymer reduces the distances between its monomers.

(a) For two monomers which are at a distance dmn = b|m − n| when the polymer is straight, compute the change δdmn(R), when the polymer is bend into a circle of radius R ≫ dmn.

3


(b) Assume that unit charges at each monomer interact through the Debye potential


where ℓB and λ and the Bjerrum and screening lengths, respectively. Compute the change in this pairwise energy if the distance is changed from d to d + δd.

(c) Show that bending increases the energy of the charged polymer by an amount propor­ tional to L/R<sup>2</sup> , where L = Nb is the total length of the polymer.

(d) The overall bending parameter for a charged polymer can be written as κ = κb+κe, where κb is the cost of deforming the backbone, while κe comes from the additional electrostatic energy. Compute κe using the model explored in the previous parts.

(e) Is electrostatic energy a significant component of the cost of bending double stranded DNA? (For DNA in water, b ≈ .17nm, ℓB ≈ .7nm, λ ≈ 1nm, and ℓP ≈ 50nm. What about single-stranded DNA or RNA?)


Suggested reading: Chapter 7 of Biological Physics by Philip Nelson.

4

MIT OpenCourseWare http://ocw.mit.edu

8.592J / HST.452J Statistical Physics in Biology Spring 2011

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
