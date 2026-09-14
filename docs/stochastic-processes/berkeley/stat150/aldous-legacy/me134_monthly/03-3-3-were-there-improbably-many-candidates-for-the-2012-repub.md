---
title: 3.3. Were there improbably many candidates for the 2012 Republican nomi-
source: https://www.stat.berkeley.edu/~aldous/150/me134_monthly.pdf
source_file: sources/berkeley-stat150/aldous-legacy/me134_monthly.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.3. Were there improbably many candidates for the 2012 Republican nomi-

**Source:** [`me134_monthly.pdf`](https://www.stat.berkeley.edu/~aldous/150/me134_monthly.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**nation whose fortunes rose and fell?** In the race for the 2012 Republican Presidential nomination there were many candidates whose popularity rose and then fell noticably—Donald Trump, Newt Gingrich, Sarah Palin, Rick Perry, and Michelle

August–September 2013] USING PREDICTION MARKET DATA

589

aldous.tex page 590

March 28, 2013 6:42 a.m.

Mathematical Assoc. of America

American Mathematical Monthly 120:7

Bachmann, for instance. Almost all discussions of the race have shared the presumption that the number of such candidates was much larger than usual, and speculated on the reasons, e.g., an “anyone but Romney” sentiment. But is that presumption true?

We need to distinguish between two meanings. Opinion polls ask questions such as, “if you were voting tomorrow, who would you vote for?”. Mathematics says nothing about how much such opinions may fluctuate over a year-long campaign, just as mathematics says nothing about how much fashions in popular music may fluctuate. We could devise some statistic to measure these fluctuations and compare it empirically with the statistics from previous races, but we cannot compare it to any theoretical prediction.

On the other hand, the theoretical argument that every prediction market price should be a martingale is not affected by fashion or opinion poll results. So we can examine whether the prediction market prices in this particular race behaved differently from how theory says prediction market prices should behave, which would be an indication of some unusual aspect of the 2012 race.

**3.4. Argument for the serious candidates principle.** We want a model for prediction market prices for an upcoming election, in the generalized sense of one candidate being chosen at a specified future date (so this covers future Oscar winners, for instance, for which Intrade also provides markets). The only assumption we need is that each candidate’s price is a continuous-path martingale. Here, continuous-path is not literally true (prices are discrete) but corresponds to the idea of a “liquid market” with small spread between bid and ask prices, which is reasonably accurate for the election markets under consideration.

To restate the serious candidates principle:

_Consider an upcoming election with several candidates, and a (prediction market) price for each candidate. Suppose initially that all these prices are below b, for given_ 0 _< b <_ 100 _. Theory says that the expected number of candidates whose price ever exceeds b, equals_ 100 _/b._

Here is the mathematical argument, based on a hypothetical betting system. For each candidate, buy a contract on that candidate if and when their price reaches _b_ . The total cost of these contracts is _bNb_ , where _Nb_ is the random number of candidates whose price ever reaches level _b_ . Exactly one candidate is elected, and your contract on that candidate earns you 100. So your gain is 100 − _bNb_ . The conservation of fairness theorem says that the expected gain equals zero, and that the equation _E_ [100 − _bNb_ ] = 0 rearranges to _E_ [ _Nb_ ] = 100 _/b_ .

**3.5. Data.** Table 1 shows the maximum Intrade prediction market price (up to June 8) for each of the 16 leading candidates for the 2012 Republican Presidential nomination.

**Table 1.** Maximum prediction market prices.

|Romney|98|Perry|39|Gingrich|38|Palin|28|
|---|---|---|---|---|---|---|---|
|Pawlenty|25|Santorum|18|Huntsman|18|Bachmann|18|
|Huckabee|17|Daniels|14|Christie|10|Giuliani|10|
|Bush|9|Cain|9|Trump|8.7|Paul|8.5|


⃝c THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 120

590

March 28, 2013 6:42 a.m. aldous.tex page 591

Mathematical Assoc. of America

American Mathematical Monthly 120:7

These numbers might well suggest to a non-mathematician that the number of sometime-serious candidates was unusually large. But look at Table 2, which compares observed data with the mathematical prediction for “number of candidates with maximum price ≥ _b_ ” for several values of _b_ .

