---
title: chemical warfare bacteria.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/lc3xswq62iw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# chemical warfare bacteria.

**Source:** `recordings/lc3xswq62iw-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**And this subject does come in a bit into this question of spatial structure, and how spatial structure may help facilitate the stability of populations. So there's this idea of that non-transitive interactions, whether you have Rock, Paper, Scissor type interactions, may facilitate coexistence of either genotypes or species. But in some of these studies, there's an argument that sometimes this non-transitive interaction may not be enough, but then in the presence of spatial structure, maybe it does help. On Thursday, the primary topic of the class will be trying to understand the dynamics of populations when their spatially extended. So this will transition naturally into the subject on Thursday.**

**Are there any questions about where we are here? Or administrative type issues?**

**All right, so I just want to make sure that we're first, all on the same page. We talk about logistic growth. So we can think about-- Well, what are the simplest ways that we might consider the population dynamics of just a single population. Well, the logistic growth is maybe the simplest model you might write down, where the population is at least bounded. And I might even-- Maybe I'll even just first draw exponential growth, just so that we can--**

**The very simplest thing you might do is you might just say that N dot might be equal to some r times n. In this case, if we plotted gamma, the per capita rate of population growth, this is just some line at r. In this case, the population grows exponentially. And that that means that if you plot say the number as a function of time, well it doesn't matter where you start, you always go to infinity. Right?**

**Now we can compare this to the logistic growth case, where we just assume that at low density, indeed, we grow exponentially at this rate r, but then we have a linear decrease in this per capita rate of growth as a function of density. So we might write this as something that looks like this. In which case, if we write this per capita growth rate of the population, as a function of population size, it starts out at r, but then it goes to 0. And indeed you, might even if you'd like, you could say that it goes down to a negative value. So in that case, you could start at a population size above the**

2

**carrying capacity k, and you still come back down it.**

**One of things that we want to make sure we understand is what the bifurcation structure of these equations is going to look like. In particular, we can think about what happens if we add some sort of death rate to the population. Right now, in this case, a death rate corresponds to is something-- OK, we're looking at the bifurcation diagram. What we're going to do is we're going to think about what happens if you look at the size of the population. In the bifurcation diagram, what we typically do is we look at the fixed points. The fixed points in n, as a function of some external parameter. And here, we might just think about delta here which is just some death rate. The simplest way to include this here would be to have a minus delta n.**

**So the idea is that there's this population. It grows exponentially at small sizes. As the population size grows, it might run out of nutrients or so, and that limits its overall population size. Then, we can add another term here which is corresponding to something about the quality of the environment. So this could be the amount of hunting that is taking place, or it could be a reflection of pollutants in the environment or so. And what we want to do is try to make sure we understand how the size of the population will respond to some death rate.**

**Well maybe we'll go ahead and do a verbal vote. So in the review that you guys read, this was talking about in these early warning indicators in the context of sudden transitions and populations. So this was saying that whether you're looking at a population, or an ecosystem, or maybe even other complex system, such as climate regime shifts, epileptic seizures, and so forth, the authors were arguing that in response to a slowly changing environmental knob, the system can experience a sudden transition in the state.**

**Now, the question is here. And the sudden transitions that they were describing, those were fold bifurcations, or saddle-node bifurcations. Where there's a sudden transition in say, the equilibrium. Size of the population is a function of some external knob describing the quality of the environment.**

3

**So the question is whether this population experiences such a full bifurcation at least to a sudden transition. Do understand the question? I'll say fold bifurcation. I'll let you guys vote, just so you can use your cards. And this is a full bifurcation as a function of this delta, which is death rate.**

**Ready? Three, two, one. We have a majority now that are saying the answer is no, this does not actually have a fold bifurcation.**

**And the reason for that is that we can find the-- In the absence of a death rate, what is the equilibrium population size? k, right? Indeed, what's going to happen is that as we add this death rate, we can just figure out, OK well, the fixed points occur when N dots equal to zero. All of these things. There's an n here, we can divide by that. Well we could just do it, just so that we're all on the same page. So the fixed point.**

**What we want to do is set N dot equal to zero. That tells us that n times r1 minus n over k minus delta is equal to 0. OK. How many fixed points are there going to be in the system? Two. Right, so indeed, this is N dot. So n equal to zero is going to be one fixed point, but the other one is going to be when this thing is equal to zero. And so then we end up with 1 minus n over k, is going to be equal to some delta over r.**

**So we can see that this stable fixed point is going to decrease linearly with this death rate delta. And it's just going to go smoothly to zero. That's this key feature of this bifurcation digraph. So what happens is that we come down like this, and indeed, we could even continue this and the bifurcation occurs here. We want to draw-- This corresponds to a stable fixed point. And a dashed line is unstable. In this case, this is the stable and this is the unstable.**

**So this thing here is what's known as a trans-critical bifurcation. And it's a bifurcation because the fixed points do something. In this case, they exchange stability. So what happens is that this thing becomes unstable, whereas the fixed point at n equals 0 becomes a stable fixed point.**

**So there's no tipping point or sudden transition in this logistic growth as you change**

4

**the death rate. All right, you can think of it as a situation here where the death rate just kind of starts pulling this thing down. And this bifurcation occurs when you pull it down-- when delta is equal to r.**

**And what this means is that if you plot say, the number as a function of time, for low delta, in particular, for delta equal to zero then this is your-- You come to this equilibrium k. Where as delta increases, eventually you just get to a situation where all of, regardless of where you start, you go extinct.**

**Now, in many cases, we don't draw what happens down here because n being less than 0 is not a physical thing. But it's useful to think about it mathematically, because that's what tells you that that was the bifurcation. Are there any questions about where we are here?**

**One thing that's valuable in the case of-- well, in general-- is to switch between the algebraic characterization of the dynamics a system and the graphical dynamics, because you end up seeing different things depending on how you do it.**

**For the case of the Allee effect, we're just going to look at it and analyze it graphically, just because the equation is a little bit cumbersome, and I think don't provide very much intuition. What you can see is that for the logistic growth, other individuals in the population always decrease your happiness as an individual. So if you imagine that you are some member of this population, and having more members the population there is always kind of bad for you, because it decreases your growth rate. And to think about the happiness of an individual, what you typically want to do is divide by n, because you're thinking about the per capita growth rate. So that's telling you about the ability hat you will have to reproduce. So what you did we do is just divide by n.**

**What you can see is that per capita division, gamma, is a monotonically decreasing function of the population size. This is saying that more individuals in the population just take up space, resources, mate, something. And so you as an individual never benefit from the presence of other individuals.**

5

**Whereas, when you have the Allee effect, what that's saying is that over some range of population size or densities, there is a positive effect of other individuals in the population. This is saying that if we plot gamma, in particular, the derivative of gamma with respect to n is greater than 0 for some n. This is just saying that if we plot this per capita division rate as a function of the size of the population, there's some region in which this thing has positive slope.**

**And often, people distinguish between the so-called strong Allee effect and the weak Allee effect. The strong Allee effect corresponds to the situation where at n equal to zero, you start out with negative per capita growth rates. So this is just some generic curve here, that describes the Allee effect. The important thing is that it's coming up here at low n.**

**And what this tells us is that we will have some sort of different dynamics where this is going to be the stable size of the population here. But there's also a minimal size required for survival. So if you start out below this n, then you come down. If you want you want, you could call it some-- This could be some k, and this could be n- min.**

**This is saying if we plot n as a function of time starting with different sizes of the population, then indeed, this thing is a stable state. But the key thing is that there's this other minimal size required for survival. So if you start out around here, then just above it you come up, but just below it, you come down.**

**What do you say? What you see is that this population that experiences the strong Allee effect has bistable fates. So it's bistable. This is bistable depending on the starting size n of the population.**

**Now, can somebody suggest possible explanations for why there might an Allee effect?**

**AUDIENCE: Sexual reproduction?**

**PROFESSOR: Sexual reproduction. And can you explain that a little bit more?**

6

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: That's right. And basically, just the need to find mates. So this implies that at some density, sexual reproducing species are expected to have this Allee effect. It doesn't mean that the Allee fact is super strong at moderate sizes, right? I think that this statement is true, but it might lead us to conclude that these extreme dynamics that we're talking about here are relevant for every sexually reproducing species.**

**But ultimately, the question is maybe how big is this n-min? If n-min is two, then it's not a severe constraint on the population. Whereas if n-min is-- if you need to have 100 California condors in order to have a viable population, then that's a problem. So there really is a quantitative question of how big is this minimal size. Other suggestions of why it is you might have an Allee effect?**

**AUDIENCE: The animal species in groups?**

**PROFESSOR: That's right. Group hunting. And are you aware of any cases that have group hunting ?**

**AUDIENCE: Wolves?**

**PROFESSOR: That's right, so, exactly. Right, so wolves for example, can take down like bison, of large animals they would never be able to take down on their own. So this could be this could be wolves, it could be primates. We historically did-- I guess we still have some groups. Societies will have things like this. But even at the microscopic realm, if you look at just bacteria or yeast and so forth, there are often cases where food is generated or broken down outside of the cell. So any of these cases where you have secreted enzymatic breakdown.**

**That was an i. Other thoughts? Yes?**

**AUDIENCE: Protection from predators?**

**PROFESSOR: Right, protection. And so this is the flip side of this, so this would be predator avoidance. Or an example of that would be what?**

7

**AUDIENCE: Antelopes. PROFESSOR: What do antelopes do? AUDIENCE: They run in groups. PROFESSOR: That's right. So the standard example here is kind of what herding behavior of land animals, schooling behavior of fish. Of course, researchers argue about to what degree the benefits are primarily this, versus something else. I am not going to weigh in on that debate. But, I'd be surprised if this were never true. In all these examples, there's clearly something cooperative about the dynamics. In that sense, it kind of makes sense to think there's some element of cooperative growth, whether it's on the hunting side, or the protection side. So if you look at all these cases these would all be very naturally described as some sort of cooperation. I do want to highlight though, that the Allee effect can be caused by things that lead to what you might call effective cooperation. So it's not like obviously cooperative, or not intentionally cooperative, but still has the same effect. A nice example of this is what we call predator satiation. Can somebody guess what this might mean? Somebody's laughing so it's-AUDIENCE: If there are enough animals around, the predator will be fed. PROFESSOR: That's right. If the predators gets full, then you can end up with something that's like this. And the way I think about this is just in a group like this, if 20 bears come in and eat 20 of us, then we hope that there are 20 other people that will get eaten first, so that you know that the leftovers can run off. Right? This is embodied in that joke that people tell when they're the two hikers in the woods, and they see the mother bear that's angry and one of the hikers reaches down and starts tying his shoelaces. And the other thing the hiking partner says why are you tying your shoelaces? You can't outrun a bear, right? And the guys says, well yeah I know that, but I only have to outrun you. That's predator satiation. So if the predator gets full, then you can get something that looks like this. It's below**

8

**some size, below this n-min size, they all get eaten by that bear. And above it, the population may be able to grow. So this is a good example of just that it's an effective form of cooperation.**

**Now can somebody explain-- Well, first of all, does this lead to a full bifurcation if we add a death rate? We're going to think about this first seven seconds, then we'll vote. The question: if we add a death rate to this, does that lead to a fold or saddlenode bifurcation?**

**I'm going to give you more than seven seconds, because I see a lot of brain activity. Does this one lead to a full bifurcation? Ready? Three, two, one. The answer is, in this case, yes. So we'll say Allee effect is in general the kind of thing that leads to a full bifurcation. In this case, it definitely does.**

**So it's really very important to be able to take curves like this, and figure out what the bifurcation diagram looks like. And just remember that the solid and dashed lines here are very useful for getting intuition on what's going on, because stable is telling us that any perturbation away from this point, it goes away. So this is why we draw arrows here. Arrows come here. So this is saying that starting at 0, from a differential equation standpoint at least, you can add a single individual n, and that individual will reproduce and gets to whatever the effective carrying capacity is at that delta.**

**So what we can do is we can draw the same bifurcation diagram here. Where we look at the population size as a function of delta. And now it's actually somewhat more interesting looking, because in the absence of this death rate, we have it start at k. So what's going to happen is it's going to come like this. And the reason we call it a full bifurcation is because these fixed points fold over on themselves.**

**Now this is a bifurcation where as a function is a control parameter, it's not that these fixed points exchange stability, but rather that the fixed points collide and annihilate. So in general, a bifurcation is where something qualitative happens to the fixed points. In this case, the number of fixed points did not change as a function of the control parameter. Whereas in this case, it does change. But there are only**

9

**certain characteristic ways in which these six points are allowed to change.**

**So from this, we can draw our arrows. n equal to 0 is still a stable point down here. So we can draw. This is where colored chalk would be useful. We can draw our arrows. What do I do out here?**

**Now, the reason that we say that this population experiences a sudden transition, or a tipping point, is because you can imagine that this death rate being a slowly changing parameter. So you could imagine that it could be a slow acidification of the oceans, or a slow increase in the amount of fishing that takes place here. So then what can happen is that the size of the population, it's very healthy here. It's pretty happy, happy. Here it's maybe decreasing some, but you might not sound an alarm. But what can happen is that at some critical level of environmental conditions, some critical level of fishing, for example, you can get this catastrophic collapse of the population. Where over short periods of time, it can suddenly collapse.**

**Indeed, this sort of thing has been observed in a number of fisheries around the world. So if you go to, for example, the Monterey Bay Aquarium in Monterey, California, they have a very nice display explaining how that space ended up becoming and aquarium. Because it used to be a sardine fishery, and was a very productive fishery in the years leading up to World War II. But if you look at the number of fish that were caught as a function of time, it goes up, up, because there's fishing more and more, then all of the sudden, they just presumably fish too much and over a time span of a few years, the fishery collapsed, and there were just no more sardines to catch. That whole street there used to be canneries. But then it all went out of business. And those buildings were largely unused for many years. But then eventually, the aquarium went and bought some of them and refurbished them, and now it's a beautiful aquarium. So I encourage you to check it out.**

**But that being said, the collapse is probably still bad, even though it led to this nice outcome eventually. And what you can see is that not only are these tipping points or the sudden transitions maybe undesirable in the case of fishery, but it also would**

10

**be very difficult to reverse. Because it's not that-- You couldn't imagined that the bifurcation diagram look rather different. It could have looked like this.**

**What kind of bifurcation is this? So this is still a transcritical. It doesn't have to be a line throughout, because in principle there was this unstable thing down here. This is again, and, as a function of some parameter, we'll say delta. And so you'd say, oh this is a rather sudden transition. In the sense that a modest change in delta will lead to a dramatic change in the size of the population.**

**But there's something that's very qualitatively different about these situations. Which is that, here you can imagine that if you improve the quality of the environment, and then you reintroduce fish, or maybe you don't even have to introduce fish, they can come from a different area. Then, just by improving the quality of the environment, you get recovery. Whereas here, that's very difficult to do, because the system is hysteretic, or has memory. That means that even if you improve the quality of the environment here, it may be very difficult to get back to your previous state.**

**People think that they've seen this in the context of these transitions in lake ecosystems, so-called eutrophication transition, where you get as a result of maybe runoff from agricultural uses. You can get the sun transitions of not just a single population, but of an entire ecosystem. So the lake can go from this thing where it's nice and clear and beautiful summer vacations spot, to this really green kind of algal take over. And it can be very difficult to get recovery. There's was a question? No?**

**And so the basic-- We'll say something about the early warning indicators. Well maybe I'll say it now. So based on the review that you read, there's this phenomenon of critical slowing down that tells us that in principle, you can anticipate the transitions about to take place. And the statement was that the dominant eigenvalue described in dynamics, a system went to 0 at one of these points.**

**Now, the systems they were talking about were presumably systems like this. This is a so-called zero eigenvalue bifurcation, were the eigenvalue goes to 0 at this point right here. So here's a question for you. Does the eigenvalue describe the dynamics of a system go to 0 at this point? At transcritical. In a transcritical bifurcation. Do you**

11

**understand the question?**

**I'll let you think about it for 20 seconds, because this is maybe not totally obvious.**

**Do you need more time? I'm wondering. Maybe people are sufficiently lost or confused. They're not sure what-- Nod if you want more time. OK. Ready? Three, two, one.**

**I'd say it's a kind of a 50-50 thing. So go ahead and turn to you neighbor and try to figure out, using some combination of math and graphical analysis, whether the bifurcate-- Whether at this transcritical bifurcation the eigenvalue goes to 0.**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [[SIDE CONVERSATIONS] →](03-side-conversations.md)
