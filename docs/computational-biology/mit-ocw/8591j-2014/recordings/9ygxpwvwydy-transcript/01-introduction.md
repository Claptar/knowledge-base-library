---
title: Introduction
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/9ygxpwvwydy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/9ygxpwvwydy-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=9yGxpWVWYDY**

**The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: So today, our goal is to really go through this the paper that you read maybe last night by Dekel and Alon "Optimality and Evolutionary Tuning of the Expression Level of a Protein." It was published in Nature in 2005. I think that it's a very interesting paper, exploring some kind of big general ideas.**

**I think it's also, in some ways, rather misleading. And we'll try to understand or discuss the ways in which the connections between experiment, theory, prediction, and so forth, how they all play out in the context of this problem.**

**Before we get going too much on the science, I just want to remind everyone that Andrew will not be having office hours today. He is off interviewing for MD, PhD programs right now. But if you had questions about the problems, I hope that you asked [? Sarab ?] last night.**

**You might be able to grab him after the lecture today, but yes. Any other questions about anything before we get going? No.**

**So I think that this paper in general, I guess, the lecture today is really a combination of trying to start thinking about maybe laboratory evolution or kind of population level phenomena in general, as well as this question of optimization in terms of protein expression.**

**So can somebody just maybe summarize the big idea of this paper? Yes, please.**

**AUDIENCE: Protein expression levels evolve to optimal values for cost-benefit questions.**

**PROFESSOR: Right, so that's the argument at least. And they have a very nice first sentence here. "Different proteins have different expression levels." You know, it's hard to argue with that statement, nice, concise. But the question is, well, why?**

1

**And I'd say that there is a range, different philosophical opinions out in the world. I said that some group that is very much reflected in this study is trying to think about this in the context of optimization.**

**Well, maybe the reason that we see a given level of expression of some protein is because, at least over evolutionary time, in some ancestral environment that we don't know, but maybe it evolved to optimize some cost-benefit problem.**

**And then I'd say that there's another kind of general philosophical approach that tends to be a little bit more agnostic or just maybe more of a sense that certainly things could have evolved to optimize something. But we can never really know where they evolved in, so we shouldn't be going out on a limb on these things.**

**And given that this is philosophy, I will maybe not require that you agree with any particular standpoint. But I will say that it's at least worth thinking about the question and maybe you can do measurements to illuminate whether all these ideas might make sense.**

**And then we'll try to, over the next hour and a half, figure out to what degree this paper maybe should convince us of this optimization in the context of this particular protein.**

**Now, even if it's the case that somebody convinces you maybe that expression of the lac operon maybe does optimize some cost-benefit analysis. That does not prove that every protein optimize things. So don't get overwhelmed or underwhelmed or whatever it might be.**

**Let's just first make sure that we understand what we mean by costs and benefits in this case. Can somebody pick one of them? Now, what is a cost and benefit in the context of maybe this paper? Yes.**

**AUDIENCE: Producing protein requires some kind of resource.**

**PROFESSOR: Right, requires--**

2

|**AUDIENCE:**|**[INAUDIBLE] energy--**|
|---|---|
|**PROFESSOR:**|**--requires resources of some sort or another to express these proteins. And this can**<br>**manifest in many different ways. But certainly, if you were not making these**<br>**proteins, you could have been making some other proteins. And so if these proteins**<br>**are not helping you, then maybe something else would have.**<br>**But they're are many different ways of looking at this. But there is some finite**<br>**number of things that the cell can do. And the benefits, of course, in the case-- and**<br>**this is in particular in the case of a lac operon, what does this network allow us to**<br>**do? Yeah.**|
|**AUDIENCE:**|**You get to consume the energy of lactose.**|
|**PROFESSOR:**|**Yes.**|
|**AUDIENCE:**|**Lets you go faster.**|
|**PROFESSOR:**|**That's right, you get to consume lactose in this case. Now, we've already spent**<br>**some time thinking or discussing the lac operon.**<br>**What were the two key components in here in the lac operon? If you were a cell and**<br>**you wanted to eat lactose, what would you need to do? I'm picking somebody to--**<br>**yes, please.**|
|**AUDIENCE:**|**It's a gene that you should express, the lac gene?**|
|**PROFESSOR:**|**OK, right. So the lac genes. But maybe in a little bit more detail, what do we mean**<br>**when we say the lac genes? Well, I mean, it's not just lactose. But I mean, what are**<br>**the things that have to happen if you want to eat anything, I guess? Your cell--**|
|**AUDIENCE:**|**Import.**|
|**PROFESSOR:**|**Right, so you first have to import it. Now, in some cases, this can be done maybe for**<br>**some-- maybe nutrients, it could be done even passively, if it crosses the**<br>**membrane easily. But for most of the things that you might think about, you actually**|


