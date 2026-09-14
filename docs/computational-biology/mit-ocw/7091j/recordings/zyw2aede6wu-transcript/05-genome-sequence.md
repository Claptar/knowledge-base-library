---
title: genome sequence.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/zyw2aede6wu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# genome sequence.

**Source:** `recordings/zyw2aede6wu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Now, not all graphs have these walks. And graphs do our Eulerian. And we won't distinguish different types of these graphs. And if a graph has two semi-balanced nodes and all the rest of the nodes are balanced, then it will have a walk through it. So if we think about our original graph, there are two arguments for it having such a walk. The first argument is that we show the walk. And the second is that we have two semi-balanced nodes and the rest of the nodes are balanced.**

**So the reason that we care about this is that we want to study cases where this goes wrong. So to build a De Bruijn graph of a genome, we're going to take our original sequence reads. And we're going to take all the k-mers that occur in those reads. And we're going to add edges to a De Bruijn graph based upon those k- mers.**

**So if we have a read like this, and we consider a k-mer in the read, we're going to add an edge in the graph between the left k minus 1-mer and the right k minus 1- mer. And we'll do that for every single k-mer in the read. Now note what this does is it destroys some information. It destroys information about the ordering of certain of the k-mers in this read just destroying their read contiguity in order to make some simplifying assumptions to represent the sequence ordering of these k minus 1- mers in the graph. So we build the graph in this way and if I were to build the graph like this, what is the minimum sequence overlap for two reads to actually share an edge in the resulting graph? Can anybody see how long the sequence must be in the second read for it to actually overlap at edge with the first read?**

**Well, if this second read also has a k-mer, right? It's going to produce another structure just like this one if these two do overlap. And thus the edge produced by this read and the edge by this read will overlap like this. And thus all of the nodes that came from this part of read one will feed into this graph. And then all the nodes to come out of this k-mer from the purple read will come out of it like so, right?**

**And thus when we're tracing the graph, the idea is that the graph will be connected. And we'll be able to come between these reads and reconstruct the sequence that**

17

**was suggested by the overlap. The thing, however, you should note in this-- yes, question?**

- **AUDIENCE: So you're picking two k minus 1 reads there-- are those from different reads? Or from the white read?**

- **PROFESSOR: No, it's from the white read. These are the 2k minus 1-mers that came out of this read. So they actually overlap.**

- **AUDIENCE: Yeah, but then you were talking about how the one was purple in that case. PROFESSOR: Right, well, this is the same sequence let's say. This is the same, exact sequence down here. So if it's the same, exact sequence, it will have the same k minus 1- mers. And when we build the graph if a node already exists, we reuse it. And thus if we reuse the nodes that were created when we built the graph nodes and edges for the white read, then when the purple read comes along, we're going to put another edge here between these two k minus 1-mers because they are contained here as well. So these are identical sequences to this because these two reads overlap. And this part is the same sequence as that part.**

**AUDIENCE: Yeah, so why do you need k minus 1-mers if you have overlapped k? PROFESSOR: Because the way we're finding these overlaps is through the graph. And we're not indexing things of size k, right? We're indexing things of size k minus 1. In each edge represents a sequence of length k because we know this sequence and this sequence are overlapped by one base. So when we find an edge that's the same between the white and the purple read, we know that they're overlapping by k bases. Is that making sense to you? AUDIENCE: No. PROFESSOR: No, OK, so let's try it again. AUDIENCE: You can keep going.**

18

**PROFESSOR: No, it's OK. Let's just start with the purple read to start for a moment because I think if you have a question, other people may have a question. So we have this sequence, which is this sequence right here, right? And then we have this sequence, which is the sequence right here. They overlap by one base. And so we put an edge between them like this in the graph. OK?**

**AUDIENCE: Don't they overlap by more than one base? They can only contain one base from each k-mer.**

**PROFESSOR: I'm sorry. That's what I meant. Yeah. And then the same thing is true down here. And so we will find this k minus 1-mer and this k minus 1-mer. And then they overlap. For genome assembly, we record the forward and reverse complement reads in twin nodes. And we're not going to show those because it just complicates our graphs without really adding any illustrative power.**

**And we always choose k to be odd so that a node can't be its own reversed complement. And here is the graph growing if we think about k equals 5. So we have reads of length five. And we are adding sequences to the graph. And you note that the graph is acyclic until we get to the repeated sequence.**

**And we get to the second long the sequence comes back around begins a looping back on itself. And if we consider the last part of this De Bruijn graph construction, then we wind up with the finished graph on the right-hand side. And you can see the multiplicity of the edges correspond to the number of times the long is repeated in this graph.**

**So once again, repeats are causing the circular structure, which only could be resolved if we had sufficiently long reads, which we don't have in this particular case. However, if we consider perfect sequencing we always have a path to the graph. And the reason is that the leftmost part of the genome, so to speak, is going to be semi-balanced. And the rightmost part is going to be semi-balanced. And all the parts in between are going to be balanced.**

**So the k minus 1-mer on the very left end is semi-balanced and the k minus 1-mer**

19

**on the right is semi-balanced. And all the nodes in between are balanced. Now, this does not allow for errors of course. And we talk about following this Eulerian walk to find the original sequence. But the question we can ask ourselves is whether or not this walk always really corresponds to the original genome sequence.**

**It turns out I can show you this example, which is we have this graph for this sequence. And there are two different walks through this graph. And the two different walks produced two different sequences. And they depend upon which way you start walking from the node AB.**

**So once again, here we have seen that even when we have a path to the graph, the path may not be unique. It may not be able to generate the original sequence that we started with. So the other problem we can have when we are building a graph like this is that gaps in coverage can create holes in the graph.**

**So if we omit certain of our reads, we'll come up with a graph that is broken into two parts. And this corresponds to the idea that we're going to create two different contigs that are contiguous sequence but will be unable to fill in the middle part. OK?**

**So we also can have differences in coverage of a graph when we have extra reads at particular locations in the genome. And that causes the degrees on the individual nodes to vary and causes us to not be able to rely upon the indegree and outdegree as an absolute metric for how to trace a path through the graph.**

**And the other thing is that if you have differences between the chromosomes, which we talked about last time in our overlap layout consensus assembler, it also can cause graphs to split apart and to have subgraphs that correspond to one allele versus the other allele, which is present perhaps in the main graph.**

**All right, so it's actually the case that these graphs are attractive for a very important reason, which is there extraordinarily efficient to build. That is in order to build a graph like this, you need to take each one of these k minus 1-mers and actually find the node, which you can do by hashing and then put the edges into the graph. And**

20

**so you find that you need to put in an edge and two nodes for each k-mer. And if you have a hash map that encoded these nodes and edges, it's constant time work. So you wind up with a graph which costs order of the number of reads to build.**

**So it's a linear time graph construction problem. Recall that our last overlap construction, we thought we could get down to N log N. And here is an example of sub-setting part of the lambda phage genome using a De Bruijn graph assembler. And you can see that roughly the time required to assemble parts of the genome is linear in the amount of genome sequence that you give it.**

**So these assemblers were favored early on in the days of short-read assembly in part because they were so efficient. And typically in some of the projects, you have very high coverage. And so you wind up with graphs that actually have a huge number of edges between nodes. And this can be summarised in terms of a graph that simply annotates the edges with the number of instances.**

**And so you have a weighted graph on the right-hand side, which is easier in some sense to trace because we can now begin to eliminate low-coverage edges as potential anomalies. But the essential idea is to trace these graphs to produce the ultimate genome sequence. And in order to do so, we may need to do some error correction.**

**So we talked earlier about the idea that if we have an error, we're going to actually produce a portion of the graph that hangs off into outer space. And we can cut these dead-end tips of the graph off if they are low coverage because they presumably correspond to errors.**

**If we get an error in the middle of a read, we can wind up with a so-called bubble in the graph, which once again is low coverage. And we can get rid of these bubbles in a similar fashion. And it's also possible to get chimeric edges of the graph. And those can be caused by errors as well. And we can clip those edges.**

**So there are different kinds of error correction we can do in the graph. These are all quite heuristic. Each assembler has its own set of heuristics for how to deal with**

21

**graph anomalies and how to eliminate edges in the graph to permit assembly. But these are getting rid of dead-end tips and popping bubbles and getting rid of chimeric edges are important things to consider for any assembler.**

**So the limitations of these graphs are the idea that we're immediately splitting these reads into this k-mer representation, which is destroying information. And in order to overcome this, one of the things that people have done in these De Bruijn graph assemblers is to take the original reads and to map them back on to the graph.**

**So when you're attempting to trace the path through the graph, what you do is you take the original reads. You thread them through the graph. And you know that the original read represents contiguous genome sequence. So it provides you with a path through the graph that you know is good.**

**People have been doing this in part because they didn't want to go to the full overlap graph implementation because of the cost. But I think that these overlap graph implementations now are sufficiently sophisticated that I personally would use them instead of a De Bruijn graph assembler. And so the trade off really centers around speed and space versus accuracy.**

**So we can look at some example assemblers and look at their performance. But before I do that and we leave De Bruijn graphs, are there any other questions about De Bruijin graph assemblers?**

**AUDIENCE: I have one.**

**PROFESSOR: Yeah, question.**

**AUDIENCE: How long is k typically?**

**PROFESSOR: We're going to talk about that. The k typically is somewhere around 60-- something like that-- Somewhere in that neighborhood. It's actually-- it has to be odd, right? So 61, 57-- something like that. Good question. Any other questions about De Bruijin graph assemblers?**

**So once again returning to over our architecture, we have these reads. We need to**

22

**produce contigs. In the case of overlap graphs, we're going to trace the overlap graphs. In the case of De Bruijn graphs, we're going to trace the De Bruijn graph.**

**For scaffolding, we can use the read pairs to put scaffolds back together again. And here is some comparison of the performance of these various assemblers. So the first assembler-- SGA-- is an overlap layout consensus-style assembler. Velvet/Abyss and SOAPdenovo are all De Bruijn, graph-based assemblers. So these are all contemporary assemblers that people use for assembling genomes.**

**An important metric for assemblers is something called N50, which is the size of a contig or scaffold where at that length or larger 50% of the bases are present in scaffolds of that length. So, for example, for SGA, they say that scaffold N50 size is 26.3 kilobases, which means that in scaffolds of length 26.3 kilobases or larger, half of the bases of the assembly lie.**

**So the larger the N50 is, the larger the scaffolds are that cover things. And you want larger and larger scaffolds or contigs so that you have fewer gaps in your assembly. So the N50 number is a principle comparison metric when one is thinking about assemblers.**

**So in this particular case, for SGA the overlap metric was that the reads had to overlap by at least 75 bases or more. And these were 100-base pair reads. You can see the details on the read data on the bottom line there. So as long as the reads overlap by 75 bases, they were put together in the graph.**

**And the De Bruijn graph assemblers each had their own optimum number for k. And the way that you tune these parameters is you run the assembler on a range of k values. And you see which k value produced the assembly with the highest N50. And you pick that k.**

**Can anybody think of a reason why it is that although these are all roughly in the same ballpark, different assemblers might have different k values given that the underlying technology is quite similar? Any guesses about what is going on here?**

23

**Well, we know that the differences in the assemblers really are rooted in the way that they are processing the graphs and the way that they are simplifying them. And therefore, one has to imagine that the differences lie in the post-processing of the graph once it's built and that certain assemblers like larger k values. Whereas other ones can tolerate smaller k values.**

**And you can see if we look at the running statistics for these, that the performance of SGA if you look at the reference bases covered by contigs greater than one kilobase is roughly comparable to all the other assemblers. But its mismatch performance is much better. That is the other assemblers are producing-- well, I take it back except for SOAPdenovo. But it does quite a good job at correcting reads in coming up with the correct sequence.**

**The last lines however tell the story about running time, which is that the overlap consensus assembler is taking 41 hours of CPU time for C. elegans genome assembly. Whereas the other assemblers, the De Bruijn assembler are running much faster.**

**So the thing that I wanted to emphasize today was that once you have the final graph whether it be an overlap graph or a De Bruijn graph, which represents possible ways of putting back together again the jigsaw puzzle, it still is an art to be able to build an assembler that uses appropriate heuristics to trace the graph to come up with a genome sequence.**

**And I think another lesson is that repeats are very problematic. With short reads, we really cannot resolve repeats exactly. As a consequence, when we think about any reference genome that we're dealing with, if we consider the size of the reads that were used to assemble that genome, then we need to be mindful of what that tells us about whether or not the repeat structure that we're observing in the genome is really an accurate rendition of what's going on in the genome itself.**

**And finally, I think that we've talked today about the problem of assembling genomes from a set of reads that represent a uniform, single individual albeit with possibilities of differences of alleles between mom and dad in a diploid organism.**

24

**However, environmental sequencing where one takes up sea water or other samples and sequences all the organisms in it and then attempts to assemble those organisms de novo admits the possibility that there are many different genomes that you're considering.**

**And that, of course, creates a whole new set of research problems, which I think are unsolved in part because of the read links that we're currently dealing with. Are there any final questions about assembly? OK, great. Well, we will see you then on Thursday where we will talk about ChIP-seq and IDR analysis. Until then, have a great Wednesday. Thank you very much.**

25

---

[← graph?](04-graph.md) · [Up: contents](index.md)
