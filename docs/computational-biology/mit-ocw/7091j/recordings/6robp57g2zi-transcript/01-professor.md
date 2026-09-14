---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6robp57g2zi-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/6robp57g2zi-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**I'm Ernst Frankel. I'll be teaching next two lectures. I'd like to encourage you to contact me outside of class if you have any questions, if you want to meet. And also, please, during class, ask questions. It's a somewhat impersonal setting with the video cameras and the amphitheater, but hopefully we can overcome that.**

**This unit is going to focus on moving across scales in computational biology, looking from computational issues that deal with the fundamentals of protein structure at the atomic level to the level of protein-protein interactions between pairs of molecules, protein DNA interactions and small molecules, and then ultimately into protein network. So we've got a lot of ground to cover, but I think we'll be able do it. As you've seen in the syllabus, the first couple of lectures are really a detailed look at protein structure, molecular level analysis, and then we'll move into some of these other levels of higher order, including protein DNA interactions and gene regulatory networks.**

**I think may of you are probably familiar with this quote, that "nothing in biology makes sense except in the light of evolution." And I'd like to offer a modified version of that, which is little in biology make sense except in light of structure, protein structure, DNA structure. We've, of course, seen this very early on in molecular biology when the structure of DNA was solved, and immediately became clear why it was the basis for heredity. But protein structures have been even more lasting impact time and time again, many, many more events, which have really revolutionized the understanding of particular biological problems.**

**So one example that was stunning at the time had to do with the most frequently mutated protein in cancer. This is the p53 gene. It's mutated in about half of all cancers, and what was observed early on-- this was in the days before genomic**

1

**sequencing when it was actually very expensive and hard to identify mutations in tumors.**

**So they focused on this particular gene, and they observed that the mutations clustered. So this is the structure of the gene from the n-terminus-- the protein from the n-terminus and the c-terminus, and the bars indicate the frequency of mutations. And you can see that they're all clustered pretty much in the center of this molecule.**

**Now, why is that? It was enigmatic until the structure was solved here at MIT by Carl Pabo and his post-doc at the time, Nikola Pavletich, and they showed, actually, that these correspond to critical domains. And in a second paper, they actually showed why the mutations occur in those particular locations.**

**So if you look at the plot on the upper left, here's the protein sequence; above it, the frequency of mutations; below it, the secondary structure elements. And you'll see that mutations occur in regions that don't have any regular secondary structure and can occur frequently in regions with secondary structure or not all in regions with secondary structure. So the mere fact that there's a secondary structure element does not define why there're mutations. But when the three-dimensional structure was solved in the complex with DNA, over here on the right-- this is the protein structure on the left, the DNA structure on the right, and in yellow are some of these highly mutated residues.**

**It turns out that all of the frequently mutated residues are ones that occur at the protein DNA interface. All right, so in a single picture, we now understand what was an enigma for years and years and years. Why are the mutations so particularly clustered in this protein in non obvious ways? Since that is the interface between the protein and the DNA, these mutations upset the transcriptional regulation through the action of p53.**

**So if we want to understand protein structure in order to understand protein function, where are we going to get these structures from? So the statistics on how proteins themselves-- I show here. This is from the-- I'll call it the PDB, the Protein**

2

**Database. Its full name is the RCSB Protein Database, but it's usually just called the PDB. And here, it shows that, at the time of this slide, around 80,000 structures have been determined by x-ray crystallography.**

**The next most frequent method was NMR, Nuclear Magnetic Resonance, which identified about 10,000 structures, and all the other techniques produce very, very few structures, hundreds of structures rather than thousands. So how do these techniques work? Well, they don't magically give you a structure. Right? They give you information that you have to use computationally to derive the structure.**

**Here's a schematic of how structures are solved by x-ray crystallography. One has to actually grow a crystal of the protein or the protein and other molecules that you're interested in studying. These are not giant crystals like quarts. They're even smaller than table salt. They're usually barely visible with the naked eye, and they're very unstable.**

**They have to be kept in solution or, often, frozen, and you should a very high powered x-ray beam through them. Now, most of the x-rays are-- what are they going to do? They're going to pass right through because x-rays interact very weakly with matter. But a few of the x-rays will be diffracted, and from that weak diffraction pattern, you can actually deduce where the electrons were that scattered the x-rays as they hit the crystal.**

**And so this is a picture, the lower right, of electron density cloud in light blue with the protein structures snaking through it, and what you can calculate, after a lot of work, from these crystallographic diffraction patterns is the location of the electron density. And then there's a computational challenge to try to figure out the location of the atoms that would have given rise to that electron density that then, when hit with x- rays, would have given rise to the x-ray diffraction pattern. So it's actually an iterative process where one arrives at the initial structure and then calculates, from that structure, where the electrons would be, from the position of electrons where the diffraction pattern would be when the x-rays hit it, and determines how well that predicted diffraction pattern agrees with the actual diffraction pattern, and then**

3

---

[Up: contents](index.md) · [continuously iterates. →](02-continuously-iterates.md)
