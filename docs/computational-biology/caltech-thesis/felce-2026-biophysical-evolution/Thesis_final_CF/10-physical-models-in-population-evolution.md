---
title: PHYSICAL MODELS IN POPULATION EVOLUTION
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PHYSICAL MODELS IN POPULATION EVOLUTION

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Felce, Catherine, Steinunn Liorsdóttir, and Lior Pachter (Nov. 2025). “Analogies between the virial theorem and the Price equation”. In: _Phys. Rev. E_ 112 (5), p. 054139. doi: `10.1103/r8bd-lhm3` . url: `https://link.aps.org/doi/10. 1103/r8bd-lhm3` .

### **5.1 Introduction**

We observe that the time-averaged continuous Price equation is identical to the positive momentum virial theorem, and we discuss the applications and implications of this connection. We also introduce ecological models, using a maternal effect, which can describe arbitrary population size cycles and trait evolution across spatially separated populations. The virial theorem sheds light on the time-averaged behavior of these models.

### **5.2 The virial theorem**

The virial theorem was first described by Rudolf Clausius in connection with his studies on heat transfer (Clausius, 1870). In its simplest form, it relates the timeaveraged kinetic energy ⟨ _𝑇_ ⟩ _𝜏_ = ⟨ 2<sup><u>1</u></sup> � _𝑖𝑛_ =1<sup>_𝑚𝑖𝑣𝑖_(</sup><sup>_𝑡_)2⟩</sup><sup>_𝜏_=</sup> <u>1</u> _𝜏_ ∫0 _𝜏_ <u>12</u> � _𝑖𝑛_ =1<sup>_𝑚𝑖𝑣𝑖_(</sup><sup>_𝑡_)2</sup><sup>_𝑑𝑡_of</sup> _𝑛_ objects with masses _𝑚_ 1 _, . . . , 𝑚𝑛_ and velocities _𝑣_ 1( _𝑡_ ) _, . . . , 𝑣𝑛_ ( _𝑡_ ), to their time averaged potential energy ⟨ _𝑈_ ⟩ _𝜏_ = ⟨<sup>�</sup> _𝑖_<sup>_𝑛_</sup> =1<sup>_𝐹𝑖_(</sup><sup>_𝑡_)</sup><sup>_𝑧𝑖_(</sup><sup>_𝑡_)⟩</sup><sup>_𝜏_, where</sup><sup>_𝐹_1(</sup><sup>_𝑡_)</sup><sup>_, . . . , 𝐹𝑛_(</sup><sup>_𝑡_) are the</sup> forces acting on the _𝑛_ objects and _𝑧_ 1( _𝑡_ ) _, . . . , 𝑧𝑛_ ( _𝑡_ ) are their respective positions: **Theorem 1** _(Virial theorem, 1870)_ **.** For stably bound gravitational systems:


The mathematical underpinning of the virial theorem is the product rule from calculus. The derivative of the Clausius virial _𝑆_ ( _𝑡_ ) =<sup>�</sup> _𝑖_<sup>_𝑛_</sup> =1<sup>_𝑝𝑖_(</sup><sup>_𝑡_)</sup><sup>_𝑧𝑖_(</sup><sup>_𝑡_) where</sup><sup>_𝑝𝑖_(</sup><sup>_𝑡_)=</sup> _𝑚𝑖𝑣𝑖_ ( _𝑡_ ) is:

69


Since for stably bound systems the velocities and positions of objects have upper and lower bounds, the average of the derivative of _𝑆_ ( _𝑡_ ) over a period of time _𝜏_ will be zero in the limit of large _𝜏_ , i.e. ⟨<sup>_𝑑𝑆_</sup> _𝑑𝑡_<sup><u>(</u></sup><sup>_𝑡_</sup><sup><u>)</u>⟩</sup><sup>_𝜏_≈0.Therefore, equation (5.2) implies:</sup>


In the specific case of a gravitationally bound system, we have the identification � _𝑖_<sup>_𝐹_</sup> _𝑖_<sup>_𝑧_</sup> _𝑖_<sup>=</sup><sup>_𝑈_, for U the potential energy, and we obtain from (5.3) the gravitational</sup> virial theorem (5.1):


where _𝑇_ is the kinetic energy of the system. In general, for forces with a potential of the form _𝑈_ ∝ _𝑟_<sup>_𝑛_</sup> , we have ⟨ _𝑇_ ⟩ =<sup>_<u>𝑛</u>_</sup> 2<sup>⟨</sup><sup>_𝑈_⟩.</sup>

The virial theorem was well known to physicists in the late 19th and early 20th centuries (Rayleigh, 1905; Einstein, 1922), however, its power as a discovery tool for astrophysics was first highlighted by Fritz Zwicky (Zwicky, 1933). Zwicky used the virial theorem to estimate the mass of the Coma cluster, thereby identifying a mass deficit in comparison to luminosity estimates, leading him to posit the existence of what he called _dunkle materie_ (dark matter) (Zwicky, 1933). Although Zwicky’s mass estimates were inaccurate (The and White, 1986; Merritt, 1987), the principle of using the virial theorem to identify a measurement gap was sound, and the virial theorem has become widely used in physics and astrophysics. For example, it has been used to deduce the strength of magnetic fields in stars (Mukhopadhyay, Sarkar, and Tout, 2025) and the radii of elliptical galaxies (Binney and Merrifield, 1998).

70

It can also be used to derive classic laws such as the ideal gas law (Fowler, 1929; Hanson, 1995), and extensions are applicable in many settings, including quantum mechanics (Georgescu and Gérard, 1999), astrophysical hydrodynamics (Shore, 2012), and fluid mechanics (Oguz and Prosperetti, 1990; Alazard and Zuily, 2023).

### **5.3 The Price equation**

The Price equation (Price et al., 1970) pertains to selection in evolutionary processes. It was motivated by a desire to understand the evolution of altruism (Harman, 2011), and has been described as a “fundamental theorem of evolution” (Queller, 2017) due to its generalization and unification of many results in evolutionary biology. For example, Fisher’s fundamental theorem of natural selection (Fisher, 1930) is a special case of the Price equation (Queller, 2017; Frank, 1997).

