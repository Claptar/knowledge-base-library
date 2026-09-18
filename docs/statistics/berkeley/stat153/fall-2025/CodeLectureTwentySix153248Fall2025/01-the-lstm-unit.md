---
title: The LSTM Unit
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentySix153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentySix153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentySix153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The LSTM Unit

---
title: LSTM (and RNN, GRU) fitting
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
```

Before fitting LSTM models, let us first see how the basic LSTM unit in PyTorch (nn.LSTM) works (see \url{https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html} for details). The LSTM unit can be seen as a black box which (for a fixed $p$ and $k$) holds weight matrices $W_{ii}, W_{hi}, W_{if}, W_{hf}, W_{ig}, W_{hg}, W_{io}, W_{ho}$ and bias vectors $b_{ii}, b_{hi}, b_{if} b_{hf}, b_{ig}, b_{hg}, b_{io}, b_{ho}$. In order to create the LSTM unit, we only need to specify $p$ (this is the dimension of $x_t$ and will be referred to as the input size) and $k$ (this is the dimension of $h_t$ and will be referred to as the hidden size).

```python
lstm_net = nn.LSTM(input_size = 1, hidden_size = 5, batch_first = True)
```

The above code line will create a LSTM unit and will randomly initialize all its parameters $W_{ii}, W_{hi}, W_{if}, W_{hf}, W_{ig}, W_{hg}, W_{io}, W_{ho}$ and $b_{ii}, b_{hi}, b_{if} b_{hf}, b_{ig}, b_{hg}, b_{io}, b_{ho}$. Given a sequence $x_1, \dots, x_T$ for some $T$ (here each $x_t$ needs to be of dimension input_size), the LSTM unit will then use the formulas to compute $(c_1, h_1), \dots, (c_T, h_T)$. It will output $h_1, \dots, h_T$ as well as $(h_T, c_T)$.

If we create two sets of input sequences $x_1, \dots, x_T$ and $\tilde{x}_1, \dots, \tilde{x}_T$, then the LSTM unit will use its formulae to output $h_1, \dots, h_T$ (as well as $(h_T, c_T)$) corresponding to $x_1, \dots, x_T$, as well as $\tilde{h}_1, \dots, \tilde{h}_T$, as well as $(\tilde{h}_T, \tilde{c}_T)$ corresponding to $\tilde{x}_1, \dots, \tilde{x}_T$. In general, if we send in $B$ input sequences (i.e., $B$ batches of input sequences), each sequence having length $T$ (and each $x$ in each sequence has dimension input_size), the output of the LSTM will correspond to $B$ sequences of length $T$ (each element of the sequence has dimension equal to hidden_size). The inputs and outputs can therefore both be treated as tensors. The 'batch_first = True' in the specification of lstm_net above indicates that the input tensor should have shape (B, T, input_size) and the output tensor will have shape (B, T, hidden_size). We will only use $B = 1$.

```python
#Let us create an input tensor for lstm_net:
input = torch.randn(1, 10, 1)
#this input has one batch, which is a sequence x_1, \dots, x_10 of length 10. Each x_t is a scalar (input_size = 1).
print(input)

output, (hn, cn) = lstm_net(input)

#output will have shape (1, 10, 5). It is a simply the sequence h_1, \dots, h_10 where each h_t is of dimension hidden_size = 5.
print(output.shape)

print(hn.shape) #h_n is simply the hidden vector h_t corresponding to the last time (here t = 10). You can check that hn is identical to the last element of the output

print(cn.shape) #c_n is the cell state corresponding to the last output

print(output[:, 9, :])
print(hn)
#check that hn and output[:, 9, :] are identical
```

```
tensor([[[-0.6010],
         [ 0.5618],
         [-1.5536],
         [-0.8574],
         [ 0.0943],
         [ 0.6305],
         [ 0.8702],
         [ 0.6343],
         [-0.4735],
         [ 1.1954]]])
torch.Size([1, 10, 5])
torch.Size([1, 1, 5])
torch.Size([1, 1, 5])
tensor([[ 0.0266, -0.0024, -0.1292,  0.0224,  0.0120]],
       grad_fn=<SliceBackward0>)
tensor([[[ 0.0266, -0.0024, -0.1292,  0.0224,  0.0120]]],
       grad_fn=<StackBackward0>)
