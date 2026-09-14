---
title: JEFF GORE
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/ct855rpx8bc-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# JEFF GORE

**Source:** `recordings/ct855rpx8bc-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Today, what we want to do is focus more explicitly on bacterial chemotaxis. Of course, a discussion that we had on Thursday about "Life at Low Reynolds Numbers" is certainly very relevant to this question of how bacteria are maybe able to find food or what constraints they're faced in trying to solve this problem. Today, we're going to discuss in more depth this idea of the biased random walk that runs and tumbles that we talked about on Thursday, that allow bacteria to swim towards attractants and away from repellents. But in particular, there's something that is rather subtle about the particular biased random walk that bacteria implement.**

**Now, the way that you might kind of naively imagine that this thing would work is that you would just have this tumbling frequency be a function of the concentration of the attractant, for example. And that indeed would allow you to swim or to execute a biased random walk towards, say, food sources, towards attractants, but it would not be effective over a very wide range of concentrations. However, if you experimentally ask, how well can bacteria swim towards attractants, it turns out they can respond over five orders of magnitude of concentration of these attractants, which is really quite incredible, if you think about the engineering challenge that these little one-micron cells are able to overcome.**

**And the basic way that they do this is they implement what's essentially equivalent to integral feedback in the context of engineering, where it turns out that the steadystate tumbling frequency, so the frequency of which they'd execute one of these tumbles that randomizes their motion, that displays what's known as perfect adaptation. It's not a function of the concentration of-- if you have a constant concentration of an attractant, then it's not a function of that. Of course, changes in concentrations it responds to, but somehow, E. coli and many other microorganisms are able to implement this very clever thing where the steady-state frequency of**

1

**tumbling, of changing direction, is somehow not a function of the overall attractant concentration.**

**Now, that's already an interesting, I think, phenomenon. And in some ways, you can think of it as some kind of robustness, because there is some way in which this tumbling frequency is robust against constant changes in the level of attractants. And it's that aspect, I think, that makes this example both rather subtle but also quite confusing, because it's the phenomenon of perfect adaptation that already has some aspects of robustness, but it's this phenomenon of perfect adaptation that is robust against changes in concentrations of proteins, for example, the concentration of the protein [? key ?] R that we're going to talk about.**

**So I think that this is in some ways maybe the prettiest example that we have of this principle of robustness, but I think it's also in some ways the most tricky to wrap your head around, because it's sort of robustness of a robustness in some ways.**

**All right. So our goal for today is going to be to make sure that we understand the challenge that E. coli are facing and then to try to understand the genetic circuit that they use in order to overcome this challenge. So what I'm going to do for the next hour and 15 minutes is we're going to leave this network up on the board so that any time that you're confused about what is R, B, Z, Y, so forth, you can kind of look up here and remind yourself what this thing is. But hopefully, the reading from last night will help you in following what's going on. There are a fair number of letters, I will admit it.**

**So first, I just want to make sure that we're all kind of remembering the basic phenomenon that we're trying to study, which is this idea of consecutive runs and tumbles. So this random walk is really composed of what you might call or what we do call runs, where the bacteria goes sort of straight and then tumbles, which they randomize their motion. So this is runs and tumbles, where bacteria, they go semistraight for of order a second-- order one second-- and this is the run. Then, they have this tumbling that might last about one second, so a 0.1 second tumble, over which the motion is sort of random in this axis of the orientation. And then, they kind**

2

**of go in a new direction and then tumble again and then new direction and so forth. So it's runs followed by tumbles.**

**Now, the thing that changes depending on whether the cells are sensing that they're moving up or down, say, an attractant gradient is the frequency of those tumbles, i.e. how long are the runs? I said that they're around one second, but this will vary depending upon whether bacteria sense that things are getting better or things are getting worse. Can somebody remind us how the bacteria actually execute one of these tumble motions? Yes?**

**AUDIENCE: They have this other motors-- they have mini-motors in their flagella and they usually all spin one way, which I think is counterclockwise. JEFF GORE: That's right. I always have trouble-- so the runs are indeed when these things are rotating counterclockwise. AUDIENCE: Yeah. And one of them can decide to switch and start turning clockwise. And what it does, it just sort of-- I don't know. I just imagine it throws the whole motor off.**

**JEFF GORE: Exactly. And the flagella in the context of-- so we have our E. coli. The velocity is of order, say, 30 microns per second. Now, they have these flagella that are actually distributed-- the motors are actually distributed across the entire cell. So it's not just on the back. But then, these individual filaments kind of come together towards the back and then they have this corkscrew shape.**

**When these things are all rotating in the counterclockwise direction, that corresponds to a run, when there's directed motion. But then if one of them goes clockwise, the bundle falls apart. And indeed, there are some very nice movies online where you can see that when they're going clockwise, you see that the flagella are kind of doing crazy things and that causes this thing to kind of tumble in a random orientation. So it randomizes its direction.**

**Now, one thing that we did not talk about in the context of this low Reynolds number motion was the question of how hard you would have to pull in order to get a cell to go 30 microns per second. Now, remember, we're in the low Reynolds number**

3

**regime, where the force you have to apply is in general proportional to this velocity. And this thing is very much not a sphere, but if it were a sphere, for a sphere, the proportionality constant is this 6 pi eta av, where a here is again the radius.**

**Now, regardless of the precise shape, you'll always get for the low Reynolds regime something that looks vaguely like this, where this is going to the longest linear dimension and this here depends on the precise geometry of the object. And so just-- it's useful to try to get a sense of order of magnitude. How large are these forces that we're talking about? In particular, how hard would you have to pull a cell in order to get it to go 30 microns per second?**

**Now, of course then, there's a question. What's roughly the scale that we should be thinking about? Right now, a newton is the scale that's for macroscopic objects. So you'd say, OK, probably not going to be up that large. Then, on the other scale, we can think about the forces that can be applied or exerted by individual molecular motors. Has anybody studied this at all?**

---

[Up: contents](index.md) · [AUDIENCE: [INAUDIBLE] →](02-audience-inaudible.md)
