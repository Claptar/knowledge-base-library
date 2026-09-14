---
title: Complete Block Design Example
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/06-power-calculations/lab.tex
source_file: sources/berkeley-stat158/spring-2026/labs/06-power-calculations/lab.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Complete Block Design Example

**Source:** [`labs/06-power-calculations/lab.tex`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/06-power-calculations/lab.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

We now look at an example calculation for a sample Complete Blocked Design $CB[1]$ experiment in `R`. Note that we use fixed Block effects here as opposed to random effects.

####  {#section .unnumbered}

Step 1: Linear Model and Data Generating Process<span id="step-1-linear-model-and-data-generating-process" label="step-1-linear-model-and-data-generating-process"></span>

We first identify the linear model associated with our design as follows:

$$Y_i = \mu + \alpha_{j(i)} + \beta_{k(i)} + \epsilon_i$$

$$\hat{\mu} = \bar{Y}$$

$$\hat{\alpha}_{j(i)} = \bar{Y}_{j(i)} - \hat{\mu}$$

$$\hat{\beta}_{k(i)} = \bar{Y}_{k(i)} - \hat{\mu}$$

**Where:**

- $Y_i$ is the response for observation $i$;

- $\mu$ is the overall (grand) mean;

- $\alpha_{j(i)}$ is the factor effects, where $j(i)$ indicates the factor level of the $i$th observation;

- $\beta_{k(i)}$ are block effects, where $k(i)$ indicates the block the $i$th observation belongs to;

- $\epsilon_i$ is the error term, $\epsilon_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)$.

$\bar{Y}, \bar{Y}_{j(i)}, \bar{Y}_{k(i)}$ are sample means.
Write this out in R as follows:

<span style="color: 0.37,0.37,0.37">\# Data Generating Process outline</span>

<span style="color: 0.37,0.37,0.37">\# Write out the linear model as an R function</span>

<span style="color: 0.00,0.23,0.31">generate\_Y </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.00,0.23,0.31">**function**</span><span style="color: 0.00,0.23,0.31">(mu, alpha, beta, sigma\_sq, j, k) {</span> <span style="color: 0.37,0.37,0.37">\# j: n length vector of factor level indices</span> <span style="color: 0.37,0.37,0.37">\# k: n length vector of block indices</span>

<span style="color: 0.00,0.23,0.31"> n </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">length</span><span style="color: 0.00,0.23,0.31">(j)</span>

<span style="color: 0.28,0.35,0.67">set.seed</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.68,0.00,0.00">42</span><span style="color: 0.00,0.23,0.31">)</span> <span style="color: 0.00,0.23,0.31"> epsilon </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">rnorm</span><span style="color: 0.00,0.23,0.31">(n, </span><span style="color: 0.40,0.45,0.13">mean =</span> <span style="color: 0.68,0.00,0.00">0</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">sd =</span> <span style="color: 0.28,0.35,0.67">sqrt</span><span style="color: 0.00,0.23,0.31">(sigma\_sq))</span>

<span style="color: 0.00,0.23,0.31"> Y </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> mu </span><span style="color: 0.37,0.37,0.37">+</span><span style="color: 0.00,0.23,0.31"> alpha$$j$$ </span><span style="color: 0.37,0.37,0.37">+</span><span style="color: 0.00,0.23,0.31"> beta$$k$$ </span><span style="color: 0.37,0.37,0.37">+</span><span style="color: 0.00,0.23,0.31"> epsilon</span>

<span style="color: 0.28,0.35,0.67">return</span><span style="color: 0.00,0.23,0.31">(Y)</span> <span style="color: 0.00,0.23,0.31">}</span>

####  {#section-1 .unnumbered}

Step 2: Choosing Parameters<span id="step-2-choosing-parameters" label="step-2-choosing-parameters"></span>

We now choose the relevant parameters for our power calculation. Set effect sizes to the smallest value that would be scientifically meaningful to you. For instance, . You may also choose these from previous literature etc. Keep in mind that your size should match conditions on these parameters (sum to zero etc)!

Next, use an estimate of the error variance $\sigma^2$, ideally from your pilot data or dry run. Set the sample size as a meaningful sample size that you feasibly hope to attain or collect while conducting your experiment.

For the purposes of our example we stick to two factor levels and two blocks, i.e 4 observations in total.

