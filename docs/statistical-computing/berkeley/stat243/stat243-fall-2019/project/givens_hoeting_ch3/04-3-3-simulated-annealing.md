---
title: 3.3 SIMULATED ANNEALING
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/project/givens_hoeting_ch3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/project/givens_hoeting_ch3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.3 SIMULATED ANNEALING

**Source:** [`project/givens_hoeting_ch3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/project/givens_hoeting_ch3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Simulated annealing is a popular technique for combinatorial optimization because it is generic and easily implemented in its simplest form. Also, its limiting behavior is well studied. On the other hand, this limiting behavior is not easily realized in practice, the speed of convergence can be maddeningly slow, and complex esoteric tinkering may be needed to substantially improve the performance. Useful reviews of simulated annealing include [75, 641].

Annealing is the process of heating up a solid and then cooling it slowly. When a stressed solid is heated, its internal energy increases and its molecules move randomly. If the solid is then cooled slowly, the thermal energy generally decreases slowly, but

**3.3 SIMULATED ANNEALING 69**

**TABLE 3.2** Results of random starts local search model selection for Example 3.3. The bullets indicate inclusion of the corresponding predictor in each model selected, with model labels explained in the text. In addition, all models in this table included predictors 3, 8, 13 and 14.

|||||Pr<br>|edict<br>|ors s|elec|ted||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Method|1<br>2<br>6|7<br>9<br>10|12|15|16|18|19|20|21|22|24|25|26|27|AIC|
|LS (2,3)|•<br>•|•||•|•||||||•|•|•||−418_._95|
|S-Plus|•<br>•|•||•|•||||||•|•|•||−418_._94|
|LS (5)||•|•|•|•|||•||•||•||•|−416_._15|
|LS (4)||•<br>•|||||•|•|•|•|||||−415_._52|
|LS (1)|•||•||||||•|•|•|•|||−413_._04|
|Efroy.||•<br>•||||•|||||•||•||−402_._16|


there are also random increases governed by Boltzmann’s probability. Namely, at temperature _τ_ , the probability density of an increase in energy of magnitude _�E_ is exp{− _�E/kτ_ } where _k_ is Boltzmann’s constant. If the cooling is slow enough and deep enough, the final state is unstressed, where all the molecules are arranged to have minimal potential energy.

For consistency with the motivating physical process, we pose optimization as minimization in this section, so the minimum of _f_ ( **_θ_** ) is sought over **_θ_** ∈ **_�_** . Then it is possible to draw an analogy between the physical cooling process and the process of solving a combinatorial minimization problem [130, 378]. For simulated annealing algorithms, **_θ_** corresponds to the state of the material, _f_ ( **_θ_** ) corresponds to its energy level, and the optimal solution corresponds to the **_θ_** that has minimum energy. Random changes to the current state (i.e., moves from **_θ_**<sup>(</sup><sup>_t_)</sup> to **_θ_**<sup>(</sup><sup>_t_+1)</sup> ) are governed by the Boltzmann distribution given above, which depends on a parameter called temperature. When the temperature is high, acceptance of uphill moves (i.e., moves to a higher energy state) are more likely to be tolerated. This discourages convergence to the first local minimum that happens to be found, which might be premature if the space of candidate solutions has not yet been adequately explored. As search continues, the temperature is lowered. This forces increasingly concentrated search effort near the current local minimum, because few uphill moves will be allowed. If the cooling schedule is determined appropriately, the algorithm will hopefully converge to the global minimum.

The simulated annealing algorithm is an iterative procedure started at time _t_ = 0 with an initial point **_θ_**<sup>(0)</sup> and a temperature _τ_ 0. Iterations are indexed by _t_ . The algorithm is run in stages, which we index by _j_ = 0 _,_ 1 _,_ 2 _, . . ._ , and each stage consists of several iterations. The length of the _j_ th stage is _mj_ . Each iteration proceeds as follows:

**1.** Select a candidate solution **_θ_**<sup>∗</sup> within the neighborhood of **_θ_**<sup>(</sup><sup>_t_)</sup> , say _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ), according to a proposal density _g_<sup>(</sup><sup>_t_)</sup> (· | **_θ_**<sup>(</sup><sup>_t_)</sup> ).

**2.** Randomly decide whether to adopt **_θ_**<sup>∗</sup> as the next candidate solution or to keep another copy of the current solution. Specifically, let **_θ_**<sup>(</sup><sup>_t_+1)</sup> = **_θ_**<sup>∗</sup> with probability equal to min �1 _,_ exp �[ _f_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) − _f_ ( **_θ_**<sup>∗</sup> )] _/τj_ ��. Otherwise, let **_θ_**<sup>(</sup><sup>_t_+1)</sup> = **_θ_**<sup>(</sup><sup>_t_)</sup> .

**70 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

**3.** Repeat steps 1 and 2 a total of _mj_ times.

**4.** Increment _j_ . Update _τj_ = _α_ ( _τj_ −1) and _mj_ = _β_ ( _mj_ −1). Go to step 1.

If the algorithm is not stopped according to a limit on the total number of iterations or a predetermined schedule of _τj_ and _mj_ , one can monitor an absolute or relative convergence criterion (see Chapter 2). Often, however, the stopping rule is expressed as a minimum temperature. After stopping, the best candidate solution found is the estimated minimum.

The function _α_ should slowly decrease the temperature to zero. The number of iterations at each temperature ( _mj_ ) should be large and increasing in _j_ . Ideally, the function _β_ should scale the _mj_ exponentially in _p_ , but in practice some compromises will be required in order to obtain tolerable computing speed.

Although the new candidate solution is always adopted when it is superior to the current solution, note that it has some probability of being adopted even when it is inferior. In this sense, simulated annealing is a stochastic descent algorithm. Its randomness allows simulated annealing sometimes to escape uncompetitive local minima.

### **3.3.1 Practical Issues**

**_3.3.1.1 Neighborhoods and Proposals_** Strategies for choosing neighborhoods can be very problem specific, but the best neighborhoods are usually small and easily computed.

Consider the traveling salesman problem. Numbering the cities 1 _,_ 2 _, . . . , p_ , any tour **_θ_** can be written as a permutation of these integers. The cities are linked in this order, with an additional link between the final city visited and the original city where the tour began. A neighbor of **_θ_** can be generated by removing two nonadjacent links and reconnecting the tour. In this case, there is only one way to obtain a valid tour through reconnection: One of the tour segments must be reversed. For example, the tour 143256 is a neighbor of the tour 123456. Since two links are altered, the process of generating such neighbors is a 2-change, and it yields a 2-neighborhood. Any tour has _p_ ( _p_ − 3) _/_ 2 unique 2-change neighbors distinct from **_θ_** itself. This neighborhood is considerably smaller than the ( _p_ − 1)! _/_ 2 tours in the complete solution space.

It is critical that the chosen neighborhood structure allows all solutions in **_�_** to _communicate_ . For **_θ_** _i_ and **_θ_** _j_ to communicate, it must be possible to find a finite sequence of solutions **_θ_** 1 _, . . . ,_ **_θ_** _k_ such that **_θ_** 1 ∈ _N_ ( **_θ_** _i_ ), **_θ_** 2 ∈ _N_ ( **_θ_** 1), _. . ._ , **_θ_** _k_ ∈ _N_ ( **_θ_** _k_ −1), and **_θ_** _j_ ∈ _N_ ( **_θ_** _k_ ). The 2-neighborhoods mentioned above for the traveling salesman problem allow communication between any **_θ_** _i_ and **_θ_** _j_ .

The most common proposal density, _g_<sup>(</sup><sup>_t_)</sup> (· | **_θ_**<sup>(</sup><sup>_t_)</sup> ), is discrete uniform—a candidate is sampled completely at random from _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ). This has the advantage of speed and simplicity. Other, more strategic methods have also been suggested [281, 282, 659].

Rapid updating of the objective function is an important strategy for speeding simulated annealing runs. In the traveling salesman problem, sampling a 2-neighbor at random amounts to selecting two integers from which is derived a permutation of the current tour. Note also for the traveling salesman problem that _f_ ( **_θ_**<sup>∗</sup> ) can be efficiently calculated for any **_θ_**<sup>∗</sup> in the 2-neighborhood of **_θ_**<sup>(</sup><sup>_t_)</sup> when _f_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) has

**3.3 SIMULATED ANNEALING 71**

already been found. In this case, the new tour length equals the old tour length minus the distance for traveling the two broken links, plus the distance for traveling the two new links. The time to compute this does not depend on problem size _p_ .

**_3.3.1.2 Cooling Schedule and Convergence_** The sequence of stage lengths and temperatures is called the _cooling schedule_ . Ideally, the cooling schedule should be slow.

The limiting behavior of simulated annealing follows from Markov chain theory, briefly reviewed in Chapter 1. Simulated annealing can be viewed as producing a sequence of homogeneous Markov chains (one at each temperature) or a single inhomogeneous Markov chain (with temperature decreasing between transitions). Although these views lead to different approaches to defining limiting behavior, both lead to the conclusion that the limiting distribution of draws has support only on the set of global minima.

To understand why cooling should lead to the desired convergence of the algorithm at a global minimum, first consider the temperature to be fixed at _τ_ . Suppose further that proposing **_θ_** _i_ from _N_ ( **_θ_** _j_ ) has the same probability as proposing **_θ_** _j_ from _N_ ( **_θ_** _i_ ) for any pair of solutions **_θ_** _i_ and **_θ_** _j_ in **_�_** . In this case, the sequence of **_θ_**<sup>(</sup><sup>_t_)</sup> generated by simulated annealing is a Markov chain with stationary distribution _πτ_ ( **_θ_** ) ∝ exp{− _f_ ( **_θ_** ) _/τ_ }. This means that lim _t_ →∞ _P_ [ **_θ_**<sup>(</sup><sup>_t_)</sup> = **_θ_** ] = _πτ_ ( **_θ_** ). This approach to generating a sequence of random values is called the _Metropolis algorithm_ and is discussed in Section 7.1.

In principle, we would like to run the chain at this fixed temperature long enough that the Markov chain is approximately in its stationary distribution before the temperature is reduced.

Suppose there are _M_ global minima and the set of these solutions is _M_ . Denote the minimal value of _f_ on **_�_** as _f_ min. Then the stationary distribution of the chain for a fixed _τ_ is given by


for each **_θ_** _i_ ∈ **_�_** .

Now, as _τ_ → 0 from above, the limit of exp{− � _f_ ( **_θ_** _i_ ) − _f_ min�� _τ_ } is 0 if _i_ ∈ _/ M_ and 1 if _i_ ∈ _M_ . Thus


The mathematics to make these arguments precise can be found in [67, 641].

It is also possible to relate the cooling schedule to a bound on the quality of the final solution. If one wishes any iterate to have not more than probability _δ_ in equilibrium of being worse than the global minimum by no more than _ϵ_ , this can be achieved if one cools until _τj_ ≤ _ϵ/_ log{( _N_ − 1) _/δ_ }, where _N_ is the number of points in **_�_** [426]. In other words, this _τj_ ensures that the final Markov chain configuration will in equilibrium have _P_ � _f_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) _> f_ min + _ϵ_ � _< δ_ .

**72 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

If neighborhoods communicate and the depth of the deepest local (and nonglobal) minimum is _c_ , then the cooling schedule given by _τ_ = _c/_ log{1 + _i_ } guarantees asymptotic convergence, where _i_ indexes iterations [292]. The depth of a local minimum is defined to be the smallest increase in the objective function needed to escape from that local minimum into the valley of any other minimum. However, mathematical bounds on the number of iterations required to achieve a high probability of having discovered at least one element of _M_ often exceed the size of **_�_** itself. In this case, one cannot establish that simulated annealing will find the global minimum more quickly than an exhaustive search [33].

If one wishes the Markov chain generated by simulated annealing to be approximately in its stationary distribution at each temperature before reducing temperature, then the length of the run ideally should be at least quadratic in the size of the solution space [1], which itself is usually exponential in problem size. Clearly, much shorter stage lengths must be chosen if simulated annealing is to require fewer iterations than exhaustive search.

In practice, many cooling schedules have been tried [641]. Recall that the temperature at stage _j_ is _τj_ = _α_ ( _τj_ −1) and the number of iterations in stage _j_ is _mj_ = _β_ ( _mj_ −1). One popular approach is to set _mj_ = 1 for all _j_ and reduce the temperature very slowly according to _α_ ( _τj_ −1) = _τj_ −1 _/_ (1 + _aτj_ −1) for a small value of _a_ . A second option is to set _α_ ( _τj_ −1) = _aτj_ −1 for _a <_ 1 (usually _a_ ≥ 0 _._ 9). In this case, one might increase stage lengths as temperatures decrease. For example, consider _β_ ( _mj_ −1) = _bmj_ −1 for _b >_ 1, or _β_ ( _mj_ −1) = _b_ + _mj_ −1 for _b >_ 0. A third schedule uses


where _sτ_<sup>2</sup> _j_ −1<sup>is the square of the mean objective function cost at the current temperature</sup> minus the mean squared cost at the current temperature, and _r_ is some small real number [1]. Using the temperature schedule _τ_ = _c/_ log{1 + _i_ } mentioned above based on theory is rarely practical because it is too slow and the determination of _c_ is difficult, with excessively large guesses for _c_ further slowing the algorithm.

Most practitioners require lengthy experimentation to find suitable initial parameter values (e.g., _τ_ 0 and _m_ 0) and values of the proposed schedules (e.g., _a_ , _b_ , and _r_ ). While selection of the initial temperature _τ_ 0 is usually problem dependent, some general guidelines may be given. A useful strategy is to choose a positive _τ_ 0 value so that exp �[ _f_ ( **_θ_** _i_ ) − _f_ ( **_θ_** _j_ )] _/τ_ 0� is close to 1 for any pair of solutions **_θ_** _i_ and **_θ_** _j_ in **_�_** . The rationale for this choice is that it provides any point in the parameter space with a reasonable chance of being visited in early iterations of the algorithm. Similarly, choosing _mj_ to be large can produce a more accurate solution, but can result in long computing times. As a general rule of thumb, larger decreases in temperature require longer runs after the decrease. Finally, a good deal of evidence suggests that running simulated annealing long at high temperatures is not very useful. In many problems, the barriers between local minima are sufficiently modest that jumps between them are possible even at fairly low temperatures. Good cooling schedules therefore decrease the temperature rapidly at first.

**3.3 SIMULATED ANNEALING 73**


<!-- Start of picture text -->
−360 1.0<br>−380<br>0.5<br>−400<br>−420 0<br>0 1000 2000<br>Iteration<br>AIC<br>Temperature<br><!-- End of picture text -->

**FIGURE 3.4** Results of two simulated annealing minimizations of the regression model AIC for Example 3.4. The temperature for the bottom curve is shown by the dotted line and the right axis. Only AIC values between −360 and −420 are shown.

**Example 3.4 (Baseball Salaries, Continued)** To implement simulated annealing for variable selection via the AIC in the baseball salary regression problem introduced in Example 3.3, we must establish a neighborhood structure, a proposal distribution, and a temperature schedule. The simplest neighborhoods contain 1-change neighbors generated from the current model by either adding or deleting one predictor. We assigned equal probabilities to all candidates in a neighborhood. The cooling schedule had 15 stages, with stage lengths of 60 for the first 5 stages, 120 for the next 5, and 220 for the final 5. Temperatures were decreased according to _α_ ( _τj_ −1) = 0 _._ 9 _τj_ −1 after each stage.

Figure 3.4 shows the values of the AIC for the sequence of candidate solutions generated by simulated annealing, for two different choices of _τ_ 0. The bottom curve corresponds to _τ_ 0 = 1. In this case, simulated annealing became stuck at particular candidate solutions for distinct periods because the low temperatures allowed little tolerance for uphill moves. In the particular realization shown, the algorithm quickly found good candidate solutions with low AIC values, where it became stuck frequently. However, in other cases (e.g., with a very multimodal objective function), such stickiness may result in the algorithm becoming trapped in a region far from the global minimum. A second run with _τ_ 0 = 6 (top solid line) yielded considerable mixing, with many uphill proposals accepted as moves. The temperature schedule for _τ_ 0 = 1 is shown by the dotted line and the right axis. Both runs exhibited greater mixing at higher temperatures. When _τ_ 0 = 1, the best model found was first identified in the 1274th step and dominated the simulation after that point. This model achieved an AIC of −418 _._ 95, and matched the best model found using random starts local search in Table 3.2. When _τ_ 0 = 6, the best model found had an AIC of −417 _._ 85.

**74 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

This run was clearly unsuccessful, requiring more iterations, cooler temperatures, or both. □

### **3.3.2 Enhancements**

There are many variations on simulated annealing that purport to improve performance. Here we list a few ideas in an order roughly corresponding to the steps in the basic algorithm.

The simplest way to start simulated annealing is to start once, anywhere. A strategy employing multiple random starts would have the dual advantages of potentially finding a better candidate solution and allowing confirmation of convergence to the particular optimum found. Purely random starts could be replaced by a stratified set of starting points chosen by strategic preprocessing to be more likely to lead to minima than simple random starts. Such strategies must have high payoffs if they are to be useful, given simulated annealing’s generally slow convergence. In some cases, the extra iterations dedicated to various random starts may be better spent on a single long run with longer stage sizes and a slower cooling schedule.

The solution space, **_�_** , may include constraints on **_θ_** . For example, in the genetic mapping problem introduced in Example 3.1, **_θ_** must be a permutation of the integers 1 _, . . . , p_ when there are _p_ markers. When the process for generating neighbors creates solutions that violate these constraints, substantial time may be wasted fixing candidates or repeatedly sampling from _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) until a valid candidate is found. An alternative is to relax the constraints and introduce a penalty into _f_ that penalizes invalid solutions. In this manner, the algorithm can be discouraged from visiting invalid solutions without dedicating much time to enforcing constraints.

In the basic algorithm, the neighborhood definition is static and the proposal distribution is the same at each iteration. Sometimes improvements can be obtained by adaptively restricting neighborhoods at each iteration. For example, it can be useful to shrink the size of the neighborhood as time increases to avoid many wasteful generations of distant candidates that are very likely to be rejected at such low temperatures. In other cases, when a penalty function is used in place of constraints, it may be useful to allow only neighborhoods composed of solutions that reduce or eliminate constraint violations embodied in the current **_θ_** .

It is handy if _f_ can be evaluated quickly for new candidates. We noted previously that neighborhood definitions can sometimes enable this, as in the traveling salesman problem where a 2-neighborhood strategy led to a simple updating formula for _f_ . Simple approximation of _f_ is sometimes made, often in a problemspecific manner. At least one author suggests monitoring recent iterates and introducing a penalty term in _f_ that discourages revisiting states like those recently visited [201].

Next consider the acceptance probability given in step 2 of the canonical simulated annealing algorithm in Section 3.3. The expression exp{[ _f_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) − _f_ ( **_θ_**<sup>∗</sup> )] _/τj_ } is motivated by the Boltzmann distribution from statistical thermodynamics. Other acceptance probabilities can be used, however. The linear Taylor series expansion of the Boltzmann distribution motivates min �1 _,_ 1 + �� _f_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) − _f_ ( **_θ_**<sup>∗</sup> )�� _τj_ �� as a possible acceptance probability [352]. To encourage moderate moves away from

**3.4 GENETIC ALGORITHMS 75**

local minima while preventing excessive small moves, the acceptance probability min �1 _,_ exp �� _c_ + _f_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) − _f_ ( **_θ_**<sup>∗</sup> )�� _τj_ ��, where _c >_ 0, has been suggested for certain problems [169].

In general, there is little evidence that the shape of the cooling schedule (linear, polynomial, exponential) matters much, as long as the useful range of temperatures is covered, the range is traversed at roughly the same rate, and sufficient time is spent at each temperature (especially the low temperatures) [169]. Reheating strategies that allow sporadic, systematic, or interactive temperature increases to prevent getting stuck in a local minimum at low temperatures can be effective [169, 256, 378].

After simulated annealing is complete, one might take the final result of one or more runs and polish these with a descent algorithm. In fact, one could refine occasionalacceptedstepsinthesameway,insteadofwaitinguntilsimulatedannealing has terminated.

---

[← 3.2 LOCAL SEARCH](03-3-2-local-search.md) · [Up: contents](index.md) · [3.4 GENETIC ALGORITHMS →](05-3-4-genetic-algorithms.md)
