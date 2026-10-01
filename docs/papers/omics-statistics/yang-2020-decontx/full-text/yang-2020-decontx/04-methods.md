---
title: Methods
source: https://doi.org/10.1186/s13059-020-1950-6/
source_file: sources/papers/yang-2020-decontx/yang-2020-decontx.jats
licence: CC BY 4.0
route: pandoc-jats
fidelity: high
converted: '2026-10-02'
---

> **Converted source.** `yang-2020-decontx.jats` from [papers/yang-2020-decontx](https://doi.org/10.1186/s13059-020-1950-6/) — papers · yang-2020-decontx, licensed CC BY 4.0. Converted 2026-10-02 from `.jats`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Methods

### Statistical model {#Sec6}

We assume there are *K* known distinct cell populations among the *M* cell samples, where cell *j* has *N*_(*j*) observed transcripts. We denote native expression distribution for cell population *k* as a G-length vector *ϕ*_(*k*). For the notational convenience, we will use ***ϕ***_(−*k*)={*ϕk*′:*k*^(′)≠*k*,*k*^(′)∈{1,2,...,*K*}} to represent gene expressions from all other cell populations other than *k*. Each cell *j* has a parameter *θ*_(*j*) to represent the proportion of transcript counts that are derived from native expression distribution. *θ*_(*j*) is assumed to come from a global beta distribution which leverages the variation of contamination level across all the cells in the dataset, with hyperparameters *a*₁ and *a*₂ a priori. The *t*th transcript *x*_(*jt*) in cell *j* has a hidden state, *y*_(*jt*), which follows a Bernoulli distribution parameterized by *θ*_(*j*) and denotes the transcript’s membership to native expression distribution (*y*_(*jt*)=1) or contamination distribution (*y*_(*jt*)=0). Assuming that transcripts are conditionally independent given hidden state *y*_(*jt*) and cell’s population *z*_(*j*),*x*_(*jt*) follows a multinomial distribution either parameterized by $\phi_{z_{j}}$ denoting native expression or $\mathbf{\phi}_{- z_{j}}$ denoting contamination. The joint posterior distribution can be expressed as:

$$\begin{matrix}
\begin{matrix}
{P\left( \mathbf{X},\mathbf{Z},\mathbf{Y},\mathbf{\theta} \middle| \mathbf{\phi},a_{1},a_{2} \right)} & {= \prod\limits_{j = 1}^{M}p\left( \theta_{j} \middle| a_{1},a_{2} \right)\prod\limits_{t = 1}^{N_{j}}} \\
\left( \left\lbrack {p\left( y_{\textit{jt}} = 1 \middle| \theta_{j} \right) \cdot p\left( x_{\textit{jt}} = g \middle| \phi_{z_{j}} \right)} \right\rbrack^{I(y_{\textit{jt}} = 1)} \right) & \\
{\left( \left\lbrack {p\left( y_{\textit{jt}} = 0 \middle| \theta_{j} \right) \cdot p\left( x_{\textit{jt}} = g \middle| \mathbf{\phi}_{- z_{j}} \right)} \right\rbrack^{I(y_{\textit{jt}} = 0)} \right).} &
\end{matrix}
\end{matrix}$$

To simplify computation work and notation, we assume the contamination distribution *η*_(*k*) is a simple linear combination of ***ϕ***_(−*k*), such that:

$$\begin{matrix}
\eta_{k} & = & {\sum\limits_{k':k' \neq k}w_{k'}\phi_{k'},}
\end{matrix}$$

where the weight $w_{k'}$ is the proportion of native transcripts from cluster *k*^(′) and is calculated using expected values, of which the full definition is given later in inference. DecontX model construction is shown in the plate diagram:

![](https://doi.org/10.1186/s13059-020-1950-6/)

#### Variational inference {#Sec7}

We use variational inference [21] to approximate the posterior probability of our model.

Similar to LDA [14], the following variational distributions are introduced to break down the coupling of ***θ*** and ***Y*** for variational inference:

$$\begin{matrix}
\begin{matrix}
{q\left( \mathbf{\theta},\mathbf{Y} \middle| \mathbf{\gamma},\mathbf{\pi} \right)} & {= \prod\limits_{j = 1}^{M}q\left( \theta_{j} \middle| \gamma_{j} \right)\prod\limits_{t = 1}^{N_{j}}q\left( y_{\textit{jt}} \middle| \pi_{\textit{jt}} \right),}
\end{matrix}
\end{matrix}$$

where the beta parameter *γ*_(*j*)={*γ*_(*j*1),*γ*_(*j*2)} and Bernoulli parameter *π*_(*jt*)={*π*_(*jt*1),*π*_(*jt*2)} are the free variational parameters. *π*_(*jt*) satisfies *π*_(*jt*1)+*π*_(*jt*2)=1, and $q\left( y_{\textit{jt}} \right) = \pi_{\textit{jt}1}^{I(y_{\textit{jt}} = 1)}\pi_{\textit{jt}2}^{I(y_{\textit{jt}} = 0)}$. The variational beta distribution for *θ*_(*j*) is $q\left( \theta_{j} \right) = \frac{\Gamma\left( \gamma_{j1} + \gamma_{j2} \right)}{\Gamma\left( \gamma_{j1} \right)\Gamma\left( \gamma_{j2} \right)}\theta_{j1}^{\gamma_{j1} - 1}\theta_{j2}^{\gamma_{j2} - 1}$.

The need to compute the expectation of the *θ*_(*j*) arises in deriving the variational inference. Using the general fact for exponential family that the derivative of the log normalization factor with respect to the natural parameter is equal to the expectation of the sufficient statistic (log*θ*_(*ji*),*i*∈{1,2} in our beta distribution), we have:

$$\begin{matrix}
\begin{matrix}
{E\left\lbrack \log\theta_{\textit{ji}} \middle| \gamma_{j1},\gamma_{j2} \right\rbrack = \Psi\left( \gamma_{\textit{ji}} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right),i \in \left\{ 1,2 \right\},}
\end{matrix}
\end{matrix}$$

where *Ψ* is the digamma function, the first derivative of the log gamma function.

For simplicity in notation, let us use *Q*={***θ***,***Y***} and *a*={*a*₁,*a*₂}. We begin variational inference by bounding the log-likelihood using Jensen’s inequality.

$$\begin{matrix}
\begin{matrix}
{\log p\left( \mathbf{X},\mathbf{Z} \middle| a,\mathbf{\phi} \right)} & {= \log\int\limits_{Q}p\left( \mathbf{X},\mathbf{Z},\mathbf{\theta},\mathbf{Y} \middle| a,\mathbf{\phi} \right)\textit{dQ}} \\
{= \log\int\limits_{Q}\frac{p\left( \mathbf{X},\mathbf{Z},\mathbf{\theta},\mathbf{Y} \middle| a,\mathbf{\phi} \right)}{q\left( \mathbf{\theta},\mathbf{Y} \middle| \mathbf{\gamma},\mathbf{\pi} \right)}q\left( \mathbf{\theta},\mathbf{Y} \middle| \mathbf{\gamma},\mathbf{\pi} \right))\textit{dQ}} & \\
{\geq \int\limits_{Q}\log\frac{p\left( \mathbf{X},\mathbf{Z},\mathbf{\theta},\mathbf{Y} \middle| a,\mathbf{\phi} \right)}{q\left( \mathbf{\theta},\mathbf{Y} \middle| \mathbf{\gamma},\mathbf{\pi} \right)}q\left( \mathbf{\theta},\mathbf{Y} \middle| \mathbf{\gamma},\mathbf{\pi} \right))\textit{dQ}} & \\
{= E_{Q}\left\lbrack \log p\left( \mathbf{X},\mathbf{Z},\mathbf{\theta},\mathbf{Y} \middle| a,\mathbf{\phi} \right) \right\rbrack - E_{Q}\left\lbrack \log q\left( \mathbf{\theta},\mathbf{Y} \middle| \mathbf{\gamma},\mathbf{\pi} \right) \right\rbrack.} &
\end{matrix}
\end{matrix}$$

Jensen’s inequality provides us with a lower bound on the log likelihood for an arbitrary variational distribution *q*(***θ***,***Y***\|***γ***,***π***).

We then expand the lower bound:

$$\begin{matrix}
\begin{matrix}
{L\left( \mathbf{\gamma},\mathbf{\pi};a,\mathbf{\phi} \right)} & {= E_{Q}\left\lbrack {\log p\left( \mathbf{X},\mathbf{Z},\mathbf{\theta},\mathbf{Y} \middle| a,\mathbf{\phi} \right)} \right\rbrack} \\
{\quad - E_{Q}\left\lbrack {\log q\left( \mathbf{\theta},\mathbf{Y} \middle| \mathbf{\gamma},\mathbf{\pi} \right)} \right\rbrack} & \\
{= E_{Q}\left\lbrack {\log p\left( \mathbf{\theta} \middle| a \right) + \log p\left( \mathbf{Y} \middle| \mathbf{\theta} \right)} \right)} & \\
{\quad\left( {+ \log p\left( \mathbf{X},\mathbf{Z} \middle| \mathbf{Y},\mathbf{\phi} \right)} \right\rbrack} & \\
{\quad - E_{Q}\left\lbrack {\log q\left( \mathbf{\theta} \middle| \mathbf{\gamma} \right) + \log q\left( \mathbf{Y} \middle| \mathbf{\pi} \right)} \right\rbrack.} &
\end{matrix}
\end{matrix}$$

Expanding each term in the lower bound by taking expectation with respect to *q*(***θ***,***Y***\|***γ***,***π***):

$$\begin{matrix}
\begin{matrix}
{E_{Q}\left\lbrack {\log p\left( \mathbf{\theta} \middle| a \right)} \right\rbrack} & {= E_{Q}\left\lbrack {\log\prod\limits_{j = 1}^{M}p\left( \theta_{j} \middle| a \right)} \right\rbrack} \\
{= E_{Q}\left\lbrack {\sum\limits_{j = 1}^{M}\log p\left( \theta_{j} \middle| a \right)} \right\rbrack = \sum\limits_{j = 1}^{M}E_{Q}\left\lbrack {\log p\left( \theta_{j} \middle| a \right)} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}E_{Q}\left\lbrack {\log\Gamma\left( a_{1} + a_{2} \right) - \log\Gamma\left( a_{1} \right)} \right)} & \\
\left( {- \log\Gamma\left( a_{2} \right) + \left( a_{1} - 1 \right)\log\theta_{j1} + \left( a_{2} - 1 \right)\log\theta_{j2}} \right\rbrack & \\
{= \sum\limits_{j = 1}^{M}\left\lbrack {\log\Gamma\left( a_{1} + a_{2} \right) - \left( {\sum\limits_{i = 1}^{2}\log\Gamma\left( a_{i} \right)} \right)} \right)} & \\
\left( {+ \sum\limits_{i = 1}^{2}\left( a_{i} - 1 \right)\left( {\Psi\left( \gamma_{\textit{ji}} \right) - \Psi\left( {\gamma_{j1} + \gamma_{j2}} \right)} \right)} \right\rbrack &
\end{matrix}
\end{matrix}$$

$$\begin{matrix}
\begin{matrix}
{E_{Q}\left\lbrack {\log p\left( \mathbf{Y} \middle| \mathbf{\theta} \right)} \right\rbrack} & {= E_{Q}\left\lbrack {\log\prod\limits_{j = 1}^{M}\prod\limits_{t = 1}^{N_{j}}p\left( y_{\textit{jt}} \middle| \theta_{j} \right)} \right\rbrack} \\
{= E_{Q}\left\lbrack {\sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}\log p\left( y_{\textit{jt}} \middle| \theta_{j} \right)} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}E_{Q}\left\lbrack {\log p\left( y_{\textit{jt}} \middle| \theta_{j} \right)} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}E_{Q}\left\lbrack {y_{\textit{jt}}\log\theta_{j1} + \left( 1 - y_{\textit{jt}} \right)\log\theta_{j2}} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}\left\lbrack {\pi_{\textit{jt}1}\left( {\Psi\left( \gamma_{j1} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right)} \right)} \right)} & \\
\left( {+ \pi_{\textit{jt}2}\left( {\Psi\left( \gamma_{j2} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right)} \right)} \right\rbrack &
\end{matrix}
\end{matrix}$$

$$\begin{matrix}
\begin{matrix}
{E_{Q}\left\lbrack {\log p\left( \mathbf{X},\mathbf{Z} \middle| \mathbf{Y},\mathbf{\phi} \right)} \right\rbrack} & {= E_{Q}\left\lbrack {\log\prod\limits_{j = 1}^{M}\prod\limits_{t = 1}^{N_{j}}p\left( x_{\textit{jt}},z_{j} \middle| y_{\textit{jt}},\phi_{z_{j}},\eta_{z_{j}} \right)} \right\rbrack} \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}E_{Q}\left\lbrack {\log p\left( x_{\textit{jt}},z_{j} \middle| y_{\textit{jt}},\phi_{z_{j}},\eta_{z_{j}} \right)} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}E_{Q}\left\lbrack {\sum\limits_{g = 1}^{G}x_{\textit{jt}}^{g}y_{\textit{jt}}\log\phi_{z_{j},g}} \right)} & \\
{\quad\left( {+ x_{\textit{jt}}^{g}\left( 1 - y_{\textit{jt}} \right)\log\eta_{z_{j},g}} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}\sum\limits_{g = 1}^{G}E_{Q}\left\lbrack {x_{\textit{jt}}^{g}y_{\textit{jt}}\log\phi_{z_{j},g}} \right)} & \\
{\quad\left( {+ x_{\textit{jt}}^{g}\left( 1 - y_{\textit{jt}} \right)\log\eta_{z_{j},g}} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}\sum\limits_{g = 1}^{G}\left\lbrack {x_{\textit{jt}}^{g}\pi_{\textit{jt}1}\log\phi_{z_{j},g}} \right)} & \\
{\quad\left( {+ x_{\textit{jt}}^{g}\pi_{\textit{jt}2}\log\eta_{z_{j},g}} \right\rbrack} &
\end{matrix}
\end{matrix}$$

$$\begin{matrix}
\begin{matrix}
{E_{Q}\left\lbrack {\log q\left( \mathbf{\theta} \middle| \mathbf{\gamma} \right)} \right\rbrack} & {= E_{Q}\left\lbrack {\log\prod\limits_{j = 1}^{M}q\left( \theta_{j} \middle| \gamma_{j} \right)} \right\rbrack} \\
{= E_{Q}\left\lbrack {\sum\limits_{j = 1}^{M}\log q\left( \theta_{j} \middle| \gamma_{j} \right)} \right\rbrack = \sum\limits_{j = 1}^{M}E_{Q}\left\lbrack {\log q\left( \theta_{j} \middle| \gamma_{j} \right)} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}E_{Q}\left\lbrack {\log\Gamma\left( {\gamma_{j1} + \gamma_{j2}} \right) - \log\Gamma\left( \gamma_{j1} \right)} \right)} & \\
{- \log\Gamma\left( \gamma_{j2} \right) + \left( {\gamma_{j1} - 1} \right)\log\theta_{j1}} & \\
\left( {+ \left( {\gamma_{j2} - 1} \right)\log\theta_{j2}} \right\rbrack & \\
{= \sum\limits_{j = 1}^{M}\left\lbrack {\log\Gamma\left( {\gamma_{j1} + \gamma_{j2}} \right) - \left( {\sum\limits_{i = 1}^{2}\log\Gamma\left( \gamma_{\textit{ji}} \right)} \right)} \right)} & \\
\left( {+ \sum\limits_{i = 1}^{2}\left( {\gamma_{\textit{ji}} - 1} \right)\left( \Psi\left( \gamma_{\textit{ji}} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right) \right)} \right\rbrack &
\end{matrix}
\end{matrix}$$

$$\begin{matrix}
\begin{matrix}
{E_{Q}\left\lbrack {\log q\left( \mathbf{Y} \middle| \mathbf{\pi} \right)} \right\rbrack} & {= E_{Q}\left\lbrack {\log\prod\limits_{j = 1}^{M}\prod\limits_{t = 1}^{N_{j}}q\left( y_{\textit{jt}} \middle| \pi_{\textit{jt}} \right)} \right\rbrack} \\
{\quad = E_{Q}\left\lbrack {\sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}\log q\left( y_{\textit{jt}} \middle| \pi_{\textit{jt}} \right)} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}E_{Q}\left\lbrack {\log q\left( y_{\textit{jt}} \middle| \pi_{\textit{jt}} \right)} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}E_{Q}\left\lbrack {y_{\textit{jt}}\log\pi_{\textit{jt}1} + \left( 1 - y_{\textit{jt}} \right)\log\pi_{\textit{jt}2}} \right\rbrack} & \\
{= \sum\limits_{j = 1}^{M}\sum\limits_{t = 1}^{N_{j}}\left\lbrack {\pi_{\textit{jt}1}\log\pi_{\textit{jt}1} + \pi_{\textit{jt}2}\log\pi_{\textit{jt}2}} \right\rbrack.} &
\end{matrix}
\end{matrix}$$