<span style="color: 0.37,0.37,0.37">\# Defining parameter values</span>

<span style="color: 0.00,0.23,0.31">mu </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.00,0.23,0.31">alpha </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">c</span><span style="color: 0.00,0.23,0.31">(,) </span><span style="color: 0.37,0.37,0.37">\# Fill in levels of alpha: they should sum to zero!</span> <span style="color: 0.00,0.23,0.31">beta </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">c</span><span style="color: 0.00,0.23,0.31">(,) </span><span style="color: 0.37,0.37,0.37">\# Fill in levels of beta: they should sum to zero!</span>

<span style="color: 0.00,0.23,0.31">sigma\_sq </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.00,0.23,0.31">n </span><span style="color: 0.00,0.23,0.31">&lt;-</span>

Note in particular the role of $\sigma^2$ in the power calculations. Once you finish steps 1-4, remember to come back and double the value of $\sigma^2$. What do you see?

####  {#section-2 .unnumbered}

Step 3: Simulating a dataset and Inference<span id="step-3-simulating-a-dataset-and-inference" label="step-3-simulating-a-dataset-and-inference"></span>

We now simulate a dataset using the linear data-generating process and the parameters defined above. We can do this simply as follows.

Fill in the missing steps, in particular choose $j$ and $k$ for each observation and store it in the vectors. Sketching out a table for your experiment may be useful here!

<span style="color: 0.37,0.37,0.37">\# Simulating the dataset</span>

<span style="color: 0.00,0.23,0.31">j </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">c</span><span style="color: 0.00,0.23,0.31">() </span><span style="color: 0.37,0.37,0.37">\# fill in factor levels</span> <span style="color: 0.00,0.23,0.31">k </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">c</span><span style="color: 0.00,0.23,0.31">() </span><span style="color: 0.37,0.37,0.37">\# fill in blocks</span>

<span style="color: 0.37,0.37,0.37">\# Simulate response using the model</span> <span style="color: 0.00,0.23,0.31">Y </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">generate\_Y</span><span style="color: 0.00,0.23,0.31">(mu, alpha, beta, sigma\_sq, j, k)</span>

<span style="color: 0.37,0.37,0.37">\# Put into a data frame</span> <span style="color: 0.00,0.23,0.31">dat </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">data.frame</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.40,0.45,0.13">Y =</span><span style="color: 0.00,0.23,0.31"> Y,</span> <span style="color: 0.40,0.45,0.13">treatment =</span> <span style="color: 0.28,0.35,0.67">factor</span><span style="color: 0.00,0.23,0.31">(j),</span> <span style="color: 0.40,0.45,0.13">block =</span> <span style="color: 0.28,0.35,0.67">factor</span><span style="color: 0.00,0.23,0.31">(k)</span> <span style="color: 0.00,0.23,0.31">)</span>

We now proceed to run inference and calculate the p-value for our single factor here using the traditional ANOVA and F-test. Complete the steps!

<span style="color: 0.37,0.37,0.37">\# Inference on simulated data </span>

<span style="color: 0.37,0.37,0.37">\# Fit linear model (fixed effects for both)</span> <span style="color: 0.00,0.23,0.31">fit </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">lm</span><span style="color: 0.00,0.23,0.31">(Y </span><span style="color: 0.37,0.37,0.37">~</span> <span style="color: 0.37,0.37,0.37">\# fill in linear model</span> <span style="color: 0.00,0.23,0.31"> , </span><span style="color: 0.40,0.45,0.13">data =</span><span style="color: 0.00,0.23,0.31"> dat)</span>

<span style="color: 0.37,0.37,0.37">\# Extract ANOVA table</span> <span style="color: 0.00,0.23,0.31">aov\_tab </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">anova</span><span style="color: 0.00,0.23,0.31">(fit)</span>

<span style="color: 0.37,0.37,0.37">\# Get p-value for treatment effect</span> <span style="color: 0.00,0.23,0.31">p\_val </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> aov\_tab$$</span><span style="color: 0.13,0.47,0.30">"treatment"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.13,0.47,0.30">"Pr(&gt;F)"</span><span style="color: 0.00,0.23,0.31">$$</span>

