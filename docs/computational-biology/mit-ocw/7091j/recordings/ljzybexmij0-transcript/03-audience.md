---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/ljzybexmij0-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/ljzybexmij0-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Are they covering the same material, Peter and Colette?**

**PROFESSOR: Peter and Colette will cover similar material and Tahin will cover different material.**

**Python instruction-- so the first problem set, which will be posted this evening, doesn't have any programming on it. But if you don't have programming, you need to start learning it very soon. And so there will be a significant programming problem on p set two. And we'll be posting that problem soon-- this week, some time. And you'll want to look at that and gauge, how much Python do I need to learn to at least do that problem.**

**So what is this project component that we've been hearing about? So here's a more concrete description. So again, this is only for the graduate versions of the course. So students will-- basically, we've structured it so you work incrementally toward the final research project and so that we can offer feedback and help along the way if needed.**

**So the first assignment will be next week. I think it's on Tuesday. I'll have more instructions on Thursday's lecture. But all the students registered for the grad version will submit their background and interests for posting on the course website. And then you can look at those and try to find other students who have, ideally, similar interests but perhaps somewhat different backgrounds. It's particularly**

16

**helpful to have a strong biologist on the team. And perhaps, a strong programmer would help as well.**

**So then, you will choose your teams and submit a project title and one-paragraph summary, the basic idea of your project. Now we are not providing a menu of research projects. It's your choice-- whatever you want to do, as long as it's related to computational and systems biology.**

**So it could be analysis of some publicly available data. Could be analysis of some data that you got during your rotation. Or for those of you who are already in labs that you're actually working on, it's totally fine and encouraged that the project be something that's related to your main PhD work if you've started on that. And it could also be more in the modeling, some modeling with MATLAB or something, if you're familiar with that.**

**But, a variety of possibilities. We'll have more information on this later. But we want you to form teams. The teams can work independently or with up to four friends in teams of five. And if people want to have a giant team to do some really challenging project, then you can come and discuss with us. And we'll see if that would work.**

**So then there's the initial title and one-paragraph summary. We'll give you a little feedback on that. And then you'll submit an actual specific aims document-- so with actual, NIH-style, specific aims-- the goal is to understand whether this organism has operons or not, or some actual scientific question-- and a bit about how you will undertake that.**

**And then you'll submit a longer two-page research strategy, which will include, specifically, we will use these data. We will use this software, these statistical approaches-- that sort of thing. And then, toward the end of the semester, a final written report will be due that'll be five pages.**

**You'll work on it together, but it'll need to be clear who did what. You'll need an author contribution statement. So and so did this analysis. So and so wrote this section-- that sort of thing. And then, as I mentioned before, there will be oral**

17

**presentations, by each team, on the last two course sessions. OK? Questions about the projects? There's more information on the course info document online. OK? Good.**

**Yes, so for those taking 6.874, in addition to the project, there will also be additional AI problems on both the p sets-- and the exam? David? Yes. OK. And they're optional for others. All right. Good.**

**OK. So how are we going to do the exam? So as I mentioned, there's two 80-minute exams. They're non-cumulative. So the first exam covers, basically, the first three topics. The second exam is on the last three topics. They're 80 minutes. They're during normal class time. There's no final exam.**

**The grading-- so for those taking the undergrad version, the homeworks will count 36% out of the maximum 100 points. And the exams will count 62%. And then, this peer review, where there's two days where you go, and you listen to presentations, and you submit comments online counts 2%. For the graduate Bio BE HST versions, it's 30% homeworks, 48% exams, 20% project, 2% peer review. For the EECS version, 6.874, 25% homework, 48% exams, 20% project, and then, 5% for these extra AI related problems, and 2% peer review.**

**And those should add up to 100. And then, in addition, we will reward 1% extra credit for outstanding class participation-- so questions, comments during class. OK. All right.**

**So a few announcements about topic one. And then, each of us will review the topics that are coming up. So p set one will be posted tonight. It's due February 20th, at noon. It involves basic microbiology, probability, and statistics. It'll give you some experience with BLAST and some of the statistics associated.**

**P set two will be posted later this week. So you don't need to, obviously, start on p set two yet. It's not due for several weeks. But definitely, look at the programming problem to give you an idea of what's involved and what to focus on when you're reviewing your Python. Mentioned the probability/stats primer.**

18

