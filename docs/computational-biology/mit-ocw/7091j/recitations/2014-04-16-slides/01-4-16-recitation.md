---
title: 4-16 Recitation
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-16-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-04-16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4-16 Recitation

EF Lecture #1

## Boolean Framework

- Often used on top of the network structure to explain experimental observations
- Variables (nodes – e.g. TFs or signaling molecules) are ON/OFF
- We connect nodes through AND & OR logic gates to represent cellular interactions & pathways

```
       A          B          C
        \       /   \NOT   /
         \     /     \    /
          v   v       v  v
           AND         AND
            |           |
            v           v
            E           F
             \         /
              \       /
               v     v
                 OR
                  |
                  v
            +---> G
            |     |
           NOT    v
            |     S
            |
            +--- (from A)
```

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Boolean Framework

- Often used on top of the network structure to explain experimental observations
- Variables (nodes – e.g. TFs or signaling molecules) are ON/OFF
- We connect nodes through AND & OR logic gates to represent cellular interactions & pathways
- We can then perturb the variables *in silico* to predict outcomes if we introduce a therapeutic

---

---

[Up: contents](index.md) · [Sample Experimental Data →](02-sample-experimental-data.md)
