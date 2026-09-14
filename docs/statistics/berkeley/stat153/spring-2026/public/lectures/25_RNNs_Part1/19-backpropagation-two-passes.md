---
title: 'Backpropagation: Two passes'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/25_RNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Backpropagation: Two passes

**Source:** [`public/lectures/25_RNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- _hℓ_ = _fℓ_ ( _hℓ_ −1; _Wℓ_ ), ℒ= Loss(̂ _y_ , _y_ )

- **Forward pass:**

   - <sup>Compute and cache</sup> _h_ 1, _h_ 2, …,̂ _y_ , then the loss

- **Backward pass:**

   - <sup>Starting from</sup> ∂ℒ/∂̂ _y_ , walk backward through the layers. At each layer, we use the chain rule:

      - ∂∂ℒ _Wℓ_ =<sup>∂ℒ</sup> ∂ _hℓ_ ⋅ ∂<sup>∂</sup> _W_<sup>_hℓ_</sup> _ℓ_ , ∂∂ℒ _hℓ_ −1 =<sup>∂ℒ</sup> ∂ _hℓ_ ⋅ ∂<sup>∂</sup> _h_<sup>_h_</sup> _ℓ_ −1<sup>_ℓ_</sup>

      - <sup>The first equation gives the gradient to update</sup> _Wℓ_ , the second is the upstream gradient passed to the previous layer

#### **Backpropagation through time for RNN Training**

- BPTT is _mostly_ the same as normal BP


<!-- Start of picture text -->
Loss ( yt,  ˆ yt )<br>@Loss<br>@  ˆ yt<br>y<br>h h h h<br>x x x x<br><!-- End of picture text -->

#### **Backpropagation through time for RNN Training**

##### • BPTT is _mostly_ the same as normal BP


<!-- Start of picture text -->
Loss ( yt,  ˆ yt )<br>@Loss<br>@  ˆ yt<br>y<br>@  ˆ yt<br>@ht<br>h h h h<br>@ht<br>@ht− 1 @ht , @ht<br>@Wxh @bh<br>x x x x<br><!-- End of picture text -->

#### **Backpropagation through time for RNN Training**

##### • BPTT is _mostly_ the same as normal BP


<!-- Start of picture text -->
Loss ( yt,  ˆ yt )<br>@Loss<br>@  ˆ yt<br>y<br>@  ˆ yt<br>@ht<br>h h h h<br>@ht<br>@ht− 1 @ht , @ht<br>@Wxh @bh<br>x x x x<br><!-- End of picture text -->

#### **Backpropagation through time for RNN Training**

- BPTT is _mostly_ the same as normal BP


<!-- Start of picture text -->
• … but with one caveat Loss ( yt,  ˆ yt )<br>@Loss<br>@  ˆ yt<br>y<br>@  ˆ yt<br>@ht<br>Where<br>h h h h<br>do you<br>@ht<br>@ht− 1 @ht<br>stop?!?<br>, @ht<br>@Wxh @bh<br>x x x x<br><!-- End of picture text -->

#### **Backpropagation through time for RNN Training**

- Except in some very specific circumstances, most RNNs are trained using **truncated BPTT** :

   - Instead of back-propagating forever, choose some BPTT length, **_k_**

   - Then only back-propagate for **_k_** time steps

- <sup>_Truncated BPTT is so common that we don’t even usually call it “truncated_</sup> _BPTT”, we just call it “BPTT”_

#### **Backpropagation through time (BPTT) for RNNs**

- An RNN unrolled over T timesteps is a deep feedforward network with two changes:

   - <sup>the same parameters</sup> _Wh_ and _Wx_ are reused at every time step

   - Gradients flow backward through the time step chain

_T_ ∂ℒ ∂ℒ _t_ = • ∑ ∂ _Wh_ ∂ _Wh t_ =1 • Each of these terms requires propagating gradients back through all earlier timesteps via repeated multiplication by ∂ _ht_ /∂ _ht_ −1

---

[← Backpropagation](18-backpropagation.md) · [Up: contents](index.md) · [Why RNNs vs. CNNs? →](20-why-rnns-vs-cnns.md)
