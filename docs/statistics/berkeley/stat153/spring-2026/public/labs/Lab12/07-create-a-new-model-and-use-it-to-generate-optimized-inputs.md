---
title: Create a new model and use it to generate optimized inputs
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Create a new model and use it to generate optimized inputs

**Source:** [`public/labs/Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Finally, let's try to generate new sounds that would maximally activate each of the output units in our `WordRecognizer` model. Input optimization is one type of feature visualization (in this case, "audiolization") that can help understand how a model works.

We will do this by using gradient backpropagation to generate sounds that maximally activate each of the `WordRecognizer` outputs. This requires us to define a new model, `InputOptim`, which has one parameter tensor: `optimized_input`, the input that it is trying to optimize. In its `forward` method, this model should apply the pretrained `WordRecognizer` to its `optimized_input` and return the result. We will then use some optimizer (e.g. Adam) to make the `WordRecognizer` output the desired value. We will repeat this for each of the output classes ("zero", "one", "two", etc.). Then we will check to make sure that this works correctly (after optimization, the `WordRecognizer` should be 100% certain that the optimized input belongs to the desired class) and listen to the resulting sounds.

There are two things that you should consider here:
* How should you initialize `optimized_input`? There are many possibilities, and this choice will greatly affect your result.
* How should you do the optimization? Number of epochs, weight decay, and other optimization choices will also have a big effect on your result.

**The key trick: optimizing the input instead of the weights.** Normally in PyTorch, *weights* are the learnable parameters and the *input* is fixed. Here we flip that: we freeze the trained recognizer's weights and treat the input waveform as the thing to optimize. We do this by making `optimized_input` a tensor with `requires_grad=True`, putting it into the optimizer's parameter list (via a custom `parameters()` method), and then running gradient *ascent* on the recognizer's confidence for a target class (equivalently, gradient descent on the cross-entropy loss against that target).

This is called *activation maximization* or *feature visualization*. This is the audio analog of the classic "what image most activates this neuron" plots in vision CNNs.

```python
# InputOptim: wraps the pretrained recognizer so we can optimize the input to it.
#
# Two things worth noticing:
#   * self.optimized_input is created with requires_grad=True, meaning PyTorch
#     will track gradients through it — that's what makes it optimizable.
#   * We override parameters() to return ONLY optimized_input. This way, when we
#     pass input_model.parameters() to an optimizer, the optimizer will update
#     the input waveform, NOT the recognizer's weights (which we want to keep
#     frozen from their trained values).
class InputOptim(nn.Module):
    def __init__(self, recognizer_model, input_shape=(1,1,8000)):
        super().__init__()
        self.recognizer_model = recognizer_model
        # Random initialization of the waveform we're going to optimize.
        self.optimized_input = torch.randn(size = input_shape, requires_grad=True)

    def forward(self):
        # Pass the current optimized_input through the frozen recognizer.
        return self.recognizer_model(self.optimized_input)

    # Override: optimizer will see only this one tensor, not the recognizer's weights.
    def parameters(self):
        return [self.optimized_input]
```

```python
# Train 10 InputOptim models, one per output class.
# Each run: start from random noise, tweak the waveform to maximize the
# recognizer's probability for the target digit.
targets = torch.arange(10).long()
opt_stims = []

n_epochs = 100

for t in targets:
    input_model = InputOptim(model)
    # Adam + a large lr works well here because we're optimizing in 8000-D input
    # space and the gradients are small. Same training-step pattern as before:
    # zero_grad -> forward -> loss -> backward -> step.
    optimizer = torch.optim.Adam(input_model.parameters(), lr = 1e-1)
    lossfxn = nn.CrossEntropyLoss()

    print("target: ", t)
    for epoch in range(n_epochs):
        optimizer.zero_grad()
        outputs = input_model.forward()
        # CrossEntropyLoss expects (batch, classes) logits and (batch,) labels,
        # so wrap the scalar target t in a length-1 batch dim.
        loss = lossfxn(outputs, torch.unsqueeze(t, 0))
        loss.backward()
        optimizer.step()

    # .detach() to pull the tensor out of the computation graph before converting
    # to numpy. Without it you'd get "Can't call numpy on a tensor that requires grad".
    opt_stims.append(input_model.optimized_input.detach().numpy())
```

```python
# finally, use this cell to see model predictions for the optimized inputs & listen to the sounds

def predict(tensor):
    # Use the model to predict the label of the waveform
    logits = model(tensor.unsqueeze(0))
    tensor = get_likely_index(logits)
    tensor = sel_labels[tensor.squeeze().item()]
    return logits.squeeze().detach().numpy(), tensor

for ind in range(10):
    utterance = sel_labels[ind]

    probs, pred = predict(torch.Tensor(opt_stims[ind].reshape(1,8000)))
    print(f"Expected: {utterance}. Predicted: {pred}.")

    plt.figure()
    plt.bar(range(10), np.exp(probs) / np.exp(probs).sum())
    plt.xticks(range(10), sel_labels)

    ipd.Audio(opt_stims[ind].squeeze(), rate=8000)
```

```python
ipd.Audio(opt_stims[0].squeeze(), rate=8000)
```

---

[← Create contingency matrix to show performance](06-create-contingency-matrix-to-show-performance.md) · [Up: contents](index.md) · [Lab12 Part 08 — →](08-lab12-part-08.md)
