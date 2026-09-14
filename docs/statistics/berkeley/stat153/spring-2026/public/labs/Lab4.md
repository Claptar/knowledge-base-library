---
title: Lab 4
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab 4

**Source:** [`public/labs/Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

# Lab 4

We ran through parts of this notebook in class for Lecture 7 and Lecture 8. Now we will extend these analyses to look at our data in more detail and apply some of the

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
import glob
import os
```

```python
summary_df = pd.read_csv('Lab4_data/summary_df.csv')
df_all = pd.read_csv('Lab4_data/df_all.csv')
df_bins = pd.read_csv('Lab4_data/df_bins.csv')
google_form = pd.read_csv('Lab4_data/google_form.csv')
```

```python
# summary_df has one row per observation and shows the number of taps for that observation
summary_df
```

```python
# df_all has all of the data from everyone, including all the individual taps, as well
# as repeated metadata about the person ('subj') who completed the task
# For example, the first several rows are from subj 0, who is left handed and used
# their left index finger for the first part of the task
df_all
```

```python
# df_bins is the binned data when we use 10 second bins -- this is very
# much an oversimplification of the trend over time, but for now
# is simple to look at
# For example, the first row is for subj 0, time_bin 0 corresponds to the
# first 10 seconds of their attempt, and they had 66 taps in that time bin.
# In the second 10 seconds, they had 54 taps.
df_bins
```

```python
# google_form has additional data about whether they slept enough, whether
# they play video games more than 10 hrs a week, and how many years they
# played a sport. Remember this doesn't fully overlap with our other dataset
# and has a different number of rows, though we could try to match them up
# later
google_form
```

# Using seaborn to explore our dataset

[Seaborn](https://seaborn.pydata.org/) is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

We'll use it to explore some of the features of our data

```python
!pip install seaborn # Comment out if already installed
import seaborn as sns
```

```python
sns.lineplot(x='tap_index', y='t_seconds', hue='finger', data=df_all)
```

```python
sns.violinplot(data=df_all, x='dominant_hand', y='dt_seconds', hue='finger')
```

```python
summary_df
```

# Fitting regression models

Now we're going to fit some simple linear regression models with OLS. This is not necessarily the best choice for these data, but more on that later. For now, we're interested in whether the number of taps that someone makes can be modeled as a function of whether they used their dominant hand and which finger they used:

$\text{ntaps} = \beta_0 + \beta_1 (\text{dominant hand}) + \beta_2 (\text{pinky finger})$

As we saw in class, we could use dummy coded variables to assign Left/Right and Pinky/Index to new columns of zeros and ones, but we can also use the statsmodels formulas to make this a little more intuitive, as follows:

```python
import statsmodels.formula.api as smf
```

```python
model = smf.ols(formula="ntaps~ C(dominant_hand) + C(finger)", data=summary_df).fit()
print(model.summary())
```

```python
# What if we just wanted to fit whether taps depend only on using dominant hand? Note
# the difference in Adj. R-squared compared to the last example.

# FILL IN
```

# Plots to look at balance within our data

Are we sampling evenly across handedness? Around 10-12% of the world's population is left-handed, so we should expect that to be roughly the case for the data we get here. Let's see if that pans out.

```python
sns.countplot(x='handedness', data=summary_df)
```

We do indeed have an imbalance in the data, with many more right-handed people than left-handed people. If we ran a regression just looking at whether using your right hand helps, it would show that there is a strong positive effect, but this is drive by the fact that we are mostly running this on right-handed people! So remember to think about how to interpret your coefficients in the context of your actual data.

Let's also just plot which hand the person used to do the task, and whether it was their dominant hand:

```python
sns.countplot(x='hand', data=summary_df, hue='dominant_hand')
```

# Google form data

We also collected data from our google form on sports, gaming, and sleep. Let's look at that here:

```python
google_form
```

# Investigate other model effects

Effect of playing sports and being a gamer are shown below:

```python
model = smf.ols(formula = "ntaps ~ C(finger) + C(dominant_hand) + sport", data=google_form).fit()
print(model.summary())
```

```python
model = smf.ols(formula = "ntaps ~ C(finger) + C(dominant_hand) + C(gamer)", data=google_form).fit()
print(model.summary())
```

```python
sns.boxplot(x='dominant_hand', y='ntaps', hue='gamer', data=google_form)
```

```python
# can you make a boxplot showing whether using your pinky vs your index finger
# results in more taps for gamers vs. non gamers? Your data should be colored
# by gamer vs. nongamer.

# FILL IN
```

```python
# Let's show the same data (ntaps) but change which is x and which is hue.
# (Let's make the finger the color this time)
# Does this make you interpret the data differently or think about it
# differently? Do the two graphs make certain comparisons more obvious?

# FILL IN
```

# Look at the data as a time series

What if we want to see how the number of taps changes over time? We can bin the data (though this can be dangerous... so do look at how binning data affects your results). We'll start here by binning our data in 10 second bins and looking at decay over time bins.

```python
bin_size = 10 # in seconds -- you could also change this to something else!
df_all['time_bin'] = (df_all['t_seconds'] // bin_size).astype(int)
df_all

df_bins = ( df_all.groupby(['subj', 'handedness', 'finger','hand','dominant_hand', 'time_bin'])
            .size()
            .reset_index(name='taps_bin')
          )
df_bins
```

# Examples of how taps change as a function of time bin

Again let's do some exploration of the dataset, splitting by different categories.

```python
sns.lineplot(x='time_bin', y='taps_bin', data=df_bins)
```

```python
sns.lineplot(x='time_bin', y='taps_bin', hue='hand', data=df_bins)
```

```python
sns.lineplot(x='time_bin', y='taps_bin', hue='finger', data=df_bins)
```

# Fitting models

Now we can fit some models to see how the number of taps per bin varies as a function of the time bin and other covariates. Note the adjusted R-squared and other metrics. Are these good models? Why or why not?

```python
model=smf.ols('taps_bin ~ time_bin', data=df_bins).fit()
print(model.summary())
```

```python
model = smf.ols('taps_bin ~ time_bin*C(finger) + C(dominant_hand)', data=df_bins).fit()
print(model.summary())
```

# Try the regressions again but using a different binning ... what do you notice?

```python
# binning of 2 seconds, 5 seconds, something else?
```

# What assumptions are we making?

When we collected our data, we had each person tap twice, once with their pinky and once with their index finger, but using the same hand. Does this affect the validity of any of the assumptions we make with this analysis?

# Relating to other topics

* How do the data we've collected here relate to topics about autocovariance? (can you calculate the autocovariance of your own dataset by loading the csv?)
* How do you think this regression would look if we had people trying to do the finger tapping task for an even longer time? Is linear regression the best solution?

---

[Up: contents](../../index.md)
