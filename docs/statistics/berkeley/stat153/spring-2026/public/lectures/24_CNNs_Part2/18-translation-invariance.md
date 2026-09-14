---
title: Translation invariance
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/24_CNNs_Part2.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Translation invariance

**Source:** [`public/lectures/24_CNNs_Part2.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Object classes are **_translation invariant_**

- i.e., object class (mostly) doesn’t depend on where the object is within the image

## **Convolutional layer**

- Idea 2: **_translation invariant networks_**

- Instead of learning a separate set of weights for each “localized” unit, let’s learn **one** set of weights that is **shared** across all the localized units

- This operation—applying the same “filter” to each patch in the image— resembles **convolution** of the image with a filter/kernel

   - So let’s call it a “convolutional layer”

## **Convolutional layer**

_Input: 196,608 features_

- Using convolution makes it easy to add more “feature detectors” for each location in the image

- Instead of training 4096 detectors (one for each location), we can just train (e.g.) 96, each of which is **shared** across the 4096 locations


<!-- Start of picture text -->
…<br>96 localized<br>unit TYPES<br>(4096 of each) 1000 hidden<br>units<br><!-- End of picture text -->

_1000 output units_

## **Convolutional layer**

_Input: 196,608 features_

- This network is better, and doesn’t have too many weights!

- But it’s still not very expressive

- This could be improved by making it deeper, but that’s expensive


<!-- Start of picture text -->
…<br>96 localized<br>unit TYPES<br>(4096 of each) 1000 hidden<br>units<br><!-- End of picture text -->

_1000 output units_

## **Convolutional layer**

- Convolutional layers enable us to detect whether the same feature appears at any location in the image

- But what we are ultimately concerned with is whether some feature (e.g. a dog) appears **_anywhere_** in the image


## **Convolutional layer**

- We can try to find things “anywhere in the image” with **_max pooling_**

- Instead of directly using the output of one convolutional layer as the input for the next, we reduce the “image size” at each layer by **pooling** the activations across adjacent units

- Taking the **maximum** across a group of units is like a logical OR, captures the “anywhere” property

_Input: 196,608 features_


<!-- Start of picture text -->
…<br>96 localized<br>unit TYPES<br>(4096 of each)<br>max pooling<br>layer<br>1000 hidden<br>units<br>1000 output<br>units<br><!-- End of picture text -->

## **Sound classification**

- **Problem:** we want to classify _sounds_ , represented as waveforms

   - Each sound comprises (up to) 16000 samples

   - * Can we apply the same tricks as for images?


<!-- Start of picture text -->
“backward”<br><!-- End of picture text -->

## **Sound classification**

- Solution: **1-D convolution** !


_from https://en.wikipedia.org/wiki/Convolution_

## **Sound classification**

- Solution: **1-D convolution** !

_(f is length T vector, h and g_ * Assuming: _f 2 R_<sup>_T_</sup> _, {h, g} 2 R_<sup>_n_</sup> _are length n vectors)_

_1_ * Definition: ( _f ? g_ )[ _t_ ] = _f_ [ _t_ ] _g_ [ _t − ⌧_ ] _greater than n or less than 1)(defining g[.]=0 for indices_ X _⌧_ = _−1_

_n_ * Or: ( _f ? h_ )[ _t_ ] = _f_ [ _t − ⌧_ ] _h_ [ _⌧_ ] = _f_ [ _t − n_ : _t_ ] _· h_ X _⌧_ =1

## **Sound classification**

- We can stack multiple convolutional filters (aka kernels) into a **1-D convolutional layer** :

   - Let _g_ 1 _. . . gk_ be a set of length-n vectors, and  be a length-T vector (input) _x_

   - Define


<!-- Start of picture text -->
g 1  ? x<br>2 3<br>g 2  ? x<br>g ( x ) =<br>. . .<br>gk ? x<br>664 775<br><!-- End of picture text -->

## **Sound classification**

- Then we can:

   - apply a nonlinearity (e.g. ReLU) to the results

   - downsample the results using **max-pooling** or **average-pooling**

   - (maybe pass the results into a fully-connected layer?)

## **Sound classification**

- Example: **M3** (Dai et al., 2016)


## **Sound classification**

- 1-D convolutional networks!

   - (they’re pretty much the same as 2-D convolutional networks, so far)

   - You’ll see a demo in lab!

---

[← Image Classification](17-image-classification.md) · [Up: contents](index.md)
