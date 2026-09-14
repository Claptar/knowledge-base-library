---
title: 10 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 slides

**Source:** `lectures/10-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**LECTURE 10**

# **The Bayes variations**

# **Continuous Bayes rule; Derived distributions**

- **Readings:** Section 3.6; start Section 4.1


# **Example:**

# **Review**

_pX_<sup>(</sup><sup>_x_)</sup> _fX_ (<sup>_x_)</sup> _pX,Y_ ( _x, y_ ) _fX,Y_ ( _x, y_ ) _pX,Y_ ( _x, y_ ) _fX,Y_ ( _x, y_ ) _pX|Y_ ( _x | y_ ) = _pY_ ( _y_ ) _fX|Y_ ( _x | y_ ) = _fY_ ( _y_ ) _pX_ ( _x_ ) = ￿ _y pX,Y_ ( _x, y_ ) _fX_ ( _x_ ) = ￿ _−∞∞ fX,Y_ ( _x, y_ ) _dy_

- _X_ = 1 _,_ 0: airplane present/not present

- _Y_ = 1 _,_ 0: something did/did not register on radar

# **Continuous counterpart**


# **Discrete** _X_ **, Continuous** _Y_


# **Example:**

- _X_ : a discrete signal; “prior” _pX_ ( _x_ )

- _Y_ : noisy version of _X_

- _fY |X_ ( _y | x_ ): continuous noise model

# **Continuous** _X_ **, Discrete** _Y_


**Example:**

- _X_ : a continuous signal; “prior” _fX_ ( _x_ ) (e.g., intensity of light beam);

- _Y_ : discrete r.v. affected by _X_ (e.g., photon count)

- _pY |X_<sup>(</sup><sup>_y| x_):modelofthedi</sup> s<sup>cre</sup> t<sup>er.</sup> v<sup>.</sup>

**Example:** _X_ : some signal; “prior” _fX_ ( _x_ ) _Y_ : noisy version of _X fY |X_ ( _y | x_ ): model of the noise

# **What is a derived distribution**

- It is a PMF or PDF of a function of one or more random variables with known probability law. E.g.:


<!-- Start of picture text -->
y<br>f X,Y(y,x)=1<br>1<br>1 x<br><!-- End of picture text -->

- Obtaining the PDF for


involves deriving a distribution. Note: _g_ ( _X, Y_ ) is a random variable

# **When not to find them**

- Don’t need PDF for _g_ ( _X, Y_ ) if only want to compute expected value: **E** [ _g_ ( _X, Y_ )] = ￿￿ _g_ ( _x, y_ ) _fX,Y_ ( _x, y_ ) _dx dy_

1

# **How to find them**

- **Discrete case**

- Obtain probability mass for each possible value of _Y_ = _g_ ( _X_ )


<!-- Start of picture text -->
pY  ( y ) = P ( g ( X ) =  y )<br>= ￿ pX ( x )<br>x :  g ( x )= y<br>x  y<br>g(x)<br>. .<br>. .<br>. .<br>. .<br>. .<br>. .<br>. .<br><!-- End of picture text -->

# **Example**

- Joan is driving from Boston to New York. Her speed is uniformly distributed between 30 and 60 mph. What is the distribution of the duration of the trip?

   - 200

- Let _T_ ( _V_ ) = . _V_

- Find _fT_ ( _t_ )


<!-- Start of picture text -->
f v(v )0<br>1/30<br>30 60 v0<br><!-- End of picture text -->

# **The continuous case**

- **Two-step procedure:**

- Get CDF of _Y_ : _FY_ ( _y_ ) = **P** ( _Y ≤ y_ )

- Differentiate to get


# **Example**

- _X_ : uniform on [0,2]

- Find PDF of _Y_ = _X_ 3

- **Solution:**


# **The pdf of Y=aX+b**

_Y_ = 2 _X_ + 5:


- Use this to check that if _X_ is normal, then _Y_ = _aX_ + _b_ is also normal.

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
