---
title: 'AUDIENCE: [INAUDIBLE].'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/onl-uf4flvm-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE].

**Source:** `recordings/onl-uf4flvm-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Yes. Both in this case and the simple predator-prey oscillations. One thing we're going to see the predator-prey populations later is that you can also get this sort of oscillations in time. So this could be in time or this could be a function of space. But in both cases, it's really that you have a resonant enhancement in some areas. So that the demographic fluctuation somehow excite all frequencies or all wavelengths.**

**But then what happens is that, in this case, if you look at the eigenvalues-- OK, I want to be close to 0, though. If you look at how the modes decay-- so the eigenvalue's function of a wave number-- what you see is that you end up getting things that look like this.**

**So whereas a Turing pattern is when particular wave length or wave modes actually becomes unstable, and then you get mean field type patterns. And in this situation what happens is that you're just close here, so then you excite all the wave numbers or wavelengths. And then some of them take a long time to go away, so then they build up and then that's the resulting patterns that you see.**

**So what I want to do is just for the last 10 minutes to talk about this Min system. Because it's I think it's a beautiful example of a combination of Systems Biology questions together with reaction diffusion systems, and also some beautiful in vitro experiments that I've quite appreciated.**

**So the question is-- imagine yourself, you've gone to all this work right, so now you're nice and long. So you'd like to divide into two cells. And the question is, how do you know where to divide? So you imagine that you're some E. coli cell. You're maybe six microns long, everything is great. And the question is, you want to**

23

**divide? Where would you like to divide if you're an E. coli cell? Middle.**

**OK, so what you'd like to do is go here. And indeed, what happens is that there's the so-called z-ring. There's a a pseudo-polymer protein that forms a ring around here, then it constricts itself and pinches off the membrane. And that's how you get two cells.**

**So there's this formation of this z-ring that constricts and that's this cell division event. The question is how do you know where to put it? And that's what this Min system is for. And it's, of course, like everything in bacterial genetics, it was identify by mutations.**

**So the Min system it's called that because these mutants formed so-called mini cells. If you, instead of dividing the center where you might have two copies of the genome here. If instead you divide over here, then what your going to end up with is a very long cell with two copies of the genome. You're going to end up with this mini cell without any DNA.**

**And those mini cells, are they going to do well for the long term?**

**AUDIENCE:**

**No.**

**PROFESSOR: Right. They actually can survive for a little bi. And people have argued that maybe that could be useful for synthetic biology because they still make proteins, but they're not going to go take over the world because they don't have any DNA. But these are the so-called mini cells that happen if you have mutations in The min system.**

**Now, I think the three players are MinC, MinD, and MinE. So I think that MinA and MinB ended up not actually existing or something, in the sense that they identified the mutants, but then they were wrong about something. So the three that actually ended up being involved in the actual Min system are C, D and E.**

**So this MinC prevents formation of the z-ring. Now MinD and MinE are kind of the amazing guys. So this guy binds to the membrane and recruits MinC. Whereas**

24

**MinE-- what it does is it pulls MinD off the membrane. So it binds to MinD and ejects from the membrane.**

**And what has been seen by doing imaging in live E. coli cells with fluorescently labeled MinD and MinE is that there are remarkable oscillations from pole to pole. And indeed, that doesn't require MinC, so MinC is somehow following the others.**

**What happens is that MinD binds over here, then MinE binds and pushes it off. And then the MinD comes over here, and then MinE pulls it off, and it goes back and forth. The period is minutes, maybe. So it's a really remarkable thing that happens in vivo.**

**And the idea of what's happening is that if MinD comes here and then it comes here, on each of the edges, then it doesn't hang out in the middle. And that means that it's only in the middle where MinC can then bind-- oh, sorry. Because MinC is following MinD, then only in the middle can you form the z-ring, because that's where MinC is not. Right.**

**It's wonderful to do things in live cells because that's the native context and so forth. But I think that in some cases, it's also wonderful if you can take purified components and recapitulate interesting behaviors in vitro. Because then at least you know what is sufficient to generate a particular kind of dynamical behavior.**

**And because this system had been proposes as a model system for reaction diffusion mechanism to get this behavior. And so there's this paper by Martin Loose, in Petra Schwille's lab in-- where was it? In Dresden.**

**And what they did is they took a supported lipid bilayer-- so a membrane on glass-and then they added purified components of MinD and MinE that were fluorescently labeled. And then they saw amazing patterns, these amazing reaction diffusion waves traveling along.**

**Now on the first day of lecture, I actually showed you what some of those things look like. I didn't want to use up the projector again, but maybe I can pull up this movie because it is kind of fabulous. So maybe you can't see these things very well.**

25

**But this is a MinD and MinE and an overlay of the two, imaged on a two dimensional membrane.**

**And the movies are just amazing. When you see this, you think that it's a simulation. It's so incredible watching these things go. After class, you can come up, I can show you the paper, and you can look at the movie in more depth. But they're really amazing patterns, and it's patterns that you would predict from some sort of Turing type reaction diffusion mechanism.**

**So there are few things that are may be worth saying in this business. So these are fluorescently labeled MinD, MinE. They started out with MinD that was uniform. And then they added MinE, and over the time scale of about an hour they started seeing these sorts of patterns.**

**And as maybe you expected from the in vivo behavior, what you see are these things where MinD looks like this, whereas MinE looks like that. And then the wave travels here to the left. Because the MinE is ejecting the MinD from the membrane, causing this whole thing to move.**

**So this is a situation where you have both of these proteins in the liquid. All right, so in buffer, as well as on the membrane and they're coming on and off and so forth. And in this situation, it's wonderful because they can do all sorts of things like control the concentration of MinE, and see that the velocity of these waves changes as you change concentration in MinE.**

**So this is a really experimentally trackable system. And then you can ask what kind of model would lead to that sort of behavior? Such waves, do you think that it requires ATP? Just for fun, we can vote yes or no, it's all right. Ready three, two, one.**

**AUDIENCE: Yes.**

**PROFESSOR: Yeah. So indeed it does require ATP. And that's a general feature of these Turing type patterns is that there is a non-equilibrium structure formation.**

26

**Now one nice thing you can do in this sort of system is you can ask, well, what happens if I photo bleach a particular area? So I come in and I photo bleach. So now the profile looks like-- I locally deplete the fluorescence here.**

**Question is, will this move together with the traveling wave, or does it stay fixed? And in these mechanisms, do you think should this locally depleted area, should it move or should it stay where it is? Do you understand the question? Move, yes/no. Ready three, two, one.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: It actually doesn't move. Depleted area doesn't move. And this is just a reflection. These waves are not the result of individual molecules moving together with the wave. A wave like what you see in the ocean, or on a stream, or what not.**

**So the motion is a result of the individual molecules coming and going and communicating with each other, but it's not a reflection of actual molecules having directed motion. Because indeed, there's no mechanism in these models for directed motion. What you see is that in all these models, the only thing that is a function of position is diffusion terms. So it's all random diffusion, but then you get global motion.**

27

---

[← AUDIENCE: [INAUDIBLE].](05-audience-inaudible.md) · [Up: contents](index.md)
