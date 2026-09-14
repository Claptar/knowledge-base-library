---
title: Calculate the return
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Calculate the return

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

djia_return = np.diff(np.log(djia_data['Close']))

plt.figure()
plt.subplot(2,1,1)
plt.plot(djia_data['Date'],djia_data['Close'])
plt.gca().xaxis.set_major_locator(locator)
plt.gca().set_xticklabels([]) # Hide labels since they're the same for both subplots
plt.ylabel('Returns')
plt.gca().grid(True)

plt.subplot(2,1,2)
plt.plot(djia_data['Date'][1:],djia_return)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().tick_params(axis='x', labelrotation=45)
plt.ylabel('Returns')
plt.gca().grid()

plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

## fMRI data

```python
fmri_data = astsa.load_fmri1()

print(fmri_data)

plt.subplot(3,1,1)
plt.plot(fmri_data['cort1'])
plt.plot(fmri_data['cort2'])
plt.ylabel('BOLD')

plt.subplot(3,1,2)
plt.plot(fmri_data['thal1'])
plt.plot(fmri_data['thal2'])
plt.ylabel('BOLD')

plt.subplot(3,1,3)
plt.plot(fmri_data['cere1'])
plt.plot(fmri_data['cere2'])
plt.xlabel('Time (s)')
plt.ylabel('BOLD')

plt.tight_layout()
```

```
time  cort1  cort2  cort3  cort4  thal1  thal2  cere1  cere2
0       1 -0.336 -0.088 -0.579 -0.221 -0.222 -0.046 -0.354 -0.028
1       2 -0.192 -0.359 -0.475 -0.058  0.072 -0.039 -0.346 -0.032
2       3  0.062  0.062  0.063  0.192  0.145 -0.256 -0.337  0.272
3       4  0.128  0.221  0.234 -0.004 -0.104 -0.030  0.149  0.042
4       5  0.358  0.199  0.388  0.255  0.035 -0.081  0.311 -0.080
..    ...    ...    ...    ...    ...    ...    ...    ...    ...
123   124 -0.500 -0.306 -0.279 -0.040 -0.166  0.211 -0.006 -0.191
124   125 -0.443 -0.213 -0.456 -0.103 -0.230  0.156 -0.124 -0.103
125   126 -0.497 -0.526 -0.457  0.376 -0.170  0.126 -0.087 -0.253
126   127 -0.401 -0.081 -0.294 -0.016 -0.186  0.047 -0.081 -0.398
127   128 -0.419 -0.199 -0.394  0.222 -0.044  0.049 -0.031 -0.367

[128 rows x 9 columns]
```

*(1 figure omitted — see the original notebook.)*

## White Noise

In Lecture 2, we talked about _white noise_, which is a special case of a time series generated from uncorrelated random variables, $w_t$ with mean 0 and finite variance $\sigma^2_w$. The name comes from the analogy with white light, indicating that all possible periodic oscillations are present with equal strength (we will see later how this looks in power spectral analysis).

Let's create function that returns `nt` samples of independent/iid Gaussian white noise, that is, where $w_t \sim \mbox{iid } \mathcal{N}(0,\sigma^2_w)$.

```python
def white_noise(nt, var=1):
    '''
    Generate a time series with uncorrelated random variables, `w_t`, with mean 0 and finite variance `var`.
    If var=1 this is the standard normal distribution.
    Inputs:
        nt [int] : number of time points
        var [float] : variance
    Output:
        w [np.array] = array of length nt
    '''
    w = np.sqrt(var) * np.random.randn(nt,)
    return w
```

Now let's plot some white noise data for 250 time points, as in Fig. 1.9 (SS)

```python
nt = 250
w = white_noise(nt)
plt.plot(w)
plt.xlabel('Time')
plt.ylabel('w')
plt.title('White noise');
```

*(1 figure omitted — see the original notebook.)*

Since we are drawing the data randomly at each time point, we will get a different time series if we repeat this process to generate another white noise sample. Next, let's create a matrix of `nt` by `nsamps`, where `nsamps = 100` and `nt=250`. Then plot these time series on top of one another. What do you notice about the expected mean and variance over time?

```python
nsamps = 100
w_matrix = np.zeros((nt, nsamps))
for n in np.arange(nsamps):
    w_matrix[:,n] = white_noise(nt)

plt.plot(w_matrix, color='gray', linewidth=0.1);
plt.plot(w_matrix.mean(1), color='y', linewidth=2)
plt.plot(w_matrix.var(1), color='k', linewidth=2);
```

*(1 figure omitted — see the original notebook.)*

You see here that, as expected, the mean and variance don't change over time, and are pretty close to $0$ and $1$, respectively.

---

[← These are functions named loadX](06-these-are-functions-named-loadx.md) · [Up: contents](index.md) · [Moving average and filtering →](08-moving-average-and-filtering.md)
