---
title: 'Lecture 26: Recurrent neural networks part 2'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/26_RNNs_Part2.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/26_RNNs_Part2.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 26: Recurrent neural networks part 2

**Source:** [`public/lectures/26_RNNs_Part2.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/26_RNNs_Part2.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Liberty Hamilton April 30, 2026**

## **Announcements**

- For Stat248 - Final Project Instructions are on bCourses

- For Stat153 - Final Exam will be May 14 - 7-10pm, in this classroom

- No class next week, but we will have a final review session on Tuesday

- I will have regular office hours (Tuesday after class)

- Homework 5 is now optional/extra credit (3%)

- We will also have a little on pytorch with RNNs + exam review in Lab this week

## **Recap**

- Recurrent neural networks (RNNs)

   - Appropriate for problems where data have sequential dependence

   - Trainable using backpropagation through time (BPTT)

      - This is like “unrolling” the recurrent network into a (very) deep feedforward network, and then applying backpropagation

   - RNNs are great for problems like language, which requires more sequential processing than vision

## **Today**

- Gated RNNs

   - LSTMs

   - GRUs

## **More reading for today…**

- <u>The Unreasonable Effectiveness of Recurrent Neural Networks (Andrej Karpathy)</u>

- <u>Understanding LSTM Networks (Chris Olah)</u>

## **The trouble with RNNs**

• Suppose we want to predict the last word: _When she tried to print her tickets, she found that the printer was out of toner. She went to the stationery store to buy more toner. It was very overpriced. After installing the toner into the printer, she finally printed her _________

## **The trouble with RNNs**

- Suppose we want to predict the last word:

_When she tried to print her tickets, she found that the printer was out of toner. She went to the stationery store to buy more toner. It was very overpriced. After installing the toner into the printer, she finally printed her _________

~37 steps back!

## **The trouble with RNNs**

- RNNs suffer from the problems of **vanishing** and **exploding gradients**

- This problem is worse when backpropagating over a **long** sequence

   - Limits temporal dependence of functions that simple RNNs can learn

## **The trouble with RNNs**

- Simple 1-D example:


<!-- Start of picture text -->
@ht +1<br>ht +1 =  σ ( wht ) =  wσ 0 ( wht )<br>@ht<br>nonlinearity (e.g.<br>tanh, sigmoid,<br>maaybe ReLu)<br><!-- End of picture text -->

## **The trouble with RNNs**

- Simple 1-D example:


<!-- Start of picture text -->
@ht +1<br>ht +1 =  σ ( wht ) =  wσ 0 ( wht )<br>@ht<br>@ht +2<br>=  wσ 0 ( wht +1) wσ 0 ( wht )<br>@ht<br><!-- End of picture text -->

## **The trouble with RNNs**

- Simple 1-D example:

_@ht_ +1 _ht_ +1 = _σ_ ( _wht_ ) = _wσ_<sup>_0_</sup> ( _wht_ ) _@ht @ht_ +2 = _wσ_<sup>_0_</sup> ( _wht_ +1) _wσ_<sup>_0_</sup> ( _wht_ ) _@ht n−_ 1 _@ht_ + _n_ = _w_<sup>_n_</sup> _σ_<sup>_0_</sup> ( _wht_ + _j_ ) Y _@ht j_ =0

## **The trouble with RNNs**

- Simple 1-D example:


<!-- Start of picture text -->
@ht +1<br>ht +1 =  σ ( wht ) =  wσ 0 ( wht )<br>@ht<br>@ht +2<br>=  wσ 0 ( wht +1) wσ 0 ( wht )<br>@ht<br>n− 1<br>@ht + n<br>=  w n σ 0 ( wht + j )<br>Y<br>@ht<br>j =0<br>really bad<br>also bad<br><!-- End of picture text -->

## **The trouble with RNNs**

- **Vanishing gradients** occur if

   - n large, |w| < 1, or activations ht far from 0


## **The trouble with RNNs**

- **Exploding gradients** occur if

   - n large, |w| > 1


<!-- Start of picture text -->
w n<br>n<br><!-- End of picture text -->

## **The trouble with RNNs**

- How can these things be solved?

   - By breaking the chains of (1) weight multiplications, and (2) nonlinearities


<!-- Start of picture text -->
n− 1<br>@ht + n<br>=  w n σ 0 ( wht + j )<br>Y<br>@ht<br>j =0<br><!-- End of picture text -->

- Enter: **_Gated Recurrent Networks_**

## **But first, notation**

- Matrix Multiplication (*)


<!-- Start of picture text -->
0.8    0.1 0.3 0.18<br>* =<br>-0.9   0.2 -0.6 -0.39<br><!-- End of picture text -->

- “Hadamard product” ( )

   - Element-wise multiplication

   - Notice the participating matrices & output all have the same shape


<!-- Start of picture text -->
0.8   0.3 0.24<br>-0.9 -0.6 = -0.54<br><!-- End of picture text -->


## **LSTM**

- **L** ong **S** hort- **T** erm **M** emory network

- The LSTM was introduced by Hochreiter & Schmidhuber in 1997

- One example of a **gated recurrent network**

## **LSTM**

- Basic idea:

- In addition to the **hidden state** , maintain a separate **cell state** (ct) that does not pass through a non-linearity at each timestep


<!-- Start of picture text -->
ct −1 ct +2<br>ht −1 ht +2<br><!-- End of picture text -->


**LSTM vs Vanilla RNN**

## **LSTM**

- Basic idea:

- In addition to the **hidden state** , maintain a separate **cell state** (ct) that does not pass through a non-linearity at each timestep


<!-- Start of picture text -->
Element-wise<br>Element-wise<br>addition<br>multiplication<br>Input at timestep t<br><!-- End of picture text -->


## **LSTM**

- The LSTM uses a set of **gates** that can open or close to allow information to flow

   - Each gate is computed by _learning_ a function on xt and ht-1, and applying sigmoid


<!-- Start of picture text -->
ct −1 ct<br>ht −1 ht<br><!-- End of picture text -->

## **LSTM**

- The LSTM uses a set of **gates** that can open or close to allow information to flow

   - Each gate is computed by _learning_ a function on xt and ht-1, and applying sigmoid

   - The **forget gate** controls how information is removed from the cell state


<!-- Start of picture text -->
ct −1 ct<br>ht −1 ht<br>forget gate<br><!-- End of picture text -->

## **LSTM**

- The LSTM uses a set of **gates** that can open or close to allow information to flow

   - Each gate is computed by _learning_ a function on xt and ht-1, and applying sigmoid

   - The **forget gate** controls how information is removed from the cell state

   - The **input gate** controls how information is added to the cell state


<!-- Start of picture text -->
input gate<br>ct −1 ct<br>ht −1 ht<br>forget gate<br><!-- End of picture text -->

## **LSTM**

- The LSTM uses a set of **gates** that can open or close to allow information to flow

   - Each gate is computed by _learning_ a function on xt and ht-1, and applying sigmoid

   - The **forget gate** controls how information is removed from the cell state

   - The **input gate** controls how information is added to the cell state


<!-- Start of picture text -->
input gate<br>ct −1 ct<br>ht −1 ht<br>forget gate<br>output gate<br><!-- End of picture text -->

- The **output gate** controls how information from the cell state becomes output

## **LSTM**

- Each gate is computed as a learnable function of: **current input** and **previous hidden state**


<!-- Start of picture text -->
Example:<br>forget gate<br>ft =  σg ( Wf xt  +  Uf ht− 1 +  bf )<br>sigmoid nonlinearity (0…1)<br><!-- End of picture text -->

## **LSTM**

- Information can be **added to** the cell state at each timestep


<!-- Start of picture text -->
ct −1 ct<br>ht −1 ht<br><!-- End of picture text -->

## **LSTM**

- Information can also be **removed from** the cell state (or “forgotten”) at each timestep


<!-- Start of picture text -->
ct −1 ct<br>ht −1 ht<br><!-- End of picture text -->

## **LSTM**

- The new cell state is then used to construct the **output** “hidden” state


<!-- Start of picture text -->
ct −1 ct<br>ht −1 ht<br><!-- End of picture text -->

## **LSTM - Cell state** _ct_

- Like a conveyor belt - easy for info to flow unchanged


## **LSTM - gates**

- Gates are a way to let information through

- **Sigmoid neural net layer** and a **pointwise multiplication**

- Sigmoid outputs [0,1]

   - let **nothing** (0) or


- **everything** (1) through

## **LSTM - forget gate**

- The **forget gate** is multiplied by the **previous cell state** and then added to the **proposed cell state** times the **input gate**


forget gate: _ft_ = _σg_ ( _Wf xt_ + _Uf ht−_ 1 + _bf_ ) new cell state: _ct_ = _ft ◦ ct−_ 1 + _it ◦ c_ ˜ _t_

## **LSTM - forget gate**

- Why do we need this?

- “ **_The woman_** walked into the bookstore cafe, enjoying the pleasant smells of coffee, cinnamon pastries, and old books. **_She_** ordered a latte. After finishing, she paid and left. **A man** sat down at the same table. **_He_** opened a book.”


## **LSTM - input gate**

- The **input gate** is multiplied by a **proposed cell state** and then added to the **previous cell state**


input gate: _it_ = _σg_ ( _Wixt_ + _Uiht−_ 1 + _bi_ ) proposed cell _c_ ˜ _t_ = tanh( _Wcxt_ + _Ucht−_ 1 + _bc_ ) state: new cell state: _ct_ = _· · ·_ + _it ◦ c_ ˜ _t_

_element-wise or “Hadamard” product_

## **LSTM - input gate**

- The **input gate** is multiplied by a **proposed cell state** and then added to the **previous cell state**


input gate: _it_ = _σg_ ( _Wixt_ + _Uiht−_ 1 + _bi_ ) proposed cell _c_ ˜ _t_ = tanh( _Wcxt_ + _Ucht−_ 1 + _bc_ ) state: new cell state: _ct_ = _· · ·_ + _it ◦ c_ ˜ _t_

_element-wise or “Hadamard” product_

## **LSTM - output gate**

- The **output gate** is multiplied by the **current cell state** (with non-linearity applied) to form the **new hidden state**


output gate: _ot_ = _σg_ ( _Woxt_ + _Uoht−_ 1 + _bo_ )

new hidden state: _ht_ = _ot ◦_ tanh( _ct_ )

- Might output information relevant to what’s coming next (is subject singular or plural to help verb conjugation)

## **LSTM**

- All together now!

   - Input gate:

   - Forget gate:

   - Output gate:

   - Proposed cell:

   - New cell state:

   - New hidden state:


<!-- Start of picture text -->
ct −1 ct<br>ht −1 ht<br><!-- End of picture text -->

- _it_ = _σg_ ( _Wixt_ + _Uiht−_ 1 + _bi_ ) _ft_ = _σg_ ( _Wf xt_ + _Uf ht−_ 1 + _bf_ ) _ot_ = _σg_ ( _Woxt_ + _Uoht−_ 1 + _bo_ )

_c_ ˜ _t_ = tanh( _Wcxt_ + _Ucht−_ 1 + _bc_ ) _ct_ = _ft ◦ ct−_ 1 + _it ◦ c_ ˜ _t ht_ = _ot ◦_ tanh( _ct_ )

## **LSTM**

_ct_ −1 _ct ht_ −1 _ht_ All together now! _it_ = _σg_ ( _Wixt_ + _Uiht−_ 1 + _bi_ ) • Input gate: _ft_ = _σg_ ( _Wf xt_ + _Uf ht−_ 1 + _bf_ ) • Forget gate: _fitted values ot_ = _σg_ ( _Woxt_ + _Uoht−_ 1 + _bo_ ) • Output gate: _c_ ˜ _t_ = tanh( _Wcxt_ + _Ucht−_ 1 + _bc_ ) • Proposed cell: • New cell state: _ct_ = _ft ◦ ct−_ 1 + _it ◦ c_ ˜ _t_ • New hidden state: _ht_ = _ot ◦_ tanh( _ct_ )

- All together now!

## **LSTM**

- How does the LSTM solve the problems of exploding & vanishing gradients?

- Similar to our earlier 1-D example:


<!-- Start of picture text -->
@ct +1<br>ct +1 =  ft +1  ◦ ct  +  . . . ⇡ ft +1<br>@ct<br><!-- End of picture text -->

## **LSTM**

- How does the LSTM solve the problems of exploding & vanishing gradients?

- Similar to our earlier 1-D example:


<!-- Start of picture text -->
@ct +1<br>ct +1 =  ft +1  ◦ ct  +  . . . ⇡ ft +1<br>@ct<br>n<br>@ct + n<br>⇡<br>ft + j<br>Y<br>@ct<br>j =1<br><!-- End of picture text -->

## **LSTM**

- How does the LSTM solve the problems of exploding & vanishing gradients?

- Similar to our earlier 1-D example:


<!-- Start of picture text -->
@ct +1<br>ct +1 =  ft +1  ◦ ct  +  . . . ⇡ ft +1<br>@ct<br>n<br>@ct + n<br>can shrink (a bit)  ⇡<br>ft + j<br>Y<br>@ct<br>but not explode!<br>j =1<br><!-- End of picture text -->

## **LSTM**


<!-- Start of picture text -->
Max value of ft is 1<br>n− 1<br>@ht + n => in the best case, the partial<br>=  w n Y σ 0 ( wht + j ) derivative could evaluate to 1 n<br>@ht<br>j =0 @ct + n n<br>⇡<br>Max value of ’ is 0.25  σ ≈ Y ft + j<br>@ct<br>=> in the best case, the partial  j =1<br>derivative could evaluate to 0.25 n<br><!-- End of picture text -->

- How does the LSTM solve the problems of exploding & vanishing gradients?

- Similar to our earlier 1-D example:

## **LSTM visualization**

- Train an LSTM to predict the **next character** in a sequence from the previous characters

   - Network trained either on text (e.g. _War and Peace_ ) or C++ code (e.g. the Linux kernel)

- Visualizing the **cell state values** (for a few units) at each character can show a bit of what the network has learned!


_<u>From: http://karpathy.github.io/2015/05/21/rnn-effectiveness/</u>_

## **LSTM visualization**

- Train an LSTM to predict the **next character** in a sequence from the previous characters

   - Network trained either on text (e.g. _War and Peace_ ) or C++ code (e.g. the Linux kernel)

- Visualizing the **cell state values** (for a few units) at each character can show a bit of what the network has learned!


_<u>From: http://karpathy.github.io/2015/05/21/rnn-effectiveness/</u>_

## **Gated Recurrent Unit**

- <u>Kyunghyun Cho et al., 2014 and Junyoung Chung et al. 2014</u>

- Combines forget and input gates into single “update gate”


LSTM

- Merges cell state and hidden state

- Simpler than standard LSTMs, fewer parameters to fit!

GRU


### **Applications of LSTMs/RNNs**


- <u>Anumanchipalli et al. 2019</u>

- Synthesizing speech from brain data

- One of the foundational papers for speech BCI

- Used bidirectional LSTM


### **Applications of LSTMs/RNNs**


- <u>Anumanchipalli et al. 2019</u>

- Synthesizing speech from brain data

- One of the foundational papers for speech BCI

- Used bidirectional LSTM


### **Applications of LSTMs/RNNs**


- Handwriting decoding (Willett et al. 2021)


- Two layer, GRU to convert neural activity into time series of character probabilities

- GRU outperformed simple HMM decoder

### **Applications of LSTMs/RNNs**


- <u>Littlejohn et al. 2025</u>

- Real-time decoding of speech from a patient with severe paralysis and anarthria

- Architecture was RNN-T (RNNtransducer)

https://www.youtube.com/watch?v=vL7yMn6kiMg&source_ve_path=MTc4NDI0

## **So what have we learned?**

- Measures of dependence in time series signals (autocovariance/autocorrelation)

- Power spectral analysis and time-frequency analysis

- Linear and nonlinear methods for predicting time series data

   - Regression, ARIMA, state space analyses

- Cross-validation for time series and important considerations

- Modern methods for time series and sequence data (CNNs, RNNs, LSTMs)

- **_Time series are everywhere!_**

**That’s all!**

## **Course evaluations**

- Please take some time to complete your course evaluations!

- I’d love to hear what you liked, what could be improved

---

[Up: contents](../../index.md)
