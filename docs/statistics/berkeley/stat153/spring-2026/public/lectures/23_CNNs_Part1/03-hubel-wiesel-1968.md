---
title: Hubel & Wiesel 1968
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/23_CNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hubel & Wiesel 1968

**Source:** [`public/lectures/23_CNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Using CNNs to decode imagined images from the brain**


<u>Horikawa and Kamitani (2017)</u>

## **Example learned filters**


<u>Horikawa and Kamitani (2017)</u>

## **Representation Learning**

• Deep learning is fundamentally about representation learning • A representation is a symbol that approximates the entities and/or relations in the real world • Your brain has representations of the real world because it cannot actually contain the real world

How do CNNs work?

## **Important properties**

- Images, sound clips, other types of data have structure

- They can be stored as multi-dimensional arrays

- • They feature axes for which ordering matters (e.g. width vs. height, time) • One axis (the channel axis) can be used to access different views of the data (e.g. R/G/B color channels in an image, L/R of a stereo audio track)

## **Discrete convolution**


<!-- Start of picture text -->
output<br><!-- End of picture text -->

###### _input feature map_

##### _kernel_

---

[← Krizhevsky et al., 2012](02-krizhevsky-et-al-2012.md) · [Up: contents](index.md) · [Dumouilin and Visin 2018 →](04-dumouilin-and-visin-2018.md)
