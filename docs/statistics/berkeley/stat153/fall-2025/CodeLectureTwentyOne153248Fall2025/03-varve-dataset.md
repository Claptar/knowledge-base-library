---
title: Varve Dataset
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Varve Dataset

This dataset is from the Shumway and Stoffer book. It records the thickness of yearly glacial varves—layers of sediment deposited by melting glaciers—collected from a single site in Massachusetts. Each varve represents one year of sedimentation, formed when meltwater streams carried sand and silt into a glacial lake during the spring and summer melt seasons at the end of the last Ice Age. The dataset contains 634 annual measurements, covering a continuous period that began about 11,834 years ago, when the glaciers in New England were retreating. Thicker varves indicate warmer years with more melting and heavier sediment flow, while thinner varves reflect colder years with less melting. Although these deposits stopped forming thousands of years ago when the glacial lake drained, the preserved layers now provide scientists with a high-resolution record of past climate variations, helping reconstruct temperature and melting patterns during the planet’s transition out of the Ice Age.

See Example 2.6 of the Shumway-Stoffer book, 4th edition, for more details on the dataset.

```python
varve_data = pd.read_csv("varve.csv")
yraw = varve_data['x']
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We shall work with the logarithms of the raw data.

```python
#We shall work with the logarithms:
ylog = np.log(yraw)
plt.plot(ylog)
plt.xlabel('Time')
plt.ylabel('log(Thickness)')
plt.title('Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Fitting a stationary model such as MA($q$) is not appropriate for the logarithmed data. This is because the data does not seem to have constant mean. To deal with this, we difference the data as follows.

```python
ylogdiff = np.diff(ylog)
plt.plot(ylogdiff)
plt.xlabel('Time')
plt.ylabel('diff(log(Thickness))')
plt.title('Differenced Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now let us look at the sample acf of this dataset.

```python
h_max = 50
fig, ax = plt.subplots()
plot_acf(ylogdiff, lags = h_max, ax = ax)
ax.set_title("Sample ACF of log differenced varve series")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear that the sample ACF shows one negative nonnegligible spike at lag one.  The other spikes seem insignificant. This is MA(1) behaviour which suggests that the MA(1) should be appropriate for this data (which is differenced logarithms of the varve data).

---

[← Sample ACF](02-sample-acf.md) · [Up: contents](index.md) · [Fitting MA models using the ARIMA function →](04-fitting-ma-models-using-the-arima-function.md)