<span style="color: 0.37,0.37,0.37">\# Convert to rejection indicator</span> <span style="color: 0.00,0.23,0.31">reject </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">as.integer</span><span style="color: 0.00,0.23,0.31">(p\_val </span><span style="color: 0.37,0.37,0.37">&lt;</span> <span style="color: 0.68,0.00,0.00">0.05</span><span style="color: 0.00,0.23,0.31">)</span>

<span style="color: 0.00,0.23,0.31">reject</span>

####  {#section-3 .unnumbered}

Step 4: Iterating to calculate Power<span id="step-4-iterating-to-calculate-power" label="step-4-iterating-to-calculate-power"></span>

Now that we have outlined the pipeline for simulating a dataset and doing inference, we compile it together into a single `R` function so that it is easy to replicate.

<span style="color: 0.37,0.37,0.37">\# One simulation run through of Steps 1-3</span>

<span style="color: 0.00,0.23,0.31">one\_sim </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.00,0.23,0.31">**function**</span><span style="color: 0.00,0.23,0.31">(mu, alpha, beta, sigma\_sq, j, k) {</span> <span style="color: 0.37,0.37,0.37">\# Generate data</span> <span style="color: 0.00,0.23,0.31"> Y </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">generate\_Y</span><span style="color: 0.00,0.23,0.31">(mu, alpha, beta, sigma\_sq, j, k)</span>

<span style="color: 0.00,0.23,0.31"> dat </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">data.frame</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.40,0.45,0.13">Y =</span><span style="color: 0.00,0.23,0.31"> Y,</span> <span style="color: 0.40,0.45,0.13">treatment =</span> <span style="color: 0.28,0.35,0.67">factor</span><span style="color: 0.00,0.23,0.31">(j),</span> <span style="color: 0.40,0.45,0.13">block =</span> <span style="color: 0.28,0.35,0.67">factor</span><span style="color: 0.00,0.23,0.31">(k)</span> <span style="color: 0.00,0.23,0.31"> )</span>

<span style="color: 0.37,0.37,0.37">\# Fit model</span> <span style="color: 0.00,0.23,0.31"> fit </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">lm</span><span style="color: 0.00,0.23,0.31">(Y </span><span style="color: 0.37,0.37,0.37">~</span><span style="color: 0.00,0.23,0.31"> treatment </span><span style="color: 0.37,0.37,0.37">+</span><span style="color: 0.00,0.23,0.31"> block, </span><span style="color: 0.40,0.45,0.13">data =</span><span style="color: 0.00,0.23,0.31"> dat)</span>

<span style="color: 0.37,0.37,0.37">\# Extract ANOVA p-value for treatment</span> <span style="color: 0.00,0.23,0.31"> p\_val </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">anova</span><span style="color: 0.00,0.23,0.31">(fit)$$</span><span style="color: 0.13,0.47,0.30">"treatment"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.13,0.47,0.30">"Pr(&gt;F)"</span><span style="color: 0.00,0.23,0.31">$$</span>

<span style="color: 0.37,0.37,0.37">\# Return rejection indicator</span> <span style="color: 0.28,0.35,0.67">return</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.28,0.35,0.67">as.integer</span><span style="color: 0.00,0.23,0.31">(p\_val </span><span style="color: 0.37,0.37,0.37">&lt;</span> <span style="color: 0.68,0.00,0.00">0.05</span><span style="color: 0.00,0.23,0.31">))</span> <span style="color: 0.00,0.23,0.31">}</span>

Now, we use our single-run function to iterate over many such simulated datasets under the same proposed “Alternate Hypothesis” of our chosen effect sizes. We use the Monte Carlo machinery from previous power calculations to estimate the probability of rejecting the null () under this alternate!

<span style="color: 0.37,0.37,0.37">\# Iterate over Steps 1-3 multiple times: Turn the Monte Carlo crank!</span>

<span style="color: 0.37,0.37,0.37">\# Number of simulations</span> <span style="color: 0.00,0.23,0.31">iter </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.68,0.00,0.00">1000</span>

<span style="color: 0.37,0.37,0.37">\# Run simulations</span> <span style="color: 0.00,0.23,0.31">reject\_vec </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">replicate</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.00,0.23,0.31"> iter,</span> <span style="color: 0.28,0.35,0.67">one\_sim</span><span style="color: 0.00,0.23,0.31">(mu, alpha, beta, sigma\_sq, j, k)</span> <span style="color: 0.00,0.23,0.31">)</span>

