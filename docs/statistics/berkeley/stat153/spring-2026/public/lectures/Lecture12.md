---
title: Stat153/248 Lecture 12 - Power spectral analysis
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stat153/248 Lecture 12 - Power spectral analysis

```python
import numpy as np
from matplotlib import pyplot as plt
import math
plt.rcParams['figure.figsize'] = (4, 3)
```

```python
fs = 1000 # sampling rate
t = np.arange(0, 0.5, 1/fs)

# Let's make three different sinusoids:
f = [6,10,39] # Frequencies of the sinusoids
x1 = 2*np.cos(2*math.pi*f[0]*t) + 3*np.sin(2*math.pi*f[0]*t)
x2 = 4*np.cos(2*math.pi*f[1]*t) + 5*np.sin(2*math.pi*f[1]*t)
x3 = 6*np.cos(2*math.pi*f[2]*t) +7*np.sin(2*math.pi*f[2]*t)

plt.figure(figsize=(5,3))
plt.subplot(2,2,1)
plt.plot(t,x1)
plt.axhline(-np.sqrt(2**2+3**2),color='r')
plt.axhline(np.sqrt(2**2+3**2),color='r')
plt.title(f'f={f[0]}')
plt.subplot(2,2,2)
plt.plot(t,x2)
plt.title(f'f={f[1]}')
plt.subplot(2,2,3)
plt.plot(t,x3)
plt.title(f'f={f[2]}')
plt.xlabel('Time (s)')
plt.ylabel('Amp')
plt.subplot(2,2,4)
plt.plot(t,x1+x2+x3)
plt.axhline(np.sqrt(2**2+3**2)+np.sqrt(4**2+5**2)+np.sqrt(6**2+7**2), color='r')
plt.title('x1+x2+x3')
plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

Note that the amplitudes of each of these series are defined by $\sqrt{U_1^2+U_2^2}$. For the sum of sinusoids, it's theoretical maximum amplitude is given by the sum of the amplitudes of each of the components, but this maximum will only be reached if the peaks of the sinusoids are in phase (which does not always happen if they aren't harmonically related - meaning they aren't integer multiples of some underlying frequency).

```python
from IPython.display import Audio, display

fs2 = 44100 # sampling rate
t2 = np.arange(0, 1, 1/fs2)

# Let's make three different sinusoids:
freqs = [261.6, 329.7, 392] # Frequencies of the sinusoids
#freqs = [200, 400, 800]

tone = np.zeros(len(t2),)
for f in freqs:
    tone+= 1*np.cos(2*math.pi*f*t2) + 1*np.sin(2*math.pi*f*t2)
#
#tone+= 10*np.cos(2*math.pi*f*t2) + 10*np.sin(2*math.pi*f*t2)

plt.plot(t2,tone)
plt.gca().set_xlim([0,0.01])
display(Audio(tone, rate=fs2, autoplay=False))
```

```
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

```python
from scipy.signal import periodogram

fs = 100 # sampling rate
t = np.arange(0, 1, 1/fs)

# Let's make three different sinusoids:
f = [6,10,39] # Frequencies of the sinusoids
x1 = 12*np.cos(2*math.pi*f[0]*t) + 13*np.sin(2*math.pi*f[0]*t)
x2 = 4*np.cos(2*math.pi*f[1]*t) + 5*np.sin(2*math.pi*f[1]*t)
x3 = 6*np.cos(2*math.pi*f[2]*t) +7*np.sin(2*math.pi*f[2]*t)

freqs, power = periodogram(x1+x2+x3, fs=fs)

plt.stem(freqs, power)
plt.xlabel('frequency')
plt.ylabel('power')
```

```
Text(0, 0.5, 'power')
```

*(1 figure omitted — see the original notebook.)*

```python
freqs
```

```
array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12.,
       13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25.,
       26., 27., 28., 29., 30., 31., 32., 33., 34., 35., 36., 37., 38.,
       39., 40., 41., 42., 43., 44., 45., 46., 47., 48., 49., 50.])
```