We then maximize the lower bound with respect to the variational parameters ***γ*** and ***π***.

First we maximize the lower bound with respect to ***π***. Since (*π*_(*jt*))s are independent, for *t*∈{1,2,...,*N*_(*j*)}, we isolate the terms that contains *π*_(*jt*). Lagrangian multiplier is added due to the constraint *π*_(*jt*1)+*π*_(*jt*2)=1. We substituted $x_{\textit{jt}}^{g}\pi_{\textit{jt}1}\log\phi_{z_{j},g}$ and $x_{\textit{jt}}^{g}\pi_{\textit{jt}2}\log\eta_{z_{j},g}$ from Eq. 9 with $\pi_{\textit{jt}1}\log\phi_{z_{j},g}$ and $\pi_{\textit{jt}2}\log\eta_{z_{j},g}$, respectively, since $x_{\textit{jt}}^{g} = I\left( x_{\textit{jt}} = g \right)$ and is observed:

$$\begin{matrix}
\begin{matrix}
L_{\lbrack\pi_{\textit{jt}}\rbrack} & {= \left\lbrack {\pi_{\textit{jt}1}\left( {\Psi\left( \gamma_{j1} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right)} \right)} \right)} \\
{\quad\left( {+ \pi_{\textit{jt}2}\left( {\Psi\left( \gamma_{j2} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right)} \right)} \right\rbrack} & \\
{\quad + \left\lbrack {\pi_{\textit{jt}1}\log\phi_{z_{j},g} + \pi_{\textit{jt}2}\log\eta_{z_{j},g}} \right\rbrack} & \\
{\quad - \left\lbrack {\pi_{\textit{jt}1}\log\pi_{\textit{jt}1} + \pi_{\textit{jt}2}\log\pi_{\textit{jt}2}} \right\rbrack} & \\
{\quad - \lambda\left( \pi_{\textit{jt}1} + \pi_{\textit{jt}2} - 1 \right).} &
\end{matrix}
\end{matrix}$$

Taking derivative with respect to *π*_(*jt*1), we obtain:

$$\begin{matrix}
\begin{matrix}
\frac{\partial L}{\partial\pi_{\textit{jt}1}} & {= \left( {\Psi\left( \gamma_{j1} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right)} \right)} \\
{\quad + \log\phi_{z_{j},g} - \log\pi_{\textit{jt}1} - \lambda - 1.} &
\end{matrix}
\end{matrix}$$

Setting this derivative to zero yields the maximizing value of the variational parameter *π*_(*jt*1):

$$\begin{matrix}
\begin{matrix}
{\pi_{\textit{jt}1} \propto \phi_{z_{j},g}\exp\left( \Psi\left( \gamma_{j1} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right) \right).}
\end{matrix}
\end{matrix}$$

Similarly, we could have *π*_(*jt*2):

$$\begin{matrix}
\begin{matrix}
{\pi_{\textit{jt}2} \propto \eta_{z_{j},g}\exp\left( \Psi\left( \gamma_{j2} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right) \right).}
\end{matrix}
\end{matrix}$$

Next, we maximize the lower bound with respect to ***γ***. Since (*γ*_(*j*))s are independent for *j*∈1,2,...,*M*, each *γ*_(*j*) can be estimated separately. We isolate the terms that contain *γ*_(*j*).

$$\begin{matrix}
\begin{matrix}
L_{\lbrack\gamma_{j}\rbrack} & {= \sum\limits_{i = 1}^{2}\left( a_{i} - 1 \right)\left( {\Psi\left( \gamma_{\textit{ji}} \right) - \Psi\left( {\gamma_{j1} + \gamma_{j2}} \right)} \right)} \\
{+ \sum\limits_{t = 1}^{N_{j}}\left\lbrack {\pi_{\textit{jt}1}\left( {\Psi\left( \gamma_{j1} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right)} \right)} \right)} & \\
\left( {\quad + \pi_{\textit{jt}2}\left( {\Psi\left( \gamma_{j2} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right)} \right)} \right\rbrack & \\
{- \left\lbrack {\log\Gamma\left( {\gamma_{j1} + \gamma_{j2}} \right) - \left( {\sum\limits_{i = 1}^{2}\log\Gamma\left( \gamma_{\textit{ji}} \right)} \right)} \right)} & \\
{\left( {+ \sum\limits_{i = 1}^{2}\left( {\gamma_{\textit{ji}} - 1} \right)\left( \Psi\left( \gamma_{\textit{ji}} \right) - \Psi\left( \gamma_{j1} + \gamma_{j2} \right) \right)} \right\rbrack.} &
\end{matrix}
\end{matrix}$$

Taking derivative with respect to *γ*_(*ji*), we obtain:

$$\begin{matrix}
\begin{matrix}
\frac{\partial L}{\partial\gamma_{\textit{ji}}} & {= \Psi'\left( \gamma_{\textit{ji}} \right)\left( {a_{i} + \sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1} - \gamma_{j1}} \right) - \Psi'\left( \gamma_{j1} + \gamma_{j2} \right)} \\
{\quad\left( {a_{1} + \sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1} - \gamma_{j1} + a_{2} + \sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}2} - \gamma_{j2}} \right),} &
\end{matrix}
\end{matrix}$$