<span style="color: 0.37,0.37,0.37">\# Estimated power</span> <span style="color: 0.00,0.23,0.31">power\_est </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(reject\_vec)</span>

<span style="color: 0.00,0.23,0.31">power\_est</span>

Thus, `power_est` gives us an estimate for power under our specified design and alternative (the minimum deviation from the null that we care about!). We can also run some diagnostics to make sure this estimate has correctly converged.

<span style="color: 0.28,0.35,0.67">library</span><span style="color: 0.00,0.23,0.31">(ggplot2)</span>

<span style="color: 0.37,0.37,0.37">\# Running Monte Carlo estimate of power</span> <span style="color: 0.00,0.23,0.31">running\_power </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">cumsum</span><span style="color: 0.00,0.23,0.31">(reject\_vec) </span><span style="color: 0.37,0.37,0.37">/</span> <span style="color: 0.28,0.35,0.67">seq\_along</span><span style="color: 0.00,0.23,0.31">(reject\_vec)</span>

<span style="color: 0.37,0.37,0.37">\# Put into a data frame for ggplot</span> <span style="color: 0.00,0.23,0.31">df\_power </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">data.frame</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.40,0.45,0.13">iter =</span> <span style="color: 0.28,0.35,0.67">seq\_along</span><span style="color: 0.00,0.23,0.31">(reject\_vec),</span> <span style="color: 0.40,0.45,0.13">power =</span><span style="color: 0.00,0.23,0.31"> running\_power</span> <span style="color: 0.00,0.23,0.31">)</span>

<span style="color: 0.37,0.37,0.37">\# Convergence plot</span> <span style="color: 0.28,0.35,0.67">ggplot</span><span style="color: 0.00,0.23,0.31">(df\_power, </span><span style="color: 0.28,0.35,0.67">aes</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">x =</span><span style="color: 0.00,0.23,0.31"> iter, </span><span style="color: 0.40,0.45,0.13">y =</span><span style="color: 0.00,0.23,0.31"> power)) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_line</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">0.8</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_hline</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">yintercept =</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(reject\_vec), </span><span style="color: 0.40,0.45,0.13">linetype =</span> <span style="color: 0.13,0.47,0.30">"dashed"</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">labs</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.40,0.45,0.13">title =</span> <span style="color: 0.13,0.47,0.30">"Monte Carlo Power Estimate Convergence"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">x =</span> <span style="color: 0.13,0.47,0.30">"Number of Simulations"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">y =</span> <span style="color: 0.13,0.47,0.30">"Estimated Power"</span> <span style="color: 0.00,0.23,0.31"> ) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">theme\_minimal</span><span style="color: 0.00,0.23,0.31">()</span>

If the value of the estimate starts to stay constant after a few iterations, it means that it is stable and reliable as an estimate of your power!

Feel free to go back and change your parameters and rerun the power analysis. In particular, investigate the effect of changing $\sigma^2$!

\## Applying this to your own Group Projects

Use the same pipeline as above, following Steps 1-4 for your own group projects!

**Step 1:** Update the linear model and the data generating process according to the design you choose for your experiment. Be careful about random effects, and model constraints.

**Step 2:** Choose the effect sizes, and sample size that best reflects your setting and the question you want to answer. Keep in mind zero-sum constraints etc!

**Step 3:** Fill out the design matrix or table for your experiment, and use this to fill out `i` and `j` vectors. Add other factors or terms as necessary. Simulate a dataset and hypothesis test.

**Step 4:** Iterate through these steps as many times as needed to ensure your power estimate has converged!
This should give you an idea of what power you can achieve with your chosen design and sample size. Discuss as a group if it is sufficient for your purposes or not. A power of 0.7 - 0.9 is usually considered ideal.

Experiment with different sample sizes to see what size is suitable for your experiment. Feel free to try out different designs, random vs fixed block effects, or play around with the number of factors, levels etc. See which of these gives you the highest power, you may use this to pin down a design/factors if you’re still uncertain. Another way of increasing power is by decreasing $\sigma^2$, either by blocking, protocols, or better measurement.

Evaluate your group project ideas and submit a protocol. Best of luck with your experiments :)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md)
