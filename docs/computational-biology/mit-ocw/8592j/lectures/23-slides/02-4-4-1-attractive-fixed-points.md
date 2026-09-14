---
title: 4.4.1 Attractive fixed points
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.4.1 Attractive fixed points

**Source:** `lectures/23-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

With only one variable, the generic outcome is for it to approach an attractive fixed point. This is because the one dimensional equation can be regarded as describing descent in a potential V (x), as


The coordinate x will descend in this potential, settling down to possible fixed points that are solutions to F (x<sup>∗</sup> ) = 0. Note that a general function F (x) does not necessarily have a zero. However, in most physically relevant situations the variable x is constrained to a finite interval; for example, the concentration of a chemical has to be positive and less than some maximal value. In such cases V (x) is effectively infinite outside the allowed interval, and the potential will have a minimum, possibly at the limits of the interval. The function V (x) is also relevant to the stochastic counterpart of Eq. (4.21): The addition of uncorrelated noise η(t) to this equation (with ⟨η(t)⟩ = 0 and ⟨η(t)η(t<sup>′</sup> )⟩ = 2Dδ(t − t<sup>′</sup> )) results in a Lang´evin equation with steady steady probability density p<sup>∗</sup> (x) ∝ [−V (x)/D].

76


The above conclusions hold for coupled equations with many variables, only if they correspond to gradient descent in a multi-variable potential V (x1, x2, · · · , xN ), i.e. for


The equality of second derivatives then immediately implies that


This condition is too constraining, for example in a linear system with Fi =<sup>�</sup> j<sup>Wijxjit</sup> requires symmetric interactions with Wij = Wji.

An interesting variant of gradient descent that avoids the constraint of symmetric interactions is provided by Hopfield’s model of a neural network with graded response. In this model the activity of each neuron is indicated by a variable xi (related to the spiking rate of the neuron), and evolves in time according to


In Eq. (4.24), τ is a natural time constant for decay of activity in the absence of stimuli, and for simplicity we set it to unity; bi represents external input to the network, say from sensory cells; and Wij is a matrix encoding the strength of synaptic connections from neuron j to neuron i. (The matrix does not have to be symmetric and in general Wij̸ = Wji.) The function f captures the input/output characteristics of the neuron’s response; it is assumed to be a monotonic function of its argument, typically a sigmoidal form that switches between a low and a high value at a threshold input (which can be folded into the parameter bi). A simplified version of the neural network assigns discrete binary values (say -1 and +1) to each neuron, and a randomly selected neuron i asynchronously switches depending on the sign of �j<sup>Wijxj+ bi.Hopfieldinfactintroducedthemodelwithcontinuousvariables{xi(t)}to</sup> address criticism that the binary model was too removed from biological neurons.<sup>1</sup>

> 1J.J. Hopfiled, Proc. Nat. Acad. Sci. 81, 3088 (1984).

77


For asymmetric connections,


and the Hopfield model does not correspond to gradient descent in a potential. Nonetheless, we can still demonstrate the existence of fixed points by introducing a Lyapunov function,


where the function G shall be defined shortly. The time derivative of L is given by


With appropriately chosen G, we can show that L is always either decreasing or stationary. To achieve this goal, let us set


where f<sup>−1</sup> (x) is the inverse function such that f<sup>−1</sup> [f (x)] = x. This definition implies that


where we have made the auxiliary definitions


Note that since f (x) is monotonically increasing, the two factors in Eq. (4.27) always have opposite signs, unless they happen to be zero, and thus


78

The proof of Eq. (4.29) is similar in spirit to that for the Boltzmann’s H-theorem in Statistical Physics. A similar proof exists for the discrete (binary) version of the network.

The activities of neurons in the Hopfield network thus proceed to attractive fixed points which are solutions to x<sup>∗</sup> i<sup>=f(bi+ �</sup> j<sup>Wijx</sup> j<sup>∗).ThefixedpointsoftheHopfieldmodelcan</sup> be interpreted as associative, or content addressable memories. The idea is to first imprint a memory in the network by appropriate choice of the couplings Wij. For a particular “memory” represented by {x<sup>∗</sup> i<sup>}, the network is trained according to ∆Wij= ηx</sup> i<sup>∗x∗</sup> j<sup>.The new</sup> network will be described by a Lyaponov function, L + ∆L, with a deeper minimum at the encoded memory as


The imprinting procedure is a computational implementation of the so called Hebbian rule according to which “neurons that fire together wire together.” If the thus trained network is presented with a partial or corrupted version of the stored memory, it is likely to be in the basin of the Lyapunov function that is attracted to the original memory. In principle one can store many different memories in the network, each with its own separate basin of attraction. Of course at some point the memories interfere, and the network has a finite capacity dependent on the number of its nodes.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [4.4.2 Stability, Bifurcation, and Cycles →](03-4-4-2-stability-bifurcation-and-cycles.md)
