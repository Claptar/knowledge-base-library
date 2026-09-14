---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/ob9xgbpvr-s-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/ob9xgbpvr-s-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So good afternoon, once again. And welcome back to Computational Systems Biology, lecture number seven. And today we're going to put to good use two things that we have learned. We've learned how to align high throughput reads to genomes. And we've learned how to take a collection of high throughput reads and assemble a genome.**

**And today we're going to delve into the mysteries of transcriptional regulation. And so what I'd like to discuss with you today is a very important set of techniques that allows us to elucidate exactly how genes are regulated. It's probably the most important technique for allowing us to get at that question. And I'm sure many of you are familiar with the idea of transcriptional regulators, which are proteins that bind in a sequence specific way to the genome and act as molecular switches.**

**And we'll return to some aspects of these when we talk about proteomics later in the term. But suffice to say, these proteins have domains that interact in a sequence specific way with the DNA bases in one of the grooves of DNA. They also typically contain a domain which is an activation domain or repression domain that interacts with other proteins that can cause the genome to fold up. And it can also help recruit the RNA polymerase holoenzyme to actually turn on a gene transcription.**

**So here we have a figure of a collection of Pit1 molecules interacting with the genome. And of course, there are many flavors of genomic regulators. It's estimated that humans have about 2,000 different proteins that act as these molecular switches, some as activators, some as repressors. And we're going to be talking about, fundamentally, today the idea of how these molecules interact with the genome and control gene expression through the analysis of where they actually interact with specific genome loci.**

1

**So if we were to draw a picture of how we understand gene regulation in cartoon form, if we have a gene here with the transcription start site and we can imagine RNA molecules being produced off of this genomic template, we know that there are non-coding regions of a gene that permit for the binding of these regulators. And my definition of a gene is all of the DNA that's required to make a specific transcriptive protein. So that includes not only the coding parts of the gene but the non-coding, regulatory parts as well.**

**So we can imagine out here that there are a collection of regulators, perhaps just one, that bind to a sequence that in turn activate this gene, producing the RNA transcript, which then in turn this turned into another protein. This protein may undergo some sort of post-translational modification by signaling pathway or other mechanism that activates it. So regulators need to be activated before they could bind and some do not. And this activated regular combine to get another gene and cause another RNA to be expressed.**

**And it may be, in the second context, that we need two different proteins to bind to activate the gene. And so during the course of the term, we're going to be talking about many aspects of these regulatory networks, including things like what the regulatory code of a genome is, that is where these binding sites are and how they're occupied. And we'll return to that later on in today's lecture.**

**We'll talk about the dynamics of binding of proteins, including how concentration [? they ?] dependent are. And we'll talk about combinatorial control, whether or not, for example, both of these have to be present or just one of them needs to be present for a gene to be transcribed, and how you can use these regulatory sequences to implement very complex computational functions.**

**But suffice to say, the most important thing that we have to identify is the programming that underlies the genome, which includes these regulatory sequences and exactly how they're occupied by regulatory proteins. Ideally what we would like to be able to do is to do a single experiment that elucidated all of the regulatory sites in the genome and which ones were occupied by which proteins.**

2

---

[Up: contents](index.md) · [But presently, that's technically not possible. →](02-but-presently-that-s-technically-not-possible.md)
