---
title: Introduction
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/klrpm-beeoi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/klrpm-beeoi-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=KLrPm-BEEOI**

**The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: All right, why don't we go ahead and get started. So today what we want to do is start thinking a bit about evolution in finite populations. And of course, what we mean by that, is evolution in populations where we have to really think about stochastic dynamics.**

**And now in general, just like in the context of gene networks within cells, the situation where we have to worry about stochastic dynamics is in the small number kind of limit. What's perhaps surprising about evolution is that they're always-- the small numbers are always important. Even if you're in a large population, I'd say 10 to the 9 individuals, if you want to study evolution, then you're interested in cases where new mutants will arise in the population.**

**And kind of by definition, those new mutants start out as kind of a single member of the population. Which means that in the context of evolution, we always have to think about stochastic type dynamics.**

**Now the basic model that we're going to use in this class is the Moran process, which is a model that fixes population size. And then instead of having discrete generations, where all the individuals are reproducing at the same time-- which is what you might have seen in the Wright-Fisher process-- instead, we're going to think about the situation where it occurs more stepwise. In the sense that individuals reproduce one at a time. And then we contract the dynamics of the population.**

**So we're going to think about both the situation where we're trying to understand neutral dynamics, when we're tracking the composition of a population when the fitness of individuals is equal or nearly equal. But because in stochastic dynamics, there are interesting things that happen. But then we'll get into the question of non-**

1

**neutral evolution. And really, we want to consider both halves of that.**

**All right, so in many cases, in the context of evolution, we're interested in, or focused on beneficial mutants. Now for those beneficial mutants, one of the basic things we're going to find is that even beneficial mutants will typically go extinct. It doesn't mean that they're not important over the long run. But it does mean that there is a very real sense that randomness is dominating the life of even beneficial mutants.**

**And then finally, if there's time, we will discuss this idea of Muller's ratchet, which is basically pointing out that if there are deleterious mutants or mutations in the population, those deleterious mutations can in some cases spread and fix in the population. And when that happens, you can have a decrease in the fitness of a population over time. And this is particularly a strong effect for small populations, because small populations, they're not as effective, what you might call filters, for selection.**

**And so what we want to do is start by thinking about this Moran process. And the key feature here is that we're going to have a constant population size, constant N. And that's not because we believe that real populations always have a fixed population size, but rather, we want to try to get some intuition in this simple model.**

**And then of course, it's reasonable to ask, well, which aspects of the mathematics or intuition we develop are going to change as a result of allowing fluctuations in the total population size? But I think there's a lot of value in starting out by analyzing the simplest model that you can.**

**So what we're going to think about is a situation where we have a population composed of N individuals. And for now we'll just consider two types, A and B. And this is going to be a model for asexually reproducing populations. Constant N, asexual. What that means is, in particular, that we're going to assume that an A individual can lead to two individuals. Similarity, a B individual can lead to two B individuals.**

2

**Right, so you can think about this as, for example, a model for how microbial populations may evolve. And for now, we will not consider any mutations. All right, so we're going to think about the process of assume that those mutations are already there. So A and B could be different. They could have, for example, different-- they could be different at some point mutation side of some gene that is relevant for growing a low glucose concentration, for example. OK?**

**So here we're going to-- so this is birth slash division, and in particular here we're going to, for now, assume no mutation. So we'll assume that A's always give birth to A's, and B's always give birth to B's.**

**We'll follow the nomenclature from the reading that you guys did last night, Martin Nowak's book, chapter six, where we're going to think about-- we're going to assume that there are initially i A individuals, and therefore, N minus i B individuals. Now we'll assume that the basic process for the-- in this Moran process is that you have reproduction, or birth, that's proportional to fitness.**

**And then the resulting kind of what you might call a daughter cell replaces one member of the population at random. So there's birth and then replacement. And indeed we'll assume that replacement, that the daughter cell, for example, could even replace the mother cell, if we want. So this is just the birth. So A is going to lead-- there's going to be two As, and this new A will have to replace one of the other individuals in the population, to keep constant population size.**