**Sequencing technology-- so for Thursday's lecture, it will be very helpful if you read the review, by Metzger, on next gen sequencing technologies. It's pretty well written. Covers Illumina, 454, PACBIO, and a few other interesting sequence technologies.**

**Other background reading-- so we'll be talking about local alignment, global alignment, statistics, and similarly matrices for the next two lectures. And chapters four and five of the textbook provide a pretty good background on these topics. I encourage you to take a look.**

**OK. So I'm just going to briefly review my lectures. And then we'll have David and Ernest do the same. So sequencing technologies will be the beginning of lecture two. And then we'll talk about local ungapped sequence alignment-- in particular, BLAST.**

**So BLAST is something like the Google search engine of bioinformatics, if you will. It's one of the most widely used tools. And it's important to understand something about how it works, and in particular, how to evaluate the significance of BLAST hits, which are described by this extreme value distribution here.**

**And then, lecture three, we'll talk about global alignment and introducing gaps into sequence alignments. We'll talk about some dynamic programming algorithms-Needleman-Wunsch, Smith-Waterman. And in lecture four, we'll talk about comparative genomic analysis of gene regulation-- so using sequence similarity across genomes two infer location of regulatory elements such as microRNA target sites, other things like that.**

**All right. So I think this is now-- oh sorry, a few more lectures. Then, in the next unit, modeling biological function, I'll talk about the problem of motif finding-- so searching a set of sequences for a common subsequence, or similar subsequences, that possess a particular biological function, like binding to a protein. It's often a complex search space. We'll talk about the Gibbs sampling algorithm and some alternatives.**

**And then, in lecture 10, I'll talk about Markov and hidden Markov models, which**

19

**have been called the Legos of bioinformatics, which can be used to model a variety of linear sequence labeling problems. And then, in the last lecture of that unit, I'll talk a little bit about protein-- I'm sorry, about RNA-- secondary structure-- so the base pairing of RNAs-- predicting it from thermodynamic tools, as well as comparative genomic approaches.**

**And you'll learn about the mfold tool and how you can use a diagram like that to infer that this RNA may have different possible structures that I can fold into, like those shown. All right. So I'm going to pass it off to David here.**

**PROFESSOR: Thanks very much, Chris. All Right. So I'm David Gifford. And I'm delighted to be here.**

**It's really a wonderfully exciting time in computational biology. And one of the reasons it's so exciting is shown on this slide, which is the production of DNA base sequence per instrument over time. And as you can see, it's just amazingly more efficient as time goes forward.**

**And if you think about the reciprocal of this curve, the cost per base is basically becoming extraordinarily low. And this kind of instrument allows us to produce hundreds of millions of sequence reads for a single experiment. And thus do we not only need new computational methods to handle this kind of a big data problem, but we need computational methods to represent the results in computational models.**

**And so we have multiple challenges computationally. Because modern biology really can't be done outside of a computational framework. And to summarise the way people have adapted these high throughput DNA sequencing instruments, I built this small figure for you.**

**And you can see that-- Professor Burge will be talking about DNA sequencing next time. And obviously, you can use DNA sequencing to sequence your own genomes, or the genomes of your favorite pet, or whatever you like. And so we'll talk about, in lecture six, how to actually do genome sequencing. And one of the challenges in doing genome sequencing is how to actually find what you have sequenced. And**

20

**we'll be talking about how to map sequence reads as well.**

**Another way to use DNA sequencing is to take the RNA species present in a single cell, or in a population of cells, and convert them into DNA using reverse transcriptase. Then we can sequence the DNA and understand the RNA component of the cell, which, of course, either can be used as messenger RNA to code for protein, or for structural RNAs, or for non-coding RNAs that have other kinds of functions associated with chromatin.**

**In lecture seven, we'll be talking about protein/DNA interactions, which Professor Burge already mentioned-- the idea that we can actually locate all the regulatory factors associated with the genome using a single high throughput experiment. We do this by isolating the proteins and their associated DNA fragments and sequencing the DNA fragments using this DNA sequencing technology.**

**So briefly, the first thing that we'll look at in lecture five is, given a reference genome sequence and a basket of DNA sequence reads, how do we build an efficient index so that we can either map or align those reads back to the reference genome. That's a very important and fundamental problem. Because if I give you a basket of 200 million reads, we need to build its alignment very, very rapidly, and quickly, and accurately, especially in the context of repetitive elements. Because a genome obviously has many repeats in it. We need to consider how our indexing and searching algorithms are going to handle those sorts of elements.**

