---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/so6mk-fcp4e-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/so6mk-fcp4e-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: Measure all the distances [INAUDIBLE] to all the nodes in the other. PROFESSOR: Right. So you could do all to all. What else could you do? You can take the minimum of all those values. You can take the maximum of all those values. And we'll see that all those are things that people do. So this clustering, there are already rather uninformative terms for some of these kinds of decisions. So it's called single linkage, is you decide that the distance between two clusters is based on the minimum distance between any member of cluster Y and any member of cluster Z. Complete linkage takes the maximum distance. And then the extremely unfortunately named Unweighted Pair Group Method using Centroids-- UPGMC, I won't try to say that very often-- takes the centroid, which was an early suggestion from the class. And then the UPGMA, Unweighted Pair Group Method with Arithmetic Mean, takes the average of all the distances, all suggestions that people have made.**

**So when would you use one versus the other? Well, a priori, you don't necessarily know. But it's good to know how they'll behave. So what do you imagine is going to happen if you use single linkage, versus complete linkage. Remember, single linkage is the minimum distance. And complete linkage is the maximum distance. So what's going to happen in this case, if I use the minimum distance. Which two groups will I combine?**

**AUDIENCE: The blue and the red.**

**PROFESSOR: The blue and the red, right? Whereas if I use the maximum distance, then I'll combine the green and the red. So it's important to recognize, then, that the single linkage has this property of chaining together clusters, based on points that are near each other. Whereas the complete linkage is resistant to grouping things together, if they have outliers. So they'll behave differently. Now, if your data are compact, and you really do have tight clusters, it's not going to matter too much would you use. But in most biological settings, we're dealing with much noise, there's data. So you actually will get different results based on this. And**

13

**as far as I know, there's no really principal way to figure out if you have no prior knowledge, which to use.**

**Now all of these hierarchical clustering come with what's called a dendogram. And you'll see these at the top of all the clustering. And this represents the process by which the data were clustered. So the things that are most similar are most tightly connected in this dendogram. So these two data points, one and two, you have to go up very little in the y-axis, to get from one to two. Whereas if you want to go from one to 16, you have to traverse the entire dendogram. So the distance between two samples is how far vertically you have to go to connect between them.**

**Now the good things are that the dendogram is, you can then understand the clustering of the data. So I can cut this dendogram at any particular distance, and get clearly divisions among my data sets. So if I cut here at this distance level, then I have two groups. One small, one consisting of these data. And one large, one consisting of these. Whereas if I cut down here, I have more groups of my data. So it doesn't require me in advance to know how many groups I have. I can look at the dendogram and infer it.**

**The one risk is that you always get a dendogram that's hierarchical, regardless of if the data were hierarchical or not. So it's more a reflection of how you did your clustering than any fundamental structure of the data. So the fact that you get a hierarchical dendogram means really nothing about your data. It's simply a tool that you can use to try to divide it up into different groups. Any questions on the hierarchical clustering? Yes?**

**AUDIENCE: If each data point is its own cluster, then won't that be consistent across, like, single linkage, complete linkage-- like, why would you cluster? Does that question make sense? Like if you cut it down below, then haven't you minimized-- don't you successively minimize the variance, I guess, up to your clusters, by--**

**PROFESSOR: So if I cut it at the lowest level, everybody is their own cluster. That's true. Right. I'm interested in finding out whether there are genes that behave similarly across the data sets. Or--**

14

---

[← AUDIENCE: [INAUDIBLE] square there?](03-audience-inaudible-square-there.md) · [Up: contents](index.md) · [AUDIENCE →](05-audience.md)
