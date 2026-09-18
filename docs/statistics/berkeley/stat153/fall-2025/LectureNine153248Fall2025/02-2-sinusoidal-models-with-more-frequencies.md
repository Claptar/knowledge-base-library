---
title: 2 Sinusoidal Models with more frequencies
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Sinusoidal Models with more frequencies

Consider the model:
$$y_t = \beta_0 + \beta_1 \cos(2\pi f_1 t) + \beta_2 \sin(2\pi f_1 t) + \beta_3 \cos(2\pi f_2 t) + \beta_4 \sin(2\pi f_2 t) + \epsilon_t. \tag{3}$$
Formal inference for this model proceeds very similarly to inference for model (1). The main difference is that the definition of RSS should now be changed to:
$$RSS(f_1, f_2) = \min_{\beta_j, 0 \le j \le 4} \sum_{t=0}^{n-1} (y_t - \beta_0 - \beta_1 \cos(2\pi f_1 t) - \beta_2 \sin(2\pi f_1 t) - \beta_3 \cos(2\pi f_2 t) - \beta_4 \sin(2\pi f_2 t))^2$$
The analysis now proceeds as before with this modified definition of RSS. The least squares estimates of $f_1$ and $f_2$ are obtained by minimizing $RSS(f_1, f_2)$ over $f_1, f_2$, and the Bayesian posterior is given by
$$\propto \left(\frac{1}{RSS(f_1, f_2)}\right)^{(n-5)/2} |X_{f_1, f_2}^T X_{f_1, f_2}|^{-1/2}$$
where $X_{f_1, f_2}$ is now given by
$$X_{f_1, f_2} = \begin{pmatrix} 1 & \cos(2\pi f_1(0)) & \sin(2\pi f_1(0)) & \cos(2\pi f_2(0)) & \sin(2\pi f_2(0)) \\ 1 & \cos(2\pi f_1(1)) & \sin(2\pi f_1(1)) & \cos(2\pi f_2(1)) & \sin(2\pi f_2(1)) \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ 1 & \cos(2\pi f_1(n-1)) & \sin(2\pi f_1(n-1)) & \cos(2\pi f_2(n-1)) & \sin(2\pi f_2(n-1)) \end{pmatrix}$$
Evaluation and minimization of $RSS(f_1, f_2)$ needs to be done on a joint grid for $f_1$ and $f_2$.

## 2.1 Restriction to Fourier Frequencies

Suppose we restrict $f_1$ and $f_2$ to be distinct Fourier frequencies lying strictly between 0 and 0.5. Then it can be proved that
$$RSS(f_1, f_2) = \sum_{t=0}^{n-1} (y_t - \bar{y})^2 - 2I(f_1) - 2I(f_2). \tag{4}$$
From the above, it is clear that $f_1$ and $f_2$ which minimize $RSS(f_1, f_2)$ equal the top two maximizers of the periodogram (remember that we are assuming $f_1$ and $f_2$ to be distinct).

The equality (4) is a consequence of the orthogonality of sinusoidal vectors corresponding to Fourier frequencies. It is proved below.

## 2.2 Orthogonality of Sinusoidal Vectors at Fourier Frequencies

Orthogonality of Sinusoids at Fourier frequencies is best described through complex sinusoids. For every $0 \le j \le (n-1)$, let us define the $n \times 1$ vector
$$u^j = (1, \exp(2\pi i j/n), \exp(2\pi i 2j/n), \dots, \exp(2\pi i (n-1)j/n))^T.$$
This vector can be interpreted as the complex sinusoid $e^{2\pi i f t}$ with Fourier frequency $f = j/n$ evaluated at the time points $t = 0, 1, \dots, (n-1)$. It is easy to see that

1. When $j = 0$, we have $u^0 = (1, 1, \dots, 1)$.
2. When $1 \le j \le n - 1$, we have $u^j = \overline{u^{n-j}}$. Here $\bar{u}$ denotes complex conjugate of $u$ (the complex conjugate $\bar{u}$ of a vector $u$ is defined as the vector obtained by taking the complex conjugates of each entry of $u$).

The most important property of these complex valued vectors $u^0, u^1, \dots, u^{n-1}$ is orthogonality. Specifically, for $0 \le j \ne k \le n - 1$, we have
$$\langle u^j, u^k \rangle = 0. \tag{5}$$
Recall that the inner product between two complex valued vectors $a = (a_1, \dots, a_n)^T$ and $b = (b_1, \dots, b_n)^T$ is given by
$$\langle a, b \rangle = \sum_{j=1}^n a_j \bar{b}_j.$$
Note specially the complex conjugate of $b_j$ above.

