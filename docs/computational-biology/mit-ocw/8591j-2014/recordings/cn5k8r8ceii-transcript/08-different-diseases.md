---
title: different diseases.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/cn5k8r8ceii-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# different diseases.

**Source:** `recordings/cn5k8r8ceii-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**And I think that's somehow easier to measure than many other things. Because you can try to do tracing of infections. So if you think about somebody that gets infected and moves to a new city or lands in a new city, you can try to figure out who they infected. So then, you can go and measure these R0 parameters.**

**And of course, the diseases that we worry about tend to have R0s larger than 1. And how large they are tells you about how difficult the vaccination will be in order to be successful and to remove the disease from the population.**

**So if you're curious, after class, you can come up. And there's a nice table that I have here for smallpox, measles, whooping cough, German measles, chickenpox, diphtheria, scarlet fever, mumps, and poliomielitis. Estimates of R0s-- and they kind of range 5 to 15, to give you a sense.**

**And so, if you want to remove the disease from the population, what is it that changes? --in terms of vaccination, in order to remove the disease. Yes?**

**AUDIENCE: In R0, then, the [INAUDIBLE] for u, as the population available [INAUDIBLE].**

**PROFESSOR: That's right. So by vaccinating you're removing susceptible individuals from the population and making them resistant somehow. And the R0 parameter tells you about what fraction of the population you have to vaccinate in order to remove the parasite from the population. And so, basically, you have to vaccinate a fraction, a percentage, p that's greater than 1 minus 1 over R0.**

**So as R0 gets very large, it means that you have to vaccinate, essentially, everybody. So if you have R0 of, say, five-- which is typical of many of these diseases-- it's saying you have to vaccinate 80% of the population. You can never get to 100%. And that's why it's very difficult to get rid of these diseases with large R0s.**

**And incidentally, they note that smallpox has an R0 of 3 to 5. And this always depends on the environment. But in the case where they measured, smallpox R0 is**

24

**3 to 5. And this is sort of small, as compared to many of these diseases.**

**And this is telling us that smallpox is easier to get rid of via vaccinations than many of these other diseases. And indeed, the vaccination procedures have been more successful in smallpox than the others.**

**AUDIENCE: Do you know what is 3, 4? PROFESSOR: I don't. But maybe in the next 20 minutes, somebody can Google this. We can estimate this right now, though. We've had, what? --five Ebola patients come to the United States. And we've gotten two or three infections. So I'll say, 3/5.**

**[LAUGHTER]**

**It obviously depends on the environment, right?**

**AUDIENCE: Yeah.**

**PROFESSOR: Yes.**

**AUDIENCE: I mean, I guess that was my question. You're not going to take someone with Ebola and throw them in New York City and just measure how many people they infect.**

**PROFESSOR: That's right.**

**AUDIENCE: So--**

**AUDIENCE: That would be [INAUDIBLE].**

**AUDIENCE: Like--**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah, but the thing is, you don't have to do anything that's so immoral. Because what you're interested in is the R0 for individual in an actual environment that they're actually going to be in. So this is a situation where the doctor comes back from Africa after working with Doctors Without Borders. In this day and age, he knows that he has to watch out for a fever, da-da-da. And then, if he gets a fever,**

25

**he calls in. And he's brought to the hospital.**

**And that's the world that we're interested in of what the R0 is. It's not the world in which there's fevers everywhere and nobody knows. So the R0 in the United States is going to be much lower than the R0 somewhere else. Yeah?**

**AUDIENCE: Is there enough of R0 for a disease that you don't transmit between people? You get malaria of the plague-PROFESSOR: Yeah, right. So I think that you could try to generate a similar kind of R0 for those to diseases. Although, it's going to be very muddled, in the case of where you have all the vectors and so forth. Because it's not even clear-- yeah, I'm hesitant to say too much. Because I don't know anything.**

**AUDIENCE: According to Wikipedia, it's like 1.5 to 2.5. PROFESSOR: For Ebola? AUDIENCE: Yeah.**

**PROFESSOR: Here? Or in--**

**AUDIENCE: It says the 2014 West Africa aggregate. PROFESSOR: Ah, so this is in West Africa then. AUDIENCE: Apparently.**

**PROFESSOR: Right. Yeah And it has obviously spread exponentially, which means it had to have been larger than 1. And I think it's important to remember that, just because you have a chart with a bunch of R0s, this is not set in stone. Public policy, hygiene, and everything changes this. And we'd like to drive it down. Was there a question in the back? AUDIENCE: I just was going to say about two.**

**PROFESSOR: Same thing, about two. OK, so that means that we could actually, in principle,**

26

**vaccinate against Ebola. We'd only have to get over 50% of the population vaccinated in West Africa. And then, we can maybe make it so it cannot spread and become an epidemic. Of course, we need to have a vaccine first.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: So I think I'm going to skip the discussion of SIR models. Because you are going to play with some of them in the context of your problem set. And if you just Google SIR, you can find it. And a very similar kind of intuition that you get from this model. Because I do want to spend the last 15 minutes, at least, talking about the evolution of sex. Because it is an interesting topic. And I think the paper is a nice discussion of it. So can somebody say why it is that this is a puzzle at all? Yeah?**

**AUDIENCE: In almost all the situations we imagine and things that can be [INAUDIBLE] introduce much faster, even violating the [INAUDIBLE]--**

**PROFESSOR: That's right.**

**AUDIENCE: --80% [INAUDIBLE] right?**

**PROFESSOR: So sex is costly, and in particular, if you have this obligate bi-parental sex. In particular, there's the so-called twofold cost of males. Because you can imagine comparing these two populations, one of which has both males and females. And one of them is just, maybe, reproducing asexually, or parthenogenetically, or hermaphroditically, or what not.**

**And so, if you have a male and a female, then on average, if they have two kids, you end up with another male and a female. And of course, this could be many different males and females. So you don't have to have any sibling anything. But if, every generation, each female is giving birth to two progeny, then you end up with a constant population size.**

**Whereas, if you started out in a population with just two females and they were reproducing hermaphroditically, then you end up with-- whatever-- more. 8. So you can see that you get a factor of 2 in the rate of exponential growth of the population.**

27

---

[← AUDIENCE](07-audience.md) · [Up: contents](index.md) · [Yeah? →](09-yeah.md)
