---
title: '[INTERPOSING VOICES]'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kun6rj21hno-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [INTERPOSING VOICES]

**Source:** `recordings/kun6rj21hno-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Riboswitches. We're going to come to what riboswitches are in a moment for those not familiar. And I think I have an example later of a pseudoknot that's important. So that's a good question.**

**I think I should have added to this list the point that you made in the back that they have to be close enough that you can get a good alignment. I should add that to this last. Thanks. It's a good point.**

**All right, so classes of non-coding RNAs. As promised, my favorites listed here. Everyone knows tRNAs, rRNAs. You can think of UTRs as being non RNAs. They often have structure that can be involved in regulating the message.**

**snRNAs involved splicing. snoRNAs-- small nucleolar RNAs-- are involved in directing modification of other RNAs, such as ribosomal RNAs and snRNAs, for example. Terminators of transcription in prokaryotes are like little stem loop structures.**

**RNaseP is an important enzyme. SRP is involved in targeting proteins with signal peptides to the export machinery. We won't go into tmRNA. micro RNAs and link RNAs, you probably know, and riboswitches. So Tim, can you tell us what a riboswitch is?**

**AUDIENCE: A riboswitch is any RNA structure that changes confirmation according to some stimulus [INAUDIBLE] or something in the cell. It could be an ion, critical changes in the structure. [INAUDIBLE].**

**PROFESSOR: Yeah, that was great. So just for those that may not have heard, I'll just say it again. So a riboswitch is any RNA that can have multiple confirmations, and changes confirmation in response to some stimulus-- temperature, binding of some ligand, small molecules, something like that, et cetera. And often, one of those structures will block a particular regulatory element. I'll show an example in a moment. And so when it's in one confirmation, the gene will be**

25

**repressed. And when it's in the other, it'll be on. so it's a way of using RNA's secondary structure to sense what's going on in the cell and to appropriately regulate gene expression.**

**All right, so now we're going to talk about a second approach. So this would be the approach. You've got some RNA. It may not do something, and maybe you can't find any homologues.**

**It might be some newly evolved species-specific RNA, or your studying some obscure species where you don't have a lot of genomic sequence around. So you want to use the first principles, approach, the energy minimization approach. Or maybe you have the homologues, but you don't trust your alignment. You want a second opinion on what the structure is going to be.**

**So just in the way that protein folding-- you could think of an equilibrium model where it's determined by folding free energy, and enthalpy will favor base pairing. You get gain some enthalpy when you form a hydrogen bond, and entropy will tend to favor unfolding. So an RNA molecule that's linear has all this confirmational flexibility, and lose some of that when you form a stem. It forms a helix. Those things don't have as much flexibility.**

**And even the nucleotides in the loop are a little bit confirmationally-- they're not as flexible as they were when it was linear. So that means that at high temperatures, it'll favor unfolding. So the earliest approaches were approaches that sought to maximize the number of base pairs.**

**So they basically ignore entropy and focus on the enthalpy that you gain from forming base pairs. And so Ruth Nussinov described the first algorithm to figure out what is the maximum number of base pairs that you can form in an RNA. And so a way to think about this is imagine you've got this sequence.**

**What is the largest number of base pairs I can form with this sequence? I could just draw all possible base pairs. That A can pair with that T. This A can pair with that T.**

**They can't both pair simultaneously, right? And this C can pair with that G. So if we**

26

**don't allow crossing, which-- coming back to Sally's point-- this would cross this, right? So we're not going to allow that. So the best you could do be to have this A pair with this C and this C pair with this G and form this little structure.**

**This is not realistic because RNA loops can't be one base. They minimum is about three. But just for the sake of argument, you can list all these out, but imagine now you've got 100 bases here.**

**Every base will on average potentially be able to pair with 24 or 25 other bases. So you're just going to have just an incredible mishmash of possible lines all crisscrossing. So how do you figure out how to maximize that pairing? Any ideas? Don, yeah?**

**AUDIENCE: You look for sections of homology.**

**PROFESSOR: We're not using homology. We're doing [INAUDIBLE] AUDIENCE: I'm sorry, not homology, but sections where-PROFESSOR: Complementary? AUDIENCE: Complementary. Yeah, that's the word I was thinking. PROFESSOR: The blocks are complementary. AUDIENCE: And then so-PROFESSOR: You could blast the sequence against inverse complements itself and look for little blocks. You could do that. That's not what people generally do, mostly because the blocks of complementarity in real RNA structures are really short. They can be two, three, four, bases. Sally, yeah? AUDIENCE: Could you use [INAUDIBLE] approach where you just start with a very small case and build up? PROFESSOR: So we've seen that work for protein sequence alignment. We've seen it work for the Viterbi algorithm. So that is sort of the go-to approach in bioinfomatics, is to use**

27

---

[← AUDIENCE: [INAUDIBLE]](04-audience-inaudible.md) · [Up: contents](index.md) · [some sort of dynamic programming. →](06-some-sort-of-dynamic-programming.md)
