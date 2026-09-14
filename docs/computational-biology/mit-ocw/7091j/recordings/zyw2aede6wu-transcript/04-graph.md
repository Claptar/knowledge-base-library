---
title: graph?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/zyw2aede6wu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# graph?

**Source:** `recordings/zyw2aede6wu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So we'll first start with the idea of the shortest common superstring. The shortest common superstring of a string S is the shortest string that contains all the strings in S as substrings for a particular length of substring. So, for example, if we didn't have the constraint of shortest, then just finding a string that contains all the substrings is easy. You just put them all together. But if we want the shortest, then we need to be more thoughtful in terms of the way that we compute this shortest common substring. And here is an example of the shortest common substring for the substrings that I have shown you up there.**

**So one way to think about the assembly problem is that we're trying to compute the shortest common substring of all the reads that we have. And that will be the most efficient representation of those reads in a linear sequence. Now, we can describe this problem in terms of an overlap graph.**

**And if you think about the way that we would solve this in overlap graph, in the shortest strings, we want the maximum amount of overlap. So we want to trace a path through the overlap graph that gives us the largest amount of overlap, which gives us the shortest string. Right? So if we simply negate the overlaps, we want to minimize the total cost of the graph.**

**Now, it turns out that this problem is known to be a very hard computational problem. It's in the class of something called NP-hard because it's known as the traveling salesman problem. And when you think about the fact that we're going to have hundreds of millions of reads, this is not really going to be tractable. If we got rid of the weights, and we simply wanted to find a path through the graph, that's called the Hamiltonian Path problem. That's also NP-complete.**

**So the shortest common substring is a way to think about assembling. But we can't really necessarily optimize metrics because it's going to be intractable. So think about ways of doing this that are greedier. So here's an example of how we would compute the shortest common substring starting with the first string. And each step along the way, is a concatenation of strings or a collapsing of strings that works**

8

**towards building the shortest common substring.**

**And we get the input string and the output string. So we could articulate our assembly problem as a greedy SCS algorithm to try and put all the reads together to come up with a superstring. And let me just describe to you this will give us an intuition into what goes wrong with assembly in a moment.**

**But we do know there are some bounds on this-- that if we actually did the greedy algorithm, then the assembly that we got would be only two and a half times longer than the true shortest common substring. That isn't really very much comfort to us. So we're going to have to come up with different, more heuristic ways of approaching the assembly problem.**

**Here is another example. Now, this is the one that I want to show you where we start with a string at the top where we're going to be looking for minimum overlaps of three and these are reads of six long. And when we do this greedy algorithm, we come up with a string, which is shorter than the original beginning string we started with.**

**Can somebody see what happened here? Why are we missing part of the original string? Yes?**

**AUDIENCE: The reads were short enough. And they repeated enough that we never found out that it was of the length that it actually was. And so we just kind of [INAUDIBLE] did it [INAUDIBLE].**

**PROFESSOR: So the point was that the reads were too short to be able to unambiguously identify the number of repeats of long that we had in the original sequence. That's absolutely correct. So we're not able to disambiguate what was going on. And perhaps if we went back to our graph formalism we could solve this problem, right? Because here we have our graph and the overlaps are written in on the edges of the number bases that each one of these reads overlaps. And all we need to do is to trace through this graph to find the original string.**

**So here is one tracing, which gives a total overlap of 39, which actually faithfully**

9

**reproduces the original string, right? However, that's not the best tracing. A better tracing through this graph or path through the graph would be this, which gives us more overlap and gives us a shorter string. But as we know, even though it's better according to this metric, it isn't really optimum because it gives us the wrong answer. It's better but wrong.**

**So we're going to have to take into account other things when we do our assembly and our tracing of this graph to be able to come up with the best possible assembly. So if we increase the read length as was pointed out to span appropriately, we will be able to reconstruct the original sequence. And the point of this example is that we need to consider this when we're thinking about recovering repeat structures in genomes.**

**So if we don't have long enough reads, in this case reads of length 8, we're not going to go to recover the original repeat structure. And if we look at this, repeats are really the bane of assemblers in some sense. And as you know, roughly 50% of the human genome is repetitive content. So we need to be very, very careful in terms of the way that we utilize reads to be able to recover the best approximation of our genome sequence.**

**So here's another example where we look at l is minimum over length and k is the length of the reads. And you can see the sequence that we're trying to recover-It_was_the_best_of_times_it_was_the_worst_of_times-- and the output from our greedy SCS assembler. And as you can see, we need to get up to a read length of 13 characters for us to be able to properly assemble that original sentence.**

**So the essential message here is that unless you have reads that are long enough to span repeats, you're not going to go to recover the original sequence exactly. And this can be also thought of in the following example. Imagine you have repeats that are tandem repeats out at the end of a sequence. And we're using the English language here because it's easier to see than if I put up a bunch of genomic sequence. But, of course, the principles are the same.**

**You can see that unless we have reads that actually are anchored and unique**

10

**sequence and span out towards a repetitive sequence, we can't really tell how many times the word bells is repeated. Another possibility is that we can actually coming from both sides. And if we can anchor our reads and unique sequence on both the left and the right side of a repetitive element, then we can figure out how many copies of something like bells is present.**

**But in the absence of that, we really can't do it. In fact, we wind up with a structure looks like this. We wind up with-- there it is-- a structure where we have-- let's just say that there are four different stretches of genome in disparate parts of chromosomes and we repeat sequence in the middle. The blue parts of the chromosomes are unique sequence. And the red parts are repetitive sequences.**

**What will happen is that if the reads aren't long enough, we'll be able to find out in each one of the four locations that we've gone from unique sequence to repeat sequence. And then we will get lost in the middle of this identical repeated sequence. And then on the right-hand side we'll once again transition back from repeated sequence to unique sequence. But we won't know how to put things together in the middle. Right? We won't be able to figure out what the path is through these repetitive elements.**

**So that's the essential point I'd like to make about repeats. And we can now turn to the question of layout and how to process an overlap graph towards making contigs. This is the actual layout graph. When we think about that sentence up there. And we say the minimum over that length is four characters. And we have seven-character reads out of the sequence. You can see it's a pretty messy graph.**

**If we clean up the graph by removing the redundant edges, the edges like this that span over reads and are implied by other reads, we can remove edges that are transitive over one reads or two reads. Now, my presentation is going to talk about how to remove these edges. However, as I said at the outset, if you use the algorithm by Simpson et al., you actually don't generate these transitive edges in the first place.**

**But assuming that you didn't use an algorithm and you did generate them, you want**

11

**to get rid of these transitive edges like so. And it starts getting somewhat simpler as you begin simplifying the graph, removing these transitive edges. And then we can remove edges that skip two nodes. So here's what happens after you remove the single transitive edges in this graph. Yes?**

**AUDIENCE: So it seems that the transitive and verbal edges gave us a little bit more information about the genome. Do we lose some useful ordering principles by-PROFESSOR: They provide redundant information. They don't really provide any additional information. It's the same linear sequence that's implied by those edges. Any other questions?**

**So we can then remove edges that span two nodes. And we get an even simpler graph like this. Now this is beginning to look more tractable because we can look at this and we can output contigs that correspond to linear portions of the graph, which should be linear sequence. And when we do that what we wind up with are two contigs. And there's just a bit of problem in the middle, which is that we're unable to resolve the bit in the middle and as a consequence, we know that that is the number of terms that are in that original sentence because we didn't have a read long enough to be able to resolve that.**

**The other problem that we can have in doing this kind of layout is that when there are portions of the genome that occur or sequences in the genome that occur multiple times, when we actually do this layout, we may find that the portions of the genome that occur in two disparate locations line up with one another. And it may be that as you exit the portion that's shared you get a mismatched base.**

**So that mismatch could be because you have disparate parts of the genome that actually have very similar sequence. Or it could be that you had a read error at the end of your read. And it's difficult to tell the two apart except by the amount of coverage that you have. We'll talk about how to prune graphs like this in a few moments.**

**But in any event, assuming that we have pruned the graph, we have done our**

12

**overlap. We've done our layout. We've found our paths to the graph for our contigs. And then what we find is that for each contig, we have many reads. And we're going to take those reads. And we're going to look at them. And as you recall, we could either have errors causing disagreement among the reads.**

**We could have allelic differences between mom and dad causing those errors, well, not really errors-- differences. And then we can take a consensus to come up with what the haploid genome is. So that's the essential idea of a overlap layout consensus assembler. We compute the overlap graph. During the layout phase we actually simplify the graph. And we find pass through it. And during the consensus phase, we take our reads, and we build a consensus sequence of the genome.**

**And as I said, this graph building can be slow. Although, we'll talk about how slow it is here in just a moment. And the challenge is that modern sequencing data sets are hundreds of millions of reads. So let's talk about a contemporary overlap-based assembler-- something called the stream graph assembler, which is done over at the Sanger in the UK. And there are three separate steps it goes through.**

**The first step is it tries to correct reads. And the way it does this is it actually looks at all the k-mers that occur in reads-- it tries to find sequences that are very, very rare and find sequences that are nearby in sequence base that aren't as rare. And it can correct bases that it believes are sequencing errors.**

**The next step is assembly once it has taken all these reads and corrected them. It indexes all the reads as I suggested earlier using an FM index. And then it can find the overlap from that FM index directly. And part of the assembly process is throwing away duplicate reads and throwing away reads that have low quality scores.**

**So that's the filtering step. It then has the set of contigs that it has generated. And it does something quite interesting to find the scaffolds is that it takes the contigs it's assembled in terms of linear sequence. And it completely re-indexes them once again using an FM index.**

13

**And then it takes all the reads that you started with. And it maps them back onto the contigs. And by mapping the paired reads back on to the contigs, it can actually figure out what contigs should be formed into scaffolds where there are holes that are breached by these longer reads. So it's using the FM indexed both for correction to find out nearby k-mers for assembly to find overlaps and for scaffolding to put things together. And it does its indexing three different times.**

**And just to give you an idea of how long it takes for a human-sized genome, it's actually quite expensive in terms of CPU time. It takes many days have elapsed time to assemble an entire human genome right now. And it's thousands of CPU hours to actually put a genome together starting from scratch. OK, so that's the essential idea of an overlap-based assembler. Are there any questions at all about overlap-based assemblers? Yeah?**

**AUDIENCE: So in the case of an error , it's obvious how you would call that. But in an allelic difference, hypothetically, there would be 50% of the reads would have one and 50% of the reads would have another.**

**PROFESSOR: That's correct.**

**AUDIENCE: So in that case does it assemble-- do you just bias towards whichever ones weren't easily amplified? Or do you assemble two sequences?**

**PROFESSOR: Most assemblers produce a single sequence. And I don't know how SGA decides between the different alleles because I don't recall what the paper said they did. But they have to essentially flip a coin to come up with a haploid sequence. Yes?**

**AUDIENCE: You said there was three different times that you index. What are the three?**

**PROFESSOR: Yeah, the question was I said there are three different they indexed. They indexed at the outset to find errors. They indexed the second time to do the overlap computation. And they indexed the third time to realign all the original reads to the contigs they have to figure out which contigs to put together into scaffolds. Right?**

**But they have this essential foundational platform, which is the FM index. And so**

14

**they use that over and over again to be able to do the assembly. These are all great questions. All right, any other questions about overlap-based assemblers. And you can see that if you think about how much coverage they get out of an assembler like this, it's actually, we'll compare all the assemblers at the very end.**

**But if you look at the number of bases of autosomes and the X chromosome covered by an assembly, you can consider that as a function of the minimum alignment length to a referenced genome. And as the minimum alignment length goes up, that means you have to match longer and longer portions of the reference genome for your assembly contig to count. You can see that the number of bases dropped somewhat. In here they're showing that they do better than another assembler called SOAPdenovo.**

**But they do get a fairly good coverage. On the other hand, they don't get coverage anywhere near as good as Lander-Waterman might suggest because the coverage should suggest that the probability of uncovered base using Lander-Waterman would be roughly e to the minus 40th-- something like that. And e to the minus 40th is like 4 times 10 to the minus 18. So they're not anywhere near what we would think the Lander-Waterman bound would be for assembly.**

**So we've talked about these overlap-based assemblers. Now I'm going to turn to De Bruijn graph assemblers. How many people have heard of De Bruijn graphs before? Anybody? One person? So before we talk about De Bruijn graphs themselves, let's just talk terminology. So when I'm using terms we're all on the same page where we were talking about k-mers where the word mer is from the Greek "part."**

**And we talk about 4-mers of an original sequence as a sequence that's four bases long. And we can think about all of the 3-mers of an original sequence. So we talk a lot about k-mers. And a k minus 1-mer is a substring of length k minus 1 obviously from a k-mer. So if we think about the collection of reads-- here these are our super-simple economy sequencers producing reads of only length three, which is pretty desperate. But at any rate we'll go with that for the time being.**

**And we think about each one of these reads as having a left k minus 1-mer and a**

15

**right k minus 1-mer. We split them into two halves that way. And we're going to build a graph that is as follows. We're going to take all of the k minus 1-mers-- in this case the 2-mers. And for each read, we're going to draw an edge between its left 2- mer and its right 2-mer.**

**OK, once again, for each read, these sort of anemic, three-base-pair reads, we're going to draw an edge between its left 2-mer and its right 2-mer. And they overlap in one base. So all of the graphs that are De Bruijn graphs, the edges represent an overlap of one base. OK? So if you look at the graph at the bottom, that represents the overlaps present in the original sequence. You note that we have AA as one of the 2-mers. And its left half and right half obviously overlap by one base.**

**The triple-A read has AA as its left read and AA as a right read-- thay overlap at one base. And that's why we have that circular edge from A to itself. And the next edge from AA to AB comes from the next read-- the AAB read. So each edge then represents an overlap of one base. And therefore, each edge represents a unique k-mer sequence.**

**So the way to think about this graph is it that all of the edges represent the original reads. And we have represented the k minus 1 words as the nodes. OK? So we can take this graph then and generalize this idea. And if we look at how the graph changes as we add more structure, here you see that we've added an extra b. And we get another edge in the graph back to the same node.**

**So when we're building these graphs, if possible, we reuse a node that already exists. Now the way to think about coming back to the original sequence is finding a path through this graph and emitting sequence as we trace the path. And we would like to have a path that traverses all of the nodes.**

**And so we have some definitions here, which is that a node is balanced if its indegree equals it's outdegree. And you can see that not all the nodes are balanced down the graph of the lower, right-hand corner. And it's connected if all the components or nodes can be reached. And a Eulerian walk visit each edge exactly once, which is what we would like to actually take a De Bruijn graph and emit a**

16

---

[← proportional to the length of the read.](03-proportional-to-the-length-of-the-read.md) · [Up: contents](index.md) · [genome sequence. →](05-genome-sequence.md)
