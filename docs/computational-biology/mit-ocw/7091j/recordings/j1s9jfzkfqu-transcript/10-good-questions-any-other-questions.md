---
title: Good questions. Any other questions?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/j1s9jfzkfqu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Good questions. Any other questions?

**Source:** `recordings/j1s9jfzkfqu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

20

**All, right so that was CASP. One was in 1995, which seems like an eon ago. So how have things improved over the course of the last decade or two?**

**So there was an interesting paper that came out recently that just looked at the differences between CASP 10, one of are the most recent ones, and CASP 5. They're every two years, so that's a decade. So how have things improved or not over the last decade in this challenge?**

**So in this chart, the y-axis is the percent of the residues that were modeled and that were not in the template. OK? So I've got some template. Some fraction of the amino acids have no match in the template.**

**How many of those do I get correct? As a function of target difficulty, they have their own definition for target difficulty. You can look in the actual paper to find out what is in the CASP competition, but it's a combination of structural and sequence data. So let's just take them that they made some reasonable choices here. They actually put a lot of effort into coming up with a criteria for evaluation.**

**Every point in this diagram represents some submitted structure. The CASP5, a decade ago, are the triangles. CASP 9, two years ago, were the squares, and the CASP10 are the circles. And then they have trend lines for CASP9 and CASP10 are shown here-- these two lines.**

**And you can see that they do better for the easier structures and worse for the harder structures, which is what you'd expect, whereas CASP5 was pretty much flat across all of them and did about as well even on on the easy structures as these ones are doing on the hard structures.**

**So in terms of the fraction of the protein that they don't have a template for that they're able to get correct, they're doing much, much better in the later CASPs than they did a decade earlier. So that's kind of encouraging. Unfortunately, the story isn't always that straightforward.**

**So this chart is, again, target difficulty on the x-axis. The y-axis is what they call the Global Distance Test, and it's a model of accuracy. It's the percent of the carbon**

21

**alpha atoms in the predictions that are close-- and they have a precise definition of close that you can look up-- that are close to the true structure.**

**So for a perfect model, it would be up here in the 90% to 100% range, and then random models would be down here. You can see a lot of them are close to random. But more important here are the trend lines. So the trend line for CASP10, the most recent one in this report, is black. And fore CASP5, it's this yellow one, which is not that different from the black.**

**So what this shows is that, over the course of a decade, the actual prediction accuracy overall has not improved that much. It's a little bit shocking. So they tried in this paper to try to figure out, why is that? I mean, the percentage of the amino acids that you're getting correct is going up, but overall accuracy has not.**

**And so they make some claims that it could be that target difficulty is not really a fair measure, because a lot of the proteins that are being submitted are now actually much harder in different sense, in that they're not single domain proteins initially. So in CASP5, a lot of them were proteins that had independent structures.**

**By the time of CASP10, a lot of the proteins that are being submitted are more interesting structural problems in that they're folding is contingent on interactions with lots of other things. So maybe all the information you need is not composed entirely in the sequence of the peptide that you've been given to test but depends more on the interactions of it with its partners.**

**So those were for homology models. These are the free modeling results. So in free modeling, there's no homology to look at, so they don't have a measure of difficulty except for length. They're using, again, that Global Distance Test. So up here are perfect models. Down here are nearly random models. CASP10 is in red. CASP5, a decade earlier, is in green. And you can see the trend lines are very, very similar. And CASP9, which is the dashed line here, looks almost identical to CASP5.**

**So again, this is not very encouraging. It says that the accuracy the models has not approved very much over the last decade. And then, they do point out that if you**

22

**focus on the short structures, then it's kind of interesting. So in CASP5, which are the triangles, only one of these was above 60%. CASP9, they had 5 out of 11 were pretty good. But then you get to CASP10 and now only three are greater than 60%. So it's been fluctuating quite a lot.**

**So modeling de novo is still a very, very hard problem. And they have a whole bunch of theories as to why that could be. They proposed, as I already said, that maybe the models that they're trying to solve have gotten harder in ways that are not easy to assess.**

**A lot of the proteins that previously wouldn't have had a homologue now already do, because there has been a decade of structural work trying to fill in missing domain structures. And that these targets tend to have more irregularity. Tendency be part of larger proteins. So again, there's not enough information in the sequence of what you're given to make the full prediction.**

---

[← Yes?](09-yes.md) · [Up: contents](index.md) · [Questions? →](11-questions.md)