**All right. Are there any questions about the basic model? OK. So that, in principle, here we can use this model to try to understand both neutral and non-neutral evolution. But let's start out by thinking about the neutral case.**

**So in particular, the fitness, rA is equal to rB. Now what I want to do is, given the rules we just kind of laid out for you, let's assume that i over n is equal to one third. So for now, we'll say, OK a third of the population is A, 2/3 is then B.**

**And we can think about these probabilities of going from i to i plus 1, as compared to going from i to i minus 1. So these are the probabilities that in one cycle of birth**

3

**replacement, the number of A's goes up one or goes down one. Can you ever go up two or three or four in the Moran process in one step? No. Because each step is always one birth and one replacement.**

**So you can move, at most, one. Do you always move-- does i change always? No. And what we want to know is the probability of going from i to i plus 1, as compared to the probability of going from i to i minus one. The ratio of these probabilities is equal to what?**

**We're considering a case where the A's and B's have the same fitness, so they're somehow equal per capita probability of being chosen to reproduce. But there's-but we're not in a symmetric population distribution, right? So 1/3 of the population is A, 2/3 is B. So I'll give you 20 seconds to think about this.**

**All right, do you need more time? Everybody nod or shake. Do you need more time? OK. I'll give you another 10 seconds, because it's--**

**Let's go ahead and see where we are. Ready? Three, two, one. All right. We have a wide range of different answers here. OK, perfect. This is exactly the situation that we hope for. So turn to your neighbor. You should certainly be able to find somebody that disagrees with you. So if the first person you turn to agrees with you, try to find somebody else talk to.**

**All right, why don't we go ahead and reconvene. I know that there was quite a lot of disagreement, so that means that you guys will probably not be able to converge in this one minute time frame. But let me just see, let me see if anybody's mind was changed by their neighbors.**

**All right, let's re-vote. Ready, three, two, one. OK, all right, so it's pretty much the same as where we started, maybe. All right. OK I would say-- does anybody want to volunteer what their neighbor said? I know what your neighbors said. So tell us.**

**AUDIENCE:**

**OK, so if you-- so I would say it's E. And the reason is that-- so there are two cases. In the first case, both the number A and B stay the same. Right, for example, A gets born and A dies. So you first decide, is the pop-- is the number of A and B going to**

4

**change, or is it not going to change?**

**PROFESSOR: OK.**

**AUDIENCE: Once you've decided that it's not going to change-- I'm sorry. Once you've decided that it is going to change--**

**PROFESSOR: Right.**

**AUDIENCE: --then you just want to know, OK, then what's the probability that you just choose A to change [INAUDIBLE].**

**PROFESSOR: OK. Yeah.**

**AUDIENCE: And then the probability that A-- you choose--**

**PROFESSOR: OK. But you haven't said anything about replacement yet. So I'm-- replacement should be-- because certainly, we're talking about the ratio of the probability that the number of A goes up, as compared to the probability that the number of A goes down. Right? So we've already, in some ways, excluded the cases where the number of A individuals doesn't change.**

**And in your-- what you just told us, you're asking about the probability that individuals are going to be chosen to reproduce.**

**AUDIENCE: Yeah, because [INAUDIBLE].**

**PROFESSOR: OK. Yeah, but I guess all I'm saying is that there're going to be two halves to this, right? So you have to think about the probability that an individual is being chosen to reproduce, and also the probability that a particular type of individual will be chosen to get replaced. So it's the-- there's somehow a balance of those two.**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: Right, because in this case--**

**AUDIENCE: [INAUDIBLE] replace--**

5

- **PROFESSOR: --replace, this is-- right, death, slash-- right. And I should maybe just highlight-- if you want, you could call-- replacement-- I mean, this is just a nice way of saying death, right? Death--**

