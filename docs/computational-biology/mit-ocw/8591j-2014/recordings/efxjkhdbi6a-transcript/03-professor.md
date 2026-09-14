---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/efxjkhdbi6a-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/efxjkhdbi6a-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Were they trying to minimize the parameter numbers?**

**Right. OK, so in this case, they wanted to compare these three distributions. Each of them were specified by two parameters. You could come up with other underlying distributions that might, for example, have a larger number that might be specified by a larger number parameters. But then, it's harder to compare the quality of the fit and so forth.**

**So they chose these three distributions just because this is, somehow, the rate that these new mutations will appear in the population. And then, this tells us something about how good those mutations are. Right. Now some of you have the paper in front of you. And that's OK.**

**But based on our understanding of how the clonal interference, kind of, manifests itself in terms of leading, eventually, they have the log of the fraction. So the fraction starts out 50-50. Log F1 over F2. So like, cyan and yellow, say?**

**All right. So this thing starts out here. And then, one side gets beneficial mutation. So it, kind of, comes up. So they measure the slope, for example, of the lineage that is taking over the population. So they want to know, well, which of these distributions and associated parameters will be able to explain the range of different trajectories that they saw?**

**So the question is, can we order these things? And why? All right, which one of these should be the largest, second largest, third largest, and so forth? OK. Now it's OK if you just-- well, if you had the paper in front of you, you could just read it off. But ultimately, you're going to have to be able to explain why it is that one is larger than the other. OK?**

3

**So what I want to know is, for example, at what order should these things come in? All right. So what I want to do is let you think about it for a minute. And then, we're going to vote by putting our cards from high mutation rate to low mutation rate among a, b, and c. Yes?**

**AUDIENCE: So the means are constrained to be the same?**

**PROFESSOR: So it's really going to be some range of parameters on each of these. So the question is, why is it that in the range of parameters that are consistent with what they observe experimentally, that these things have some order? Are there any other questions about the question?**

**I'll give you 30 seconds to think about what the mutation rate should, kind of, be in this situation.**

**AUDIENCE: The answer is highest to lowest mutation rate.**

**PROFESSOR: Right. So you're going to put the highest mutation rate up high, the lowest mutation rate down there, and the middle one in between. Yeah. All right. Do you need more time? All right, let's see where we are.**

**And it's OK if you're confused or don't know what I'm trying to ask. But let me see where the group is. Ready? Three, two, one. All right. So I would say it's, pretty much, all over the place, whether people are voting something in reality or not.**

**OK, right. So the situation is that we have the data, which is shown in figure 3A, which is a bunch of these things that, kind of, look like this. All right. So we have some times. We have some slopes. We want to know how can we understand that data that we get out.**

**So what we're going to do is we're going to take a model in which we say, all right, we're going to start with this population that's all identical. And then, we're going to allow some mutations to accumulate. And we're going to let them compete against each other. And then, see what happens to the other. So there's going to be some, again, distribution of slopes and so forth.**

4

**All right. To what degree does this sort of data constrain that underlying distribution? Between something that looks like an exponential, something that has a uniform distribution, and something that is a delta function. So that's the exponential. This is the delta. And this is the uniform. Yeah.**

**AUDIENCE: So we measure the slope at what time [INAUDIBLE]?**

**PROFESSOR: Yeah, it could. That's right. So this thing could turn around at various times. So I think that there are a number of different ways that you could argue about the right way to do this. In practice, I think it's not going to be very sensitive because there's a minority of them that will actually be turning around, for example.**

**So you could, for example, just say all of the trajectories that cross some point, I mean, measure the slope. And I think that would be sufficient.**

**AUDIENCE: But if you don't see this fraction turn over, you could still have clonal interference?**

**PROFESSOR: If you don't see the fraction.**

**AUDIENCE: Like, in the sense--**

**PROFESSOR: That's right. So even if you don't see these things like, the flatten out, for example, then you could still have clonal interference because the slope might still be steeper than it would be in the absence of clonal interference.**

**All right, what I'm going to do is I'm going to let you discuss with a neighbor for one minute. And then, we'll, maybe, discuss as a group just because I want to make sure that everybody gets a chance to try and verbalize their thought process. And if we discuss in a group, then only a few of us get to. All right, so one minute. Try to discuss it with your neighbor. And then we'll reconvene.**

**[SIDE CONVERSATIONS]**

**Yeah, and we're going to discuss the means in a moment. So indeed, these distributions will not end up having the same mean s.**

5

**AUDIENCE: What are you controlling? PROFESSOR: What we're controlling is that we're asking about what range of parameters for each distribution will adequately fit the data. AUDIENCE: I know [INAUDIBLE]. Does it depend on what you get? PROFESSOR: The data will be, basically, the initial slopes here and when they deviated from a 5050 mixture. AUDIENCE: OK. PROFESSOR: All right, so that's what [INAUDIBLE] is those histograms. AUDIENCE: Yeah. OK. [INAUDIBLE]. PROFESSOR: All right, so it seems like we've quieted down, which means that we all agree on the answer. Is that-- no? OK, well I think that this is, actually, pretty tricky. So that's fine. I just want to see where we are, though. All right. Reconfigure your cards. Your best guess for the orders of the mutation rates between exponential uniform and delta. All right, ready? Three, two, one. OK, so we're migrating towards some things. OK, great. And can somebody verbalize the answer that their group got? AUDIENCE: So our answer is A, B, and C. PROFESSOR: OK. AUDIENCE: [INAUDIBLE] exponential [INAUDIBLE]. We can not see most of the [INAUDIBLE] lower selection coefficient mutations. PROFESSOR: OK. AUDIENCE: So we're actually underestimating the mutation rate from the data. PROFESSOR: Underestimate. OK, no, I can see what you're saying. OK, yeah, so the idea is that you're saying that we don't see an awful lot of the mutations here, which means that**

