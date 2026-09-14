---
title: Data Analysis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/05-sequential-testing/lab.tex
source_file: sources/berkeley-stat158/spring-2026/labs/05-sequential-testing/lab.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Data Analysis

**Source:** [`labs/05-sequential-testing/lab.tex`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/05-sequential-testing/lab.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

We will now analyze our own collected data. You will be collecting binary data with each iteration of the experiment, and you can simply append the outcome (1 or 0) to the `my_data` vector below. Also remember to load libraries like `tidyverse` or `ggplot2` if you plan to use them! You may also store your data in a `.csv` file, and append that and reload it if you prefer.

<span style="color: 0.37,0.37,0.37">\# load your collected data into R</span>

<span style="color: 0.00,0.23,0.31">my\_data </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">c</span><span style="color: 0.00,0.23,0.31">()</span>

### The SPRT {#the-sprt}

1.  We shall first implement the Sequential Probability Ratio Test (SPRT) for the collected response time data in real time. Identify the assumptions, define the parameters and add your data as you collect them until the SPRT terminates!

**Q:** What assumptions are required by the SPRT test in this binary setting?

**A:**






First,

<span style="color: 0.37,0.37,0.37">\# define the parameters</span>

<span style="color: 0.37,0.37,0.37">\#p0 &lt;- \# acceptable defect rate under H0</span> <span style="color: 0.37,0.37,0.37">\#p1 &lt;- \# unacceptable defect rate under H1</span> <span style="color: 0.37,0.37,0.37">\#alpha &lt;-</span> <span style="color: 0.37,0.37,0.37">\#beta &lt;-</span>

Calculate the log-likelihood ratio for this Bernoulli case.

<span style="color: 0.37,0.37,0.37">\# Calculate the formula for the log-likelihood ratio</span>

<span style="color: 0.00,0.23,0.31">log\_lr\_function </span><span style="color: 0.00,0.23,0.31">&lt;-</span>

<span style="color: 0.37,0.37,0.37">\# Append your data (Cell 1) in real time and calculate the cumulative log-LR</span>

<span style="color: 0.00,0.23,0.31">log\_lr </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">cumsum</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.28,0.35,0.67">log\_lr\_function</span><span style="color: 0.00,0.23,0.31">(my\_data))</span>

<span style="color: 0.37,0.37,0.37">\# SPRT thresholds</span> <span style="color: 0.00,0.23,0.31">A </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> (</span><span style="color: 0.68,0.00,0.00">1</span> <span style="color: 0.37,0.37,0.37">-</span><span style="color: 0.00,0.23,0.31"> beta) </span><span style="color: 0.37,0.37,0.37">/</span><span style="color: 0.00,0.23,0.31"> alpha</span> <span style="color: 0.00,0.23,0.31">B </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> beta </span><span style="color: 0.37,0.37,0.37">/</span><span style="color: 0.00,0.23,0.31"> (</span><span style="color: 0.68,0.00,0.00">1</span> <span style="color: 0.37,0.37,0.37">-</span><span style="color: 0.00,0.23,0.31"> alpha)</span> <span style="color: 0.00,0.23,0.31">logA </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">log</span><span style="color: 0.00,0.23,0.31">(A)</span> <span style="color: 0.00,0.23,0.31">logB </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">log</span><span style="color: 0.00,0.23,0.31">(B)</span>

Check and visualize the results of your SPRT with each iteration of data below!

<span style="color: 0.37,0.37,0.37">\# Check results</span>

<span style="color: 0.00,0.23,0.31">current\_log\_lr </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">tail</span><span style="color: 0.00,0.23,0.31">(log\_lr, </span><span style="color: 0.40,0.45,0.13">n =</span> <span style="color: 0.68,0.00,0.00">1</span><span style="color: 0.00,0.23,0.31">)</span>

<span style="color: 0.37,0.37,0.37">\# Check the SPRT stopping conditions</span>

