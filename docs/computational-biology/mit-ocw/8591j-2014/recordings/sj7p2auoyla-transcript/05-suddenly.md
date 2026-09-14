---
title: suddenly.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/sj7p2auoyla-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# suddenly.

**Source:** `recordings/sj7p2auoyla-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**One thing that I strongly encourage everyone to do is, in these sorts of problems, it's wonderful to spend time-- Oh, sorry. This is log. Free x log of xT. It's really very valuable to plot things in multiple different ways, by hand or by the computer or both or whatnot, just to make sure that you're keeping track of what's going on. Because often what you see and what you think is very different depending on what you plot. And you'd like to be able to see your problem from as many different angles as possible.**

**All right, I think that we've probably spent about as much time on this as we ought to. But are there any other questions about how this is going to come about? Yes**

**AUDIENCE: Are there any negative autoregulation that can use sequestration to get a switch-like [INAUDIBLE]?**

**PROFESSOR: OK, that's an interesting question, although we have to be careful about-- If you really want it to be more switch-like, you'd probably use positive autoregulation. And I'm not aware of a case where this has been combined, although-- It's likely there are some. I just don't know them.**

**I'm going to switch gears to this autoregulation, which is something, of course, that you guys just read about. And it looked like your understanding of it was solid. But we want to move through these different ideas. First, this idea of a network motif. And this is just the simplest example of a network motif. And it's so simple, we often don't even call it a network motif. But the idea here is that we have some network, and it has maybe N nodes and E edges. And the example that they give, that Uri gives in his book, N was 420, and E was 520. ,**

**And there's a basic question that if you have a network with N nodes and then you have directed edges-- these are edges that have an arrow pointing on one end. Now, in that case, and if you allow self-directed , edges how many possible edges are there? Does anybody remember what this looks like?**

13

**AUDIENCE: More than 20 possible, right? PROFESSOR: What's that? AUDIENCE: There'd be more than 20 possible. PROFESSOR: Right, not even in terms of the actual number. Just in terms of N, for example. AUDIENCE: Total or just self-directed? PROFESSOR: Total self-directed. Or Sorry, total directed edges, total number of possible directed edges, if we included self edges, I guess. N squared. And you can think about this in multiple ways. One is just that, well, you can start at any of the N nodes. And you can end at any of the N nodes, and that gives you N squared. Right? But there's another way that you could-- For instance, this is Emacs. It's NE N squared. You could also think about this, if you like, as just-- say, well, as they point out, there's sort of-- 1/2 N times N minus 1 is the total number of pairs in the network. And then for each of the pairs, you can have an edge pointing either direction, so that gives you a 2. Plus, you can have N self edges, right? Now, of course, these are just different ways of counting N squared. But it's useful to just think about it in different ways to make sure that you're comfortable with the combinatorics of it. In particular, because next week or the week after that, we're going to be talking about network motifs in more detail, in particular the feedforward loop. And then we really have to keep track of these sorts of combinatorics better. The way that Uri thinks about this is he says, all right, well, we're going to invoke this null model of a network, this Erdos-Renyi network, where we just simply say we're going to assign the E edges randomly across the Emacs possible. So of all possible edges, we're going to place the edges randomly and then I generate some random network. So this is basically what we typically call a random network. And that's going to allow us to define some null model that if everything were random, we can ask, for example, how many self edges do expect to get?**

14

**Well, one way to construct this sort Erdos-Renyi network-- Yeah. AUDIENCE: But how do you know if you have other kind of constraints in the system, how do you know that transcription might require in some cases autoregulation-The answer that was give that was a good answer was that evolution is the only thing that can-- if you find a network motif that has to do with evolution--**

**PROFESSOR: So that is the argument that Uri makes, and you're maybe saying maybe that's not a good argument. And what Uri is saying as well, if you see these networks more frequently than you would expect by chance-- and of course, you can define what you mean by chance-- then you can say oh, maybe it was select for, it was evolved. And I think that, in the case of this autoregulation case, I think the results are not very sensitive. But I think that this question of what the right null model is, is a real issue, especially when you're talking about some of these other networks.**

**And what we'll see for the feed-forward loop is that you have to decide-- well, one thing we're going to see is an Erdos-Renyi random network is very much not an accurate description of real transcription networks. So then you could say, well, that's not a good null model to use. And so we'll definitely spend some more time thinking about this.**

**In the context of the Erdos-Renyi network, though, one way that you can generate it is that for each of the Emacs possible, each of these total number of edges, there is some probability that you're going to actually place a real edge there. And that probability is just E over N squared. E is the number of edges. N squared is the number of possible edges. So if you just create a random network in that way, then this is a manifestation of a random network that has at least the basic properties, the same number of edges as our network.**

**So from this, you say, well, how many self edges would you expect in this world? And you'd say well, in that case-- There are two ways of thinking about this. So you can either say, we're going to take, for each of the N edges, there's one possible self-directed arrow. And for each of those cases, we can just multiply this by P. And**

15

**this gives us E over N.**

**You could also think about it as-- There are multiple ways once again, of doing the counting. In an Erdos-Renyi network, you can say, all right, you would expect to get roughly E over N autoregulatory loops.**

**And this is of order 1. So this is 1.2, in the case of the network that Uri analyzes in his book and his paper. Whereas, how many were actually observing in the network that he studied?**

**AUDIENCE: 40.**

**PROFESSOR: There were 40, right? So in the observed transcriptional network-- and this is in E. coli-- he found that there were 40. And the basic statement here is that 40 is just much larger than 1.2.**

**And you can quantify this a little bit better, because, it's really you would expect 1.2 plus or minus the square root of this, in a random network like this. But that is, you'd expect 0, 1, 2, maybe 3. So 40 is definitely not what you would expect based on an Erdos-Renyi network. So this is the sense in which it's a network motif. It's that the observed network just doesn't look like a random network in this very particular sense.**

**And of these 40, does anybody remember kind the distribution between negative autoregulation and positive autoregulation?**

**AUDIENCE: It was 30-10 or something.**

**PROFESSOR: Yeah, I think it was like 34 and 6 was my recollection. I didn't write this down. So most of these guys have a form of x inhibiting x. But some had the form of x activating x. So this was something like 34 and 6. What you would say then is that negative autoregulation is a very strong network motif, whereas positive autoregulation is a weaker network motif, but still something that occurs perhaps more than you would expect by chance. Are there any questions about that where that argument came from, other concerns about it?**

16

**All right, then from this, then Uri says, OK, well, maybe these things evolved for a reason. And so what we'll do in the next half hour just argue or discuss what possible evolutionary advantages such a social network motif might have. Yeah.**

|**AUDIENCE:**|**Can you really propose adversarial explanations like that?**|
|---|---|
|**PROFESSOR:**|**Oh, you can propose whatever you want.**|
|**AUDIENCE:**|**I know, but it doesn't have much value. It's unquantifiable.**|
|**PROFESSOR:**|**Yes. No, I'd say this is a major issue in a lot of evolutionary arguments. And I would**<br>**say that the purpose of ideas and hypotheses is to get you to go and make new**<br>**measurements. And so right now, we're the stage, OK, well, maybe these things are**<br>**occurring more frequently than you would expect by chance. So now, we can just sit**<br>**down and think, oh, what advantage might it give. And then we can go and try to**<br>**experimentally ask whether those advantages are at least manifested in real**<br>**systems. It doesn't prove that that's why they evolved, but it makes you more**<br>**comfortable with the argument. feel**|
||**Ultimately, we assign some-- we have some agent probability somewhere in our**<br>**brain. And the more evidence that we can accumulate that's consistent with these**<br>**ideas, the more likely that we think it is. But in general, you don't prove things in this**<br>**sort of evolutionary space the way you prove things in many other fields. Yeah.**|
|**AUDIENCE:**|**I feel like it's hard to call this an argument. It feels more like just an observation.**|
|**PROFESSOR:**|**Which thing is an argument versus--**|
|**AUDIENCE:**|**I guess the thing is it should be evolutionarily advantageous, that's an argument, but**<br>**essentially, the whole thing is an observation, and then there's a little bit of an**<br>**argument in the end.**|
|**PROFESSOR:**|**Yeah, I will let each person decide what fraction and observation. Yeah, I don't feel**<br>**especially strongly about it. My guess is that it did evolve it because it provides**<br>**some useful function. And therefore, I think it's valuable to explore what those useful**|


17

**functions might be. But for example, it's very hard to know which of these explanation-- this thing about increasing the response time, or sorry, increasing the response rate as compared to increasing robustness, how do you decide which one's more important? Then I think, once again, reasonable people can disagree about these things, yeah.**

**So first negative autoregulation, because this is the one that is the stronger network motif. I think that the book does a nice explanation of why it decreases the response time. OK, we can just ask. OK, response time-- and this is for a negative autoregulation. Response time goes down. And is this for turning on, off, both, or maybe neither, or E, don't know.**

**And I'll give you just 10 seconds to think about this. It's nice if you just remember it, but it's also maybe even better if you can figure it out. Because in a week, you're probably not going to just have it memorized, but you should be able to think through the logic of it and understand why this is going to be what it is.**

**All right, so the question is, negative autoregulation, maybe it does something. Maybe it decreases the response time. But does it decrease the response time for turning a gene on, for turning it off, for both, neither, or don't know**

**AUDIENCE: When you say turning it off, what exactly is the process you're imagining.**

**PROFESSOR: I'm imagining a process where the expression turns off immediately. So there's a signal that just stops--**

**AUDIENCE: what transcription can go ahead.**

**PROFESSOR: Right, so then it's just I chop up all the polymerases, and no more expression. But so a signal comes and tells the polymerases to stop making. Yeah.**

**All right, so do you need more time? No. Ready, three, two, one. All right, so we actually are all over the place on this. OK, turn to your neighbor. And you should be able to explain one way or the other why thi-- what is going on.**

**[SIDE CONVERSATIONS]**

18

**Let's go ahead and reconvene. I just want to remind everybody that when I say simple regulation, there's no autoregulation. It's just responding to a signal. That for a stable protein, the time to get to say, for example, half saturating concentration here is defined by the cell generation time. And that's true for turning on and for turning off. And what was the strategy that you could use if you wanted to decrease the response time in this situation?**

**AUDIENCE: Increase the degradation rate.**

**PROFESSOR: Right, so you could increase the degradation rate. And does that the on, off, or both?**

**AUDIENCE: Both.**

**PROFESSOR: Both. But there's a cost, which was what?**

**AUDIENCE: You have to make protein.**

- **PROFESSOR: Right, you have to make a bunch of protein, and then you're just going to chop it up right after you make it. There is a reasonable-- there is a way to make things faster, but it has a significant cost.**

**The question is, if you have negative autoregulation-- so in this case, you have x that is repressing itself-- what is it that it's going to do? Is it going to affect the on time, the off time, or both. Let's just see where we are. Ready, three, two, one.**

**OK, so it's interesting. We're moving towards C, it seems. OK, so can somebody give me an explanation for C. Did we read the chapter?**

- **AUDIENCE: Well, the chapter doesn't discuss the effect of negative autoregulation and turning off. I don't think it does.**

- **PROFESSOR: Wow, it's a good thing we're doing that here then. All right. So first of all, can somebody give the explanation. Does T on go up, down, or sideways.**

- **AUDIENCE: Up.**

19

- **PROFESSOR: So T on-- It's the time that goes down. I always get this confused. So time is the one that goes down, so the rate goes up. Negative autoregulation is faster turning on, we decided. Right? And does somebody want to give the explanation for why this is?**

- **AUDIENCE: Well, your equilibrium level is lower.**

- **PROFESSOR: Yeah, right. Yeah, exactly. Yes, this is actually surprisingly difficult to explain even though it's not a deep concept. But the idea is that you start out expressing a lot, so that if you had kept on expressing that high level, you would have done some exponential-- It would have take cell generation time from way up here. But instead, what happens is that you shoot on up. But then, once you get up here, you repress expression. So then you get an effective thing, where the time it takes you get half of your equilibrium, that goes down. So Tl in here is shorter than here. Yes.**

- **AUDIENCE: So in negative autoregulation, for decreasing what the book calls beta, to have the same steady state?**

- **PROFESSOR: That's right. The initial beta, that rate, that maximal rate of expression, that goes up in a case of negative autoregulation. But then you start repressing expression once your concentration of x here gets to some reasonable level.**

**So now we're just talking about production rate of x. And that's as a function of x. And of this logic approximation is when it just is maximal until it gets to some K and then is completely repressed. So real versions will be much smoother, but this is just useful to start getting the intuition.**

**And the idea is that you shoot up to this K, and then you stop expressing. In this limit, actually, it's not even-- it's like a kink here. Because it just shoots up and then it turns around. But any real system will be smoother. Yes, question.**

**AUDIENCE: So if you get to a certain equilibrium level, then in autoregulation, you would need a stronger promoter.**

20

**PROFESSOR: Yes, you want a stronger promoter, because you really want to have high expression initially and then later repress that. So negative autoregulation allows you to speed up turning on, so T on goes down.**

**AUDIENCE: Without increasing the promoter, which is a good thing, because someone would die if you increase the promoter.**

**PROFESSOR: This is a very important point, which I was about to get to, which is that this is something that was done-- We could have done that without negative autoregulation by increasing the degradation rate. So the question the that we're bringing up here is, is there that same cost that we were referring to before of this futile expression of protein at equilibrium.**

**AUDIENCE: No.**

**PROFESSOR: So it's actually not. In a cell, you start out expressing a lot, but then later, you actually bring down your rate of expression. And in any case, there's no degradation. in this. The only effective degradation is due to the dilution, the growth of the cell. So if you have the same concentration, then actually, you don't make any more protein than you did here, because you have the same concentration at equilibrium.**

**So this is neat because this speeds up the response when you're turning on, without the associated cost of making that protein then degrading it. Any questions about that statement?**

**So now what about off? Is the off time the same as the on time here?**

**So what sets how fast--**

**AUDIENCE: Should the off time be slower because you have lots of degradation.**

**PROFESSOR: Right, and in principle, is there any active degradation that we've invoked on this?**

**AUDIENCE: I think not.**

21

**PROFESSOR: Of course, we could have both negative autoregulation and active degradation. But in principle right now, you can have the negative autoregulation without any active degradation. In that case, how long does it take for that concentration to go away when you stop expressing?**

**AUDIENCE: The cell degeneration time.**

**PROFESSOR: The cell degeneration time. So this thing actually looks the exact same as this. So these guides are the same, whereas this one is faster than that one. Because the idea is that the best that-- unless you're inactively degraded, all you can do is you can shut off expression. But then if you turn off expression on the negative autoregulation, it's the exact same thing as turning off expression in the absence of the neg-- in either case, you just stop making protein. So the concentration just goes down because it's being diluted away during cell growth. So this is saying that response time was down only when turning off in the case of negative autoregulation.**

**Are there any questions about that idea? Yes.**

**AUDIENCE: With the negative autoregulation, in order to reach the same protein levels, you'd need much greater production rates, correct?**

**PROFESSOR: Yeah, so the idea is that this beta might be-- so this is the beta of negative autoregulation. It could be much larger than the beta of simple regulation in order to get to the same equilibrium.**

**OK, so what about this idea of robustness? Well, this is production rate and then degradation rate. So this is an alpha x. And so my question here is, I told you that robustness-- something is robust-- Yeah, question.**

**AUDIENCE: My question is in this case, you're saying that the off means signal disappears, right? PROFESSOR: OK, T off is this idea. It's the T 1/2. So this is the time that it takes for the protein concentration to reach half-- to go from halfway the distance from where you were**

22

**to where you're going to end up. AUDIENCE: But what if the signal not disappear, but to half of the original signal? PROFESSOR: So the signal could do a range of different things. And it could be that the signal just changes so that instead of going down to 0, you go down to some other value. Is that what you're imagining? AUDIENCE: Yes. PROFESSOR: In that case, you still go exponentially to this new value, so actually the T-- the response time there is still actually the cell generation time. So it doesn't matter, in the absence of any these, for example, autoregulation. The time, the characteristic timescale, is always the cell generation time if it's a stable protein. It doesn't matter whether you're going up, down, or all the way to 0 or not. So the question here is-- OK, x equilibrium is robust to what? And this is to small changes in what? It's going to be A, alpha. So this is going to be our first example of an advanced use of our cards. So the way that it works is that you can choose more than one. OK, now, this requires some manual dexterity. So what you have to do is if you think that the answer is more than one of these things, then what you have to do is show me more than one card. These cards are amazing, right? You can do so many different combinations. I'll give you 20 seconds to think about it. AUDIENCE: So what's e? What do those things mean? PROFESSOR: OK, the question is, are the equilibrium concentration of protein x is robust means it does not change in response to small changes in what quantities? So if I change the degradation rate, does it change equilibrium. If I change the beta. And I'm asking about this case here, perfect negative autoregulation, just so we can try to establish our intuition here. K is this repression threshold. None means that it's not robust to any of these things. DK always means "don't know."**

23

**I'll give you an extra 30 seconds. This might be--**

**So this one's the production rate. This one's the degradation rate. This figure might be useful to you.**

**AUDIENCE: Can you define K again? PROFESSOR: Yes, so K is the concentration of the protein x at which this super effective repression kicks in. So we're assuming perfect negative autoregulation. Beta is the rate of expression for low concentrations. The moment you get to concentration K, you get perfect repression and no more expression. Do you need more time? Question. AUDIENCE: By saying that x equilibrium is robust, so you mean that when you change these perimeters, x equilibrium stays exactly the same, or will x equlibrium-PROFESSOR: For now, what we'll mean right now is that a small change in this parameter leads to no change in x equilibrium. Now, for any real example, what we'll typically mean is 's going to be some sort of sensitivity analysis. For example, where you'll say oh, a 1% change in a parameter leads to a less than 1% change, for example. But in this case, there's going to be no change, I'll tell you, just so we can get the intuition clear here. All right, do you need more time? Let's go ahead and vote. Remember, you can vote for more than one thing if you like. Ready, three, two, one. All right, some people are using our more than one. And of course, I can give you a hint. The reason that I'm letting you vote more than once is because more than one thing is going to be-- All right, so the majority of the group has got this, but not everyone. So let's discuss. Can somebody give an explanation for why both alpha and beta are going to work here? AUDIENCE: So the equilibrium is basically when degradation involves production. PROFESSOR: I want to make sure I'm okay. The equilibrium is when the production rate is equal to the degradation rate. So this is a very important thing to make sure we're on top of. And in this case, we have very sharp-- this production. So then what happens?**

24

**AUDIENCE: Well, [INAUDIBLE] is the intersection of-PROFESSOR: Right, so in this case, what is the equilibrium concentration? AUDIENCE: K. PROFESSOR: It's equal to K. Now, I strongly encourage you, whenever possible, to draw things out. Because this is a problem that when you have the drawing. It's reasonable to do. And if you don't have the drawing, you're going to get yourself tied up into weird knots. And indeed, we can see that if we change alpha, what happens in this spot? Right, it changes the slope. And you can see that if we change the slope by small amounts, we get no change where this crossing point is. And even for a real system, if it came around, you'd see that it's going to end up being a less than proportional change in the equilibrium. And what about what about beta? That just raises and lowers this. And again, that doesn't change the equilibrium. Of course, if we changed K, then we get a 1 to 1 change. So a 10% change in K leads to a 10% change in the equilibrium concentration of x.**

**So this is the sense in which the equilibrium concentration in negative autoregulation is robust to changes in both-- in the book, they say oh, the production rate, but it's actually also in principle the degradation rate over some range. And this could be useful, because there are lots of things that are going to affect the production rate of a protein, and also the degradation rate, for that matter. The division rate, it changes it.**

**Whereas it may be that K is subjected to less severe changes, because that's determined by, for example, in the kinetics of binding of this protein to this promoter. And that is perhaps less subject to changes. It can still change depending upon the pH and so forth of the interior of the cell. But at least it's probably not subject to the big changes that alpha and beta are going to be a good experience.**

**So the argument that Uri makes for why it is we see so much negative**

25

**autoregulation in the cell is because it both increases the rate that the cell can respond to changes, in the on direction, at least, but also that it makes the concentration of protein more robust to changes in several of the parameters that govern the equilibrium . Concentration And once again, you could argue about which one of these is more important, but I think they're both likely playing a significant role in different cases.**

**I'm going to want to move on, but I will tell you that only over some range of these -- alpha, beta, K-- will this thing be robust. So for example, if this comes up too high, we're going to lose this phenomenon of robustness. So I expect you to be able to tell me in some later date the conditions in which that might happen.**

**And I'm available for the next half hour after class, so if you do not know what I'm talking about right there, please hang out with me after, and I'll tell you the solution to that question on the exam. OK? All right.**

**But I do want to talk about positive autoregulation, because this is another interesting beast. So if negative autoregulation has those nice properties, then you can imagine that positive autoregulation will have some drawbacks in the same kind of ways. But it leads to some other very interesting, just qualitative features.**

**Positive autoregulation. So we have some x that is activating itself. And often we think about cases where it's activating its own expression in a cooperative fashion. In particular, we might assume that x dot is equal to, for example, some beta 0 plus some beta one of some cooperative thing here where N might be 2 3 4 and then again minus alpha x. Right? Now, if you just look at this, you might think oh, I don't know what this is going to do and so forth. But you've got to draw things out. Once you draw it, then you'll see that it's pretty straightforward.**

**So again, this is the production and the degradation rates. So that's production. And degradation, for example, might look like this. So this is the production. This is the degradation. So that's the alpha x term.**

**One question would be, how many fixed points does this system have? So a fixed**

26

**point means that if you started right there, and in the absence of any noise, you would stay right there. So it's clearly both stable and unstable at these points.**

**Can you read that? I'll give you 15 seconds to count them.**

**Ready, three, two, one. All right, it seems like we have pretty good agreement. There are indeed 3 fixed points. Once again, the fixed point is where these curves cross. So we have one right here, one here, and one here,**

**Now, how many are stable? We're going to do this verbally. Ready, three, two, one. AUDIENCE: 2.**

- **PROFESSOR: 2. Let's try that again. Ready, three, two, one.**

**AUDIENCE: 2.**

**PROFESSOR: 2. Yeah, you get so used to the card, it's hard to speak. So they're the ones on the ends of the stable ones. And you see here that around this point, the production rate over here is more than the degradation rate. That means that if you leave that fixed point, you're going to get pushed away.**

**So it's very nice to draw these little arrows here to make one happy. So this thing here is stable, unstable, and again stable.**

**Now, the reason we call this bistability is because there are 2 stable fixed points. This is important because this phenomenon is the basic dynamical system's origin of memory. Now it's, not obvious how memory comes from this.**

**So memory is a generalist idea that the g-network or the cell can retain a memory of its past state. And we're going to see examples of this over the next few weeks. But just to be clear, if, for example, we imagine a situation where the alpha changes. And it could be division rate, for example, high-food, low-food environments.**

**What we do is we can plot-- Often, you can plot, for example, the equilibrium, but that's a little bit trickier. So I'm just going to plot the production rate as a function of**

27

**alpha. Now, the question is, if we change alpha, what's going to happen? Now, for a fixed alpha, you can see already that there are two different production rates that are stable in this case.**

**But what happens if we increase alpha? So we increase the growth rate so it goes like this. Can that change the number of fixed points?**

**And indeed, what we can see is that as this line gets steeper here, eventually you only have a single fixed point, and it's stable. And that's known as a bifurcation of the dynamics of the system. So this is for large alpha, you end up-- And just to be clear, this is beta 0 down here. And then up here is the beta 1.**

**So what we do is we know that beta 0 is where we get for large alpha. Now, for small alpha, do we end up getting another-- We get another bifurcation. So actually, there's only again one stable point up here at small alpha. And what we're going to get is what's known as a full bifurcation where solid lines denote stable points, stable fixed points. Dashed lines represent unstable fixed points. So stable, and the dash is unstable. There are some regions of alpha conditions where the system is bistable. But then outside of that, it's just monostable.**

**Can somebody explain why this thing-- why I might make the argument that this thing displays memory? Well, one of those two is fine, but any new people want to explain my thought process? No. All right, maybe you.**

**AUDIENCE: All right, well depending on whether we had high degradation or low degradation rates in the past, we'll be on the lower or the upper range of that if we return to normal.**

**PROFESSOR: That's right. So the argument here is that-- let's say that this is some normal condition. This is where you are right now, for example. Now, depending upon whether you're sitting here or here, that's perhaps giving some information about the past state of the cell. Because if you were here, that means oh, maybe in the past you were out at high degradation rates, whereas if you're here, maybe were at low.**

28

**In particular, you could reset things. If you start here, then you can reset this memory module by coming over here. Once you get to this point here, that's the bifurcation dynamics, the full bifurcation. Then you come up here, and now you'll retain this state. In principle, until you get over here. Of course, there could be stochastic switching dynamics. We're going to talk a lot about that in the coming weeks. But at least in the limit of a low rates of stochastic switching, then this represents some sort of memory module, the simplest version of it.**

**I'd say that in the cell, most examples of such memory modules involve not just positive feedback of one protein activating itself, although this happens, but often through a whole network, where the one protein activates another, activates another, and then you come back. Or it could be repressing, repressing. 2 0's, is a po-- two negatives is a positive. Just like two lefts is a right.**

**Right, so are there any questions about the sense in which this thing can serve as a basic memory module?**

**And this is maybe not the most interesting example of it, because alpha is such a global parameter. But you can also get similar dynamics as a function of, for example, the galactose in the concentration of some sugar in your media.**

**So given that different small molecules such as food sources can act as inputs into these g-networks, you can also get these sorts of dynamics as a function of what you might call really some simple, external molecule, which is nice, because that means that you can have memory modules that are really independent of all the other memory modules that are going on in your cell. Whereas if you had a vary alpha, then this changes everything. Whereas if it's just a concentration of some sugar outside, then you can imagine that that could be very useful to retain a memory of what the cell has encountered in the past.**

**So today, what we've been able to do is analyze something about a possible evolutionary explanation for why autoregulation is as commonly observed as is. So negative autoregulation is the one that's observed perhaps most frequently. And that, I think, has some very clear purposes.**

29

**And this idea of the concentration being robust to other biochemical parameters I think is a big idea. We're going to see this idea of robustness crop up multiple times over the course of this semester. And I think that it's nice to think about robustness in this case, because it's perhaps the simplest example of how robustness as an approach can be useful as a way of thinking about a problem.**

**We're later going to be thinking about robustness in the context of perfect adaptation in chemotaxis, where bacteria try to find food. And there, I think everything's more subtle, because already the base phenomenon that is robust is a form of robustness. And so it kind of gets you mixed up. So I think that it's good to be very clear about what robustness means here, so that we can use that to think about robustness in other biological functions.**

**With that, have a good weekend. Good luck on the problem set, and I'll see you on Tuesday.**

30

---

[← Yes.](04-yes.md) · [Up: contents](index.md)
