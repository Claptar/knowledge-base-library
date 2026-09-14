---
title: '[INTERPOSING VOICES].'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/9ygxpwvwydy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [INTERPOSING VOICES].

**Source:** `recordings/9ygxpwvwydy-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- **PROFESSOR: All right, yeah. OK, but I think you're arguing for something already maybe. But let's just say that this was a-- I mean, let's just for concreteness let's say that I measured at 15 values of x. I have some error bars and some error.**

**But then I needed three parameters to characterize this curve. And so those I used to fit. Are you happier with three fitting parameters and 15 measurements? All right, let's just see where we are. OK, ready, 3, 2, 1.**

13

**OK, so we have a majority of A but a significant minority of B. So just to be a lot more concrete, can somebody say why they're saying yes? Yeah.**

**AUDIENCE: I guess intuitively, [INAUDIBLE] we try to optimize the number of error bars that go through.**

**PROFESSOR: Yeah, so the fit is somehow trying to get the curve to go near the error bars. And typically when we do a fit, we're typically trying to minimize this mean squared error or deviation from our curve to the data point.**

**How much you expect this to make a difference? So for concreteness again, let's say that I had 15 values of x that I was measuring things at. Now, we expect say five of them-- five will miss true curve, we decided roughly.**

**Now the question is, what happens if we, instead of having this true curve, if we do a fit using these three parameters? How much of a difference should it make to this very, very roughly?**

**We'll see-- Now, I'm asking roughly how many of these error bars do you expect to then miss the fitted curve? And this is we used three fitting parameters, say. That was parameters over there.**

**Do understand the question? So instead of plotting this god-given curve, instead we're plotting a curve that I'm giving you, where I use three fitting parameters to fit to the data.**

**And I'm just trying to get it roughly. I think that this is not a rigorous statement I'm about to make, but just so that we're all roughly on the same page. All right, ready, 3, 2, 1.**

**Right, so it'll be somewhere in here. And I think this is not quite true. But the idea is that, in particular, if you make n measurements and then you use n fitting parameters, in general you will get a perfect fit, i.e. the curve will go through every single data point amazingly perfectly.**

14

**So if I give you 15 measurements across here and then I give you a 15-degree polynomial-- I guess, we only need a 14-degree polynomial with 15 free parameters-- then that polynomial will go through everyone of your data points spot on, not even a question of whether it goes through the error bars. I'm saying literally-- and that's just because you're just solving an equation at that stage.**

**Now, this is a stupid statement, except that once you're kind of like in the heat of the moment, eagerly trying to do some fitting for your advisor or whatever, it's easy to fall into this trap, where you just kind of like add extra parameters.**

**I mean, I definitely remember in graduate school, I was surprised. I was like, oh, this thing, it works wonderfully. It's like it seems to magically goes through all my data. And then I felt very stupid like 30 seconds later. But this is just a very easy thing to screw up and forget about.**

**So what this is saying is that, if you see a curve-- if in the course of your work or if you're reading a paper and you see some curve and you want to know something about how much information is it or whether things look reasonable given the data, it's useful to kind of orient yourself relative to these statements, that depending on how many free parameters you're kind of using, you expect a larger or smaller number of these data points to kind of go through the curve that you see.**

**But I would just want to stress that you don't want to be anywhere close to the point where you have a number of parameters equal to the number of kind of measurements that you're making.**

**And for any sort of reasonable curve describing what you hope is a reality, you expect some of those data points with their error bars to kind of miss the curve. And that doesn't mean that they're sloppy experimentalists. It doesn't mean whatever.**

**OK, now coming back to the task at hand, do you understand why they're plotting the standard error of the mean rather than the standard deviation?**

**Because what your interest in, in principle, is not-- the question you're trying to answer is not how variable are their measurements but to what certainty can they**

15

**claim to know the actual god-given, real cost associated with expressing these proteins as a function of the expression level. And for that, you really want to ask about the standard error of the mean.**

**Great. So now, we can come back and ask about, why did I just spend half an hour talking about standard error of the mean, standard deviations, fitting to data? Well, you guys are probably all asking yourself that question. But does anybody have an answer if I-- Yeah.**

**AUDIENCE: You can fit with different curves if you use different things.**

**PROFESSOR: You can fit with different curves if you-- yeah, I think that that's hard to argue that statement. But the statement is a little bit like "different proteins have different expression levels," but a little bit more concrete maybe. Yeah.**

**AUDIENCE: So in this case, I didn't check their calculations, but if you have a natural line, then you can't make this calculation of optimization.**

**PROFESSOR: Yeah, but I think that-- right, so--**

**AUDIENCE: In the sense that there won't be [INAUDIBLE].**

**PROFESSOR: Yeah, OK. So I think that this is a tricky thing. The data certainly do argue for a super linear cost. But I would say that they argued for it rather weakly, in that if you look at their data and you just fit a line, you would say, it's maybe OK.**

**And of course, once again, should we be surprised that the quadratic fits better? No. And this is a very dangerous thing, if you're comparing models. It'll always be the case, if you add another parameter, it will look better.**

**But the question then is how strong of a case should we make of this? And then how important is it for the conclusions of the study? Now, in addition to the line and the quadratic, they had another curve in here, which looks like-- let me see if I can get it right for you guys. So this is fine, tricky thing. So it's the dashed line that looks very similar to the solid quadratic line.**

16

**Can somebody remind us what the difference was between those two non-linear curves that they had? Why do they have two curves that look so similar?**

**AUDIENCE: I think the dashed line responds to some model where there's only so much of this certain resource that-PROFESSOR: Right, OK, so my dashed line is their red line, just to-- OK dashed red in the paper. So it's this line where there's a finite amount of resources or protein-making machinery that the cell has. And if you use them up, then you don't get any growth. And of course, that statement kind of has to be true on some level. And the question is whether--**

**AUDIENCE: --that scale is-PROFESSOR: --it's relevant here, right. Certainly, I would say that one question is whether you can reject the hypothesis that this cost function is a line. Another question is whether you can distinguish between the two quadratic or the two non-linear curves based on the data. And I think the answer to the second question is certainly not. And they don't claim that they can. But it's important to just note that it's just impossible for them to assume-- I mean, those curves are so, so similar over the entire range where they have data that it's going to be possible to distinguish those two things. But does it matter which of the two cost functions is the true cost function? Yeah. AUDIENCE: Is it because the [INAUDIBLE] where the marginal benefits become zero is like inside the range where the cost functions are still exactly the same? PROFESSOR: OK, right. So what you're saying is that the two cost functions they have they behave similarly over the range that is relevant maybe, so then therefore, it doesn't matter. Is that-- or am I-- OK.**

**So why do they have to cost functions there then, why two non-linear cost**

17

**functions? Just to provide variety in our modeling? Yep. AUDIENCE: They were doing another experiment later on, and they said something like something was saturated and that was modeled by the second cost function. PROFESSOR: Right, yes. That's right. And what's the later experiment they're going to do, just so that we're-AUDIENCE: You should ask somebody else to explain that, not me. PROFESSOR: You regret opening your mouth. No, OK. So yeah, so what is the experiment that they're going to do? AUDIENCE: Measuring the benefit? PROFESSOR: So next, they're going to measure the benefit. But this question about the two cost functions is not somehow relevant yet for the benefit part. Yes. AUDIENCE: So they're doing it in different concentrations of lactose and seeing if the protein expression could adapt [INAUDIBLE]. PROFESSOR: Right, after a long time. So they actually do laboratory evolution experiments, where they grow these bacterial populations in different lactose concentrations. And then they look to see what level of the lac operon expression does the population evolve to.**

**So what they're trying to do here is they're trying to say, OK, well, we can measure some cost as a function of expression. Maybe we can measure some benefits as a function of expression. And then from that, we'd like to be able to predict where the population will evolve to.**

**And they had these two non-linear cost functions, which based on the data they have, they can't distinguish. But they say, oh, well, they're both kind of reasonable cost functions.**

**And in some ways, maybe the problem here is that the two costs functions end up**

18

**being wildly different in terms of predicting what happens for large lac concentrations, where you would want to express more of the protein.**

**Do you guys-- do you remember this or not? Sort of. And that's actually-- well, you might as well just look at that. So that's figure 4.**

**That's the normalized lacZ activity that the populations evolve to as a function of the lactose concentration they're evolving in. And what you see is that this red curve corresponding to the finite resources cost function, it explains the data. Whereas, the other ones very much do not.**

**And that's just because these other models then would predict that if you grow the cells in a lot of lactose they should express out to five times the lac expression, much, much, much more, which is not what they see experimentally. Yes.**

**AUDIENCE: Is there another way to put a bound on the expression, because of this expression we have? You mentioned for that promoter, it's not possible to--**

**PROFESSOR: OK, but the idea of evolution is that evolution can make it a stronger promoter. So you guys, one statement is, given this DNA sequence at that promoter, how much expression can you get? And the most you can get is this amount that's normalized to 1. But if you make mutations in that promoter, then you could go out further.**

**So the question now is, after we kind of tell you the results of these evolution experiments, how much should that favor this dashed red line, this super linear cost function with finite resources? And on one level, you'd say, oh, well, that's pretty compelling.**

**On another level, later people that have come and measured this find that it's basically a line. So are there any questions? So it seems to basically be not true within this range. It is the case that if you go out far enough, then the growth does go to 0. But that's much further out. Yes.**

**AUDIENCE: After they-- on the experiment, they had [INAUDIBLE] expression protein at the [INAUDIBLE] level. Why didn't they go back and do the experiment again, just to see**

19

---

[← [LAUGHTER]](03-laughter.md) · [Up: contents](index.md) · [[INAUDIBLE]? →](05-inaudible.md)
