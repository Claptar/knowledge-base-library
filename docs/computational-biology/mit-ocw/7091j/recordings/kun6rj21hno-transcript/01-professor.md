---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kun6rj21hno-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/kun6rj21hno-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**All right. We should probably get started. So RNA plays important regulatory and catalytic roles in biology, and so it's important to understand its function. And so that's going to be the main theme of today's lecture.**

**But before we get to that, I wanted to briefly review what we went over last time. So we talked about hidden Markov models, some of the terminology, thinking of them as generative models, terminology of the different types of parameters, the initiation probabilities and transition probabilities and so forth. And Viterbi algorithm, just sort of the core algorithm used whenever you apply HMMs. Essentially, you always use the Viterbi algorithm.**

**And then we gave as an example the CpG Island HMM, which is admittedly a bit of a toy example. It's not really used in practice, that illustrates the principles. And then today we're going to talk about a couple of real world HMMs.**

**But before we get to that, I just wanted to-- sort of toward the end, we talked about the computational complexity of the algorithm, and concluded that if you have a case state HMM run on a sequence of length L, it's order k squared L. And this diagram is helpful to many people in sort of thinking about that.**

**So you can have transitions from any state-- for example, from this state-- to any of the other five states, and there's five-state HMM. And when you're doing the Viterbi, you have to maximize over the five possible input transitions into each state. And so the full set of computations that you have to do from going from position i to i plus 1 is k squared. Does that make sense? And then there's L different transitions you have to do, so it's k squared L.**

**Any questions about that? OK. All right and, so the example that we gave is shown**

1

**here. And what we did was to take an example sort of where you could sort of see the answer-- not immediately see it, but if we're thinking about it a little, figure out the answer. And then we talked about how the Viterbi algorithm actually works, and why it makes the transitions at the right place.**

**It seems to intuitively like it would make a transition later, but actually transitions at the right place. And one way to think about that is that these are not hard and fast decisions because you're optimizing two different paths. At every state, you're considering two possibilities.**

**And so you explore the possibility of-- the first time you hit a c, you explore the possibility of transitioning from genome to island, but you're not confirming whether you're going to do that yet until you get to the end and see whether that path ends up having a higher probability at the end of the sequence than the alternative. So that's sort of one way of thinking about that. Any questions about this sort of thing, how to understand when a transition will be made?**

**And I want to emphasize, for this simple HMM, we talked about you can kind of see what the answer's going to be. But if you have any HMM, any sort of interesting real world HMM with multiple states, there's no way you're going to be able to see it. Maybe you could guess what the answer might be, but you're not going to be able to be confident of what that is, which is why you have to actually implement it.**

**All right, good. Let's talk about a couple of real world HMMs. So I mentioned gene finding. That's been a popular application of HMMs, both in prokaryotes and eukaryotes. There's some examples discussed in the text.**

**Another very popular application are so-called profile HMMs. And so this is a hidden Markov model that's made based on a multiple alignment of proteins which have a related function or share a common domain. For example, there's a database called Pfam, which includes profile HMMs for hundreds of different types of protein domains.**

**And so once you have many dozens or hundreds or thousands of examples of a**

2

**protein domain, you can learn lots of things about it-- not just what the frequencies of each residue are in each position, but how likely you are to have an insertion at each position. And if you do have an insertion, what types of amino acid residues are likely to be inserted in that position, and how often you are likely to have a deletion at each position in the multiple alignment.**

**And so the challenge then is to take a query protein and to thread it through all of these profile HMMs and ask, does it have a significant match to any of them? And so that's basically how Pfam works. And the nice thing about HMMs is that they allow you to-- if you want to have the same probability of an insertion at each position in your multiple alignment, you can do that. But if you have enough data to observe that there's a five-fold higher likelihood of having an insertion at position three in a multiple alignment than there is at position two, you can put that in. You just change those probabilities.**

**So in this HMM, each of the hidden states is either an M state, which is a match state, or an I state, or an insert state. And so those will emit actual amino acid residues. Or it could be a delete state, which is thought of as emitting a dash, a placeholder in the multiple alignment. So these are also widely used.**

**And then one of my favorite examples-- it's fairly simple, but it turns out to be quite useful-- is the so-called TMHMM for prediction of transmembrane helices in protein. So we know that many, especially eukaryotic proteins, are embedded in membranes. And there's one famous family of seven transmembrane helix proteins, and there are others that have one or a few transmembrane helices. And knowing that a protein has at least one transmembrane helix is very useful in terms of predicting its function.**

**You predict it's localization. And knowing that it's a seven transmembrane helix protein is also useful. And so you want to predict whether the protein has transmembrane helices and what their orientation is. That is, proteins can have their end terminus either inside the cell or outside the cell. And then of course, where exactly those helices are.**

3

**And this program has about a 97% accuracy, according to [? the author. ?] So it works very well. So what properties do you think-- we said before that you have to have strongly different emission probabilities in the different hidden states to have a chance of being able to predict things accurately. So what properties do you think are captured in a model of transmembrane helices? What types of emission probabilities would you when you have for the different states in this model? Anyone?**

**So for this protein, what kind of residues would you have in here? Oops, sorry. I'm having trouble with this thing. All right, here in the middle of the membrane, what kind of residues are you going to see there?**

---

[Up: contents](index.md) · [AUDIENCE: [INAUDIBLE] →](02-audience-inaudible.md)
