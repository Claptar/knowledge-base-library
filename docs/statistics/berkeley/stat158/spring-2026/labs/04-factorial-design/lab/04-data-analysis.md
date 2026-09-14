---
title: Data Analysis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/04-factorial-design/lab.tex
source_file: sources/berkeley-stat158/spring-2026/labs/04-factorial-design/lab.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Data Analysis

**Source:** [`labs/04-factorial-design/lab.tex`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/04-factorial-design/lab.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

We will now analyze our own collected data. Ensure that you tabulate your data into a `.csv` file. This can be done by entering your data into Google Sheets or Microsoft Excel before saving as `.csv`.

As earlier, use the `readr` package, which is included inside the `tidyverse`. If you haven’t installed the tidyverse before, you can do so by running `install.packages("tidyverse")` once.

<span style="color: 0.37,0.37,0.37">\# load tidyverse (includes readr for CSVs)</span> <span style="color: 0.28,0.35,0.67">library</span><span style="color: 0.00,0.23,0.31">(tidyverse)</span>

<span style="color: 0.37,0.37,0.37">\# load your collected data into R</span>

<span style="color: 0.37,0.37,0.37">\#my\_data &lt;- </span>

### EDA and Scatterplots {#eda-and-scatterplots}

1.  Explore how your helicopters’ flight times differed by wing width. Create a beehive plot using the `ggplot2` and `ggbeeswarm` packages in `R`. If you don’t have these installed, install them by running `install.packages("ggplot2")` and `install.packages("ggbeeswarm")` once.

Stick to a single level of weight while making this for height, or add levels of weight by color coding them!

<span style="color: 0.37,0.37,0.37">\# Load necessary packages</span>

<span style="color: 0.28,0.35,0.67">library</span><span style="color: 0.00,0.23,0.31">(ggplot2)</span> <span style="color: 0.28,0.35,0.67">library</span><span style="color: 0.00,0.23,0.31">(ggbeeswarm)</span>

<span style="color: 0.37,0.37,0.37">\# Beeswarm Plot (Fill in)</span>

<span style="color: 0.37,0.37,0.37">\# my\_data \|&gt;</span> <span style="color: 0.37,0.37,0.37">\# ggplot(aes(x = , y = )) +</span> <span style="color: 0.37,0.37,0.37">\# geom\_beeswarm(cex = 3, size = 3)</span>

Next, calculate the group means. You may choose to this for any one factor or group by both. This requires the `dplyr` package, which you can install using `install.packages("dplyr")`. Also calculate the difference of each group mean with the overall mean. You may plot this to see if it is meaningful. Is it linear, non-linear etc?

<span style="color: 0.37,0.37,0.37">*\### Load necessary packages*</span>

<span style="color: 0.28,0.35,0.67">library</span><span style="color: 0.00,0.23,0.31">(dplyr)</span>

<span style="color: 0.37,0.37,0.37">*\### Calculate Group Means*</span>

<span style="color: 0.37,0.37,0.37">\# group\_means &lt;- my\_data \|&gt;</span> <span style="color: 0.37,0.37,0.37">\# group\_by() \|&gt;</span> <span style="color: 0.37,0.37,0.37">\# summarize(avg = mean())</span> <span style="color: 0.37,0.37,0.37">\# group\_means</span>

<span style="color: 0.37,0.37,0.37">*\### Plot:*</span>

<span style="color: 0.37,0.37,0.37">\# ggplot(effects\_df,</span> <span style="color: 0.37,0.37,0.37">\# aes(x = width,</span> <span style="color: 0.37,0.37,0.37">\# y = effect,</span> <span style="color: 0.37,0.37,0.37">\# group = 1)) +</span> <span style="color: 0.37,0.37,0.37">\# geom\_point(size = 3) +</span> <span style="color: 0.37,0.37,0.37">\# geom\_line(linewidth = 1) +</span> <span style="color: 0.37,0.37,0.37">\# geom\_hline(yintercept = 0, linetype = "dashed") +</span> <span style="color: 0.37,0.37,0.37">\# labs(x = "Wing Width",</span> <span style="color: 0.37,0.37,0.37">\# y = "Difference from Overall Mean")</span>

### Randomization Based Inference {#randomization-based-inference}

1.  Next, conduct a randomization based test for the F-statistic to check whether the width of the wings turned out to be significant in determining flight times. Again, note that you will have to do this after fixing a level for weight.

For reference, see the [Stat 158 F-inference slides page](https://stat158.berkeley.edu/spring-2026/13-f-inference/slides.html#/title-slide).

<span style="color: 0.37,0.37,0.37">*\### Selecting the weight factor*</span>

<span style="color: 0.37,0.37,0.37">\# my\_data\_subset &lt;- my\_data \|&gt;</span> <span style="color: 0.37,0.37,0.37">\# filter(weight == "light")</span>

<span style="color: 0.37,0.37,0.37">*\### Function to simulate under the Null*</span>

<span style="color: 0.00,0.23,0.31">shuffle4\_f </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.00,0.23,0.31">**function**</span><span style="color: 0.00,0.23,0.31">(y, z) {</span> <span style="color: 0.00,0.23,0.31"> Z </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">sample</span><span style="color: 0.00,0.23,0.31">(z) </span><span style="color: 0.37,0.37,0.37">\# source of randomness</span>

<span style="color: 0.00,0.23,0.31"> my\_data\_subset </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">data.frame</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">flight\_time =</span><span style="color: 0.00,0.23,0.31"> y,</span> <span style="color: 0.40,0.45,0.13">width =</span><span style="color: 0.00,0.23,0.31"> Z)</span>

<span style="color: 0.00,0.23,0.31"> avg\_var </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> my\_data\_subset </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">group\_by</span><span style="color: 0.00,0.23,0.31">(width) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">var =</span> <span style="color: 0.28,0.35,0.67">var</span><span style="color: 0.00,0.23,0.31">(flight\_time)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">avg\_var =</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(var)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">pull</span><span style="color: 0.00,0.23,0.31">(avg\_var)</span> <span style="color: 0.00,0.23,0.31"> var\_avg </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> my\_data\_subset </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">group\_by</span><span style="color: 0.00,0.23,0.31">(width) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">avg =</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(flight\_time)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">var\_avg =</span> <span style="color: 0.28,0.35,0.67">var</span><span style="color: 0.00,0.23,0.31">(avg)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">pull</span><span style="color: 0.00,0.23,0.31">(var\_avg)</span>

<span style="color: 0.00,0.23,0.31"> var\_avg </span><span style="color: 0.37,0.37,0.37">/</span><span style="color: 0.00,0.23,0.31"> avg\_var</span> <span style="color: 0.00,0.23,0.31">}</span>

