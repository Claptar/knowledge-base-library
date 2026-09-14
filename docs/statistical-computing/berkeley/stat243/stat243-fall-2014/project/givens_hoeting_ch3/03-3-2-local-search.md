---
title: 3.2 LOCAL SEARCH
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/project/givens_hoeting_ch3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/project/givens_hoeting_ch3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.2 LOCAL SEARCH

**Source:** [`project/givens_hoeting_ch3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/project/givens_hoeting_ch3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Local search is a very broad optimization paradigm that arguably encompasses all of the techniques described in this chapter. In this section, we introduce some of the its simplest, most generic variations such as _k-optimization_ and _random starts local search_ .

Basic local search is an iterative procedure that updates a current candidate solution **_θ_**<sup>(</sup><sup>_t_)</sup> at iteration _t_ to **_θ_**<sup>(</sup><sup>_t_+1)</sup> . The update is termed a _move_ or a _step_ . One or more possible moves are identified from a neighborhood of **_θ_**<sup>(</sup><sup>_t_)</sup> , say _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ). The advantage of local search over global (i.e., exhaustive) search is that only a tiny portion of **_�_** need be searched at any iteration, and large portions of **_�_** may never be examined. The disadvantage is that the search is likely to terminate at an uncompetitive local maximum.

A neighborhood of the current candidate solution, _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ), contains candidate solutions that are near **_θ_**<sup>(</sup><sup>_t_)</sup> . Often, proximity is enforced by limiting the number of changes to the current candidate solution used to generate an alternative. In practice, simple changes to the current candidate solution are usually best, resulting in small neighborhoods that are easily searched or sampled. Complex alterations are often difficult to conceptualize, complicated to code, and slow to execute. Moreover, they rarely improve search performance, despite the intuition that larger neighborhoods would be less likely to lead to entrapment at a poor local maximum. If the neighborhood is defined by allowing as many as _k_ changes to the current candidate solution in order to produce the next candidate, then it is a _k-neighborhood_ , and the alteration of those features is called a _k-change_ .

The definition a neighborhood is intentionally vague to allow flexible usage of the term in a wide variety of problems. For the gene mapping problem introduced in Example 3.1, suppose **_θ_**<sup>(</sup><sup>_t_)</sup> is a current ordering of genetic markers. A simple

**66 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

neighborhood might be the set of all orderings that can be obtained by swapping the locations of only two markers on the chromosome whose order is **_θ_**<sup>(</sup><sup>_t_)</sup> . In the regression model selection problem introduced in Example 3.2, a simple neighborhood is the set of models that either add or omit one predictor from **_θ_**<sup>(</sup><sup>_t_)</sup> .

A local neighborhood will usually contain several candidate solutions. An obvious strategy at each iteration is to choose the best among all candidates in the current neighborhood. This is the method of _steepest ascent_ . To speed performance, one might instead select the first randomly chosen neighbor for which the objective function exceeds its previous value; this is _random ascent_ or _next ascent_ .

If _k_ -neighborhoods are used for a steepest ascent algorithm, the solution is said to be _k-optimal_ . Alternatively, any local search algorithm that chooses **_θ_**<sup>(</sup><sup>_t_+1)</sup> uphill from **_θ_**<sup>(</sup><sup>_t_)</sup> is an _ascent algorithm_ , even if the ascent is not the steepest possible within _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ).

The sequential selection of steps that are optimal in small neighborhoods, disregarding the global problem, is reminiscent of a _greedy algorithm_ . A chess player using a greedy algorithm might look for the best immediate move with total disregard to its future consequences: perhaps moving a knight to capture a pawn without recognizing that the knight will be captured on the opponent’s next move. Wise selection of a new candidate solution from a neighborhood of the current candidate must balance the need for a narrow focus enabling quick moves against the need to find a globally competitive solution. To avoid entrapment in poor local maxima, it might be reasonable—every once in a while—to eschew some of the best neighbors of **_θ_**<sup>(</sup><sup>_t_)</sup> in favor of a direction whose rewards are only later realized. For example, when **_θ_**<sup>(</sup><sup>_t_)</sup> is a local maximum, the approach of _steepest ascent/mildest descent_ [306] allows a move to the least unfavorable **_θ_**<sup>(</sup><sup>_t_+1)</sup> ∈ _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) (see Section 3.5). There are also a variety of techniques in which a candidate neighbor is selected from _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ) and a random decision rule is used to decide whether to adopt it or retain **_θ_**<sup>(</sup><sup>_t_)</sup> . These algorithms generate Markov chains { **_θ_**<sup>(</sup><sup>_t_)</sup> } ( _t_ = 0 _,_ 1 _, . . ._ ) that are closely related to simulated annealing (Section 3.3) and the methods of Chapter 7.

Searching within the current neighborhood for a _k_ -change steepest ascent move can be difficult when _k_ is greater than 1 or 2 because the size of the neighborhood increases rapidly with _k_ . For larger _k_ , it can be useful to break the _k_ -change up into smaller parts, sequentially selecting the best candidate solutions in smaller neighborhoods. To promote search diversity, breaking a _k_ -change step into several smaller sequential changes can be coupled with the strategy of allowing one or more of the smaller steps to be suboptimal (e.g., random). Such _variable-depth local search_ approaches permit a potentially better step away from the current candidate solution, even though it will not likely be optimal within the _k_ -neighborhood.

Ascent algorithms frequently converge to local maxima that are not globally competitive. One approach to overcoming this problem is the technique of _random starts local search_ . Here, a simple ascent algorithm is repeatedly run to termination from a large number of starting points. The starting points are chosen randomly. The simplest approach is to select starting points independently and uniformly at random over **_�_** . More sophisticated approaches may employ some type of stratified sampling where the strata are identified from some pilot runs in an effort to partition **_�_** into regions of qualitatively different convergence behavior.

**3.2 LOCAL SEARCH 67**

**TABLE 3.1** Potential predictors of baseball players’ salaries.

|1. Batting average|10. Strikeouts (SOs)|19. Walks per SO|
|---|---|---|
|2. On base pct. (OBP)|11. Stolen bases (SBs)|20. OBP / errors|
|3. Runs scored|12. Errors|21. Runs per error|
|4. Hits|13. Free agency<sup>_a_</sup>|22. Hits per error|
|5. Doubles|14. Arbitration<sup>_b_</sup>|23. HRs per error|
|6. Triples|15. Runs per SO|24. SOs×errors|
|7. Home runs (HRs)|16. Hits per SO|25. SBs×OBP|
|8. Runs batted in (RBIs)|17. HRs per SO|26. SBs×runs|
|9. Walks|18. RBIs per SO|27. SBs×hits|


> _a_ Free agent, or eligible.

> _b_ Arbitration, or eligible.

It may seem unsatisfying to rely solely on random starts to avoid being fooled by a local maximum. In later sections we introduce methods that modify local search in ways that provide a reasonable chance of finding a globally competitive candidate solution—possibly the global maximum—on any single run. Of course, the strategy of using multiple random starts can be overlaid on any of these approaches to provide additional confidence in the best solution found. Indeed, we recommend that this is always done when feasible.

**Example 3.3 (Baseball Salaries)** Random starts local search can be very effective in practice because it is simple to code and fast to execute, allowing time for a large number of random starts. Here, we consider its application to a regression model selection problem.

Table 3.1 lists 27 baseball performance statistics, such as batting percentages and numbers of home runs, which were collected for 337 players (no pitchers) in 1991. Players’ 1992 salaries, in thousands of dollars, may be related to these variables computed from the previous season. These data, derived from the data in [654], may be downloaded from the website for this book. We use the log of the salary variable as the response variable. The goal is to find the best subset of predictors to predict log salary using a linear regression model. Assuming that the intercept will be included in any model, there are 2<sup>27</sup> = 134,217,728 possible models in the search space.

Figure 3.3 illustrates the application of a random starts local search algorithm to minimize the AIC with respect to regression variable selection. The problem can be posed as maximizing the negative of the AIC, thus preserving our preference for uphill search.Neighborhoodswerelimitedto1-changesgeneratedfromthecurrentmodelby either adding or deleting one predictor. Search was started from 5 randomly selected subsets of predictors (i.e., five starting points), and 14 additional steps were allocated to each start. Each move was made by steepest ascent. Since each steepest ascent step requires searching 27 neighbors, this small example requires 1890 evaluations of the objective function. A comparable limit to objective function evaluations was imposed on examples of other heuristic techniques that follow in the remainder of this chapter.

**68 CHAPTER 3 COMBINATORIAL OPTIMIZATION**


<!-- Start of picture text -->
420<br>400<br>380<br>360<br>1 16 31 46 61<br>Cumulative Iterations<br>Negative AIC<br><!-- End of picture text -->

**FIGURE 3.3** Results of random starts local search by steepest ascent for Example 3.3, for 15 iterations from each of five random starts. Only AIC values between −360 and −420 are shown.

Figure 3.3 shows the value of the AIC for the best model at each step. Table 3.2 summarizes the results of the search. The second and third random starts (labeled LS (2,3)) led to an optimal AIC of −418 _._ 95, derived from the model using predictors 2, 3, 6, 8, 10, 13, 14, 15, 16, 24, 25, and 26. The worst random start was the first, which led to an AIC of −413 _._ 04 for a model with 10 predictors. For the sake of comparison, a greedy stepwise method (the step() procedure in S-Plus [642]) chose a model with 12 predictors, yielding an AIC of −418 _._ 94. The greedy stepwise method of Efroymson [465] chose a model with 9 predictors, yielding an AIC of −402 _._ 16; however, this method is designed to find a good parsimonious model using a criterion that differs slightly from the AIC. With default settings, neither of these off-the-shelf algorithms found a model quite as good as the one found with a simple random starts local search. □

---

[← 3.1 HARD PROBLEMS AND NP-COMPLETENESS](02-3-1-hard-problems-and-np-completeness.md) · [Up: contents](index.md) · [3.3 SIMULATED ANNEALING →](04-3-3-simulated-annealing.md)
