---
title: Create contingency matrix to show performance
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Create contingency matrix to show performance

**Source:** [`public/labs/Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

`contingency` should be a 10x10 matrix where each row is a predicted label and each column a true label. The value of each element in this matrix should be the number of times a test example with the true label given by the column was assigned the predicted label given by the row. For example, if the predicted label for an example was "seven" but the true label was "six", then you should add one to `contingency[7,6]`. Do this for all examples in the test set.

This is a nice way to visualize how well the model is working.

```python
# Build a confusion (contingency) matrix on the test set.
all_preds = []
all_targets = []

model.eval()
# Collect predictions and true labels over the full test set.
correct = 0
total = 0

with torch.no_grad():
    for inputs, labels in test_loader:
        transformed_inputs = transform(inputs)

        # Apply the model to an input and return output
        outputs = model.forward(transformed_inputs)

        predicted = get_likely_index(outputs)
        # .extend unpacks the batch into individual tensor elements so the
        # final lists have one entry per test sample, not one per batch.
        all_preds.extend(predicted)
        all_targets.extend(labels)

# create contingency table
contingency = np.zeros((10, 10))
for i in range(len(all_preds)):
    # .detach() returns a view of the tensor with no gradient tracking —
    # needed because we're about to use it as an index, outside the graph.
    contingency[all_preds[i].detach()][all_targets[i].detach()] += 1

plt.matshow(contingency)
plt.colorbar()
```

---

[← Fit the model! Tweak until you get test accuracy of at least 80%](05-fit-the-model-tweak-until-you-get-test-accuracy-of-at-least.md) · [Up: contents](index.md) · [Create a new model and use it to generate optimized inputs →](07-create-a-new-model-and-use-it-to-generate-optimized-inputs.md)
