---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/iklvcufd1ma-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/iklvcufd1ma-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**All right, well, good afternoon and welcome back. We have an exciting fun-filled program for you this afternoon. I'm David Gifford. I'm delighted to be back with you again, here in computational systems biology.**

**Today we're going to talk about chromatin structure and how we can analyze it. And to give you the narrative arc for our discussion today, we're first going to begin with looking at computational methods that we can break the, quote unquote code, that describes the epigenome.**

**Now, epigenetic state is extraordinarily important and one way you can visualize this is that the genome is like a hotel filled with lots of different rooms. And a lot of the doors are locked and some of the doors are unlocked.**

**And only in the doors that we can go into, where the genome is open and accessible can there actually be work done, regulation performed and transcripts and proteins made.**

**So we're going to talk about how to actually analyze epigenetic state. And then we're going to talk about how to use epigenetic information to understand the entire regulatory occupancy of the genome.**

**We've already talked about ChIP-seq and the idea that we can understand where individual regulators sit on the genome, and how they regulate proximal genes.**

**We're now going to see if we can learn more about the genome. How it's state-whether it's open or closed. Is it self-regulated? And answer a puzzle.**

**The puzzle is, if there are hundreds of thousands of possible binary locations that are equally good for a regulator, why are only tens of thousands occupied? And**

1

**how are those sites picked? Because that level of regulation is extraordinarily important to establish a basal level of what genes are accessible and operating.**

**And finally, we're going to talk about how we can map, which regulatory regions in the genome are affecting which genes. It turns out that about 1/3 of the regulatory sites in the genome skip over a gene that's closest to them to regulate a gene that's farther away.**

**This is a million genomes. And so given that rough approximation, how is it that we can make connections between regulatory sites and the genes that they control?**

**Now, in computational systems biology, we always talk a lot about biology, but we also need to reflect upon the computational methods that we're bringing to bear on these questions.**

**And so, today, we're going to be talking about three different methods. We'll talk about dynamic Bayesian networks as a way to approach, understanding the histone code.**

**We'll talk about how to classify factor binding, using log likelihood ratios. And finally, we'll turn to our friend, the hypergeometric distribution to analyze which locations in the genome are interacting with one another.**

**So let's begin with establishing a vocabulary. I'm sure some of you have seen this before. This is the way that chromatin can be thought of being organized at different levels. There's the primary DNA sequence, which can include methylated CPGs.**

**That's cysteine, phosphate, guanine. And the nice thing about that is that it's symmetrical so that when you have a CPG, a methyltransferase during DNA replication can copy that methy mark over. So it's a mark that's heritable.**

**The next level down are histone tails. On the amino terminus of histones H3 and H4, different chemical modifications can be made, and they serve as sign posts, as we'll see, to give us clues about what's going on in the genome in that proximal location.**

2

**The next level down is, whether or not the chromatin is compacted or not. Whether it's open or closed. And that relates to whether or not DNA binding proteins are actually on the genome.**

**And finally, certain domains of the genome can be associated with the nuclear lamina. And so they're different levels of organization of chromatin. And we'll be exploring all of these today.**

**So the cartoon version of the way that the genome is organized is that at the top we have a transcribed gene. And you can see that there's an enhancer that is interacting with the RNA polymerase II start site.**

**And you can see varied histone marks that are associated with this activated gene. There are also marks that are associated with that active enhancer.**

**Down below, you see an inactive gene. And you can see that there's a boundary element that's bound by CTCF, which, one of its function is to serve as a genomic insulator, which insulates the effect of the enhancer above from the gene below.**

**So through careful biochemical analysis over the years, these different marks have been analyzed and characterized. And a general paradigm for understanding how the marks transition as genes are activated is shown here.**

**So genes that are fairly active and cycle between active and inactive states typically have a high CPG content in their promoters. And transition is shown on the left.**