The Price equation relates the change in a trait in a population over time, to fitness values in subpopulations. Formally, the (discrete) Price equation as published in (Price et al., 1970) (we follow notation from (Frank, 1997)) considers a numerical trait in _𝑛_ subpopulations at time _𝑡_ denoted **z** ( _𝑡_ ) = ( _𝑧_ 1( _𝑡_ ) _, . . . , 𝑧𝑛_ ( _𝑡_ )). The subpopulations have sizes _𝑝_ 1( _𝑡_ ) _, . . . , 𝑝𝑛_ ( _𝑡_ ), and have (Wrightian) fitness **w** ( _𝑡_ ) = ( _𝑤_ 1( _𝑡_ ) _, . . . , 𝑤𝑛_ ( _𝑡_ )) defined by _𝑤𝑖_ ( _𝑡_ ) =<sup>_<u>𝑝𝑖</u>_</sup><sup><u>(</u></sup><sup>_𝑡_+Δ</sup><sup>_𝑡_</sup><sup><u>)</u></sup> where Δ _𝑡_ denotes the time interval of one generation (Wag- _𝑝𝑖_ ( _𝑡_ ) ner, 2010). The Wrightian fitness is the average number of offspring an individual _<u>𝑝𝑖</u>_ <u>(</u> _𝑡_ <u>)</u> contributes to the next generation. Let _𝑞𝑖_ ( _𝑡_ ) = <u>�</u> _<u>𝑛𝑗</u>_ =1<sup>_𝑝𝑗_(</sup><sup>_𝑡_)be the relative size of the</sup><sup>_𝑖_t</sup><sup>_ℎ_</sup> population, and define the population average fitness to be **<u>w</u>** ( _𝑡_ ) =<sup>�</sup> _𝑖_<sup>_𝑛_</sup> =1<sup>_𝑞𝑖_(</sup><sup>_𝑡_)</sup><sup>_𝑤𝑖_(</sup><sup>_𝑡_).</sup> Note that **q** ( _𝑡_ ) forms a probability distribution for **w** ( _𝑡_ ) viewed as a random variable, and E( **w** ( _𝑡_ )) = **<u>w</u>** ( _𝑡_ ). Let Δ _𝑧𝑖_ ( _𝑡_ ) = _𝑧𝑖_ ( _𝑡_ + Δ _𝑡_ ) − _𝑧𝑖_ ( _𝑡_ ), Δ **z** ( _𝑡_ ) = **z** ( _𝑡_ + Δ _𝑡_ ) − **z** ( _𝑡_ ), and **<u>z</u>** ( _𝑡_ ) =<sup>�</sup> _𝑖_<sup>_𝑛_</sup> =1<sup>_𝑞𝑖_(</sup><sup>_𝑡_)</sup><sup>_𝑧𝑖_(</sup><sup>_𝑡_)with</sup><sup><u>Δ</u></sup> **<u>z</u>** ( _𝑡_ ) = **<u>z</u>** ( _𝑡_ + Δ _𝑡_ ) − **<u>z</u>** ( _𝑡_ ).

**Theorem 2** _(The Price equation, 1970)_ **.**


where E( **w** ( _𝑡_ ) ⊙ Δ **z** ( _𝑡_ )) is the expected value of the Hadamard product of **w** ( _𝑡_ ) and Δ **z** ( _𝑡_ ) with respect to the relative subpopulation sizes, and cov( **w** ( _𝑡_ ) _,_ **z** ( _𝑡_ )) = E( **w** ⊙ **z** ) − E( **w** )E( **z** ) is the covariance between the subpopulation fitnesses and trait values with respect to the relative subpopulation sizes.

Intuitively, if subpopulation fitness has positive covariance with trait values, then the trait is beneficial, and the trait value, averaged across populations, will increase after a generation. However, if the covariance between subpopulation fitness and trait

71

values is negative, higher trait values are detrimental and the trait value averaged across populations will decrease after a generation.

The Price equation as published in (Price et al., 1970) is discrete in time, and proof of the identity uses basic properties of expectation and covariance along with the fact that _𝑞𝑖_ ( _𝑡_ + Δ _𝑡_ ) =<sup>_<u>𝑞𝑖</u>_</sup><sup><u>(</u></sup><sup>_𝑡_</sup><sup><u>)</u></sup><sup>_𝑤𝑖_</sup><sup><u>(</u></sup><sup>_𝑡_</sup><sup><u>)</u></sup> , which we leave as an exercise for the reader. Note **<u>w</u>** ( _𝑡_ ) that:


The discrete-time Price equation has a continuous-time analog (Price, 1972; Ellner, Geber, and Hairston Jr, 2011). It is formulated using the Malthusian fitness **r** ( _𝑡_ ) = <u>1</u> _𝑑𝑝𝑖_ <u>(</u> _𝑡_ <u>)</u> _𝑟_ 1 _, . . . , 𝑟𝑛_ given by _𝑟𝑖_ ( _𝑡_ ) = _𝑝𝑖_ ( _𝑡_ ) _𝑑𝑡_ instead of the Wrightian fitness **w** ( _𝑡_ ). The Malthusian fitness is the per capita rate at which individuals contribute offspring to the next generation.

**Theorem 3** _(The continuous Price equation, 1972)_ **.**


The continuous-time Price equation (5.5) is the continuum limit of the discrete Price **<u>w</u>** <u>(</u> _𝑡_ <u>)</u> equation (5.4). To see this, we begin by multiplying the Price equation by Δ _𝑡_<sup>:</sup>

72


We will now see why, contrary to convention, we have indexed the variables in equation (5.4) with time. Starting with the left hand side, we observe that:


Therefore:


The covariance term, in the limit as Δ _𝑡_ → 0, is given by:


Let _𝑔𝑖_ ( _𝑡_ ) = Δ1 _𝑡_<sup>_𝑙𝑛_(</sup><sup>_𝑤𝑖_(</sup><sup>_𝑡_)).Notethat</sup><sup>_𝑤𝑖_(</sup><sup>_𝑡_)=</sup><sup>_𝑒𝑔𝑖_(</sup><sup>_𝑡_)Δ</sup><sup>_𝑡_andthatlimΔ</sup><sup>_𝑡_→0</sup><sup>_𝑔𝑖_(</sup><sup>_𝑡_)=</sup><sup>_𝑟𝑖_(</sup><sup>_𝑡_).</sup>

73

Substituting _𝑒_<sup>_𝑔𝑖_(</sup><sup>_𝑡_)Δ</sup><sup>_𝑡_</sup> for _𝑤𝑖_ ( _𝑡_ ) yields:


Finally, we have that:


In summmary:


(continuous Price equation (5.5)) _._

### **5.4 The Price equation from the virial theorem**

_𝑑𝑧𝑖_ <u>(</u> _𝑡_ <u>)</u> In the physics setting, recall that the momentum _𝑝𝑖_ ( _𝑡_ ) = _𝑚𝑖𝑣𝑖_ ( _𝑡_ ) = _𝑚𝑖 𝑑𝑡_<sup>.Let</sup> <u>1</u> _𝑑𝑝𝑖_ <u>(</u> _𝑡_ <u>)</u> _𝑟𝑖_ = _𝑝𝑖_ ( _𝑡_ ) _𝑑𝑡_<sup>,i.e.</sup> acceleration divided by velocity. If all the momenta are

74

greater than zero, i.e., _𝑝𝑖_ ( _𝑡_ ) _>_ 0 for all _𝑖_ , we can define relative momentum as _<u>𝑝𝑖</u>_ <u>(</u> _𝑡_ <u>)</u> _𝑞𝑖_ ( _𝑡_ ) = <u>�</u> _<u>𝑛𝑗</u>_ =1<sup>_𝑝𝑗_(</sup><sup>_𝑡_).</sup> Consider the virial density _𝑆_<sup>˜</sup> ( _𝑡_ ) =<sup>�</sup> _𝑖_<sup>_𝑛_</sup> =1<sup>_𝑞𝑖_(</sup><sup>_𝑡_)</sup><sup>_𝑧𝑖_(</sup><sup>_𝑡_)(Englert,</sup> 2014), whose derivative is<sup>_𝑑𝑆_</sup> _𝑑𝑡_<sup>˜(</sup><sup>_𝑡_</sup><sup><u>)</u></sup> = _𝑑𝑡_<sup>_<u>𝑑</u>_E(</sup><sup>**z**(</sup><sup>_𝑡_)).The product rule applied to the virial</sup> density is:


This shows that the virial (density) equation (5.6) and the continuous Price equation (5.5) are mathematically identical. Therefore, the relationships between traits and fitness in evolutionary biology are not only reminiscent of the relationships between physical quantities like distance, velocity, and acceleration; they are the same. It is therefore not surprising to find a direct analog of the virial theorem in genetics (Frank and Slatkin, 1990):

**Theorem 4** _(Frank and Slatkin, 1990)_ **.** For a population in equilibrium, with **z** ( _𝑡_ )<sup>2</sup> = **z** ( _𝑡_ ) ⊙ **z** ( _𝑡_ ):

cov( **w** ( _𝑡_ ) _,_ **z** ( _𝑡_ )<sup>2</sup> ) = −E( **w** ⊙ Δ[ **z** ( _𝑡_ )<sup>2</sup> ]) _._

75

In other words, the rate at which selection removes phenotypic variance from the population (left-hand side) is equal to the rate at which mutation adds variance (right-hand side). This result is a special case of the discrete Price equation (5.4), where the traits whose evolution are being considered are the squares of _𝑧𝑖_ . Because the population is assumed to be in equilibrium, we can take the left-hand side to be zero. The time variable, _𝑡_ , takes discrete values, separated by the length of a generation, as in equation (5.4). However, the result also has a continuous-time analog similar to Theorem 3. Frank and Slatkin considered the specific case where the _𝑧𝑖_ are proportional to the allelic states of the haploid genotypes, but their result is independent of the form of _𝑧_ .

In summary, we have the following relationships:

|**Biology**<br>**Physics**|
|---|
|Price equation<br>virial theorem|
|�limΔ_𝑡_→0<br>�_𝑝𝑖>_0|
|continuous Price<br>=<br>positive momentum|
|equation<br>virial theorem|


In genetics, the natural time increment to consider is discrete (generation), whereas in physics continuous-time is more natural. Thus, the discrete Price equation pertains to change in a trait after a single generation, whereas the virial theorem is formulated with continuous-time, and is additionally time averaged. However, the less intuitive forms of these equations that arise from the correspondences derived above may yield important insights. For example, the perspective of the virial theorem as a special case of the equipartition theorem (Podio-Guidugli, 2019) may be fruitful in evolutionary biology (Nourmohammad, Held, and Lässig, 2013). From the other direction, it might be interesting to consider physical systems with positive-momentum constituents in terms of means and covariances over a momentum-weighted distribution. Translation between biology and physics via the virial theorem and the Price equation may also accelerate discovery of generalizations. While the stochastic Price equation in evolution (Rice, 2008) and the stochastic virial theorem in astronomy (Cresson, Nottale, and Lehner, 2021) were discovered independently, their similarity suggests other generalizations could similarly parallel each other. Moreover, the virial theorem has been applied in a variety of fields, meaning that understanding its relationship to the Price equation could be relevant beyond physics and biology.

76

For example, Anderson (Andersen, 2004) discusses the utility of the Price equation in decomposing short-term economic growth into selection and innovation effects. He emphasizes that the general form of the Price equation allows complex systems to be described in terms of nested selection effects in a ‘multi-level population’ (e.g. corporations which are made up of constituent plants). In the following section, we likewise consider how the composition of subpopulations could explain complicated dynamics in ecology. Although Anderson identifies interpopulation interactions as a limitation of the Price equation for describing long-term evolutionary change, we show that a spatial population growth model can be used with the Price equation to study separate but interacting subpopulations.

### **5.5 Simple Harmonic Motion**

The connection between the Price equation and the virial theorem is evident in the study of a model motivated by work of Ginzburg and Colyvan (L. Ginzburg and Colyvan, 2004). In their book “Ecological Orbits: How Planets Move and Populations Grow”, they show that a maternal effect can generate population cycles (L. R. Ginzburg and Taneyhill, 1994), obviating the need for predator-prey models to explain such dynamics. A maternal effect is defined as “the causal influence of the maternal genotype or phenotype on the offspring phenotype” (Wolf and Wade, 2009). Note that these maternal attributes can be genetic (e.g. snail shell chirality determined by maternal genotype (Boycott et al., 1931)), or due to environmental effects (Fox, Thakar, and Mousseau, 1999). The Price equation motivates an analysis of an extension of the Ginzburg and Colyvan model to subpopulations, while the virial theorem motivates a study of time-averaged behavior, which we show leads to a relationship between population-size entropy and trait variance. Formally, (L. Ginzburg and Colyvan, 2004) posit that a trait _𝑧_ ( _𝑡_ ) that changes over time is linked to the size _𝑝_ ( _𝑡_ ) of a population as follows:


where _𝑓_<sup>˜</sup> and _𝑔_ ˜ are monotonically increasing functions, and Δ _𝑡_ again represents the time interval for a single generation. The maternal effect is captured by _𝑧_ ( _𝑡_ ) on the right-hand side of the trait evolution equation (5.8), indicating that a trait associated with individuals in a generation depends on the trait of mothers in the

77

current generation, as well as the fraction of the total resources, _𝑅_ , available to each individual in the next generation, i.e. _<u>𝑅</u>_ We extend this model to _𝑝_ ( _𝑡_ +Δ _𝑡_ )<sup>.</sup> include an additional function _ℎ_<sup>˜</sup> that captures the potentially dominant impact of transgenerational effects as seen in matrotrophic species (Bian et al., 2015; Harding, 2001; Reznick, Callahan, and Llauredo, 2015; Roseboom, Rooij, and Painter, 2006):


This formulation captures environmental impacts on the mother which affect her offspring directly, such as nutrition during gestation (Thorne, Dean, and Hepworth, 1976). We can further simplify (5.9) to the case where transgenerational effects dominate, i.e. we assume that _𝑔_ ˜ = 1, giving:


To derive a continuum limit from (5.10), as in our derivation of (5.5), we consider the limit where Δ _𝑡_ becomes an infinitesimal time increment. We have:


_ℎ_ ˜ <u>(</u> _𝑅_ <u>/</u> _<u>𝑝</u>_ <u>(</u> _𝑡_ <u>))−1</u> . wherewehavedefinedtheinfinitesimalgrowthrate, _ℎ_ , via _ℎ_<sup>�</sup> _𝑝_<sup>_<u>𝑅</u>_</sup> ( _𝑡_ ) � ≡ limΔ _𝑡_ →0 Δ _𝑡_ This gives, equivalently:


Similarly, equation (5.7) has a continuum limit given by:


78


Figure 5.1: Simple harmonic motion of ln _𝑧_ and ln _𝑝_ .

