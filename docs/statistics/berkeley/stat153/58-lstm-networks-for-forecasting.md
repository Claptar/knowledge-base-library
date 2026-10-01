---
title: "58. LSTM Networks for Forecasting"
course: "Berkeley Stat 153"
chapter: 58
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 58. LSTM Networks for Forecasting

## What this covers

This is a code lecture: instead of deriving a model, it walks through fitting one. It answers a
practical question — given a scalar time series, how do you set up and train a recurrent neural
network to forecast it, and when does the extra machinery of an LSTM actually buy you something
over a plain RNN or over the AR($p$) models from earlier in the course? It assumes you already
know what an AR($p$) model is and what it means to fit one, and that you have the basic vocabulary
of a feedforward neural network trained by backpropagation (loss function, gradient step, epoch).
No new theorem is proved here; the content is a sequence of worked examples in PyTorch, and this
chapter keeps their numbers and their punch lines.

## The LSTM unit as a black box

An LSTM unit is created by fixing two numbers: the **input size** $p$, the dimension of each
$x_t$ in the input sequence, and the **hidden size** $k$, the dimension of the hidden vector
$h_t$ it produces at each step. In PyTorch,

```python
lstm_net = nn.LSTM(input_size=1, hidden_size=5, batch_first=True)
```

creates the unit and randomly initializes all of its parameters: weight matrices
$W_{ii}, W_{hi}, W_{if}, W_{hf}, W_{ig}, W_{hg}, W_{io}, W_{ho}$ and bias vectors
$b_{ii}, b_{hi}, b_{if}, b_{hf}, b_{ig}, b_{hg}, b_{io}, b_{ho}$. Given a sequence
$x_1, \dots, x_T$ (each $x_t$ of dimension $p$), the unit applies its update formulas
recursively to produce a sequence of pairs $(c_1, h_1), \dots, (c_T, h_T)$: $h_t$ is the hidden
state and $c_t$ is the **cell state**, an internal running memory that the hidden state is read
off from at each step. The unit returns the whole sequence $h_1, \dots, h_T$, plus the final pair
$(h_T, c_T)$ on its own (PyTorch calls these `hn`, `cn`). The lecture treats the unit exactly as
a black box at this level of detail — it names the parameters and points at the PyTorch
documentation for the update formulas themselves, rather than deriving them.

The `batch_first = True` argument fixes the tensor convention: if you send in $B$ input
sequences (batches) each of length $T$, with each element of dimension `input_size`, the input
tensor has shape $(B, T, \text{input\_size})$ and the output tensor has shape
$(B, T, \text{hidden\_size})$. The course mostly works with $B = 1$ — a single long sequence — and
only revisits $B > 1$ later, for the speed-up in ["Speed versus memory"](#speed-versus-memory-batching-a-long-sequence) below.

Running a random sequence through confirms the shapes: for `input_size = 1`, `hidden_size = 5`,
and an input of shape $(1, 10, 1)$,

```python
output, (hn, cn) = lstm_net(input)
print(output.shape)   # torch.Size([1, 10, 5])
print(hn.shape)        # torch.Size([1, 1, 5])
print(cn.shape)        # torch.Size([1, 1, 5])
```

and `hn` is exactly `output[:, 9, :]` — the last time step of the output sequence, reshaped. The
parameter tensors reveal the internal structure: with `hidden_size = 5` and `input_size = 1`,

```python
print(lstm_net.weight_ih_l0.shape)  # torch.Size([20, 1])
print(lstm_net.weight_hh_l0.shape)  # torch.Size([20, 5])
print(lstm_net.bias_ih_l0.shape)    # torch.Size([20])
print(lstm_net.bias_hh_l0.shape)    # torch.Size([20])
```

$20 = 4 \times 5$: PyTorch stacks the four input-to-hidden matrices $W_{ii}, W_{if}, W_{ig},
W_{io}$ into the single $(4k, p)$ tensor `weight_ih_l0`, the four hidden-to-hidden matrices
$W_{hi}, W_{hf}, W_{hg}, W_{ho}$ into the $(4k, k)$ tensor `weight_hh_l0`, and similarly for the
two bias tensors, each of shape $(4k,)$. The subscript `l0` marks the first (and, throughout this
course, only) LSTM layer — stacking several LSTM layers is possible but not used here. The values
shown for these tensors on creation are just the random initialization; fitting the model means
choosing them to minimize a loss.

<figure>
<svg viewBox="0 0 480 200" role="img" aria-label="An LSTM unit applied at three consecutive time steps, passing hidden and cell state forward along the sequence">
  <defs>
    <marker id="arrow58" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <rect x="40" y="70" width="90" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="85" y="105" text-anchor="middle" font-size="13" fill="currentColor">LSTM</text>

  <rect x="195" y="70" width="90" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="240" y="105" text-anchor="middle" font-size="13" fill="currentColor">LSTM</text>

  <rect x="350" y="70" width="90" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="395" y="105" text-anchor="middle" font-size="13" fill="currentColor">LSTM</text>

  <line x1="85" y1="175" x2="85" y2="132" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="85" y="190" text-anchor="middle" font-size="12" fill="currentColor">x_t-1</text>

  <line x1="240" y1="175" x2="240" y2="132" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="240" y="190" text-anchor="middle" font-size="12" fill="currentColor">x_t</text>

  <line x1="395" y1="175" x2="395" y2="132" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="395" y="190" text-anchor="middle" font-size="12" fill="currentColor">x_t+1</text>

  <line x1="85" y1="68" x2="85" y2="30" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="85" y="20" text-anchor="middle" font-size="12" fill="currentColor">h_t-1</text>

  <line x1="240" y1="68" x2="240" y2="30" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="240" y="20" text-anchor="middle" font-size="12" fill="currentColor">h_t</text>

  <line x1="395" y1="68" x2="395" y2="30" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="395" y="20" text-anchor="middle" font-size="12" fill="currentColor">h_t+1</text>

  <line x1="130" y1="100" x2="193" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="161" y="92" text-anchor="middle" font-size="11" fill="currentColor">h, c</text>

  <line x1="285" y1="100" x2="348" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow58)"/>
  <text x="316" y="92" text-anchor="middle" font-size="11" fill="currentColor">h, c</text>

  <line x1="15" y1="100" x2="38" y2="100" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrow58)"/>
  <line x1="442" y1="100" x2="465" y2="100" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrow58)"/>
