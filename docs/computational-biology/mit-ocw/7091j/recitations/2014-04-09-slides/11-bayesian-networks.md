---
title: Bayesian Networks
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bayesian Networks

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_P_ ( _Ro_ = 1) = 0 _._ 1 Ro Pa **Ro** _P_ ( _Pa_ = 1) = 0 _._ 3 **0 1** 0 _._ 3 **0** _P_ ( _Ti_ = 1 _|Ro, Pa_ ) = **Pa** 0 _._ 5 0 _._ 9 Co Ti 0 _._ 1 � **1 0**<sup>**Ro**</sup> **1** _P_ ( _Co_ = 1 _|Ro_ ) = ⇥0 _._ 1 0 _._ 5⇤ **0**<sup>**Co**</sup> **1** 0 _._ 8 EF _P_ ( _EF_ = 1 _|Ti, Co_ ) = **0   Ti** 0 _._ 4 0 _._ 9 **1** 0 _._ 1 � From   graph = _P_ ( _EF_ = 1 _|Ti, Co_ ) _P_ ( _Ti|Ro_ = 1 _, Pa_ = 0) _P_ ( _Co|Ro_ = 1) X structure: _T i,Co_ =1-­‐P(Ti=1   |   Ro=1,Pa=0) =1-­‐P(Co=1   |   Ro=1)

4   possible   combina'ons   of   {Ti,   Co}   to   sum   over.

For   Ti   =   0,   Co   =   0:   P(EF=1   |   Ti=0,Co=0)=0.1,   P(Ti=0   |   Ro=1,Pa=0)=0.7,   P(Co=0   |   Ro=1)=0.5 For   Ti   =   0,   Co   =   1:   P(EF=1   |   Ti=0,Co=1)=0.8,   P(Ti=0   |   Ro=1,Pa=0)=0.7,   P(Co=1   |   Ro=1)=0.5 Likewise   for   Ti   =   1,   Co   =   0   and   Ti   =   1,   Co   =   1 =   (0.1)(0.7)(0.5) +(0.8)(0.7)(0.5) +(0.4)(0.3)(0.5) +(0.9)(0.3)(0.5) = **0.51**

## Learning   Bayesian   Networks: parameters   for   given   network

- Given   a   network   structure   (ver'ces   and   edges)   and   observa'ons,   we   can learn   the   most   likely   condi'onal   probabili'es   (e.g.   we   know   a   signaling pathway   from   previous   experiments,   but   would   like   to   determine   its probabili'es   in   response   to   a   new   stress   condi'on)

   - This   is   an   inuerence   task,   in   contrast   to   the   previous   predic've   task. **Maximum Likelihood   (ML)   esKmaKon   –   based   on   observed   counts**

   - find   parameters   (condi'onal   probs.)   that   maximize   the   likelihood   of   the   data: _✓_ ˆ _ML_ = _argmaxP_ ( _Data|✓_ ) _✓_

   - – example   -­‐   given   structure   and   observed   counts   below   for   binary   vars   A   and   B, es'mate   P(A)   and   P(B|A):

   - P(A=1)   =   (4+22)/(15+3+4+22)   =   26/44   ≈   0.59

   - P(B=1|A=0)   =   3/(3+15)   ≈   0.167

   - P(B=1|A=1)   =   22/(22+4)   ≈   0.846

- **Maximum** **_a   posteriori_ (MAP)**

   - incorporate   prior   knowledge                  about   how   params   are   distributed _P_ ( _✓_ ) _P_ <u>(</u> _data|✓_ <u>)</u> _P_ <u>(</u> _✓_ <u>)</u>

   - _✓_ ˆ _ML_ = _argmaxP_ ( _✓|data_ ) = _argmax ✓ ✓ P_ ( _Data_ )

   - – Observed   counts   plus   pseudocounts   corresponding   to   prior

17

## Learning   Bayesian   Networks: network   structure

- There   are   way   too   many   possible   structures   for   an   exhaus've approach   (e.g.   trying   every   possible   structure   and   calcula'ng the   likelihood   of   the   data   given   that   structure)

- **Common   greedy   approach   (what   Pebl   does   in   Pset   4):**

   - start   with   a   random   network

   - make   a   small   perturba'on   (e.g.   adding   or   removing   an   edge)   and rescore   network

   - if   network   scores   higher,   accept   (otherwise   reject   change)

   - repeat   from   many   star'ng   points,   pick   best   one

- **Simulated   Annealing   approach:**

   - similar   to   above,   but   accept   lower   scoring   network   with   some probability   propor'onal   to   difference   in   scores   and   temperature

   - accept   with   higher   probability   ini'ally,   then   “lower”   temp   gradually

18

- Hierarchical   Clustering

- • Useful   when   trying   to   find   structure   (e.g.   clusters of   genes   upregulated   in   repsonse   to   a   stress)   in your   data

- • Algorithm:

   - ini'alize   every   point   to   be   its   own   cluster

   - un'l   only   1   cluster   lej: • calculate   distance   between   each   cluster   and   all   other clusters   :   O(N<sup>2</sup> )   for   each   connec'on   -­‐>   O(N<sup>3</sup> )   overall

- find   the   two   closest   clusters,   merge   them   into   one   cluster

- • Can   use   various   distance/similarity   metrics   (e.g. Euclidean   distance,   correla'on,   etc.)

19

---

[← Bayesian Networks](10-bayesian-networks.md) · [Up: contents](index.md) · [Hierarchical Clustering →](12-hierarchical-clustering.md)
