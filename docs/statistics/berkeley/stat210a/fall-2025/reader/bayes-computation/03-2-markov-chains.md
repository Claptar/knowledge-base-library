---
title: 2 Markov chains
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-computation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Markov chains

**Source:** [`reader/bayes-computation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

## <span class="header-section-number">2.1</span> Markov chains and stationarity {.anchored number="2.1" anchor-id="markov-chains-and-stationarity"}

A Markov chain is a sequence of random variables <span class="math inline">\$X^{(0)},X^{(1)},X^{(2)},\\ldots\$</span> the distribution of <span class="math inline">\$X^{(t+1)}\$</span> given <span class="math inline">\$X^{(0)},\\ldots,X^{(t)}\$</span> depends on <span class="math inline">\$X^{(t)}\$</span> alone. A Markov chain is sometimes called *memoryless*: at “time” <span class="math inline">\$t\$</span>, the only thing we need to know about the entire history of the chain up until <span class="math inline">\$t\$</span> is the present state <span class="math inline">\$X^{(t)}\$</span>.

In particular, a **stationary Markov chain** with transition kernel <span class="math inline">\$Q(y \\mid x)\$</span> and initial distribution <span class="math inline">\$\\pi\_0(x)\$</span> (on state space <span class="math inline">\$\\cX\$</span> with base measure <span class="math inline">\$\\mu\$</span>) is a sequence of random variables <span class="math inline">\$X^{(0)},X^{(1)},X^{(2)},\\ldots\$</span> where <span class="math inline">\$X^{(0)}\\sim \\pi\_0\$</span> and <span class="math inline">\$X^{(t+1)}\$</span> given <span class="math inline">\$X^{(0)},\\ldots,X^{(t)}\$</span> is distributed as <span class="math inline">\$Q(\\cdot\\mid X^{(t)})\$</span>.

Fixing <span class="math inline">\$x\$</span>, we can think of the function <span class="math inline">\$Q(\\cdot \\mid x)\$</span> as the probability density of <span class="math inline">\$X^{(t+1)}\$</span> given <span class="math inline">\$X^{(t)}=x\$</span>.

The joint density of the chain up to finite time <span class="math inline">\$T\$</span> can therefore be factored as <span class="math inline">\$\\pi\_0(x^{(0)})\\prod\_{t=0}^{T-1} Q(x^{(t+1)}\\mid x^{(t)})\$</span>, so a Markov chain is thus a special kind of graphical model wherein there is an arrow pointing from each variable to the next, but there are no other arrows.

We can calculate the transition probabilities after two steps integrating over the probability of all two step paths <span class="math display">\\$$ Q^2(y \\mid x) = \\int\_{\\cX} Q(y\\mid z)Q(z \\mid x)\\,d\\mu(z), \\$$</span> and more generally the transition probabilities after <span class="math inline">\$n\$</span> steps as <span class="math inline">\$Q^n(y \\mid x) = \\int\_{\\cX} Q(y\\mid z)Q^{n-1}(z \\mid x)\\,d\\mu(z)\$</span>. Then the distribution of <span class="math inline">\$X^{(t)}\$</span> is <span class="math display">\\$$ \\pi\_t(y) = \\int\_{\\cX} Q^t(y\\mid x)\\pi\_0(x)\\,d\\mu(x). \\$$</span>

We say a distribution <span class="math inline">\$\\pi\$</span> is **stationary** for <span class="math inline">\$Q\$</span> if this operation leaves <span class="math inline">\$\\pi\$</span> fixed: <span class="math display">\\$$ \\pi(y) = \\int\_\\cX Q(y\\mid x)\\pi(x)\\,d\\mu(x). \\$$</span> A sufficient (but not necessary) condition for <span class="math inline">\$\\pi\$</span> to be stationary for <span class="math inline">\$Q\$</span> is **detailed balance**: <span class="math display">\\$$ \\pi(x)Q(y\\mid x) = \\pi(y)Q(x\\mid y), \\quad \\text{ for all } x, y\\in \\cX. \\$$</span> The proof is one line: if we have detailed balance, then <span class="math display">\\$$ \\int Q(y\\mid x)\\pi(x)\\,d\\mu(x) = \\pi(y)\\int Q(x\\mid y)\\,d\\mu(x) = \\pi(y), \\$$</span> since <span class="math inline">\$Q(x \\mid y)\$</span> is a probability density.

## <span class="header-section-number">2.2</span> Convergence {.anchored number="2.2" anchor-id="convergence"}

The idea of Markov chain Monte Carlo methods is to devise a Markov chain transition kernel <span class="math inline">\$Q\$</span> whose stationary distribution <span class="math inline">\$\\pi\$</span> is the posterior distribution that we want to sample from. One reason this works is that Markov chains tend to converge over time to their stationary distributions, under mild conditions. Denote the transition kernel for <span class="math inline">\$2\$</span> steps as \$Q^2(y x) =

**Theorem (Markov chain convergence):** Suppose <span class="math inline">\$X^{(0)},X^{(1)},\\ldots\$</span> is a Markov chain with transition kernel <span class="math inline">\$Q\$</span> and stationary distribution <span class="math inline">\$\\pi\$</span>. If additionally the chain is: 1. Irreducible: for all <span class="math inline">\$x,y\\in\\cX\$</span>, there is some <span class="math inline">\$n\$</span> for which <span class="math inline">\$Q^n(y \\mid x)&gt;0\$</span>, and 2. Aperiodic: for all <span class="math inline">\$x\\in\\cX\$</span>, the greatest common divisor of <span class="math inline">\$\\{n:\\; Q^n(x \\mid x)&gt;0\\}\$</span> is <span class="math inline">\$1\$</span>. Then, regardless of the initial distribution <span class="math inline">\$\\pi\_0\$</span>, <span class="math inline">\$\\pi\_t \\to \\pi\$</span> in total variation distance as <span class="math inline">\$t\\to\\infty\$</span>, meaning <span class="math display">\\$$ \\\|\\pi\_t-\\pi\\\|\_{\\text{TV}} = \\sup\_{A \\in \\cX} \|\\pi\_t(A)-\\pi(A)\| \\to 0 \\$$</span> Intuitively, the irreducibility condition ensures the sample space is not split into “parallel universes” that don’t communicate with each other, and the aperiodic condition ensures we are not regularly cycling through subsets of the sample space. Aperiodicity is especially easy to fix, just by making a new transition kernel that flips a coin to choose randomly between transitioning according to <span class="math inline">\$Q\$</span> and staying in place (check for yourself that this does not change the stationary distribution).

Caution

Note this theorem applies to discrete sample spaces; for continuous sample spaces it is a bit more complicated to state the two conditions. They go through without modification if we assume <span class="math inline">\$Q\$</span> is continuous, but more generally we might have to worry about measure-zero pathologies of the kind that we have been ignoring all semester.

*Proof sketch (discrete case):* Let <span class="math inline">\$Y^{(0)},Y^{(1)},\\ldots\$</span> be an independent Markov chains with initial distribution <span class="math inline">\$\\pi\$</span> and transition kernel <span class="math inline">\$Q\$</span>. We construct a probabilistic *coupling* between the two chains.

Let <span class="math inline">\$\\tau = \\min\\{t:\\; X^{(t)}=Y^{(t)}\\}\$</span> and define the *coupled chain* that starts as <span class="math inline">\$X^{(t)}\$</span> but then switches to <span class="math inline">\$Y^{(t)}\$</span> after they meet. <span class="math display">\\$$ Z^{(t)} = \\begin{cases} X^{(t)} & \\text{ if } t\\leq\\tau\\\\ Y^{(t)} & \\text{ if } t &gt; \\tau\\end{cases} \\$$</span> It can be shown that <span class="math inline">\$Z\$</span> is also a Markov chain with transition kernel <span class="math inline">\$Q\$</span> and transition kernel <span class="math inline">\$\\pi\_0\$</span>, so <span class="math inline">\$Z^{(t)} \\sim \\pi\_t\$</span>. Moreover, <span class="math display">\\$$ \\\|\\pi\_t-\\pi\\\|\_{\\text{TV}} = \\sup\_{A \\subseteq \\cX} \|\\PP(Z^{(t)}\\in A) - \\PP(Y^{(t)}\\in A)\| \\leq \\PP(\\tau &gt; t), \\$$</span> since <span class="math inline">\$Z^{(t)}=Y^{(t)}\$</span> on the event <span class="math inline">\$\\{\\tau \\leq t\\}\$</span>. The key step, which we omit here for brevity, is that the irreducibility and aperiodicity conditions, plus the existence of a stationary distribution <span class="math inline">\$\\pi\$</span>, guarantee that <span class="math inline">\$\\tau &lt; \\infty\$</span> with probability <span class="math inline">\$1\$</span>, so <span class="math inline">\$\\PP(\\tau&gt;t)\\to 0\$</span>. <span class="math inline">\$\\blacksquare\$</span>

The important implication of this theorem from our perspective is that, if we can only find an irreducible and aperiodic transition kernel <span class="math inline">\$Q\$</span> on the state space <span class="math inline">\$\\Theta\$</span>, whose stationary distribution is the posterior <span class="math inline">\$\\lambda(\\theta \\mid x)\$</span>, we will be able to sample from the posterior by running the Markov chain <span class="math inline">\$\\theta^{(0)},\\theta^{(1)},\\ldots\$</span> from any initialization <span class="math inline">\$\\theta^{(0)}\$</span>.

---

[← 1 Why Bayesian computation is difficult](02-1-why-bayesian-computation-is-difficult.md) · [Up: contents](index.md) · [3 The Gibbs sampler →](04-3-the-gibbs-sampler.md)