Table 2 indicates that the number of candidates whose fortunes rose and fell in this “probability of winning” sense was scarcely more than would be expected on mathematical grounds.

**Table 2.** Observed and expected numbers exceeding threshold prices.

||Expected|Observed|
|---|---|---|
|_b_=33_._3|3|3|
|_b_=20|5|5|
|_b_=16_._6|6|9|
|_b_=12_._5|8|10|


**Two technical points.** In Table 2 we used 100 _/b_ as “expected”, without considering whether some initial prices might have been greater than _b_ . Data on initial prices is somewhat unreliable (because the contract may initially be thinly traded), but the only candidate whose initial price was clearly above 10 was Romney, at about 23. Correcting for this would make the “expected” numbers slightly smaller for small _b_ . Of course, for a campaign where two candidates started with price 40, the “expected” numbers would be very different. Another important general point is that, for long-duration contracts, low prediction market prices overstate the true consensus probability because of the “covering your position” requirement. That is, even if you were certain an event would not happen, you might not be willing to sell a contract for 3 because your sure gain of 3 is offset by the opportunity or interest cost of the market requirement that you deposit 97 to cover a possible loss. Correcting for this effect would make the “expected” numbers in Table 2 larger than shown for small _b_ .

**A bottom-line conclusion.** To the extent that mathematics can say anything relevant, it says that the fundamental driving feature of the 2012 nominee campaign was that it started without any clear favorite. The subsequent fluctuations were then consistent with what theory predicts. In other words, even if it is actually true that the monthto-month fluctuations in opinion poll standings were greater than usual, we can see no sign that this unduly influenced the smart money being wagered on the prediction market.

**3.6. Another check of theory and data.** A mathematician familiar with martingale theory might look at the Figure 1 chart for Newt Gingrich and wonder if it shows too many fluctuations to be plausibly a martingale. For instance, the chart shows two separate downcrossings from 20 to 10, in December 2011 and in late January 2012. This mathematician has in mind the _upcrossing inequality_ ([ **10** , 11.3]), which limits the likely number of such crossings. We can conduct another check of theory versus data by considering crossings. The relevant theory turns out to be:

_Consider a price interval_ 0 _< a < b <_ 100 _. Then consider an upcoming election with several candidates, and a (prediction market) price for each candidate,_

591

August–September 2013] USING PREDICTION MARKET DATA

March 28, 2013 6:42 a.m. aldous.tex page 592

Mathematical Assoc. of America

American Mathematical Monthly 120:7

_where initially all these prices are below b. Theory says that the expected total number of downcrossings of prices (sum the numbers for each candidate) over the interval_ [ _a, b_ ] _equals (_ 100 − _b)/(b_ − _a)._

To gather data for the interval [10 _,_ 20], we need only look at the five candidates in Table 1 whose maximum price exceeded 20. Their numbers of downcrossings of [10 _,_ 20] were:


So the observed total 7 is in fact close to the theoretical expectation of 8. To derive the formula quoted, we again consider a hypothetical betting system. For each candidate, buy a contract on that candidate if and when their price reaches _b_ . If the price subsequently falls to _a_ , then sell; but buy again if the price reaches _b_ , and continue. Exactly one of these contracts will expire at 100, and the others will be sold at price _a_ , the number _Da,b_ of these others being the number of downcrossings of [ _a, b_ ]. So your gain is _(_ 100 − _b)_ − _Da,b(b_ − _a)_ . The conservation of fairness theorem says the expected gain equals zero, and the equation _E_ [ _(_ 100 − _b)_ − _Da,b(b_ − _a)_ ] = 0 rearranges to _E_ [ _Da,b_ ] = _(_ 100 − _b)/(b_ − _a)_ .

**4. COMPARING PREDICTION MARKETS AND STOCK MARKETS.** We asserted that prediction markets are conceptually simpler than stock markets, so let us finish by making some comparisons between the two.