</svg>
<figcaption>The same LSTM unit applied at every time step, with the hidden state and cell state
carried forward along the horizontal arrows. That chain is what lets the network in principle
recall something from many steps back — and cutting it, as batching does at every chunk boundary,
is exactly what trades memory for speed.</figcaption>
</figure>

The course's own notation for the two internal vectors, used later when reading off code
comments, is $r_t$ for the hidden state (PyTorch's $h_t$) and $s_t$ for the cell state (PyTorch's
$c_t$).

## From LSTM unit to a forecasting model

To turn the unit into a one-step-ahead forecaster of a scalar series, wrap it in a small module
that adds a linear read-out on top:

```python
class lstm_net(nn.Module):
    def __init__(self, nh):
        super().__init__()
        self.rnn = nn.LSTM(input_size=1, hidden_size=nh, batch_first=True)
        self.fc  = nn.Linear(nh, 1)
    def forward(self, x, hc=None):
        out, hc = self.rnn(x, hc)
        out     = self.fc(out)
        return out, hc
```

The fully connected layer (`fc`) maps each hidden vector $h_t$ down to a scalar
$\mu_t = \beta_0 + \beta^T h_t$ — the predicted mean of $y_{t+1}$ given everything the hidden
state has summarized about $y_1, \dots, y_t$. This makes the whole thing a nonlinear
autoregression: unlike AR($p$), which only looks back a fixed $p$ steps, the hidden state can in
principle carry information from arbitrarily far back in the sequence.

Before fitting, the series is standardized, $y^{\text{std}} = (y - \bar y)/s_y$, and the inputs
and targets are built as one-step-shifted copies of the standardized series:

```python
X = torch.tensor(y_std[:-1], dtype=torch.float32).unsqueeze(0).unsqueeze(-1)  # (1, T, 1)
Y = torch.tensor(y_std[1:],  dtype=torch.float32).unsqueeze(0).unsqueeze(-1)  # (1, T, 1)
```

`unsqueeze(0)` adds the batch dimension and `unsqueeze(-1)` adds the input dimension. Training
minimizes mean squared error between `model(X)` and `Y` with Adam:

```python
model = lstm_net(nh)
criterion = nn.MSELoss()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(1, n_epochs + 1):
    opt.zero_grad()
    pred, _ = model(X)
    loss = criterion(pred, Y)
    loss.backward()
    opt.step()
```

