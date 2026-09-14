---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`public/labs/Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

# Lab 12: Convolutional Neural Networks

Here we will implement a CNN to classify spoken numerals.

Please follow <a href="https://pytorch.org">these instructions</a> to install pytorch.

Run the first two cells to import the relevant libraries

```python
!pip3 install torch torchvision torchaudio torchcodec
import os
# Prevents an OpenMP conflict between numpy and torch on macOS; harmless elsewhere
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import numpy
import torch

# Run these two blocks to load important libraries and set things up
import torch
from torch import nn   # nn = neural-network building blocks (layers, loss functions, Module base class)
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
```

```python
# Set the random seed.
# Seeding all three (numpy, torch CPU, torch CUDA) + disabling cudnn's nondeterministic
# kernels is how you get reproducible runs across CPU/GPU.
seed = 42

np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
torch.cuda.manual_seed(seed)
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True
```

## 1-D CNNs and model interpretation

In this problem you will train a 1-D CNN on audio data, here to classify spoken numerals (e.g. "one", "two"). Then you will use additional techniques to interpret (since it's audio, one can't really say "visualize", but same idea) what the model is doing. Run these cells first to set things up.

**About the data.** `torchaudio.datasets.SPEECHCOMMANDS` is a PyTorch `Dataset` object wrapping Google's Speech Commands corpus. A `Dataset` in PyTorch is any object with `__len__` and `__getitem__` — indexing into it returns one sample. Here each sample is a tuple `(waveform, sample_rate, label, speaker_id, utterance_number)`. The dataset handles the download, caching, and file I/O for us.

```python
import IPython.display as ipd

import torchaudio
from torchaudio import datasets as audiodatasets

# We will download the data here ... it's big so it might take a bit
audio_save_dir = './'#SPEECHCOMMANDS_data' # set to wherever you want to keep these files
sc_training = audiodatasets.SPEECHCOMMANDS(audio_save_dir, download=True, subset="training")
sc_validation = audiodatasets.SPEECHCOMMANDS(audio_save_dir, download=True, subset="validation")
sc_testing = audiodatasets.SPEECHCOMMANDS(audio_save_dir, download=True, subset="testing")
```

```python
# the audio will be downsampled to 8 kHz to make it easier to work with. just run this
new_sample_rate = 8000
transform = torchaudio.transforms.Resample(orig_freq=16000, new_freq=new_sample_rate)
```

```python
# the dataset contains a lot of words, but let's focus on the numbers
# this cell can take some time to run, so just keep waiting if it seems like
# it is stuck
sel_labels = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

training_inds = np.array([ii for ii,datum in enumerate(sc_training) if datum[2] in sel_labels])
validation_inds = np.array([ii for ii,datum in enumerate(sc_validation) if datum[2] in sel_labels])
testing_inds = np.array([ii for ii,datum in enumerate(sc_testing) if datum[2] in sel_labels])
```

```python
# Utility: pad each sample in a batch to the same length.
# Audio clips have different durations, but tensors in a batch must be the same
# shape. torch.nn.utils.rnn.pad_sequence pads the short ones with zeros at the end.
def pad_sequence(batch):
    # Each item comes in as shape (1, time); .t() transposes to (time, 1) because
    # pad_sequence expects the variable-length axis first.
    batch = [item.t() for item in batch]
    batch = torch.nn.utils.rnn.pad_sequence(batch, batch_first=True, padding_value=0.)
    # Permute back to (batch, channels, time) — the shape Conv1d expects.
    return batch.permute(0, 2, 1)
```

**`DataLoader` and `collate_fn`.** A `DataLoader` wraps a `Dataset` and yields *batches* during training — it handles shuffling, batching, and (optionally) parallel loading with worker processes. The `collate_fn` argument tells it how to combine a list of individual samples into one batch tensor. We need a custom one here because (a) the raw samples come with extra metadata we don't want and (b) they have different lengths and need padding. `SubsetRandomSampler` restricts each loader to the indices we computed above (only samples whose label is a digit).

```python
# make data loaders
from torch.utils.data.sampler import SubsetRandomSampler

def collate_fn(batch):
    tensors, targets = [], []
    for waveform, _, label, *_ in batch:
        tensors += [waveform]
        targets += [torch.Tensor([sel_labels.index(label)]).squeeze().long()]

    tensors = pad_sequence(tensors)
    targets = torch.stack(targets)

    return tensors, targets


batch_size = 64

train_loader = torch.utils.data.DataLoader(
    sc_training,
    batch_size=batch_size,
    collate_fn=collate_fn,
    sampler=SubsetRandomSampler(training_inds)
)
val_loader = torch.utils.data.DataLoader(
    sc_validation,
    batch_size=batch_size,
    drop_last=False,
    collate_fn=collate_fn,
    sampler=SubsetRandomSampler(validation_inds)
)
test_loader = torch.utils.data.DataLoader(
    sc_testing,
    batch_size=batch_size,
    drop_last=False,
    collate_fn=collate_fn,
    sampler=SubsetRandomSampler(testing_inds)
)
```

---

[Up: contents](index.md) · [Plot the waveform and play the audio for one training sample →](02-plot-the-waveform-and-play-the-audio-for-one-training-sample.md)
