---
title: derivative is zero.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/j1s9jfzkfqu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# derivative is zero.

**Source:** `recordings/j1s9jfzkfqu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**The one difference is that we can't write out analytically what this function looks like and choose directions and locations in space that are the minima. So we're going to have to take an approach that has a series of perturbations to a structure that try to improve the free energy systematically.**

**The simplest understanding is this gradient descent approach, which says that I have some initial coordinates that I choose and I take a step in the direction of the first derivative of the function. So what does that look like?**

**So here are two possibilities. I've got this function. If I start off at x equals 2, this minus some epsilon, some small value times the first derivative, is going to point me to the left. And I'm going to take steps to the left until this function, f prime, the first derivative, is zero. Then I'm going to stop moving. So I move from my initial coordinate a little bit each time to the left until I get to the minimum. And similarly, if I start off on the right, I'll move a little bit further to the right each time until the first derivative is zero.**

**So that looks pretty good. It can take a lot of steps, though. And it's not actually guaranteed to have great convergence properties. Because of the number of steps you might have to take, it might take quite a long time. So that's the first derivative, in a simple one-dimensional case. We're dealing with a multi-dimensional vector, so instead of doing the first derivative we use the gradient, which is a set of partial first derivatives.**

**And I think one thing that's useful to point out here is that, of course, the force is negative of the gradient of the potential energy. So when we do gradient descent, you can think of it from a physical perspective as always moving in the direction of the force. So I have some structure. It's not the true native structure, but I take incremental steps in the direction of the force and I move towards some local minima.**

**And we've done this in the case of a continuous energy, but you can actually also**

6

**do this for discrete ones.**

**Now, the critical point was that you're not guaranteed to get to the correct energetic structure. So in the case that I showed you before where we had the side chain side-on, if you actually do the minimization there, you actually end up with the side chain rotated 180 degrees where it's supposed to be. So it eliminates all the steric clashes, but it doesn't actually pick up all the hydrogen bonds. So this is an example of a local energetic minima that's not the global energetic minima.**

**Any questions on that? Yes.**

**AUDIENCE: Where do all these n-dimensional equations come from?**

**PROFESSOR: Where do what come from?**

**AUDIENCE: The n-dimensional equations. PROFESSOR: So these are the equations for the energy in terms of every single atom in the protein if you're allowing the atoms to move, or in terms of every rotatable bond, if you're allowing only bonds to rotate.**

**So the question was, where do the multi-dimensional equations come from. Other questions? OK. All right, so that's the simplest approach. Literally minimize the energy. But we said it has this problem that it's not guaranteed to find the global free energy minimum. Another approach is molecular dynamics. So this actually attempts to simulate what's going on in a protein structure in vitro, by simulating the force in every atom and the velocity. Previously, there was no measure of velocity. Right? All the atoms were static. We looked at what the gradient of the energy was and we move by some arbitrary step function in the direction of the force.**

**Now we're actually going to have velocities associated with all the atoms. They're going to be moving around in space. And we'll have the coordinate at any time t is going to be determined by the coordinates of the previous time, t of i minus 1 plus a**

7

**velocity times the time step. And the velocities are going to be determined by the forces, which are determined by the gradient of the potential energy. Right?**

**So we start off, always, with that potential energy function, which is either from the physics approach or the statistical approach. That gives us velocities, eventually giving us the coordinates.**

**So we start off with the protein. There are some serious questions of how you equilibrate the atoms. So you start off with a completely static structure. You want to apply forces to it. There are some subtleties as to how you go about doing that, but then you actually end up simulating the motion of all the atoms.**

**And just give you a sense of what that looks like, I'll show you a quick movie. So this is the simulation of the folding of a protein structure. And the backbone is mostly highlighted. Most of the side chains are not being shown. Actually, in bold, but you can see the stick figures. And slowly it's accumulating its three-dimensional structure.**

**[VIDEO PLAYBACK]**

**[LAUGHTER]**

---

[← PROFESSOR](02-professor.md) · [Up: contents](index.md) · [[END VIDEO PLAYBACK] →](04-end-video-playback.md)
