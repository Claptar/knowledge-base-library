---
title: Random incidence under erlang arrivals transcript
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/worked-examples/random-incidence-under-erlang-arrivals-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Random incidence under erlang arrivals transcript

**Source:** `worked-examples/random-incidence-under-erlang-arrivals-transcript.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Hi. In this problem, we're going to look at random incidence under Erlang arrivals. First, let's parse what that means. In a Poisson process, remember, the time between arrivals, or the interarrival time, is distributed as an exponential random variable. And random incidence for a Poisson process refers to the somewhat surprising result that when you consider a specific time, say, T-star, then the length of the inter-arrival interval that contains that time T-star is not distributed as an exponential random variable. It's actually distributed as an Erlang random variable of order 2 or it's distributed as a sum of two exponential random variables. And the reason for that is that it comprises of two parts. One is the time since the last arrival until T-star, which is exponentially distributed, and the time from T-star until the next arrival, which is also exponentially distributed.

So that brings us to a review of what Erlang random variables are. An Erlang random variable of order k is just the sum of k independent and identically distributed exponential random variables. So to be more specific, if Ti is an exponential random variable with parameter lambda, then if you take kiid copies of Ti and add them up, and call that Yk, then Yk is an Erlang random variable of order k.

And one other fact is that the mean of Yk, the mean of an Erlang random variable of order k, is just k, the order, over lambda, which is the rate of the underlying exponential random variables.

So as a consequence, if you have an Erlang random variable of order two and that random variable also has a mean of two over lambda, we can interpret that random variable as just being the sum of two exponential random variables. 2 iid exponential random variables, T1 and T2, where each one takes exponential with the rate in lambda.

OK, so in this problem now, we're dealing with the random incidence not under Poisson processes, but under something else, which we call here an Erlang process with Erlang arrival times. So to be more specific, what we're saying is that, instead of inter-arrival time being exponentially distributed, in this process, and inter-arrival time is actually distributed as an Erlang random variable of order 2 with mean 2 over lambda.

So to be explicit, this is no longer a Poisson process. It's some other process because the interarrival times are not exponential. So let's make use of this fact that we talked about earlier because now we know that the inter-arrival times of this Erlang process are Erlang order 2 with mean 2 over lambda. But we know that that can just be re-interpreted as a sum of two simple exponentials, each with parameter lambda.

So let's just draw another picture and imagine that for each of these arrivals, so say we have three sample arrivals in this Erlang process, we can fill in, kind of, the gaps between these with additional arrivals. And then think of each one of these times as all being exponential with parameter lambda.

1

So this is a valid interpretation because when we connect these, these inter-arrival times correspond to the combination of two inter-arrival times, which we know we can split that into just two exponentials. So each one of these is an exponential random variable. And when you combine them, you get an Erlang order of 2.

But the nice thing about this is that if we look at this diagram, it actually is just exactly a Poisson process with a rate lambda because now, what we're dealing with are exactly-- the inter-arrival times are now exactly exponential random variables. And so this is in fact, now, just a simple Poisson process.

And we can also just think of it as we take the Poisson process, and take every other arrival, say, all the even-numbered arrivals, and make those corresponds to be arrivals in the Erlang process.

OK, so now let's think about some specific time T-star. We want to know what is the distribution of the length of this to be specific inter-arrival interval that T-star is in.

Well, what we can do is take it down to the level of this Poisson process and look at it from there. Well, we do that because, for a Poisson process, we know about random incidence for Poisson processes. And we know how to deal with Poisson processes.

So let's think about this now. Well, T-star is here. And what we know from random incidence for a Poisson processes is that the length of this inter-arrival interval for the Poisson process, we know that this is an exponential plus an exponential. So combined, this is Erlang order 2.

But that only covers from here to here. And what we want is actually from here to there. Well now, we tack on an extra exponential because we know that the inter-arrival times-- the time between this arrival and that arrival in the Poisson process is just another exponential. And now all of these are in [INAUDIBLE] time intervals. And they're all independent. And so the time of this inter-arrival interval in the Erlang process is just going to be the sum of three independent exponentials within the underlying Poisson process. And so to answer here is actually, it's going to be an Erlang of order 3.

Now this is one possible scenario for how this might occur. Another scenario is actually that T- star is somewhere else. So let's draw this again.

And suppose now, in this case, T-star landed between an even numbered arrival in the Poisson process and an odd numbered arrival. Now it could also arrive between an odd numbered and an even numbered arrival. So it could be that T-star is actually here.

Well, but in this case, it's actually more or less the same thing because now what we want is the length of this entire inter-arrival interval, which, in the Poisson world, we can break it down into random incidence within this interval, this inter-arrival interval, which is two exponentials, or an Erlang of 2, plus this interval, which is just a standard inter-arrival time, which is another exponential.

2

So in this case as well, we have the sum of three independent exponential random variables. And so, in either case, we have that the inter-arrival time in the Erlang process is an Erlang of order 3. And so the final answer is, in fact, that the inter-arrival for random incidence under these Erlangtype arrivals is an Erlang of order 3.

OK, so in this problem we looked at the random incidence under a different type of an arrival process, not Poisson, but with Erlang random variables. But we used the insight that Erlang really can be re-interpreted as the sum of independent and identically distributed exponential random variables. And exponential random variables can be viewed as one way of interpreting and viewing a Poisson process.

And so by going through those steps, we were able to use what we know about random incidence under Poisson processes to help us solve this problem of random incidence its Erlang arrivals. So I hope that was helpful. And I'll see you next time.

3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