_<u>𝑓</u>_ ˜( _<u>𝑧</u>_ <u>(</u> _𝑡_ <u>))−1</u> . where, again, wedefinetheinfinitesimalgrowthrate _𝑓_ via _𝑓_<sup>�</sup> _𝑧_ ( _𝑡_ )<sup>�</sup> ≡ limΔ _𝑡_ →0 Δ _𝑡_ We note that it makes biological sense that _ℎ_ (and _ℎ_<sup>˜</sup> ) should be a monotonically increasing concave function, since it captures the diminishing returns of increasing food per individual mother. This motivates the following specific functional form for _ℎ_ :


where _𝑚_<sup><u>1</u>isascalingfactorrepresentingthestrengthofthegestationalmaternal</sup> effect. Note that in what follows _ℎ_ can be more general and include an additive constant, although we omit it for simplicity of presentation. Substituting (5.14) into (5.12) and defining _𝑝_ 0 := _𝑅_ yields:


Now, as suggested by the covariance term in (5.6), we consider the relationship _𝑑_ ln _<u>𝑝</u>_ <u>(</u> _𝑡_ <u>)</u> between Malthusian fitness _𝑟_ ( _𝑡_ ) = _𝑑𝑡_ and trait value _𝑧_ ( _𝑡_ ). If we assume that fitness is linearly related to the logarithm of the trait value, i.e. _𝑓_ ( _𝑧_ ( _𝑡_ )) = _𝑘_ ln( _𝑧_ ( _𝑡_ )) + _𝑐_ , for some constants, _𝑐_ and _𝑘_ , equation (5.13) becomes:


79

The form of equations (5.15-5.16) leads to the well-studied dynamics of simple harmonic motion for the logarithms of _𝑧_ and _𝑝_ . In particular, differentiating (5.15) and setting _𝑧_ 0 := _𝑒_ − _𝑘𝑐_ we find that:


Note that this second order differential equation resembles the acceleration equation for a mass on a spring, where _𝑘_ is the analog of a spring constant. The “stiffness” of the spring, _𝑘_ , is related to the strength of the trait’s effect on fitness. The angular frequency of the motion is determined by the product of _𝑘_ with the strength of the maternal effect, _𝑚_<sup><u>1</u>, via</sup><sup>_𝜔_=</sup> ~~√~~ _𝑚𝑘_<sup>.The explicit solution for ln (</sup><sup>_𝑧_) is given by:</sup>

ln _𝑧_ ( _𝑡_ ) = _𝐴_ cos( _𝜔𝑡_ ) + _𝐵_ sin( _𝜔𝑡_ ) + ln _𝑧_ 0 _, 𝑑_ ln _<u>𝑧</u>_ <u>(</u> _𝑡_ <u>)</u> where _𝐴_ = ln _𝑧_ (0) − ln _𝑧_ 0 and _𝐵_ = _𝜔_<sup><u>1</u></sup> _𝑑𝑡_ (0) . � �

The logarithmic population size also oscillates with simple harmonic motion according to:


so that:


Equation (5.15) shows that, for a certain form of maternal effect, there is a natural relationship between the time derivative of (the logarithm of) the trait value and the logarithm of the population size. By choosing the form of the selection “force” via _𝑓_ ( _𝑧_ ( _𝑡_ )), we can consider different kinds of “bound motion” of which simple harmonic motion is a fundamental example.

The evolution equations (5.7,5.8) and the extension (5.9) deal with single populations but can be readily extended to multiple subpopulations, which can then be aggregated to shed light on the behavior of a full system. Consider the case in which the _𝑖_<sup>t</sup><sup>_ℎ_</sup> subpopulation from among the _𝑛_ subpopulations has a value for a trait represented by _𝑧𝑖_ ( _𝑡_ ), a population size _𝑝𝑖_ ( _𝑡_ ), a fitness scaling _𝑘𝑖_ , and individual maternal effects _𝑚𝑖_ . Suppose, in addition, that each subpopulation follows simple harmonic motion as described above. The virial equation (5.6) applied to ln **z** ( _𝑡_ ) is:


80


Figure 5.2: Behavior of three subpopulations and the quantities in (5.20).

Since each subpopulation performs simple harmonic motion in ln _𝑧_ ( _𝑡_ ), E[ln( _𝑧_ )] = � _𝑖𝑛_ =1<sup>_𝑞𝑖_ln</sup><sup>_𝑧𝑖_is bounded,so the time average of</sup> _𝑑𝑡_<sup>_<u>𝑑</u>_E(ln</sup><sup>**z**(</sup><sup>_𝑡_))will go to zero.From</sup> equations (5.15) and (5.16) , we therefore have:


where we have defined the total population, _𝑃_ t _𝑜𝑡_ ( _𝑡_ ) =<sup>�</sup> _𝑖_<sup>_𝑝_</sup> _𝑖_<sup>(</sup><sup>_𝑡_).In the special case</sup> where the values _𝑘𝑖_ , _𝑚𝑖_ , _𝑐𝑖_ , and _𝑝_ 0 _𝑖_ are the same between subpopulations and given by _𝑘_ , _𝑚_ , _𝑐_ , and _𝑝_ 0, respectively, the above simplifies to:

81


This equation describes the balance between variation in the trait between subpopulations and the entropy in the distribution of subpopulation sizes, when subpopulations are following simple harmonic motion in the way we have described. When subpopulations have different trait values, selection acts to create a non-uniform distribution of populations sizes. This illustrates the essence of the general case (5.19), where the Shannon entropy is replaced by a weighted entropy (Suhov et al., 2016).

Notably, as a simple consequence of the Fourier theorem (Rudin et al., 1964), the combination of multiple subpopulations exhibiting simple harmonic motion can give rise to almost completely general dynamics for the overall population size: **Theorem 5** _(Universality of ecological orbits)_ **.** Maternal effects driving simple harmonic motion in subpopulations are sufficient to generate any periodic population dynamics that satisfy the Dirichlet conditions.

### **5.6 Spatial Population Growth**

Now, we consider a situation where a trait _𝑧_ affects the population growth rate of a subpopulation via competition with neighboring subpopulations. We first consider subpopulations that are spatially separated along one direction, such that each subpopulation is centered at a unique spatial coordinate, _𝑥_ , a distance Δ _𝑥_ away from its two nearest neighbors. Whereas before, the growth rate of each subpopulation was given by a function, _𝑓_ ( _𝑧_ ), of its average trait value, now the growth rate is determined by how much an ‘intrinsic fitness’ function, _𝑓_ i _𝑛𝑡_ ( _𝑧_ ), exceeds that of the subpopulation’s neighbors. This represents the competitive fitness advantage over the neighbors conferred by this trait. This situation would give rise to the following form for the population growth rate:


82

where _𝑧_ ( _𝑥, 𝑡_ ) is the average value of a trait in the subpopulation at position _𝑥_ , at time _𝑡_ , and Φ is a function relating the excess intrinsic fitness of a subpopulation over its neighbor to an additive contribution to its growth rate.

Since the function Φ represents the effect of competition over resources, it should increase with the difference in intrinsic fitness between neighboring populations, and decrease with their distance apart. If we posit that Φ is linear in the fitness differential between neighboring populations, and inversely proportional to the square of the distance between populations, we have that:


for some constant _𝜙_<sup>˜</sup> , where in the second line we have taken the limit as Δ _𝑥_ → 0. This represents the case where the distance between subpopulations is negligible compared with the distances covered by the overall population, and the spatial dimension becomes effectively continuous.

If we choose the intrinsic fitness function, _𝑓_ i _𝑛𝑡_ , to be linear in the logarithm of the trait: _𝑓_ i _𝑛𝑡_ = _𝜙_<sup>_<u>𝜙</u>_</sup> ˜<sup>ln (</sup><sup>_𝑧_) + c</sup><sup>_𝑜𝑛𝑠𝑡_, for</sup><sup>_𝜙_some new constant, then (5.22) implies:</sup>


If, within each subpopulation, (i.e. at each spatial coordinate), we retain the maternal effect relation from above (5.15), the dynamics for _𝑧_ are described by:


This is the one-dimensional wave equation for ln( _𝑧_ ). The speed of the waves in this system would be given by _𝑐_<sup>2</sup> = _𝑚_<sup>_<u>𝜙</u>_.Thespeedofpropagationofthesewaves</sup> increases with the strength of the maternal effect ( _𝑚_<sup><u>1</u>)andthesizeoftheeffectof</sup> relative intrinsic fitness on the growth rate for a subpopulation ( _𝜙_ ). This formulation

83


Figure 5.3: A snapshot of the evolution of ln ( _𝑧_ ) via the wave equation with two spatial coordinates (units are arbitrary).

could be straightforwardly extended to the more realistic two-dimensional case, with the substitution of the spatial gradient operator, ∇<sup>2</sup> , in place of the one-dimensional derivative. Dynamics for ln ( _𝑧_ ) in the two-dimensional case are illustrated in Figure 5.3.

A solution to the one-dimensional homogeneous wave equation (5.24) is given by the sum of modes of the form:


where _𝛼𝑛_ are constants and<sup>_𝜔_</sup> _𝑘 𝑛_<sup>_<u>𝑛</u>_=</sup> ~~√~~ _𝑚𝜙_<sup>forallmodes,</sup><sup>_𝑛_.Thiscorrespondstoa</sup> solution for ln ( _𝑝_ ) of the form:


where, again, _𝑝_ 0 is defined as _𝑅_ in (5.14). An example of these solutions at a single point in time is shown in Figure 5.4.

84


<!-- Start of picture text -->
4<br>ln(z)<br>2 ln(p)<br>0<br>2<br>k1 = 2,  1 = 4,  1 = 1<br>4<br>10 ln(z)<br>ln(p)<br>0<br>k1 = 4,  1 = 12.0,  1 = 0.5<br>10 k2 = 2,  2 = 6.0,  2 = 1.5<br>0 1 2 3 4 5 6<br>Spatial dimension x<br><!-- End of picture text -->

Figure 5.4: Spatial oscillations of the logarithmic trait value (ln ( _𝑧_ )) and population size (ln ( _𝑝_ )) for solutions of the one-dimensional wave equation of the form (5.25, 5.26). The top panel depicts the spatial pattern for a single mode, and the bottom panel the sum of two modes, with amplitudes and wavenumbers shown.

We then return to the virial-Price equation (5.5), again taking ln ( _𝑧_ ) as our trait. The _𝑑_ ln <u>(</u> _<u>𝑧</u>_ <u>(</u> _𝑡_ <u>))</u> E _𝑑𝑡_ term evaluates to zero as in the simple harmonic motion example above. � � For the covariance term, using the explicit forms of the solutions in (5.25, 5.26), and considering the case of a single wave mode with amplitude _𝛼_ and frequencies _𝑘, 𝜔_ , we have:


where, as above, the expectations in the variance are taken over the population fractions, _𝑞𝑖_ , for each spatially separated subpopulation. We therefore have, analogously to equation (5.20), that:


where _𝑃_ t _𝑜𝑡_ is given by summing the subpopulation sizes at each spatial position. The second term is related to the entropy of the population distribution, as before,

85

and the first term is related to the amplitude and frequency of the oscillatory mode of the system, and is reminiscent of mass multiplied by the energy within a single wave. A large, high frequency wave oscillation in ln( _𝑧_ ) implies a large variation in _𝑑_ ln <u>(</u> _<u>𝑧</u>_ <u>)</u> _𝑑𝑡_ , and hence large variations in ln ( _𝑝_ ) (5.15), leading to a lower entropy in the distribution of _𝑞_ .

### **5.7 Evolutionary theory and Newtonian mechanics**

The _dynamical interpretation_ of evolutionary theory posits a correspondence between theories of evolution and Newtonian mechanics (Sober, 1984; Hitchcock and Velasco, 2014). In this framework, notions such as selection or mutation in biology are associated to forces in physics (Sober, 1984). For example, the dynamical interpretation of evolutionary theory posits that directional selection is a constant force that accelerates allele frequency change, whereas mutation provides a diffusive force introducing variability into evolutionary trajectories. The identical form of equations (5.5) and (5.6) can constrain such associations and clarify subsequent analogies (Table 5.1). For example, although the standard form of the virial theorem (5.3) is an energy equation, equation (5.6) is a velocity equation, which in biology translates to rates of change of biological quantities. Furthermore, rate of change of a trait or phenotype, i.e., _𝑑𝑡𝑑_<sup>E(</sup><sup>**z**(</sup><sup>_𝑡_))inequation(5.5)orthefinitedifference</sup> <u>Δ</u> **<u>z</u>** ( _𝑡_ ) in equation (5.4), corresponds to the momentum-averaged bulk velocity of a collection of physical objects. The momentum-averaged positions E( **z** ( _𝑡_ )) and velocities _𝑑𝑡_<sup>_<u>𝑑</u>_E(</sup><sup>**z**(</sup><sup>_𝑡_))are discrete analogs of momentum-averaged position and mo-</sup> mentum velocity in electromagnetism, where they emerge from the virial density in an application of the virial theorem to electromagnetic pulses (Englert, 2014). Whereas cov( **r** ( _𝑡_ ) _,_ **z** ( _𝑡_ )) is frequently referred to as the _selection term_ in the Price equation (Bourrat et al., 2023), the connection to the virial theorem suggests that _𝑑_ **z** <u>(</u> _𝑡_ <u>)</u> it is better described as a selection _rate_ . Similarly, the _transmission_ term E _𝑑𝑡_ � � is more accurately a transmission _rate_ . Most significantly, while the dynamical interpretation typically relies on associating force to natural selection, drift, migration, or mutation (Hitchcock and Velasco, 2014), the equivalence between the virial theorem and the Price equation, suggests that force is more naturally associated to fitness. The correspondence of force to a rate of change is not surprising, since force is the rate of change of momentum. This stands more in line with the _statistical interpretation_ of evolutionary theory (Dennis M Walsh, 2000; Denis M Walsh, Lewens, and Ariew, 2002; Matthen and Ariew, 2002), which, among several critiques of the dynamical interpretation, finds fault with the analogies of biological

86

