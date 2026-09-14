---
title: 08 questions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/08-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 08 questions

**Source:** `psets/08-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

8.592J–HST.452J: Statistical Physics in Biology

Assignment # 8

Drift, Diffusion, and Dynamic Instability

1. Treadmilling Actin: Actin filaments are long, asymmetric, polymers involved in a variety of cellular functions. In some cases the filaments are in a dynamic state in which monomers are removed from one end and added to the other. (The two ends are called minus and plus respectively, and this process is known as treadmilling.)

(a) Assume that monomers are added to the plus-end at rate a, and removed from the minus end at rate b. Write down the equations governing the rate of change of the probabilities {p(ℓ, t)}, for finding a filament of length ℓ at time t. Note that ℓ = 1, 2, , 3, · · · , and that the equation of p(1, t) is different from the rest.

- (b) It is possible to have a dynamic steady state with probabilities p<sup>∗</sup> (ℓ) that do not change with time. Find the (properly normalized) distribution p<sup>∗</sup> (ℓ) in such a case.

(c) What is the condition for the existence of a time independent steady state, and the mean length of the filament in such a case?

(d) For a > b, what is the average length of a filament at time t, starting from individual monomers at time t = 0? Calculate the fluctuations (variance) in length, and write down an approximate probability distribution p(ℓ, t) with the correct first and second moment.

*****

2. Growing/shrinking microtubules: Consider a slightly generalized model of microtubule growth and shrinkage [M. Dogterom and S. Leibler, Phys. Rev. Lett. 70, 1347 (1993)], described by the equations


(a) Such coupled linear equations are usually solved by first Fourier transforming to p˜(k, ω) = J dxdte<sup>i(kx−ωt)</sup> p(x, t). Find the dispersion relations for allowed ω(k).

(b) Expand the ‘slowly varying’ mode as ω(k) = vk + iDk<sup>2</sup> + O(k<sup>3</sup> ), and hence obtain the dependence of the drift velocity and diffusion coefficient of the microtubule length on the parameters describing the growing and shrinking states.

(c) Typical values of parameters for microtubules growing in a tubulin solution of concen­ tration c ≈ 10µM are v+ ≈ 2µm/min, v− ≈ 20µm/min, f+− ≈ 0.004s<sup>−1</sup> , f−+ ≈ 0.05s<sup>−1</sup> . Use these parameters (along with d = 0) to estimate a time scale τ beyond which diffusion effects are less important than the average drift. (Hence microtubules that have survived to a time τ are unlikely to be completely eliminated by catastrophes.)

(d) Let us assume a microscopic model in which growth occurs by addition of discrete molecules of size a at rates r+ to the growing state, and detachment at rate r− shrinking state. Write the corresponding Master equations and construct their continuum limit.

*****

1

3. Internal states: Consider a molecular motor modeled by an asymmetric hopping model with m internal states. Assume equal forward rates and no backward rates; i.e. ui = u and wi = 0 for i = 1, · · · , m. Visscher et al., in Nature 400, 184 (1999), use such a model to estimate the number of (rate limiting) internal states from observations of motion of kinesin on microtubules. In particular, they measure a ‘randomness parameter’ defined by


where x(t) is the displacement of the motor after a time t, and d is the step size of kinesin along the microtubule.

(a) Relate r defined above to the parameters v and D of a drift–diffusion equation.

(b) Obtain v and D in terms of the parameters u, d, and m of the model.

(c) The experimental data (Fig. 4b of the above reference) indicate r ≈ 1/2 at small force, and r ≈ 1 at large force. What does this imply about the internal states of the motor?

*****

4. Two state motor: Let us examine the two-state motor (with step length d) in more detail. At each site the motor can be in one of two states, indicated by n or n ′ for the n<sup>th</sup> site. The forward transition rates are u1 (for internal state change from n to n<sup>′</sup> ) and u2 (for hopping from n<sup>′</sup> to n + 1), and the corresponding backward transition rates are w1 and w2.

(a) Write down the master equations governing the time evolution of the probabilities p(n, t) and p(n<sup>′</sup> , t).

(b) Use Fourier transforms to obtain the dispersion relation ω(k) for the slowly varying mode.

(c) Calculate the drift velocity v, the diffusion coefficient D, and the Einstein force fE, as a function of u1, u2, w1, and w2. (d) Assume that under an external load F , the forward hopping rate changes as u2 → u2 exp −<sup>fd</sup> ( kB T )<sup>, while all the other rates remain unchanged. Calculatev(f), andobtain the</sup> stalling force fs.

(e) Direct observation of kinesin motors moving along microtubules (by Block’s group at Stanford using in vitro solution of [ATP]=2mM) indicate v ≈ 670nm/s, D ≈ 1400nm<sup>2</sup> /s, and fs ≈ 5pN. Data from chemical analysis suggest that forward state changes occur at rates of u1 ∼ 2 × 10 s3<sup>−1</sup> and u2 ∼ 50s −1. The backward rates are harder to measureassume values of w1 ∼ u1/100 and w2 ∼ u2/100. How consistent are these results with a two state model? *****

5. Chemotaxis: The motion of E. Coli in a solution of nutrients consists of an alternating sequence of runs and tumbles. During a run the bacterium proceeds along a straight line for a time tr with a velocity v. It then tumbles for a time tt, after which it randomly chooses

2

a new direction nˆ to run along. Let us assume that the times tr and tt are independently selected from probability distributions


(a) Assuming values of τr ≈ 2s, τt ≈ 0.2s, and v ≈ 30µms<sup>−1</sup> , calculate the diffusion coefficient D for the bacterium at long times.

(b) In the presence of a chemical gradient the run times become orientation dependent, and are longer when moving in a favorable direction. For preferred motion up the z axis, let us assume that the average run time depends on its orientation nˆ according to τr (nˆ) = τ0+gnˆ·zˆ. Calculate the average drift velocity at long times.

*****

3

MIT OpenCourseWare http://ocw.mit.edu

8.592J / HST.452J Statistical Physics in Biology Spring 2011

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
