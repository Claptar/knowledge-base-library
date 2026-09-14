---
title: Usage
source: https://github.com/pachterlab/biophysics/blob/ca6fe2ae824eb4cc3508ce951e1a7a868f50a043/docs/source/usage.rst
source_file: sources/pachter-biophysics-docs/docs/source/usage.rst
licence: BSD-2-Clause
route: pandoc-rst
fidelity: high
converted: '2026-09-14'
---

# Usage

**Source:** [`docs/source/usage.rst`](https://github.com/pachterlab/biophysics/blob/ca6fe2ae824eb4cc3508ce951e1a7a868f50a043/docs/source/usage.rst) · **Licence:** BSD-2-Clause · Converted 2026-09-14 from `.rst` (high)

## Installation {#installation}

To use Lumache, first install it using pip:

``` console
(.venv) $ pip install lumache
```

## Creating recipes {#creating-recipes}

To retrieve a list of random ingredients, you can use the `lumache.get_random_ingredients()` function:

lumache.get\_random\_ingredients

The `kind` parameter should be either `"meat"`, `"fish"`, or `"veggies"`. Otherwise, `lumache.get_random_ingredients` will raise an exception.

lumache.InvalidKindError

For example:

&gt;&gt;&gt; import lumache &gt;&gt;&gt; lumache.get\_random\_ingredients() $$'shells', 'gorgonzola', 'parsley'$$

---

[Up: contents](../../index.md)