**In the next lecture, we'll talk about how to actually sequence a genome and assemble it. So the fundamental way that we approach genome sequencing given today's sequencing instruments is that we take intact chromosomes at the top, which, of course, are hundreds of millions of bases long, and we shatter them into pieces. And then we sequence size selected pieces in a sequencing instrument. And then we need to put the jigsaw puzzle back together with a computational assembler.**

**So we'll be talking about assembly algorithms, how they work, and furthermore, how resolve ambiguities as we put that puzzle together, which often arise in the context**

21

**of repetitive sequence. And in the next lecture, in lecture seven, we'll be looking at how to actually take those little DNA molecules that are associated with proteins and analyze them to figure out where particular proteins are bound to the genome and how they might regulate target genes. Here we see two different occurrences of OCT4 binding events binding proximally to the SOX2 gene, which they are regulating.**

**So that's the beginning of our analysis of DNA sequencing. And then we'll look at RNA sequencing-- once again, with going through a DNA intermediate-- and ask the question, how can we look at the expression of particular genes by mapping RNA sequence reads back onto the genome. And there are two fundamental questions we can address here, which is, what is the level of expression of a given gene, and secondarily, what isoforms are being expressed.**

**The second sets of reads, you see up on the screen, are split reads that cross splice junctions. And so by looking at how reads align to the genome, we can figure out which particular axons are included or excluded from a particular transcript. So that's the beginning of the high throughput biology genomic analysis module. And I'll be returning to talk, later in the term, about computational genetics, which, really, is a way to summarize everything we're learning in the course into an applicable way to ask fundamental questions about genome function, which Professor Burge talked about earlier.**

**Now we all have about 3 billion bases in our genomes. And as you know, you differ from the individual sitting next to you in about one in every 1,000 base pairs, on average. And so one question is, how do we actually interpret these differences between genomes. And how can we build accurate computational models that allow us to infer function from genome sequence? And that's a pretty big challenge.**

**So we'll start by asking questions about, what parts of the genome are active and how could we annotate them. So we can use, once again, different kinds of sequencing based assays to identify the regions of the genome that are active in any given cellular state. And furthermore, if we look at different cells, we can tell**

22

**which parts of the genome are differentially active.**

**Here you can see the active chromatin during the differentiation of an ESL into a terminal type over a 50 kilobase window. And the regions of the genome that are shaded in yellow represent regions that are differentially active. And so, using this kind of DNA seq. data and other data, we can automatically annotate the genome with where the regulatory elements are and begin to understand what the regulatory code of the genome is.**

**So once we understand what parts of the genome are active, we can ask questions about, how do they contribute to some overall phenotype. And our next lecture, lecture 19, we'll be looking at how we can build a model of a quantitative trait based upon multiple loci and the particular alleles that are present at that loci. So here you see an example of a bunch of different quantitative trait loci that are contributing to the growth rate of yeast in a given condition.**

**So part of our exploration during this term will be to develop computational methods to automatically identify regions of the genome that control such traits and to assign them significance. And finally, we'd like to put all this together and ask a very fundamental question, which is, how do we assign variations in the human genome to differential risk for human disease. And associated questions are, how could we assign those variants to what best therapy would be applied to the disease-- what therapeutics might be used, for example.**

**And here we have a bunch of results from genome wide association studies, starting at the top with bipolar disorder. And at the bottom is type 2 diabetes. And looking along the chromosomes, we're asking which locations along the genome have variants that are highly associated with these particular diseases in these socalled Manhattan plots. Because the things that stick up look like buildings.**

**And so these sorts of studies are yielding very interesting insights into variants that are associated with human disease. And the next step, of course, is to figure out how to actually prove that these variants are causal, and also, to look at mechanisms where we might be able to address what kinds of therapeutics might**

23

**be applied to deal with these diseases.**

**So those are my two units. Once again, high throughput genomic analysis, and secondarily, computational genetics. And finally, if you have any questions about 6.874, I'll be here after lecture. Feel free to ask me. Ernest.**

---

[← Question. Yes.](02-question-yes.md) · [Up: contents](index.md) · [PROFESSOR →](04-professor.md)
