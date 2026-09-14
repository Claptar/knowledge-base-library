---
title: 3.5 TABU ALGORITHMS
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/givens_hoeting_ch3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/project/givens_hoeting_ch3.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.5 TABU ALGORITHMS

**Source:** [`project/givens_hoeting_ch3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/givens_hoeting_ch3.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A tabu algorithm is a local search algorithm with a set of additional rules that guide the selection of moves in ways that are believed to promote the discovery of a global maximum. The approach employs variable neighborhoods: The rules for identifying acceptable steps change at each iteration. Detailed studies of tabu methods include [254, 255, 257–259].

In a standard ascent algorithm, entrapment in a globally uncompetitive local maximum is likely, because no downhill moves are allowed. Tabu search allows downhill moves when no uphill move can be found in the current neighborhood (and possibly in other situations too), thereby potentially escaping entrapment. An early form of tabu search, called steepest ascent/mildest descent, moved to the least unfavorable neighbor when there was no uphill move [306].

**86 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

**TABLE 3.4** Examples of attributes. The left column gives examples in a generic context. The right column gives corresponding attributes in the specific context of 2-change neighborhoods in a regression model selection problem.

|Attribute|Model Selection Example|
|---|---|
|A change in the value of_θ_<sup>(</sup><sup>_t_)</sup><br>_i_ <sup>. The attribute</sup><br>may be the value from which the move<br>began, or the value at which it arrived.<br><br>|_A_1: Whether the_i_th predictor is added (or<br>deleted) from the model.|
|A swap in the values of_θ_<sup>(</sup><sup>_t_)</sup><br>_i_<br>and_θ_<sup>(</sup><sup>_t_)</sup><br>_j_ <sup>when</sup><br>_θ_<sup>(</sup><sup>_t_)</sup><br>_i_<br>_/_=_θ_<sup>(</sup><sup>_t_)</sup><br>_j_ <sup>.</sup>|_A_2: Whether the absent variable is exchanged for<br>the variable present in the model.|
|A change in the value of_f_ resulting from the<br>step,_f_(**_θ_**<sup>(</sup><sup>_t_+1)</sup>)−_f_(**_θ_**<sup>(</sup><sup>_t_)</sup>).|_A_3: The reduction in AIC achieved by the move.|
|The value_g_(**_θ_**<sup>(</sup><sup>_t_+1)</sup>) of some other strategically<br>chosen function_g_.|_A_4: The number of predictors in the new model.|
|A change in the value of_g_resulting from the<br>step,_g_(**_θ_**<sup>(</sup><sup>_t_+1)</sup>)−_g_(**_θ_**<sup>(</sup><sup>_t_)</sup>).|_A_5: A change to a different variable selection<br>criterion such as Mallows’s_Cp_ [435] or the<br>adjusted_R_<sup>2 </sup>[483].|


If a downhill step is chosen, care must be taken to ensure that the next step (or a future one) does not simply reverse the downhill move. Such cycling would eliminate the potential long-term benefit of the downhill move. To prevent such cycling, certain moves are temporarily forbidden, or made _tabu_ , based on the recent history of the algorithm.

There are four general types of rules added to local search by tabu search methods. The first is to make certain potential moves temporarily tabu. The others involve _aspiration_ to better solutions, _intensification_ of search in promising areas of solutionspace,and _diversification_ ofsearchcandidatestopromotebroaderexploration of the solution space. These terms will be defined after we discuss tabus.

### **3.5.1 Basic Definitions**

Tabu search is an iterative algorithm initiated at time _t_ = 0 with a candidate solution **_θ_**<sup>(0)</sup> . At the _t_ th iteration, a new candidate solution is selected from a neighborhood of **_θ_**<sup>(</sup><sup>_t_)</sup> . This candidate becomes **_θ_**<sup>(</sup><sup>_t_+1)</sup> . Let _H_<sup>(</sup><sup>_t_)</sup> denote the history of the algorithm through time _t_ . It suffices for _H_<sup>(</sup><sup>_t_)</sup> to be a selective history, remembering only certain matters necessary for the future operation of the algorithm.

Unlike simple local search, a tabu algorithm generates a neighborhood of the current candidate solution that depends on the search history; denote this by _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> _, H_<sup>(</sup><sup>_t_)</sup> ). Furthermore, the identification of the preferred **_θ_**<sup>(</sup><sup>_t_+1)</sup> in _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> _, H_<sup>(</sup><sup>_t_)</sup> ) may depend not only on _f_ but also on the search history. Thus, we may assess neighbors using an augmented objective function, _fH_ ( _t_ ) .

A single step from **_θ_**<sup>(</sup><sup>_t_)</sup> to **_θ_**<sup>(</sup><sup>_t_+1)</sup> can be characterized by many _attributes_ . Attributes will be used to describe moves or types of moves that will be forbidden, encouraged, or discouraged in future iterations of the algorithm. Examples of attributes are given in the left column of Table 3.4. Such attributes are not unique to tabu search; indeed, they can be used to characterize moves from any local search.

**3.5 TABU ALGORITHMS 87**

However, tabu search explicitly adapts the current neighborhood according to the attributes of recent moves.

The attributes in Table 3.4 can be illustrated by considering a regression model selection problem. Suppose _θi_<sup>(</sup><sup>_t_)</sup> = 1 if the _i_ th predictor is included in the model at time _t_ , and 0 otherwise. Suppose that 2-change neighborhoods consist of all models to which two variables separately have each been added or deleted from the current model. The right column of Table 3.4 gives one example of each generic attribute listed, in the context of these 2-change neighborhoods in the regression model selection problem from Example 3.2. These examples are labeled _A_ 1 through _A_ 5. Many other effective attributes can be identified from the context of specific optimization problems.

Denote the _a_ th attribute as _Aa_ . Note that the complement (i.e., negation) of an attribute is also an attribute, so if _Aa_ corresponds to swapping the values of _θi_<sup>(</sup><sup>_t_)</sup> and _θj_<sup>(</sup><sup>_t_+1)</sup> , then _Aa_ corresponds to not making that swap. As the algorithm progresses, the attributes of the _t_ th move will vary with _t_ , and the quality of the candidate solution will also vary. Future moves can be guided by the history of past moves, their objective function values, and their attributes. The _recency_ of an attribute is the number of steps that have passed since a move most recently had that attribute. Let _R_ � _Aa, H_<sup>(</sup><sup>_t_)�</sup> = 0 if the _a_ th attribute is expressed in the move yielding **_θ_**<sup>(</sup><sup>_t_)</sup> , let _R_ � _Aa, H_<sup>(</sup><sup>_t_)�</sup> = 1 if it is most recently expressed in the move yielding **_θ_**<sup>(</sup><sup>_t_−1)</sup> , and so forth.

### **3.5.2 The Tabu List**

When considering a move from **_θ_**<sup>(</sup><sup>_t_)</sup> , we compute the increase in the objective function achieved for each neighbor of **_θ_**<sup>(</sup><sup>_t_)</sup> . Ordinarily, the neighbor that provides the greatest increase would be adopted as **_θ_**<sup>(</sup><sup>_t_+1)</sup> . This corresponds to the steepest ascent.

Suppose, however, that no neighbor of **_θ_**<sup>(</sup><sup>_t_)</sup> yields an increased objective function. Then **_θ_**<sup>(</sup><sup>_t_+1)</sup> is ordinarily chosen to be the neighbor that provides the smallest decrease. This is the mildest descent.

If only these two rules were used for search, the algorithm would quickly become trapped and converge to a local maximum. After one move of mildest descent, the next move would return to the hilltop just departed. Cycling would ensue.

To avoid such cycling, a _tabu list_ of temporarily forbidden moves is incorporated in the algorithm. Each time a move with attribute _Aa_ is taken, _Aa_ is put on a tabu list for _τ_ iterations. When _R_ � _Aa, H_<sup>(</sup><sup>_t_)�</sup> first equals _τ_ , the tabu expires and _Aa_ is removed from the tabu list. Thus, moves with attributes on the tabu list are effectively excluded from the current neighborhood. The modified neighborhood is denoted


This prevents undoing the change for _τ_ iterations, thereby discouraging cycling. By the time that the tabu has expired, enough other aspects of the candidate solution

**88 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

should have changed that reversing the move may no longer be counterproductive. Note that the tabu list is a list of attributes, not moves, so a single tabu attribute may forbid entire classes of moves.

The _tabu tenure_ , _τ_ , is the number of iterations over which an attribute is tabu. This can be a fixed number or it may vary, systematically or randomly, perhaps based on features of the attribute. For a given problem, a well-chosen tabu tenure will be long enough to prevent cycling and short enough to prevent the deterioration of candidate solution quality that occurs when too many moves are forbidden. Fixed tabu tenures between 7 and 20, or between 0 _._ 5<sup>√</sup> _<u>p</u>_ and 2<sup>√</sup> _<u>p</u>_ , where _p_ is the size of the problem, have been suggested for various problem types [257]. Tabu tenures that vary dynamically seem more effective in many problems [259]. Also, it will often be important to use different tenures for different attributes. If an attribute contributes tabu restrictions for a wide variety of moves, the corresponding tabu tenure should be short to ensure that future choices are not limited.

**Example 3.6 (Genetic Mapping, Continued)** We illustrate some uses of tabus, using the gene mapping problem introduced in Example 3.1.

First, consider monitoring the swap attribute. Suppose that _Aa_ is the swap attribute corresponding to exchanging two particular loci along the chromosome. When a move _Aa_ is taken, it is counterproductive to immediately undo the swap, so _Aa_ is placed on the tabu list. Search progresses only among moves that do not reverse recent swaps. Such a tabu promotes search diversity by avoiding quick returns to recently searched areas.

Second,considertheattributeidentifyingthelocuslabel _θj_ forwhich _d_<sup>ˆ</sup> ( _θj, θj_ +1) is smallest in the new move. In other words, this attribute identifies the two loci in the new chromosome that are nearest each other. If the complement of this attribute is put on the tabu list, any move to a chromosome for which other loci are closer will be forbidden moves for _τ_ iterations. Such a tabu promotes search intensity among genetic maps for which loci _θj_ and _θj_ are closest.

Sometimes, it may be reasonable to place the attribute itself, rather than its complement, on the tabu list. For example, let _h_ ( **_θ_** ) compute the mean _d_<sup>ˆ</sup> ( _θj, θj_ +1) between adjacent loci in a chromosome ordered by **_θ_** . Let _Aa_ be the attribute indicating excessive change of the mean conditional MLE map distance, so _Aa_ equals 1 if �� _h_ ( **_θ_** ( _t_ +1)) − _h_ ( **_θ_** ( _t_ ))�� _> c_ and 0 otherwise, for some fixed threshold _c_ . If a move with mean change greater than _c_ is taken, we may place _Aa_ itself on the tabu list for _τ_ iterations. This prevents any other drastic mean changes for a period of time, allowing better exploration of the newly entered region of solution space before moving far away. □

### **3.5.3 Aspiration Criteria**

Sometimes, choosing not to move to a nearby candidate solution because the move is currently tabu can be a poor decision. In these cases, we need a mechanism to override the tabu list. Such a mechanism is called an _aspiration criterion_ .

**3.5 TABU ALGORITHMS 89**

A simple and popular aspiration criterion is to permit a tabu move if it provides a higher value of the objective function than has been found in any iteration so far. Clearly it makes no sense to overlook the best solution found so far, even if it is currently tabu. One can easily envision scenarios where this aspiration criterion is useful. For example, suppose that a swap of two components of **_θ_** is on the tabu list and the candidate solutions at each iteration recently have drifted away from the region of solution space being explored when the tabu began. The search will now be in a new region of solution space where it is quite possible that reversing the tabu swap would lead to a drastic increase in the objective function.

Another interesting option is _aspiration by influence_ . A move or attribute is influential if it is associated with a large change in the value of the objective function. There are many ways to make this idea concrete [257]. To avoid unnecessary detail about numerous specific possibilities, let us simply denote the influence of the _a_ th attribute as _I_ � _Aa, H_<sup>(</sup><sup>_t_)�</sup> for a move yielding **_θ_**<sup>(</sup><sup>_t_)</sup> . In many combinatorial problems, there are a lot of neighboring moves that cause only small incremental changes to the value of the objective function, while there are a few moves that cause major shifts. Knowing the attributes of such moves can help guide search. Aspiration by influence overrides the tabu on reversing a low-influence move if a high-influence move is made prior to the reversal. The rationale for this is that the recent high-influence step may have moved the search to a new region of the solution space where further local exploration is useful. The reversal of the low-influence move will probably not induce cycling, since the intervening high-influence move likely shifted scrutiny to a portion of solution space more distant than what could be reached by the low-influence reversal.

Aspiration criteria can also be used to encourage moves that are not tabu. For example, when low-influence moves appear to provide only negligible improvement in the objective function, they can be downweighted and high-influence moves can be given preference. There are several ways to do this; one approach is to incorporate in _fH_ ( _t_ ) either a penalty or an incentive term that depends on the relative influence of candidate moves.

### **3.5.4 Diversification**

An important component of any search is to ensure that the search is broad enough. Rules based on how often attributes are observed during search can be used to increase the diversity of candidate solutions examined during tabu search.

The _frequency_ of an attribute records the number of moves that manifested that attribute since the search began. Let _C_ ( _Aa, H_<sup>(</sup><sup>_t_)</sup> ) represent the count of occurrences of the _a_ th attribute thus far. Then _F_ ( _Aa, H_<sup>(</sup><sup>_t_)</sup> ) represents a frequency function that can be used to penalize moves that are repeated too frequently. The most direct definition is _F_ ( _Aa, H_<sup>(</sup><sup>_t_)</sup> ) = _C_ ( _Aa, H_<sup>(</sup><sup>_t_)</sup> ) _/t_ , but the denominator may be replaced by the sum, the maximum, or the average of the counts of occurrences of various attributes.

Suppose the frequency of each attribute is recorded, either over the entire history or over the most recent _ψ_ moves. Note that this frequency may be one of two types, depending on the attribute considered. If the attribute corresponds to some feature

**90 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

of **_θ_**<sup>(</sup><sup>_t_)</sup> , then the frequency measures how often that feature is seen in candidate solutions considered during search. Such frequencies are termed _residence frequencies_ . If, alternatively, the attribute corresponds to some change induced by moving from one candidate solution to another, then the frequency is a _transition frequency_ . For example, in the regression model selection problem introduced in Example 3.2, the attribute noting the inclusion of the predictor _xi_ in the model would have a residence frequency. The attribute that signaled when a move reduced the AIC would have a transition frequency.

If attribute _Aa_ has a high residence frequency and the history of the most recent _ψ_ moves covers nearly optimal regions of solution space, this may suggest that _Aa_ is associated with high-quality solutions. On the other hand, if the recent history reflects the search getting stuck in a low-quality region of solution space, then a high residence frequency may suggest that the attribute is associated with bad solutions. Usually, _ψ > τ_ is an intermediate or long-term memory parameter that allows the accumulation of additional historical information to diversify future search.

Ifattribute _Aa_ hasahightransitionfrequency,thisattributemaybewhathasbeen termed a crack filler. Such an attribute may be frequently visited during the search in order to fine-tune good solutions but rarely offers fundamental improvement or change [257]. In this case, the attribute has low influence.

A direct approach employing frequency to increase search diversification is to incorporate a penalty or incentive function in _fH_ ( _t_ ) . The choice


with _c >_ 0 has been suggested [566]. If all nontabu moves are downhill, then this approach discourages moves that have the high-frequency attribute _Aa_ . An analogous strategy can be crafted to diversify the selection of uphill moves.

Instead of incorporating a penalty or incentive in the objective function, it is possible to employ a notion of graduated tabu status, where an attribute may be only partially tabu. One way to create a tabu status that varies by degrees is to invoke probabilistic tabu decisions: An attribute can be assigned a probability of being tabu, where the probability is adjusted according to various factors, including the tabu tenure [257].

### **3.5.5 Intensification**

In some searches it may be useful to intensify the search effort in particular areas of solution space. Frequencies can also be used to guide such intensification. Suppose that the frequencies of attributes are tabulated over the most recent _υ_ moves, and a corresponding record of objective function values is kept. By examining these data, key attributes shared by good candidate solutions can be identified. Then moves that retain such features can be rewarded and moves that remove such features can be penalized through _fH_ ( _t_ ) . The time span _υ > τ_ parameterizes the length of a long-term memory to enable search intensification in promising areas of solution space.

**3.5 TABU ALGORITHMS 91**

### **3.5.6 Comprehensive Tabu Algorithm**

Below we summarize a fairly general tabu algorithm that incorporates many of the features described above. After initialization and identification of a list of problemspecific attributes, the algorithm proceeds as follows:

**1.** Determine an augmented objective function _fH_ ( _t_ ) that depends on _f_ and perhaps on

   - **a.** frequency-based penalties or incentives to promote diversification, and/or **b.** frequency-based penalties or incentives to promote intensification.

**2.** Identify neighbors of **_θ_**<sup>(</sup><sup>_t_)</sup> , namely the members of _N_ ( **_θ_**<sup>(</sup><sup>_t_)</sup> ).

**3.** Rank the neighbors in decreasing order of improvement, as evaluated by _fH_ ( _t_ ) .

**4.** Select the highest ranking neighbor.

**5.** Is this neighbor currently on the tabu list? If not, go to step 8.

**6.** Does this neighbor pass an aspiration criterion? If so, go to step 8.

**7.** If all neighbors of **_θ_**<sup>(</sup><sup>_t_)</sup> have been considered and none have been adopted as **_θ_**<sup>(</sup><sup>_t_+1)</sup> , then stop. Otherwise, select the next most high-ranking neighbor and go to step 5.

**8.** Adopt this solution as **_θ_**<sup>(</sup><sup>_t_+1)</sup> .

**9.** Update the tabu list by creating new tabus based on the current move and by deleting tabus whose tenures have expired.

**10.** Has a stopping criterion been met? If so, stop. Otherwise, increment _t_ and go to step 1.

It is sensible to stop when a maximum number of iterations has been reached, and then to take the best candidate solution yet found as the final result. Search effort can be split among a collection of random starts rather than devoting all resources to one run from a single start. By casting tabu search in a Markov chain framework, it is possible to obtain results on the limiting convergence of the approach [191].

**Example 3.7 (Baseball Salaries, Continued)** A simple tabu search was applied to the variable selection problem for regression modeling of the baseball data introduced in Example 3.3. Only attributes signaling the presence or absence of each predictor were monitored. Moves that would reverse the inclusion or removal of a predictor were made tabu for _τ_ = 5 moves, and the algorithm was run for 75 moves from a random start. The aspiration criterion permitted an otherwise tabu move if it yielded an objective function value above the best previously seen.

Figure 3.7 shows the values of the AIC for the sequence of candidate solutions generated by this tabu search. The AIC was quickly improved, and an optimum value of −418 _._ 95, derived from the model using predictors 2, 3, 6, 8, 10, 13, 14, 15, 16, 24, 25, and 26, was found on two occasions: iterations 29 and 43. This solution matches the best model found using random starts local search (Table 3.2). □

**92 CHAPTER 3 COMBINATORIAL OPTIMIZATION**


<!-- Start of picture text -->
420<br>400<br>380<br>360<br>0 20 40 60<br>Iteration<br>Negative AIC<br><!-- End of picture text -->

**FIGURE 3.7** Results of tabu search for Example 3.7. Only AIC values between −360 and −420 are shown.

---

[← 3.4 GENETIC ALGORITHMS](05-3-4-genetic-algorithms.md) · [Up: contents](index.md) · [PROBLEMS →](07-problems.md)