3

**have to do active import.**

**So this is done by what? Anybody remember? lacY. So lacY is a membrane protein that imports lactose. And then what do you need to do?**

**AUDIENCE: Break the two apart, and then you can metabolize.**

**PROFESSOR: Right, then you have to eat it somehow. Now, of course, metabolism is a very complicated thing. But the key thing that's different between lactose and maybe the simple sugars is that you first have to break down the lactose into its constituent parts.**

**A lactose is a disaccharide composed of two simple monosaccharides. So what you need is you need this lacZ, beta-galactosidase, in order to cleave that bond. And then you have the two simple monosaccharides that can be eaten.**

**Now, the lac operon also has this lacA. And it's not quite obvious what that thing does, so nobody ever talks about it. But there is a third protein there. But what we always talk about is lacY, that's require to import the lactose and then lacZ that is required to break the lactose down into its monosaccharides.**

**And then the idea-- and that's not sufficient. You don't take those monosaccharides and instantly make more cells out of it. But the idea is that the rest of the metabolic machinery is kind of there any ways to do other-- that's kind of some assumptions. Can somebody explain how it is that they measured the cost of expressing these proteins? Yes.**

**AUDIENCE: So they [INAUDIBLE] expressed these proteins at different levels using different concentrations of IPTG.**

**PROFESSOR: Right.**

**AUDIENCE: There was no lactose around, so it was only the cost to no benefits. And then they measured [INAUDIBLE].**

4

**PROFESSOR:**

**All right, perfect. OK, so there are several key things in here. So first of all, normally, what we do is it's lactose inside the cell that causes this lac repressor to fall off and then you get expression of the lac operon.**

**But in order to kind of sidestep or circumvent that normal network, what we are doing in this case is adding IPTG. So IPTG allows one to get expression of-- and what IPTG is that it stops the inhibition of this lac promoter, where you get lacZ and lacY.**

**Now, the idea here is that you can control the level of expression of this operon, because what we really want is we want to measure a plot of something that you would call cost-- and we'll explore a little bit more what that means-- as a function of the lac operon expression.**

**And this is often done relative to the full induction of the wild type lac operon. And this is a relative growth rate reduction. So basically, this is a percentage, say, decrease in growth rate.**

**Now, there was a key thing that you brought up, which is that you want to measure the growth rate in the absence of lactose. Because otherwise as we increase the level of expression here-- so we're controlling this by IPTG, so there's some mapping from IPTG concentration to the level of expression here.**

**But we want to be able to measure the cost separate from the benefits. So it's important then to grow this in the absence of lactose. So say, no lactose.**

**But if I just take bacteria and I put them in a tube with say minimal media, salt, so forth, but no lactose, are they going to grow? They need to draw something. So what is it that the authors have done? Yes.**

**AUDIENCE: Glycerol.**

**PROFESSOR: That's right, they added some glycerol and in different parts. I think it's 1% glycerol. Does anybody happen to remember? I think, for most of it, it was 0.1%. I tell you what, we'll say a little bit of small concentrations of glycerol.**

5

**So the idea is that this is kind of a second rate carbon source. The bacteria are not super happy, but they're OK. And then given this, what they were able demonstrate is that, if they did add lactose, they would have grown faster.**

**So there's a sense that the lactose does help the cells. But you have to have some glycerol. Otherwise, you can't really measure these things. Yeah.**

**AUDIENCE: Why is it that-- you were saying if you put like a very good carbon source--**

**PROFESSOR: Well--**

**AUDIENCE: You're not going to see any [INAUDIBLE].**

**PROFESSOR: OK, so first of all what I was saying is that you have to have some carbon source. AUDIENCE: Sure.**

**PROFESSOR: Right, so you have to do something. And it's just good conceptually to make sure you think about how you would actually do this experiment. Now, you have to add some carbon source. But the question is, well, what happens if you just added a bunch of glucose?**

**Now, in that case actually, for some of the other experiments, I think that would have caused problems in the sense that then there would not be any benefits associated with growing or with adding increasing lac operon expression. For this experiment, in principle, one could have done that, although you really want to measure the costs and associated benefits in some environment, which you're to be doing in later experiments.**

