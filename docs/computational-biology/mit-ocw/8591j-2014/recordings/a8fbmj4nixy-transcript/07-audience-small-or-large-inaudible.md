---
title: 'AUDIENCE: Small or large [INAUDIBLE]?'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/a8fbmj4nixy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: Small or large [INAUDIBLE]?

**Source:** `recordings/a8fbmj4nixy-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: To be on the safe or conservative side, we want to take this to be as big as possible. So we take S actually as big as we can, right? It's in the log. So details, right?**

**But we can see we have 10 to the minus 6, 10 to the 3, and then this is the log of maybe 100, which is, like, 4 or 5. Is it closer to 4 or 5? I don't know, but it doesn't matter. We'll say 5. This is indeed much less than 1.**

**So indeed, we don't have to worry about clonal interference. This is a wonderful simplification. What it's saying is that the population is dividing. Every now and then, a mutation occurs in the population.**

**It could be either the 0, 1 or the 1, 0. But in either case, the fate of that mutation is**

9

**resolved before the next mutation occurs. So you don't need to worry about them competing in the population.**

**Instead, just at some constant rate they're appearing. And given that they appear, there's some probability that they're going to fix. So that leads to effective rates going to each of those two steps-- going to 0, 1 or 1, 0.**

**And in particular, this is like a chemical reaction, where we have some chemical state here. We have two rates. There's the k going to 0, 1, the k going to 1, 0.**

**And what we know is we know the ratio of those rates. And that's everything we need to know to calculate the relative probabilities of taking those states, because the probability of going through to 0, 1-- we want to go that direction-- 0, 1, this is going to be given by k 0, 1 divided by k 0, 1 plus k 1, 0.**

**So this is how we get 1/6 instead of 1/5. Because this thing is 1/5 of that. So it's like 1, and then 1, 5.**

**So this is actually, in principle, not quite answering the question that I asked, because this is talking about the relative probability of the first state, the first mutant to fix. In principle, it is possible that from there, there's some rate of coming back. Or they might not necessarily move forward on up that hill.**

**Do you guys understand what I'm talking about? Because it goes from here to there. Because we really want to know about this next step, going to the 1, 1 state.**

**But in this case do we have to worry about going backwards? No. And why not?**

**It's very unlikely. And in particular, you could think now that you're here you can talk about the rate of going to the 1, 1 state as compared to the rate of going to 0, 1. And those are going to be exponentially different.**

**Because just as this was a non-neutral beneficial mutation, that means that going from 0, 1 back is going to be a non-neutral deleterious mutation. So the probability of fixing it in the back direction is not 0, but it's exponentially suppressed. I think it's very important to understand all the different pieces of this kind of puzzle, because it**

10

**incorporates many different ideas that we've talked about over the last few weeks. If there are questions, please ask now. Yes.**

- **AUDIENCE: What about the [INAUDIBLE]? [INAUDIBLE] 0, 0 to 1, 0 to 1, 1? Then it seems like the benefit of 1, 0 versus [INAUDIBLE].**

- **PROFESSOR: All right, so you're wondering about-- so the fitness of the 1, 1 state was 1.2. So you're pointing out that it's actually easier to go from the 0, 1 state to the 1, 1 as compared to the 1, 0 to the 1, 1.**

- **AUDIENCE: Right, which seems like a reason for why we wouldn't care about [INAUDIBLE].**

- **PROFESSOR: Yeah, OK, right. So if anything, in some ways, this actually provides a bias going towards the 0, 1 state, because it's saying that if we do get to 0, 1, it's actually easier to move forward as compared to this other path. In practice, it doesn't actually matter, because this acts as a ratchet.**

   - **Because all these mutations are non-neutral, once you fix this state or this one, you can't go back. So the population will move forward once it gets to one of those two states. Now I mean, it would be a very interesting question to ask if we instead did a different arrangement. What would the rate of evolution be, and so forth?**

**Yeah, but what you're saying is certainly true, that if this took up all of the benefit going here, then it may not actually be somehow an optimal path in terms of the rate of evolution or something like that. I'll think about that when designing. Problems.**

- **AUDIENCE: In this system, 0, 0 eventually becomes 1, 1.**

**PROFESSOR: That's right.**

- **AUDIENCE: So the probability is 1.**

- **PROFESSOR: That's right, so we are guaranteed that we will eventually evolve to this peak in the fitness landscape. And so what we're asking here is which of these two paths is going to be taken.**

11

**AUDIENCE: Yeah, so how to mathematically prove that the system will go from 0, 0 to 1, 1? PROFESSOR: I mean, I feel like I kind of proved it, although I understand that nothing I said was rigorous. And of course, there are non-zero probabilities of going backwards. It's just that they are reduced.**

**And actually, you can prove, for those of you who are interested in such things, that over long time scales, there's going to be an equilibrium that distribution over all these states, where the probability of being in a particular state will-- it goes as the fitness. It scales as the relative fitness to the Nth power. So we talk about these fitness landscapes as energy landscapes. And indeed, in this regime where you have small mutation rates, then it's going to be a detailed balance. And it's actually a thermodynamic system. So then in that case, you can make a correspondence between everything that we normally talk about, where fitness is like energy and population size is like temperature. So the relative amplitude of being in this peak as compared to the other states is going to be, in this case, the ratios of those things is, indeed, described by the ratios of the fitnesses. And it's going to go as kind of like 1.1 to the 1,000th power, which is big. Which means that the population has really cohered at this peak in the finished landscape. Yeah.**

**AUDIENCE: So if you want to calculate a problem going from 0, 1 to 0, 0, then [INAUDIBLE] that would just be-- I guess I'm not sure.**

**PROFESSOR: OK, you want to know the rate that that's going to happen.**

**AUDIENCE: Yeah.**

**PROFESSOR: No, that's fine. Let's do that. So for example, let's imagine that we don't have-- so let's imagine that we just have the 0, 0 and the 0, 1 states, just so we don't have to worry about going up the landscape. And so what we have is we have r is relative fitness 1 and 1.02.**

12

**Now what we want to do is we want to ask, well, what is the rate of going back and forth? Well, so the rate of going forward, well, we sample mutations at a rate mu. And this is mu only for this one state, because pretend that we're not going to mutate this other one. So rate mu N, you have mutations appearing. And times this s, 0.02, is the probability that it'll actually fix in the forward direction.**

**And now what we want to know is the rate of coming back. Well, the beginning part's the same, because we have mu N is the rate that you get this deleterious mutant in the population. But then we need to multiply it by the probability of fixation.**

**And the probability of fixation is-- there was this thing X1, which was 1 minus-- now this is r, but it's r in the other direction, so be careful. Because the general equation was 1 over. But now r, instead of being 1.02, is 1/1.02.**

**So which of these terms is going to be dominant? This thing gets up to be some really big number is our problem. So we should be able to figure this out, though. Because this new r is 1/1.02. So we for example, have 1 minus 1.02, 1 minus 1.02 to the 1,000. All right, so this is a negative number, but this is a negative number, too. So we end up with 0.02--**

**AUDIENCE: 200.**

**PROFESSOR: Is it 200? Yeah, you're keeping only the first, which, since it's much larger than 1, it's bigger than 200. Right? I mean do you guys understand what I'm saying? You can't keep just the first term in a series. If the terms grow with number.**

**AUDIENCE: [INAUDIBLE] squared, 3.98 or something.**

**PROFESSOR: Wait, which one?**

**AUDIENCE: 1.02 to the 1,000.**

**PROFESSOR: It's 4? OK, all right. OK, so it's 1 minus 4. So it's 2/300. OK, so this is teamwork, right?**

13

**OK, so there's less than a 1% probability of it fixing. Is this believable?**

**AUDIENCE: It's about right. PROFESSOR: 2, 1,000, 50-- I think that you did it 1.02 to the 100 rather than 1.02 to the 1,000. AUDIENCE: OK. PROFESSOR: No? Do you not have it in front of you? AUDIENCE: No, it's 3-- [INAUDIBLE]. AUDIENCE: 4 times 10 to the 8. AUDIENCE: I never thought that my calculator would become so controversial. AUDIENCE: Oh, 4 times 10 to the 8. PROFESSOR: Yes, sorry, I was just saying this doesn't-- so this is why I'm saying you always check to make sure that your calculation makes any sense at all. So it's not this. But it's tiny, right? AUDIENCE: Yes, [INAUDIBLE]. PROFESSOR: Yeah, because this didn't make sense, because this was of the same order as-well, this would be larger than 1 over N, so it's totally nonsensical. Because 1 over N would be the probability of fixation of a neutral mutation. This is a deleterious mutation. It's not even nearly neutral. So it has to be much less than 1 over N, right? So this whole thing is 10 to the minus 10, or something like that? OK, 4 times 10 to the minus 8. Well, OK, whatever. It's 10 to the minus 9. It's something small. So this times the probability of fixation, which is 10 minus 9-- this is how you would calculate the rate of going backwards. There's some rate that the mutation appears, and you multiply by the probability that it would fix. And it's tiny. OK? All right, any other questions about how to think about these sorts of evolutionary dynamics with**

14

**presence of mutation, fixation, everything? Yeah. AUDIENCE: Can we handle a situation where [INAUDIBLE] interference is important at this point? PROFESSOR: Yeah, so this is what you do in your problem set with simulations. Yeah. AUDIENCE: [INAUDIBLE] numerical. PROFESSOR: You know, I think that it gets really messy with clonal interference, I'll say. AUDIENCE: But, like, with basic-- I guess I was thinking about it and you could probably imagine that [INAUDIBLE] calculate the probability that 1, 0 doesn't arise first. PROFESSOR: Right, yeah, OK, this is an important statement. In the limit, as you get more and more mutations, when clonal interference is really significant, then you're pretty much just guaranteed to take the 1, 0 path. Because if you have many mutants, the definition of clonal interference is you have multiple mutations that have established. And once you have multiple mutations that have established, then it's likely that one of them is going to be this.**

**And if it's established, it's going to win. But the other thing is that as you go up in the mutation rate, you don't even do successive fixations. So it may be that neither state ever actually fixes, because it could be that the 1, 0 state is growing exponentially, but is a minority of the population. And it gets another mutation that allows it to go to 1, 1.**

**So as you increase the mutation rate, you don't have to actually take single steps. You can kind of move through states. And there's a whole literature of the rate at which you cross fitness valleys. So this is like tunneling in quantum mechanics or so.**

**And it has a lot of the same behaviors, in the sense of exponential suppression of probabilities as a function of the depth and the width of the valley you're trying to traverse. And there's some very nice papers, if you're interested in looking at this stuff. And one of them is actually in the syllabus that I mentioned. I'm trying to remember who. It was Journal of Theoretical Biology, but I put it on as optional**

15

**reading for those of you who are interested.**

**All right, OK. So what I want to do now is I want to switch gears, so we can think about this evolutionary game theory business. And I think the most important thing to stress when thinking about evolutionary game theory is just that this point that we don't need to assume anything about rationality. Because the puzzles that we like to give each other in your dorm rooms Friday night, you give these logic puzzles to each other. Is that-- I don't know.**

---

[← AUDIENCE](06-audience.md) · [Up: contents](index.md) · [[LAUGHTER] →](08-laughter.md)