<span style="color: 0.37,0.37,0.37">*\### Calculating the observed value of F - statistic*</span>

<span style="color: 0.00,0.23,0.31">avg\_var </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> my\_data\_subset </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">group\_by</span><span style="color: 0.00,0.23,0.31">(width) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">var =</span> <span style="color: 0.28,0.35,0.67">var</span><span style="color: 0.00,0.23,0.31">(flight\_time)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">avg\_var =</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(var)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">pull</span><span style="color: 0.00,0.23,0.31">(avg\_var)</span>

<span style="color: 0.00,0.23,0.31">var\_avg </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> my\_data\_subset </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">group\_by</span><span style="color: 0.00,0.23,0.31">(width) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">avg =</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(flight\_time)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">var\_avg =</span> <span style="color: 0.28,0.35,0.67">var</span><span style="color: 0.00,0.23,0.31">(avg)) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">pull</span><span style="color: 0.00,0.23,0.31">(var\_avg)</span>

<span style="color: 0.00,0.23,0.31">f\_stat </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> var\_avg </span><span style="color: 0.37,0.37,0.37">/</span><span style="color: 0.00,0.23,0.31"> avg\_var</span>

<span style="color: 0.37,0.37,0.37">*\### Plotting the Null Distribution*</span>

<span style="color: 0.37,0.37,0.37">\# null\_stats &lt;- replicate(500, shuffle4\_f(y = , z = ))</span> <span style="color: 0.00,0.23,0.31">null </span><span style="color: 0.00,0.23,0.31">&lt;-</span> <span style="color: 0.28,0.35,0.67">data.frame</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">stats =</span><span style="color: 0.00,0.23,0.31"> null\_stats)</span>

<span style="color: 0.28,0.35,0.67">ggplot</span><span style="color: 0.00,0.23,0.31">(null, </span><span style="color: 0.28,0.35,0.67">aes</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">x =</span><span style="color: 0.00,0.23,0.31"> stats)) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_histogram</span><span style="color: 0.00,0.23,0.31">() </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_vline</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">xintercept =</span><span style="color: 0.00,0.23,0.31"> f\_stat, </span><span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"tomato"</span><span style="color: 0.00,0.23,0.31">, </span><span style="color: 0.40,0.45,0.13">lwd =</span> <span style="color: 0.68,0.00,0.00">2</span><span style="color: 0.00,0.23,0.31">)</span>