- **AUDIENCE: Yeah, you can. I mean, [? the point ?] [? is ?] once you've ruled out-- once you say, OK, the populations are going to change, then if you choose an A to reproduce, a B has to die.**

**PROFESSOR: Oh, OK, once you've already-AUDIENCE: If an A is chosen to reproduce, and an A is chosen to die, then--**

- **PROFESSOR: OK, yeah, right. But, OK, I think I understand what you're saying. But we-- you still have to keep track of there are the two sides. There's the replace-- there's the birth, and the replacements. And we have to figure out how the relative probabilities or rates that those two things happen.**

**Does somebody want to make an argument for something else? I mean, we'll see how this plays out in a moment.**

**AUDIENCE: I want to argue for C. PROFESSOR: OK.**

**AUDIENCE: So take the numerator.**

**PROFESSOR: Yeah.**

**AUDIENCE: In order to go from i to i plus 1-- so we're going to take two individuals from the population. We need one of them to be type A, that's the one that's going to reproduce.**

**PROFESSOR: Yep.**

**AUDIENCE: And the other to be type B, the one that's going to die.**

**PROFESSOR: Yeah.**

6

- **AUDIENCE: So we get the product of those-PROFESSOR: Perfect. OK. And we can actually just be more-- be explicit about this. OK, so the probability-- in one cycle, the probability that you go from i to i plus one. That requires that two things happen. One is that you choose an A individual to reproduce. And what's the probability that you choose an A individual to reproduce?**

- **AUDIENCE: It's going to be i over N. PROFESSOR: i over N. So we have i over N. Right, so this the probability that A reproduces. And then for i to go from-- to increase by one, requires not only that an A individual is chosen to reproduce, but that a B individual is chosen for replacement, or death. And what's the probability that that's going to happen?**

- **AUDIENCE: That's N minus i all over N.**

- **PROFESSOR: N minus i, all over N. OK. So this is the probability that in one cycle you're going to go from i to i plus 1. Now of course it's not-- we haven't said what the probability of staying in i is, but this is the probability that i will increase by one. Do we agree?**

**And indeed, where is it that we've assumed-- where is it that we've assumed neutrality in this calculation? That A and B have equal fitness? Yep?**

**AUDIENCE: Just take the probability of reproducing to be about-- or, the-PROFESSOR: That's right. That's right. So indeed, we've-- this probability that A reproduces, we've assumed that it's just simply i over N. Whereas, if it were non-neutral we'd have to write something else. Maybe we'll figure out what that's going to be in a moment. But it's in here that we've assumed that.**

**Incidentally, you could write down a reasonable model similar to the Moran process, where differences in fitness show up instead of here, in the probability of reproduction, you can have it as a difference in probability of death, or being replaced. But this is the most maybe intuitive way of thinking about it.**

**And this is very similar to, for example, what happens in a, what you might call, a**

7

**y , p , pp , y g ,**

**turbidostat, where you keep constant population size. And as the cells divide other cells are randomly sucked out. So I'd say that this Moran process is really a theoretical kind of implementation of what you could do experimentally, is this turbidostat. Which is like a chemostat, instead of keeping constant dilution rate, you fix population size. Yes.**

**AUDIENCE: So do we care about the step of, OK, first A reproduces. Then, from the pool of new individuals-- because you're going to have N plus 1, so--**

**PROFESSOR: OK, so all right. I think maybe I wasn't totally clear on this. OK so, you have N individuals here. What you're going to do is you're going to choose one of them randomly, maybe proportional to fitness for reproduction. And then, but then, from this original N, you choose one of them for death.**

**So it's not-- you're not, yes. It's not-- so the daughter cell is not allowed to--**

**AUDIENCE: Die.**

**PROFESSOR: Right. The daughter cell always replaces somebody, but it could've been the mother cell. If we're thinking about this in the context of cells. So we haven't yet figured out which answer is which, right? But we can go ahead. OK, this is the probability that A reproduces, and over here, this is the probability that a B individual is replaced. Right?**

