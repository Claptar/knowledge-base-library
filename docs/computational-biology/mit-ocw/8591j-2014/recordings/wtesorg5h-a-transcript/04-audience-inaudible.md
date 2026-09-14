---
title: 'AUDIENCE: [INAUDIBLE]'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/wtesorg5h-a-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE]

**Source:** `recordings/wtesorg5h-a-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: So I think there were some disagreements there probably. It was a little hard to tell from the verbal. And one way that we can think about this as that we can ask, well, the predator in the absence of the prey, what happens to it? So it kind of comes down here. So along this axis it's stable.**

**However, in the absence of predator, if you think about the prey, that'll grow. So this is actually an unstable fixed point. Stable along one axis and unstable on the other. Incidentally, what does this tell us about the eigenvectors around this fixed point?**

9

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: That's right. The eigenvectors are really just 0, 1, 1, 0. Because you can see that if you start along one of these, you come straight down. Start along the other one, you come straight down.**

**And the other one we can just see by-- well, we can solve it directly. Just we pull out an x. It's when a minus by is equal to zero. And also when minus c plus dx is equal to zero. So the other fixed point, this x star, y star, and this is maybe the important one. It's going to be just c over d and a over b.**

**Super simple model. Right? You can calculate where the fixed points are kind of immediately. But it's actually a model that has many weird properties. Some of which you might think of as features. Some of which you might think of as bugs. But in particular, the location of this fixed point, I think, is really sort of surprising in that its dependence on this abcd.**

**This is part of why I really think that when analyzing this model, I very much prefer to keep the a's, b's, c's, d's, rather than using the nondimensionalized version of it. Because when you do that, you lose track of what's going on. So this model for example, makes very clear predictions of what should happen if you hunt the predator.**

**There are various contexts in which wildlife managers have been interested in trying to help a prey population. So if a prey population is suffering in some way, then you can reasonably think what you should want to do is kill the predator. And this is all these debates where you have the wildlife managers, where they buy automatic rifles in order to shoot wolves from helicopters.**

**We have a Canadian in the room, right? I mean, wasn't this a Canadian proposal?**

**AUDIENCE:**

**I'm very American.**

**PROFESSOR: All right. We'll have to do some more research to figure out exactly. OK. Right.**

10

**So the question is, well, what happens at least in this model? And people apparently have seen this sort of thing occurring in natural populations as well, right? If you hunt the predator by going out and shooting them, what does this do to the predator and the prey populations.**

**In particular, we think about x star, y star. Well maybe this-- am I confused? Maybe this is the example that I'm confused by. Well we have to complete it now that I started it. But now I might have gone backwards. We'll see what happens, and then discuss.**

**All right. Ready. Three-- Oh wait. I don't have enough options. OK. Sorry. We should do one, then the other. Because sometimes things don't change, right? So how do I do this? OK. Sorry. OK. We should just do one, then the other, right?**

**No change. This is down. OK. There's gonna be a problem [INAUDIBLE]. Let's first do y star. Cause that's the most direct one. Sorry. I think that my story I got backwards. But we'll figure this out. OK. Ready?**

**OK. So the question is, there's a population that you want to-- all right. Now I'm going to redo my story to make it-- but there's a population you want to keep in check somehow. So you might reasonably go out and shoot it. Right? So the question is, if you go out and you do this on the predator, at least in this model, what happens?**

**All right. Ready. Three, two, one. Right. So although we actually have a fair number of disagreements on this. So we're actually kind of 50-50 at this stage.**

**What is it if you go out and from the helicopter, you start shooting this animal, what does that do from the standpoint of this model? Right. So we're shooting the predator. a, b, c, d, what you think? What should it change? c. And does c go up or go down? C goes up. OK.**

**Well, how does that affect y star?**

**AUDIENCE: [INAUDIBLE]**

11

**PROFESSOR: Yeah. AUDIENCE: [INAUDIBLE] PROFESSOR: Yeah. Right. You know, I mean, I'm thinking daily helicopter rides where you shoot wolves as you see them. AUDIENCE: This is Canada. PROFESSOR: This is Canada. This is Canada. Yeah, those Canadians. AUDIENCE: So effectively, you're changing the death rate of-- that's what you're saying. PROFESSOR: Well, OK. So that's my claim. Of course, all of these things can be more complicated. But it certainly is change in the death rate when you go and shoot them. So I guess I would say that in the context of this model, that's the simplest way to think about it. So the statement is that if you hunt this predator, you're increasing the death rate for the predator. You're increasing c. Hunting predator. This causes c to go up. And the striking thing is that y star does not change. OK. AUDIENCE: I believe you. I think it's funny. PROFESSOR: OK. [LAUGHS] You believe me. OK, I'm glad. One thing is believing me in the context of this model. Another thing is asking whether this is happening in real life. But I think people have seen such weird phenomenon in the context. But then of course, it's a matter of is this a dominant source? What's going on? Like many, many things. Right. But certainly in this model, there's this weird phenomenon where the death rate of the predator does not alter this y star. OK. We have to figure out what the y star means here in a moment.**

**What is the effect on this fixed point number concentration of the prey? It goes up.**

12

**So my original story, I think I was getting confused.**

**So at least in this model there's a sense that if you hunt the predator, it's true that you don't bring down the steady state, or the time average-- we'll see-- time averaged number of the predator population. But you do increase the prey population. Because in this case you can help the prey. But you don't bring down the predator.**

**Now I want to say something more about justifying this thing about why we might care about x star and y star so much. So this thing is x star/y star. Well, maybe all. Yes.**

**AUDIENCE: As soon as you stop shooting, this is a very temporary solution. When you stop shooting, c goes back to its original value.**

**PROFESSOR: That's right. When you stop shooting, c goes back to its original model, or original value. And then the prey population will come back down. So this is something you have to continue to do.**

**Yes. What do I wanna say? If you go ahead and you calculate the-- if we linearize around this fixed point x star/y star, that's our standard thing that we did early on the semester, what we find is that this Jacobian, this matrix A, the linearized matrix you get is-- all right. Well, we come here and we take the derivative with respect to x.**

**So we get a minus by. Derivative of this guy up top with respect to y. And we get minus bx. And derivative of this g function with respect to x. We get dy. Now aspect to y, we have a minus c plus dx.**

**Now we want to evaluate this around that fixed point at x star/y star, which is given here. We plug this in. So evaluate at y star. It's a over b 0. Evaluate at x star. This is just minus bc over d. Now y star, this is ab over b. And here we can get 0.**

**So this is telling us about the linearized dynamics around a fixed point x star/y star. Now for this sort of matrix, what are the eigenvalues? It's not that the eigenvalues are 0. It's a slightly different statement.**

13

**What are the eigenvalues for a matrix like this? What's that?**

**AUDIENCE: They're imaginary.**

**PROFESSOR: Right. They're purely imaginary. So the real part is equal to zero. So indeed, we can figure out this. Cause remember, to figure out what the eigenvalues are, you take the determinant of this vector a minus this lambda times the identity matrix. So we end up with, we want to take the determinant of-- we have a minus lambda, a minus lambda, and then minus bc over d. This is lambda squared. And then this is a plus, we have bc over d, ab over b.**

**So we end up that the eigenvalues are equal to plus minus square root of a times ci. So they're purely imaginary eigenvalues. And what does this mean again? What can you say when you do this sort of analysis and you have purely imaginary eigenvalues?**

**AUDIENCE: The orbits look like ellipses or something like that.**

**PROFESSOR: Right. So the statement is that-- OK. And then we have to be careful in all of this business. So what we've done is we've taken a set of non-linear, a pair of non-linear differential equations. We've done the linear stability analysis. And we get purely imaginary.**

**So one thing that you can say is that if you started with a linear system, and you got purely imaginary eigenvalues, that would tell you that indeed, you have these neutrally stable orbits, they go around. They can have a variety of different shapes.**

**But given that the order that we did things in is that we took a nonlinear system, and we linearized, and then got this. What does that allow you to say? Does that prove that you actually have these neutrally stable [INAUDIBLE]?**

**Yeah. Because this is one of those border cases, it unfortunately does not actually allow you to say that you have neutrally stable orbits. Because it turns out that the slight nonlinearities in the equations could cause problems, and cause it to go either**

14

**to a stable limit cycle or to a stable spiral. The confusing thing is that in this case it is true that you have neutrally stable orbits. But that did not have to be true.**

**And guys will get the chance to do this proof and so forth. Because there some conserved quantities. Of course, people have analyzed this thing in more depth. And it is true that you have neutrally stable orbits. But what is very hard to remember is that it didn't have to be the case just based on what we've said so far. Yeah.**

**AUDIENCE: So you mentioned, it's not a coincidence. There is a deeper reason why? PROFESSOR: Well, coincidence. I guess what I'm saying is that you can prove that this thing does have these neutrally stable orbits. But we have not proven that. And we're not going to. Do these orbits go around clockwise or counterclockwise? Ready. Three, two, one. AUDIENCE: Counterclockwise. PROFESSOR: Counterclockwise. Right. And you can get that from thinking about what predator and prey should do. But also I've already drawn some arrows here. And that kind of helps provide some guidance. So they kind of come around like this. Now is this the only orbit that I should be drawing here? No. Right. Because it turns out that in this case there are an infinitely large number of orbits that could possibly come around. Yes.**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: Yeah. Well, in the context of our simulation, the simplest thing that you guys would probably do is you would simulate and see what comes around. But yeah. I think even in the reading, did they prove it? Different authors in different books either prove it or don't. And there are a number of different-- you'll see in the problems, you can find that there is a quantity that is conserved along the equations of motion.**

15

**But the quantity's different for each of these orbits. Right. So it's really saying that as you go, there's some quantities conserved. And it still has the same value when you go around. And so that means you had to kind of come back to where you were. So there is a conserved quantity. You'll see it.**

**Now these neutrally stable orbits are kind of funny in several ways. Well, first of all, this eigenvalue tells you about the period of the orbits when you're close to the fixed point. And you can see that it doesn't depend on everything in the model. It depends on a and c. Does that kind of make sense, maybe?**

**Yeah. Sort of. Cause a is telling us about how rapidly we grow up here. c is talking about how rapidly we die over here. So you know, it has something that at least has units of 1 over time.**

**It makes sense that a and c should appear here. But I would submit that it's not totally obvious that b and d should not appear at all.**

**So neutrally stable orbits, there's no characteristic amplitude to the oscillations, nor period. And this is at least true far from the fixed point. This tells you about maybe these orbits. But then it doesn't tell you about what happens far away.**

**And these are not the kind of oscillations that from a mathematical standpoint we like the most, which are limit cycles. And remember, a limit cycle would look like this. If it were a limit cycle, it would be that there's some orbit that is stable in the sense that if you start inside of it, then you would approach it over time. If you start outside of it, then again, you would approach it over time.**

**And this orbit then would have a characteristic amplitude, and a characteristic period, because it's one orbit. Whereas here, this has kind of an infinite number of different orbits. What this means is that just any sort of noise-- demographic fluctuations and so forth-- would cause the system to drift over time in terms of this amplitude of period.**

**So it's true that if you got it started in the absence of any noise, it would keep on**

16

**doing that oscillation forever with that amplitude. But any random noise will cause the thing to drift.**

**The other thing that is worth stressing in this is that if you do a time average of the predator concentration, or the prey concentration, so if you do the average or the mean, x as a function of time, or y is a function of time is indeed x star y star. That's also something that you'd have to show. Not at all obvious from this.**

**It's not a surprise for these orbits that are out here that the time average is indeed x star /y star. But for these big orbits, they probably already didn't have to be. So this is telling us that the analysis that we were talking about-- well, what happens if you do one thing or another thing-- that's actually kind of a reasonable quantity to be trying to calculate, because that is the average or the mean number of predator/prey in this model.**

**Yes.**

**AUDIENCE: So in a zombie apocalypse, how do we thin down the zombie [INAUDIBLE].**

**PROFESSOR: Yes. That's a very important question. In the event of a zombie apocalypse, what do we have to do in order to thin out the zombie population? All right. Well, the zombie movies typically are not yet at equilibrium.**

**But certainly at equilibrium, what do you want to do? This is not a formal recommendation, by the way. But in this model, if you want to decrease the number of the predator, what is it that we want to do?**

**Right. Well, OK. So in this model, if you want to decrease the number of the zombies at equilibrium, you want to decrease a, which corresponds to--**

**AUDIENCE: So it's a is equal to 0. So the birth rate is equal to the death rate, then there aren't new zombies.**

**PROFESSOR: Yeah. There are probably also no people.**

**AUDIENCE: But there are. The birth rate is equal to the-- so you have a stable population.**

17

**PROFESSOR: Right. So in the limit, as a goes to 0, it's true that the number of zombies goes to 0. AUDIENCE: So you just have to beat [INAUDIBLE]. PROFESSOR: Yes. This is a good situation where it's important to ask about whether your assumptions in the model are good before making public policy based on them. OK? Indeed. But can we go back just for a moment before we switch gears, to ask about this question of why it was that war might have favored these predator fish? And by favored, what he really measured, he measured the number of the frequency of these kind of predator fish at the markets. So it's somehow is maybe the ratio of those two, or so.**

**Yeah. That's right. Yes, it could that the fisherman just-- yeah. So they could have fished in a different region. And so the explanation could be something--**

**AUDIENCE: Because it's not very well controlled. PROFESSOR: It's not a controlled experiment. That's why you need to have many different wars in order to average the importance of large data.**

- **AUDIENCE: That's going to be a great [INAUDIBLE].**

**PROFESSOR: Right. And then of course, in all this business you have to ask, well, which thing are you varying more or less, et cetera, et cetera. But let's say that to first order, the fishermen are going out there and they're just catching all the fish in an unbiased fashion. But the war is making it more difficult to fish. So not as many fishermen go out.**

**And then what does that do to these parameters? Right. So it might increase a, because the prey are not getting caught as much. And it might do something also to the predator. What?**

**So the predator fish are also being caught, cause they're showing up at the market.**

18

**Right. So which other parameters does it change? So what's that?**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: Right. So lets be clear. It's a war makes a go down. All right. And what other parameter might change? AUDIENCE: Fewer fishermen. PROFESSOR: Oh. I'm sorry. I'm sorry. You're right. You're right. I was starting to think about the next one.**

**OK. So a goes up. And what also happens? And c goes down. And this is just because a is a growth rate. c is a death rate. So it's not that the fishermen are preferentially changing what they're doing between the prey fish and the predator fish, but it's just that these are defined different ways. Right?**

**And in particular, what this means is that in times of war, Voltaire's argument to his future son-in-law was that what you expect is that the predator population should go up. And the prey population should go down. So the ratio of them should certainly shift in favor of the predator.**

**Or maybe it's just that the fishermen didn't go into the deep regions of water or something, where predator fish like to hang out. But it's striking at least that a simple model like this can actually provide some insight.**

**Any questions about where we are before we modify the model in some way? Now, the problem with this model is that it's making lots of assumptions that we very much think are not true. So we have a few of the assumptions up there.**

**Which ones are you guys least happy about among those assumptions? Yeah. The second one, the prey grows exponentially, i.e., without bound. That's not physical. We should fix that.**

**So let's go ahead and do that. All right. So real prey populations-- and all**

19

**populations-- populations saturate. Don't go to infinity, right. We can just make a quick little fix to our model to capture this, right? X dot. So now it's going to be this ax. But what we can do is we can add a logistic term here. And we can leave everything else constant.**

**So we just add this logistic row term. So now in the absence of a predator, what will happen is that the prey population saturates at some point, at some value k. Right? And k could be rather large, if you like.**

**And I think this is the kind of situation where you say, oh well, that could be just a really modest change. Because it's primarily telling us about what happens kind of in the absence of the predator. But really, the dynamics around here could be unchanged.**

**But what's striking is that because of this neutral stability of the model, any little change can lead to a qualitative change in the outcome at equilibrium. And in particular, adding a carrying capacity causes the sustained oscillations to disappear. Instead you get damped oscillations.**

**So in this case, xy, you still have this fixed point. But what happens is that you get-it orbits the look. Kind of like this. Yes.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Yeah OK. So that depends upon [INAUDIBLE]. And indeed, as k goes to infinity, the timescale of this decay goes to infinity as well.**

**AUDIENCE: [INAUDIBLE] clean scaling.**

**PROFESSOR: A clean scaling.**

**AUDIENCE: But I mean just [INAUDIBLE].**

**PROFESSOR: I mean, I don't have nothing intelligent to say. But what I can say is that if you put in a k at values that are close to this fixed point, then the oscillations really disappear.**

20

**It's really only as k goes way, way out.**

**And I maybe won't do this calculation. But you can do it quickly. It's the kind of thing you can do in five minutes on an exam or so, right? But then the question you might ask me, well what can you do in order to get these oscillations that we really like? These sustained limit cycle oscillations?**

**And there are two ways you can think about this. One is by a kind of taking this sort of model and adding features and playing with it and so forth. Or you can ask a mathematician who kind of derives everything in kind of totality. And then you can see it. I'll say that one thing you can do on a concrete basis to change the outcome of this is you can add something that is kind of like some saturation effect at the level of the interaction between predator and prey.**

**So instead of scaling purely as x times y, if instead there some sort of MichaelisMenten type behavior as a function of the prey, then this model is actually converted to one that has a stable limit cycle. And in this case, can you guys remember how you show that something has a stable limit cycle?**

**Yes.**

**AUDIENCE: [INAUDIBLE] use the Poincare--**

**PROFESSOR: That's right. There's this Poincare-Bendixson theorem, which tells us that if we can draw some box out here where the trajectories are all kind of coming in, indeed, here the trajectories are kind of coming in. Now in this case the trajectories have to come in everywhere. But this is typically true in any of these reasonable systems. Because they should, if there's just not that much food, they should be coming in.**

**Now in this case, there's a single fixed point. So then the question of whether there's a limit cycle is equivalent to the question of the stability of this interior fixed point. It's a stable fixed point, then all of these trajectories will spiral in. However, if it's an unstable fixed point, then you have to have a limit cycle oscillation somewhere in between.**

21

**Yes. AUDIENCE: It could be that it's a stable midpoint. And then you have two limit cycles. Could that be? PROFESSOR: Right. So the question is whether there can be a stable limit cycle and two limit cycles. I think that that requires more fixed points. Because let's say you had a limit cycle here. That this is saying that the trajectories come in. But it's also saying the trajectories are coming out. I think that you have to have a fixed point inside here in order to have these trajectories going-AUDIENCE: So what I'm saying [INAUDIBLE] two circles, and way outside, all the trajectory is [INAUDIBLE]. But between the two circles, the trajectories go from the outer circle to the inner circle. And then from the inner circle in [INAUDIBLE]. PROFESSOR: Are the circles encircling each other? AUDIENCE: Yeah. PROFESSOR: OK. So here's one circle. Here's another circle. And the trajectories are coming into this one and what are they doing? AUDIENCE: So each of these limit cycles are only semi-stable. There are some-PROFESSOR: Yeah. All right. All right. So you're talking about these limit cycles where the trajectories come to it from one side, but then leave from the other side. I'd have to think about this more. Everything that I'm talking about are the limit cycles that are stable from both sides. And I think that in the presence of any amount of noise, those are the only ones that we care about. Because you can write these models where you have orbits that are stable from one side but not the other. But then they don't matter in any real system that is subject to noise. Because it's not a stable orbit in that case, right?**

22

**AUDIENCE: Then we can make the outer circle stable from both sides, and the inner circle [INAUDIBLE] from both sides, and we could get it [INAUDIBLE].**

- **PROFESSOR: OK So it could go like this. So you're saying that this outer orbit is now stable from both sides. And then this one is unstable from here. And oh, OK. Now you're saying this thing is unstable from-- so now it's stable.**

- **AUDIENCE: So we can have--**

- **PROFESSOR: Yes. OK. So I can certainly draw the trajectories, as you pointed out. And it works. Yeah. I don't know if this is a loophole in the wording of the theorem, or if this is just not possible.**

- **AUDIENCE: [INAUDIBLE] There's like one way in which it applies. And then the other way you kind of usually think that it applies, but then you're wrong because there are these counter examples.**

- **PROFESSOR: I see. Well, how about this. I will look it up. And then I will tell you what I think the answer is. I'm certainly not going to be able to derive it on the spot. But You're right, though. I can draw the orbits and they do it. I don't know what that means.**

- **AUDIENCE: So I think the theorem is if on this large circle on the outside everything is coming in, then if your fixed point is unstable, then you must have at least one stable [INAUDIBLE] outside. Or you must have at least one that is [INAUDIBLE] or something like that.**

**PROFESSOR: OK. But you're saying that it-AUDIENCE: But if you flip it so the fixed point is stable, then you could have--**

**PROFESSOR: I see. That may be right. I can't remember which direction. But I'll look it up.**

**But if you are curious about the situations in which these predator/prey functions will have limit cycles, you can look up Kolmogorov's conditions. So he basically has**

23

**these four conditions in which you will get a stable limit cycle in the predator/prey populations. And maybe I will.**

**And they're surprisingly simple. They were in the reading. So you can look at them. But they're basically just these questions of the derivatives. And they're derivatives of the per capita growth rates.**

**So you take those functions, you divide by x. So it's x dot over x. And then it's some f, y dot over y, sub g. And the derivatives of those functions withe respect to x and y have to be something, at least in some limits. And then you get limit cycles.**

**But I want to talk about the experiments. Because I think that they were quite pretty. So this is a paper by Yoshida, et al.**

**This is Nature 2003. And the title was "Rapid Evolution Drives Ecological Dynamics in a Predator/ Prey System." Could somebody kind of say what they think is the big point of this paper?**

**Do you guys like the paper, dislike the paper? Too long? Was it three pages? Although it's really only-- I mean, one of the pages is figures. And one of the pages is essentially methods. So it's really basically a one-page paper, so it's not such heavy lifting, maybe.**

**All right. Maybe I'll be concrete. What features of their predator/prey oscillations were different from a normal predator/prey oscillation? What were the features they were trying to explain?**

**AUDIENCE: There's a longer phase life between the maximum.**

**PROFESSOR: And this is an interesting history, actually, that these are authors-- they took what I think are basically like samples from the Great Lakes, or something like that. So they took a predator and prey. So it's a rotifer algal system. So the rotifer eats algae.**

**They had previously published a paper just a few years before, where it was called something like "Crossing the Hopf Bifurcation in a Predator/Prey System." And so**

24

**what they did is they had a chemostat where there was some constant rate of dilution in their chemostat. And then they measured the dynamics between the predator and the prey.**

**And they showed that depending upon, for example, the nutrients or this dilution rate in their chemostat, they could go from a situation where you have a stable coexistence-- so a stable fixed point between the predator/prey-- but at increasing dilution rate, they started getting these oscillations.**

**So they went from stable to oscillations. And then at higher dilution rates, they got collapse of this predator/prey system. So this is crossing the so-called Hopf bifurcation, where you go from stable to unstable. So they could actually see that they could use a simple model to try to get some insight into why it is that a predator/prey system might oscillate or it might not oscillate.**

**And so that was great. But there were some features in their data that they didn't understand. So the features were that the oscillations had a really long period. Long period oscillations.**

**And in all this data, it's a little bit hard to get the exact phase lag, but in many of the cases they saw that the predator and prey were not at this 90 degrees out of phase like you would expect. And in particular, for the predator/prey, given that you have x and y, and it's going around some circle, the idea is that first the prey population peaks. And then kind of 90 degrees later phase, you get a peak of the predator.**

**And you can imagine that in any predator/prey model that you write down, not just Lotka-Volterra, but if you write down a differential equation with some x and some y, it's hard to get something where it looks much different. Of course, you can imagine maybe funny orbits or something like that. But generically you really expect this 90 degree phase lag of the predator relative to the prey.**

**Whereas in the experiments, they often saw 180 degree lag, lack of predator relative to the prey. Yes.**

25

**AUDIENCE: So when you say [INAUDIBLE] theory of oscillation, what does that mean? What's the time scale? PROFESSOR: Yeah. AUDIENCE: What would make this suprisingly [INAUDIBLE]? PROFESSOR: Right. Yeah. OK. So this is really in the context of-- I mean, they wrote down a model where they did basically have something like this, where they said there's some--**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: That's right. And in particular the predator, I think, was not really dying on it's own. Except for the dilution. So it's really the dilution rate from the chemostat gave them c. And they could see that indeed, the rotifer wasn't dying much.**

**And then a is telling you about what happens if you don't have the rotifer, you don't have the predator. And then at that dilution rate, you ask what the division rate is. And that's essentially the growth rate of that prey population minus the dilution rate of the chemostat. I'd say that they had these parameters pretty well.**

**Yes. And what they saw experimentally was that it took much longer. I mean, the period was 5 times, 10 times longer than what they would have expected based on the measured parameters for the predator and the prey. And of course, that was annoying for them, because they're actually doing the experiments. So they had to do these chemostat experiments that lasted six months or something like that, in order to see a couple oscillations.**

**And so this longer period wasn't just a mathematical-- I'm sure that they were disappointed to see these really long time-scale oscillations, because it was something that made it very difficult for them to do the measurements. But this is what they saw experimentally. And they didn't know what was causing it.**

**But they later then did more modeling where they asked, which of the assumptions in our original model might not be true. And the nature of these things is that there**

26

**are an infinite number of things are true that are not incorporated in the model. And this makes it quite challenging to isolate what the effects might be.**

**But at the very least what they can do is they can go in. And they have some sense of their system. And they can make guesses of what might have been the primary things missing. And then they kind of went through the models and they asked, well, if we kind of change this assumption or that assumption, what does it do in terms of the oscillations.**

**And then what they found in a modeling paper-- so this is their previous experimental paper before this. What they found in their models was that prey evolution was kind of the one thing that if they allowed prey evolution, i.e. If they allowed different types of prey in their prey population that might be oscillating independently, then they could get both of these effects.**

**So from the models they concluded that prey evolution could give this, could maybe explain those two things. These are the two experimental features. Yeah.**

**AUDIENCE: It might be that you have [INAUDIBLE] symantic point. If you have two types of species, pre-species-- [INAUDIBLE] they have these characteristics and they're not evolving. They're just fixed.**

**PROFESSOR: Yes.**

**AUDIENCE: You would still be able to--**

**PROFESSOR: Exactly. Right. This is a major--**

**AUDIENCE: [INAUDIBLE] PROFESSOR: Yes. You can argue about what you want to call evolution and not revolution. Over these time scales what they are not looking at is the de novo kind of emergence of new mutants spreading in the population. What they're looking at is variations in say, different types of prey.**

**AUDIENCE: So is that what we would call evolution?**

27

**PROFESSOR:**

**Well, OK. This is a major question. I think different people call evolution different things. And in particular there's a distinction between the ecologists and the evolutionary biologists, or evolutionary microbiologists, or whatnot. And this is something that I certainly encounter.**

**For the experimental microbial evolution guys, I'd say that for them, if you use the word "evolution," what they really want to see, or what they're expecting to see is kind of new mutants arising in the population, spreading, fixing, and that changes the character of the population.**

**Whereas from that standpoint of ecologists-- and indeed, if you look up the definition of evolution, it's some change in allele frequency over time. And this could certainly be a change allele frequency over time in the sense that you could imagine this arising just from, for example, there could be a point mutation in some gene that leads it to do something or another.**

**And in this paper they didn't identify exactly what was going on. I'll tell you a little bit about a later paper where they get a better sense of it. But at least you could imagine it being the case that there's just a point mutation, some gene that has some fitness defect in the absence of the predator, but then allows the algae to avoid the predator in some way.**

---

[← AUDIENCE](03-audience.md) · [Up: contents](index.md) · [AUDIENCE: [INAUDIBLE] →](05-audience-inaudible.md)
