---
title: Here we will read in the contents of the file
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Here we will read in the contents of the file

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

xtrain = {}
xtest = {}
with h5py.File(data_file, 'r') as hf:
    # This is neural data [time points x electrodes]
    ytrain = hf['ytrain'][:]
    ytest = hf['ytest'][:]

    # This is the spectrogram of the sounds the person heard
    xtrain['spec'] = hf['xtrain_spec'][:]
    xtest['spec'] = hf['xtest_spec'][:]

    # These are the phoneme features for the words the person heard
    xtrain['phn'] = hf['xtrain_phn'][:]
    xtest['phn'] = hf['xtest_phn'][:]

    # Sampling rate of the data
    fs = hf.attrs['fs']
```

```python
print(ytrain.shape, ytest.shape)

---

[← Define a z-scoring function](02-define-a-z-scoring-function.md) · [Up: contents](index.md) · [Show whether the data have been z-scored →](04-show-whether-the-data-have-been-z-scored.md)
