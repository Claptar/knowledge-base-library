---
title: In our setting
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# In our setting

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_X_ Joint probabilty function : _P_ ( _x_ 1 , _x_ 2<sup>,</sup> _x_ ) _f_ 3<sup>=</sup> ∏ _j_<sup>(</sup> _j_<sup>)</sup> ∈ _j J_

Variable node, _x_ = state of gene/protein/pathway

Factor node, _f_ describes relationships


<!-- Start of picture text -->
x3<br>f<br>x1 x2<br><!-- End of picture text -->

Edge exists iff x is an argument of f

Factor graph

###### _x x x x x_ <u>Global function:</u> _g_ ( 1, 2, 3, 4, 5 )

<u>Marginal</u> _gi_<sup>(</sup> _a_<sup>)</sup> : sum _g_ ( _x_ 1, _x_ 2, _x_ 3, _x_ 4, _x_ 5 ) over all configurations of the variables with xi=a


What is the probability that MYC/MAX is active?

P(xi=active)

Factor graphs provide a method to compute such marginals

© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Goldstein, Theodore C., Evan O. Paull, et al. "Molecular Pathways: Extracting Medical Knowledge from High-throughput Genomic Data." _Clinical Cancer Research_ 19, no. 12 (2013): 3114-20.

###### <u>Global function:</u>

_x x x x x x x x x x x x g_ ( _x_ 1, _x_ 2, 3, 4, 5  ) = _f A_ ( 1 ) _f B_ ( 2 ) _fC_ ( 1, 2, 3 ) _f D_ ( 3, 4 ) _f E_ ( 3, 5 ) _x x x_ <u>Marginal</u> _gi_ ( _a_ ) : sum _g_<sup>(</sup> _x_ 1<sup>,</sup> _x_ 2, 3, 4, 5 ) over all configurations of the variables with xi=a _x_ × _g_ 1( _x_ 1 ) = _f A_ ( 1 )     <sup></sup>  _f_ ( _x_ )  _f_ ( _x_ 1, , _x_ 2 _x_ ) _f D_ ( _x_ 3, _x_ ) _f_ ( _x_ 3, _x_ )  <sup>∑</sup><sup>_B_</sup> 2 ∑ _C_ 3<sup></sup> ∑ 4<sup></sup> ∑ _E_ 5<sup></sup>  <sup>_x_</sup> 2 <sup>_x_</sup> 3 <sup>_x_</sup> 4 <sup>_x_</sup> 5  x1 x2 x3 x4 x5 fA fB fC fD fE

###### <u>Global function:</u>

_x x x x x x x x x x g_ ( _x_ 1, _x_ 2, 3, 4, 5 ) = _f A_ ( 1 ) _f B_ ( 2 ) _fC_ ( 1, 2, 3) _f D_ ( _x_ 3, _x_ 4 ) _f E_ ( 3, 5 ) _x x x x x_ <u>Marginal</u> _gi_ ( _a_ ) : sum<sup>_g_(</sup> 1<sup>,</sup> 2, 3, 4, 5 ) over all configurations of the variables with xi=a = _x x x x x gi_ ( _xi_ ) _g_ ( 1, 2, 3, 4, 5 ) ∑ _x_ ~{ _i_ } “not-sum” or summary over all values of xj≠i x1 x2 x3 x4 x5 fA fB fC fD fE

###### <u>Global function:</u>


<!-- Start of picture text -->
x x x x x x x x x x x x<br>g ( x 1, x 2, 3, 4, 5  )  = f A ( 1 ) f B ( 2 ) fC ( 1, 2, 3 ) f D  ( 3, 4 ) f E ( 3, 5 )<br>x x x<br>Marginal gi ( a ) : sum  g ( x 1 , x 2, 3, 4, 5  )<br>over all configurations of the variables with xi=a<br>x ×<br>g 1( x 1 )  = f A ( 1 )<br>     <br> f ( x )   f ( x 1, x 2, x )  f D ( x 3, x  ) f ( x 3, x  ) <br> ∑ B 2 ∑ C 3  ∑ 4  ∑ E 5  <br>x x<br> 2  3   x 4  x 5  <br>x ×<br>g 1( x 1 )  = f A ( 1 )<br>    <br>x x x x x x<br> f B ( 2 )  fC ( 1, 2, )  f D ( 3,  ) f ( x 3, x  ) <br>∑  3   ∑ 4     ∑ E 5  <br>x x<br>~{ x 1 }   ~{ 3}  ~{ 3 }  <br><!-- End of picture text -->