processes such as mutation with forces in physics, arguing that the physical forces are causal in a way that processes such as selection or mutation are not (Dennis M Walsh, 2000). However, the analogy of population growth with force can be viewed as consistent with the dynamical interpretation; for example, population growth can directly affect DNA polymorphism patterns (Williamson et al., 2005). Moreover, the virial theorem in the setting of the ecological simple harmonic oscillator affirms (Hitchcock and Velasco, 2014) in noting that “natural selection turns out to be more similar to forces such as friction and elastic forces rather than the more canonical gravitation.”

Table 5.1: Glossary of Terms

|Variable|Biology|Physics|Dim.|
|---|---|---|---|
|_𝑖_<br>_𝑧𝑖_(_𝑡_)<br>|subpopulation<br>trait / phenotype|object<br>position|-<br>L<br>|
|_𝑑𝑧𝑖_(_𝑡_)<br>_𝑑𝑡_|evolutionary rate|velocity|LT<sup>−1</sup><br>|
|_𝑟𝑖_(_𝑡_)|Malthusian fitness|acceleration÷velocity|T<sup>−1</sup><br>|
|_𝑝𝑖_(_𝑡_)|population size|momentum|MLT<sup>−1</sup>|
|_𝑞𝑖_(_𝑡_)<br>|relative population size|relative momentum|1|
|_𝑑𝑝𝑖_(_𝑡_)<br>_𝑑𝑡_|population growth rate|force|MLT<sup>−2</sup>|
|E(**z**(_𝑡_))|population-averaged|momentum-averaged|L|
||trait/phenotype|position||
|_𝑑_<br>_𝑑𝑡_<sup>E(</sup><sup>**z**(</sup><sup>_𝑡_))</sup>|group evolutionary rate|bulk momentum<br>velocity|LT<sup>−1</sup><br>|
|cov(**r**(_𝑡_)_,_**z**(_𝑡_))<br>E<br>�<br>_𝑑_**z**(_𝑡_)<br>_𝑑𝑡_<br>�|selection rate<br>transmission rate|extrinsic momentum<br>velocity<br>intrinsic momentum<br>velocity|LT<sup>−1</sup><br>LT<sup>−1</sup>|


In particular, considerations of the analogies between biology and physics via the virial theorem led us to generalize the work of (L. Ginzburg and Colyvan, 2004) and to derive the ecological simple harmonic oscillator, which to our knowledge is the first example of such an oscillator that emerges solely from maternal effects and does not require a predator-prey or other more sophisticated model. The extension of (5.8) to (5.9) is interesting in its own right, and should be fruitful to develop in future work. Moreover, Theorem 5 shows that subpopulations subject to distinct maternal effects can generate arbitrarily complex population dynamics, thereby affirming the main thesis of (L. Ginzburg and Colyvan, 2004). We have further extended Ginzburg and Colyvan’s work (L. Ginzburg and Colyvan, 2004) by considering

87

an ecological model for spatial population growth. In this model, competition between neighboring populations, combined with maternal effects, gives a spatial wave equation for trait evolution (5.24). In both the simple harmonic motion and spatial models, we have shown that simple ecological mechanisms can reproduce the fundamental modes of motion in physics. Whilst the similarity between the ecological equations and physical equations of motion (e.g. the resemblence of (5.17) to a mass on a spring) is optical only, the usefulness of such equations in deriving fundamental modes of ecological motion highlights the utility of alternative physical-biological analogies to those chosen in Table 5.1.

Ultimately, analogies between the Price equation and the virial theorem point towards potentially productive directions for exploration in both biology and physics. The statistical framing of the virial theorem in (5.6) highlights phenomena that may have been overlooked in the physics realm. For example, the first term on the right-hand side of (5.6), namely cov( **r** ( _𝑡_ ) _,_ **z** ( _𝑡_ )), can be understood to quantify the extent of the Yule-Simpson effect (Pearson, Lee, and Bramley-Moore, 1899; Yule, 1903; Simpson, 1951), which describes a situation where within-group trends can be reversed upon averaging. In biology, the Price equation has the potential to be used more widely as a tool. Although it has been hailed as a unifying framework for researchers (Luque, 2017), one that “can serve as a heuristic principle to formulate and systematize different theories and models in evolutionary biology” (Luque and Baravalle, 2021), the emphasis on its use has been more oriented toward understanding how it generalizes specific equations, rather than applying it for biological discovery. For example, the Price equation can be used to derive the breeder’s equation (Bijma, 2020; Zhang and Hill, 2010), Fisher’s fundamental theorem (Queller, 2017; Price, 1972), the high rare mutation large effect “house of cards approximation” regime for genetic variance at mutation-selection balance (Zhang and Hill, 2010; Turelli, 1984), and many other formulas and identities in genetics (Zhang and Hill, 2010; Rice, 2004). However, it has been referred to as a tautology and a vacuous statement without application. In (Van Veelen et al., 2012) the Price equation is described as a theorem that establishes that “If the left-hand side is computed as suggested in (Price et al., 1970), and the right-hand side too, then they are equal.” This critique of the Price equation, namely that it does not and cannot serve as a _tool_ , stands in contradiction to evidence from physics, where the mathematically equivalent virial theorem has been understood as a powerful tool since its use to discover dark matter in 1933 (Zwicky, 1933). In fact, the Price equation has already been used to deduce the existence of specific environmental

88

effects in evolutionary biology. Grant and Grant (P. R. Grant and B. R. Grant, 1995) conducted an experiment on Daphne Major, a Galápagos island, capturing and labeling mature finches and their offspring. They were able to measure the change in mean trait value between successive generations. They also compared the trait measurements in adult populations before and after selection events to determine selection rates. They used the breeder’s equation, a restricted form of the Price equation, to predict the measured mean trait change from the measured selection rates and known heritabilities. Specifically, they start with the breeder’s equation, _𝑅_ = _ℎ_<sup>2</sup> _𝑠_ , where _𝑅_ , the response, is equivalent to the change in the mean, Δ _𝑧_ ¯. The heritablity, _ℎ_<sup>2</sup> , and selection strength, _𝑠_ , combine to give a linear approximation to the covariance term in the Price equation. They then expand to a multivariate version of this term, which takes into account the correlation of different traits. For the six traits they considered, the equations, _𝑖_ = 1 _, . . . ,_ 6, become:


where the _𝛽𝑖_ are direct selection coefficients on each trait, _𝑖_ , and the _𝑟 𝑗𝑖_ represent the genetic correlations between traits _𝑖_ and _𝑗_ . Note that the final term of the Price equation, ∝ E( **_w_** ⊙Δ **_z_** ), is ignored in this framework. Where there was a gap between their predictions and the measured mean trait change, they were able to identify environmental effects which made this non-selective term of the Price equation significant. They predicted a restricted food supply which affected the growth of the adult finches, which corresponded to a drought period. The gap identified by Grant and Grant is analogous not only to the way the virial theorem is used in physics and astrophysics (Marc and McMillan, 1985), but also to the missing heritability in human genetics where heritability for complex traits estimated from twin studies do not match heritability estimates derived from genome-wide association studies. In other words, the equivalence we have demonstrated between the Price equation and the virial theorem shows that the description of missing heritability as dark matter (Manolio et al., 2009) may be understood to be more than just an informal analogy between mysteries in genetics and astronomy.

