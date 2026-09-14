---
title: 2.1.1 Charge dissociation in solution
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.1.1 Charge dissociation in solution

**Source:** `lectures/09-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Entropy is indeed the reason why many molecules (electrolytes) dissociate and ionize in solution. The opposing charges making up an ion clearly minimize the Coulomb energy by being in close proximity in a bound (molecular) state. The loss of this electrostatic energy in the dissociated (ionized) state is balanced by the gain in configurational entropy. We can quantify this by an approximate evaluation of the change in free energy upon dissociation, as


Here, Eb is the binding energy, T is the temperature, kB is the Boltzmann constant, and v0 is some characteristic volume. The gain in entropy is estimated from the number of positions available for each of N particles in the volume V . In a more systematic evaluation of the partition function, v0 = λ<sup>3</sup> , where λ is the “thermal wavelength”. Setting the free energy change to zero, gives the equilibrium concentration


The electrostaic contribution to the binding energy, Ec, can be computed from Coulomb’s law, as


27

where ǫ denotes the dielectric constant of water, z is the valence, and e is the electron charge. The physically significant quantity is the ratio of this energy to the thermal energy kBT , which can be expressed as


where we have defined the Bjerrum length


For water, ǫ ≈ 81, and the Bjerrum length is about 7.1<sup>˚</sup> A. Very roughly, we can say that at separations larger than lB, the Coulomb interaction between unit charges in water is insignificant compared to thermal energy.


We can also think of dissociation as the chemical reaction


(The dissociated positive charge is called a cation, the negative one an anion.) The equilibrium constant of the reaction


is a measure of the ease with which ionization occurs. For strong electrolytes, such as Na<sup>+</sup> Cl<sup>−</sup> (salt), Na<sup>+</sup> OH (base) and H<sup>+</sup> Cl (acid), which dissociate almost totally, the net binding energy is small. Weaker electrolytes are more strongly bound and dissociate less readily. Water itself can dissociate into H<sup>+</sup> and OH<sup>−</sup> ions, but at room temperature this process only produces about 10<sup>−7</sup> hydrogen ions per mole.

28

Biological molecules also dissociate, and the ‘charge environment’ of a cell is quite complicated. The lipids forming the cell membrane become negatively charged upon dissociation, as does DNA. The latter is an acid that releases H<sup>+</sup> ions, leaving behind a negatively charged backbone. Proteins can also release H<sup>+</sup> ions, but some of the amino-acid side groups are actually basic, releasing OH<sup>−</sup> . A molecule of this sort, which can develop regions both of positive and of negative charge upon dissociation, is called a polyampholyte. Molecules like the DNA backbone, which carry a uniform charge, are known as polyelectrolytes. Together, both sorts of macromolecules are referred to as macroions, and the small charged particles they give up into the cytoplasm are called counterions. The electrostatic interactions between the macromolecules are very important for their biological function– the repulsive forces prevent aggregation, while attractions are important for docking and recognition. However, calculating these interactions in the environment of the moving counterions is not an easy task.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2.1.2 The Poisson–Boltzmann Equation →](03-2-1-2-the-poisson-boltzmann-equation.md)
