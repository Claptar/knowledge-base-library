---
title: Write the training and test functions
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Write the training and test functions

**Source:** [`public/labs/Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Remember you need to downsample the data to 8000 Hz (using the `transform` function) before you put it into the model!

```python
# Run this cell first

# Helper: count how many predictions match the target labels in one batch.
# .squeeze() drops any dimensions of size 1; .eq() is elementwise equality;
# .sum() counts the Trues; .item() pulls a Python scalar out of a 0-D tensor.
def number_of_correct(pred, target):
    return pred.squeeze().eq(target).sum().item()

# Classifier outputs one logit per class; argmax over the class dim = predicted label.
def get_likely_index(tensor):
    return tensor.argmax(dim=-1)

# --- Training ingredients ---
# Optimizer: the algorithm that updates weights given gradients. SGD is the
# classic; Adam (used later for input optimization) is an adaptive variant.
# model.parameters() gives the optimizer the list of tensors it's allowed to change.
optimizer = torch.optim.SGD(model.parameters(), lr=.005)  # Try lr=0.05

# Learning-rate scheduler: multiplies lr by gamma every step_size epochs.
# Common pattern — start with a larger lr, drop it later to fine-tune.
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.1)

# CrossEntropyLoss expects raw logits (not softmaxed) and integer class labels.
# It combines log-softmax + negative log likelihood in one numerically stable op.
lossfunction = nn.CrossEntropyLoss()
```

```python
# One pass through the training set = one epoch.
#
# The canonical PyTorch training step is always these four calls, in this order:
#   1. optimizer.zero_grad()   -- clear gradients from the previous batch
#   2. outputs = model(inputs) -- forward pass; builds the autograd graph
#   3. loss.backward()         -- backprop; fills .grad on every parameter
#   4. optimizer.step()        -- apply the update to the weights
#
# Skipping zero_grad is a common bug: PyTorch accumulates gradients by default.
def train_one_epoch(model):
    model.train()
    total_loss = 0
    count = 0
    for inputs, labels in train_loader:
        # Zero out the gradients
        optimizer.zero_grad()

        # Downsample the audio data to 8000 Hz
        transformed_inputs = transform(inputs)

        # Run the model on the inputs to get output
        outputs = model.forward(transformed_inputs)

        # Compute the loss
        loss = lossfunction(outputs, labels)

        # Do backprop (compute derivatives for every step)
        loss.backward()

        # Take a step along the gradients and update
        optimizer.step()
        # loss is a 0-D tensor; .item() pulls the Python float so we can
        # accumulate without keeping the computation graph around.
        total_loss += loss.item()
        count += 1
    print('{:>12s} {:>7.5f}'.format('Train loss:', total_loss/count))


# Evaluation loop.
# In a larger project you'd wrap this in `with torch.no_grad():` to save memory,
# and call model.eval() to disable dropout / switch BatchNorm to inference mode.
def test(model):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels  in test_loader:
            transformed_inputs = transform(inputs)
            outputs = model.forward(transformed_inputs)
            total += len(outputs)
            correct += number_of_correct(labels, get_likely_index(outputs))
    print('%s accuracy: %0.3f' % ("Test", correct/total))
```

---

[← Define model](03-define-model.md) · [Up: contents](index.md) · [Fit the model! Tweak until you get test accuracy of at least 80% →](05-fit-the-model-tweak-until-you-get-test-accuracy-of-at-least.md)
