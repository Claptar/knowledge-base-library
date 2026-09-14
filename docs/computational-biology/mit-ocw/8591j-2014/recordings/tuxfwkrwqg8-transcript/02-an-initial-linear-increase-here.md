---
title: an initial linear increase here.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/tuxfwkrwqg8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# an initial linear increase here.

**Source:** `recordings/tuxfwkrwqg8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: But I guess my question is sort of, how can we get that 50% of 1%? Is there a central calculation that you can do to get that, or [INAUDIBLE]?**

**PROFESSOR: Oh no, we can do it. Because actually, I think that the most straightforward way to do this is to ask, what is the absorbing rate of a little patch, let's say a circular patch? And we already figured out that when-- so these are very related problems, as you can kind of see. I just don't remember whether it's 2 pi or if it's 4 pi for that particular problem.**

**Because this is some uptake of a patch, we'll say. It's going to be either 1, 2 or 4 pi Dca. But there's some uptake rate from each patch. But then that means just that the uptake total for small numbers is indeed just going to be equal to the number of patches or transporters times the uptake rate of each one. Because they're just not competing against each other. And the striking thing is that because of this difference in scaling between the radius and the area, this can give you a lot of uptake rate while only occupying a small fraction of the area. This is a fraction of area covered. Do you see why that ends up being the case? Yes.**

**AUDIENCE: So that's also saying that [INAUDIBLE] pretty soon.**

**PROFESSOR: Well, it depends on what you mean by soon. I mean, it's soon on the scale of the amount of area. But it could be that you can have 1,000 of them or so, right? So the way I would think about it is that you don't have to cover up very much of the cell surface in order to get really good uptake kinetics.**

**Now, these are some, say, fundamental limits to the way that bacteria, for example, and other cells can uptake food and other nutrients. But from the standpoint of trying to find where the nutrients are better, what you need to be able to do is you need to be able to measure the concentration.**

**Now, the basic way that you could, for example, measure a concentration of**

14

**something, the best that you could do, is if you're a perfect absorber, you uptake molecules at this rate. And then you count the number of molecules that you uptake over some time t. Indeed, the number that you uptake over some time t will just be given by this.**

**What will be the distribution of these numbers? I should just have somewhere up on the side always a bunch of probability distributions that we can vote on. But think about it for a moment, and then we'll vote. All right, ready? Three, two, one.**

**What is going to be the probability distribution of the number of these things absorbed over some time? Right, it's going to be distributed Poisson. What is going to be the distribution of times between successive absorption events? Ready? Three, two, one. All right, yeah, that is going to end up being exponential.**

**And this is all confusing. So this is a Poisson process. These things are occurring at random times, at some rate. And if you have such a process that's random, and you ask, how many events over some time t, that is the definition of a Poisson.**

**If this is a large number, then the probability distribution is going to look like something else. What is it going to look like? Ready, three, two, one. Most people are trying to find the D, the central limit theorem there.**

**What is going to determine the resolution of that measurement that we make? So in some ways, what you would like to know is, well, what's the standard deviation in your measurement of the concentration divided by the concentration? So this is maybe a fractional error in your measurement of the concentration.**

**Do you guys understand why this is the error in the measurement? Well, this actually will go as the standard deviation in our measurement of the number divided by the number that we measure. What's going to be the standard deviation of this number?**

**AUDIENCE: The scale--**

**PROFESSOR: What's that?**

15

**AUDIENCE: [INAUDIBLE] PROFESSOR: The mean, yeah, so it's close to-AUDIENCE: [INAUDIBLE] PROFESSOR: Yeah, it's the square root of the mean number. What that means is that this thing is going to be the square root of a 4 pi cDaT. And this is just 4 pi cDaT. The number that you measure here, the number that you uptake over some time period t, that's going to be distributed as a Poisson. And in a Poisson, the variance is equal to the mean, which means the standard deviation, which is the square root of the variance. It's going to be this. Yes.**

**AUDIENCE: I'm not understanding the first step where you changed the c [INAUDIBLE]. PROFESSOR: Right, so from the standpoint of the cell, what the cell is doing is it's counting the number of these things that have come. And it's true that from that number of, say, molecules that are absorbed, to get a concentration of units of number per cubic micron and whatnot, the cell would need to know kind of how big it is, what the diffusion coefficient is, and so forth. But in terms of the fractional error, those all end up disappearing. Because the fractional error is telling us, well, if this time I measure it, and I get 10, and next time I measure it I get 20, then this is telling us about how much error. This is indeed just the fractional error in our measurement of the concentration, and irrespective of whether the cell is able to estimate the concentration units of a physical quantity. Because that sort of error would scale together. I'm worried that I'm not helping you, though. AUDIENCE: So you're kind of saying because c and n are linearly related, any proportionality factors would cancel out. PROFESSOR: Yeah. AUDIENCE: Would I be right to think that since n is distributed as a Poisson, so is c?**

16

- **PROFESSOR: Yeah, our estimate of c would be-- because ultimately, what the cell would do is it would measure some number. And then it would say, all right, well, I multiply by all these things. And then that results in an error in c that is distributed in the same way as the error in n. But they're kind of proportional to each other.**

- **AUDIENCE: What has me confused is I'm thinking that c is Poisson distributed, and then our original ratio that we want, sigma of c over c, should be 1 over square root of c, because c is Poisson itself. But then that's different from what we got.**

- **PROFESSOR: Sure, OK, I think we have to be careful. So it's not that the c is actually Poisson distributed. Because it's really that you take a Poisson distribution and multiply it by something to get an estimate of c. But if you take a Poisson distribution and you multiply the numbers by 10, then it's no longer a Poisson distribution.**

**Because the mean goes up by 10, but the variance goes up by 100. So then the variance no longer equals the mean, so it's not a Poisson anymore. So you can't just multiply a number times a Poisson to get--**

**AUDIENCE: All right, thanks.**

**PROFESSOR: And this expression kind of makes sense in that the longer that the cell measures, the less error there is. If there's more diffusion or higher concentration-- less error. And this is really in some ways some estimate of the best the cell could do. And surprisingly, cells can get close to this.**

**Now, this is a measurement of the concentration for a perfectly absorbing sphere as a cell. Now, you might ask, well, how would our error change if instead of absorbing the molecules we simply had a detector? So they just asked, OK, each time that a molecule bounces against my cell, I count one? Do you understand the difference?**

**So this is for a perfect absorber. So what about a perfect monitor? And the question there is, does a perfect monitor do better or worse than a perfect detector? So we'll say, better, worse, or no change.**

17

**And it's of course not possible for you to actually do this calculation. But it's useful to imagine the situation and make your best guess-- better, worse, and same. I'll give you 5, 10 seconds to think about it. Because it's interesting to imagine the situation. All right, let's see where we are-- ready, three, two, one. Oh, we have a fair range of answers.**

**All right, I think everybody agrees it's going to do something. Because it would be kind of a coincidence if it didn't change things. Can I get somebody to volunteer what their neighbor is thinking? I know you didn't actually talk to your neighbor yet. But you can still invoke that. Yes.**

- **AUDIENCE: So I don't know about this so much. But the first thing I was thinking is that maybe this monitor might be encountered on at a different rate proportional to its area. It seemed like it wouldn't change the concentration gradient, because it wouldn't be subtracting any. And so then things would bounce off of it, and that would be proportional to its area.**

- **PROFESSOR: OK, that's interesting. So you're arguing for a different scaling. And then it would actually be either-- depending on the area, then it would be different.**

- **AUDIENCE: Yeah, so that seemed weird to me, which is why I wanted to just check where other people were on that.**

- **PROFESSOR: Yeah, no, that's fair. That's fair. In the end, the scaling is the same. Although this is very complicated, confusing. Can I hear somebody else argue for one or the other? Because he actually argued for both.**

- **AUDIENCE: I just thought if it's not taking up the molecules, then it could bounce against the same molecule several times.**

**PROFESSOR: Yeah, and therefore, so which one are you arguing for?**

**AUDIENCE: For worse.**

**PROFESSOR: Yeah, for worse, OK. Yeah, and indeed, it does end up being worse. And it's actually significantly worse. It's something like 10 times worse. And I think the**

18

**intuitive explanation is indeed what you just said, that a perfect monitor, that's great. Except for the fact that it's counting every time that something hits. But then it doesn't know if it already counted that molecule or not. So then there's extra uncertainty that results from that. Of course, ultimately, you have to go and do the calculation if you want to be convinced of something like this. But indeed, the perfect absorber is the best that you can possibly do.**

**AUDIENCE: Unless it tagged the molecule [INAUDIBLE]. PROFESSOR: That's right. Right, so that's equivalent to being a perfect absorber, right? AUDIENCE: Oh, OK. Well, no, because then-- oh. PROFESSOR: Yeah, because these are non-interacting molecules. So if you tag it green, then all that you do is when the green molecule comes back, you say, I'm going to ignore that. But then that's equivalent to if you had just absorbed it.**

**AUDIENCE: But there's no local depletion.**

**PROFESSOR: Yeah, there's no local depletion. But because these are all non-interacting particles, then it can't make a difference. And I agree that this is confusing. But I'm pretty confident what I said is true. Because since they're all non-interacting, there's just no more information there. Yeah.**

**AUDIENCE: So what exactly is the error? PROFESSOR: Right, OK, this is asking, over some period of time, I count the number of molecules that hit me or that I absorb, and then I say, OK, well, I think that I counted 20. And the question is really, well, if I did this again, how close to 20 would I get? Would I get, again, 20 or 21, or would I next time get 10 or 50? And that's the real question. How repeatable are my measurements?**

**So if I plot a histogram of a bunch of numbers that I get over this time-- this is the frequency that I observe a particular number of molecules over some period of time t. I get some histogram. And this is telling us about the width of that histogram**

19

**relative to the mean.**

**Now let's imagine that you're the cell, and you calculated the concentration in a really wonderful way. Now, the question is, do you know where you should go to get more food? No, right? So you know the concentration at your location. But what you need to know for that purpose is a gradient.**

**And I'm trying to remember, in this paper, they maybe are not very explicit. Why is it that a bacterial cell might do this biased random walk that's described in the paper instead of just measure the gradient? Yeah.**

**AUDIENCE: Because cell size is so small.**

**PROFESSOR: Yeah, so bacteria are just small, I think this is the argument that we often give. And that's just saying that if you want to measure a gradient, then what you would do is, if you have a sphere like this, you might say, OK, I'm going to count the number of the molecules that hit me over here, and I'm going to compare that to the number of molecules that hit me over there.**

**So you get two measurements of concentration. But then in order to get a gradient, what's relevant is you have to look at this distance. And of course if you have a bigger cell, then a given gradient shows up as a larger difference in concentration, or a large difference in the number of molecules that are going to hit the cell. And does that scale linearly or quadratically with a?**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [AUDIENCE →](03-audience.md)