### **Author Contributions and Acknowledgements**

SL studied the virial theorem while participating in the “Introduction to Astrophysics” cluster in the COS- MOS summer program held at UC Irvine from July 9,

89

2023 to August 4, 2023. Specifically, she used the virial theorem to repeat Zwicky’s Coma cluster mass estimates using modern measurements of velocity dispersion and galaxy positions. LP learned of the virial theorem from SL and, in discussing its proof with SL, realized that it must be related to the Price equation. SL and LP explored the applications and implications of the connection. CF identified and developed the connection to ecological orbits and simple harmonic motion via the maternal effect. LP drafted the initial manuscript; both SL and LP edited the first version posted on arXiv [24]. CF, SL, and LP edited the final version and code [12]. The authors are ordered alphabetically.

SL thanks Manoj Kaplinghat and Gopolang Mohlabeng who led the “Introduction to Astrophysics” cluster (cluster 4) at the 2023 UC Irvine COSMOS program. LP relied in part on notes about Fisher’s theorem of natural selection from his April 22, 2008 lecture for UC Berkeley course Math 239: Discrete Mathematics for the Life Sciences that were transcribed and edited by Cynthia Vinzant and Caroline Uhler. LP thanks Junhyong Kim for suggesting a possible connection of this work to the ideas in the book Ecological Orbits: How Planets Move and Populations Grow by Lev Ginzburg and Mark Colyvan, a discussion that led to CF’s extension of the work described in the book and the sections on simple harmonic motion and spatial population growth. CF was partially supported by funding from Charles Trimble.

### **References**

- Alazard, Thomas and Claude Zuily (2023). “Virial theorems and equipartition of energy for water-waves”. In: _arXiv preprint arXiv:2304.07872_ .

- Andersen, Esben S (2004). “Population thinking, Price’s equation and the analysis of economic evolution”. In: _Evolutionary and Institutional Economics Review_ 1, pp. 127–148.

- Bian, Jiang-Hui et al. (2015). “Maternal effects and population regulation: maternal density-induced reproduction suppression impairs offspring capacity in response to immediate environment in root voles Microtus oeconomus”. In: _Journal of Animal Ecology_ 84.2, pp. 326–336. doi: `https://doi.org/10.1111/13652656.12307` . eprint: `https://besjournals.onlinelibrary.wiley.com/ doi / pdf / 10 . 1111 / 1365 - 2656 . 12307` . url: `https : / / besjournals . onlinelibrary.wiley.com/doi/abs/10.1111/1365-2656.12307` .

- Bijma, P (2020). “The Price equation as a bridge between animal breeding and evolutionary biology”. In: _Philosophical Transactions of the Royal Society B_ 375.1797, p. 20190360.

- Binney, James and Michael Merrifield (1998). _Galactic Astronomy_ .

90

- Bourrat, Pierrick et al. (2023). “What is the price of using the Price equation in ecology?” In: _Oikos_ , e10024.

- Boycott, Arthur Edwin et al. (1931). “II. The inheritance of sinistrality in _Limnæa peregra_ (Mollusca, Pulmonata)”. In: _Philosophical Transactions of the Royal Society of London. Series B, Containing Papers of a Biological Character_ 219, pp. 51–131. doi: `10.1098/rstb.1931.0002` . url: `http://doi.org/10. 1098/rstb.1931.0002` .

- Clausius, Rudolf (1870). “XVI. On a mechanical theorem applicable to heat”. In: _The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science_ 40.265, pp. 122–127.

- Cresson, Jacky, Laurent Nottale, and Thierry Lehner (2021). “Stochastic modification of Newtonian dynamics and induced potential—Application to spiral galaxies and the dark potential”. In: _Journal of Mathematical Physics_ 62.7.

- Einstein, Albert (1922). “Die Grundlage der allgemeinen Relativitätstheorie”. In: _Annalen der Physik_ 49.7.

- Ellner, Stephen P, Monica A Geber, and Nelson G Hairston Jr (2011). “Does rapid evolution matter? Measuring the rate of contemporary evolution and its impacts on ecological dynamics”. In: _Ecology letters_ 14.6, pp. 603–614.

- Englert, Berthold-Georg (2014). _lectures on classical electrodynamics_ . World Scientific Publishing Company.

- Fisher, Ronald A (1930). _The genetical theory of natural selection_ . Clarendon Press, Oxford, Valorium edition, Bennett JH (Editor), 1999, Oxford University Press, Oxford, UK].

- Fowler, Ralph H (1929). _Statistical Mechanics_ . Cambridge University Press, Cambridge, UK.

- Fox, Charles W., Meghna S. Thakar, and Timothy A. Mousseau (1999). “The evolutionary genetics of an adaptive maternal effect: egg size plasticity in a seed beetle”. In: _Evolution_ 53.2, pp. 552–560. doi: `10.1111/j.1558-5646.1999.tb03790. x` . url: `https://doi.org/10.1111/j.1558-5646.1999.tb03790.x` .

- Frank, Steven A (1997). “The Price equation, Fisher’s fundamental theorem, kin selection, and causal analysis”. In: _Evolution_ 51.6, pp. 1712–1729.

- Frank, Steven A and Montgomery Slatkin (1990). “The distribution of allelic effects under mutation and selection”. In: _Genetics Research_ 55.2, pp. 111–117.

- Georgescu, VladimirandChristian Gérard(1999). “Onthe virialtheoremin quantum mechanics”. In: _Communications in Mathematical Physics_ 208.2, pp. 275–281.

- Ginzburg, Lev and Mark Colyvan (2004). _Ecological orbits: How planets move and populations grow_ . Oxford University Press.

91

- Ginzburg, Lev R. and Dale E. Taneyhill (1994). “Population Cycles of Forest Lepidoptera: A Maternal Effect Hypothesis”. In: _Journal of Animal Ecology_ 63.1, pp. 79–92. issn: 00218790, 13652656. url: `http://www.jstor.org/stable/ 5585` (visited on 12/06/2024).

- Grant, Peter R. and B. Rosemary Grant (Apr. 1995). “Predicting microevolutionary responses to directional selection on heritable variation”. In: _Evolution_ 49.2, pp. 241–251. doi: `10.1111/j.1558-5646.1995.tb02236.x` .

- Hanson, Mervin P (1995). “The virial theorem, perfect gases, and the second virial coefficient”. In: _Journal of chemical education_ 72.4, p. 311.

- Harding, JE (Feb. 2001). “The nutritional basis of the fetal origins of adult disease”. In: _International Journal of Epidemiology_ 30.1, pp. 15–23. issn: 0300-5771. doi: `10.1093/ije/30.1.15` . eprint: `https://academic.oup.com/ije/articlepdf/30/1/15/18478235/300015.pdf` . url: `https://doi.org/10.1093/ ije/30.1.15` .

- Harman, Oren (2011). _The price of altruism: George Price and the search for the origins of kindness_ . WW Norton & Company, New York, NY.

- Hitchcock, Christopher and Joel D Velasco (2014). “Evolutionary and Newtonian forces”. In: _Ergo_ 1.2, p. 39.