```python
freqs, power = periodogram(tone, fs=fs2)

plt.stem(freqs, power)
plt.gca().set_xlim([0,600])
```

```
(0.0, 600.0)
```

*(1 figure omitted — see the original notebook.)*

In the periodogram, our frequency resolution is $1/T$ where $T$ is the duration of our signal (in seconds! not samples!).

```python
import astsa
```

```python
sunspots=astsa.load_sunspotz()
```

```python
plt.plot(sunspots['Time'], sunspots['Value'])
print(sunspots['Time'])
```

```
0      1749.0
1      1749.5
2      1750.0
3      1750.5
4      1751.0
        ...
454    1976.0
455    1976.5
456    1977.0
457    1977.5
458    1978.0
Name: Time, Length: 459, dtype: float64
```

*(1 figure omitted — see the original notebook.)*

```python
freqs, power = periodogram(sunspots['Value'], fs=2)
plt.plot(freqs,power)
plt.xlabel('Frequency (cycles/year)')
plt.axvline(1/11, color='r') # 1 cycle every 11 years
plt.axvline(1/110, color='r') # 1 cycle every 80-110 years (Gleissberg cycle), slow!
```

```
<matplotlib.lines.Line2D at 0x16b46a3e0>
```

*(1 figure omitted — see the original notebook.)*

```python
plt.semilogx(1/freqs,power)
plt.xlabel('Period')
```

```
/var/folders/3f/h3pnh73d18ldksmkrp_fvtk00000gn/T/ipykernel_23869/2295188987.py:1: RuntimeWarning: divide by zero encountered in divide
  plt.semilogx(1/freqs,power)
Text(0.5, 0, 'Period')
```

*(1 figure omitted — see the original notebook.)*

```python
import scipy.io.wavfile

[fs3, w] =scipy.io.wavfile.read('sounds/lec1_aah_hi.wav')
w = w/w.max()
plt.plot(w)

t = np.arange(0, len(w)/fs3, 1/fs3)
line_noise = 1*np.cos(2*math.pi*60*t) + 1*np.sin(2*math.pi*60*t)

display(Audio(w+10*line_noise, rate=fs3, autoplay=False))
```

```
/var/folders/3f/h3pnh73d18ldksmkrp_fvtk00000gn/T/ipykernel_23869/295426981.py:3: WavFileWarning: Chunk (non-data) not understood, skipping it.
  [fs3, w] =scipy.io.wavfile.read('sounds/lec1_aah_hi.wav')
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

```python
freqs, power = periodogram(w+0.1*line_noise, fs=fs3)

