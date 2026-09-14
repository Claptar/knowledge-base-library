---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/ljzybexmij0-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `recordings/ljzybexmij0-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **MITOCW | watch?v=lJzybEXmIj0**

**The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.**

**PROFESSOR: Welcome to Foundations of Computational and Systems Biology. This course has many numbers. We'll explain all the differences and similarities. But briefly, there are three undergrad course numbers, which are all similar in content, 7.36, 20.390, 6.802. And then, there are four graduate versions.**

**The 7.91, 20.490, and HST versions are all very similar, basically identical. But the 6.874 has some additional AI content that we'll discuss in a moment. So make sure that you are registered for the appropriate version of this course.**

**And please interrupt with questions at any time. The main goal today is to give an overview of the course, both the content as well as the mechanics of how the course will be taught. And we want to make sure that everything is clear.**

**So this course is taught by myself and Chris Burge from Biology, Professor Fraenkel from BE, and Professor Gifford from EECS. We have three TAs, Peter Freese and Collette Picard, from Computational and Systems Biology, and Tahin, from EECS. All the TAs have expertise in computational biology as well as other quantitative areas like math, statistics, computer science.**

**So in addition to the lectures by the regular instructors, we will also have guest lectures by George Church, from Harvard, toward the end of the semester. Doug Lauffenburger will give a lecture in the regulatory network section of the course. And we'll have a guest lecture from Ron Weiss on synthetic biology. And just a note that today's lecture and all the lectures this semester are being recorded by AMPS, by MIT's OpenCourseWare. So the videos, after a little bit of editing, will eventually end up on OpenCourseWare.**

**What are these courses? So these course numbers are the graduate level versions,**

1

**which are survey courses in computational biology. Our target audience is graduate students who have a solid background and comfort-- or, a solid background in biology, and also, a comfort with quantitative approaches.**

**We don't assume that you've programmed before, but there will be some programming content on the homeworks. And you will therefore need to learn some Python programming. And the TAs will help with that component of the course. We also have some online tutorials on Python programming that are available.**

**The undergrad course numbers-- this is an upper level undergraduate survey course in computational biology. And our target audience are upper level undergraduates with solid biology background and comfort with quantitative approaches. So there's one key difference between the graduate and undergraduate versions, which I'll come to in a moment.**

**So the goal of this course is to develop understanding of foundational methods in computational biology that will enable you to contextualize and understand a good portion of research literature in a growing field. So if you pick up Science, or Nature, or PLOS Computational Biology and you want to read those papers and understand them, after this course, you will have a better chance. We're not guaranteeing you'll be able to understand all of them. But you'll be able to recognize, perhaps, the category of paper, the class, and perhaps, some of the algorithms that are involved.**

**And for the graduate version, another goal is to help you gain exposure to research in this field. So it's actually possible to do a smaller scale computational biology research project on your own, on your laptop-- perhaps, on ATHENA-- with relatively limited computational resources and potentially even discover something new. And so we want to give you that experience. And that's through the project component that we'll say more about in a moment.**

**So just to make sure that everyone's in the right class-- this is not a systems biology class. There are some more focused systems biology classes offered on campus. But we will cover some topics that are important for analyzing complex systems. This is also certainly not a synthetic biology course. Some of the systems methods**

2

**are also used in synthetic biology. And there will be this guest lecturer I mentioned, Ron Weiss, which will cover synthetic biology.**

**It's also not an algorithms class. We don't assume that you have experience in designing or analyzing algorithms. We'll discuss various bioinformatics algorithms. And you'll have the opportunity to implement at least one bioinformatics algorithm on your homework. But algorithms and not really the center of the course.**

**And there's one exception to this, which is, those of you who are taking 6.874 will go to a special recitation that will cover more advanced algorithm content. And there will be special homework problems for you as well. So that course really does have more algorithm content.**

**So the plan for today is that I will just do a brief, anecdotal history of computational and systems biology. This is to set the stage and the context for the class. And then we'll spend a significant amount of time reviewing the course mechanics, organization, and content. Because as you'll see, it's a little bit complicated. But it'll make sense once we go over it, hopefully.**

**So this is my take on computational and systems biology. Again, it's not a scholarly overview. It doesn't hit everything important that happened. It just gives you a flavor of what was happening in computational biology decade by decade.**

**So first of all, where does this field fall in the academic scheme of things? So I consider computational biology to be actually part of biology. So in the way that genetics or biochemistry are disciplines that have strategies for understanding biological questions, so does computational biology. You can use it to understand a variety of computational questions in gene regulation, many other areas.**

**There is also, some people make a distinction that bioinformatics is more about building tools whereas computational biology is more about using tools, for example. Although many people don't-- it's very blurry-- and don't try to-- people use them in various ways. And then, you could think of bioinformatics as being embedded in the larger field of informatics, where you include tools for**

3

**management and analysis of data in general.**

**And it's certainly true that many of the core concepts and algorithms in bioinformatics come from the field, come from computer science, come from other branches of engineering, from statistics, mathematics, and so forth. So it's really a cross disciplinary field. And then, synthetic biology cuts across in the sense that it's really an engineering discipline. Because you're designing and engineering synthetic molecular cellular systems. But you can also use synthetic biology to help understand natural biological systems, of course.**

**All right, so what was happening, decade by decade? So in the '70s, there were not genome sequences available or large sequence databases of any sort. Except there were starting to be some protein sequences. And early computational biologists focused on comparing proteins, understanding their function, structure, and evolution. And so in order to compare proteins, you need a protein-- an amino acid substitution matrix-- a matrix that describes how often one amino acid is substituted for another.**

**And Margaret Dayhoff was a pioneer in developing these sorts of matrices. And some of the matrices she developed, the PAM series, are still used today. And we'll discuss those matrices early next week.**

**So in terms of asking evolutionary questions, two big thinkers were Russ Doolittle and Carl Woese, analyzing both ribosomal RNA sequences to study evolution. And Carl Woese realized, looking at these RNA alignments, that actually, the prokaryotes, which had been-- there was this big split between prokaryotes and eukaryotes was sort of a false split-- that actually, there was a subgroup of singlecelled anuclear organisms that were closer to the eukaryotes-- and named them the Archaea. So a whole kingdom of life was recognized, really, by sequence analysis.**

**And Russ Doolittle also did a lot of analysis approaching sequences and came up with this molecular clock idea, or contributed to that idea, to actually build-- instead of systematics being based on phenotypic characteristics, do it on a molecular level.**

4

**So in the '80s, the databases started to expand. Sequence alignment and search became more important. And various people developed fast algorithms to compare protein and DNA sequences and align them. So the FASTA program was widely used. BLAST-- several of the authors of BLAST are shown here-- David Lipman, Pearson, Webb Miller, Stephen Altschul.**

**The statistics for knowing when a BLAST search result is significant were developed by Karlin and Altschul. And there was also progress in gapped alignment, in particularly, Smith-Waterman, shown above. Also progress in RNA secondary structure prediction from Nusinov and Zuker. We'll talk about all of these algorithms during the course.**

**And there was also development of literature databases. I always liked this picture. Many of you probably used PubMed. But Al Gore was well coached here, by these experts, in how to use it.**

**And then, in the '90s, computational biology really started to expand. It was driven partly by the development of a microarrays, the first genome sequences, and questions like how to identify domains in a protein, how to identify genes in the genome. It was recognized that this family of models from electrical engineering, the hidden Markov model, were quite useful for these sort of sequence labeling problems. That was really pioneered by Anders Krogh here, and David Haussler. And a variety of algorithms were developed that performed these useful tasks.**

**There was also important progress in the earliest comparative genomic approaches, since you have-- the first genomes were sequenced in the mid '90s, of free living organisms. And so you could then start to compare these genomes and learn a lot. We'll talk a little bit about comparative genomics.**

**And there was important progress on predicting protein structure from primary sequence. Particularly, David Baker made notable progress on this Rosetta algorithm. So it's a biophysics field, but it's very much part of computational biology as well.**

5

**So in the 2000s, definitely, genome sequencing became very fashionable, as you can see here. And the genomes of now larger organisms, including human, it became possible to sequence them. And then, this introduced a huge host of computational challenges in assembling the genomes, annotating the genomes, and so forth. And we'll hear from Professor Gifford about some genome assembly topics. And annotation will come up throughout.**

**Actually, let's just mention, this is Jim Kent, who's the guru who did the first human genome assembly-- at least, that was widely used-- and also was involved in UCSC. And here, Ewan Birney has started Ensembl and continues to run it today. You know who these other people are, probably.**

**OK. All right. So in another phase of the last decade, I would say that much of biological research became more high throughput than it was before. So molecular biology had traditionally, in the '80s and '90s, mostly focused on analysis of individual gene or protein products. But now it became possible, and in widespread use, that you could measure the expression of all the genes, in theory-- using microarrays, for example-- and you could start to profile all of the transcripts in the cell, all of the proteins in the cell, and so forth.**

**And then, a variety of groups started to use some of these high throughput data to study various challenges in gene expression to understand how transcription works, how splicing works, how microRNAs work, translation, epigenetics, and so forth. And you'll hear updates on some of that work in this course. Bioimage informatics, particularly for developmental biology, became popular. It continues to be a new emerging area.**

**Systems biology was also really born around 2000, roughly. A very prominent example would be the development of the first gene regulatory network models that describe sea urchin development, here, my Eric Davidson, as well as a whole variety of models of other gene networks in the cell that control things like cell proliferation, apoptosis, et cetera.**

**At the same time, a new field of synthetic biology was born with the development of**

6

**some of the first completely artificial gene networks that would then program cells to perform desired behavior. So an example would be this so-called repressilator, where you have a network of three transcription factors. Each represses the other. And then, one of them represses GFP.**

**And you put these into bacteria. And it causes oscillations in GFP, expressions that are described by these differential equations here. And some of the modeling approaches used in synthetic biology will be covered by Professor Fraenkel and Lauffenburger later.**

**All right. So late 2000s, early 2010s, it's still too early to say, for sure, what the most important developments will be. But certainly, in the late 2000s, next gen sequencing-- which now probably should be called second generation sequencing, since there may be future generations-- really started to transform a whole wide variety of applications in biology, from making genome sequencing-- instead of having to be done in the genome center, now an individual lab can easily do microbial genome sequencing. And when needed, it's possible, also, to do genome sequencing of larger organisms.**

**Transcriptome sequencing is now routine. We'll hear about that. There are applications for mapping protein-DNA interactions genome wide, including both sequence specific transcription factors as well as more general factors like histones, protein-RNA interactions-- a method called CLIP-Seq-- methods for mapping all the translated messages, the methylated sites in the genome, open chromatin, and so forth.**

**So many people contributed to this, obviously. I'm just mentioning, Barbara Wold was a pioneer in both RNA-Seq as well as ChIP-Seq. And some of the sequencing technologies that came out here are shown here. And we will discuss those at the beginning of lecture on Thursday.**

**So I encourage you to read this review here, by Metzger, which covers many of the newer sequencing technologies. And they're pretty interesting. As you'll see, there's some interesting tricks, interesting chemistry and image analysis tricks.**

7

**All right. So that was not very scholarly. But if you want a proper history, then this guy, Hallam Stevens, who was a History of Science PhD student at Harvard and recently graduated, wrote this history of bioinformatics.**

**OK. So let's look at the syllabus. So also posted on the [INAUDIBLE] site is a syllabus. It looks like this. This is quite an information-rich document. It has all the lecture titles, all the due dates of all the problem sets, and so forth. So please print yourself a copy and familiarize yourself with it. So we'll just try to look at a high level first, and then zoom in to the details.**

**So at a high level, if you look in this column here, we've broken the course into six different topics. OK? So there's Genomic Analysis I, that I'll be teaching, which is more classical computational biology, you could say-- local alignment, global alignment, and so forth. Then, Genomic Analysis II, which Professor Gifford will be teaching, covers some newer methods that are required when you're doing a lot of second generation sequencing-- the standard algorithms are not fast enough, you need better algorithms, and so forth.**

**And then, I will come back and give a few lectures on modeling biological function. This will have to do with sequence motifs, hidden Markov models, and RNA secondary structure. Professor Fraenkel will then do a unit on proteomics and protein structure. And then, there will be an extended unit on regulatory networks. Different types of regulatory networks will be covered, with most of the lectures by Ernest, one by David, and one by Doug.**

**And then, we'll finish up with computational genetics, by David. And there will also be some guest lecturers, one of them interspersed in regulatory networks, and then two at the end, from Ron Weiss and George Church.**

**So I just wanted to point out that in all of these topics, we will include some discussion of motivating question. So, what are the biological questions that we're seeking to address with these approaches. And there will also be some discussion of the experimental method.**

8

**So for example, in the first unit, it's heavy on sequence analysis. So we'll talk about how sequencing is done, and then, quite a bit about the interaction between the experimental technology and the computational analysis, which often involves statistical methods for estimating the error rate of the experimental method, and things like that. So the emphasis is on the computational part, but we'll have some discussion about experiments.**

**Everyone with me so far? Any questions? OK.**

**All right. So what are some of these motivating questions that we'll be talking about? So what are the instructions encoded in our genomes? You can think of the genome as a book. But it's in this very strange language. And we need to understand the rules, the code that underlies a lot of research in gene expression.**

**How are chromosomes organized? What genes are present-- so tools for annotating genomes. What regulatory circuitry is encoded? You'd like to be able to eventually look at a genome, understand all the regulatory elements, and be able to predict that there's some feedback circuit there that responds to-- a particular stimulation that responds to light, or nutrient deprivation, or whatever it might be.**

**Can the transcriptome be predicted from the genome? This is a longstanding question. The translatome, if you will-- well, let's say, the proteome can be predicted from the transcriptome in the sense that we have a genetic code and we can look up those triplets. So there's a dream that we would be able to model other steps in gene expression with the precision with which the genetic code predicts translation-that we'd be able to predict where the polymerase would start transcribing, where it will finish transcribing, how a transcript will be spliced, et cetera-- all the other steps in gene expression. And that motivates a lot of work in the field.**

**Can protein function be predicted from sequence? So this is a very classical problem. But there are a number of new and interesting developments as resolved from a lot of this high throughput data generation, both in nucleic acid sequencing as well as in proteomics.**

9

**Can evolutionary history be reconstructed from sequence? Again, this has been a longstanding goal of the field. And a lot of progress has been made here. And now most evolutionary classifications are actually based on molecular sequence at some level. And new species are often defined based on sequence.**

**OK. Other motivating questions. So what would you need to measure if you wanted to discover the causes of a disease, the mechanisms of existing drugs, metabolic pathways in a micro-organism? So this is a systems biology question.**

**You've got a new bug. It causes some disease. What should you measure? Should you sequences its genome? Should you sequence its transcriptome? Should you do proteomics? What type of proteomics? Should you perturb the system in some way and do a time series? What are the most efficient ways? What information should be gathered, and in what quantities? And how should that information be integrated in order to come up with an understanding of the physiology of that organisms so that, then, you can know where to intervene, what would be suitable drug targets?**

**Yeah. What kind of modeling would help you to use the data to design new therapies, or even, in a synthetic biology context, to re-engineer organisms for new purposes? So microbes to generate-- to produce fuel, for example, or other useful products. What can we currently measure?**

**What does each type of data mean individually? What are the strengths and weaknesses of each of the types of high throughput approaches that we have? And how do we integrate all the data we have on a system to understand the functioning of that system? So these are some of the questions that motivate the latter topics on regulatory networks. OK.**

**So let's now zoom in and look more closely at the course syllabus. I've just broken it into two halves, just so it's more readable. So today we're going over, obviously, course mechanics mostly. On Thursday, we'll cover both some DNA sequencing technologies and we'll talk about local alignment on BLAST. More on that in a bit.**

**The 6.8047 recitation-- 6.874, thank you-- recitation will be on Friday. The other**

10

**recitations will start next week. And then, as you can see, we'll move through the other topics. So each of the instructors is going to briefly review their topic. So I won't go through all the titles here.**

**But please note, on the left side here, that their assignment due dates are marked. OK? And they're all due at noon on the indicated day. And so some of these are problem sets. So for example, problem set 1 will be due on Thursday, February 20 at noon.**

**And some of the other assignments relate to the project component of the course, which we're going to talk more about in a moment. In particular, we're going to ask you to submit a brief statement of your background and your research interests related to forming teams. So the projects are going to be done in teams of one to five students.**

**And in order to facilitate especially cross disciplinary teams-- we'd love if you interact with, maybe, students in a different grad program, or whatever-- you'll post your background. You know, I'm a first year BE student and I have a background in Perl programming, but never done Python, or whatever-- something like that. And then, I'm interested in doing systems biology modeling in microbial systems, or something like that.**

**And then you can match up your interests with others and form teams. And then you'll come up with your own project ideas so that the team and initial idea will be due here, February 25th. Then you'll need to do some aims and so forth. So the project components here, these are only for those taking the grad version of the course. We'll make that clear later. OK.**

**So after the first three topics here, taught by myself and David, there will be an exam. More on that later. And then there will be three more topics, mostly taught by Ernest. And notice there are additional assignments here related to the project-- so, to research strategy-- and the final written report, additional problems sets.**

**We'll have a guest lecturer here. This will be Ron Weiss. Then, there will be the**

11

**second exam. Exams are non-cumulative, so the second exam will just cover these three topics here predominantly. And then there will be another guest lecturer. This would be George Church here.**

**And then notice, here, presentation. So those who are doing the project component, those teams will be given-- assigned a time to present, to the class, the results of their research. And you'll be graded-- the presentation will be part of the overall project grade assigned by the instructors. But you'll also-- we'll also ask all the students in the class to send comments on the presentations.**

**So you may find that you get helpful suggestions about interpreting your data from other people and so forth. So that'll be a required component of the course for all students, to attend the presentations and comment on them. And we hope that will be a lot of fun.**

**OK. So is this the right course for me? So I just wanted to let you know you're fortunate to have a rich selection of courses in computational systems, synthetic biology here at MIT. I've listed many of them. Probably not all, but the ones that I'm aware of that are available on-campus.**

**757 is really only for biology grad students. But the other courses listed here are generally open. Some are more geared for graduate students, some more undergrads. Some are more specialized. So for example, Jeff Gore's systems biology course, it's more focused on systems biology whereas our course covers both computational and systems. So keep that in mind. Make sure you're in the right place, that this is what you want.**

**OK. A few notes on the textbook-- so there is a textbook. It's not required. It's called Understanding Bioinformatics by Zvelebil and Baum. It's quite good on certain topics. But it really only covers about, maybe, a third of what we cover in the course. So there is good content on local alignment, global alignment, scoring matrices-- the topics of the next couple lectures. And I'll point you to those chapters.**

**But it's very important to emphasize that the content of the course is really what**

12

**happens in lecture, and on the homeworks, and to some extent, what happens in recitation. And the textbook is just there as a backup, if you will, or for those who would like to get more background on the topic or want to read a different description of that topic. So you decide whether you want to purchase the textbook or not.**

**It's available at the Coop or through Amazon. Shop around. You can find it. It's paperback. Pretty good general reference on a variety of topics, but it doesn't really have much on systems biology.**

**All right. Another important reference that was developed specifically for this course a few years ago is the probability and statistics primer. So you'll notice that some of the homeworks, particularly in the earlier parts of the course, will have significant probability and statistics. And we assume that you have some background in this area. Many of you do. If you don't, you'll need to pick that up. And this primer was written to provide those topics, in probability especially, that are foundational and most relevant to computational biology.**

**So for example, there are some concepts like p-value, probability density function, probability mass function, cumulative distribution function, and then, common distributions, exponential distribution, Poisson distribution, extreme value distribution. If those are mostly sounding familiar to you, that's good. If they're familiar, but you couldn't-- you really don't-- you get binomial and Poisson confused or something, then, definitely, you want to consult this primer.**

**So I think, looking at the lectures and the homeworks, it should probably become pretty clear which aspects are going to be relevant. And I'll try to point those out when possible. And you can also consult your TAs if you're having trouble with the probability and statistics content.**

**So we are going to focus, here, on, really, the computational biology, bioinformatics content. And we might briefly review a concept from probability, like, maybe, conditional probability when we talk about Markov chains. But we're not going to spend a lot of time. So if that's the first time you've seen conditional probability, you**

13

**might be a little bit lost. So you'd be better off reading about it in advance. OK?**

**Questions? No questions? All right. Maybe it's that the video is intimidating people. OK. All right. The TAs know a lot about probability and statistics and will be able to help you.**

**OK. So homework-- so I apologize, the font is a little bit small here. So I'll try to state it clearly. So there are going to be five problem sets that are roughly one per topic. Except you'll see p set two covers topics two and three. So it might be a little bit longer.**

**The way we handle students who have to travel-- so many of you might be seniors. You might be interviewing for graduate schools. Or you might have other conflicts with the course. So rather than doing that on a case by case basis, which, we've found, gets very complicated and is not necessarily fair, the way we've set it up is that the total number of points available on the five homeworks is 120. OK? But the maximum score that you can get is 100.**

**So if you, for example, were to get 90% on all five of the homeworks, that would be 90% of 120, which would be 108 points. You would get the full 100-- you'd get 100% on your homework. That would be a perfect score on the homework. OK? But because of that-- because there's more points available than you need-- we don't allow you to drop homeworks, or to do an alternate assignment, or something like that.**

**So the way it works is you can basically miss-- as long as you do well on, say, four of the homeworks-- you could actually miss one without much of a penalty. For example, if each of the homeworks were worth 24 points and you got a perfect score on four of them, that would be 96 points. You would have an almost perfect score on your homework and you could miss that fifth homework.**

**Now of course, we don't encourage you to skip that homework. We think the homeworks are useful and are a good way to solidify the information you've gotten from lecture, and reading, and so forth. So It's good to do them. And doing the**

14

**homeworks will help you and perhaps prepare you for the exams. But that's the way we handle the homework policy.**

**Now I should also mention that not all the homeworks will be the same number of points. We'll apportion the points in proportion to the difficulty and length of the homework assignment. So for example, the first homework assignment is a little bit easier than the others. So it's going to have somewhat fewer points.**

**So late assignments-- so all the homeworks are due at noon on the indicated day. And if it's within 24 hours after that, you'll be eligible for 50% credit. And beyond that, you don't get any points, in part because the TAs will be posting the answers to the homeworks. OK? And we want to be able to post them promptly so that you'll get the answers while those problems are fresh in your mind. Questions about homeworks? OK. Good.**

**So collaboration on problem sets-- so we want you to do the problem sets. You can do them independently. You can work with a friend on them, or even in a group, discuss them together. But write up your solutions independently. You don't learn anything by copying someone else's solution.**

**And if the TAs see duplicate or near identical solutions, both of those homeworks will get a 0. OK? And this occasionally happens. We don't want this to happen to you. So just avoid that. So discuss together, but write up your solutions separately.**

**Similarly, with programming, if you have a friend who's a more experienced programmer than you are, by all means, ask them for advice, general things, how should I structure my program, do you know of a function that generates a loop, or whatever it is that you need. But don't share code with anyone else. OK? That would be a no-no. So write up your code independently.**

**And again, the graders will be looking for identical code. And that will be thrown out. And so we don't want to have any misconduct of that type occurring.**

**All right. So recitations-- there are three recitation sessions offered each week, Wednesday at 4:00 by Peter, Thursday at 4:00 by Colette, Friday at 4:00 by Tahin.**

15

**And that is a special recitation that's required for the 6.874 students-- David? Yes-and has additional AI content. So anyone is welcome to go to that recitation. But those who are taking 6.874 must go.**

**For students registered for the other versions of the course, going to recitation is optional but strongly recommended. Because the TAs will go over material from the lectures, material that's helpful for the homeworks or for studying for exams-- in the first weeks, Python, probability as well. So go to the recitations, particularly if you're having trouble in the course. So Tahin's recitation starts this week. And Peter and Colette's will start next week.**

---

[Up: contents](index.md) · [Question. Yes. →](02-question-yes.md)
