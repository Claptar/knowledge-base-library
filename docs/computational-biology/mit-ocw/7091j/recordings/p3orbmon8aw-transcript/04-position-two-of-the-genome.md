---
title: position two of the genome.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/p3orbmon8aw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# position two of the genome.

**Source:** `recordings/p3orbmon8aw-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**But then the problem with that is that it actually takes a lot of space. And we want to have compact indices. So the trick is what we do is, instead of storing that entire suffix array, we store every so many rows, like every 25 rows. And all we do is, we walk left until we hit a row that actually has the value, and then we add how many times we walked left, plus the value and we know where we are in the genome.**

**So we can sample the suffix array, and by sampling the suffix array, we cut down our storage hugely and it's still pretty efficient. Because what we can do is, we just walk left until we hit a sample suffix array location and then add the two numbers together. All right?**

**So that's how it's done. OK? So that's how we actually do the alignment and figure out where things are. The one thing I haven't told you about is how to compute count efficiently. Now remember what count does. Count is a function-- but this is putting it all together where we're matching this query, we do the steps. We get the match. Then we do walk left once and then we look at the suffix to figure out where we are, right?**

**The business about count is that what we need to do is to figure out the rank of a particular base in a position in the transform. And one way to do that is to go backwards to the whole transform, counting how many g;s occur before this one, and that's very expensive, to compute the rank of this particular g. Remember the rank is simply the number of g's that occur before this one in the BWT. Very simple metric.**

**So instead of doing that, what we can do is, we can build a data structure that every once in awhile, counts how many a's, c's, g's, and t's have occurred before now in the BWT. And so we're going to sample this with these checkpoints, and then when you want to compute count at any point, you can go to the nearest checkpoint, wherever that is, and make an adjustment by counting the number of characters between you and that checkpoint. Very straightforward. All Right**

24

**So this, coming back to question, it's Time, right? --asked you need to build this checkpointing mechanism at the same time you build the index, as well as the sampling of the suffix array. So a full index consists of the transform itself, which is the genome transformed into its BWT. And they literally take the entire genome and do this.**

**Typically they'll put dollar signs between the chromosomes. So they'll transform the whole thing. It takes a sampling of the suffix array we just saw and it takes the checkpointing of the LF function to make a constant time. And that's what is inside of an FM index. OK?**

**Now it's small, which is one of the nice things, compared to things like suffix tree, suffix arrays, or even other kinds of hash structures for looking for seeds, it really is not even twice the size of the genome. So it's a very compact index that is very, very efficient. And so it's a wonderful data structure for doing what we're doing, except we have not dealt with mismatches yet, right?**

**And so once again, I want to put a plug in for BWA which is really a marvelous aligner. And we'll talk about tomorrow in recitation if you want to know all of the details of what it actually takes to make this work in practice. Now, it finds exactness matches quickly, but it doesn't really have any allowances for mismatches. And the way that bow tie and other aligners deal with this, and they're all pretty consistent, is in the following way, which is that they do backtracking.**

**Here's the idea. You try and match something or match a read and you get to a particular point in the read, and you can't go any further. Top is equal to bottom. So you know that there's no suffix in the genome that matches your query. So what do you do?**

**Well, what you can do is you can try all of the different bases at that position besides the one you tried to see whether it matches or not. I can see the horror coming over people. Oh, no, not backtracking, not that. But sometimes it actually works.**

25

**And just to give you order of magnitude idea about how this works in practice, when reads don't match, they limit backtracking to about 125 times in these aligners. so they try pretty hard to actually match things. And yes, it is true that even with this backtracking, it's still a great approach. And sometimes the first thing you try doesn't work, and you have to backtrack, trying multiple bases at that location until you get one that matches. And then you can proceed. OK And you eventually wind up at the alignment you see in the lower right hand corner, where you're substituting a g for an a, an a for a g, excuse me, to make it go forward.**

**Do people understand the essential idea of this idea of backtracking? Does anybody have any comments or questions about it? Like ew, or ideas? Yes.**

**AUDIENCE: What about gaps?**

**PROFESSOR: What about gaps? BWA, I believe, processes gaps. But gaps are much, much less likely than missed bases. The other thing is that if you're doing a sequencing library, and you have a read that actually has a gap in it, it's probably the case you have another read that doesn't. For the same sequence. So it is less important to process gaps than it is to process differences.**

**The reason is that differences mean that it might be a difference of an allele. In other words, it might be that your base is different than the reference genome. Indels are also possible. And there are different strategies of dealing with those. That would be a great question for Hang tomorrow about gaps. Because he can tell you in practice what they do. And we'll get into a little bit of that at the end of today's lecture. Yes. Question?**

**AUDIENCE: I'm Levy.**

**PROFESSOR: Hi, Levy.**

**AUDIENCE: How do you make sure when you're backtracking that you end up with the best possible match? Do you just go down the first--**

**PROFESSOR: The questions is how do you guarantee you wind up with the best possible match?**

26

||**The short answer is that you don't. There's a longer answer, which we're about to**<br>**get to, about how we try to approximate that. And what judgment you would use to**<br>**get to what we would think is a practically good match. OK? But in terms of**<br>**theoretically optimal, the answer is, it doesn't attempt to do that. That's a good**<br>**question. Yes.**|
|---|---|
|**AUDIENCE:**|**In practice, does this backtracking method at the same time as you're computing**<br>**the matches or--**|
|**PROFESSOR:**|**Yes. So what's happening is, you remember that loop where we're going around,**<br>**where we were moving the top and bottom pointers. If you get to a point where they**<br>**come together, then you would at that point, begin backtracking and try different**<br>**bases. And if you look, I posted the BWA paper on the Stellar website. And if you**<br>**look in one of the figures, the algorithm is there, And you'll actually see, if you can**<br>**deconvolute what's going on, that inside the loop, it's actually doing exactly that.**<br>**Yes. Question.**|
|**AUDIENCE:**|**In practice, is the number of errors is small, would it make sense just to use**<br>**[INAUDIBLE]?**|
|**PROFESSOR:**|**We're going to get to that. I think the question was, if the number of errors is small,**<br>**would it be good to actually use a different algorithm, drop into a different**<br>**algorithm? So there are algorithms on FM index assisted Smith Waterman, for**<br>**example. Where you get to the neighborhood by a fast technique and then you do a**<br>**full search, using a more in depth principles methodology, right? And so there's**<br>**some papers I have in the slides here that I referenced that do exactly that.**<br>**These are all great questions. OK. Yes.**|
|**AUDIENCE:**|**If you're-- If you only decide to backtrack a certain number of times, like 100 times,**<br>**then wouldn't like the alignment be biased towards the end of the short read?**|
|**PROFESSOR:**|**I am so glad you asked this question. The question is, and what was your name**<br>**again?**|


27

**AUDIENCE: Kevin.**

**PROFESSOR: Kevin. Kevin asks, gee, if you're matching from the right to the left, and you're doing backtracking, isn't this going to be biased towards the right into the read, in some sense, right? Because if the right into the read doesn't match, then you're going to give up, right? In fact, what we know is the left end of the read is the better end of the read. Because sequences are done five prime to three prime and thus typically, the highest quality scores or the best quality scores are in the left hand side of the read.**

**So do you have any idea about how you would cope with that?**

**AUDIENCE: You could just reverse one of them. But you'd reverse--**

**PROFESSOR: Exactly what they do. They execute the entire genome and they reverse it and then they index that. And so, when they create what's called a mirror index, they just reverse the entire genome, and now you can match left to right, as opposed to right to left. Pretty cool, huh? Yeah.**

**So backtracking, just note that there are different alignments that can occur across different backtracking paths. And this is not optimal in any sense. And to your question about how you actually go about picking a backtracking strategy, assuming we're matching from right to left again for a moment, what you can do is, if you hit a mismatch, you backtrack to the lowest quality based position, according to PHRED scores.**

**We talked about PHRED scores earlier, which are shown here on the slide. And you backtrack there and you try a different base and you move forward from there. So you're assuming that the read, which is the query, which is associated quality scores, is most suspect where the quality score is the lowest. So you backtrack to the right to the leftmost lowest quality score.**

**Now it's a very simple approach. Right? And we talked a little bit about the idea that you don't necessarily want to match from the right side and thus, typically the parameters to algorithms like this include, how many mismatches are allowed in the**

28

**first L bases on the left end, the sum of the mismatch qualities you're going to tolerate, and so forth. And you'll find that these align yourself with a lot of switches that you can set. And you can consult with your colleagues about how to set switches, because it depends upon the particular type of data you're aligning, the length of the reads and so forth.**

**But suffice it to say, when you're doing this, typically we create these mirror indices that actually reverse the entire genome and then index it. So we can either match either right to left or left to right. And so for example, if you have a mirror index, and you only tolerate up to two errors, then you know that either, you're going to get the first half right in one index or the mirror index. And so you can use both indices in parallel, the forward and the reverse index of the genome, and then get pretty far into the read before you have to start backtracking.**

**There are all these sorts of techniques, shall we say, to actually overcome some the limitations of backtracking. Any questions about backtracking at all? Yes.**

**AUDIENCE: Is it trivial knowing the BWT originally to find the mirror BWT? Like for example,**

**PROFESSOR: No, it's not trivial. AUDIENCE: So it's not like a simple matrix transforming [INAUDIBLE].**

**PROFESSOR: No. Not to my knowledge. I think you start with the original genome, you reverse it and then you compute the BWT with that. Right? That's pretty easy to do. And Hang was explaining to me today how you compute his new ways of compute BWT, which don't actually involve sorting the entire thing. There are insertion ways of computing the BWT that are very [INAUDIBLE], and you could ask him this question tomorrow if you care to come.**

**All right just to give you an idea on how complex things are, to build an index like this, takes, for the entire human genome, we're talking five hours of compute time to compute an index to give you an order of magnitude time for how to compute the BWT. the LF checkpoints, and the suffix array sampling. Something like that.**

29

**So it's really not too bad to compute the index of the entire genome. And to do searches, you know, we're talking about, like on a four processor machine, we're talking about maybe upwards of 100 million rads per hour to map. So if you have 200 million reads and you want to map them to a genome, or align them as it's sometimes called, it's going to take you a couple hours to do it. So this is sort of the order of magnitude of the time required to do these sorts of functions.**

**And there are a couple fine points I wanted to end with today. The first is we haven't talked at all about paired, erred, and read alignment. In paired read alignment, you get, for each molecule, you get two reads. One starting at the five prime end on one side, , and one starting from the five prime end on the other side. So typical read links might be 100 base pairs on the left and 100 base pairs on the right.**

**What is called the insert size is the total size of the molecule from five prime end to five prime end to read. And the stuff in the middle is not observed. We actually don't know what it is. And we also don't know how long it is. Now when these libraries are prepared, size selection is done, so we get a rough idea of what it should be. We can actually compute by looking at where things align on the genome, what it actually is. But we don't know absolutely.**

**If we were able to strictly control the length of the unobserved part, which is almost impossible to do, then we would get molecular rulers. And we would know exactly down to the base, whether or not there were indels between the left read and the right read when we did the alignment. We actually don't have that today.**

**The sequencing instrument actually identifies the read pairs in its output. That's the only way to do this. So when you get an output file, like a fast Q file, from a sequencing instrument, it will tell you, for a given molecule, here's the left read and here's the right read. Although left and right are really sort of misnomers because there really is no left and right, right? This is one end and then this is the other end.**

**Typical ways of processing these paired reads, first you align left and right reads. And they could really only be oriented with respect to a genome sequence where you say that one has a lower coordinate than the other one when you're actually**

30

**doing the alignment. And if one read fails to align uniquely, then what you can do is, you know what neighborhood you're in because you know, roughly speaking, what the insert size is, so you can do Smith Waterman to actually try and locate the other read in that neighborhood. Or you can tolerate multiply mapped reads.**

**One thing that I did not mention to you explicitly, is that when you match the entire query, and top and bottom are more than one away from each other, that means you've got many places in the genome that things map. And thus you may report all of those locations or I might report the first one. So that's one bit of insight into how to do a map paired reads.**

**And these are becoming very important because as sequencing costs go down, people are doing more and more paired and sequencing because they give you much more information about the original library you created and for certain protocols can allow you to localize events in the genome far more accurately.**

**Final piece of advice on considerations for read alignment. We talked about the idea that some reads will map or align uniquely to the genome and some will multimap. You know that the genome is roughly 50% repeat sequence. And thus it's likely that if you have a particular read molecule, there's a reasonable chance that it will map to multiple locations. Is there a question here? No. OK.**

**You have to figure out what your desired mismatch tolerance is when you're doing alignment and set the parameters to your aligner carefully, after reading the documentation thoroughly, because as you could tell, there's no beautiful matrix formulation like there is with a well established basis in the literature, rather it's more ad hoc. And you need to figure out what the desired processing is for paired reads.**

**So what we've talked about today is we started off talking about library complexity and the idea that when we get a bunch of reads from a sequencer, we can use that collection of reads to estimate the complexity of our original library and whether or not something went wrong in the biological processing that we were doing. Assuming it's a good set of reads, we need to figure out where they align to the genome.**

31

**So we talked about this idea of creating a full text minute size index, which involves a Burrows-Wheeler transform. And we saw how we can compute that and throw away almost everything else except for the BWT itself, the suffix array checkpoints, and the FM index checkpoints to be able to reconstruct this at a relatively modest increase in size over the genome itself and do this very, very rapid matching, albeit with more problematic matching of mismatches. And then we turned to the question of how to deal with those mismatches with backtracking and some fine points on paired end alignment.**

**So that is the end of today's lecture. On Tuesday of next week, we'll talk about how to actually construct a reference genome, which is a really neat thing to be able to do, take a whole bunch of reads, put the puzzle back together again. I would encourage you to make sure you understand how this indexing strategy works. Look at the slides. Feel free to ask any of us.**

**Thanks so much for your attention. Welcome back. Have a great weekend. We'll see you next Tuesday.**

32

---

[← But there are other little tricks you can play here.](03-but-there-are-other-little-tricks-you-can-play-here.md) · [Up: contents](index.md)