Here is the proof of (5). Fix $0 \le j \ne k \le n - 1$ and write
$$\begin{aligned}
\langle u^j, u^k \rangle &= \sum_{t=0}^{n-1} \exp\left(2\pi i \frac{j}{n} t\right) \overline{\exp\left(2\pi i \frac{k}{n} t\right)} \\
&= \sum_{t=0}^{n-1} \exp\left(2\pi i \frac{j}{n} t\right) \exp\left(-2\pi i \frac{k}{n} t\right) \\
&= \sum_{t=0}^{n-1} \exp\left(2\pi i \frac{j-k}{n} t\right) \\
&= \sum_{t=0}^{n-1} \left[\exp\left(2\pi i \frac{j-k}{n}\right)\right]^t \\
&= \frac{1 - \left(\exp\left(2\pi i \frac{j-k}{n}\right)\right)^n}{1 - \exp\left(2\pi i \frac{j-k}{n}\right)} \\
&= \frac{1 - \exp(2\pi i (j-k))}{1 - \exp\left(2\pi i \frac{j-k}{n}\right)} \\
&= \frac{1 - \cos(2\pi(j-k)) - i\sin(2\pi(j-k))}{1 - \exp\left(2\pi i \frac{j-k}{n}\right)} = \frac{1 - 1 - 0}{1 - \exp\left(2\pi i \frac{j-k}{n}\right)} = 0
\end{aligned}$$
This proves (5). It is also easy to see that (just take $j = k$ in the above calculation and the answer can be found in the third line)
$$\langle u^j, u^j \rangle = \|u^j\|^2 = n.$$
This orthogonality of complex sinusoids also extends to real sinusoids made of sines and cosines. For a Fourier frequency $j/n$ strictly lying between 0 and 1 (i.e., $0 < j/n < 1/2$), define
$$c^j := (1, \cos(2\pi j/n), \cos(2\pi 2j/n), \dots, \cos(2\pi (n-1)j/n))^T$$
and
$$s^j := (0, \sin(2\pi j/n), \sin(2\pi 2j/n), \dots, \sin(2\pi (n-1)j/n))^T.$$
These are the vectors obtained by evaluating $\cos(2\pi f t)$ and $\sin(2\pi f t)$ with Fourier Frequency $f = j/n$ at time points $t = 0, 1, \dots, (n-1)$. So far we have assumed that $0 < f = j/n < 1/2$ i.e., $0 < j < n/2$. The definition can be extended to the boundary points 0 and 1/2 as well.

When $j = 0$, the vector $c^0$ is the vector of all ones, while $s^0$ equals the zero vector. When $f = 1/2$ (this is only when $n$ is even other 1/2 will not be a Fourier frequency) or $j = n/2$, we have
$$c^{n/2} = (1, -1, 1, -1, \dots, (-1)^{n-1}) \quad \text{and} \quad s^{n/2} = (0, \dots, 0).$$
Thus when $n$ is even, the non-zero vectors among these are:
$$c^0, c^1, s^1, \dots, c^{\frac{n}{2}-1}, s^{\frac{n}{2}-1}, c^{\frac{n}{2}}.$$
When $n$ is odd, we are looking at
$$c^0, c^1, s^1, \dots, c^{\frac{n-1}{2}}, s^{\frac{n-1}{2}}.$$
In either case, the total number of these vectors equals $n$.

These vectors are orthogonal in $\mathbb{R}^n$. This can be proved as a consequence of the orthogonality of $u^0, \dots, u^{n-1}$, and the facts:
$$c^j = \frac{u^j + \bar{u}^j}{2} = \frac{u^j + u^{n-j}}{2} \quad \text{and} \quad s^j = \frac{u^j - \bar{u}^j}{2i} = \frac{u^j - u^{n-j}}{2i}$$
For example, fix two distinct Fourier frequencies $j/n$ and $k/n$ which are both strictly in $(0, 1/2)$. Then
$$\begin{aligned}
\langle c^j, c^k \rangle &= \left\langle \frac{u^j + u^{n-j}}{2}, \frac{u^k + u^{n-k}}{2} \right\rangle \\
&= \frac{1}{4} \left( \langle u^j, u^k \rangle + \langle u^j, u^{n-k} \rangle + \langle u^{n-j}, u^k \rangle + \langle u^{n-j}, u^{n-k} \rangle \right).
\end{aligned}$$
Each inner product above equals zero because of orthogonality of $u^0, \dots, u^{n-1}$. Indeed, $\langle u^j, u^k \rangle$ and $\langle u^{n-j}, u^{n-k} \rangle$ are zero because $j \ne k$. Also we assumed that $j/n < 0.5$ and $k/n < 0.5$ so that $j + k < n$ which means that $n - j \ne k$ and also $n - k \ne j$. Thus $\langle u^j, u^{n-k} \rangle$ and $\langle u^{n-j}, u^k \rangle$ are also zero. Therefore: $\langle c^j, c^k \rangle = 0$ for $j \ne k$ (it can be easily checked that this will be true even when $j/n$ or $k/n$ equal 0 or 1/2).