**So I think it's really from a conceptual standpoint, in principle, you can measure this in glucose, but then you'd always worry, oh, well, maybe it's different. Yeah. AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Oh, yeah, right. So you could have broken down-- So the other issue is that, in principle-- and they don't talk about this here-- but yeah, if you add a bunch of**

6

**glucose, then you would have to have another mutant in order to break the glucose repression, because if you have this preferred carbon source, glucose, then you'll naturally repress the CRP, all of the alternative modes of carbon metabolism just because glucose was kind of the best.**

**And what was the key conclusion from this first data plot?**

**AUDIENCE: It's nonlinear.**

**PROFESSOR: All right, nonlinear. The cost is a function of the lac expression. And it grows super linearly. I always forget what the difference is in concave and convex is. I don't know if other people have this particular brain problem.**

**But the second derivative is positive. In particular, that means that if you do draw some sort of like line, then they have data that looks something like-- so here is 0.5. We have something that kind of falls below here.**

**They had about a 0.25. And it was also a little bit below that crossed. They had a 0.75. And then they had a 1.**

**Why is it that they can't go above 1 here? Why do they not have more data out here?**

**AUDIENCE: Because you can't have more expression than full expression.**

**PROFESSOR: You can't have more expression than full expression with this promoter, because what they are doing is they're adding IPTG, so they titrate between 0 and maximal expression from this promoter. In principle, you could always get another one. And then you should be able to go out further, right?**

**And at maximal expression, they measure about a 4% growth deficit, 0.04, just to give you a sense of scale. So this is 4% deficit. Now, I want to ask a more general question.**

**So let's imagine that you are measuring some quantity. So we'll say this is some quality y as a function of x. And let's imagine that the true y as a function of x looks**

7

**like something.**

**Now, you go and you measure at multiple values of x this curve, because we're very interested in what this curve looks like. Now, the question is, what fraction of the error bars will contain this curve and, of course, contain this is true curve?**

**So I'm assuming that this curve is the god-given actual thing that you're measuring. And so you measure this quantity with noise. So we measure this some number of times, some number of times. Do you understand the question?**

**So here, contained the curve. There, it didn't. So what fraction of error bars will contain that curve?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Right. And indeed, what we want-- it's always good-- what were the error bars in the figure 2A in this? Right, well, OK, so they're experimental error, right.**

**Incidentally, how is it that they actually measure these things? Does anybody-- And so these are actually a result of growing on a nice [INAUDIBLE] well, like a microtiter plate, where they used a checkerboard pattern. And they take 48 different cultures. And they measure the growth rates for each one individually. And then they're plotting the standard error of the mean.**

**Do you understand what I'm trying to ask you?**

**AUDIENCE: So in that case, I mean, the size of the error bars, you just want a scaling or something, [? if that's right, ?] because the size of the error bars--**

**PROFESSOR: Right, well--**

**AUDIENCE: I just--**

**PROFESSOR: Yeah, OK, so this is a good question. We'll find out. So it depends on n, where n is the number of samples that we took at each location. Question, yeah.**

**AUDIENCE: Yeah, the standard error is just the [INAUDIBLE]?**

8

**PROFESSOR: Right, so standard error of the mean, this is an important question. What you do is you calculate the standard deviation, divide by the square root of n-- OK, now, I always forget whether it's n or n minus 1, now.**

**We already did one n minus 1, right? So it's you measure the standard deviation of the data, the standard deviation in y divided by root n, where n is the number of measurements you took at that point.**

**But of course, when you measure the standard deviation, there was already an n minus 1, right? Have I lost a minus 1? Do you guys-- OK. Yeah. AUDIENCE: Isn't the standard-- I thought the standard error of the mean and not the actual standard deviation [INAUDIBLE]? PROFESSOR: Yes. And we're going to spend a lot of time talking about what the difference is between a standard deviation and a standard error of the mean. And it depends on what you're trying to ask. Do you guys understand what I'm trying to ask here? All right, well, let's just see where we are, and then we'll discuss. OK, ready? 3, 2, 1. All right, so we got many A's, B's, C's. Nobody likes D. OK, but it's very common to see that.**

**Let's go ahead and-- it's worthwhile, I think there's enough variation to decide. And in particular, between your neighbor, try to agree on why or why not it might depend on n and so forth. We'll just have a minute to think about this. AUDIENCE: [INTERPOSING VOICES]. PROFESSOR: So what do you guys think? AUDIENCE: We're still [INAUDIBLE]. PROFESSOR: OK, no, that's fine. AUDIENCE: [INTERPOSING VOICES].**

9

---

[Up: contents](index.md) · [PROFESSOR →](02-professor.md)