<span style="color: 0.00,0.23,0.31">**if**</span><span style="color: 0.00,0.23,0.31"> (current\_log\_lr </span><span style="color: 0.37,0.37,0.37">&gt;=</span><span style="color: 0.00,0.23,0.31"> logA) {</span> <span style="color: 0.28,0.35,0.67">print</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.13,0.47,0.30">"Decision Reached: Crosses Upper Boundary (logA)."</span><span style="color: 0.00,0.23,0.31">)</span> <span style="color: 0.28,0.35,0.67">print</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.13,0.47,0.30">"Conclusion: Reject the Null Hypothesis (H0)."</span><span style="color: 0.00,0.23,0.31">)</span> <span style="color: 0.00,0.23,0.31">} </span><span style="color: 0.00,0.23,0.31">**else**</span> <span style="color: 0.00,0.23,0.31">**if**</span><span style="color: 0.00,0.23,0.31"> (current\_log\_lr </span><span style="color: 0.37,0.37,0.37">&lt;=</span><span style="color: 0.00,0.23,0.31"> logB) {</span> <span style="color: 0.28,0.35,0.67">print</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.13,0.47,0.30">"Decision Reached: Crosses Lower Boundary (logB)."</span><span style="color: 0.00,0.23,0.31">)</span> <span style="color: 0.28,0.35,0.67">print</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.13,0.47,0.30">"Conclusion: Fail to reject the Null Hypothesis (H0)."</span><span style="color: 0.00,0.23,0.31">)</span> <span style="color: 0.00,0.23,0.31">} </span><span style="color: 0.00,0.23,0.31">**else**</span><span style="color: 0.00,0.23,0.31"> {</span> <span style="color: 0.28,0.35,0.67">print</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.13,0.47,0.30">"No Decision Yet: The statistic is still between the boundaries."</span><span style="color: 0.00,0.23,0.31">)</span> <span style="color: 0.28,0.35,0.67">print</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.13,0.47,0.30">"Conclusion: Continue collecting data!"</span><span style="color: 0.00,0.23,0.31">)</span> <span style="color: 0.00,0.23,0.31">}</span>

<span style="color: 0.37,0.37,0.37">\# Plot the SPRT</span>

<span style="color: 0.37,0.37,0.37">\# Load required library</span> <span style="color: 0.28,0.35,0.67">library</span><span style="color: 0.00,0.23,0.31">(ggplot2)</span>

<span style="color: 0.37,0.37,0.37">\# Create the dataframe </span> <span style="color: 0.00,0.23,0.31">df\_sprt </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">data.frame</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.40,0.45,0.13">n =</span> <span style="color: 0.68,0.00,0.00">1</span><span style="color: 0.37,0.37,0.37">:</span><span style="color: 0.28,0.35,0.67">length</span><span style="color: 0.00,0.23,0.31">(log\_lr),</span> <span style="color: 0.40,0.45,0.13">log\_lr =</span><span style="color: 0.00,0.23,0.31"> log\_lr</span> <span style="color: 0.00,0.23,0.31">)</span>

<span style="color: 0.37,0.37,0.37">\# Generate the plot</span> <span style="color: 0.28,0.35,0.67">ggplot</span><span style="color: 0.00,0.23,0.31">(df\_sprt, </span><span style="color: 0.28,0.35,0.67">aes</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">x =</span><span style="color: 0.00,0.23,0.31"> n, </span><span style="color: 0.40,0.45,0.13">y =</span><span style="color: 0.00,0.23,0.31"> log\_lr)) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_line</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"black"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">0.8</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_point</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"black"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">size =</span> <span style="color: 0.68,0.00,0.00">1.5</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_hline</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">yintercept =</span><span style="color: 0.00,0.23,0.31"> logA, </span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"black"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linetype =</span> <span style="color: 0.13,0.47,0.30">"dashed"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">0.8</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_hline</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">yintercept =</span><span style="color: 0.00,0.23,0.31"> logB, </span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"black"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linetype =</span> <span style="color: 0.13,0.47,0.30">"dashed"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">0.8</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">labs</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.40,0.45,0.13">title =</span> <span style="color: 0.13,0.47,0.30">"One SPRT path"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">x =</span> <span style="color: 0.13,0.47,0.30">"Number tested"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">y =</span> <span style="color: 0.13,0.47,0.30">"Log likelihood ratio"</span> <span style="color: 0.00,0.23,0.31"> ) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">theme\_minimal</span><span style="color: 0.00,0.23,0.31">()</span>

### Group Sequential Tests {#group-sequential-tests}

We shall now implement a grouped SPRT test with the group sizes that you decided on earlier. Use the same data that you had collected but instead batch it in groups.

1.  Do you think any of the assumptions of the SPRT changes in this grouped setting?

