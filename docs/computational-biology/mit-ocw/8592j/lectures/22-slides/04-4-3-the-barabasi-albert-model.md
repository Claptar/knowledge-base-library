---
title: 4.3 The Barabasi-Albert model
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/22-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.3 The Barabasi-Albert model

**Source:** `lectures/22-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

While examining a variety of networks, initially in the context of internet, Barabasi and Albert obtained degree distributions that were quite different from Poisson. Rather than the exponential behavior of Eq. (4.11) they observed a tendency for distributions to fall more slowly for large k, approximately as a power law 1/k<sup>3</sup> . To explain this observation, they noted that networks such as internet are obtained through a dynamic growth process, with new nodes added to a pre-existing network. They postulated that newly added nodes are more likely to link to popular pre-existing nodes, the latter thus becoming even more popular (the rich become richer) over time.

Consider an algorithm in which nodes are added to the network one at a time. Each new node makes exactly m links, but the probability that a link is made to a pre-existing node is proportional to the number of links already emanating from that node. Starting with no nodes or links, after t steps, the network will have N(t) = t nodes, and L(t) = mt links. A particular realization of this algorithm can be described by the set {Nk(t)} of the number of nodes with k links. After the next node is added, these numbers change, such that


The rule for preferential attachment states that the probability of attachment to a site with k links is k/(<sup>�</sup> k<sup>′ k′Nk′).Sincetherearemnewlinkstobeadded,Eq.(4.12)impliesthat</sup> on average


74

For large t, we hypothesize that the system evolves towards fixed probabilities pk for finding nodes with k edges, such that


Substituting Eq. (4.14) into Eq. (4.13), and noting that<sup>�</sup> k<sup>′ k′Nk′(t) = L(t) = 2mt,gives</sup>


We see that terms involving t cancel out, justifying our assumption of a steady state, and yielding a recursion relation for the probabilities, as


For k > m, successive recursions give


For k = m, the addition to probability is not from pk−1 but from the new nodes, and thus


We thus find the final distribution


which is properly normalized as<sup>�</sup> k<sup>pk=1.Thek≫1thetailofthisdistributionindeed</sup> decays as k<sup>−3</sup> , as empirically observed for the internet and a number of other cases.

75

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 4.2 The random graph](03-4-2-the-random-graph.md) · [Up: contents](index.md)
