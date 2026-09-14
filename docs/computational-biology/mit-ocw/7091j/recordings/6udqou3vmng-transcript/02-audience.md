---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6udqou3vmng-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/6udqou3vmng-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**I'm Simona. So the ribonucleotide is the top right. The deoxy is the one below it. And the dideoxy is the one to the left.**

**PROFESSOR: OK, so that is correct. So one way to keep these things in mind is the numbering of the bases. So the carbons in the ribo sugar are numbered one, so carbon 1 is the one where the base is attached. Two is here, which has an OH in RNA and just an H in DNA. And then three is very important. Four, and then five. So five connects to the phosphates, which then will connect the base to the sugar phosphate backbone. And three is where you extend. That's where you're going to add the next base in a growing chain.**

**And so what will happen if you give DNA polymerase a template and some dideoxy nucleotides? It won't be able to extend because there's no 3-prime OH. And all the chemistry requires the OH. And so that's the basis of classical or Sanger sequencing, which Fred Sanger got the Nobel Prize for in the 1980s-- I think it was developed in the '70s-- and it's really the basis of most of the sequencing, or pretty much all the DNA sequencing up until the early 2000s before some newer technologies came about. And it takes advantage of this special property of dideoxy nucleotides that they terminate the growing chain.**

**So imagine we have a template DNA. So this is the molecule whose sequence we want to determine shown there in black. We then have a primer. And notice the primer's written in 5-prime to 3-prime direction. The ends would be primer sequences and then primer complimentary sequences in the template. So you typically will have your template cloned-- this is in conventional sequencing-- cloned into some vector like a phage vector for sequencing so you know the flanking sequences.**

2

**And then you do four sequencing reactions in conventional Sanger sequencing. And I know some of you have probably had this before. So let's take the first chemical reaction. The one here with a DDGTP. So what would you put in that reaction? What are all the components of that reaction if you wanted to do conventional sequencing on, say, an acrylonitrile? Anyone? What do you need and what does it accomplish? Yeah, what's your name?**

**AUDIENCE: I'm Tim. PROFESSOR: Tim? Oh yeah, I know you, Tim. OK, go ahead. AUDIENCE: So you need the four nucleotides-- the deoxynucleotides. You will need the dideoxy P nucleotides. In addition, you need all the other [INAUDIBLE]. You need polymerase. Generally, you need a buffer of some sort, [INAUDIBLE], to [INAUDIBLE]. PROFESSOR: Yeah, primary template. Yeah. Great. That's good. It sounds like Tim could actually do this experiment. And what ratio would you put in? So you said you're going to put in all four conventional deoxynucleotides and then one dideoxynucleotide. So let's say dideoxy G just for simplicity here. So in what ratio would you put the dideoxynucleotide compared to the conventional nucleotides? AUDIENCE: To lower the concentration. PROFESSOR: Lower? Like how much lower? AUDIENCE: Like, a lot lower. PROFESSOR: Like maybe 1%? AUDIENCE: Yeah. PROFESSOR: Something like that. You want to put it a lot lower. And why is that so important? AUDIENCE: Because you want the thing to be able to progress. Because you need enough of the ribonucleotide concentration so that [INAUDIBLE] every [INAUDIBLE] equivalent**

3

**or excess and you're going to terminate [INAUDIBLE].**

**PROFESSOR:**

**Right. So if you put equamolar deoxy G and dideoxy G, then it's going to be a 50% chance of terminating every time you hit a C in the template. So you're going to have half as much of the material at the second G, and a quarter as much as the third, and you're going to have vanishingly small amounts. So you're only going to be able to sequence the first few C's in the template. Exactly. So that's a very good point.**

**So now let's imagine you do these four separate reactions. You typically would have radiolabeled primer so you can see your DNA. And then you would run it on some sort of gel. This is obviously not a real gel, but an idealized version. And then in the lane where you put dideoxy G, you would see the smallest products. So you read these guys from the bottom up.**

**And in this lane there is a very small product that's just one base longer than the primer here. And that's because there was a C there and it terminated there. And then the next C appears several bases later. So you have sort of a gap here.**

**And so you can see that the first base in the template would be a complement of T, or C. And the second base would be, you can see, the next smallest product in this dideoxy T lane, therefore it would be A. And you just sort of snake your way up through the gel and read out the sequence. And this works well.**

**So what does it actually look like in practice? Here are some actual sequencing gels. So you run four lanes. And on big polyacrylamide gels like this. Torbin, you ever run one of these?**

**AUDIENCE: Yes.**

**PROFESSOR: Yes? They're a big pain to cast. Run for several hours, I think. And you get these banding patterns. And what limits the sequence read length? So we normally call the sequence generated from one run of a sequencer as a read. So that one attempt to sequence the template is called a read.**

4

**And you can see it's relatively easy to read the sequence toward the bottom, and then it gets harder as you go up. And so that's really what fundamentally limits the read length, is that the bands get closer and closer together. So they'll run inversely proportional to size with the small ones running faster. But then the difference between a 20 base product and a 21 might be significant. But the difference between a 500 base product and a 501 base product is going to be very small. And so you basically can't order the lanes anymore. And therefore, that's sort of what fundamentally limits it.**

**All right. So here we had to run four lanes of a gel. Can anyone think of a more efficient way of doing Sanger sequencing? Is there any way to do it in one lane? Yeah, what's your name?**

**AUDIENCE: Adrian. You can use four different types of the entities. Maybe like four different colors.**

**AUDIENCE: Four different colors. OK, so instead of using radio labeling on the primary, you use fluorophore on your dideoxy entities, for example. And then you can run them. Depending where that strand terminated, it'll be a different color. And you can run them all in one lane. OK, so that looks like that.**

**And so this was an important development called terminator sequencing in the '90s. That was the basis of the ABI 3700 machine, which was really the workhorse of genome sequencing in the late '90s and early 2000s. Really what enabled the human genome to be sequenced.**

**And so one of the other innovations in this technology was that instead of having a big gel, they shrunk the gel. And then they just had a reader at the bottom. So the gel was shrunk to as thin as these little capillaries. I don't know if you can see these guys. But basically it's like a little thread here. And so each one of these is effectively-- oops! Oh no. No worries, this is not valuable. Ancient technology that I got for free from somebody.**

**So the DNA would be loaded at the top. There would be a little gel in each of these--**

5

**it's called capillary sequencing. And then it would run out the bottom and there would be a detector which would detect the four different flours and read out the sequence.**

**So this basically condensed the volume needed for sequencing. Any questions about conventional sequencing? Yes?**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [6udqou3vmng transcript Part 03 — →](03-6udqou3vmng-transcript-part-03.md)
