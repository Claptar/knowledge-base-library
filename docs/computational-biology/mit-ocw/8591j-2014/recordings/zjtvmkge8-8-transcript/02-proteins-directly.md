---
title: proteins directly.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/zjtvmkge8-8-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# proteins directly.

**Source:** `recordings/zjtvmkge8-8-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**But at least it's just useful to know what the properties of this thing are on average even though, for the outgoing edges, the average is a little bit dangerous. Because it's really that most proteins don't have any outgoing edges, and then some have many. All right so this is this probability P. And this is going to be useful, because this P will appear when we're trying to construct these random networks.**

**So what we're going to do is we're going to ask how frequently or how many of a given subgraph you expect to appear in this larger network that we have here? And we're going to characterize each of these subgraphs by two properties. And in particular, if we're going to analyze some smaller graph, we just have to keep track of how many nodes are in the subgraph, and how many edges are in the subgraph.**

**So for example, if we have auto regulation, then we're just talking about little n equal to one, little g equal to one. Whereas in the case of this feed-forward loop, what is little n and what's little g? Well we can count now. Here n is equal to three, one, two, three, and g is also equal to three. And we're going to find that actually the fact that these two numbers are equal is somehow very relevant in thinking about the dynamics of these networks later.**

**In this framework, when I just draw an arrow in the context of a generic subgraph, am I necessarily trying to say that this is up regulation of x up regulating y? No. So this is a bit confusing because depending on the context, sometimes the arrows actually do mean up regulation, sometimes they just mean regulate. And in this case, where we're talking about subgraphs, we're just saying that x regulates y in one way or another.**

**This is also how we're going to write the so-called coherent type one feed-forward loop, but for right now this is just a generic feed-forward loop. Yes.**

**AUDIENCE: Regulate means positive regulation?**

**PROFESSOR: Yes. We say activate. So the way that we think about is we ask, what's the expected number of some subgraph G? And indeed what we're going to be doing for right**

4

**now is assuming this Erdos-Renyi random network. Now what we're told is that this is going to look something like the following.**

**could somebody explain one of these three terms? Yes.**

- **AUDIENCE: Well you have to select edges, and you have choose them correctly. So for each one, there's a chance that [INAUDIBLE].**

- **PROFESSOR: So for here what we're going to do is, for example in this context, we'll say, we're going to choose these three. And now the question is, we have to put in three edges as well to connect those nodes, and each one of them has some probability P of actually somehow appearing. Because this is what we're keeping constant from the original network.**

**So we're assuming that we have this Erdos-Renyi network with the same number, say roughly 400 nodes, and then what we're going to do is grab maybe three of them and ask, all right, what's the probability that we get these three actual edges? So you get P to the g. Now where does this term come from? Yes.**

**AUDIENCE: Selecting a node.**

**PROFESSOR: So we're going to be selecting N nodes. We're assuming that this N is much larger. We're assuming that we have a big network, so it's much larger than the size of the subgraph we're looking at, so we don't have to think about n times n minus one, n minus two, and so forth. And then there's this factor a here as well, which, depending on how you do your counting-- this is a little bit tricky, but what was a again? Yes.**

**AUDIENCE: It's the number of ways to arrange the edges. It's a symmetry factor.**

**PROFESSOR: Yes, it's a symmetry factor, it's a way of-- there are multiple ways of looking at this. You could think about it as the number of ways of rearranging x, y, and z and having the same subgraph, the exact same one. In this case, there's actually no way to rearrange x, y, and z to have the same one.**

5

**Because x occupies a special spot, y is indeed again a special spot. z is special. So there's no permutations that you can do to get the same thing. Whereas if you have this repressilator-- now here I'm just drawing this as an arrow, because again we're just thinking about the generic version of these things. So it's just when we have x, y, and z regulating each other. In this case, you can get the same network by rotating these x's, y's, and z's.**

**So in this case, you get a equal to three. For pretty much all the conclusions we're going to talk about, these factors of one, two, three don't actually end up being relevant. But it's good to know that they indeed exist. So this is fine, but it's useful to express this in another way. In particular, we can always define this lambda, which is E/N, as the mean number of incoming edges or the mean number of outgoing edges.**

**And with this, we can express this guy in a way that is surprisingly informative. Nothing happened except that we just plugged this thing in here. But by doing, we see something that's kind of interesting, which is that there's reason to believe that for many of these networks, this lambda, this mean number of incoming edges, that lambda will be roughly similar-- whether you're talking about a network that is 500 nodes large or 5,000 nodes large.**

**And indeed in this case, it's around one. It's just over one. So that means that when we think about the number of subgraphs that will be in this large network, it scales with the size of the overall network. We had this little n minus little g. And in particular, in cases when you're analyzing a subgraph with the same number of nodes as edges, then you just get n to the 0, and it doesn't scale with a number. So for those, and indeed basically for all those subgraphs where little n is equal to little g-- then you expect of order one of those-- if lambda is around one, then you expect of order one of those to appear in the network.**

**And so from a very simple standpoint, the networks, like the feed-forward loop that we see that is a network motif, the expectation is that in a random network, you would get around one, maybe two. Whereas if you see many of them, dozens, then**

6

**it's indeed a network motif. Are there any questions about how that appeared in the chapter or the argument there?**

**So indeed, we can actually just then say, for the feed-forward loop, we can just go ahead and ask how many were observed in E. coli, this network that was actually observed? And this was 42 I believe. Whereas if you do this analysis for the ErdosRenyi network, you get 1.7 plus or minus 1.3. Because these things appear randomly, they should be Poisson distributed.**

**So you expect of order one of them to appear in a random network with this same kind of sparseness, the same number of edges. But we actually observe this much larger number. So then you can say, all right, this is evidence for the feed-forwad loop being a network motif. That for some reason, this subgraph appears more frequently than what you'd expect based on genes.**

**Of course, we alluded to this on the end of class on Tuesday, that maybe this Erdos-Renyi network is not the proper null model or null network to be using. And maybe we should use one of these degree-preserving networks. So maybe we should try to preserve more the properties of the original network. And So can because somebody say a little bit of what we mean by degree-preserving?**

**There's an element that our null model here already preserves something about the degree. It preserves the means. So it's not just that we picked up some random null model, some random ER network. So what is it that we want to keep track of in this degree-preserving network? I saw a hand over there, but I'm not trying to call on people randomly. Although I'm going to start in the second half of the semester, just after drop date.**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [[LAUGHTER] →](03-laughter.md)
