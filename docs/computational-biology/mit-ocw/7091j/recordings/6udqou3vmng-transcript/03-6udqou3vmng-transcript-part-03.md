---
title: 6udqou3vmng transcript Part 03 —
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6udqou3vmng-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6udqou3vmng transcript Part 03 —

**Source:** `recordings/6udqou3vmng-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Yeah, that's a good question. I don't actually remember. I think there are different options available. And sometimes with some of these reactions, you need to use modified polymerases that can tolerate these modified nucleotides. Yeah, so I don't remember that. It's a good question. I can look that up.**

**So how long can a conventional sequencer go? What's the read length? Anyone know? It's about, say, 600 or so. And so that's reasonably long. How long is a typical mammalian mRNA? Maybe two, three kb? So you have in a typical exon, maybe 150 bases or so. So you have a chunk. You don't generally get full length cDNA. But you get a chunk of a cDNA that's say, three, four exons in length. And that is actually generally sufficient to uniquely identify the gene locus that that read came from.**

**And so that was the basis of EST sequencing-- so-called Expressed Sequence Tag sequencing. And millions of these 600 base chunks of cDNA were generated and they have been quite useful over the years.**

**All right. So what is next-gen sequencing? So in next-gen sequencing, you only read one base at a time. So it's often a little bit slower. But it's really massively parallel. And that's the big advantage. And it's orders of magnitude cheaper per base than conventional sequencing. Like when it first came out it, it was maybe two orders of magnitude cheaper. And now it's probably another four orders of magnitude.**

**So it really blows away conventional sequencing if the output that you care about is mostly proportional to number of bases sequence. If the output is proportional to the**

6

**quality of the assembly or something, then there are applications where conventional sequencing still is very useful Because the next-gen sequencing tends to be shorter. But in terms of just volume, it generates much, much more bases in one reaction.**

**And so the basic ideas are that you have your template DNA molecules. Now typically, tens of thousands for technologies like PacBio or hundreds of millions for technologies like Illumina that are immobilized on some sort of surface-- typically a flow cell-- and there are either single molecule methods where you have a single molecule of your template or there are methods that locally amplify your template and produce, say, hundreds of identical copies in little clusters. And then you use modified nucleotides, often with fluorophores attached, to interrogate the next base at each of your template molecules for hundreds and hundreds of millions of them.**

**And so there are several different technologies. We won't talk about all of them. We'll just talk about two or three that are interesting and widely used. And they differ depending on the DNA template, what types of modified nucleotides are used, and to some extent, in the imaging and the image analysis, which differs for single molecule methods, for example, compared to the ones that sequence a cluster.**

**So there's a table in the Metzger review. And so I've just told you that next-gen sequencing is so cheap. But then you see how much these machines cost and you could buy lots of other interesting things with that kind of money. And I also want to emphasize that that's not even the full cost. So if you were to buy an Illumina GA2-this would be like a couple years ago when the GA2 was the state of the art-- for half a million dollars, the reagents to run that thing, if you're going to run it continuously throughout the year, the reagents to run it would be over a million. So this actually underestimates the cost.**

**However, the cost per base is super, super low. Because they generate so much data at once. All right, So we'll talk about a couple of these.**

**The first next-gen sequencing technology to be published and still used today was from 454-- now Roche-- and it was based on what's called emulsion PCR. So they**

7

**have these little beads, the little beads have adapter DNA molecules covalently attached. You incubate the beads with DNA, and you actually make an emulsion. So it's an oil water emulsion.**

**So each bead, which is hydrophilic, is in the little bubble of water inside oil. And the reason for that is so that you do it at a template concentration that's low enough that only a single molecule of template is associated with each bead. So the oil then provides a barrier so that the DNA can't get transferred from one bead to another. So each bead will have a unique template molecule. You do sort of a local PCR-like reaction to amplify that DNA molecule on the bead, and then you do sequencing one base at a time using a luciferase based method that I'll show you on the next slide.**

**So Illumina technology differs in that instead of an emulsion, you're doing it on the surface of a flow cell. Again, you start with a single molecule of template. Your flow cell has these two types of adapters covalently attached. The template anneals to one of these adapters. You extend the adapter molecule with dNTPs and polymerase. Now you have the complement of your template, your denature.**

**Now you have the inverse complement of your template molecule covalently attached to the cell surface. And then at the other end there's the other adapter. And so what you could do is what's called bridge amplification where that now complement of the template molecule will bridge over hybridized to the other adapter, and then you can extend that adapter. And now you've regenerated your original template. And so now you have the complementary strand, and the original strand, your denature. And then each of those molecules can undergo subsequent rounds of bridge amplification to make clusters of typically several hundred thousand molecules. Is that clear? Question. Yeah, what's your name?**

**AUDIENCE: Stephanie. How do they get the adapters onto the template molecules?**

**PROFESSOR: How do you get the adapters onto the template molecules? So that's typically by DNA ligation. So we may cover that in later steps. It depends. There's a few different protocol. So for example, if you're sequencing microRNAs, you typically**

8

**would isolate the small RNAs and use RNA litigation to get the adapters on. And then you would do an RT step to get DNA.**

**With most other applications like RNA-seq or genome sequencing-- so with RNAseq, you're starting from mRNA, you typically will isolate total RNA, do poly(A) selection, you fragment your RNA to reduce the effects of secondary structure, you random prime with, like, random hexamers RT enzyme. So that'll make little bits of cDNA 200 bases long. You use second strand synthesis. Now you have double stranded cDNA fragments. And then you do, like, blunt end ligation to add the adapters. And then you denature so you have single strand.**

**AUDIENCE: I guess my question is how do you make sure that the two ends sandwiching the DNA are different as opposed to--**

**PROFESSOR: That the two ends are different. Yeah, that's a good question. I'll post some stuff about-- It's a good question. I don't want to sweep it under the rug. But I kind of want to move on. And I'll post a little bit about that.**

**All right so we did 454 Illumina. Helicos is sort of like Illumina sequencing except single molecule. So you have your template covalently attached to your substrate. You just anneal primer and just start sequencing it And there's major pros and cons of single molecule sequencing, which we can talk about.**

**And then the PacBio technology is fundamentally different in that the template is not actually covalently attached to the surface. The DNA polymerase is covalently attached to the surface and the template is sort of threaded into the polymerase. And this is a phage polymerase that's highly processive and strand displacing. And the template is often a circular molecule. And so you can actually read around the template multiple times, which turns out to be really useful in PacBio because the error rate is quite high for the sequencing.**

**So in the top, in the 454, you're measuring luciferase activity-- light. In Illumina, you're measuring fluorescence. Four different fluorescent tags, sort of like the four different tags we saw in Sanger sequencing. Helicose, it's single tag one base at a**

9

**time. And in PacBio, you actually have a fluorescently labeled dNTP that has the label on-- it's actually hexaphosphate-- it's got the label on the sixth phosphate.**

**So the dNTP is labeled. It enters the active site of the DNA polymerase. And the residence time is much longer if the base is actually going to get incorporated into that growing chain. And so you measure how much time you have a fluorescent signal. And if it's long, that means that that base must have incorporated into the DNA.**

**But then, the extension reaction itself will cleave off the last five phosphates and the fluorophore tag. And so you'll regenerate native DNA. So that's another difference. Whereas in Illumina sequencing, as we'll see, there's this reversible terminator chemistry. So the DNA is not native that you're synthesizing.**

**So this is just a little bit more on 454. Just some pretty pictures. I think I described that before. The key chemistry here is that you add one dNTP at a time. So only a subset of the wells-- perhaps a quarter of them-- that have that next base, the complementary base free-- as the next one after the primer-- will undergo synthesis. And when they undergo synthesis, you release pyrophosphate.**

**And they have these enzymes attached to these little micro beads-- the orange beads-- sulfurylase and luciferase, that use pyrophosphate to basically generate light. And so then you have one of these beads in each well. You look at which wells lit up when we added dCTP. And they must have had G as the next base and so forth.**

**And there's no termination here. The only termination is because you're only adding one base at a time. So if you have a single gene in the template, you'll add one base. But if you have two Gs in the template, you'll add two Cs. And in principle, you'll get twice as much light.**

**But then you have to sort of do some analysis after the fact to say, OK how much light do we have? And was that one G, two G, and so forth. And the amount of light is supposed to be linear up to about five or six Gs. But that's still a more error-prone**

10

**step. And the most common type of error in 454 is actually insertions and deletions. Whereas in Illumina sequencing, it's substitutions.**

**David actually encouraged me to talk more about sequencing errors and quality scores. And I need to do a little bit more background. But I may add that a little bit later in the semester.**

**OK, so in Illumina sequencing, you add all four dNTPs at the same time. But they're non-native. They have two major modifications. So one is that they're three prime blocked. That means that the OH is not free, I'll show the chemical structure in a moment.**

**So you can't extend more than one base. You incorporate that one base, and the polymerase can't do anything more. And they're also tagged with four different fluors. So you add all four dNTPs at once. You let the polymerase incorporate them. And then you image the whole flow cell using two lasers and two filters.**

**So basically, to image the four fluors. So you have to sort of take four different pictures of each portion of the flow cell and then the camera moves and you scan the whole cell. And so then, those clusters that incorporated a C, let's say, they will show up in the green channel as spots. And those incorporated in A, and so forth.**

**So you basically have these clusters, each of them represents a distinct template, and you read one base at a time. So, first you read the first base after the primer. So it's sequencing downwards into the template. And you read the first base so you know what the first base of all your clusters is. And then you reverse the termination. You cleave off that chemical group that was blocking the 3-prime OH so now it can extend again. And then you add the four dNTPs again, do another round of extension, and then image again, and so forth.**

**And so it takes a little while. Each round of imaging takes about an hour. So if you want to do 100 base single and Illumina sequencing, it'll be running on the machine for about four days or so. Plus the time you have to build the clusters, which might be several hours on the day before.**

11

**So what is this? So actually the whole idea of blocking termination-- basically Sanger's idea-- is carried over here in Illumina sequencing with a little twist. And that's that you can reverse the termination. So if you look down here at the bottom, these are two different 3-prime terminators. Remember your base counting. Base one, two, three. So this was the 3-prime OH, now it's got this methyl [INAUDIBLE], or whatever that is. I'm not much of a chemist, so you can look that one up.**

**And then here's another version. And this is sort of chemistry that can cleave this off when you're done. And then this whole thing here, hanging off the base, is the fluor. And you cleave that off as well. So you add this big complicated thing, you image it, and then you cleave off the fluor and cleave off the 3-prime block.**

**These are some actual sequencing images you would image in the four channels. They're actually black and white. These are pseudocode. And then you can merge those and you can see then all the clusters on the flow cell. So this is from a GA2 with the recommended cluster density back in the day, like a few years ago. And nowadays, the image now since the software has gotten a lot better, so you can actually load the clusters more densely and therefore get more sequence out of the same area.**

**But imagine just millions and millions of these little clusters like this. Notice the clusters are not all the same size. Basically, you're doing PCR in situ, and so some molecules are easier to amplify by PCR than others. And that probably accounts for these variations in size.**

**So what is the current throughput? These data are accurate as of about, maybe, last year. So the HiSeq 2000 instrument is the most high performance, widely used instrument. Now there's a 2500, but I think it's roughly similar. You have one flow cell. So a flow cell looks sort of like a glass slide, except that it has these tunnels carved in it like eight little tubes inside the glass slide. And on the surfaces of those tubes is where the adapters are covalently attached. And so you have eight lanes and so you can sequence eight different things in those eight lanes. You could do yeast genome in one and fly RNA-seq in another, and so forth.**

12

**And these days, a single lane will produce something like 200 million reads. And this is typically routine to get 200 million reads from a lane. Sometimes you can get more. You can do up to 100 bases. You can do 150 these days on a MiSeq, which is a miniature version. You can do maybe 300 or more. And so that's a whole lot of sequence. So that's 160 billion bases of sequence from a single lane. And that will cost you-- that single lane-- maybe $2,000 to $3,000, depending where you're doing it. And the cost doesn't include the capital cost, that's just the reagent cost for running that.**

**So 160 billion-- the human genome is 3 billion, so you've now sequenced the human genome over many times there.**

**You can do more. So you can do paired-end sequencing, where you sequence both ends of your template. And that'll basically double the amount of sequence you get. And you can also, on this machine, do two flow cells at once. So you can actually double it beyond that.**

**And so for many applications, 160 billion bases is overkill. It's more than you need. Imagine you're doing bacterial genome sequencing. Bacterial genome might be five megabases or so. This is complete overkill. So you can do bar coding where you add little six base tags to different libraries, and then mix them together, introduce them to the machine, sequence the tags first or second, and then sequence the templates. And then you effectively sort them out later. And then do many samples in one lane. And that's what people most commonly do.**

**So, questions about next-gen sequencing? There's a lot more to learn. I'm happy to talk about it more. It's very relevant to this class. But I'm sure it'll come up later in David's sections, so I don't want to take too much time on it.**

**So, now once you generate reads from an Illumina instrument or some other instrument, you'll want to align them to the genome to determine, for example, if you're doing RNA-seq mapping reads that come from mRNA, you'll want to know what genes they came from. So you need to map those reads back to the genome. What are some other reasons you might want to align sequences? Just in general,**

13

**why is aligning sequences-- meaning, matching them up and finding individual bases or amino acid residues that match-- why is that useful? Diego?**

**AUDIENCE: You can assemble them if you want.**

- **PROFESSOR: You can assemble them? Yes. So if you're doing genome sequencing, if you align them to each other and you find a whole stack that sort of align this way, you can then assemble and infer the existence of a longer sequence. That's a good point. Yes, your name?**

**AUDIENCE: Julianne. Looking at homologs.**

**PROFESSOR: Looking at homologs. Right. So if you, for example, are doing disease gene mapping, you've identified a human gene of unknown function that's associated with a disease. Then you might want to search it against, say, the mouse database and find a homolog in mouse and then that might be what you would want to study further. You might want to then knock it out in mouse or mutate it or something. So those are some good reasons. There's others.**

**So we're going to first talk about local alignment, which is a type of alignment where you want to find shorter stretches of high similarity. You don't require alignment of the entire sequence. So there are certain situations where you might want to do that.**

**So here's an example. You are studying a recently discovered human non-coding RNA. As you can see, it's 45 bases. You want to see if there's a mouse homolog. You run it through NCBI BLAST, which as we said is sort of the Google search engine of mathematics-- and you're going get a chance to do it on pump set one, and you get a hit that looks like this.**

**So notice, this is sort of BLAST notation. It says Q at the top. Q is for "query," that's the sequence you put in. S is "subject," that's the database you were searching against. You have coordinates, so 1 to 45. And then, in the subject, it happened to be base 403 to 447 in some mouse chromosome or something. And you can see**

14

**that it's got some matching. But it also has some mismatches. So in all, there are 40 matches and five mismatches in the alignment.**

**So is that significant? Remember, the mouse genome is 2.7 billion bases long. It's big. So would you get a match this good by chance? So the question is really, should you trust this? Is this something you can confidently say, yes mouse is a homolog, and that's it? Or should you just be like, well, that's not better than I get by chance so I have no evidence of anything? Or is it sort of somewhere in between? And how would you tell? Yeah, what's your name?**

- **AUDIENCE: Chris. You would want to figure out a scoring function for the alignment. And then, with that scoring function, you would find whether or not you have a significant match.**

- **PROFESSOR: OK. So Chris says you want to define a scoring system and then use the scoring system to define statistical significance. Do want to suggest a scoring system? What's the simplest one you can think of?**

**AUDIENCE: Just if there's a match, you add a certain score. If it's a mismatch, you subtract a certain score.**

- **PROFESSOR: So let's do that scoring system. So the notation that's often used is Sii. So that would be a match between nucleotide i and then another copy of nucleotide i. We'll call that 1, plus 1 for a match. And sij, where i and j are different, we'll give that a negative score. Minus 1. So this is i not equal to j.**

**So that's a scoring matrix. It's a four by four matrix with 1 on the diagonal and minus 1 everywhere else. And this is commonly used for DNA. And then there's a few other variations on this that are also used. So good, a scoring system. So then, how are we going to do the statistics? Any ideas? How do we know what's significant?**

**AUDIENCE: The higher score would probably be a little more significant than a lower score. But the scale, I'm not sure--**

**PROFESSOR: The scale is not so obvious. Yes, question?**

15

---

[← AUDIENCE](02-audience.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