```

The weight matrices $W_{ii}, W_{if}, W_{ig}, W_{io}$ as well as $W_{hi}, W_{hf}, W_{hg}, W_{ho}$, and the biases $b_{ii}, b_{if}, b_{ig}, b_{io}$ as well as $b_{hi}, b_{hf}, b_{hg}, b_{ho}$ can be accessed as follows.

```python
print(lstm_net.weight_ih_l0.shape)
print(lstm_net.weight_ih_l0) #this contains the four weight matrices W_{ii}, W_{if}, W_{ig}, W_{io}

print(lstm_net.weight_hh_l0.shape)
print(lstm_net.weight_hh_l0) #this contains the four weight matrices W_{hi}, W_{hf}, W_{hg}, W_{ho}

print(lstm_net.bias_ih_l0.shape)
print(lstm_net.bias_ih_l0)  #this contains  the four biases b_{ii}, b_{if}, b_{ig}, b_{io}

print(lstm_net.bias_hh_l0.shape)
print(lstm_net.bias_hh_l0)  #this contains  the four biases b_{hi}, b_{hf}, b_{hg}, b_{ho}

#l0 here refers to the fact that there is a single LSTM layer. Sometimes, it is common to stack multiple LSTM units, in which case there will be weights and biases for each LSTM. We will only deal with a single LSTM layer
```

```
torch.Size([20, 1])
Parameter containing:
tensor([[ 0.2603],
        [-0.2236],
        [ 0.2664],
        [ 0.1512],
        [-0.2186],
        [-0.1205],
        [-0.1810],
        [ 0.1973],
        [-0.1793],
        [ 0.1518],
        [ 0.0319],
        [-0.3571],
        [-0.2811],
        [-0.3101],
        [ 0.2343],
        [ 0.0969],
        [-0.0112],
        [-0.2663],
        [-0.4431],
        [-0.1583]], requires_grad=True)
torch.Size([20, 5])
Parameter containing:
tensor([[-0.3423, -0.4448, -0.4265, -0.2921, -0.4348],
        [ 0.1394,  0.1673,  0.1803, -0.4452,  0.2765],
        [ 0.0872,  0.2287, -0.1099,  0.2148, -0.4241],
        [ 0.1523,  0.3546,  0.1880, -0.4215, -0.1255],
        [-0.0555,  0.2343, -0.1692,  0.0643, -0.1570],
        [-0.0710, -0.0089, -0.2568, -0.3104,  0.3692],
        [ 0.3757, -0.0135,  0.3871,  0.3446, -0.2817],
        [-0.1777, -0.3072,  0.1446,  0.0113, -0.0613],
        [ 0.3320, -0.1748, -0.2448, -0.3179, -0.2275],
        [ 0.4310, -0.2174, -0.1231,  0.2016, -0.3435],
        [-0.2714,  0.3292, -0.1715, -0.2321, -0.0579],
        [-0.0637,  0.0817,  0.1640, -0.3448,  0.4064],
        [-0.4252,  0.1515, -0.1262, -0.1889,  0.4183],
        [-0.4310,  0.0305,  0.2866,  0.3998, -0.3781],
        [ 0.0539,  0.4425, -0.4381,  0.1092, -0.2802],
        [ 0.0726, -0.4045,  0.2200, -0.0992,  0.2673],
        [-0.0067, -0.0637, -0.1086, -0.4095, -0.1900],
        [ 0.0149, -0.3460,  0.3925, -0.2909, -0.1742],
        [-0.0598, -0.3623, -0.0035, -0.2154, -0.3743],
        [ 0.0110,  0.3959,  0.1101,  0.3689, -0.0044]], requires_grad=True)
torch.Size([20])
Parameter containing:
tensor([-0.1561,  0.3604, -0.2381, -0.4137,  0.0979,  0.2229, -0.2673,  0.1574,
        -0.1587, -0.0543, -0.0990, -0.0957, -0.3639,  0.1096, -0.1176,  0.3420,
         0.0746, -0.3657, -0.3402, -0.2331], requires_grad=True)
torch.Size([20])
Parameter containing:
tensor([ 0.2142, -0.2887, -0.2046,  0.0812, -0.3101, -0.2202,  0.4055, -0.2364,
        -0.1490,  0.3198,  0.1002,  0.3510, -0.3940,  0.2235, -0.0684, -0.2865,
        -0.1915, -0.4326,  0.3094, -0.0858], requires_grad=True)
```

The values that we see above for the weights and biases are randomly chosen initial values. Given some data, they will be trained so as to minimize some loss function.

---

[Up: contents](index.md) · [Simulated Dataset One →](02-simulated-dataset-one.md)
