---
title: Identical and interacting binding sites
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l2-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Identical and interacting binding sites

**Source:** `recordings/l2-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the following discussion we will confine ourselves to two binding sites (n=2). First, let us assume that both binding sites are identical. In this case we only have to consider three states for the protein-substrate complex: no substrate bound, one substrate molecule bound, and two substrate molecules bound. The rate constants k+ and k- characterize the transitions between the unbound and single-bound state, and k<sup>*</sup> +<sup>and k*</sup> -<sup>the transitions</sup> between single-bound and double-bound states. The intrinsic association constants are defined by: K = k+/k- and K<sup>*</sup> = k<sup>*</sup> +<sup>/k*</sup> -<sup>. Analogous to [II.10] and [II.11] we find:</sup>


By using Adair’s equation [II.7] we find:


The saturation function Y = r/n is:


For K=K* we recover the hyperbolic (Michaelis-Menten like) equation [II.12]:


Let’s compare the functional forms of [II.18] and [II.19] in more detail. The difference between the two functions is:


Positive cooperativity is often defined as Y − Y > 0 , and negative cooperativity as

~ Y − Y < 0 . In other words, positive cooperativity occurs when the affinity of binding a second ligand is larger than binding the first ligand (K<sup>*</sup> > K). For negative cooperativity the binding affinity for the second ligand is smaller than for the first (K<sup>*</sup> < K).

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

10

Another, often used, definition for cooperativity is sigmoidality (from ‘S shaped’). For a sigmoidal curve the second derivative should change sign. Let’s introduce the dimensionless variables β = K<sup>*</sup> /K and x = K[S]:


The second derivative can only change sign if β > 2. Note that this definition yields a different criterion for cooperativity. According to the first definition a reaction is cooperative for β > 1, whereas according to the second definition β > 2. During the rest of the course we will use the first definition.

Now consider the limit for which intermediate states can be neglected. In this example, that would mean that single-bound states are very unlikely. The effective reaction would be:


The saturation function is now:


where K = [P2]/([Po][S]<sup>2</sup> ) is the association constant of reaction [II.22]. Note that is this case the units of K are (M)<sup>-2</sup> . This limit was first consider by Hill who proposed a graphical way to represent equations such as [II.23]. In a Hill plot one plots ln [Y/(1 − Y)] versus ln[S] . The slope of this graph is called the Hill number which is in this case equals 2. The Hill number is often used as an estimation of the number of binding sites of a protein. However one should be very careful as [II.23] involves a major assumption (no intermediate states). Let’s calculate the Hill number nH for the case [II.21] in which intermediate states are allowed:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

11

The Hill number is plotted in Fig. 3 as a function of x at different values of β. The Hill number only approaches 2 for very large  and small x. β


**Figure 3.** The Hill number as a function of the dimensionless concentration at different values of β for a protein with two identical interacting binding sites. The mathematical form is given by equation [II.24].


<!-- Start of picture text -->
k2+  S  k4+<br>k2- k4-<br>S S<br>k1+  k3+<br>k1- S  k3-<br><!-- End of picture text -->

**Figure 4** . Two independent interacting binding sites.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

12

---

[← Non-identical and independent binding sites](04-non-identical-and-independent-binding-sites.md) · [Up: contents](index.md) · [Non-identical and interacting binding sites →](06-non-identical-and-interacting-binding-sites.md)