**Where in the repressed state on the bottom, they're marked by H3K27 trimethyl marks. When they're poised, they have both H3K4 trimethyl and H3K27 trimethyl. And when they're active, they only have H3K4 trimethyl.**

**And on the right hand side are genes that are less active. So in their completely shut down state, they may have no marks, but the DNA is methylated, silencing that region of the genome. And other marks then, culminating in H3K4 trimethyl once again when they become active at the top.**

3

**So I'm summarizing for you here, decades of research in histone marks. And it has been summarized in figures like this, where you can look at different classes of genetic elements-- whether they be promoters in front of genes, gene bodies themselves, enhancers, or the large scale repression of the genome-- and you can look at the associated marks with those characteristic elements.**

**OK, so, how can we learn this de novo? That is, you could memorize, and of course it's important to understand, for example, if you want to look for active enhancers in the genome, that looking for things like H3K4 monomethyl and H3K7 27 acetyl marks together, would give you a good clue where the enhancers are in the genome that are active.**

**But if we want to learn all this de novo, without having to memorize it or rely upon the literature, the great thing is that there's a lot of data out there now that characterizes, or profiles all these marks, genome-wide, in variety of cellular states. And there's the epigenome roadmap initiative to look at this in hundreds of different cell types.**

**So, what is the histone code? That is, how can we unravel the different marks present in the genome and understand what they mean? Because the genome doesn't come ready-made with those little cute labels that we had on it-- enhancer, gene body, and so forth.**

**So somehow, if we want to understand the grammar of the genome and its function, we're going to need to be able to annotate it, hopefully with computational help.**

**So here's a picture of what typical data looks like along the genome. So, obviously you can't read any of the legends on the left-hand side. If you want to look at the slides that are posted on Stellar, you can see the actual marks.**

**But the reason I posted this is because you can see the little pink thing at the top-that's where the RNA transcript has been mapped to the genome. The actual annotated genes are above. And then down below you can see a whole collection of histone marks and other kinds of chromatin information that have been mapped to**

4

**the genome and spatially create patterns that are suggestive of the function of the genomic elements, if they're properly interpreted.**

**And below, you see in blue, the binding of different TFs, as determined by ChIPseq.**

**So, what we would like to do then, is to take this kind of information and automatically learn, or automatically annotate the genome as to its functional elements.**

**Let me stop here and ask, how many people have seen histone mark information before? OK. And how many people have used it in their research? Not too many-- a couple people? OK.**

**So it's getting quite easy to collect and there are a couple of ways of analyzing this kind of data, genome-wide. One way is that we could run a hidden Markov model over these data and predict states at regular intervals. For example, every 200 bases down the genome, and see how the HMM transition from state to state and let the state suggest what the underlying genome elements that we're doing.**

**Another way is to use a dynamic Bayesian network. So a dynamic Bayesian network is simply a Bayesian network. We've talked about those before. And it models data sampled along the genome. And so it's a directed acyclic graph.**

**There are tools out there that allow us to learn these models directly. And it allows us, as we'll see, to analyze the genome at high resolution, and to handle missing data.**

**So we'll be talking about Segway, which is a particular dynamic Bayesian network that takes the kind of data we saw on the slide before and essentially parses it into labels that allow us to assign function to different genomic elements. And it does this in an unsupervised way. What I mean by that is that it is automatically learning the states, and then afterwards we can look at the states and assign meaning to them.**

**So here is the dynamic Bayesian network that Segway uses. And let me explain this**

5

**somewhat scary looking diagram of lots of little boxes and pointers to you.**

**The genome is described through the variables on the bottom-- the observation variables, going from left to right, where each base is a separate observation variable which consists of the level of a particular histone mark at a particular based position as described by mapped reads to that location.**

**The little square box-- the little boxes that says "x" on it with the other small print you can't read-- is simply an indicator, whether or not the data is present. If the data is absent, we don't try and model it. If that box contains a zero, we don't model the data. If the box is one, then we attempt to model the data.**

