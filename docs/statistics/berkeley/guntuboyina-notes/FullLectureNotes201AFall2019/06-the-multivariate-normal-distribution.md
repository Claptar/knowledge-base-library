---
title: The Multivariate Normal Distribution
source: https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf
source_file: sources/berkeley-guntuboyina-notes/FullLectureNotes201AFall2019.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The Multivariate Normal Distribution

**Source:** [`FullLectureNotes201AFall2019.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall next move to the last topic of the class: the multivariate normal distribution. For this, it is helpful to know about moment generating functions of random vectors.

### **5.1 Moment Generating Functions of Random Vectors**

The Moment Generating Function of an _n ×_ 1 random vector _Y_ is defined as


for every _a ∈_ R<sup>_n_</sup> for which the expectation exists. Note that when _a_ = (0 _, . . . ,_ 0)<sup>_T_</sup> is the zero vector, it is easy to see that _MY_ ( _a_ ) = 1.

Just like in the univariate case, Moment Generating Functions determine distributions when they exist in a neighbourhood of _a_ = 0.

Moment Generating Functions behave very nicely in the presence of independence. Suppose _Y_ (1) and _Y_ (2) are two random vectors and let _Y_ = ( _Y_ (1)<sup>_T, Y_</sup> (2)<sup>_T_)</sup><sup>_T_bethevectorobtainedbyputting</sup><sup>_Y_(1)and</sup> _Y_ (2) together in a single column vector. Then _Y_ (1) **and** _Y_ (2) **are independent if and only if**


Thus under independence, the MGF factorizes and conversely, when the MGF factorizes, we have independence.

121

_CHAPTER 5. THE MULTIVARIATE NORMAL DISTRIBUTION_

122

### **5.2 The Multivariate Normal Distribution**

The multivariate normal distribution is defined in the following way.

**Definition 5.2.1.** _A random vector Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> _is said to have the multivariate normal distribution if every linear function a_<sup>_T_</sup> _Y of Y has the univariate normal distribution._

**Remark 5.2.1.** _It is important to emphasize that for Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> _to be multivariate normal,_ **_every_** _linear function a_<sup>_T_</sup> _Y_ = _a_ 1 _Y_ 1 + _. . . anYn needs to be univariate normal. It is not enough for example to just have each Yi to be univariate normal. It is very easy to construct examples where each Yi is univariate normal but a_ 1 _Y_ 1 + _· · ·_ + _anYn is not univariate normal for many vectors_ ( _a_ 1 _, . . . , an_ )<sup>_T_</sup> _. For example, suppose that Y_ 1 _∼ N_ (0 _,_ 1) _and that Y_ 2 = _ξY_ 1 _where ξ is a discrete random variable taking the two values_ 1 _and −_ 1 _with probability_ 1 _/_ 2 _and ξ is independent of Y_ 1 _. Then it is easy to see that_


_This means therefore that Y_ 2 _∼ N_ (0 _,_ 1) _(and that Y_ 2 _is independent of ξ). Note however that Y_ 1 + _Y_ 2 _is not normal as_


**Example 5.2.2.** _We have seen earlier in the class that if Z_ 1 _, . . . , Zn are_ **_independent_** _and univariate normal, then a_ 1 _Z_ 1 + _. . . anZn is normal for every a_ 1 _, . . . , an. Therefore a random vector Z_ = ( _Z_ 1 _, . . . , Zn_ )<sup>_T_</sup> _that is made up of_ **_independent_** _Normal random variables has the multivariate normal distribution. In fact, we shall show below that if Y has a multivariate normal distribution, then it should necessarily be the case that Y is a linear function of a random vector Z that is made of independent univariate normal random variables._

#### **5.2.1 Moment Generating Function of a Multivariate Normal**

Suppose _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> is multivariate normal. Let _µ_ = E( _Y_ ) and Σ = _Cov_ ( _Y_ ) be the mean vector and covariance matrix of _Y_ respectively. Then, as a direct consequence of the definition of multivariate normality, it follows that the MGF of _Y_ equals


To see why this is true, note that by definition of multivariate normality, _a_<sup>_T_</sup> _Y_ is univariate normal. Now the mean and variance of _a_<sup>_T_</sup> _Y_ are given by


_5.3. JOINT DENSITY OF THE MULTIVARIATE NORMAL DISTRIBUTION_

123

so that


Then (5.1) directly follows from the formula for the MGF of a univariate normal.

Note that the MGF of _Y_ (given by (5.1)) only depends on the mean vector _µ_ and the covariance matrix Σ of _Y_ . Thus the distribution of every multivariate normal vector _Y_ is characterized by the mean vector _µ_ and covariance Σ. We therefore use the notation _Nn_ ( _µ,_ Σ) for the multivariate normal distribution with mean _µ_ and covariance Σ.

#### **5.2.2 Connection to i.i.d** _N_ (0 _,_ 1) **random variables**

Suppose that the covariance matrix Σ of _Y_ is positive definite so that Σ<sup>_−_1</sup><sup>_/_2</sup> is well-defined. Let _Z_ := Σ<sup>_−_1</sup><sup>_/_2</sup> ( _Y − µ_ ). The formula (5.1) allows the computation of the MGF of _Z_ as follows: _MZ_ ( _a_ ) = E _e_<sup>_aT Z_</sup>


The right hand side above is clearly the MGF of a random vector having _n_ i.i.d standard normal random variables. Thus because MGFs uniquely determine distributions, we conclude that _Z_ = ( _Z_ 1 _, . . . , Zn_ )<sup>_T_</sup> has independent standard normal random variables. We have thus proved that: **If** _Y ∼ Nn_ ( _µ,_ Σ) **and** Σ **is p.d, then the components** _Z_ 1 _, . . . Zn_ **of** _Z_ = Σ<sup>_−_1</sup><sup>_/_2</sup> ( _Y − µ_ ) **are independent standard normal random variables** .

### **5.3 Joint Density of the Multivariate Normal Distribution**

Suppose _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> is a random vector that has the multivariate normal distribution. What then is the joint density of _Y_ 1 _, . . . , Yn_ ?

Let _µ_ = E( _Y_ ) and Σ = _Cov_ ( _Y_ ) be the mean vector and covariance matrix of _Y_ respectively. For _Y_ to have a joint density, we need to assume that Σ is positive definite. We have then seen in the previous section that the components _Z_ 1 _, . . . , Zn_ of _Z_ are independent standard normal random variables where


124 _CHAPTER 5. THE MULTIVARIATE NORMAL DISTRIBUTION_

Because _Z_ 1 _, . . . , Zn_ are independent standard normals, their joint density equals


where _z_ = ( _z_ 1 _, . . . , zn_ )<sup>_T_</sup> .

Using the above formula and the fact that _Y_ = _µ_ + Σ<sup>1</sup><sup>_/_2</sup> _Z_ , we can compute the joint density of _Y_ 1 _, . . . , Yn_ via the Jacobian formula. This gives


where _y_ = ( _y_ 1 _, . . . , yn_ )<sup>_T_</sup> .

### **5.4 Properties of Multivariate Normal Random Variables**

Suppose _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> _∼ Nn_ ( _µ,_ Σ). Note then that _µ_ is the mean vector E( _Y_ ) of _Y_ and Σ is the covariance matrix _Cov_ ( _Y_ ). The following properties are very important.

1. **Linear Functions of** _Y_ **are also multivariate normal** : If _A_ is an _m × n_ deterministic matrix and _c_ is an _m ×_ 1 deterministic vector, then _AY_ + _c ∼ Nm_ ( _Aµ_ + _c, A_ Σ _A_<sup>_T_</sup> ).

   - **Reason** : Every linear function of _AY_ + _c_ is obviously also a linear function of _Y_ and, thus, this fact follows from the definition of the multivariate normal distribution.

2. If _Y_ is multivariate normal, then every random vector formed by taking a subset of the components of _Y_ is also multivariate normal.

**Reason** : Follows from the previous fact.

3. **Independence is the same as Uncorrelatedness** : If _Y_ (1) and _Y_ (2) are two random vectors such that _Y_ = ( _Y_ (1)<sup>_T, Y_</sup> (2)<sup>_T_)</sup><sup>_T_ismultivariatenormal.Then</sup><sup>_Y_(1)and</sup><sup>_Y_(2)areindependentifand</sup> only if _Cov_ ( _Y_ (1) _, Y_ (2)) = 0.

**Reason** : The fact that independence implies _Cov_ ( _Y_ (1) _, Y_ (2)) = 0 is obvious and does not require any normality. The key is the other implication that zero covariance implies independence. For this, it is enough to show that the MGF of _Y_ equals the product of the MGFs of _Y_ (1) and _Y_ (2). The MGF of _Y_ equals


where Σ = _Cov_ ( _Y_ ).

Note that _Y_ (1) and _Y_ (2) are also multivariate normal so that


_5.5. IDEMPOTENT MATRICES AND CHI-SQUARED DISTRIBUTIONS_

125

where


Now if Σ12 := _Cov_ ( _Y_ (1) _, Y_ (2)) and Σ21 = _Cov_ ( _Y_ (2) _, Y_ (1)) = Σ12<sup>_T_,thenobservethat</sup>


As a result, if _a_ = ( _a_ (1) _, a_ (2))<sup>_T_</sup> , then


Under the assumption that Σ12 = 0, we can therefore write


from which it follows that


Because the MGF of _Y_ = ( _Y_ (1) _, Y_ (2))<sup>_T_</sup> factorizes into the product of the MGF of _Y_ (1) and the MGF of _Y_ (2), it follows that _Y_ (1) and _Y_ (2) are independent. Thus under the assumption of multivariate normality of ( _Y_ (1) _, Y_ (2))<sup>_T_</sup> , uncorrelatedness is the same as independence.

4. Suppose _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> is a multivariate normal random vector. Then two components _Yi_ and _Yj_ are independent if and only if Σ _ij_ = 0 where Σ = _Cov_ ( _Y_ ).

**Reason** : Follows directly from the previous three facts.

5. **Independence of linear functions can be checked by multiplying matrices** : Suppose _Y_ is multivariate normal. Then _AY_ and _BY_ are independent if and only if _A_ Σ _B_<sup>_T_</sup> = 0. **Reason** : Note first that


is multivariate normal. Therefore _AY_ and _BY_ are independent if and only if _Cov_ ( _AY, BY_ ) = 0. The claimed assertion then follows from the observation that _Cov_ ( _AY, BY_ ) = _A_ Σ _B_<sup>_T_</sup> .

### **5.5 Idempotent Matrices and Chi-Squared distributions**

We shall next prove that quadratic forms of multivariate normal random variables with identity covariance have chi-squared distributions provided the symmetric matrix defining the quadratic form is **idempotent** . A square matrix _A_ is said to be idempotent if _A_<sup>2</sup> = _A_ . An important fact about idempotent matrices is the following.

**Fact** : If _A_ is an _n × n_ symmetric and idempotent matrix of rank _r_ if and only if


_CHAPTER 5. THE MULTIVARIATE NORMAL DISTRIBUTION_

126

for _r_ orthogonal and unit length vectors _u_ 1 _, . . . , ur_ .

To prove this fact, note first that if _A_ is symmetric, then by the spectral theorem


for an orthonormal basis _u_ 1 _, . . . , un_ and real numbers _λ_ 1 _, . . . , λn_ . The rank of _A_ precisely equals the number of _λi_ ’s that are non-zero. If _r_ is the rank of _A_ , we can therefore write (assuming without loss of generality that _λ_ 1 _, . . . , λr_ are non-zero and _λr_ +1 = _· · ·_ = _λn_ = 0)


It then follows that


Therefore if _A_ is idempotent, then _A_<sup>2</sup> = _A_ so that


which implies that _λ_<sup>2</sup> _i_<sup>=</sup><sup>_λi_whichgives</sup><sup>_λi_= 1(notethatwehaveassumedthat</sup><sup>_λi̸_= 0).Thisproves</sup> (5.2).

The following result states that quadratic forms of multivariate normal random vectors with identity covariance are chi-squared provided the underlying matrix is idempotent.

**Theorem 5.5.1.** _Suppose Y ∼ Nn_ ( _µ, In_ ) _and let A is an n × n symmetric and idempotent matrix with rank r. Then_


_Proof._ Because _A_ is symmetric and idempotent and has rank _r_ , we can write _A_ as


for some orthogonal and unit norm vectors _u_ 1 _, . . . , ur_ . Then


where _Vi_ := _u_<sup>_T_</sup> _i_<sup>(</sup><sup>_Y−µ_).Notenowthateach</sup><sup>_Vi∼N_(0</sup><sup>_,_1)andthat</sup><sup>_V_1</sup><sup>_, . . . , Vr_areuncorrelatedand</sup> hence independent (because of normality). This proves that ( _Y − µ_ )<sup>_T_</sup> _A_ ( _Y − µ_ ) _∼ χ_<sup>2</sup> _r_<sup>.</sup>

**Example 5.5.2.** _Suppose X_ 1 _, . . . , Xn are i.i.d N_ (0 _,_ 1) _. Then X_<sup>¯</sup> _∼ N_ (0 _,_ 1 _/n_ ) _and S ∼ χ_<sup>2</sup> _n−_ 1<sup>_where_</sup>


_Moreover X_<sup>¯</sup> _and S are independent._

_5.5. IDEMPOTENT MATRICES AND CHI-SQUARED DISTRIBUTIONS_

127

_The fact that X_<sup>¯</sup> _∼ N_ (0 _,_ 1 _/n_ ) _is easy. To prove that S ∼ χ_<sup>2</sup> _n−_ 1<sup>_andthatSandX_¯</sup><sup>_areindependent,_</sup> _we shall show two methods._

**_Method One_** _: To prove S ∼ χ_<sup>2</sup> _n−_ 1<sup>_,thekeyistonotethat_</sup>


_where X_ = ( _X_ 1 _, . . . , Xn_ )<sup>_T_</sup> _and_ **1** = (1 _, . . . ,_ 1)<sup>_T_</sup> _. In the last step above, we used the fact that I − n_<sup><u>1</u></sup><sup>**11**</sup><sup>_T_</sup> _is symmetric. For the first step, we used the fact that_


_Now if_


_then clearly A is symmetric and idempotent as_


_Also the rank of A equals n −_ 1 _. Thus by Theorem 5.5.1 (note that X_ = ( _X_ 1 _, . . . , Xn_ )<sup>_T_</sup> _∼ Nn_ (0 _, In_ ) _), we have_

_S_ = _X_<sup>_T_</sup> _AX ∼ χ_<sup>2</sup> _n−_ 1<sup>_._</sup>

_In order to prove that S and X_<sup>¯</sup> _are independent, we only need to observe that_


_are independent because S is a function of_


_The independence of the random variables in_ (5.3) _follows because_


**_Method Two_** _: Let u_ 1 _, . . . , un be an orthonormal basis for_ R<sup>_n_</sup> _with u_ 1 = **1** _/_<sup>_√_</sup> _<u>n</u> (check that u_ 1 _has unit norm). Let U be the matrix with columns u_ 1 _, . . . , un i.e.,_


_Note that UU_<sup>_T_</sup> = _U_<sup>_T_</sup> _U_ = _In (by the properties of an orthonormal basis). Now let Y_ = _U_<sup>_T_</sup> _X. Then Y is a linear function of X (and X ∼ Nn_ (0 _, In_ ) _) so that_


128

_CHAPTER 5. THE MULTIVARIATE NORMAL DISTRIBUTION_

_Further note that_


_and that Y_ 1 = _u_<sup>_T_</sup> 1<sup>_X_= (</sup><sup>_X_1+</sup><sup>_· · ·_+</sup><sup>_Xn_)</sup><sup>_/√_</sup> _<u>n</u>_ =<sup>_√_</sup> _<u>nX</u>_<sup>¯</sup> _. Thus,_ (5.4) _gives_

_so that_


_This and the fact that Y ∼ Nn_ (0 _, In_ ) _(which is same as saying that Y_ 1 _, . . . , Yn are i.i.d N_ (0 _,_ 1) _) imply that S ∼ χ_<sup>2</sup> _n−_ 1<sup>_.AlsonotethatSdependsonlyonY_2</sup><sup>_, . . . , YnsothatitisindependentofY_1</sup><sup>_andthus_</sup> _S and X_<sup>¯</sup> _are independent (note that X_<sup>¯</sup> = _Y_ 1 _/_<sup>_√_</sup> _<u>n).</u>_

**Example 5.5.3.** _Suppose that X ∼ Nn_ (0 _,_ Σ) _where_ Σ _is an n × n matrix with 1 on the diagonal and ρ on the off-diagonal._ Σ _can also be represented as_


_In other words X_ 1 _, . . . , Xn are multivariate normal, have mean zero, unit variance and the correlation between every pair equals ρ. Find the distribution of X_<sup>¯</sup> _and S_ :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_Xi −X_¯)2</sup><sup>_andarguethatthey_</sup> _are independent._

_X_ ¯ _is a linear function of X and so it will be normal. We then just have to find its mean and variance. Clearly_ E _X_<sup>¯</sup> = 0 _(as each_ E _Xi = 0) and_

_Thus_


_Observe that this implies that_ 1 + ( _n −_ 1) _ρ ≥_ 0 _or ρ ≥−_ 1 _/_ ( _n −_ 1) _. In other words, if ρ < −_ 1 _/_ ( _n −_ 1) _, then_ Σ _will not be positive semi-definite._

_To find the distribution of S, we can, as in the previous example, write_


_but we cannot unfortunately use Theorem 5.5.1 as X does not have identity covariance (Theorem 5.5.1) only applies to multivariate normal random vectors with identity covariance. It turns out that here the second method (described in the previous example) works here and gives the distribution of S. This is explained below._

_5.6. ADDITIONAL REMARKS ON MULTIVARIATE NORMALS AND CHI-SQUARED DISTRIBUTIONS_ 129

_Let u_ 1 _, . . . , un be an orthonormal basis for_ R<sup>_n_</sup> _with u_ 1 = **1** _/_<sup>_√_</sup> _<u>n</u> and let U be the matrix with columns u_ 1 _, . . . , un so that U_<sup>_T_</sup> _U_ = _UU_<sup>_T_</sup> = _In. Let Y_ = _U_<sup>_T_</sup> _X and note (as in the previous example) that_


_The distribution of Y is now given by Y ∼ Nn_ (0 _, U_<sup>_T_</sup> Σ _U_ ) _and_

_U_<sup>_T_</sup> Σ _U_ = _U_<sup>_T_�</sup> (1 _− ρ_ ) _In_ + _ρ_ **11**<sup>_T_�</sup> _U_ = (1 _− ρ_ ) _U_<sup>_T_</sup> _U_ + _ρ_ ( _U_<sup>_T_</sup> **1** )( **1**<sup>_T_</sup> _U_ ) = (1 _− ρ_ ) _In_ + _ρ_ ( _U_<sup>_T_</sup> **1** )( **1**<sup>_T_</sup> _U_ ) _._

_To calculate_ **1**<sup>_T_</sup> _U , note that_


_where we used that_ **1**<sup>_T_</sup> _u_ 1 = **1**<sup>_T_</sup> **1** _/_<sup>_√_</sup> _<u>n</u>_ =<sup>_√_</sup> _<u>n</u> and the fact that_ **1** _is orthogonal to u_ 2 _, . . . , un (this is because ⟨_ **1** _, ui⟩_ =<sup>_√_</sup> _<u>n</u> ⟨u_ 1 _, ui⟩_ = 0 _for i >_ 1 _). We have thus obtained_


_This means that U_<sup>_T_</sup> Σ _U is a diagonal matrix with diagonal entries_ (1 _− ρ_ + _nρ_ ) _,_ 1 _− ρ,_ 1 _− ρ, . . . ,_ 1 _− ρ. Therefore Y ∼ Nn_ (0 _, U_<sup>_T_</sup> Σ _U_ ) _implies that Y_ 1 _, . . . , Yn are independent with_


_Thus_


_or S ∼_ (1 _− ρ_ ) _χ_<sup>2</sup> _n−_ 1<sup>_.AlsobecauseX_¯</sup><sup>_onlydependsonY_1</sup><sup>_andSdependsonlyonY_2</sup><sup>_, . . . , Yn,wehave_</sup> _that S and X_<sup>¯</sup> _are independent._

### **5.6 Additional Remarks on Multivariate Normals and ChiSquared Distributions**

In the last class, we saw the following result.

**Theorem 5.6.1.** _If Z ∼ Nn_ (0 _, In_ ) _and A is a symmetric and idempotent matrix, then Z_<sup>_T_</sup> _AZ ∼ χ_<sup>2</sup> _r where r is the rank of A._

It turns out that the converse of this result is also true and we have

**Theorem 5.6.2.** _Suppose Z ∼ Nn_ (0 _, In_ ) _and A is a symmetric matrix. Then Z_<sup>_T_</sup> _AZ ∼ χ_<sup>2</sup> _r_<sup>_ifandonly_</sup> _if A is an idempotent matrix with rank r._

_CHAPTER 5. THE MULTIVARIATE NORMAL DISTRIBUTION_

130

In other words, the only way in which _Z_<sup>_T_</sup> _AZ_ has the chi-squared distribution is when _A_ is idempotent. Thus being idempotent is both necessary and sufficient for _Z_<sup>_T_</sup> _AZ_ to be distributed as chi-squared. The fact that _Z_<sup>_T_</sup> _AZ ∼ χ_<sup>2</sup> _r_<sup>implies the idempotence of</sup><sup>_A_can be proved via moment generating functions</sup> but we shall skip this argument.

When the covariance is not the identity matrix, Theorem 5.6.1 needs to be modified as demonstrated below. Suppose now that _Y ∼ Nn_ (0 _,_ Σ) and we are interested in seeing when _Q_ := _Y_<sup>_T_</sup> _AY_ is idempotent (here _A_ is a symmetric matrix). We know that _Z_ := Σ<sup>_−_1</sup><sup>_/_2</sup> _Y ∼ Nn_ (0 _, In_ ) so we can write (as _Y_ = Σ<sup>1</sup><sup>_/_2</sup> _Z_ )


Thus _Q_ is chi-squared distributed if and only if Σ<sup>1</sup><sup>_/_2</sup> _A_ Σ<sup>1</sup><sup>_/_2</sup> is idempotent which is equivalent to


We thus have

**Theorem 5.6.3.** _Suppose Y ∼ Nn_ (0 _,_ Σ) _and A is a symmetric matrix. Then Y_<sup>_T_</sup> _AY ∼ χ_<sup>2</sup> _r_<sup>_ifandonly_</sup> _if A_ Σ _A_ = _A and r_ = _rank_ (Σ<sup>1</sup><sup>_/_2</sup> _A_ Σ<sup>1</sup><sup>_/_2</sup> ) = _rank_ ( _A_ ) _._

Let us look at some examples of this result.

**Example 5.6.4.** _Suppose Y ∼ Nn_ (0 _, σ_<sup>2</sup> _In_ ) _and let A be an n × n symmetric idempotent matrix with rank r. Then it turns out that_


_This can be proved as a consequence of Theorem 5.6.3 because_

_and_


**Example 5.6.5.** _Suppose that X ∼ Nn_ (0 _,_ Σ) _where_ Σ _is an n × n matrix with 1 on the diagonal and ρ on the off-diagonal._ Σ _can also be represented as_


_We shall show this here using Theorem 5.6.3. Note first that_

_so that_


_5.7. CONDITIONAL DISTRIBUTIONS OF MULTIVARIATE NORMALS_

131

_Thus to show_ (5.5) _, we only need to prove that A_ Σ _A_ = _A. For this, see that_


_so that A_ Σ _A_ = _A. Thus Theorem 5.6.3 immediately gives_ (5.5) _._

**Example 5.6.6.** _Suppose Y ∼ Nn_ (0 _,_ Σ) _. Then Y_<sup>_T_</sup> Σ<sup>_−_1</sup> _Y ∼ χ_<sup>2</sup> _n_<sup>_.ThisfollowsdirectlyfromTheorem_</sup> _5.6.3 by taking A_ = Σ<sup>_−_1</sup> _._

Finally let us mention that when _Z ∼ Nn_ ( _µ, In_ ) and _A_ is idempotent, then _Z_<sup>_T_</sup> _AZ_ will be a non-central chi-squared distribution. We will not study these in this class.

### **5.7 Conditional Distributions of Multivariate Normals**

Suppose _Y ∼ Nn_ ( _µ,_ Σ). Let us partition _Y_ into two parts _Y_ (1) and _Y_ (2) where _Y_ (1) = ( _Y_ 1 _, . . . , Yp_ )<sup>_T_</sup> consists of the first _p_ components of _Y_ and _Y_ (2) = ( _Yp_ +1 _, . . . , Yn_ ) consists of the last _q_ := _n − p_ components of _Y_ .

We can then partition the mean vector _µ_ analogously


and the covariance matrix Σ as

The question we address now is the following: What is the conditional distribution of _Y_ (2) given _Y_ (1) = _y_ 1? The answer is given below.

**Fact** : Under the assumption that _Y ∼ Nn_ ( _µ,_ Σ), we have


In words, the conditional distribution of _Y_ (2) given _Y_ (1) = _y_ 1 is also multivariate normal with mean vector given by:


_CHAPTER 5. THE MULTIVARIATE NORMAL DISTRIBUTION_

132

and covariance matrix given by


We shall go over the proof of (5.6) below. Before that, let us make a few quick remarks on the form of the conditional distribution:

1. The conditional distributions are also multivariate normal.

2. The conditional expectation E( _Y_ (2) _|Y_ (1) = _y_ 1) is a linear function of _y_ 1.

3. E( _Y_ (2) _|Y_ (1)) is exactly equal to the BLP of _Y_ (2) in terms of _Y_ (1). Thus the BP and BLP coincide.

4. The conditional covariance matrix _Cov_ ( _Y_ (2) _|Y_ (1) = _y_ 1) does not depend on _y_ 1 (this can be viewed as some kind of _homoscedasticity_ ).

5. The conditional covariance matrix _Cov_ ( _Y_ (2) _|Y_ (1) = _y_ 1) equals Σ22<sup>_S_(theSchurcomplementofΣ22</sup> in Σ). In other words, the conditional covariance matrix _Cov_ ( _Y_ (2) _|Y_ (1) = _y_ 1) is precisely equal to the Covariance Matrix of the Residual of _Y_ (2) given _Y_ (1).

**Proof of Fact** (5.6): It is easy to see that (5.6) is equivalent to:


which is further equivalent to


Note that the distribution on the right hand above does not depend on _y_ 1. Therefore (5.7) is equivalent to

_Y_ (2) _−µ_ (2) _−_ Σ21Σ<sup>_−_</sup> 11<sup>1(</sup><sup>_Y_(1)</sup><sup>_−µ_(1))</sup><sup>_∼Np_</sup> �0 _,_ Σ22 _−_ Σ21Σ<sup>_−_</sup> 11<sup>1Σ12</sup> � and _Y_ (2) _−µ_ (2) _−_ Σ21Σ<sup>_−_</sup> 11<sup>1(</sup><sup>_Y_(1)</sup><sup>_−µ_(1))</sup><sup>_⊥⊥Y_1</sup>

where _⊥⊥_ denotes independence. Because _Y_ is multivariate normal, we know that linear functions of _Y_ are also multivariate normal and that linear functions of _Y_ are independent if and only if they are uncorrelated. The above displayed assertion is therefore equivalent to the following three equations:


In other words, we have noted that proving the above three equations is equivalent to proving (5.6) . We now complete the proof of (5.6) by proving the three equations above. We actually have already proved these three facts. The first fact simply says that the residual of _Y_ (2) given _Y_ (1) has zero expectation.

_5.7. CONDITIONAL DISTRIBUTIONS OF MULTIVARIATE NORMALS_

133

The second fact says that the covariance matrix of the residual equals the Schur complement. The third fact says that the residual of _Y_ (2) given _Y_ (1) is uncorrelated with _Y_ (1). For completeness, let us rederive these quickly as follows.


and finally


This completes the proof of (5.6).

Let us reiterate that all the three calculations (5.8), (5.9) and (5.10) do not require any distributional assumptions on _Y_ (1) and _Y_ (2). They hold for all random vectors _Y_ (1) and _Y_ (2). The multivariate normality assumption allows us to deduce (5.6) from these second order (i.e., mean and covariance) calculations.

Let us now look at the following special case of (5.6). Fix two components _Yi_ and _Yj_ of _Y_ . Let _Y_ (2) := ( _Yi, Yj_ )<sup>_T_</sup> and let _Y_ (1) denote the vector obtained from all the other components _Yk, k̸_ = _i, k̸_ = _j_ . Then


Now let _rYi|Yk,k̸_ = _i,k̸_ = _j_ and _rYj |Yk,k̸_ = _i,k̸_ = _j_ denote the residuals of _Yi_ in terms of _Yk, k̸_ = _i, k̸_ = _j_ and _Yj_ in terms of _Yk, k̸_ = _i, k̸_ = _j_ , then we have seen previously that


We thus have


_CHAPTER 5. THE MULTIVARIATE NORMAL DISTRIBUTION_

134

This means, in particular, that the conditional correlation between _Yi_ and _Yj_ given _Yk_ = _yk, k̸_ = _i, k̸_ = _j_ is precisely equal to the partial correlation _ρYi,Yj |Yk,k̸_ = _i,k̸_ = _j_ (recall that _ρYi,Yj |Yk,k̸_ = _i,k̸_ = _j_ is the correlation between _rYi|Yk,k̸_ = _i,k̸_ = _j_ and _rYj |Yk,k̸_ = _i,k̸_ = _j_ ).

Now recall the following connection between partial correlation and entries of Σ<sup>_−_1</sup> that we have seen earlier:


Putting the above observations together, we can deduce that the following are **equivalent** when _Y_ is multivariate normal with covariance matrix Σ:

1. Σ<sup>_−_1</sup> ( _i, j_ ) = 0

2. _ρYi,Yj |Yk,k̸_ = _i,k̸_ = _j_ = 0

3. The conditional correlation between _Yi_ and _Yj_ given _Yk_ = _yk, k̸_ = _i, k̸_ = _j_ equals 0 for every choice of _yk, k̸_ = _i, k̸_ = _j_ .

4. _Yi_ and _Yj_ are conditionally independent given _Yk_ = _yk, k̸_ = _i, k̸_ = _j_ equals 0 for every choice of _yk, k̸_ = _i, k̸_ = _j_ .

---

[← Second Order Theory of Random Vectors](05-second-order-theory-of-random-vectors.md) · [Up: contents](index.md)
