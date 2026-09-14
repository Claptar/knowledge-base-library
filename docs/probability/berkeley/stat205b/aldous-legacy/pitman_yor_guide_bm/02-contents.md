---
title: Contents
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Contents

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|1|Intr|oduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
|---|---|---|
||1.1|History<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
||1.2|Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>4|
|2|BM|as a limit of random walks . . . . . . . . . . . . . . . . . . . . . .<br>5|
|3|BM|as a Gaussian process . . . . . . . . . . . . . . . . . . . . . . . . .<br>7|
||3.1|Elementary transformations . . . . . . . . . . . . . . . . . . . . .<br>8|
||3.2|Quadratic variation . . . . . . . . . . . . . . . . . . . . . . . . . .<br>8|
||3.3|Paley-Wiener integrals . . . . . . . . . . . . . . . . . . . . . . . .<br>8|
||3.4|Brownian bridges . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>10|
||3.5|Fine structure of Brownian paths . . . . . . . . . . . . . . . . . .<br>10|
||3.6|Generalizations . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>10|
|||3.6.1<br>Fractional BM<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>10|
|||3.6.2<br>L´evy’s BM<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>11|
|||3.6.3<br>Brownian sheets<br>. . . . . . . . . . . . . . . . . . . . . . .<br>11|
||3.7|References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>11|
|4|BM|as a Markov process . . . . . . . . . . . . . . . . . . . . . . . . . .<br>12|
||4.1|Markov processes and their semigroups . . . . . . . . . . . . . . .<br>12|
||4.2|<br>The strong Markov property . . . . . . . . . . . . . . . . . . . . .<br>14|
||4.3|Generators<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>15|
||4.4|Transformations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>16|


0

||||_J. Pitman and M. Yor/Guide to Brownian motion_<br>1|
|---|---|---|---|
|||4.4.1|Space transformations . . . . . . . . . . . . . . . . . . . .<br>16|
|||4.4.2|Bessel processes . . . . . . . . . . . . . . . . . . . . . . . .<br>17|
|||4.4.3<br>|The Ornstein-Uhlenbeck process<br>. . . . . . . . . . . . . .<br>18<br><br>|
||4.5<br>|L´evy p<br>|rocesses<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>18<br><br>|
||4.6<br>|Refere<br>|nces for Markov processes<br>. . . . . . . . . . . . . . . . . .<br>20<br><br>|
|5|BM|as a m|artingale<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
||5.1|L´evy’s|characterization . . . . . . . . . . . . . . . . . . . . . . . .<br>21|
||5.2|Itˆo’s f|ormula<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>22|
||5.3|Stocha|stic integration<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>23|
||5.4|Constr|uction of Markov processes . . . . . . . . . . . . . . . . . .<br>26|
|||5.4.1|Stochastic differential equations . . . . . . . . . . . . . . .<br>26|
|||5.4.2|One-dimensional diffusions<br>. . . . . . . . . . . . . . . . .<br>28|
|||5.4.3|Martingale problems . . . . . . . . . . . . . . . . . . . . .<br>28|
|||5.4.4|Dirichlet forms . . . . . . . . . . . . . . . . . . . . . . . .<br>29|
||5.5|Brown|ian martingales<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>29|
|||5.5.1|Representation as stochastic integrals<br>. . . . . . . . . . .<br>29|
|||5.5.2|Wiener chaos decomposition . . . . . . . . . . . . . . . . .<br>30|
||5.6|Transf|ormations of Brownian motion . . . . . . . . . . . . . . . .<br>31|
|||5.6.1|Change of probability<br>. . . . . . . . . . . . . . . . . . . .<br>32|
|||5.6.2|Change of filtration<br>. . . . . . . . . . . . . . . . . . . . .<br>33|
|||5.6.3|Change of time . . . . . . . . . . . . . . . . . . . . . . . .<br>35|
|||5.6.4|Knight’s theorem . . . . . . . . . . . . . . . . . . . . . . .<br>35|
||5.7|BM as|a harness<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>36|
||5.8|Gaussi|an semi-martingales . . . . . . . . . . . . . . . . . . . . . .<br>36|
||5.9|Gener|alizations of martingale calculus . . . . . . . . . . . . . . .<br>37|
||5.10|Refere|nces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>37|
|6|Brow|nian f|unctionals . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>38|
||6.1|Hittin|g times and extremes<br>. . . . . . . . . . . . . . . . . . . . .<br>38|
||6.2|Occup|ation times and local times . . . . . . . . . . . . . . . . . .<br>39|
|||6.2.1|Reflecting Brownian motion . . . . . . . . . . . . . . . . .<br>41|
|||6.2.2|The Ray-Knight theorems . . . . . . . . . . . . . . . . . .<br>41|
||6.3|Additi|ve functionals<br>. . . . . . . . . . . . . . . . . . . . . . . . .<br>43|
||6.4|Quadr|atic functionals<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>44|
||6.5|Expon|ential functionals<br>. . . . . . . . . . . . . . . . . . . . . . .<br>45|
|7|Path|decom|positions and excursion theory . . . . . . . . . . . . . . . .<br>45|
||7.1|Brown|ian bridge, meander and excursion . . . . . . . . . . . . . .<br>45|
||7.2|The B|rownian zero set . . . . . . . . . . . . . . . . . . . . . . . .<br>48|
||7.3|L´evy-I|tˆo theory of Brownian excursions<br>. . . . . . . . . . . . . .<br>48|
|8|Plan|ar Bro|wnian motion . . . . . . . . . . . . . . . . . . . . . . . . . .<br>50|
||8.1|Confor|mal invariance . . . . . . . . . . . . . . . . . . . . . . . . .<br>50|
||8.2|Polarit|y of points, and windings . . . . . . . . . . . . . . . . . . .<br>50|
||8.3|Asymp|totic laws<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>51|
||8.4|Self-in|tersections . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>52|
||8.5|Expon|ents of non-intersection . . . . . . . . . . . . . . . . . . . .<br>54|
|9|Mult|idimen|sional BM<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>55|
||9.1|Skew|product representation . . . . . . . . . . . . . . . . . . . . .<br>55|