- L’Hôpital, Guillame de (1696). _Analyse Des Infiniment Petits Pour L’Intelligence Des Lignes Courbes_ . Chez Montalant, Paris, France.

- Luque, Victor J (2017). “One equation to rule them all: a philosophical analysis of the Price equation”. In: _Biology & Philosophy_ 32.1, pp. 97–125.

- Luque, Victor J and Lorenzo Baravalle (2021). “The mirror of physics: on how the Price equation can unify evolutionary biology”. In: _Synthese_ 199.5-6, pp. 12439– 12462.

- Manolio, Teri A et al. (2009). “Finding the missing heritability of complex diseases”. In: _Nature_ 461.7265, pp. 747–753.

- Marc, Guilhem and William G McMillan (1985). “The Virial Theorem”. In: _Advances in Chemical Physics_ , pp. 209–361.

- Matthen, Mohan and André Ariew (2002). “Two ways of thinking about fitness and natural selection”. In: _The Journal of Philosophy_ 99.2, pp. 55–83.

- Merritt, David (1987). “The distribution of dark matter in the Coma cluster”. In: _The Astrophysical Journal_ 313, pp. 121–135.

- Mukhopadhyay, Banibrata, Arnab Sarkar, and Christopher A. Tout (2025). “Modified Virial Theorem for Highly Magnetized White Dwarfs”. In: (). (Visited on 09/12/2025).

- Nourmohammad, Armita, Torsten Held, and Michael Lässig (2013). “Universality and predictability in molecular quantitative genetics”. In: _Current opinion in genetics & development_ 23.6, pp. 684–693.

92

- Oguz, Hasan N and Andrea Prosperetti (1990). “A generalization of the impulse and virial theorems with an application to bubble oscillations”. In: _Journal of Fluid Mechanics_ 218, pp. 143–162.

- Pearson, Karl, Alice Lee, and Leslie Bramley-Moore (1899). “VI. Mathematical contributions to the theory of evolution.—VI. Genetic (reproductive) selection: Inheritance of fertility in man, and of fecundity in thoroughbred racehorses”. In: _Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character_ 6.192, pp. 257–330.

- Podio-Guidugli, Paolo (2019). “The virial theorem: A pocket primer”. In: _Journal of Elasticity_ 137.2, pp. 219–235.

- Price, George R et al. (1970). “Selection and covariance.” In: _Nature_ 227, pp. 520– 521.

- Price, George R (1972). “Fisher’s ‘fundamental theorem’ made clear”. In: _Annals of human genetics_ 36.2, pp. 129–140.

- Queller, David C (2017). “Fundamental theorems of evolution”. In: _The American Naturalist_ 189.4, pp. 345–353.

- Rayleigh, Lord (1905). “XLII. On the momentum and pressure of gaseous vibrations, and on the connexion with the virial theorem”. In: _The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science_ 10.57, pp. 364–374.

- Reznick, D., H. Callahan, and R. Llauredo (2015). “Maternal Effects on Offspring Quality in Poeciliid Fishes”. In: _American Zoologist_ 36.2, pp. 147–156. doi: `10.1093/icb/36.2.147` .

- Rice, Sean H (2004). _Evolutionary theory: mathematical and conceptual foundations_ . Sinauer Associates, Sunderland MA.

- (2008). “A stochastic version of the Price equation reveals the interplay of deterministic and stochastic processes in evolution”. In: _BMC evolutionary biology_ 8, pp. 1–16.

- Roseboom, Tessa, Susanne de Rooij, and Rebecca Painter (Aug. 2006). “The Dutch famine and its long-term consequences for adult health”. In: _Early Human Development_ 82.8. Epub 2006 Jul 28, pp. 485–491. doi: `10.1016/j.earlhumdev. 2006.07.001` . url: `https://doi.org/10.1016/j.earlhumdev.2006.07. 001` .

- Rudin, Walter et al. (1964). _Principles of mathematical analysis_ . Vol. 3. McGraw-hill New York.

- Shore, Steven N (2012). _An introduction to astrophysical hydrodynamics_ . Academic Press, Cambridge, MA.

- Simpson, Edward H (1951). “The interpretation of interaction in contingency tables”. In: _Journal of the Royal Statistical Society: Series B (Methodological)_ 13.2, pp. 238–241.

93

- Sober, Elliott (1984). _The nature of selection_ . MIT Press, Cambridge, MA.

- Suhov, Yuri et al. (2016). “Basic inequalities for weighted entropies”. In: _Aequationes mathematicae_ 90, pp. 817–848.

- The, Lih S and Simon D M White (1986). “The mass of the Coma cluster”. In: _Astronomical Journal_ 92.6, pp. 1248–1253.

- Thorne, E Tom, Ron E Dean, and William G Hepworth (1976). “Nutrition during gestation in relation to successful reproduction in elk”. In: _The Journal of Wildlife Management_ , pp. 330–335.

- Turelli, Michael (1984). “Heritable genetic variation via mutation-selection balance: Lerch’s zeta meets the abdominal bristle”. In: _Theoretical population biology_ 25.2, pp. 138–193.

- Van Veelen, Matthijs et al. (2012). “Group selection and inclusive fitness are not equivalent; the Price equation vs. models and statistics”. In: _Journal of theoretical biology_ 299, pp. 64–80.

- Wagner, Günter P (2010). “The measurement theory of fitness”. In: _Evolution_ 64.5, pp. 1358–1376.

- Walsh, Denis M, Tim Lewens, and André Ariew (2002). “The trials of life: Natural selection and random drift”. In: _Philosophy of Science_ 69.3, pp. 452–473.

- Walsh, Dennis M (2000). “Chasing shadows: natural selection and adaptation”. In: _Studies in History and Philosophy of Science Part C: Studies in History and Philosophy of Biological and Biomedical Sciences_ 31.1, pp. 135–153.

- Williamson, Scott H et al. (2005). “Simultaneous inference of selection and population growth from patterns of variation in the human genome”. In: _Proceedings of the National Academy of Sciences_ 102.22, pp. 7882–7887.

- Wolf, Jason B. and Michael J. Wade (Apr. 2009). “What are maternal effects (and what are they not)?” eng. In: _Philosophical Transactions of the Royal Society B: Biological Sciences_ 364.1520. Place: London Publisher: Royal Society, pp. 1107– 1115. issn: 0962-8436. doi: `10.1098/rstb.2008.0238` .

- Yule, G Udny (1903). “Notes on the theory of association of attributes in statistics”. In: _Biometrika_ 2.2, pp. 121–134.

- Zhang, Xu-Sheng and William G Hill (2010). “Change and maintenance of variation in quantitative traits in the context of the Price equation”. In: _Theoretical population biology_ 77.1, pp. 14–22.

- Zwicky, Fritz (1933). “Die Rotverschiebung von extragalaktischen Nebeln”. In: _Helvetica Physica Acta, Vol. 6, p. 110-127_ 6, pp. 110–127.

94

_C h a p t e r 6_

---

[← BIOPHYSICS OF GENE EXPRESSION EVOLUTION](09-biophysics-of-gene-expression-evolution.md) · [Up: contents](index.md) · [FUTURE DIRECTIONS →](11-future-directions.md)
