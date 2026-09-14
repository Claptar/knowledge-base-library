---
title: PROFESSOR
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/bjxcf6pfrha-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/bjxcf6pfrha-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Today what we want to do is use the two papers that you read as kind of a backdrop to try to think something about the regulation of genes in response to changing environments. So there's the Mitchell paper that is talking about this idea of anticipatory regulation, whereby if the environmental changes have some typical pattern, then maybe the cells can take advantage of that and start preparing for environment number two when the cell sees environment number one.**

**But in other cases, it may be that the environment fluctuates in ways that are really fundamentally unpredictable. In that case, you can't use the sort of anticipatory regulation strategy, but instead, there may be a way that you can just stochastically switch between the different strategies and implement what's known as a bet hedging strategy. And this is modeled largely on the work that you just read about in the Kussell paper, Science maybe May 2005.**

**I do want to stress, however, that if you observe phenotypic heterogeneity in a clonal population, that does not necessarily mean that the cell or the population is implementing one of these bet hedging strategies. In particular, I would argue rather strongly that there are other possible evolutionary drivers for such phenotypic heterogeneity in the population.**

**First of all, just because you see some phenomena does not mean it is necessarily selected for. So it's possible that it's a side effect of something else. However, if you're looking for an evolutionary kind of explanation for something like this, bet hedging is not the only one. In particular, we'll talk about two other possible explanations, and they both have to do with kind of game dynamics that we might illuminate or talk about.**

1

**But I guess our game theory talk was-- that was a week and a half ago, almost two weeks ago now-- so maybe you've forgotten all the game theory that we discussed. But in particular, it could be that the phenotypic heterogeneity might be the implementation of a mixed strategy. Or possibly it could be an example of some sort of altruistic self-sacrifice. And we'll try to explain the theory behind each of these three things as well as possible biological examples of each of the three.**

**In this case, we may think about bet hedging as maybe an explanation for antibiotic persistence, this idea that cells can switch into these slow-growing persister states in which they're resistant to antibiotics and other stresses. Mixed strategies could be-- well, we're going to argue it could be implemented in the context of mixed sugar environments. And altruistic self-sacrifice may be the explanation behind colicin production in bacteria, so it's a toxin.**

**So I want to start by thinking about this thing about adaptive prediction of environmental changes by Mitchell. I think this is a very interesting paper in a number of different ways. One is, I think that it's sort of a big idea that can be explored in these simple experiments. I think that it's an exceptionally clear paper in some ways, and that they really say, oh, we're going to propose that this strategy should be characterized by these three things. And then they go and they try to show you the three things.**

**The figures, I think, are also very nice, in the sense that in many of the cases you could have shown the data just in the context of a table, where you said, oh, for each of these strains, this is the up regulation or so. But if you had done that, it would've been much, I think, less compelling, even though of course it's the same data.**

**So I think this is a neat paper, in my opinion, both from the standpoint of the ideas that are being explored, but also because it highlights some of the things that you should be thinking about when you're writing your own papers. You want to try to make the ideas as clear as possible. You want to lay the groundwork so that what you're about to show is going to be-- the reader's going to feel is a really important**

2

**thing. And then you want to take nice advantage of color and some legends that are there. So we'll kind of talk about all these issues as we go.**

**But before we get started, can somebody-- there's a very real sense that in this field of decision making and systems biology that a lot of this research program is kind of driven by following classic ideas from other fields. And what would be the corresponding classic idea this paper is exploring?**

**AUDIENCE: Conditioning.**

**PROFESSOR: Conditioning. Right. And whose name do we associate with conditioning typically? AUDIENCE: Pavlov.**

**PROFESSOR: Pavlov. All right. So I have not ever read these studies. Pavlovian conditioning. And I think that this is just-- it's good to highlight. This is something that you might have learned in your high school psychology class. And it's, again, a big idea, but it's not the kind of thing-- we've all heard-- well, we're going to talk about this in a moment.**

**Many of us, I think, have heard of this. But this is an example of how you take something that you learned in high school and you make it useful to your daily life, or pseudo daily life. Because I think you'll see that there are many kind of examples of this throughout this literature, where someone takes an idea that is, in some ways, you open up a random textbook in introductory psychology, and you can just march through and try to see to what degree the ideas that were developed in the context of humans or animals, to what degree might they be relevant in the context of cell decision making?**

**Can somebody just say what is this Pavlovian conditioning idea? Did you guys take high school psychology? I'm sure somebody did. No. All right. Well, incidentally, I recommend everybody should take a solid introductory psychology class if you have not done so. We offer a class 900. I'm sure that it's good and interesting. Yes.**

**AUDIENCE: So there's two different events or stimuli, and in Pavlovian conditioning you give one and then always give the other one following.**

3

**PROFESSOR: That's right. So there's some sense that what we might call-- there are two events of some sort. One is following the other one, so it's A and then followed by B. And people have done many different examples of this, but what's the one that we typically-- what's the classic experiment that Pavlov did?**

**AUDIENCE: You ring a bell, and then you get food.**

- **PROFESSOR: Yeah. Right. So you ring a bell and then you give-- and this is dogs, at least in the version I remember. So you have some dogs, you do this thing where you ring the bell and then you give them the food. And what's the response that you're supposed to get?**

- **AUDIENCE: Drooling.**

**PROFESSOR: Yeah, right. So the dog is supposed to start salivating. OK. So you might think your experiments are gross, but-- right. So ring a bell, and the idea is that you can train the dog to start salivating in response to the bell, rather than, of course, if you give the food they're going to start salivating. But here you can train the dog to start salivating in response to the food.**

**So now, with training, this results in salivation. And did Pavlov show there was a fitness benefit associated with the salivation? Not that I'm not I'm aware of. But this is the classic story that we learned in introductory psychology. And the question is, can we apply a similar idea in the case of microbial decision making?**

**Now was this-- can somebody say what they think was the author's contribution to the literature in the sense of-- via a vis this? How much of what-- well, we can be maybe more concrete. In the case of E. coli, what was known-- or maybe we should describe the experiment once more and then try to figure out what they did that was new new. At least can somebody kind of summarize the basic idea with E. coli?**

- **AUDIENCE: We know that they have a certain metabolic life cycle and that they exist in different environments.**

**PROFESSOR: OK. So that E. coli existent in different environments. And what environments are**

4

---

[Up: contents](index.md) · [you referring to? →](02-you-referring-to.md)
