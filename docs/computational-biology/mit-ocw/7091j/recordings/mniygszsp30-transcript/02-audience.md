---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/mniygszsp30-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/mniygszsp30-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Yes. Where did the degrees of freedom enter into the equation?**

**PROFESSOR: Where did the degrees of freedom enter into this? Great question. The chi-square tables that you look up are indexed by the number of degrees of freedom of difference. OK? And so whenever you compute a chi-squared, you will compute it with the number of degrees of freedom difference. Any other questions?**

**OK. So let's now turn to evaluating RNA-seq data once again. And I'm going to describe a method called DESeq for determining differential expression. And in our analysis, what we're going to do is we're going to let i range over a gene or an isoform. j is an experiment. And there may be multiple experiments in the same condition that are replicates. And Kij is the number of counts observed for i and j. So that's the expression of gene or isoform i in experiment j.**

**Now what we need to do, however, is to normalize experiments against one another. And the normalization factor s sub j is computed for a particular experiment. And it's used to normalize all of the values in that experiment. And if all the experiments were completely identical-- the read depth was identical and everything was the same-- then all of the s sub js would be 1.**

**If you had an experiment that had exactly twice as many reads as the other experiments, it's s sub j would be 2. So this scale factor is used to normalize things in our next slide, as we'll see. And the essential idea is that we're going to take the median value of this ratio.**

**And the reason that the denominator is a geometric mean is so that no one**

15

**experiment dominates the average. They all have equal weight for the average. But the geometric mean is simply the product of all of the expressions for a particular median gene taken to the root m power to get them back to the value for a single experiment. And that is the normalizing factor for the numerator, which is the number of counts for a particular gene. OK?**

**So we're just doing median style normalization where s sub j is a scale factor. Once again, if all the experiments were the same, s sub j would be 1. If one particular experiment had twice as many counts as another experiment uniformly, s sub j would be 2, just for that experiment. Any questions about the scale factor? Yes.**

**AUDIENCE: Sorry, what is the term on the bottom-- in the denominator?**

**PROFESSOR: That's a normalizing term across-- that's the geometric mean of all the experiments put together. All right? So because it's the product of all the experiments-- m experiments-- then, rooted m, it's equal to the geometric mean of a single experiment. Any other questions? Yes.**

**AUDIENCE: Are we normalizing different experiments to each other or different replicates of a single experiment?**

**PROFESSOR: In this particular case, each one of these is a different replicate. OK? So j is ranging over different replicates, not over conditions, right now. So each replicate, each experiment, gets its own normalizing factor. We'll see, in a moment, how to put those replicates together to build statistical strength. But we need-- since each replicate has its own read depth, we have to normalize each one independently. OK?**

**So what we then do is we compute an expression for a condition. Now a condition, we're going to call p. And q sub ip is the normalized expression for gene slash isoform i in condition p.**

**So a condition may have multiple replicates in it. So we're going to average, over all of the replicates, the average expression, as you can see here. So we're summing over all the replicates for a given condition. We're going to take each replicate,**

16

**normalize it by its scale factor we just computed, and then compute the normalized expression for a gene or an isoform in that particular condition. Is that clear to everybody, what's going on here?**

**Now I'm describing this to you because the key fact is the next line, which is that we compute the mean for a particular replicate by taking the normalized expression for a gene and then reverse correcting it back to scaling it back up again for that particular replicate by multiplying by s sub j. But the most important thing is what's on the right hand side, which is that the variance is equal to the mean plus this function of the expression.**

**And the reason this is important is that most other models for modeling expression data use Poisson models. And we've already seen, when we talked about library complexity, that Poisson models don't work that well all the time. So this is using a negative binomial function, once again. We saw negative binomials before. We're modelling both the mean and the variance. And the variance is a function, a linear function and a non-linear function, of the mean.**

**So what's going to happen, then, is that we're going to use the negative binomial to compute the probability of observing the data in a given condition. And we can either combine conditions and ask, what's the probability of seeing the conditions combined with a single mean and variance, or we can separate them into a more complex H1 hypothesis and ask, what's the probability of seeing them with separate means and variances, and then do a test to see how significant the difference is to determine whether or not we can exclude the fact that the genes are expressed at the same level.**