where *Ψ*^(′) is the derivative of the digamma function. Setting this derivative to zero yields a maximum at:

$$\begin{matrix}
\begin{matrix}
{\gamma_{\textit{ji}} = a_{i} + \sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1},i \in \left\{ 1,2 \right\}.}
\end{matrix}
\end{matrix}$$

Finally, we move forward to estimating ***ϕ*** and *a*, and to update ***η***.

To maximize with respect to *ϕ*_(*k*), we isolate terms and add Lagrangian multiplier due to the constraint $\sum\limits_{g = 1}^{G}\phi_{\textit{kg}} = 1$:

$$\begin{matrix}
\begin{matrix}
L_{\lbrack\phi_{k}\rbrack} & {= \sum\limits_{j:z_{j} = k}\sum\limits_{t = 1}^{N_{j}}\sum\limits_{g = 1}^{G}x_{\textit{jt}}^{g}\pi_{\textit{jt}1}\log\phi_{\textit{kg}} - \lambda\left( \sum\limits_{g = 1}^{G}\phi_{\textit{kg}} - 1 \right).}
\end{matrix}
\end{matrix}$$

Taking the derivative with respect to *ϕ*_(*kg*) and set it to zero, we get:

$$\begin{matrix}
\begin{matrix}
{\phi_{\textit{kg}} \propto \sum\limits_{j:z_{j} = k}\sum\limits_{t = 1}^{N_{j}}x_{\textit{jt}}^{g}\pi_{\textit{jt}1}.}
\end{matrix}
\end{matrix}$$