1. In both markets, the “market price” is by definition the price at which buyers and sellers are willing to trade. Assigning any other interpretation to the price of one share of Apple corporation is a matter of debate—one interpretation from the rationalist school would be that it represents a consensus estimate of discounted future earnings, adjusted by an equity risk premium whose size depends on the risk premiums imputed to alternative investments. In contrast, the interpretation of a prediction market price as the probability of the specified event is much more definite.

2. The price in a prediction market must be between 0 and 100, and will expire at 0 or 100 at a known time determined by an explicit event outside the market.

3. A prediction market is mathematically simpler because we need no empirical data to make the theoretical predictions; for the analogous predictions in a stock market, we need an estimate of variance rate.

4. Compared to stock markets, prediction markets are often thinly traded, suggesting that they will be less efficient and less martingale-like.

5. Standard economic theory asserts that long-term gains in a stock market will exceed long-term rewards in a non-risky investment, because investors’ risk-taking must be rewarded. In this picture, a stock market is a “positive sum game” benefiting both investors and corporations seeking capital; financial intermediaries and speculators earn their share of the gain by providing liquidity and convenient diversification for investors. In contrast, the prediction markets currently in operation are too small to have substantial effect on the real economy, and so are zero-sum, in fact, slightly negative-sum because of transaction costs.

**ACKNOWLEDGMENTS.** Thanks to Mykhaylo Shkolnikov and Andrew Gelman for comments.

592

⃝c THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 120

March 28, 2013 6:42 a.m. aldous.tex page 593

Mathematical Assoc. of America

American Mathematical Monthly 120:7

#### REFERENCES

1. D. J. Aldous, On Chance and Unpredictability: 20 lectures on the links between mathematical probability and the real world, 2012, draft at `http://www.stat.berkeley.edu/~aldous` .

2. S. N. Ethier, _The Doctrine of Chances: Probabilistic Aspects of Gambling_ , Springer-Verlag, Berlin, 2010.

3. C. M. Grinstead, W. P. Peterson, J. L. Snell, _Probability Tales_ , American Mathematical Society, Providence, RI, 2011.

4. C. M. Grinstead and J. L. Snell, _Introduction to Probability_ , 2nd ed., American Mathematical Society, Providence, RI, 1997.

5. S. Karlin, H. M. Taylor, _A First Course in Stochastic Processes_ , 2nd ed., Academic Press, New York, 1975.

6. K. Lange, _Applied Probability_ , 2nd ed., Springer, New York, 2010.

7. J. Pitman, _Probability_ , Springer, New York, 1993.

8. S. Ross, _A First Course in Probability_ , 6th ed., Prentice Hall, Upper Saddle River, NJ, 2002.

9. S. Ross, _Stochastic Processes_ , 2nd ed., Wiley, New York, 1996.

10. D. Williams, _Probability with Martingales_ , Cambridge University Press, Cambridge, 1991.

**DAVID ALDOUS** received his Ph.D. from the University of Cambridge in 1977, and since 1979 has been at U.C. Berkeley. After a career doing technical research within mathematical probability, he is now interested in relating mathematics to real-world data. Outside of work he drinks lattes, reads science fiction and _The Economist_ , drinks wine, walks the dog, and wastes too much time playing _Civilization III_ . _Department of Statistics, 367 Evans Hall, U.C. Berkeley CA 94720-3860 aldous@stat.berkeley.edu_

“I see some parallels between the shifts of fashion in mathematics and in music. In music, the popular new styles of jazz and rock became fashionable a little earlier than the new mathematical styles of chaos and complexity theory. Jazz and rock were long despised by classical musicians, but have emerged as artforms more accessible than classical music to a wide section of the public. Jazz and rock are no longer to be despised as passing fads. Neither are chaos and complexity theory. But still, classical music and classical mathematics are not dead. Mozart lives, and so does Euler. When the wheel of fashion turns once more, quantum mechanics and hard analysis will once again be in style.”

From Freeman Dyson’s review of _Nature’s Numbers_ by Ian Stewart (Basic Books, 1995). (From p. 612 in the _American Mathematical Monthly_ , August–September 1996) —Submitted by Jon Borwein

August–September 2013] USING PREDICTION MARKET DATA

593

---

[← 2.1. A little data.](02-2-1-a-little-data.md) · [Up: contents](index.md)