**And to give you an intuitive idea of what's going on, this is a plot from the paper showing the relationship between mean expression and variance. Recall, for Poisson, that variance is equal to mean. We only have one parameter to tune for Poisson, which is lambda. The purple line is Poisson. And you can check and see that the mean's equal to the variance in that case. What DESeq does is it fits the orange line to the observed data. Yes.**

17

**AUDIENCE: I don't know where the v sub p comes from. Where is that, again?**

**PROFESSOR: That's the function. V sub p, in that equation up there, is the function that we're fitting-- that's the solid orange line-- to the observed relationship between mean and variance in the data. OK? So DESeq fits that function. EdgeR is another technique that does not fit and instead uses the estimate that's the dotted line, which isn't as good.**

**So a lot of people use DESeq these days for doing differential expression analysis because it allows the variance to change as the mean increases. And this is the case for these type of count data. Before I go on though, I'll pause and see if there are any questions at all about what's going on here. Yes.**

**AUDIENCE: You said that mu sub p, then, is the [INAUDIBLE] to the data. I'm confused. How do we fit that function, or where does that come from?**

**PROFESSOR: You mean the mu sub p?**

**AUDIENCE: Yes.**

**PROFESSOR: That function is fit. And the paper describes exactly how it's fit, which I posted on the Stellar site. But it's a nonlinear function of q, in this case. Good question. Any other questions? OK.**

**So once again, we have two hypotheses, the null hypothesis that A and B are expressing identically, H1, A and B differentially express. We can compute the number of degrees of freedom. And we can do a likelihood ratio test, if we'd like, to compute the probability of H0.**

**And our model in this case is the negative binomial model of the data, which fits the data better. And that's why DESeq does a better job than other methodologies. Because it provides a better approximation to the underlying noise.**

**And the next slide shows what you get out of this kind of analysis, where the little red dots are the genes that have been called significant using Benjamini-Hochberg**

18

**correction, which we talked about previously. And you can see how, as the mean increases, the required log 2 fold change comes down to be significant. So oftentimes, you'll see plots like this in papers that describe how they actually computed what genes were differentially expressed. Any questions at all? Yes.**

**AUDIENCE: Why is it that the significance is lower as the mean increases?**

**PROFESSOR: Why the significance is lower?**

**AUDIENCE: Or the threshold.**

**PROFESSOR: Oh, because as you increase the number of observations, the mean value theorem is going to cause things to actually get closer and closer to 0. And so you need less of a fold change difference to be significant as you get more and more observations. And other questions? OK.**

**So now we're going to delve into one other area. How many people have done hypergeometric tests before? OK. So we're going to talk about hypergeometric tests.**

**So imagine that we have a universe, for simplicity, of 1,000 genes. OK? So we have this universe. And we have, B is a set of genes that there are 30 of them. And there's another set, A, of which there are 20. And the overlap between these two is a total of three genes.**

**So it might be that A is the set of genes that are differentially expressed between two conditions. B is the set of genes that, you happen to know, have a particular annotation. For example, they're involved in stress response in the cell. And you'd like to know whether or not the genes that are differentially expressed have a significant component of stress response related genes or whether or not this occurred at random. OK?**

**So we need to compute that. So how many ways could we choose B? Well, if we are going to use-- this is n1, n2, this is big N, and this is k. All right? So the number of ways I can choose B is big N choose n2. That's the number of ways I can choose B.**

19

**Is everybody with me on that? Yeah? OK.**

**How many ways can I choose three elements out of A, these three that are going to overlap? Well, that's going to be n1 choose k. So that's how many ways I can choose these three elements.**

**And then, how many ways could I choose the other elements of B? So once again, I'm figuring out how I can choose B. Well, how could I choose the rest of B? Well, how many elements do I have to choose, of B, here?**

**Well, B is n too big. But I've already chosen k of them. Right? All right. Sorry, it's the other way around. The universe I can pick from is 1,000, which is all the elements, minus the elements of A that I've already chosen from to get those three.**

**And then I need to pick the 27 things they don't overlap with A. So 27 things that don't overlap with A would be n2 minus k. So this is the number ways to choose B given this set of constraints. This is the number of ways to choose B given no constraints. So the probability that I have overlap of exactly k is equal to this, which is, how many ways are there with no constraints and how many ways are there given that I have an overlap of k. All right?**