**What we can do is, we can ask, well what's the probability that we go from i to i minus 1? Well it's the exact kind of same calculation, except now what we want to know is, we want to know the probability that a B is chosen for reproduction. And what is that going to be? Somebody? N minus i, right, the number of B individuals divided by the total number of individuals.**

**So this is the probability that a B reproduces. And then what's the probability that A-that an A type individual will be chosen for replacement or death? That's just i over N. The number of A individuals divided by the total population size.**

**All right, does everybody agree with the two calculations that we just did? Let's re-**

8

**vote. All right, ready, three, two, one. All right, see, you know, if we do the calculation, we can convince you. So indeed, these are equal, these two probabilities.**

**Right, and this is funny. Because on the one hand it's like blindingly obvious, but then the other hand, you get yourself all tied up in knots thinking about it. So I don't understand why or how those two statements can be true at the same time, but they are. So this is indeed a random walk in i space, number of A individuals.**

**And it sort of has to be, because these things are neutral. The fact that i over N is not equal to a half doesn't matter, because these two terms kind of cancel. But indeed, all of the things that you know have to be true based on the fact that A and B have equal fitness, they're going to not work if this thing were not equal to 1, if these two probabilities were not equal.**

**So any of these other answers would lead to things that you would clearly agree are going to be nonsensical, if you think through the consequence of this. And we're going to do one right now. All right, let's imagine that we start-- so here's the number of A individuals, i. I apologize that that's the nomenclature we have for a number of A individuals, but we want to be consistent with Martin's book.**

**Now let's say this is N and let's say we start out at some i here. The question is, what's the probability that B fixes? I want to make sure I write down some reasonable options.**

**So what we want to know is the probability that B fixes, and that means that it takes over eventually. That B, we'll say eventually. In the Moran process with neutral dynamics.**

**AUDIENCE: I's the number of A, right?**

**PROFESSOR: That's right. i is the number of A individuals. I'm going to give you seven more seconds. All right, ready, three, two, one.**

**All right, so we have-- it's kind of mostly split between C's and D's. Although I'd say**

9

**a majority of the group is going to say-- is saying that it's going to be D. All right, can-- all right, and this is the distinction between the probability that B fixes and that A fixes.**

**I'm not trying to be super tricky, but I just want to make sure that you keep track of A's and B's. And in particular, as i increases, the probability that A fixes should go up or down? Verbally, three, two, one.**

**AUDIENCE: Up. PROFESSOR: Up. This here-- over here is a bunch of A's, here is a bunch of B's. So if you have a larger here, than you should be more likely to fix the A individuals, vice versa. So in particular, this-- the probability that B eventually fixes is going to be this, whereas the probability that A will fix eventually is just going to be 1 minus that, it's i over N.**

**So this is indeed what was pointed out in the book. All right, and can somebody give an argument, verbally, for why the-- I mean, this is a result, that if you think about in the right way, you can just verbally say why it has to be this. Rather than writing down all the equations that-- so why is it that the probability that A will eventually fix has to be equal to i over N? Yeah.**

**AUDIENCE: [INAUDIBLE] book.**

**PROFESSOR: Yeah, perfect.**

**AUDIENCE: So at this given time, there are N individuals--**

**PROFESSOR: Yep. And there will always be N individuals, because we're keeping it-AUDIENCE: OK, yeah, right. Their descendents, at some point, the descendents of one of them is going to take over the whole population. That's a given. PROFESSOR: That's right. And that's fine. It's at first glance kind of surprising but, it's just the nature of-- if you imagine that they all were individually tagged, right, so it wasn't just that we had two types, A and B. But if they were all color coded using rainbow colors, then you could keep track of them. And one of the individuals will eventually**

10

---

[Up: contents](index.md) · [fix. Now, OK, and then what's next? →](02-fix-now-ok-and-then-what-s-next.md)