||_J. Pitman and M. Yor/Guide to Brownian motion_<br>2|
|---|---|
|9.2|Transience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>55|
|9.3|Other geometric aspects . . . . . . . . . . . . . . . . . . . . . . .<br>56|
||9.3.1<br>Self-intersections . . . . . . . . . . . . . . . . . . . . . . .<br>56|
|9.4|Multidimensional diffusions . . . . . . . . . . . . . . . . . . . . .<br>57|
|9.5|Matrix-valued diffusions . . . . . . . . . . . . . . . . . . . . . . .<br>57|
|9.6|Boundaries<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>57|
||9.6.1<br>Absorbtion<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>57|
||9.6.2<br>Reflection . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>58|
||9.6.3<br>Other boundary conditions<br>. . . . . . . . . . . . . . . . .<br>58|
|10 Brow|nian motion on manifolds<br>. . . . . . . . . . . . . . . . . . . . . .<br>58|
|10.1|Constructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>58|
|10.2|Radial processes<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>59|
|10.3|References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>59|
|11 Infin|iite dimensional diffusions . . . . . . . . . . . . . . . . . . . . . . .<br>60|
|11.1|Filtering theory . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>60|
|11.2|Measure-valued diffusions and Brownian superprocesses<br>. . . . .<br>60|
|11.3|Malliavin calculus<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>61|
|12 Con|nections with analysis . . . . . . . . . . . . . . . . . . . . . . . . .<br>62|
|12.1|Partial differential equations . . . . . . . . . . . . . . . . . . . . .<br>62|
||12.1.1 Laplace’s equation: harmonic functions . . . . . . . . . . .<br>62|
||12.1.2 The Dirichlet problem . . . . . . . . . . . . . . . . . . . .<br>63|
||12.1.3 Parabolic equations<br>. . . . . . . . . . . . . . . . . . . . .<br>64|
||12.1.4 The Neumann problem<br>. . . . . . . . . . . . . . . . . . .<br>65|
||12.1.5 Non-linear problems . . . . . . . . . . . . . . . . . . . . .<br>65|
|12.2|Stochastic differential Equations<br>. . . . . . . . . . . . . . . . . .<br>66|
||12.2.1 Dynamic Equations<br>. . . . . . . . . . . . . . . . . . . . .<br>67|
|12.3|Potential theory<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>68|
|12.4|BM and harmonic functions . . . . . . . . . . . . . . . . . . . . .<br>68|
|12.5|Hypercontractive inequalities . . . . . . . . . . . . . . . . . . . .<br>69|
|13 Con|nections with number theory . . . . . . . . . . . . . . . . . . . . .<br>69|
|14 Con|nections with enumerative combinatorics<br>. . . . . . . . . . . . . .<br>69|
|14.1|Brownian motion on fractals . . . . . . . . . . . . . . . . . . . . .<br>70|
|14.2|Analysis of fractals . . . . . . . . . . . . . . . . . . . . . . . . . .<br>71|
|14.3|Free probability . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>71|
|15 Appl|ications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>71|
|15.1|Economics and finance . . . . . . . . . . . . . . . . . . . . . . . .<br>71|
|15.2|Statistics<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>72|
|15.3|Physics<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>72|
|15.4|Fluid mechanics . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>73|
|15.5|Control of diffusions . . . . . . . . . . . . . . . . . . . . . . . . .<br>73|
|Referenc|es . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>73|


_J. Pitman and M. Yor/Guide to Brownian motion_

3

---

[← Jim Pitman and Marc Yor](01-jim-pitman-and-marc-yor.md) · [Up: contents](index.md) · [1. Introduction →](03-1-introduction.md)
