---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/me134_monthly.pdf
source_file: sources/berkeley-stat150/aldous-legacy/me134_monthly.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`me134_monthly.pdf`](https://www.stat.berkeley.edu/~aldous/150/me134_monthly.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

March 28, 2013 6:42 a.m. aldous.tex page 583

Mathematical Assoc. of America

American Mathematical Monthly 120:7

# **Using Prediction Market Data to Illustrate Undergraduate Probability**

## **David J. Aldous**

**Abstract.** Prediction markets provide a rare setting, where results of mathematical probability theory can be related to events of real-world interest and where theory can be compared to data. The paper discusses two simple mathematical results—the halftime price principle and the serious candidates principle—and corresponding data from baseball and the 2012 Republican Presidential nomination race.

**1. INTRODUCTION.** Outside the context of games of chance based on artifacts with physical symmetry (dice, lotteries, roulette wheels, etc.), it is surprisingly difficult to find interesting real-world data that illustrates undergraduate probability calculations. The majority of examples and exercises in undergraduate probability textbooks are either “just mathematics” ( _X_ ’s and _Y_ ’s without attempting a real-world story) or unmotivated (“consider an urn containing 5 black balls, 3 white balls, and 2 blue balls”) or enter a curious fantasy world. In this fantasy world, tossed coins can be biased, darts can hit a board, or a stick can be split with uniform distribution, and people choose majors or desserts at random. But none of these are any more realistic than Jedi Knights or spherical cows. A notable exception is the recent book by Grinstead, Peterson, and Snell [ **3** ], which gives a careful introduction to four topics (streaks, the stock market, lotteries, and fingerprints), combining mathematical probability models with relevant data. The purpose of this article is to publicize another topic, prediction markets. We state below two very simple results from mathematical theory, and will give their mathematical derivation and compare with some data. As well as being (hopefully) interesting to MONTHLY readers, we might regard this article (in the spirit of [ **3** ]) as supplementary material for an undergraduate probability course.

A prediction market (browse `http://www.intrade.com` for better understanding) is essentially a venue for betting whether a specified event will occur (perhaps before a specified time), where the betting is conducted via participants buying and selling contracts with each other rather than with the operators of the market. In other words, it is structured like a stock market rather than a bookmaker. As we will discuss briefly in section 4, the mathematics of prediction markets is very similar to that of stock markets, but in several respects prediction markets are conceptually simpler and therefore more suitable for an introductory-level treatment. In a typical prediction market (details vary between markets in unimportant ways) a contract will expire at 100 or 0, depending on whether or not the specified event occurs. At any time you can see posted offers to buy and to sell, say at 56.8 and 57.2, and if you wish to buy a contract you can either pay the posted 57.2 and buy instantly, or post an offer to pay (say) 57.0 and wait to find out if anyone is willing to sell at that price. The key conceptual point is that the current market price, 57 in this example, can be interpreted as a consensus probability (57 _percent_ , of course) that the event will happen—see section 3.2 for discussion. The special feature of prediction markets, as a topic within undergraduate mathematical probability, is as the essentially unique context in which

http://dx.doi.org/10.4169/amer.math.monthly.120.07.583 MSC: Primary 60G44

583

August–September 2013] USING PREDICTION MARKET DATA

aldous.tex page 584

March 28, 2013 6:42 a.m.

Mathematical Assoc. of America

American Mathematical Monthly 120:7

we have substantial real-world data interpretable as probabilities and fluctuations of probabilities over time. Here we refer to the “price” of a contract, which the reader must always interpret as “the probability of the event occurring, given what is currently known”. The price, obviously, will fluctuate as relevant real-world information becomes known; how it will fluctuate is unknown in advance, and hence random. We use “price” rather than “probability” to avoid the linguistic confusion involved when talking about probabilities of probabilities.

Figure 1 shows price fluctuations of two specific contracts. These involved two different contexts and time scales for prediction market contracts—a few hours’ duration for a sports match or a year-long run-up to an election. The first concerned which team would be the winner of a baseball game (New York Mets vs. Florida Marlins) on August 31, 2008; the second concerned whether Newt Gingrich would be chosen as the Republican U.S. Presidential nominee in 2012. In the charts, the horizontal scale is time, and the vertical scale (on the right) is price (note that in neither case is the whole range [0 _,_ 100] shown). The low bars in the second chart show daily volume, typically under a thousand $10 contracts per day. See `http://www.intrade.com` for clear examples of current charts.