6

**the true mutation rate, the underlying mutation rate is, somehow, much larger than you would have thought based on the mutations that you actually see here or something.**

**And there's maybe another. OK, so they're different. All right. OK, it's certainly along-- yeah, sometimes it's true. And then, of course, there are different ways of saying this. Yes?**

- **AUDIENCE: Yeah, same answer but a slightly different way of thinking about it. If you're just randomly sampling any of these distributions, then your sample drawn from the exponential distribution. It's going to be low selection [INAUDIBLE] more often than it's going to be for the other ones. Like the delta is [INAUDIBLE].**

**PROFESSOR: That's right. Yeah, yeah, yeah.**

**AUDIENCE: [INAUDIBLE] every time the uniform. It's going to be equally likely to be a high selection coefficient as opposed to a low selection coefficient. But with the exponential distributions, your most likely to be a low selection coefficient. So you want more mutations.**

- **PROFESSOR: That's right. You, somehow, need more mutations of that exponential in order to sample out there. Right? So which one is going to have a more clonal interference? Which of these distributions will end up having the most clonal interference after you fit the data? Yeah?**

**AUDIENCE: The one with the highest mutation.**

**PROFESSOR: The one with the highest mutation, right? Kind of has to. Of course, and even though some of those mutations are going to be loss, still it's going to have the most colonel interference there. And indeed, if the underlying distribution were modeling as a delta function and, in their [? fit ?], what they got was that this might be around 5 and 1/2%, I think.**

**Yeah, so [? 5 to 5 and 1/2 ?]. OK. So here, this guy was around 0.055. Between 5 and 5 and 1/2%. So what they're saying is, all right, well you could explain all of our**

7

**data just by assuming that there's some mutation rate where, periodically, some individual gets a beneficial mutation that is a 5, 5 and 1/2%.**

**And that could, in principle, be used to explain the base features here, how long have to wait before anything happens, and the slope when something starts happening. So the histogram that they plot is actually, somehow, this initial this initial slope once you start seeing it deviate from 50/50. OK? All right.**

**But their point is it that that does not prove that the underlying distribution is a delta function with some mutation. And indeed, to explain the data with a delta function, you don't actually don't need any clonal interference. Right? You just say, OK, well somebody gets a mutation. It's 5%. And eventually, it's going to spread. And that's what we see.**

**If you want to explain the later dynamics of flattening out and so forth, then you have to allow the other lineage to get a mutations, as well to cause a flattening. But as far as the base dynamics of when you leave the 50-50 in the initial slope, you don't even really need to have any clonal interference to explain their data with a delta function underlined. And that's why you also can get by with a very low mutation rate because you don't really need much in the way of competing lineages. Yeah?**

**AUDIENCE: But what if the slopes are [INAUDIBLE]?**

**PROFESSOR: Yeah, yeah. No, right. So you're not actually going to get the true distribution of slopes. But their argument is that a lot of that could just be noise and measuring the slopes and so forth because, if everything is a delta function, then you would start out by just getting one slope, unless you offer multiple mutations on a lineage.**

**And then, things could get more complicated. But yeah. In this case, all of these guys would have the same slope. But that's, at least, a reasonable first order approximation to the data. However, as you move to these distributions in uniform and exponential, you're going to need more and more clonal interference to, kind of, explain the data. So you'll need higher and higher mutation rate. What's interesting**

8

**is that you also have a lower and lower mean s. OK?**

**AUDIENCE: Can you just explain why you need to explain the data?**

- **PROFESSOR: Yeah, sure. And I think that drawing these underlying distributions is really helpful. So first, we're going to draw the delta function. That, kind of, makes sense that you can fit everything just by assuming 5, 5 and 1/2%, right.**

**So what we're going to do is draw the various P. So I drew those distributions. But they weren't necessarily to scale. i.e, they didn't necessarily have the proper mean selection coefficient. What we can do here is we can draw this is the mean s of the delta function, which was 5, 5 and 1/2%. All right, we got this guy here.**

**Now the question is can we describe the data using a uniform distribution with the same mean selection coefficient? All right, so we're going to have you vote yes and no. And if you say no, then you have to say what's going to go wrong. All right? The question is can we just use the same mean selection coefficient for our uniform distribution.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Right. So what we're going to do is we're going to measure the experiment where we would have, say, 96 different evolutionary trajectories where we measure the time that it takes for something to happen and then the initial slope. And we're going to take a histogram of those things, and compare it between what we would get in the model with what we got experimentally.**

**All right, the question is can we use the same mean s for a uniform as we did for the delta function. And if you say no, you have to say why not. A is yes. B is no. Ready? Three, two, one.**

**All right, so we have a bunch of no's. Maybe a few yes's. All right but then some of the no's, it's incumbent on you [INAUDIBLE]. So I don't know. So yes, so one of the no's, why not?**

**AUDIENCE: So if we have [INAUDIBLE] if it has the same average, then there are going to be**

9

---

[← AUDIENCE](02-audience.md) · [Up: contents](index.md) · [outliers that are more better for the [INAUDIBLE]. →](04-outliers-that-are-more-better-for-the-inaudible.md)
