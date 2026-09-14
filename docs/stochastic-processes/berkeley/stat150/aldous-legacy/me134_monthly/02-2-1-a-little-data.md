---
title: 2.1. A little data.
source: https://www.stat.berkeley.edu/~aldous/150/me134_monthly.pdf
source_file: sources/berkeley-stat150/aldous-legacy/me134_monthly.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.1. A little data.

**Source:** [`me134_monthly.pdf`](https://www.stat.berkeley.edu/~aldous/150/me134_monthly.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Errors using inadequate data are much less than those using no data at all. [Charles Babbage]

In the baseball match chart in Figure 1, the initial price was near 50; the price at halftime (for baseball we simply used halfway through the match duration) was around 62.

In 30 baseball games from 2008 for which we have the prediction market prices as in Figure 1, and for which the initial price was around 50%, the prices (as percentages) halfway through the match were as follows:


Figure 2 (left) compares the distribution function of this data to the (straight line) distribution function of the uniform distribution.


<!-- Start of picture text -->
1.0 1.0<br>0.5 0.5<br>0 50 100 0 50 100<br>price price<br>probability<br>proportion ofdata<br><!-- End of picture text -->

**Figure 2.** The left diagram shows the empirical distribution function for the baseball data, compared with the uniform distribution. The right diagram shows the theoretical distribution function in the soccer model, again compared with the uniform distribution.

586

⃝c THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 120

March 28, 2013 6:42 a.m. aldous.tex page 587

Mathematical Assoc. of America

American Mathematical Monthly 120:7

The data appears roughly consistent with our halftime price principle. We do not attempt formal tests of significance (“goodness of fit”), which are not informative in our context of an approximate theoretical prediction and limited data.

**Caveat.** The simplicity of the stated halftime price principle depends on the teams being equally good. For unequal teams, the distribution of halftime price will depend on the distribution of the point differences _Zi_ as well as the initial price.

**2.2. A soccer model.** To investigate the effect of discrete points theoretically, take a standard model for soccer, where we suppose that the teams score goals at the times of independent Poisson processes of rates _λ_ 1 and _λ_ 2 per match-duration, with a shoot-out to determine the winner if the score is tied at the end. We can readily adapt the previous calculation to this model. Taking, for instance, _λ_ 1 = _λ_ 2 = 2, Figure 2 (right) shows the distribution function of the halftime price in this model, compared to the (straight line) distribution function of the uniform distribution.

Here, the discrete distribution of the halftime price arises from the discrete distribution of the halftime point difference (likely to be 1 or 0 or −1). This reminds us of other defects of the model. In practice, the prediction market prices depend not only on halftime score, but also on other factors, such as quantitative (e.g., shots on goal) and qualitative assessments of each team’s play in the first half. These vary from match to match and will tend to smooth out the distribution. We conjecture that data on halftime soccer prices for equally-matched teams would, in fact, have a roughly uniform distribution, as with the baseball data above.

**3. PREDICTION MARKETS AND MARTINGALES.** From the very broad field of martingale theory, let us extract several points to emphasize.

1. The notion of your successive _fortunes_ (amounts of money you have) during a sequence of bets at fair odds can be formalized mathematically as a _martingale_ . The gambling interpretation enables proofs of theorems concerning martingales to be expressed in very intuitive language. Then the mathematical definition and theorems can be used (if their hypotheses are satisfied) for random processes arising in contexts completely unrelated to money or gambling.

2. One theorem about martingales says that the overall result of any system for deciding how much and when to bet, within this “fair odds” setting, is simply equivalent to a single bet at fair odds. So we can prove theorems about martingales by inventing hypothetical betting systems and analyzing their possible outcomes.

3. There are plausible reasons to believe that prediction market prices should behave like martingales.

In the next two sections we say a few words about these points. The reader willing to accept them may jump ahead to section 3.4, where we use them to derive the _serious candidates principle_ .

**3.1. Martingales.** For our purposes, a _fair bet_ (more accurately, a bet at fair odds) is one in which the expectation of your monetary gain _G_ equals zero; that is,


where a loss is a negative gain. This ignores issues of utility and risk-aversion, which we won’t consider. In other words, in order for you to receive from me a random payoff

August–September 2013] USING PREDICTION MARKET DATA

587

March 28, 2013 6:42 a.m. aldous.tex page 588

Mathematical Assoc. of America

American Mathematical Monthly 120:7

_X_ in the near future, the “fair” amount you should pay me now is _E_ [ _X_ ], because then your gain (and my loss) _X_ − _E_ [ _X_ ] has expectation zero. If a bet is fair, then doubling the stake and payoff, or multiplying both by −3 to bet in the opposite direction, is again a fair bet.

A formal definition of _martingale_ is a process, that is, a sequence of real-valued random variables, satisfying for each _n_ ≥ 0


This is pretty hard to interpret if you’re not familiar with the probability notation, so we’ll try to explain in words, in the context of gambling. Imagine a person making a sequence of bets, and after the _n_ th bet is settled, his fortune is _xn_ . After placing the next bet but before knowing the outcome, the gain _Gn_ +1 on that bet is random, and (3) says that


i.e., that the expected gain on the bet, given what we currently know, equals zero—the “fair” concept.