<span style="color: 0.37,0.37,0.37">*\### Calculating p-value*</span>

<span style="color: 0.00,0.23,0.31">null </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">pval =</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(stats </span><span style="color: 0.37,0.37,0.37">&gt;</span><span style="color: 0.00,0.23,0.31"> f\_stat))</span>

### Model Based Inference {#model-based-inference}

1.  We now move into two factor results using the Model Based approach.

What are the assumptions of the Model-based F-test used here?

Now, proceed to calculate the ANOVA Table as discussed in Lecture. Note that you can use `+` to add more than 1 factor, and `*` to specify interactions such as `aov(y ~ x1 + x2 + x1:x2)`.

<span style="color: 0.37,0.37,0.37">*\### Calculating the ANOVA table*</span>

<span style="color: 0.37,0.37,0.37">\# helicopter\_anova &lt;- aov(, data = my\_data)</span> <span style="color: 0.37,0.37,0.37">\# anova\_table &lt;- summary(helicopter\_anova)</span> <span style="color: 0.37,0.37,0.37">\# anova\_table</span>

What factors do you find significant? Do they align with the EDA and the Randomization based tests?

### Interaction Plots {#interaction-plots}

1.  Finally, we plot another simple diagnostic to check the pattern of any interaction between the two factors, wing width and helicopter weight (paper clips). We do this by plotting separate line graphs of flight time by width for both “light” and “heavy” helicopters.

If the lines are roughly parallel, this indicates that the effect of “heaviness” doesn’t change with wing width. However if they aren’t the plot gives you an idea of how this effect of weight changes with width, i.e it gives you an idea of how the interaction effect behaves.

<span style="color: 0.37,0.37,0.37">*\### First compute group means for each combination*</span> <span style="color: 0.37,0.37,0.37">*\### Fill in appropriate column names*</span>

<span style="color: 0.00,0.23,0.31">interaction\_means </span><span style="color: 0.00,0.23,0.31">&lt;-</span><span style="color: 0.00,0.23,0.31"> my\_data </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">group\_by</span><span style="color: 0.00,0.23,0.31">(width, weight) </span><span style="color: 0.37,0.37,0.37">\|&gt;</span> <span style="color: 0.28,0.35,0.67">summarize</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">avg\_flight\_time =</span> <span style="color: 0.28,0.35,0.67">mean</span><span style="color: 0.00,0.23,0.31">(flight\_time))</span>

<span style="color: 0.00,0.23,0.31">interaction\_means</span>

<span style="color: 0.37,0.37,0.37">*\### Plot the interaction*</span> <span style="color: 0.37,0.37,0.37">*\### Fill in appropriate column names*</span>

<span style="color: 0.28,0.35,0.67">ggplot</span><span style="color: 0.00,0.23,0.31">(interaction\_means,</span> <span style="color: 0.28,0.35,0.67">aes</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">x =</span><span style="color: 0.00,0.23,0.31"> width,</span> <span style="color: 0.40,0.45,0.13">y =</span><span style="color: 0.00,0.23,0.31"> avg\_flight\_time,</span> <span style="color: 0.40,0.45,0.13">group =</span><span style="color: 0.00,0.23,0.31"> weight,</span> <span style="color: 0.40,0.45,0.13">color =</span><span style="color: 0.00,0.23,0.31"> weight)) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_point</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">size =</span> <span style="color: 0.68,0.00,0.00">3</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">geom\_line</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">linewidth =</span> <span style="color: 0.68,0.00,0.00">1</span><span style="color: 0.00,0.23,0.31">) </span><span style="color: 0.37,0.37,0.37">+</span> <span style="color: 0.28,0.35,0.67">labs</span><span style="color: 0.00,0.23,0.31">(</span><span style="color: 0.40,0.45,0.13">x =</span> <span style="color: 0.13,0.47,0.30">"Wing Width"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">y =</span> <span style="color: 0.13,0.47,0.30">"Average Flight Time"</span><span style="color: 0.00,0.23,0.31">,</span> <span style="color: 0.40,0.45,0.13">color =</span> <span style="color: 0.13,0.47,0.30">"Paperclip Weight"</span><span style="color: 0.00,0.23,0.31">)</span>

Are the two lines parallel? Is this consistent with the ANOVA table results above?

Answer in brief: how did the structure of your experiment affect what conclusions you were allowed to draw from its final results?

---

[← Conducting Your Own Experiment](03-conducting-your-own-experiment.md) · [Up: contents](index.md)