Define the group size below and get started with implementing the Grouped SPRT!

<span style="color: 0.37,0.37,0.37">\# Define group size and import groups one at a time</span>

<span style="color: 0.00,0.23,0.31">group\_size </span><span style="color: 0.00,0.23,0.31">=</span>

<span style="color: 0.37,0.37,0.37">\# Calculate how many full groups we can form from our collected data</span> <span style="color: 0.00,0.23,0.31">num\_groups </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">floor</span><span style="color: 0.00,0.23,0.31">() </span><span style="color: 0.37,0.37,0.37">*\## Complete the floor function!* </span>

<span style="color: 0.37,0.37,0.37">\# Extract the indices corresponding to the end of each group</span> <span style="color: 0.00,0.23,0.31">group\_indices </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">seq</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">from =</span><span style="color: 0.00,0.23,0.31"> group\_size, </span><span style="color: 0.40,0.45,0.13">to =</span><span style="color: 0.00,0.23,0.31"> num\_groups </span><span style="color: 0.37,0.37,0.37">\*</span><span style="color: 0.00,0.23,0.31"> group\_size, </span><span style="color: 0.40,0.45,0.13">by =</span><span style="color: 0.00,0.23,0.31"> group\_size)</span>

The log-likelihood ratio for a single observation still stays the same, but we just add `group_size` many terms to the cumulative sum at a time together and visualize it!

<span style="color: 0.37,0.37,0.37">\# Calculating the grouped log\_lr for each group with fixed size.</span> <span style="color: 0.37,0.37,0.37">\# Note, ith element of grouped\_log\_lr represents </span>

<span style="color: 0.00,0.23,0.31">grouped\_log\_lr </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> log\_lr$$group\_indices$$ </span><span style="color: 0.37,0.37,0.37">*\## Why does this work?*</span>

We now generate the same plot for the Grouped SPRT case. Note that in such a grouped setting, there are more efficient ways of selecting the thresholds `logA` and `logB`, which can be done via the `gsDesign` R package. However, for the purposes of this lab, we shall stick to the earlier standard thresholds calculated.

<span style="color: 0.37,0.37,0.37">\# Plot the SPRT</span>

<span style="color: 0.37,0.37,0.37">\# Create the dataframe. Complete the steps!</span>

<span style="color: 0.00,0.23,0.31">df\_grouped\_sprt </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">data.frame</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.37,0.37,0.37">\#n = 1:length(),</span> <span style="color: 0.37,0.37,0.37">\#</span> <span style="color: 0.00,0.23,0.31">)</span>

<span style="color: 0.37,0.37,0.37">\# Generate the plot. Complete the aes!</span>

<span style="color: 0.28,0.35,0.67">ggplot</span><span style="color: 0.00,0.23,0.31">(df\_grouped\_sprt, </span><span style="color: 0.28,0.35,0.67">aes</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">x =</span><span style="color: 0.00,0.23,0.31"> n, </span><span style="color: 0.40,0.45,0.13">y =</span><span style="color: 0.00,0.23,0.31"> )) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_line</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"#B22222"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">0.8</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_point</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"#B22222"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">size =</span> <span style="color: 0.68,0.00,0.00">1.5</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_hline</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">yintercept =</span><span style="color: 0.00,0.23,0.31"> logA, </span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"black"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linetype =</span> <span style="color: 0.13,0.47,0.30">"dashed"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">0.8</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_hline</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">yintercept =</span><span style="color: 0.00,0.23,0.31"> logB, </span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"black"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linetype =</span> <span style="color: 0.13,0.47,0.30">"dashed"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">0.8</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">labs</span><span style="color: 0.00,0.23,0.31">(</span> <span style="color: 0.40,0.45,0.13">title =</span> <span style="color: 0.13,0.47,0.30">"Grouped SPRT path"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">x =</span> <span style="color: 0.13,0.47,0.30">"Number tested"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">y =</span> <span style="color: 0.13,0.47,0.30">"Grouped Log likelihood ratio"</span> <span style="color: 0.00,0.23,0.31"> ) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">theme\_minimal</span><span style="color: 0.00,0.23,0.31">()</span>

1.  Compare both the SPRT and the Grouped SPRT plots above. Which stopped faster? Which seemed to converge more convincingly?

---

[← Conducting Your Own Experiment](03-conducting-your-own-experiment.md) · [Up: contents](index.md)