Forecasting $n_{\text{future}}$ steps ahead is a closed loop, exactly analogous to iterating an
AR($p$) forward using its own past forecasts: run the trained model once over the training data to
get the final $(h, c)$, then repeatedly feed the last known (or last generated) value back in as a
single-step input, reusing the carried hidden and cell state each time, and record the output as
the next forecast:

```python
_, hc = model(X)
last_in = torch.tensor([[y_std[-1]]], dtype=torch.float32)
for t in range(n_future):
    out, hc = model(last_in.view(1, 1, 1), hc)
    next_val = out.squeeze().item()
    preds[t] = next_val
    last_in = torch.tensor([[next_val]], dtype=torch.float32)
```

The forecasts are then rescaled back to the original units, `preds * sig + mu`.

## Case study: a short periodic lag

The first test series has length $n = 1500$ and is built from a ramp of length 85 (`truelag`) run
from $-1$ to $1$, repeated exactly every 85 steps, with i.i.d. Gaussian noise ($\sigma = 0.2$)
added on top of the whole thing at the end — so the series is a fixed period-85 shape plus
independent noise, not noise that compounds through the recursion.

Fitting AR($p$) confirms the obvious: with $p$ smaller than the true lag the forecasts are poor,
because the model cannot see the periodicity, while with $p$ set exactly to the true lag (85) the
forecasts are good. An LSTM with hidden size 32, trained for 1000 epochs (loss falls from about
0.29 to about 0.16), and a plain RNN with `nn.RNN(1, nh, nonlinearity="tanh")` at the same hidden
size both learn the periodic structure and forecast it well into the future — for this short,
exactly-periodic case, "RNN gives predictions that are similar to the LSTM predictions."

## Speed versus memory: batching a long sequence

Feeding the entire 1500-step series through as one sequence ($B=1$) means every training step
backpropagates through all 1500 time steps, storing every intermediate gate output, cell state and
hidden state along the way — a cost, in both compute and memory, that grows roughly linearly in
$T$.

The fix used in the course is to chunk the series into $B$ shorter batches and stack them, e.g.
splitting the 1500-step series into 3 batches of length 450:

```python
X_batches, Y_batches = [], []
for i in range(n_batches):
    start, end = i * seq_len_batch, i * seq_len_batch + seq_len_batch
    X_batches.append(y_std[start:end])
    Y_batches.append(y_std[start + 1: end + 1])
X = torch.tensor(X_batches, dtype=torch.float32).unsqueeze(-1)  # (3, 450, 1)
```

Each forward/backward pass now unrolls only 450 steps (a $3.3\times$ reduction), and the three
batches can be processed in parallel along the batch dimension. The trade-off is that the hidden
state is implicitly reset at every batch boundary, so the trained model cannot capture
dependencies that span more than one chunk's length; for genuinely long-range dependence the
slower, unbatched, single-sequence fit is safer. For the period-85 series, training with 450-step
chunks gave forecasts nearly identical to the unbatched fit, but noticeably faster. Repeating the
trick on the longer, period-344 series below with 650-step chunks (2 batches) again gave forecasts
close to the unbatched LSTM — though the lecturer notes this was sensitive to the chunk length
chosen: "for different values of this parameter, the predictions seem different from the
full-sequence predictions."

## Case study: a genuinely long lag

The second series keeps $n = 1500$ but increases the true lag to 344, and changes how noise
enters: it is now added inside the recursion itself, $y_t = y_{t - 344} + \epsilon_t$, so errors
compound rather than sitting on top of a fixed shape.

Here AR($p$) with $p$ set to the true lag gives very noisy forecasts. The LSTM (hidden size 32
or 100, depending on the run) gives forecasts that are decent and visibly "clean" — qualitatively
different in character from AR's noisy ones. The plain RNN, by contrast, does not work here at
all: "I could not find any value of nh for which the RNN is giving good predictions for this
data." Its forecasts look reasonable for a short while and then drift away from the LSTM's as the
horizon grows. This is the case that makes the LSTM's extra machinery pay off: a plain RNN's single
recurrent nonlinearity struggles to preserve information across 344 steps, while the LSTM's gated
cell state is built specifically to carry information over long spans.

## Case study: nonlinear dynamics and choosing an evaluation metric

The third series is generated by a nonlinear recursion rather than a linear one,
$$y_t = 0.9 \sin(0.5 \pi\, y_{t-p}) + \epsilon_t, \qquad t > p,$$
with $p = 85$, $n = 1500$, and small noise ($\sigma = 0.01$); for $t \le p$, $y_t$ is again a
linear ramp. Because the generating function $g(y) = 0.9\sin(0.5\pi y)$ is known here, the lecture
computes **oracle predictions** by iterating $g$ forward exactly (ignoring noise) — a benchmark
against which every fitted method can be compared.

