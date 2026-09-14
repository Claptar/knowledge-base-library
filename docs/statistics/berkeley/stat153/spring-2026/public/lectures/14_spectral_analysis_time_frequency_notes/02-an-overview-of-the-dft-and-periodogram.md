---
title: An overview of the DFT and periodogram
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/14_spectral_analysis_time_frequency_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/14_spectral_analysis_time_frequency_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# An overview of the DFT and periodogram

**Source:** [`public/lectures/14_spectral_analysis_time_frequency_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/14_spectral_analysis_time_frequency_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

An intuitive relationship between the DFT and the periodogram is that the DFT gives you a complex value that incorporates both the amplitude and phase of each frequency present in the signal, whereas the periodogram represents only the real-valued power at that frequency, removing the phase information. Let's try this with a tiny example:

Suppose we have $x_1=2$, $x_2=3$, $x_3=1$, and $x_4=4$. We can use these to see how the periodogram is derived from squaring the DFT.

The DFT at frequency $j/n$ is:

$$d(j/n) = \frac{1}{\sqrt{n}}\sum_{t=1}^n x_t e^{-i2\pi t j/n}$$

The periodogram is the rescaled squared modulus:

$$P(j/n) = (4/n) |d(j/n)|^2$$

Since we have $n=4$ time points, the Fourier frequencies are $j/n = 0/4, 1/4, 2/4, 3/4$. Since by symmetry $P(j/n) = P(1-j/n)$ we only need $j=0,1,2$.

We can now look at what the sine and cosine waves look like at each frequency.

![Cosine and sine basis functions](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/14_bases.png)

Now let's compute the DFT for each $j$:

For $j=0$:

$$
\begin{aligned}
d(0) &= \frac{1}{\sqrt{4}}\sum_{t=1}^4 x_t e^{-i2\pi t 0} \\
&= \frac{1}{\sqrt{4}}\sum_{t=1}^4 x_t\\
&= \frac{1}{2}(2+3+1+4) = 5\\
\end{aligned}
$$

For $j=1$:

$$d(1/4) = \frac{1}{\sqrt{4}}\sum_{t=1}^4 x_t e^{-i2\pi t 1/4}$$

| t | $e^{-i\pi t/2}$   | $\cos(\pi t/2)$ | $\sin(\pi t/2)$ |
|---|--------------------|-----------------|-----------------|
| 1 | $-i$               |  $0$            | $-1$            |
| 2 | $-1$               | $-1$            |  $0$            |
| 3 | $i$                |  $0$            |  $1$            |
| 4 | $1$                |  $1$            |  $0$            |

$$d(1/4) = \frac{1}{2}(2(-i)+3(-1)+1(i)+4(1)) = \frac{1}{2}(1-i) = 0.5 - 0.5i$$

For $j=2$:

$$
\begin{aligned}
d(2/4) &= \frac{1}{\sqrt{4}}\sum_{t=1}^4 x_t e^{-i2\pi t 2/4}\\
&= \frac{1}{2}\sum_{t=1}^4 x_t e^{-i\pi t}\\
&= \frac{1}{2}\sum_{t=1}^4 x_t (-1)^t\\
&= \frac{1}{2}(2(-1)+3(1)+1(-1)+4(1))\\
&= \frac{1}{2}(4) = 2
\end{aligned}
$$

Now to go to the periodogram from the DFT, we can do:

$$\begin{aligned}
P(j/n) &= (4/n) |d(j/n)|^2\\
P(0/4) &= (4/4) | 5 | ^2 = 25\\
P(1/4) &= (4/4) | 0.5 - 0.5i|^2 = 0.5\\
P(2/4) &= (4/4) | 2 | ^2 = 4\\
P(3/4) &= P(1/4)\\
\end{aligned}
$$

The way to interpret this is that the DFT is a complex number that encodes both amplitude and phase at each frequency.

---

[← Moving Average](01-moving-average.md) · [Up: contents](index.md) · [Periodogram demo →](03-periodogram-demo.md)
