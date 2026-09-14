---
title: 'AUDIENCE: [INAUDIBLE] square there?'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/so6mk-fcp4e-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE] square there?

**Source:** `recordings/so6mk-fcp4e-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Yes, you're right. There should be a square there. Thank you.**

**So then to compute the Pearson correlation, we're going between two genes, A and B, we're going to take the sum over all experiments, that the z-score for A and the z-score for B, the product of that, summed over all the experiments. And these values as we'll see in a second, are going to range from plus 1, which would be a perfect correlation, to minus 1, which would be a perfect anti-correlation. And then we're going to find the distance is 1 minus this value. So things that are perfectly correlated then, would have an r of zero. And things that are anti-correlated would have a large one.**

**So if we take a look at these two obviously by Euclidean distance, they'd be quite different from each other. But the z-scores have converted the expression values into z-scores over here, you can see that the z-scores obviously, this one is the most negative of all of the ones. And this as the lowest one in all of these. This one's the highest. And similarly for the red one, lowest to the highest. So the z-**

9

**scores track very well. And when I take the product of this, the signs of the z-score for A and B are always the same. So I summed the product of the z-scores, I get a large number. And then the normalization guarantees that it comes out to one.**

**And so the red and blue here will have a very high correlation coefficient. In this case, it's going to be an r correlation coefficient of 1. Whereas compared to this one, which is relatively flat, the correlation coefficient will be approximately zero. Any questions on that?**

**So what about, say the blue and the red? Well, their z-scores are going to have almost the opposite sign every single time. And so that's going to add up to a large negative value. So for these, they'll be highly anti-correlated. So A, the blue and the red, have a correlation coefficient of minus 1. OK. So we have these two different ways of computing distance measures. We can compute the Euclidean distance, which would make the red and blue the same, but treat the green one as being completely different. Or we have the correlation, which would group all of these together, as being similar. What you want to do is going to depend on your setting. If you look in your textbook, you'll see a lot of other definitions of distance as well.**

**Now what if you're missing a particular data point? This used to be a lot more of a problem with arrays than it is with [? RNAC. ?] With arrays, you'd often have dirt on the array, that it actually would literally cover up spots. But you have a bunch of choices. The most extreme would just be to ignore that row or column of your matrix across old data sets. That's usually not what we want to do. You could put in some arbitrary small value. But frequently we will do what's called imputing, where we'll try to identify the genes that have the most similar expression, and replace the value for the missing one with a value from the ones that we do know.**

**Distance metrics, pretty straightforward. Now we want to use these distance metrics to actually cluster the data. And what's the idea here? That if we look across enough data sets, we might find certain groups of genes that function similarly across all those data sets, that might be revealing as to their biological function.**

**So this is an example of an unsupervised learning problem. We don't know what the**

10

**classes are, before we go in. We don't even know how many there are. We want to learn from the data. This is a very large area of machine learning. We're just gonna scrape the surface. Some of you may be familiar with the fact that these kinds of machine learning algorithms are used widely outside of biology. They're used by Netflix to tell you what would movie to choose next. Or Amazon, to try to sell you new products. And all the advertisers who send pop-up ads on your computer.**

**But in our biological setting then, we have our gene expression data, collected possibly over very large numbers of conditions. And we want to find groups of genes that have some similarity. This is a figure from one of these very early papers, that sort of establish how people present these datas. So you'll almost always see the same kind of presentation. Typically you'll get a heat map, where genes are rows. And the different experiments here time, but it could be different perturbations, are the columns. And genes that go up in expression are red, and genes ago down in expression are green. And apologies to anyone who's colorblind. But that's just what the convention has become.**

**OK, so then why cluster? So if we cluster across the rows, then we'll get sets of genes that potentially behave-- that hopefully if we do this properly, behave similarly across different subsets of the experiments. And those might represent similar functions. And if we cluster the columns, then we get different experiments that show similar responses. So that might be in this case, different times that are similar. Hopefully those are ones that are close to each other. But if we have lots of different patients, as we'll see in a second, they might represent patients who have a similar version of a disease.**

**And in fact, the clustering of genes does work. So even in this very early paper, they were able to identify a bunch of subsets of genes that showed similar expression at different time points, and turned out to be enriched in different categories. These ones were enriched in cholesterol biosynthesis, whereas these were enriched in wound healing, and so on.**

**So how do you actually do clustering? This kind of clustering is called hierarchical.**

11

**That's pretty straightforward. There are two versions of hierarchical clustering. There's what's called agglomerative and divisive. In agglomerative, you start off with each data point in its own cluster. And then you search for the most similar data point to it, and you group those together. And you keep doing that iteratively, building up larger and larger clusters.**

**So we've discussed how to compare our individual genes. But you should be able to, right now, to find, if I gave you the vector of expression for a single gene, to find the other genes in the data set that's most similar, by either say, Euclidean or Pearson correlation, or what have you. But once you've grouped two genes together, how do you decide whether a third gene is similar to those two? So now we have to make some choices. And so there are number of different choices that are commonly made.**

**So let's say these are our data. We've got these two clusters, Y and Z. And each circle represents a data point in those clusters. So we've got four genes in each cluster. Now we want to decide on a distance measure to compare cluster Y to cluster Z. So what could we do? So what are some possibilities? What might you do?**

**AUDIENCE: We could take the average of all points. PROFESSOR: You could take the average of all points, right. What else could you do? Only a limited number of possibilities. AUDIENCE: Centroid? PROFESSOR: Yeah, so centroid, you could take some sort of average, right. Any other possibilities? AUDIENCE: You can pick a representative from each set [INAUDIBLE]. PROFESSOR: So you could pick a representative, right? How would you decide in advance what that would be though? So maybe you have a way, maybe not. And what other possibilities are there? Yeah?**

12

---

[← hybridize to each other.](02-hybridize-to-each-other.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