A textbook example ([ **6** , ex. 10.2.6]) of a martingale _(X n)_ arising in a context unrelated to money or gambling, concerns the Wright–Fisher model in population genetics. The model shows (without mutation or selection) that the proportion _X n_ of genes in generation _n_ , which are a particular allele, forms a martingale.

Developing the basic mathematics of martingales requires many small steps to introduce and explain notation. Below we give a verbal overview and refer the reader to the advanced textbook [ **10** ] for the mathematics.

Return to the gambling story above, where another gambler’s fortune is the martingale (3). Imagine that you are copying or modifying the bets of this other gambler. A simple way to do so is to copy exactly what the gambler does, but stop after the _T_ th bet is resolved, where _T_ can be chosen on the fly, that is, depending on what has happened so far, but not foreseeing the future. It is perhaps remarkable that there is a precise mathematical definition ([ **10** , 10.8]) of a _stopping time T_ capturing this idea. Following this system, your gain is _X T_ − _x_ 0. The basic form of the _optional sampling theorem_ for martingales ([ **10** , A14]) says that


In the gambling context, this says that despite the fact that you are using a “system” (in this case just some rule for when to stop), your net result is a fair bet. (This theorem and the theorem below have side conditions that are automatically satisfied in our settings.)

As a very general way of copying another gambler, on the _n_ th bet (for each _n_ ) stake some multiple _Hn_ of the other gambler’s stake, where _Hn_ may depend on the past, but cannot foresee the result of the _n_ th bet. Following such a system, your gain _Yn_ is determined by the processes _(X n)_ and _(Hn)_ via the formula _Yn_ +1 − _Yn_ = _Hn(X n_ +1 − _X n)_ and is called a _martingale transform_ ([ **10** , 10.6]) or _discrete stochastic integral_ . The key fact is that _Yn_ behaves as a martingale, and that whenever you choose to stop, your gain _YT_ has expectation zero ([ **10** , 10.7]). The latter result is often referred to via a phrase like “impossibility of gambling systems,” but we would prefer a more positive and informative name, so let us follow [ **2** ] and call it the **conservation of fairness theorem** .

588 ⃝c THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 120

aldous.tex page 589

March 28, 2013 6:42 a.m.

Mathematical Assoc. of America

American Mathematical Monthly 120:7

**3.2. Prediction market prices are approximately martingales.** Definitions and theorems about martingales, as outlined above, can be regarded as a part of pure mathematics, with the references to gambling being just a side story to aid intuition. To now argue that _there are plausible reasons to believe that prediction market prices should behave like martingales_ , we must obviously leave pure mathematics at some point. Indeed, any serious treatment would enter realms of philosophy, psychology, economics, and empirical data. Here, we focus on where exactly pure mathematics ends and other issues begin.

First, recall that general mathematical results about probabilities and conditional probabilities of _events_ can be derived from those for expectations and conditional expectations of _random variables_ , by the device of identifying an event _A_ with its {0 _,_ 1}valued indicator random variable 1 _A_ . Second, outside very simple settings, probabilities depend on “information known at the current time _n_ ”, and the formalization of this notion within the usual axioms of mathematical probability is as a collection (a _sigmaalgebra_ or _sigma-field_ , technically) of events, conventionally denoted by _F n_ , whose outcomes we know. For such a collection _F_ and any event _A_ , we can define the conditional probability _P(A_ | _F )_ as a random variable, extending the notation (1) where the “information” in _F_ is the value of _Y_ . Here _P(A_ | _F )_ is random in the “prior” sense—before we know which events in _F_ actually happened.

A benefit of going through this abstract setup is an easy theorem ([ **10** , 10.4c]) which says that, for any event _A_ and any sequence _F n_ representing “information known at the current time _n_ ,” the conditional probabilities _X n_ := _P(A_ | _F n)_ always form a martingale.

This is about as far as pure mathematics can take us. Concerning probabilities for the kind of interesting future real-world events exemplified by results of sports matches or elections, there is longstanding philosophical debate about whether such probabilities can or should be interpreted as anything other than subjective opinions. But perhaps a more substantial issue is that the way you or I might assess probabilities for such events, though based on something that might be called “information”, is manifestly not the way envisaged in the axiomatic setup; this would involve first setting out all the possible relevant events that (from the standpoint of some past time) might have happened by now or in the future, then assigning probabilities to every combination of events happening and not happening, then looking at which of these events did or did not happen by now, and finally doing the required calculation.

In a real prediction market, different individual participants will assess probabilities somewhat differently, and (among those willing to bet actual money) the market price represents a balance point between willing buyers and willing sellers; we can call this price a “consensus probability”. So the central issue is: _Why should such consensus probabilities change in time in the same way as conditional probabilities, within the axiomatic setup of mathematical probability?_ Typical verbal arguments use an undefined notion of “information” and simply jump over this issue, and we don’t know of any satisfactory argument. So it seems most appropriate to call the assertion that _prediction market prices should behave like martingales_ , a _hypothesis_ , and seek to see if its mathematical consequences are consistent with empirical data. Obviously, this is similar to the _efficient market hypothesis_ in finance, though as discussed in section 4 the setting of prediction markets is conceptually simpler than stock markets.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [3.3. Were there improbably many candidates for the 2012 Republican nomi- →](03-3-3-were-there-improbably-many-candidates-for-the-2012-repub.md)
