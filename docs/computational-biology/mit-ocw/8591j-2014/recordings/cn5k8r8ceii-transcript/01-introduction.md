---
title: Introduction
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/cn5k8r8ceii-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/cn5k8r8ceii-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**MITOCW | watch?v=Cn5K8R8cEiI**

**The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high-quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: So today, what we want to do is we want to talk about two related topics. The first is going to this question of the evolution of virulence and how to model host-parasite interactions more broadly. That's kind of modeled on chapter 11 of Martin's book. We'll focus on the first half of it for the discussions today.**

**This is in the context of when a given host can only have one strain of the parasite or virus or whatnot inside that body. The model presented in Martin's book is very similar to classic models in epidemiology, which are the so-called SIR type models, where you divide up the host population into whether the they are sensitive-- i.e., non-infected-- infected, or resistant.**

**And then, we'll draw the parallels of how we get from the model that you read about in Martin's book to the classic SIR models. But in both of these cases, the fundamental parameter that drives these things is this R0 parameter. It tells us about the expected number of new cases that will result when you introduce one infected member into the population.**

**AUDIENCE: Sorry, will you be taking about super-infections?**

**PROFESSOR: Only a little bit but, I would say, depending on time. But if you're interested in the super-infection discussion more, we can talk about it after class, maybe. All right. And so, for the second half of class, what we're going to do though is we're going to talk about the possible evolutionary benefits of sex.**

**And in particular, we'll talk about this hypothesis, which is one of the reigning hypotheses for why it might be that sex is as widespread as it is, which is the Red Queen hypothesis, from Lewis Carroll's novel. And we're going to discuss this paper that you guys read about, "Running with the Red Queen," which I think has a nice**

1

**discussion of this debate and, then, some nice experiments looking at experimental coevolution between the C. elegans worm and it's infecting parasite, which is a serratia bacterium. Any questions before we get going?**

**OK, what I want to do is start by discussing this model in Martin's book. But also, there's a little bit of this philosophical question. Any time, that you are modeling, you always had to make decisions about which of the details you want to try to model and which of the details you do not want to model.**

**And depending upon the situation, it may be that some assumptions are more or less appropriate than others. Now, in the model that Martin wrote down-- well, we'll try to figure out what the assumptions are here.**

**So we have what you might think of as some sensitive individuals. Plus, the infected individuals are going to interact at some rate, beta. So this is how the sensitive become infected. And it results in, now, two infected individuals. Now of course, each of these individuals will, say, have some lifespan or die at some rate.**

**All right, so the sensitive or uninfected individuals die at rate u. Whereas, infected individuals, others-- an increase in the death-rate, described by some virulence, v. OK? OK. Now, the model as written-- what's going to be the fate of the population?**

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
