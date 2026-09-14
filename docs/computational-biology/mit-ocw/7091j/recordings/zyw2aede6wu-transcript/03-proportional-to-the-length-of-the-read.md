---
title: proportional to the length of the read.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/zyw2aede6wu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# proportional to the length of the read.

**Source:** `recordings/zyw2aede6wu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So here's the essential idea. What we're going to do is we're going to take all of the reads that we collect. And we're going to index them. And we can do that roughly at N log N time. And after we've indexed all of the reads, then we can use that same index to find overlaps very, very efficiently.**

**And you can conceptualize this as simply looking at a read that you have in your hand and looking it up in the index. And you'll find all the places that the suffix or prefix of that read batches. And you can trace back till you find all the places it matches where they hit an end of a read. And those all correspond to edges in the graph.**

**And it turns out that this is so clever that it eliminates redundant edges. So, for example, if I have reads that look like this where I have read one overlaps with read two which overlaps with read three. And read one and read three also overlap. An unreduced graph would have a representation like this.**

**But it turns out that we don't have to do that because we can simply reduce our graph to this because we know that read one and read three. Actually, this is the graph that we would have that would be unreduced. We can reduce the graph to eliminate this transitive edge and simply represent it in this fashion. So when we use these indices, we eliminate these transitive edges as we'll see momentarily.**

**So here's an example graph. The sequence is shown on the bottom. The read lengths are of length seven bases. And we're going to consider all overlaps a minimum size three. And the edge label is the actual length of the overlap between the reads. And you can see that at the outset that these overlap graphs are not necessarily simple. That tracing a path of the graph that represents the original string is not completely and totally straightforward.**

**So we need to come up with a way to articulate our metrics for how to trace a path to the graph to reconstruct a genome. And that comes to the question of layout, which is how do we formulate the problem of tracing a path through an overlap**

7

---

[← chromosomes.](02-chromosomes.md) · [Up: contents](index.md) · [graph? →](04-graph.md)