The weight $w_{k'}$ is the proportion of native transcripts from cluster *k*^(′) and is calculated using expected values:

$$\begin{matrix}
\begin{matrix}
{w_{k'} = \frac{\sum\limits_{k':k' \neq k}\left( {\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}} \right)}{\sum\limits_{j:z_{j} \neq k}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}}.}
\end{matrix}
\end{matrix}$$

Hence, we have our updated $\eta_{k'g}$ as:

$$\begin{matrix}
\begin{matrix}
\eta_{\textit{kg}} & {= \frac{\sum\limits_{k':k' \neq k}\left( {\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}} \right)\phi_{k'g}}{\sum\limits_{j:z_{j} \neq k}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}}} \\
{= \frac{1}{\sum\limits_{j:z_{j} \neq k}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}}\sum\limits_{k':k' \neq k}\left( {\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}} \right)\phi_{k'g}} & \\
{= \frac{1}{\sum\limits_{j:z_{j} \neq k}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}}\sum\limits_{k':k' \neq k}\left( {\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}} \right)} & \\
{\quad\frac{\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}x_{\textit{jt}}^{g}\pi_{\textit{jt}1}}{\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}}} & \\
{= \frac{1}{\sum\limits_{j:z_{j} \neq k}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}}\sum\limits_{k':k' \neq k}\left( {\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}x_{\textit{jt}}^{g}\pi_{\textit{jt}1}} \right)} & \\
{= \frac{\sum\limits_{k':k' \neq k}\left( {\sum\limits_{j:z_{j} = k'}\sum\limits_{t = 1}^{N_{j}}x_{\textit{jt}}^{g}\pi_{\textit{jt}1}} \right)}{\sum\limits_{j:z_{j} \neq k}\sum\limits_{t = 1}^{N_{j}}\pi_{\textit{jt}1}}.} &
\end{matrix}
\end{matrix}$$

To maximize with respect to *a*, we isolate terms and get:

$$\begin{matrix}
\begin{matrix}
L_{\lbrack a\rbrack} & {= \sum\limits_{j = 1}^{M}\left\lbrack {\log\Gamma\left( a_{1} + a_{2} \right) - \left( {\sum\limits_{i = 1}^{2}\log\Gamma\left( a_{1} \right)} \right)} \right)} \\
{\quad\left( {+ \sum\limits_{i = 1}^{2}\left( a_{i} - 1 \right)\left( {\Psi\left( \gamma_{\textit{ji}} \right) - \Psi\left( {\gamma_{j1} + \gamma_{j2}} \right)} \right)} \right\rbrack.} &
\end{matrix}
\end{matrix}$$

A Newton iteration can be used to find the maximal point *a* [22], which requires both the first and second derivatives of *L*_([*a*]). The first derivative, gradient ∇*L*, and the second derivative, Hessian matrix *H,* are:

$$\begin{matrix}
\begin{matrix}
{\nabla L_{i} = \frac{\partial L_{\lbrack a\rbrack}}{\partial a_{i}}} & {= \sum\limits_{j = 1}^{M}\left( {\Psi\left( a_{1} + a_{2} \right) - \Psi\left( a_{i} \right)} \right)} \\
{\quad\left( {+ \Psi\left( \gamma_{\textit{ji}} \right) - \Psi\left( {\gamma_{j1} + \gamma_{j2}} \right)} \right)} &
\end{matrix}
\end{matrix}$$

$$\begin{matrix}
\begin{matrix}
{H_{\textit{ii}} = \frac{\partial^{2}L_{\lbrack a\rbrack}}{\partial a_{i}^{2}} = M\left( {\Psi'\left( a_{1} + a_{2} \right) - \Psi\left( a_{i} \right)} \right),i \in \left\{ 1,2 \right\}} \\
{H_{\textit{ij}} = \frac{\partial^{2}L_{\lbrack a\rbrack}}{\partial a_{i}\partial a_{j}} = M\Psi'\left( a_{1} + a_{2} \right),j \neq {i.}}
\end{matrix}
\end{matrix}$$

One Newton step is then:

$$\begin{matrix}
\begin{matrix}
{a^{\textit{new}} = a^{\textit{old}} - H^{- 1}\nabla{L.}}
\end{matrix}
\end{matrix}$$

### Analysis of sorted human-mouse mixture single-cell dataset {#Sec8}

A mixture of fresh frozen human (HEK293T) and mouse (NIH3T3) cells were sequenced together in 10X Genomics Chromium. This data is available at 10X Genomics website [23]. A total of 6164 human cells, 5915 mouse cells, and 741 multiplets were detected by CellRanger. Excluding multiplets, 12,079 cells with CellRanger-predicted cell type were used to estimate contamination using DecontX.

### Analysis of sorted PBMCs single-cell datasets {#Sec9}

Nine publicly available PBMC datasets totalling of 84,432 cells [24] were obtained from 10X Genomics. Each dataset consisted of a population of cells that were isolated with flow cytometry based on expression of a predefined protein marker. Cell populations included progenitor cells(CD34+), monocytes (CD14+), B cells (CD19+), natural killer cells (CD56+), helper T cells (CD4+), regulatory T cells (CD4+/CD25+), native T cells (CD4+/CD45RA+/CD25 −), naive cytotoxic T cells (CD8+/CD45RA+), and cytotoxic T cells (CD8+). A total of 7363 genes which contained at least 3 counts across 3 cells were included in the analysis. DecontX used cell label by flow cytometry to estimate contamination. Celda [17] was used to identify 76 gene modules and 21 cell clusters, including 8 clusters predominantly expressing T cell markers, 2 clusters predominantly expressing natural killer cell markers, 2 clusters predominantly expressing B cell markers, 2 clusters predominantly expressing monocyte markers, and 7 clusters predominantly expressing CD34 progenitor cell markers. These computationally inferred cell type labels were used in downstream analyses that examined the percentage of cells that express various marker genes. Using computationally derived cell clustered mitigated instances where a cell was improperly sorted and labeled by flow cytometry as belonging to one population when in fact it was transcriptionally similar to another population.

### Analysis of the 4K PBMC single-cell dataset {#Sec10}

A total of 4340 PBMCs [25] from a healthy donor were sequenced in a single channel of the 10X Genomics Chromium. A total of 4529 genes which contained at least 3 counts across 3 cells were included in the analysis. Nineteen cell clusters and 150 gene modules were identified with Celda [17]. Cell clusters 2 and 3 were classified as B cells (MS4A1+); cell clusters 5, 6, 7, 8, 9, and 11 were classified as T cells (CD3D+/CD3E+); cell clusters 13 and 14 were identified as LYZ+ monocyte group; cell cluster 15 was identified as FCGR3A+ monocyte group; cell cluster 10 was identified as NKG7+ and GNLY+ NK cell group; cell clusters 18 and 19 were identified as FCER1A+ dendritic cell group; cell cluster 4 was identified as IRF7+ and IRF8+ plasmacytoid dendritic cell group; cell cluster 16 was identified as PPBP+ megakaryocytes; cell cluster 1 was identified as IGHG1+ and IGHG2+ plasma cell group; cell cluster 12 was identified as CD34+ cell group; cell cluster 17 is likely to be multiplets for it has shown IL7R, CD3D, and CD14 markers. DecontX used Celda-estimated cluster label to estimate contamination.

### Analysis of benchmark datasets {#Sec11}

Data were generated as previously described [7] and is available at their github repository [26]. Briefly, five human lung adenocarcinoma cell lines (HCC827, H1975, A549, H838, and H2228) were cultured separately and the same batch was processed in two different ways to create three datasets. For the two single-cell datasets, single cells from three or five cell lines were mixed together, with libraries generated using three different protocols (10X Chromium, Drop-seq, CEL-seq2). For the mixRNA datasets, RNA was extracted in bulk from three cell lines (HCC827, H1975, and H2228), mixed in seven different proportions, and diluted to single-cell equivalent amounts, with libraries generated using either CEL-seq2 or SORT-seq protocols. Available cell clusters from the paper estimated by Demuxlet were used to estimate contamination by DecontX on both single-cell datasets; all cells were included for DecontX analysis. For the mixRNA datasets, we assign the cell cluster of each pseudo-cell being the predominant cell line that has contributed more than 50% of the total mRNA.

### Analysis of three tissues across two 10X Chromium platforms {#Sec12}

Three tissue types (mouse brain, mouse heart, PBMC from healthy donor) were profiled using two different 10X 3’ protocols (V2, V3). The six datasets are available at 10X Genomics [27–32]. A total of 1206 cells were detected in BrainV2, 1301 in BrainV3, 712 in HeartV2, 1011 in HeartV3, 996 in PBMCV2, and 1222 in PBMCV3. Genes which contained at least 3 counts across 3 cells were included in the analysis. Automatic clustering is performed on each dataset. Specifically, for each dataset, genes were collapsed into 100 gene modules using Celda [17], UMAP [33] was used on the 100 gene modules to define spacial similarity between cells on a reduced two-dimensional space, and then, density-based spatial clustering of applications with noise [34] (DBSCAN) was used with parameter epsilon as 1 to define cell clusters.

## Supplementary information {#sec13}

**Additional file 1** Supplementary figures, including Figure S1–S8.

**Additional file 2** Review history.

## Acknowledgements {#ack1}

We thank Carter Merenstein, Ke Xu, and Xinyi Shi for helpful suggestions during the analysis.

### Review history {#d29e8903}

The review history is available as Additional file 2.

## Authors’ contributions {#notes1}

JDC conceived the project. JDC, SY, and MY developed the model. SY and YK performed the analysis. SY, JDC, and MY wrote the manuscript. SC and ZW assisted in the software development. SY, JDC, MY, YK, SC, ZW, and EJ reviewed the manuscript.

## Funding {#notes2}

This work was funded by the National Library of Medicine (NLM) R01LM013154-01 (JDC, MY) and Informatics Technology for Cancer Research (ITCR) 1U01 [CA220413](https://www.ncbi.nlm.nih.gov/nuccore/CA220413)- 01 (WEJ).

## Availability of data and materials {#notes3}

The human-mouse cell mixture data that support the findings of this study are available from 10X Genomics [23].

The sorted PBMC data that support the findings of this study are included in this published article *Massively parallel digital transcriptional profiling of single cells* [5]. The data are available under accession number SRP073767 in the Short Read Archive, and are also available at 10X Genomics [24].

The PBMC 4K data that support the findings of this study are available from 10X Genomics [25].

The benchmark data that support the findings of this study are included in this published article *Benchmarking Single Cell RNA-sequencing analysis pipelines using mixture control experiments* [7] and its supplementary information files, and also available at their github repository [26].

The six datasets (BrainV2, BrainV3, HeartV2, HeartV3, PBMCV2, and PBMCV3) that support the findings of this study are available at 10X Genomics [27–32].

DecontX is freely available at https://github.com/campbio/celda under MIT license. The source code used in the manuscript is deposited at Zenodo and github [35].

## Ethics approval and consent to participate {#notes4}

Not applicable.

## Consent for publication {#notes5}

Not applicable.

## Competing interests {#notes6}

The authors declare that they have no competing interests.

## Footnotes {#fn-group1}

## Contributor Information {#_ci93_}

Shiyi Yang, Email: syyang@bu.edu.

Sean E. Corbett, Email: scorbett@bu.edu

Yusuke Koga, Email: ykoga07@bu.edu.

Zhe Wang, Email: zhe@bu.edu.

W Evan Johnson, Email: wej@bu.edu.

Masanao Yajima, Email: yajima@bu.edu.

Joshua D. Campbell, Email: camp@bu.edu

## Supplementary information {#sec15}

**Supplementary information** accompanies this paper at 10.1186/s13059-020-1950-6.

## References {#Bib1}

---

[← Discussion](03-discussion.md) · [Up: contents](index.md) · [Associated Data →](05-associated-data.md)
