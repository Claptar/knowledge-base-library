---
title: Lecture 27 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_27_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_27_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 27 — post

**Source:** [`lecture_27_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_27_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 27


David Aldous

30 October 2015

David Aldous

Lecture 27


Theorem (Optional Sampling Theorem) _If_ ( _Xt_ ) _is a martingale and τ is a stopping time, then (under extra technical conditions)_


Advanced Probability courses give different versions of the “extra technical conditions” – see [BZ] Theorem 3.1 for one version of these conditions. In the examples I will give, it is not hard to show the conditions hold.

The “double when you lose” strategy shows that some extra condition is necessary. [board]

**Conceptual point:** The Optional Sampling Theorem and the previous “gambling systems” theorem constitute an informal “conservation of fairness” principle: the overall results of any “system” based on fair games is like a single fair bet. Even in models not explicitly involving gambling, one can do calculations by inventing hypothetical gambling strategies and using this principle.

David Aldous Lecture 27

2015-16 NFL Super Bowl | PredictWise

http://www.predictwise.com/node/4021

|**Outcome**|**PredictWise**|**Derived Betfair Price**|**Betfair Back**|**Betfair Lay**|
|---|---|---|---|---|
|New England Patriots|25 %|$ 0.241|4.10|4.20|
|Green Bay Packers|22 %|$ 0.211|4.70|4.80|
|Cincinnati Bengals|9 %|$ 0.093|10.50|11.00|
|Seattle Seahawks|7 %|$ 0.073|13.00|14.50|
|Carolina Panthers|6 %|$ 0.061|16.00|17.00|
|Denver Broncos|6 %|$ 0.060|16.50|17.00|
|Arizona Cardinals|5 %|$ 0.053|18.50|19.50|
|Atlanta Falcons|4 %|$ 0.038|26.00|27.00|
|Pittsburgh Steelers|3 %|$ 0.031|30.00|34.00|
|Indianapolis Colts|2 %|$ 0.021|46.00|50.00|
|New York Giants|2 %|$ 0.021|44.00|50.00|
|Philadelphia Eagles|2 %|$ 0.020|48.00|55.00|
|New York Jets|2 %|$ 0.019|50.00|55.00|
|Minnesota Vikings|1 %|$ 0.015|65.00|70.00|
|Dallas Cowboys|1 %|$ 0.014|65.00|80.00|
|St Louis Rams|1 %|$ 0.011|75.00|110.00|
|Miami Dolphins|1 %|$ 0.008|110.00|150.00|
|Washington Redskins|0 %|$ 0.006|100.00|700.00|
|Oakland Raiders|0 %|$ 0.005|160.00|350.00|
|New Orleans Saints|0 %|$ 0.004|200.00|350.00|
|San Diego Chargers|0 %|$ 0.004|150.00|550.00|
|Baltimore Ravens|0 %|$ 0.002|400.00|1,000.00|
|Kansas City Chiefs|0 %|$ 0.002|350.00|1,000.00|
|Buffalo Bills|0 %|$ 0.002|300.00|1,000.00|
|Chicago Bears<br>San Francisco 49ers|0 %<br>0 %|$ 0.002<br>$ 0.001<br>David Aldous|500.00<br>550.00<br>Lecture 27|1,000.00<br>0.00|


<!-- Start of picture text -->
Chicago Bears 1,000.0 0<br>San Francisco 49ers 0 % David Aldous$ 0.001 Lecture550.0027 0.00<br>Detroit Lions 0 % $ 0.001 1,000.00 0.00<br>Houston Texans 0 % $ 0.001 1,000.00 0.00<br>Cleveland Browns 0 % $ 0.001 1,000.00 0.00<br>Tennessee Titans 0 % $ 0.001 1,000.00 0.00<br>Tampa Bay Buccaneers 0 % $ 0.001 1,000.00 0.00<br>Jacksonville Jaguars 0 % $ 0 001 1 000 00 0 00<br>POLITICS<br><!-- End of picture text -->


David Aldous Lecture 27


[from Lecture 1] Just for fun, here are probabilities (as perceived by gamblers) for next Superbowl winner.

No simple math theory for the actual numbers here (can build complex statistical models based on players statistics for past performance) but there is math theory for how these probabilities will fluctuate as the season progresses:

**there will be (on average) 5 teams whose perceived probability will sometime exceed 20%.**

I’ll explain this in the ”martingales” section of the course.

David Aldous Lecture 27


**there will be (on average) 5 teams whose perceived probability will sometime exceed 20%.**

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Initially each team’s probability was less than 20% . So consider the strategy:

Place a 20 unit bet (fair odds) on each team, at the moment (if ever) its probability reaches 20%.

[continue on board]

(Here we assume probabilities change as a continuous function, not quite realistic).

David Aldous Lecture 27


[show relevant slides from popular talk] [Link to paper on course web page] [show Predictit] [show Ladbrokes] [show “real clear” poll]

David Aldous Lecture 27

---

[Up: contents](index.md)
