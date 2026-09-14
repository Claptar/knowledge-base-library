---
title: Multiple regression FEV half 2
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_half_2.html
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_half_2.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Multiple regression FEV half 2

**Source:** [`tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_half_2.html`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_half_2.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Code <span class="caret"></span>

- <a href="#" id="rmd-download-source">Download Rmd</a>

# Tutorial 8.2: Multiple regression on the FEV dataset {#tutorial-8.2-multiple-regression-on-the-fev-dataset .title .toc-ignore}

As an exercise on multiple regression, we will analyse the FEV dataset.

# <span class="header-section-number">1</span> The FEV dataset

The FEV, which is an acronym for forced expiratory volume, is a measure of how much air a person can exhale (in liters) during a forced breath. In this dataset, the FEV of 606 children, between the ages of 6 and 17, were measured. The dataset also provides additional information on these children: their `age`, their `height`, their `gender` and, most importantly, whether the child is a smoker or a non-smoker.

# <span class="header-section-number">2</span> Goal

The goal of this experiment was to find out if smoking has an effect on the FEV of children, accounting for potential confounders.

# <span class="header-section-number">3</span> Load libraries and import the data

# <span class="header-section-number">4</span> Data tidying

# <span class="header-section-number">5</span> Data exploration

Visualize the effect of smoking on the FEV. In addition, assess all potential confounders.

# <span class="header-section-number">6</span> Data analysis

# <span class="header-section-number">7</span> Conclusion

LS0tCnRpdGxlOiAiVHV0b3JpYWwgOC4yOiBNdWx0aXBsZSByZWdyZXNzaW9uIG9uIHRoZSBGRVYgZGF0YXNldCIgICAKb3V0cHV0OgogICAgaHRtbF9kb2N1bWVudDoKICAgICAgY29kZV9kb3dubG9hZDogdHJ1ZSAgICAKICAgICAgdGhlbWU6IGNvc21vCiAgICAgIHRvYzogdHJ1ZQogICAgICB0b2NfZmxvYXQ6IHRydWUKICAgICAgaGlnaGxpZ2h0OiB0YW5nbwogICAgICBudW1iZXJfc2VjdGlvbnM6IHRydWUKLS0tCgpBcyBhbiBleGVyY2lzZSBvbiBtdWx0aXBsZSByZWdyZXNzaW9uLCB3ZSB3aWxsIGFuYWx5c2UKdGhlIEZFViBkYXRhc2V0LgoKIyBUaGUgRkVWIGRhdGFzZXQKClRoZSBGRVYsIHdoaWNoIGlzIGFuIGFjcm9ueW0gZm9yIGZvcmNlZCBleHBpcmF0b3J5IHZvbHVtZSwKaXMgYSBtZWFzdXJlIG9mIGhvdyBtdWNoIGFpciBhIHBlcnNvbiBjYW4gZXhoYWxlIChpbiBsaXRlcnMpIApkdXJpbmcgIGEgZm9yY2VkIGJyZWF0aC4gSW4gdGhpcyBkYXRhc2V0LCB0aGUgRkVWIG9mIDYwNiBjaGlsZHJlbiwKYmV0d2VlbiB0aGUgYWdlcyBvZiA2IGFuZCAxNywgd2VyZSBtZWFzdXJlZC4gVGhlIGRhdGFzZXQKYWxzbyBwcm92aWRlcyBhZGRpdGlvbmFsIGluZm9ybWF0aW9uIG9uIHRoZXNlIGNoaWxkcmVuOgp0aGVpciBgYWdlYCwgdGhlaXIgYGhlaWdodGAsIHRoZWlyIGBnZW5kZXJgIGFuZCwgbW9zdAppbXBvcnRhbnRseSwgd2hldGhlciB0aGUgY2hpbGQgaXMgYSBzbW9rZXIgb3IgYSBub24tc21va2VyLgoKIyBHb2FsCgpUaGUgZ29hbCBvZiB0aGlzIGV4cGVyaW1lbnQgd2FzIHRvIGZpbmQgb3V0IGlmIHNtb2tpbmcgaGFzIAphbiBlZmZlY3Qgb24gdGhlIEZFViBvZiBjaGlsZHJlbiwgYWNjb3VudGluZyBmb3IgcG90ZW50aWFsIGNvbmZvdW5kZXJzLgoKCiMgTG9hZCBsaWJyYXJpZXMgYW5kIGltcG9ydCB0aGUgZGF0YSAKCiMgRGF0YSB0aWR5aW5nCgojIERhdGEgZXhwbG9yYXRpb24KClZpc3VhbGl6ZSB0aGUgZWZmZWN0IG9mIHNtb2tpbmcgb24gdGhlIEZFVi4KSW4gYWRkaXRpb24sIGFzc2VzcyBhbGwgcG90ZW50aWFsIGNvbmZvdW5kZXJzLgoKIyBEYXRhIGFuYWx5c2lzCgojIENvbmNsdXNpb24KCgoKCg==

---

[Up: contents](../../../index.md)