We now state two “principles”, by which we mean assertions based solely on mathematical arguments, about how prices in prediction markets should behave.


**Figure 1.** Two prediction market price charts

⃝c THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 120

584

American Mathematical Monthly 120:7 March 28, 2013 6:42 a.m. aldous.tex page 585

Mathematical Assoc. of America

**The halftime price principle.** In a sports match between equally good teams, at halftime there is some (prediction market) price for the home team winning. This price varies from match to match, depending largely on the scoring in the first half of the match. Theory says that its distribution should be approximately uniform on [0 _,_ 100].

**The serious candidates principle.** Consider an upcoming election with several candidates, and a (prediction market) price for each candidate. Suppose initially that all these prices are below _b_ , for given 0 _< b <_ 100. Theory says that the expected number of candidates whose price ever exceeds _b_ equals 100 _/b_ .

The mathematics involved here is simple and has undoubtedly been folklore for generations, though we are not aware of previous discussion in the spirit of this article. We invented the names above: Candidates become _serious_ (rather than fringe) when their chance of election exceeds some threshold.

For each principle we will explain the theory and then show some data. We assume that the reader is familiar with basic notions from an undergraduate textbook such as [ **4, 7, 8** ]. Explaining the second principle will involve the concept of a _martingale_ , typically not encountered until a second course in probability (e.g., Chapter 6 of [ **9** ] or Chapter 6 of [ **5** ]), but ultimately so widely useful that a graduate course on mathematical probability can be taught with martingales as the central topic [ **10** ]. We give only the minimal account of martingales needed here. Every textbook introduction to martingales we know treats them as mathematical objects without explicit relation to real-world data, but an instructor of a course introducing martingales could continue our style of illustrating other mathematical results about martingales with real-world prediction market data, and some examples can be found in [ **1** ].

**2. THE HALFTIME PRICE PRINCIPLE.** To elaborate this principle we imagine a sport in which (like almost all team sports) the result is decided by point difference, and for simplicity, imagine a sport like baseball or American football where there is a definite winner (ties are impossible or rare). Also for simplicity, we assume that the teams are equally good, in the sense that there is initially a 50% probability of the home team winning (that is, equally good after taking home-field advantage into account). Write _Z_ 1 for the point difference (points scored by home team, minus points scored by visiting team) in the first half, and _Z_ 2 for the point difference in the second half.

A fairly realistic mathematical model of this scenario is to assume that:

- (i) _Z_ 1 and _Z_ 2 are independent random variables, with the same distribution;

- (ii) their distribution is symmetric about zero, that is, their distribution function _F(z)_ satisfies _F(z)_ = 1 − _F(_ − _z)_ . For mathematical ease we add an unrealistic assumption (to be discussed later);

- (iii) the distribution is continuous.

Under these assumptions we can do a calculation, though first we recall the slightly sophisticated notation that treats conditional probabilities as random variables. For an event _A_ and a random variable _Y_ , the elementary notation for conditional probabilities


(the left side is always _some_ function of _y_ ) can be rewritten as


The following calculation exemplifies the usefulness of this notation.

August–September 2013] USING PREDICTION MARKET DATA

585

March 28, 2013 6:42 a.m. aldous.tex page 586

Mathematical Assoc. of America

American Mathematical Monthly 120:7

The probability that the home team wins, given that the first-half point difference is _z_ , is


and therefore the price at halftime, which is the conditional probability of the home team winning, given the observed value of _Z_ 1, is


But in fact (e.g., [ **8** , p. 234]), for a continuous distribution it is always true that _F(Z_ 1 _)_ has uniform distribution on _(_ 0% _,_ 100% _)_ .

That is the mathematical justification for the principle. We can think of various defects in the model, most obviously the fact that in real sports the points are integervalued, but for reasons explained below, we suspect that this does not make a huge difference, even in the worst case of a low-scoring sport like soccer.

---

[Up: contents](index.md) · [2.1. A little data. →](02-2-1-a-little-data.md)
