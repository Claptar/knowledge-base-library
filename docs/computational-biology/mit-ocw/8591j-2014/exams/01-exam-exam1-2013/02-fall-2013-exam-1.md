---
title: 'Fall 2013 Exam #1'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/exams/01-exam-exam1-2013.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Fall 2013 Exam #1

**Source:** `exams/01-exam-exam1-2013.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- <u>Instructions</u> 1) Please   do   not   open the   exam   until   instructed   to   do   so. 2) This   exam   is   closed-­‐book   and   closed-­‐notes. 3) Please   do   all   problems.

   - 4) Use   the   back   of   sheets   if   you   need   more   space.

Name:

## <u>Scores</u>

- 1:   (out   of   9)

- 2:   (out   of   14)

- 3:   (out   of   16)

- 4:   (out   of   12)

- 5:   (out   of   10)

- 6:   (out   of   14)

- 7:   (out   of   11)

- 8:   (out   of   14)

Total   (out   of   100):

1

Fall   2013   Systems   Biology,   Exam   #1

## **1)   Negative   autoregulation   (9   points)**

Consider   a   gene   X   which   represses   its   own   expression.   We   will   use   the   logic   approximation,   such that   the   concentration   rate   of   production   is β when   [X]   <   K   and   0   otherwise. Let α   be   the effective   degradation   of   protein   X.   For   what   values   of   ,   ,   and   K   is   [X]α β eq robust   against variations   in   α,   β,   and   K?

Variations   in   α   (3   pt):

Variations   in   β   (3   pt):

Variations   in _K_ (3   pt):

2

Fall   2013   Systems   Biology,   Exam   #1

**2) Oscillations   in   Negative   autoregulation   (14   points,   2   pages)** a.   Consider   a   protein represses   its   own   expression   such   that   the   differential   equation   describing ! the   concentration   of      is: _p_ 𝑝 ! − 𝑝 = !!! Under   what   parameter range   will   this   self-­‐repression   lead   to   oscillations?   Is   the   fixed   point stable   or   unstable? (4   pt)


What   is   the   fixed   point   of   this   pair   of   equations?   (2   pt)

3

Fall   2013   Systems   Biology,   Exam   #1

c.   Use   linear   stability   analysis to   determine the   conditions   (if   any)   in   which   this   fixed   point becomes   unstable, leading to oscillations. (6   pt)

d.   How   could   this   model   be   modified   to   enhance   the   ability   to   lead   to   oscillations?   (2   pt)

4

Fall   2013   Systems   Biology,   Exam   #1

## **3) Network   growth   (16   points   plus   5   points   extra   credit,   2   pages)**

Consider   the   Barabasi   model   of   network   growth   that   leads   to   power   law   distributions   of   the degree   distribution. Starting   with _m0_ nodes,   at each time   point   add one   node   and randomly connect   it   to      existing   nodes   with   probabilit _m_ ies proportional   to   the   existing   number   of   edges (first   round   connect   at   random).

a.   What   is   the   total   number   of   edges   in   the   network   at   time   t?   (2   pt)

b.   What   is   the   sum   of   the   number   of   connections   (i.e.   degree)   over   all   nodes   at   time   t?   (2   pt)

c.   If   node _i_ was added   to   the network at   time _ti_ then   how   does   the   expected   number   of   edges from   that   node ( _ki_ )   grow with time? (6   pt)

5

Fall   2013   Systems   Biology,   Exam   #1

Now we will   consider   a   model   in   which there is network   growth but no preferential   attachment. Instead,   we will   assume that   new   nodes attach   to the   existing   nodes with equal   probability independent   of   the   number   of   connections   that   a   node   has d.   Does   this   model   without   preferential   attachment   lead   to   a   random   Erdos-­‐Renyi   Network? Why   or   why   not?   (2   pt)

e. In   this   new   model,   if node _i_ was   added   to   the network at   time _ti_ then   how   does   the   expected number of   edges   from   that   node   ( _ki_ )   grow with time?   (4 pt)

EXTRA   CREDIT. Demonstrate that   for   long times   this model   does   not lead   to   a   power   law distribution   but   instead to   a distribution   that   falls   off exponentially   with   the   number   of connections.   (5   pt   extra   credit)

6

Fall   2013   Systems   Biology,   Exam   #1

- **4) Analysis   of   network motifs   (12   points).** For this   problem,   an   arrow   will   signify   either positive or   negative   regulation.   In   Uri   Alon’s book/paper,   he   studied   the   transcriptional   network of   E.   coli,   which   had   N   =   424   nodes   (genes)   and   E   =   514   edges   (interactions). For   each   of   the   four examples   given   below,   answer   the   following   three   questions   : a. Draw   the   sub-­‐network   (1   pt   for   each) b. Given   a   random   Erdos-­‐Renyi   network,   how   many   of   each   of   the   following   sub-­‐graphs   do you   expect   to   see? (1   pt   for   each)

- c. Is   the   indicated   subgraph   a   network   motif   in   this   system?   (1   pt   for   each) 1

- As   a   reminder, _NG_<sup>=</sup> _N_<sup>_n_</sup> _p_<sup>_g_</sup> ,   where _p_ is   the   probability   of   an   edge   being   realized. _a_

a.   Autoregulation   (3   pt)

- b.   Toggle-­‐switch   (3   pt)

- c.   Repressilator   (3   pt)

## d.   Feed-­‐forward   loop   (3   pt)

7

Fall   2013   Systems   Biology,   Exam   #1

## **5)   Pulse   generation   (10   points   total)**

a.   Which   Feed   Forward   Loop   can   generate   a   pulse   of   Z   in   response   to   the   signal   Sx   appearing?   (3 pt)

b. In this network   motif,   how   should   the   transcription   factors   X   and   Y   levels   be   combined   at   the Z promoter? Please   fill   in   the   logic   table   below. (2   pt)

|X <br>|Y<br>|Z|
|---|---|---|
|0|0||
|0<br>|1<br>||
|1 <br>|0  <br>||
|1<br>|1||


c. If   at   time t=   0 the   signal Sx   appears and activates   the transcription factor X (which   is   already   at steady state),   draw   the following as   a function   of   time: X,   X*,   Y* (assume   Sy always   present),   Z. (5   pt)

8

Fall   2013   Systems   Biology,   Exam   #1

**6) Protein bursts (14   points   total)** Assume that   after   an   mRNA   is   transcribed   that   it   is   degraded   at   rate   δ   and   translated   at   rate   r.

a.   What   is   the   (normalized)   probability   distribution   pfirst(t)   that   describes   the   time   in   which   the first   of   these   reactions   will   occur?   (3   pt)

- b.   What   is   the   probability   ρ   that   a   protein   will   be   translated   before   the   mRNA   is   degraded?   (2   pt)

- c.   What   is   the   probability   distribution   p(n)   describing   the   probability   that   the   mRNA   will produce   n   proteins?   (3   pt)

d. Assume   that   the   probability   ρ   from   part   (b)   is   0.5.   In   addition,   assume   that   two   mRNA   are produced   in   quick   succession.   The   resulting   protein   burst   is   then from   the proteins   transcribed from   both   of   these   mRNA.   What   is   the   probability   that   the   combined   protein   burst   has the following   sizes? (6   pt)

P(n=0): P(n=1):


P(n=3): P(n=k):

9

Fall   2013   Systems   Biology,   Exam   #1

**7)   Master   Equation   (11   points   total)** Consider   the   following   model   of   negative   autoregulation: 𝑛 = <u>!!</u> − 𝛼𝑛, !!! where _n_ is   the   number   of   proteins   in   the   cell   and _K_ is   the   number   of   proteins   at   which   there   is half repression   of   the promoter.

a. Using the Master   Equation   formalism,   write   an   expression   for   how   the   probability   of   having _n_ proteins changes   with   time.   (2   pt)

b.   Assume   that   β   =   1   min<sup>-­‐1</sup> ,   α   =   0.1   min<sup>-­‐1</sup> ,   and      =   10   proteins.   If   at   time   t   =   0   we   are   told   that   the _K_ cell   starts   such   that   p(n=20)   =   0.5,   p(n=21)   =   0.5,   what   is   the   probability   distribution   of   states   a short   time   Δt   =   0.01   min   later?      Keep   all   terms   that   are   on   the   order   of   Δt.   (5   pt)

<u>!(!!!")</u> c.   If   we   now   wait   a   long   time   until   the   system   reaches   equilibrium,   what   is   the   ratio !(!!!")<sup>?</sup> (4   pt)

10

Fall   2013   Systems   Biology,   Exam   #1

**8) Cooperatively   binding   transcription   factor   (14   points   total)** a.   Consider   a   transcription   factor   X that   dimerizes with   dissociation   constant _KX_ (units   of concentration).   What   is   the   concentration   of   the dimer [X2]   as   a   function   of   [X]T,   the   total concentration   of   X?   Simplify   in   the   limit   [X]T   << _KX_ and   in   the   limit   [X]T   >> _KX_ .   Draw   [X2]   as   a function   of   [X]T.   (7   pt)

b. Now assume that the dimer X2   activates   expression   of   gene   Y,   where   the   rate   of   expression   is proportional   to the fraction   of time   that   the   promoter   is   bound   by   the   dimer.   Assuming that   the binding   of   the   dimer   has   dissociation   constant   Kp   and   the   maximal   rate   of   expression   is   β,   what is   the   mean   rate   of   expression   as   a   function   of   [X]T?   (3   pt)

c.   Draw   the   mean   rate   of   expression   of   gene   Y   as   a   function   of   [X]T,   for _Kp_ << _Kx_ and   for _Kp_ >> _Kx_ . **Comment** .   (4pt)

11

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 7.32/7.81J/8.591J: Systems Biology](01-7-32-7-81j-8-591j-systems-biology.md) · [Up: contents](index.md)
