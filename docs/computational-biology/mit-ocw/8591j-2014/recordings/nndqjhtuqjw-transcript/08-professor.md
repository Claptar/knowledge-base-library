---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/nndqjhtuqjw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/nndqjhtuqjw-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**[INAUDIBLE].**

**--exponent. Right. So for these other models then, it falls off exponentially. Right? So even faster. So it's easy to look at 1 over k to the fourth, and think, oh, that's a fast fall off. We have to remember that it's slow compared to some other things. So in particular, if you look at the data for real networks, and you see that the probability distribution in many cases goes over orders of magnitude in terms of this probability. You think oh, that's a big range. And it is a big range, but the fact is that you actually see some nodes with the thousand ideas or whatnot, which is something that you would just never see, if it were a random network, or if it were not a power law distributed network.**

**And I think that this is also highlighting another statement, which is that a powerful way to make a difference, for example, if you're going to write down a model, or you're going to do a theory, is that it's nice if there's a clear observation that needs to be explained. Because you can always write down a model of something, and maybe you'll find something interesting. But a way to massively increase the probability that you're going to discover something interesting is if you already know there's something interesting there and that you're trying to explain it.**

**And I think that this is an example of that, right there, it was already an observation, it was already known. It's not that he was the first person to make those plots. There are other plots of citation networks before. So Sid Redner, for example, had already done some analyses of citation networks, he's a theoretical statistical physicist over at BU, but just now, I guess, moving over to the Santa Fe Institute. But it's not that he was the first person to make that observation, but he knew there was something interesting that needed to explained. So I'd say that for any of you that are thinking about doing theory, or writing down models, I would say, whenever possible start with an interesting observation. So can somebody-- maybe you guys could just**

11

||**throw out, what are some examples of nodes and edges that were given there or**<br>**elsewhere?**|
|---|---|
|**AUDIENCE:**|**Web pages and links.**|
|**PROFESSOR:**|**Right, web pages and links. And is this a directed or undirected?**|
|**AUDIENCE:**|**Directed.**|
|**PROFESSOR:**|**So this is indeed directed. Some others?**|
|**AUDIENCE:**|**Movie stars and movies.**|
|**PROFESSOR:**|**Movie stars and movies. This one's a funny one, rig-- So movie stars and then this**<br>**is like being in a movie together, right? So co-starring or so. Others?**|
|**AUDIENCE:**|**Articles and Citations.**|
|**PROFESSOR:**|**Articles and citations. And this is again directed, and this is not directed, right? And**<br>**we can maybe even try to remind ourselves, this fell off as alpha was equal to what?**<br>**I guess it was 3, I think they said. Actors work around 2.3, I guess they said. The**<br>**web was 2.1. Just because it's a power law doesn't mean that it's always going to**<br>**have the same alpha right?**|
||**But for example, what this means is that for every paper that has say 200 citations,**<br>**there are going to be roughly 10 papers that have 100 citations. If you increase k by**<br>**a factor of 2, you get almost an order of magnitude in terms of the probability**<br>**distribution.**|
||**So this is an interesting observation, and where Barabasi came in and said, well,**<br>**what would be a model that would recapitulate this? And what are the models that**<br>**did not recapitulate it?**|
|**AUDIENCE:**|**[INAUDIBLE].**|
|**PROFESSOR:**|**Right. So the Erdos Renyi-- so other models, there's the E R, other models, there's**<br>**the Erdos Renyi network, random network, and that's because here the degree**|


12

**distribution is peaked around something and then falls off exponentially as you go above that. And this is actually where I think the equations are wrong in this paper. Because if you look at the paper, page 510, where they say the Erdos Renyi, you connect the edges of probability p, and then they say you get a poisson distribution, p of k, where lambda the mean is something, but then they say, oh lambda is equal to some binomial of something of k, and so forth. So I think this is all not true, but rather that you can approximate the binomial with a poisson in the limit of small Ps. So be aware if you're looking at that.**

**I know-- there was another network that-- Do you have a question?**

---

[← AUDIENCE](07-audience.md) · [Up: contents](index.md) · [AUDIENCE →](09-audience.md)