plt.stem(freqs, power)
plt.gca().set_xlim([0,600])
```

```
(0.0, 600.0)
```

*(1 figure omitted — see the original notebook.)*

```python
periodogram?
```

```
[0;31mSignature:[0m
[0mperiodogram[0m[0;34m([0m[0;34m[0m
[0;34m[0m    [0mx[0m[0;34m,[0m[0;34m[0m
[0;34m[0m    [0mfs[0m[0;34m=[0m[0;36m1.0[0m[0;34m,[0m[0;34m[0m
[0;34m[0m    [0mwindow[0m[0;34m=[0m[0;34m'boxcar'[0m[0;34m,[0m[0;34m[0m
[0;34m[0m    [0mnfft[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m[0;34m[0m
[0;34m[0m    [0mdetrend[0m[0;34m=[0m[0;34m'constant'[0m[0;34m,[0m[0;34m[0m
[0;34m[0m    [0mreturn_onesided[0m[0;34m=[0m[0;32mTrue[0m[0;34m,[0m[0;34m[0m
[0;34m[0m    [0mscaling[0m[0;34m=[0m[0;34m'density'[0m[0;34m,[0m[0;34m[0m
[0;34m[0m    [0maxis[0m[0;34m=[0m[0;34m-[0m[0;36m1[0m[0;34m,[0m[0;34m[0m
[0;34m[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0;31mDocstring:[0m
Estimate power spectral density using a periodogram.

Parameters
----------
x : array_like
    Time series of measurement values
fs : float, optional
    Sampling frequency of the `x` time series. Defaults to 1.0.
window : str or tuple or array_like, optional
    Desired window to use. If `window` is a string or tuple, it is
    passed to `get_window` to generate the window values, which are
    DFT-even by default. See `get_window` for a list of windows and
    required parameters. If `window` is array_like it will be used
    directly as the window and its length must be equal to the length
    of the axis over which the periodogram is computed. Defaults
    to 'boxcar'.
nfft : int, optional
    Length of the FFT used. If `None` the length of `x` will be
    used.
detrend : str or function or `False`, optional
    Specifies how to detrend each segment. If `detrend` is a
    string, it is passed as the `type` argument to the `detrend`
    function. If it is a function, it takes a segment and returns a
    detrended segment. If `detrend` is `False`, no detrending is
    done. Defaults to 'constant'.
return_onesided : bool, optional
    If `True`, return a one-sided spectrum for real data. If
    `False` return a two-sided spectrum. Defaults to `True`, but for
    complex data, a two-sided spectrum is always returned.
scaling : { 'density', 'spectrum' }, optional
    Selects between computing the power spectral density ('density')
    where `Pxx` has units of V**2/Hz and computing the squared magnitude
    spectrum ('spectrum') where `Pxx` has units of V**2, if `x`
    is measured in V and `fs` is measured in Hz. Defaults to
    'density'
axis : int, optional
    Axis along which the periodogram is computed; the default is
    over the last axis (i.e. ``axis=-1``).

Returns
-------
f : ndarray
    Array of sample frequencies.
Pxx : ndarray
    Power spectral density or power spectrum of `x`.

See Also
--------
welch: Estimate power spectral density using Welch's method
lombscargle: Lomb-Scargle periodogram for unevenly sampled data

Notes
-----
Consult the :ref:`tutorial_SpectralAnalysis` section of the :ref:`user_guide`
for a discussion of the scalings of the power spectral density and
the magnitude (squared) spectrum.

.. versionadded:: 0.12.0

Examples
--------
>>> import numpy as np
>>> from scipy import signal
>>> import matplotlib.pyplot as plt
>>> rng = np.random.default_rng()

Generate a test signal, a 2 Vrms sine wave at 1234 Hz, corrupted by
0.001 V**2/Hz of white noise sampled at 10 kHz.

>>> fs = 10e3
>>> N = 1e5
>>> amp = 2*np.sqrt(2)
>>> freq = 1234.0
>>> noise_power = 0.001 * fs / 2
>>> time = np.arange(N) / fs
>>> x = amp*np.sin(2*np.pi*freq*time)
>>> x += rng.normal(scale=np.sqrt(noise_power), size=time.shape)

Compute and plot the power spectral density.

>>> f, Pxx_den = signal.periodogram(x, fs)
>>> plt.semilogy(f, Pxx_den)
>>> plt.ylim([1e-7, 1e2])
>>> plt.xlabel('frequency [Hz]')
>>> plt.ylabel('PSD [V**2/Hz]')
>>> plt.show()

If we average the last half of the spectral density, to exclude the
peak, we can recover the noise power on the signal.

>>> np.mean(Pxx_den[25000:])
0.000985320699252543

Now compute and plot the power spectrum.

>>> f, Pxx_spec = signal.periodogram(x, fs, 'flattop', scaling='spectrum')
>>> plt.figure()
>>> plt.semilogy(f, np.sqrt(Pxx_spec))
>>> plt.ylim([1e-4, 1e1])
>>> plt.xlabel('frequency [Hz]')
>>> plt.ylabel('Linear spectrum [V RMS]')
>>> plt.show()

The peak height in the power spectrum is an estimate of the RMS
amplitude.

>>> np.sqrt(Pxx_spec.max())
2.0077340678640727
[0;31mFile:[0m      ~/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages/scipy/signal/_spectral_py.py
[0;31mType:[0m      function
```

---

[Up: contents](../../index.md)
