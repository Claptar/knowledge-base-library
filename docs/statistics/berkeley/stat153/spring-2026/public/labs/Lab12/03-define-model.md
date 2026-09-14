---
title: Define model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Define model

**Source:** [`public/labs/Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Here is where we will define our CNN model. Assume you are given the basic number of channels, `n_channels`. This model should have the following layers:

* 1-D convolutional layer with `n_channels` kernels of length 80, with a stride of 16
* 1-D batch norm layer
* ReLU
* 1-D max pooling layer with kernel size 4, stride 4
* 1-D convolutional layer with `n_channels` kernels of size 3, with a stride of 1
* 1-D batch norm layer
* ReLU
* 1-D max pooling layer with same parameters as above
* 1-D convolutional layer with `2*n_channels` kernels of size 3, with a stride of 1
* 1-D batch norm layer
* ReLU
* 1-D max pooling with same parameters as above
* 1-D convolutional layer with `2*n_channels` kernels of size 3, with a stride of 1
* 1-D batch norm layer
* ReLU
* 1-D max pooling with same parameters as above
* average pooling across all remaining timepoints (see `AdaptiveAvgPool1d`)
* flattening
* Linear layer with `2*n_channels` inputs and 10 outputs

```python
# WordRecognizer: a 1-D CNN for classifying spoken digits.
#
# Pattern for defining a model in PyTorch:
#   1. Subclass nn.Module.
#   2. In __init__, create the layers as attributes of `self`. This registers them,
#      so that model.parameters() knows about their weights.
#   3. Call super().__init__() FIRST, before creating any layers. Forgetting this
#      is a common first-time bug.
#   4. Define forward() to specify how inputs flow through the layers.
#   5. At runtime, call model(x) — NOT model.forward(x) directly — so that hooks
#      (e.g., for .eval() mode) fire correctly.
class WordRecognizer(nn.Module):
    def __init__(self, n_input=1, n_output=10, stride=16, n_channel=32):
        super().__init__()
        # nn.Sequential chains layers in order. Equivalent to writing each one out
        # in forward() with h = layer(h) — just more compact.
        self.layers = nn.Sequential(
            # Conv1d args: (in_channels, out_channels, kernel_size, stride)
            # First layer: 1 -> 32 channels, kernel spans 80 samples (= 5 ms at 16 kHz
            # but here 10 ms because we downsample to 8 kHz), stride 16 = heavy
            # downsampling right away to keep later layers cheap.
            nn.Conv1d(n_input, out_channels=n_channel, kernel_size=80, stride=stride),
            # BatchNorm1d normalizes across the batch dimension per channel.
            # Stabilizes training and often lets you use higher learning rates.
            nn.BatchNorm1d(n_channel),
            nn.ReLU(),
            # MaxPool1d(kernel=4, stride=4) downsamples by 4x, taking the max
            # in each non-overlapping window. Adds local translation invariance.
            nn.MaxPool1d(4, stride=4),
            nn.Conv1d(n_channel, out_channels=n_channel, kernel_size=3, stride=1),
            nn.BatchNorm1d(n_channel),
            nn.ReLU(),
            nn.MaxPool1d(4, stride=4),
            # Double the channel count as we downsample — standard CNN pattern:
            # spatial/temporal resolution shrinks, feature diversity grows.
            nn.Conv1d(n_channel, out_channels=2*n_channel, kernel_size=3, stride=1),
            nn.BatchNorm1d(2*n_channel),
            nn.ReLU(),
            nn.MaxPool1d(4, stride=4),
            nn.Conv1d(2*n_channel, out_channels=2*n_channel, kernel_size=3, stride=1),
            nn.BatchNorm1d(2*n_channel),
            nn.ReLU(),
            nn.MaxPool1d(4, stride=4),
            # Collapse whatever time dimension is left to size 1 by averaging.
            # This gives us a fixed-size vector regardless of input length.
            nn.AdaptiveAvgPool1d(1),
            # Flatten (batch, channels, 1) -> (batch, channels) so we can feed
            # it to a Linear layer.
            nn.Flatten(),
            # Final classifier: 64 -> 10 logits (one per digit class).
            nn.Linear(2*n_channel, n_output)
        )

    # forward() defines the computation graph. Called implicitly when you do model(x).
    def forward(self, x):
        return self.layers(x)


model = WordRecognizer(n_input=1, n_output=len(sel_labels), n_channel=32)
print(model)

# Handy utility: count trainable parameters (those with requires_grad=True).
# Useful for sanity-checking model size.
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

n = count_parameters(model)
print("Number of parameters: %s" % n)
```

---

[← Plot the waveform and play the audio for one training sample](02-plot-the-waveform-and-play-the-audio-for-one-training-sample.md) · [Up: contents](index.md) · [Write the training and test functions →](04-write-the-training-and-test-functions.md)
