---
title: A practical use of autocorrelation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# A practical use of autocorrelation

Finally, let's try this for the speech dataset. Here, the autocorrelation function can be used to calculate the pitch of the person's voice, if we express the time lags in seconds rather than in samples. Here, we know that the sampling rate of the speech data was 10000 Hz (given in your book).

We can look for peaks in the autocorrelation function, and large peaks outsize of `lag=0` correspond to the pitch period and multiples of the pitch period (its harmonics).

```python
speech_data = astsa.load_speech()
sampling_rate = 10000 # This is the sampling rate of the speech data in samples per sec (Hz), according to SS
t = (speech_data['Time']-1)/sampling_rate # Subtract 1 so time series starts from 0 seconds

speech_acf = acf(speech_data['Value'], nlags=250)
plot_acf(speech_data['Value'], lags=250);
plt.gca().set_xticks(np.arange(251,step=50), labels=[t[a] for a in np.arange(251,step=50)]);
plt.xlabel('Time (s)')

# It looks like there is a large peak around t=0.01 seconds (and tellingly, another
# around t=0.02 seconds, which is a multiple. t=0.01 seconds is the pitch period,
# but typically we convert this to a frequency by dividing 1 second by this amount:
print(f'The pitch is approximately {1/0.01} Hz')

# We could use a function like `scipy.signal.findpeaks` to do this more accurately,
# but for now that is beyond the scope of the lab (you can try to implement yourself!)
```

---

[← Real data](04-real-data.md) · [Up: contents](index.md) · [Cross-covariance and cross-correlation →](06-cross-covariance-and-cross-correlation.md)