**And the most important part of the dynamic Bayesian network is the q box above, where those are the states. And each state describes an ensemble of different histone marks that are output.**

**And so the key thing is that for each state we learn what marks it's outputting. And the model learns this automatically through a learning phase. The boxes above simply are a counter.**

**And the counter allows us to define maximum lengths for particular states, so states don't run on forever. So unlike a hidden Markov model that doesn't have that kind of control, we can adjust how long we want the states to last.**

**So this model, if you turned it 90 degrees and rotated it clockwise, would be more familiar to you because all the arrows would be flowing from the top of the screen down. There are no cycles in this directed acyclic graph.**

**And therefore, it can be probabilistically viewed and learned in the same framework that we learn a Bayesian network. In fact, it is a Bayesian network. The reason it's called dynamic is because we are learning temporal information, or in this case, spatial information with these different observations along the bottom of the model.**

**Now before I go on, perhaps somebody could ask me a question about the details of these dynamic Bayesian networks, because the ability to automatically assign**

6

**labels to genome function, given the histone marks is really a key thing that's gone on the last couple of years. Yes?**

- **AUDIENCE: Could you re-explain that-- what the labeled-- the second [INAUDIBLE] was all about?**

- **PROFESSOR: Sure. So the Q label is right here, these labels. And each of these Q labels defines one of a number of states. For example, 24 different states. In a given state, describes the expected output in terms of what histone marks are present in that state.**

**So it's going to describe the means of all those different histone marks. 24 different means, let's say, of the marks it's going to output. And the job of fitting the model is picking the right states, or a set of 24 states, each of which is most descriptive of its particular subset of chromatin marks. And then defining how we transition between states.**

**So we not only need to define what a state means in terms of the marks that it outputs, but also when we transition from one state to another. Does that make sense to you?**

**AUDIENCE: So I know it states the information that tells at each of the Q boxes. Is that a series of probabilities? Or is it something else?**

**PROFESSOR: It's actually a discrete number, right. So it actually is a single-- there's only a single state in each Q box. So it might be a number between 1 and 24 that we're going to learn. And based upon that number, we're going to have a description of the marks that we would expect to see at the observation at that particular genomic location.**

**And so our job here is to learn those 24 different states and what they output in the training phase, and then once we've trained the model, we can go back and look at other held out data, and then we can decode the genome. Because we know what the states are, and we know what they are supposed to be producing, we can use a Verterbi decoder and go back and-- as we did with the**

7

**HMM and we learned the HMM-- go back and read off on the histone mark sequence and figure out what their relative states are for each base position of the genome. Is that helpful? Yes?**

**Any other questions about dynamic Bayesian networks? Yes?**

**AUDIENCE: How do you choose the number of states?**

**PROFESSOR: That's a very good question. How do you choose the number of states? Well, if you choose too many states, they obviously don't really become descriptive and you can become over fit and then can start fitting noise to your model.**

**And if you choose too few states, what will happen is, that states can get collapsed together and they won't be adequately descriptive. The answer is, it's more or less trial and error. There really isn't a principled way to choose the right number of states in this particular context. Now, you could do--**

**AUDIENCE: What's the trial, then? You run it and you get a set of things, and what do you do with those labels?**

**PROFESSOR: What do you do with labels?**

**AUDIENCE: Yeah, how do you evaluate it?**

**PROFESSOR: You typically, in both of these cases-- both in the case of chrome HMM and this-you rely upon the previous literature. And we saw on that slide earlier, what marks are associated with what kinds of features.**

**So you use the prior literature and you use what the states are telling you they're describing to try and associate those states with what's known about genome function. All right, yes?**

**AUDIENCE: Where does that information concerning the distance between states go again? Like, the counter? Like, how does that control how long the states go on and whether or not--**

8

---

[Up: contents](index.md) · [PROFESSOR →](02-professor.md)