One can similarly prove that other inner products (such as those between sines) also equal zero. As another example
$$\langle c^j, s^j \rangle = \left\langle \frac{u^j + u^{n-j}}{2}, \frac{u^j - u^{n-j}}{2i} \right\rangle = \frac{1}{4i} [\langle u^j, u^j \rangle - \langle u^{n-j}, u^{n-j} \rangle] = \frac{1}{4i}(n - n) = 0$$
where we used $\langle u^j, u^j \rangle = n$ for every $j$.

## 2.3 Proof of (4)

Suppose $f_1 = j/n$ and $f_2 = k/n$ with $j \ne k$ and both $0 < j/n, k/n < 0.5$. Then note that $X_{f_1, f_2}$ is a $n \times 5$ matrix with columns $c^0, c^j, s^j, c^k, s^k$. As a result,
$$\begin{aligned}
X_{f_1, f_2}^T X_{f_1, f_2} &= \begin{pmatrix}
\langle c^0, c^0 \rangle & \langle c^0, c^j \rangle & \langle c^0, s^j \rangle & \langle c^0, c^k \rangle & \langle c^0, s^k \rangle \\
\langle c^j, c^0 \rangle & \langle c^j, c^j \rangle & \langle c^j, s^j \rangle & \langle c^j, c^k \rangle & \langle c^j, s^k \rangle \\
\langle s^j, c^0 \rangle & \langle s^j, c^j \rangle & \langle s^j, s^j \rangle & \langle s^j, c^k \rangle & \langle s^j, s^k \rangle \\
\langle c^k, c^0 \rangle & \langle c^k, c^j \rangle & \langle c^k, s^j \rangle & \langle c^k, c^k \rangle & \langle c^k, s^k \rangle
\end{pmatrix} \\
&= \begin{pmatrix}
\langle c^0, c^0 \rangle & 0 & 0 & 0 & 0 \\
0 & \langle c^j, c^j \rangle & 0 & 0 & 0 \\
0 & 0 & \langle s^j, s^j \rangle & 0 & 0 \\
0 & 0 & 0 & \langle c^k, c^k \rangle & 0 \\
0 & 0 & 0 & 0 & \langle s^k, s^k \rangle
\end{pmatrix}
\end{aligned}$$
It is also easy to see that
$$\langle c^0, c^0 \rangle = n \quad \text{and} \quad \langle c^j, c^j \rangle = \langle s^j, s^j \rangle = \langle c^k, c^k \rangle = \langle s^k, s^k \rangle = n/2.$$
We noted these in Lecture 7. They also follow from properties of the complex sinusoidal vectors $u^j$. For example,
$$\begin{aligned}
\langle c^j, c^j \rangle &= \left\langle \frac{u^j + u^{n-j}}{2}, \frac{u^j + u^{n-j}}{2} \right\rangle \\
&= \frac{1}{4} \left(\langle u^j, u^j \rangle + \langle u^j, u^{n-j} \rangle + \langle u^{n-j}, u^j \rangle + \langle u^{n-j}, u^{n-j} \rangle\right) \\
&= \frac{1}{4}(n + 0 + 0 + n) = \frac{n}{2}
\end{aligned}$$
Thus
$$X_{f_1, f_2}^T X_{f_1, f_2} = \begin{pmatrix}
n & 0 & 0 & 0 & 0 \\
0 & n/2 & 0 & 0 & 0 \\
0 & 0 & n/2 & 0 & 0 \\
0 & 0 & 0 & n/2 & 0 \\
0 & 0 & 0 & 0 & n/2
\end{pmatrix}$$
From here the proof proceeds in the same way as in the case of a single Fourier frequency in Lecture 7 to yield (4).

## 2.4 More than two Fourier frequencies

When there are three or more Fourier frequencies, the formula (4) generalizes in the same way. For example, if $f_1, f_2, f_3$ are all distinct Fourier frequencies strictly lying between 0 and 1/2, then
$$RSS(f_1, f_2, f_3) = \sum_{t=0}^{n-1} (y_t - \bar{y})^2 - 2I(f_1) - 2I(f_2) - 2I(f_3).$$
So if we are trying to find the three best Fourier frequencies which best fit the data, we simply pick the top three maximizers of the periodogram. If we do not restrict to Fourier frequencies however, we have to do a harder (say grid based) minimization of $RSS(f_1, f_2, f_3)$. Depending on the application, there could be significant gains in RSS if we go beyond Fourier frequencies.

---

[← 1 Recap: previous two lectures](01-1-recap-previous-two-lectures.md) · [Up: contents](index.md) · [3 Other Nonlinear Models →](03-3-other-nonlinear-models.md)
