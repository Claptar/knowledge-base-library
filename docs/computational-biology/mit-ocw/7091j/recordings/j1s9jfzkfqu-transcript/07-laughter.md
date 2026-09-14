---
title: '[LAUGHTER]'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/j1s9jfzkfqu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [LAUGHTER]

**Source:** `recordings/j1s9jfzkfqu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: But even so, give them that. Give them their credit. It's a remarkably good agreement.**

**Now, we've looked at cases where there's very high sequence similarity, where there's medium sequence similarity, where there's low sequence similarity. But the**

18

**hardest category are ones where there's actually nothing in the structural database that's a detectable homologue to the protein of interest.**

**So how do you go about doing that? That's the de novo case. So in that case, they take the following strategy. They do a Monte Carlo search for backbone angles. So specifically, they take short regions-- and again, this is the exact length. Changes in different versions of the algorithm, but it's either three to nine amino acids in the backbone.**

**They find similar peptides in the database of known structure. They take the backbone confirmations from the database. They set the angles to match those. And then, they use those Metropolis criteria that we looked at in simulated annealing. Right? The relative probability of the states, determined by the Boltzmann energy, to decide whether to accept or not.**

**If it's lower energy, what happens? Do you accept? Do you not accept?**

**AUDIENCE: Accept.**

**PROFESSOR: You accept. And if it's high energy, how do you decide?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: [INAUDIBLE], probability. Very good.**

**OK, so they do a fixed number of Monte Carlo steps-- 36,000. And then they repeat this entire process to get 2,000 final structures. OK? Because they really have very, very low confidence in any individual one of these structures.**

**OK, now you've got 2,000 structures, but you're allowed to submit one. So what do you do? So they cluster them to try to see whether there are common patterns that emerge, and then they refine the clusters and they submit each cluster as a potential solution to this problem.**

**OK, questions on the Rosetta approach? Yes.**

19

---

[← Question, yes.](06-question-yes.md) · [Up: contents](index.md) · [AUDIENCE →](08-audience.md)
