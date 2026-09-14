---
title: II Equilibrium binding and cooperativity
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l2-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# II Equilibrium binding and cooperativity

**Source:** `recordings/l2-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the previous Section we considered Michaelis-Menten kinetics. We found that the traditional form of the Michaelis-Menten equation [I.6] is derived by assuming a quasisteady state in which the concentration of enzyme-substrate complex is fairly constant over time. Additionally we had to assume that initially the substrate is in excess. In this Section, we first will take a step back and focus on the steady state behavior of reversible reactions and introduce the concept of multiple binding sites. Initially we will consider multiple binding sites that are independently binding substrates. However for most protein complexes the binding of substrates is not independent. For example, after binding the first substrate molecule the binding probability of the second substrate is affected. This phenomenon is called cooperativity.

In the previous section it was assumed that one substrate molecule binds to one enzyme molecule. In biological reactions however proteins often bind multiple substrates. Assume a protein has n binding sites for a substrate. Pj denotes the protein bound to j substrate molecules S. The reactions describing this process are:


where j = 1, 2, …, n.

The time-evolution of the concentration of unbound protein Po is (j=1):


where k+1 and k-1 are the forward and backward rate constants of [II.1] for j=1. The association and dissociation constants are defined as:


In steady state, d[Po]/dt = 0:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

7

To characterize all n reactions, we introduce the n association constants Kj, j = 1, 2, … ,n.


It is experimentally difficult to measure [Pj], a more convenient quantity is the average number r (0 < r < n) of substrates bound to the protein. Because there are j substrates bound to Pj, r is given by:


combining [II.5] and [II.6] gives Adair’s equation:


Note that 0 < r < n, one often uses the normalized form, called the saturation function Y = r/n (0 < Y < 1).

---

[← I Michaelis-Menten kinetics](01-i-michaelis-menten-kinetics.md) · [Up: contents](index.md) · [Identical and independent binding sites →](03-identical-and-independent-binding-sites.md)