**And typically, what I want to ask is, what is the probability that my observed overlap is greater than or equal to k. So this case, the overlap would be three. But I also would need to consider the fact that I might have four, or five, or six, which would be even more unlikely, but still significant. So if you look at the exact computation, the probability of three here is 0.017. And the probability that I have three or more is 0.02.**

**So that's still pretty significant. Unlikely that would occur by chance. Right? That I have three or more genes overlapping in this situation could only happen two out of 100 times. Does everybody understand what's going on here? Any questions at all? So you're all now hypergeometric whizzes, right? All right? Fantastic.**

**OK. Now we're going to turn to a final kind of analysis. How many people have heard of principal component analysis before? How many people know how to do**

20

**principal component analysis? A few. OK. Great. Yes.**

**AUDIENCE: Sorry, could you just briefly mention, again, where exactly do we use the hypergeometric test? What kinds of questions are we asking when we do that? PROFESSOR: Typically, they're overlap questions. So you're asking-- you have a universe of objects, right-- like, in this case, genes. And you have a subset of 20 and a subset of 30. Let's say these are the differentially expressed genes. These are genes in the stress response pathway. They overlap by three genes. Does that actually occur at random or not? All right?**

**If I told you that there are a much smaller number of genes and the stress response genes were very much larger, it could be much easier for that overlap to occur at random. Good question. Any other questions?**

**OK. So the next part of lecture is entitled "multivariate Gaussians are your friends." OK? They are friendly. They're like a puppy dog. They are just wonderful to play with and very friendly. And the reason most people get a little turned off by them is because they get this-- the first thing they're shown is this very hairy looking exponential which describes what they are.**

**And so I'm going to shy away from complicated looking exponentials and give you the puppy dog, my favorite way of looking at multivariate Gaussians. OK? Which, I think, is a great way to look at them. And the reason we need to look at multivariate Gaussians is that they help us understand what is going on with principal component analysis in a very straightforward way.**

**And the reason that we want to use principal component analysis is that we're going to be able to reveal hidden factors and structures in our data. And they're also going to allow us to reduce the dimensionality of the data. And we'll see why in a moment.**

**But here is the friendly version of multivariate Gaussians. And let me describe to you why I think this is so friendly. So we're all familiar with unidimensional Gaussians like this. Centered at zero. They have variance 1. Just very friendly univariate Gaussians, right? Everybody's familiar with those? Normal distributions?**

21

**So let's suppose that we just take a whole collection of those. And we say that we have a vector z that is sampled from a collection of univariate Gaussians. And it can be as long as we like. OK? But they're all sampled from the same distribution. And what we're going to say is that our multivariate Gaussian, x, is going to be a matrix times z plus a mean.**

**And so what this matrix is going to do is it's going to take all of our univariate Gaussians and combine them to produce our multivariate Gaussian. All right? So the structure of this matrix will describe how these single variate Gaussians are being mixed together to produce this multivariate distribution. And you can imagine various structures for this matrix A. Right?**

**And the covariance matrix, sigma, which describes the structure of this multivariate Gaussian, is shown on this slide to be equal to A A transpose. And thus, if we knew this matrix A, which we may not know, we'd be able to compute the covariance matrix directly. OK?**

**Let me take that one more time. We take a bunch of univariate Gaussians, make a vector z out of them. And just for clarity, right, we're going to talk about matrices and vectors as rows across columns. So this is n by 1. This is n by n. This is n by 1. And this is n by 1. OK? That's the dimensionality of these various objects we're dealing with here.**

**So we get this vector of univariate Gaussians. We apply this matrix n to combine them together. We get out our multivariate Gaussian offset by some mean. Is everybody happy with that so far? Yes? No? You're suspending disbelief for the next slide. Is that-- OK.**

**Well, here's the next thing I'd like to say, is that the variance of a vector-- we'll call it v-- times x, which is a random variable, is going to be equal to-- x is derived from this distribution-- v transpose sigma v. And the demonstration of that is on the top of this page. So the variance of this vector-- sorry, the projection of this random variable onto this vector-- is going to give you a variance in this direction as that**

22

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [product. →](03-product.md)
