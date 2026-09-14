---
title: RNN variants
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/25_RNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# RNN variants

**Source:** [`public/lectures/25_RNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Stacked RNNs

- Bidirectional RNNs

- Gated RNNs

## **Stacked RNN**

- Suppose there is a relationship between **xt** and **yt** , but _it’s complicated_

- How do we make the RNN _more expressive?_


<!-- Start of picture text -->
1-layer  3-layer<br>RNN<br>FF FF<br>y y y<br>h<br>h h h<br>h<br>x x x<br><!-- End of picture text -->

## **Stacked RNN**


<!-- Start of picture text -->
h 2<br>h 1<br>x<br><!-- End of picture text -->


<!-- Start of picture text -->
yt =  f ( h 2 t )<br>h 2 t =  g ( h 1 t , h 2 t− 1 )<br>h 1 t =  g ( xt, h 1 t− 1 )<br><!-- End of picture text -->

## **Stacked RNN**

- Task: part-of-speech Tagging


<!-- Start of picture text -->
Pro VB Det NN NN<br>h h h h h<br>It was a stray puppy<br><!-- End of picture text -->

- Is something wrong?

## **Stacked RNN**

- Task: part-of-speech Tagging


<!-- Start of picture text -->
Pro VB Det NN NN<br>h h h h h<br>It was a stray puppy<br><!-- End of picture text -->

- Is something wrong?


<!-- Start of picture text -->
Bidirectional  RNN<br>Pro VB Det NN NN<br>h h h h h<br>It was a stray puppy<br>h h h h h<br>Backward<br>RNN It was a stray puppy<br><!-- End of picture text -->

## **_Bidirectional_ RNN**


<!-- Start of picture text -->
Pro VB Det JJ NN<br>Concatenate!<br>h h h h h<br>It was a stray puppy<br>h h h h h<br>Backward<br>RNN It was a stray puppy<br><!-- End of picture text -->

---

[← Why RNNs vs. CNNs?](20-why-rnns-vs-cnns.md) · [Up: contents](index.md) · [RNN Variants →](22-rnn-variants.md)
