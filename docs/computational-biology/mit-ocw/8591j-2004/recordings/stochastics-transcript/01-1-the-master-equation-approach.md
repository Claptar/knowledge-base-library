---
title: 1. THE MASTER EQUATION APPROACH
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/stochastics-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. THE MASTER EQUATION APPROACH

**Source:** `recordings/stochastics-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The master equation corresponds to the statement that the probability of being in a given state changes depending on the probabilities of transition to and from any other state in the system. It provides the full probability distribution when it can be directly solved. Unfortunately, this is not often the case, so we must settle for some of the moments of the distribution. These are easily obtained from the generating function, so we will work with the master equation in a form in which it depends on the generating function rather than the distribution.

The genetic network is defined by _N_ state variables _n1 .. nN_ and _M_ rate constants _k1 .. kM_ . The variables denote the number of copies of a certain chemical species such as mRNAs or proteins. Before applying the master equation approach to determine the noise properties of a genetic network we will start by obtaining the master equation in the generating function form for some elementary chemical equations:

_Synthesis from a template_

In numerous genetic reactions, such as transcription and translation, mRNAs and proteins are synthesized from a template (DNA and mRNA, respectively). After synthesis the number of templates is not changed. The corresponding reaction is therefore:


concentrat ion −1 Molecule A produces molecule B at a rate _k_ (in units of ( × time) ). The master equation describes how the probability to be in state [ _n1, n2_ ] ( _n1_ A molecules, _n2_ B molecules) at time _t_ changes in time. For the reaction above:


The first term reflects a transition from state [ _n1, n2_ ] to state [ _n1, n2+1_ ] and therefore leads to a decrease in _p_ ( _n_ 1, _n_ 2 , _t_ ) . The second term denotes the transition [ _n1, n2-1_ ] → [ _n1, n2_ ] and leads to an increased _p_ ( _n_ 1, _n_ 2 , _t_ ) . The master equation above is linear and can be solved for the moments by constructing the moment generating function. In general for _N_ system variables the moment generating function is given by:


1

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

where the sum runs over all possible states for each _ni_ (in this case, from 0 to ∞ ). This function has the following useful properties:


where 1  means that the function is evaluated at _zj_ = 1 for all _j_ . These expressions justify the name “moment generating”:  we can obtain the moments of the probability distribution by evaluating the partial derivatives of the function.

Multiplying the master equation above by _z_ 1 _n_ 1 _z_ 2 _n_ 2 on both sides gives:


This equation can be simplified significantly by realizing that:


where the change in the lower limit of the sum for _n2_ is allowed because _p_ ( _n_ 1 ,−,1 _t_ ) = .0 This leads to:


In the special case of synthesis from a fixed number of templates ( _n1_ = _n_ ), the equation for the moment generating function reduces to:


This equation can be explicitly solved, but in itself it does not represent the full process. We therefore will obtain the expressions for the other terms before combining them to model a real situation.

---

[Up: contents](index.md) · [Degradation →](02-degradation.md)
