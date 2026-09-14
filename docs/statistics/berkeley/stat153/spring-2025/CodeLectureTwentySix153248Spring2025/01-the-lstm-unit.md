---
title: The LSTM Unit
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentySix153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# The LSTM Unit

**Source:** [`CodeLectureTwentySix153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentySix153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Before fitting LSTM models, let us first see how the basic LSTM unit in PyTorcy (nn.LSTM) works (see \url{https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html} for details).

To create the LSTM unit, we only need to specify the input_size (this is the dimension of $x_t$) and the number of hidden units (this is the dimension of $h_t, f_t, i_t, o_t, c_t$).

```python
lstm_net = nn.LSTM(input_size = 1, hidden_size = 5, batch_first = True)
```

The above code line will create a LSTM unit and will randomly initialize all its parameters. Given a sequence $x_1, \dots, x_T$ for some $T$ (here each $x_t$ needs to be of dimension input_size), the LSTM unit will then use the formulas to compute $(c_1, h_1), \dots, (c_T, h_T)$. It will output $h_1, \dots, h_T$ as well as $(h_T, c_T)$.

If we create two sets of input sequences $x_1, \dots, x_T$ and $\tilde{x}_1, \dots, \tilde{x}_T$, then the LSTM unit will use its formulae to output $h_1, \dots, h_T$ (as well as $(h_T, c_T)$) corresponding to $x_1, \dots, x_T$, as well as $\tilde{h}_1, \dots, \tilde{h}_T$, as well as $(\tilde{h}_T, \tilde{c}_T)$ corresponding to $\tilde{x}_1, \dots, \tilde{x}_T$. In general, if we send in $B$ input sequences (i.e., $B$ batches of input sequences), each sequence having length $T$ (and each $x$ in each sequence has dimension input_size), the output of the LSTM will correspond to $B$ sequences of length $T$ (each element of the sequence has dimension equal to hidden_size). The inputs and outputs can therefore both be treated as tensors. The 'batch_first = True' in the specification of lstm_net above indicates that the input tensor should have shape (B, T, input_size) and the output tensor will have shape (B, T, hidden_size).

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
tensor([[[-0.8748],
         [-1.5131],
         [ 0.5044],
         [-0.3878],
         [ 1.0426],
         [ 0.7758],
         [-2.0535],
         [ 1.3216],
         [-0.5709],
         [-0.1411]]])
torch.Size([1, 10, 5])
torch.Size([1, 1, 5])
torch.Size([1, 1, 5])
tensor([[ 0.0240, -0.1298,  0.1951, -0.0680,  0.1436]],
       grad_fn=<SliceBackward0>)
tensor([[[ 0.0240, -0.1298,  0.1951, -0.0680,  0.1436]]],
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

#0 here refers to the fact that there is a single LSTM layer. Sometimes, it is common to stack multiple LSTM units, in which case there will be weights and biases for each LSTM. We will only deal with a single LSTM layer
```

```
torch.Size([20, 1])
Parameter containing:
tensor([[-0.2318],
        [ 0.1864],
        [ 0.2214],
        [ 0.0846],
        [ 0.1032],
        [ 0.1183],
        [-0.4182],
        [ 0.0963],
        [ 0.0765],
        [-0.1803],
        [-0.3270],
        [ 0.3187],
        [-0.1421],
        [ 0.2497],
        [-0.0431],
        [-0.4423],
        [-0.2981],
        [ 0.0622],
        [ 0.1202],
        [-0.3805]], requires_grad=True)
torch.Size([20, 5])
Parameter containing:
tensor([[-0.1067, -0.1284,  0.0910, -0.4090,  0.3202],
        [ 0.3550,  0.0644, -0.3108,  0.2166,  0.2723],
        [-0.1922, -0.1219, -0.2929, -0.4380,  0.2305],
        [-0.3198,  0.2493, -0.3492, -0.0558, -0.0403],
        [-0.0872, -0.1000,  0.3376, -0.1066,  0.2932],
        [-0.4185,  0.3633, -0.2426, -0.2061, -0.2156],
        [-0.2836, -0.1734, -0.2273,  0.0486,  0.3997],
        [-0.3430,  0.1009,  0.1448,  0.1808,  0.0743],
        [-0.0858, -0.0531, -0.2424,  0.1392, -0.2152],
        [-0.2396, -0.0764,  0.3373,  0.2089, -0.1031],
        [-0.4066,  0.0305,  0.2224,  0.3208, -0.2497],
        [ 0.3759, -0.2133, -0.1815, -0.4049,  0.1355],
        [-0.0020, -0.0276, -0.1923,  0.0173, -0.0990],
        [ 0.3280, -0.4143,  0.3849,  0.0693,  0.2058],
        [ 0.0817,  0.0821,  0.2356, -0.1024,  0.3197],
        [ 0.2500, -0.0572, -0.1750, -0.3839, -0.0397],
        [ 0.3731, -0.2695,  0.3761, -0.1600, -0.2923],
        [ 0.2802,  0.3042, -0.2077,  0.2802,  0.0779],
        [-0.1548, -0.2795, -0.3600,  0.2207,  0.0150],
        [-0.4269,  0.0217,  0.1036, -0.1682,  0.1018]], requires_grad=True)
torch.Size([20])
Parameter containing:
tensor([-0.0022,  0.4127,  0.3966, -0.2505, -0.1704, -0.3527, -0.3993, -0.0755,
         0.0578, -0.4365, -0.2093, -0.3626,  0.4391, -0.4461,  0.2969, -0.4436,
        -0.4349, -0.3425, -0.0728, -0.1951], requires_grad=True)
torch.Size([20])
Parameter containing:
tensor([ 0.2023,  0.4403, -0.0639,  0.4350, -0.3475,  0.0915,  0.3100,  0.3265,
        -0.4368, -0.2926,  0.2324,  0.0268, -0.0123,  0.1047,  0.1561,  0.1119,
        -0.2914,  0.1804, -0.3680,  0.0802], requires_grad=True)
```

The values that we see above for the weights and biases are randomly chosen initial values. Given some data, they will be trained so as to minimize some loss function.

---

[Up: contents](index.md) · [Simulated Dataset One →](02-simulated-dataset-one.md)