AR($p$) at the true lag fails: since the true relationship is nonlinear, a linear model cannot
represent it, and its forecasts visibly "expand" away from the oracle. The LSTM's forecasts track
the oracle much more closely by eye. But comparing root-mean-squared error tells a different, and
misleading, story:
$$\text{RMSE}_{\text{AR}} = 0.182, \qquad \text{RMSE}_{\text{LSTM}} = 0.210,$$
$$\text{median abs. error}_{\text{AR}} = 0.143, \qquad \text{median abs. error}_{\text{LSTM}} = 0.059.$$
By RMSE the LSTM looks *worse* than AR, even though it is visibly closer to the oracle almost
everywhere. The reason is that $g$ has sharp transitions, and a squared-error metric is dominated
by the few large errors the LSTM makes right at those transition points; the median absolute
error, which is robust to a handful of outlying errors, shows the LSTM is in fact much closer to
the oracle over the bulk of the forecast. The general lesson drawn is to prefer an evaluation
metric that is robust to outliers whenever the underlying signal has sharp transitions.

(The notebook also flags that exact numbers like these are not perfectly reproducible across
machines, even with the same random seeds, because different versions of NumPy, PyTorch and
statsmodels can change how random numbers are generated or how models are fit — small numerical
differences can grow during forecasting, especially for neural networks, though the overall
behaviour should match.)

## Real data: the sunspot series

Finally the same recipe is applied to the yearly total sunspot number series ($n = 325$), a
genuine dataset rather than a simulation. It is standardized and used directly, without batching
(the series is short enough that the full unrolled sequence is cheap), and an LSTM is trained to
forecast 300 steps ahead, again by the closed-loop, feed-the-last-output-back-in procedure above.
With hidden size 64, 1000 epochs bring the training loss down from about 0.18 to about 0.015; with
a larger hidden size of 200, the loss falls much further, to about 0.0016, over the same number of
epochs. The resulting LSTM forecasts look qualitatively realistic — the notebook describes them as
continuing to oscillate well into the future in a way that is visually similar to the true
series — which it contrasts with the character of an AR($p$) forecast, said to oscillate briefly
before settling down to a constant value.

## Sources

- Berkeley STAT 153, Code Lecture 26 ("LSTM (and RNN, GRU) fitting"), two taught instances:
  - Fall 2025:
    [`01-the-lstm-unit.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb) —
    the LSTM unit as a black box, parameter shapes.
    [`02-simulated-dataset-one.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb) —
    the forecasting wrapper, the period-85 and period-344 case studies, start of the sunspots
    section.
    [`03-lstm-for-sunspots.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb) —
    LSTM fit to the sunspot series (hidden size 64).
    [`06-simulation-three.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb) —
    the nonlinear-dynamics case study, oracle predictions, and the RMSE-versus-median-absolute-error
    discussion.
  - Spring 2025:
    [`01-the-lstm-unit.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) —
    parallel treatment of the LSTM unit.
    [`02-simulated-dataset-one.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) —
    source of the "Speed versus memory: batching a long sequence" section (batching to 450- and
    650-step chunks; this instance is not present in the fall notebook pages supplied).
    [`03-lstm-for-sunspots.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) —
    LSTM fit to the sunspot series with hidden size 200, used for the loss comparison.
- No slide deck or spoken transcript was supplied for this lecture; both instances were converted
  directly from their Jupyter notebooks (route: notebook, fidelity: lossless), so the code cells
  and their printed output are the primary source, and the exposition here follows the prose the
  notebooks already contain between cells.
- Named but not contained in the supplied material: the PyTorch `nn.LSTM` documentation
  (<https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html>), which the lecture points to for
  the actual gate update formulas rather than deriving them; the GRU sections and the "RNN for
  Sunspots" / "GRU for Sunspots" pages referenced by both notebooks' internal links but not among
  the files supplied for this chapter; and an AR($p$) forecast of the sunspot series itself, whose
  qualitative behaviour is described in `03-lstm-for-sunspots.md` (fall and spring) but whose
  fitting code is not shown in the supplied pages.

---

[← 57. Identifying and Fitting ARIMA Models](57-identifying-and-fitting-arima-models.md) · [Contents](index.md) · [59. Multiplicative Seasonal ARMA Models →](59-multiplicative-seasonal-arma-models.md)
