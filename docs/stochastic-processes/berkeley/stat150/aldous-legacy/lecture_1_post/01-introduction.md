---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_1_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_1_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 1


David Aldous

26 August 2015

David Aldous

Lecture 1


’‘Old school” course – lectures with chalk, discussion section, homework, midterms, final, textbooks. Info on web page – Google ”Aldous STAT 150”. Pencil and paper mathematical probability theory – not data/computing. Need to understand STAT 134 (seriously). First few lectures are review of STAT 134 and extra material involving conditioning; mostly by working questions. Questions presented on slides, work on blackboard, math summarized on slides, brief mentions of conceptual background. First homework due Wednesday 9 September.


- In Spring I will teach a fun “Probability in the Real World” course (STAT 157) limited to 36 students; admission by pre-quiz.

David Aldous Lecture 1


|**Outcome**<br>Seattle Seahawks|**PredictWise**<br>18 %|**Derived Betfair Price**<br>$ 0.171|**Betfair Back**<br>5.80|**Betfair Lay**<br>5.90|
|---|---|---|---|---|
|Green Bay Packers|14 %|$ 0.137|7.20|7.40|
|Indianapolis Colts|9 %|$ 0.089|11.00|11.50|
|New England Patriots|8 %|$ 0.077|12.50|13.50|
|Denver Broncos|6 %|$ 0.063|15.50|16.50|
|Dallas Cowboys|5 %|$ 0.047|21.00|22.00|
|Baltimore Ravens|4 %|$ 0.038|26.00|27.00|
|Philadelphia Eagles|3 %|$ 0.036|26.00|30.00|
|Pittsburgh Steelers|3 %|$ 0.035|28.00|30.00|
|Miami Dolphins|3 %|$ 0.033|29.00|32.00|
|Arizona Cardinals|3 %|$ 0.026|36.00|40.00|
|Cincinnati Bengals|2 %|$ 0.024|40.00|42.00|
|Kansas City Chiefs|2 %|$ 0.022|44.00|46.00|
|Carolina Panthers|2 %|$ 0.021|44.00|55.00|
|Atlanta Falcons|2 %|$ 0.020|48.00|50.00|
|New Orleans Saints|2 %|$ 0.019|50.00|55.00|
|Buffalo Bills|2 %|$ 0.018|50.00|65.00|
|Detroit Lions|2 %|$ 0.017|55.00|60.00|
|New York Giants|2 %|$ 0.017|55.00|60.00|
|Minnesota Vikings|2 %|$ 0.017|55.00|65.00|
|San Diego Chargers|1 %|$ 0.016|60.00|65.00|
|St Louis Rams|1 %|$ 0.014|65.00|75.00|
|Houston Texans|1 %|$ 0.013|75.00|80.00|
|San Francisco 49ers|1 %|$ 0.010|90.00|110.00|
|New York Jets<br>Chicago Bears|1 %<br>0 %|$ 0.010<br>$ 0.006<br>David Aldous<br>|100.00<br>160.00<br>Lecture 1|110.00<br>200.00|


<!-- Start of picture text -->
Chicago Bears 0 % David Aldous$ 0.006 Lecture160.001 200.00<br>Cleveland Browns 0 % $ 0.004 200.00 260.00<br>Washington Redskins 0 % $ 0.003 290.00 400.00<br>Tampa Bay Buccaneers 0 % $ 0.003 270.00 500.00<br>Oakland Raiders 0 % $ 0.003 310.00 410.00<br>Tennessee Titans 0 % $ 0.002 520.00 600.00<br>Jacksonville Jaguars 0 % $ 0 002 450 00 600 00<br>POLITICS<br><!-- End of picture text -->


Just for fun, here are probabilities (as perceived by gamblers) for next Superbowl winner.

No simple math theory for the actual numbers here (can build complex statistical models based on players statistics for past performance) but there is math theory for how these probabilities will fluctuate as the season progresses:

**there will be (on average) 5 teams whose perceived probability will sometime exceed 20%.**

- I’ll explain this in the ”martingales” section of the course.

David Aldous Lecture 1

---

[Up: contents](index.md) · [1. A famous hypothetical example. →](02-1-a-famous-hypothetical-example.md)
