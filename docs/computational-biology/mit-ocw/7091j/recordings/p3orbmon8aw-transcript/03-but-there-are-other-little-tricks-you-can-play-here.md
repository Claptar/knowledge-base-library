---
title: But there are other little tricks you can play here.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/p3orbmon8aw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# But there are other little tricks you can play here.

**Source:** `recordings/p3orbmon8aw-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Any other questions? Yes.**

**AUDIENCE: I'm Deborah. What is the FM index? PROFESSOR: What is the FM index. Well, the guys who thought this up have the last initials of F and M, but that's not what it stands for, contrary to popular opinion. It stands for full text minute size. That's what they claim. So if you hear people talking about full text minute size indices, or FM indices, the Fm index is actually the part that was being asked over here, the Occ part and the LF part, how you actually compute those quickly.**

**That was what FNM contributed to this but, generically when we're talking about this style of indexing, it's called FM indexing or you might hear, I'm using a BWT. Some people will say that. But that's what FM stands for. Does that answer your question? Excellent. OK. All right. Any-- these are all great questions. Yes.**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: Oh, you don't know that a and c are there, except that remember, if you look at the way that this is working, is that you're not actually reconstructing strings, you're only trying to find them. Right? And so at the end, top and bottom are going to point to the row that contains the suffix where your original read was. And now your next question is going to be, where is that in the genome? This doesn't do me any good. I mean, the number 1 doesn't help me out here, doesn't mean anything. Not good, right? So where is it in the genome is the next question. So we'll get to that in a second. What happens if you give me a read that doesn't match anywhere in this index? Well if you give me a read that doesn't match anywhere in this index, what happens is the top and bottom become the same. So on top and bottom become the same, it's a failed look up. All right?**

**And that's because the suffix doesn't exist in the index. And once top and bottom**

21

**become the same, they remain the same throughout that loop. Yes. AUDIENCE: I'm Sally. My main question is that this doesn't provide any leeway for errors. You kind of have to be able to present all of your rates. PROFESSOR: Sally, you're absolutely correct. I'm so glad you asked that question. Your observation is it does not provide any leeway for mismatches. And so unlike all the other algorithms we study, which had these very nice matrices and ability to assign weights to mismatches, this is only doing exact matching. And so what you need help understanding is, how we can deal with mismatches in the presence of this. And I'll get to that in less than 10 minutes. And it won't be quite as elegant as what you saw from Professor Berg but it's what everybody does. So that's my only excuse for it OK? Yes.**

**AUDIENCE: What is the bottom set of arrows doing? What's its significance?**

**PROFESSOR: The significance of top and bottom, that's a great question. What the significance of top and bottom? Top and bottom bracket in that original matrix, the suffixes that are matching the original query. OK? And so between top and bottom minus 1 are all of the rows that have a suffix that match our original query. And if top equals bottom, there are no matching suffixes. But assuming there are matching suffixes, those are rows that contain a matching suffix. And as we progress along, top and bottom change as the suffixes change as we expand the suffix to contain more and more bases.**

**OK? OK. Any other questions? OK. So now back to the question over here, which is that OK, I know that we've matched, and I know that we have this hit. The question is, where is it in the Genome because the fact that it matched row one of my BWT matrix does me absolutely no good at all. Right?**

**Anybody have any ideas about how we could figure out where it is the genome? Given what I've told you so far, which is that you have the BWT, you have Occ, and you have count, and you can compute the LF function. Any ideas? Doesn't matter how slow it is.**

22

**OK well how could I figure out what came before aac in the genome? Yes. AUDIENCE: So, for, like at the beginning, we rebuilt this whole string, starting at the end. You could rebuild the whole string starting at, rebuild the whole genome starting at the 1 and see-PROFESSOR: You could rebuild the entire genome that prepends or occurs before aac, right? AUDIENCE: Exactly.**

- **PROFESSOR: Exactly. So that's what we can do. We could actually do our walk left algorithm. We can walk left from there, find out that we go two steps until we hit dollar sign, and therefore, the offset is two, where it occurs in the genome. So we can give a match position by walking left. Does everybody see that, that we could walk left to figure where it is? It's not fast, but it works. Yes.**

- **AUDIENCE: I'm Ted.**

- **PROFESSOR: Hi, Ted. AUDIENCE: So now our function first has to take the read and it has to align it and the same, where the position is built into the end of the function, the speed of the function is now dependent on position as well. Is that right? Because the longer it takes,**

- **PROFESSOR: I was being a little bit glib find if it matches or not this linear time. Now you're saying, hey, wait a minute. I want to know where it is in the genome. That's a big bonus, right? And so you'd like to know where that is? Yes. But I still can do that in linear time. And we'll show you how to do that in a second. This is not linear time. This actually needs to walk back, order the length of genome for every single query. That's not good. All right? Well,**

**What we could do is, we could store what's called a suffix array with each row and say, where in the genome that position is. Where that row starts. And then maybe a simple look-up. That when you actually have a hit in row one, ah, OK, start your**

23

---

[← AUDIENCE](02-audience.md) · [Up: contents](index.md) · [position two of the genome. →](04-position-two-of-the-genome.md)