<u>Global function:</u> _x x x x x x x x x x g_ ( _x_ 1, _x_ 2, 3, 4, 5 ) = _f A_ ( 1) _f B_ ( 2 ) _fC_ ( 1, 2, 3) _f D_ ( _x_ 3, _x_ 4 ) _f E_ ( 3, 5 )


<!-- Start of picture text -->
How do we find the marginal for any factor graph?<br>x1  x2 x3 x4  x5<br>fA fB fC fD  fE<br><!-- End of picture text -->

###### To compute the marginal with respect to variable xi : draw the factor graph as a tree with root xi


<!-- Start of picture text -->
© IEEE. All rights reserved. This content is excluded from our Creative Commons<br>license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Source: Kschischang, Frank R., Brendan J. Frey,et al. "Factor Graphs<br>and the Sum-product Algorithm."  Information Theory, IEEE Transactions on  47,<br>no. 2 (2001): 498-519.<br>x1  x2  x3 x4  x5<br>fA fB fC fD  fE<br><!-- End of picture text -->

###### **Expression Tree**

###### **Factor Graph**


© IEEE. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Kschischang, Frank R., Brendan J. Frey,et al. "Factor Graphs

and the Sum-product Algorithm." _Information Theory, IEEE Transactions on_ 47, no. 2 (2001): 498-519.

###### <u>Marginal:</u>


<!-- Start of picture text -->
x ×<br>g 1( x 1 )  = f A ( 1 )<br>   <br>x x x x x x<br> f ( 2 )  fC ( 1, 2, )  f D ( 3,  ) f ( x 3, x  ) <br>∑  B 3   ∑ 4      ∑ E 5   <br>x x<br>~{ x 1 }   ~{ } 3  ~{ }  3  <br><!-- End of picture text -->


<!-- Start of picture text -->
Compute product of “summary”<br>function for parent variable<br>Compute “summary” function<br>for parent variable<br>© IEEE. All rights reserved. This content is excluded from our Creative Commons<br>license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Source: Kschischang, Frank R., Brendan J. Frey,et al. "Factor Graphs<br>and the Sum-product Algorithm."  Information Theory, IEEE Transactions on  47,<br>no. 2 (2001): 498-519.<br>Marginal:<br>x ×<br>g 1 ( x 1 )  = f A ( 1 )<br>    <br>x x x<br> f B ( x 2 ) fC  ( x 1 , x 2  , 3  )  f D ( 3 , 4  )  f E ( x 3 , x 5  )  <br>∑ ∑ ∑<br>    <br>x x x<br>~{ 1 }    ~{ } 3   ~{ } 3   <br><!-- End of picture text -->

###### <u>Marginal:</u>


© IEEE. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Kschischang, Frank R., Brendan J. Frey,et al. "Factor Graphs and the Sum-product Algorithm." _Information Theory, IEEE Transactions on_ 47, no. 2 (2001): 498-519.

- Messages flow up from leaves:

- •Each vertex waits for messages from all children before computing message to send to parents

- •Variable nodes send product of messages from children

- •Factor nodes with parent x send the “summary” for x of the product of the children’s functions.

Kschischang, F.R.; Frey, B.J.; Loeliger, H.-A., "Factor graphs and the sum-product algorithm," 2001 <u>http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=910572&isnumber=19638</u>

**Belief propagation:** An algorithm known as “Sum-Product” can be used to simultaneously compute all marginals! See citation for details


© IEEE. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Kschischang, Frank R., Brendan J. Frey,et al. "Factor Graphs and the Sum-product Algorithm." _Information Theory, IEEE Transactions on_ 47, no. 2 (2001): 498-519.

Kschischang, F.R.; Frey, B.J.; Loeliger, H.-A., "Factor graphs and the sum-product algorithm," 2001 http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=910572&isnumber=19638

---

[← Factor graphs](05-factor-graphs.md) · [Up: contents](index.md) · [Factor graphs in PARADIGM →](07-factor-graphs-in-paradigm.md)
