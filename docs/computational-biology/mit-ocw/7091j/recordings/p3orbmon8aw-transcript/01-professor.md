---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/p3orbmon8aw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/p3orbmon8aw-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**OK, so welcome back to computational systems biology, I'm David Gifford. I'm delighted to be with you here here today. And today we're going to be talking about a topic that is central to modern high throughput biology, which is understanding how to do short read alignment, sometimes called read mapping. Now it's very important to me that you understand what I'm about to say today, and so I'm hopeful that you'll be uninhibited to raise your hand and ask questions about the fine points in today's lecture if you have any, because I'd be totally delighted to answer any questions and we have enough time today that we can spend time looking at one aspect of this problem and understand it thoroughly.**

**An associated topic is the question library complexity. How many people have heard of sequencing libraries before? Let's see a show of hands. OK, how many people have heard of read alignment before, read mapping? OK, great, fantastic. Let's start with what we're going to be talking about today. We're going to first begin talking about what a sequencing library is and what we mean by library complexity.**

**We'll then turn to what has been called a full text minute size index, sometimes called a burrows Wheeler transform index, a BWT index, an FM index, but this is at the center of most modern computational biology algorithms for processing high throughput sequencing data. And then we'll turn how to use that type of index for read alignment. So let's start now with what a sequencing library Is. Let's just say that you have a DNA sample, we'll be talking about various ways of producing said samples throughout the term.**

**But we're going to assume that we have a bunch of different DNA molecules. And I'll illustrate the different molecules here in different colors. And we have three different types of molecules here. Some molecules are duplicated, because as you know,**

1

**typically, we're preparing DNA from an experiment where there are many cells and we can get copies of DNA from those cells or the DNA could be amplified using PCR or some other technique. So we have this collection of molecules, and to make a library, we're going to process it.**

**And one of the things that we'll do when we process the library is we'll put sequencing adapters on. These are short DNA sequences that we put on to the end of the molecules to enable them to have defined sequences at the ends which permits sequencing. Now, if somebody hands you a tube of DNA like this, there are a couple questions you could ask. You could check the DNA concentration to find out how DNA is there, you could run a gel to look at the size of the fragments that you're sequencing. We'll be returning to that later, but these are typically called the insert sizes of the library that you're sequencing, the total length of the DNA excluding the adapters.**

**But we could also ask questions about how complex this library is, because it's possible to run experiments where you produce libraries that are not very complex, where they don't have very many different types of molecules. Now that typically is a failure of the experiment. So an important part of quality control is characterizing the library complexity where we want to figure out here complexity is equal to 3. There are three different types of molecules. And we sample these molecules.**

**And when we sample them, we get a bunch of DNA sequence reads. And typically the number of reads that we get is larger than the complexity of the library. Here we have a total of 12 different reads. And when we sequence a library, we're sampling from it. And so the probability that we get any one particular molecule is going to be roughly speaking equal to 1 over c, which is the complexity. And thus, we could use the binomial distribution to figure out the likelihood that we had exactly four of these type one molecules.**

**However, as n the number of sequencing reads grows to be very large, typical numbers are a hundred million different reads, the binomial becomes cumbersome to work with. And so we typically are going to characterize this kind of selection**

2

**process with a different kind of distribution. So one idea is to use a Poisson, where we say that the rate of sequencing is going to be n over c. And we can see that here shown on the slide above is the same process where we have the ligation of the adapters.**

**We have a library and we have reads coming from the library. We have a characterized library complexity here, there are four different types of molecules. And the modeling approach is that assuming that we have c different unique molecules, the probability that we'll get any one of them when we're doing the sequencing is 1 over c. And if we do end sequencing reads, we can find out the probability that we'll get a certain number of each type of molecule. Let's just stick with the first one to start, OK?**

**Now part of the challenge in analyzing sequencing data is that you don't see what you don't sequence. So things that actually occur 0 times in your sequencing data still may be present in the library. And what we would like to do is from the observed sequencing data, estimate the library complexity. So we have all of the sequencing data, we just don't know how many different molecules there are over here. So one way to do with this is to say that let us suppose that we make a histogram of the number of times we see distinct molecules and we're going to say that we can observe molecules that are sequenced or appear l times up through r times.**

**So we actually can create a version of the distribution that characterizes just a part of what we're seeing. So if we do this, we can build a Poisson model and we can estimate lambda from what we can observe. We don't get to observe things we don't see. So for sure, we know we can't observe the things that are sequenced 0 times. But for the things that are sequenced at least one time, we can build an estimate of lambda. And from that estimate of lambda, we can build an estimate of C.**

**So one way to look at this is that if we look at the total number of unique molecules that we sequence, which is equal to m, then the probability that we observe between l and r occurrences of a given individual sequence times c is going to be**

3

**equal to the total number of unique molecules that we observe. Another way to look at this is the very bottom equation where we note that if we look at the total complexity of the library and we multiply it by 1 minus the probability that we don't observe certain molecules, that will give an estimate of the total number of unique molecules that we do see.**

**And thus we can manipulate that to come up with an estimate of the complexity. Are there any questions about the details of this so far? OK, so this is a very simple model for estimating the complexity of a library based upon looking at the distribution of reads that we actually observe for quality control purposes. And let us suppose that we apply this to thousands genomes data, which is public data on human. And suppose we want to test whether this model works or not, so what we're going to do is we're going to estimate the library complexity from 10 percent of the sequencing reads, so we'll pick 10 percent of the reads of an individual at random, we'll estimate the complexity of the library, and then we'll also take all of the region the individual and estimate the complexity.**

**And if our estimator is pretty good, we should get about the same number, from 10 percent of the reads and from all of the reads. Will people go along with that? Think that seems reasonable? OK, so we do that. And this is what we get. And it's hard to see the diagonal line here, but there's a big oops here. And the big oops is that if we estimate the library complexity from just 10 percent of the reads, it's grossly underestimating the number of unique molecules we actually have. In fact, it's off by typically a factor of two or more.**

**So for some reason, even though we're examining millions of reads in this subsample, we're not getting a good estimate of the complexity of the library. Does anybody have any idea what could be going wrong here? Why is it that this very simple model that is attempting to estimate how many different molecules we have here based upon what we observe is broken? Any ideas at all? And please say your name first.**

**AUDIENCE: I'm Chris.**

4

**PROFESSOR: Hi Chris. AUDIENCE: Is it because repeated sequences, so there could be a short sequence at the end of one molecule that's the beginning of another one, middle of another one, so [INAUDIBLE].**

**PROFESSOR: Chris, you're on the right track, OK? Because what we have assumed at the outset was that all of these molecules occur with equal probability. Right? What would happen if in fact there are four copies of this purple one and only two copies of the other molecules? Then the probability of sampling this one is going to be twice as high as the probability of sampling one of these. If there's non uniformity in the original population, that's going to mess up our model big time.**

**And that could happen from repeated sequences or other kinds of duplicated things, or it could be that there's unequal amplification. It might be that PCR really loves a particular molecule, right, and amplifies that one a lot, and doesn't amplify another one that's difficult to amplify. So somewhere in our experimental protocol pipeline, it could be that there's non uniformity and thus we're getting a skewness to our distribution here in our library. So the other thing that's true is in a Poisson, lambda, which is equal to the mean, is also equal to the variance.**

**And so our Poisson's only one knob we could turn to fit the distribution. So coming back to this, we talked about the idea that the library complexity still may be four but then there may be different numbers of molecules of each type. And here's an idea for you, right? The idea is this. Imagine that the top distributions are the number of each type of molecule that are present. And it might be that our original assumption was that it was like the very top, that typically there are two copies of each molecule in the original sequencing library, and that's a fairly tight distribution.**

**But it could be, in fact, that the number of molecules of each type is very dispersed. And so if we look at each one of those plots at the top, the first four, those are going to be our guesses about the distribution of the number of copies of a molecule in the original library. And we don't know what that is, right? That's something we can't directly observe, but imagine that we took that distribution and used it for lambda in**

5

**our Poisson distribution down below for sampling.**

**So we have one distribution over the number of each type of molecule we have and we have the Poisson for sampling from that, and we put those two together. And when we do that, we have the Poisson distribution at the top, the gamma distribution is what we'll use for representing the number of different species over here and their relative copy number. And when we actually put those together as shown, we wind up with what's called the negative binomial distribution, which is a more flexible distribution, it has two parameters.**

**And that negative binomial distribution can be used, once again, to estimate our library complexity. And when we do so, we have lamba be the same, but k is a new parameter. It measures sort of the variance or dispersion of this original sequencing library. And then when we fit this negative binomial distribution to that 1,000 genomes data, it's going to be hopefully better. Let's start with a smaller example. If we have a library that's artificial with a known million unique molecules and we subsample, it gives you 100,000 reads, you can see that with different dispersions here in the left, k with different values from 0.1 to 20, the Poisson begins to grossly underestimate the complexity of the library as the dispersion gets larger, whereas the negative binomial, otherwise known as the GP or gamma Poisson, does a much better job.**

**And furthermore, when we look at this, in the context of the thousand genomes data, you can see when we fit this how much better we are doing. Almost all those points are almost exactly on the line, which means you can take a small sampling run and figure out from that sampling run how complex your library is. And that allows us to tell something very important, which is what is the marginal value of extra sequencing. So for example, if somebody comes to you and they say, well, I ran my experiment and all I could afford was 50 million reads. Do you think I should sequence more? Is there more information in my experimental DNA preparation?**

**It's easy to tell now, right? Because you can actually analyze the distribution of the reads that they got and you can go back and you could estimate the marginal value**

6

**of additional sequencing. And the way you do that is you go back to the distribution that you fit this negative binomial and ask if you have r more reads, how many more unique molecules are you going to get? And the answer is that you can see that if you imagine that this is artificial data, but if you imagine that you had a complexity of 10 to the 6 molecules, the number sequencing regions is on the x-axis, the number of observed distinct molecules is on the y-axis, and as you increase the sequencing depth, you get more and more back to the library.**

**However, the important thing to note is that the more skewed the library is, the less benefit you get, right? So if you look at the various values of k, as k gets larger, the sort of the skewness of the library increases, and you can see that you get fewer unique molecules as you increase the sequencing depth. Now I mention this to you because it's important to think in a principled way about analyzing sequencing data. If somebody drops 200 million reads on your desk and says, can you help me with these, it's good to start with some fundamental questions, like just how complex is the original library and you think that these data are really good or not, OK?**

**Furthermore, this is a introduction to the idea that certain kinds of very simplistic models, like Poisson models of sequencing data can be wrong because they're not adequately taking into account the over dispersion of the original sequencing count data. OK, so that's all there is about library complexity. Let's move on now to questions of how to deal with these reads once we have them. So the fundamental challenge is this.**

**I hand you a genome like human. 3 times 10 to the ninth bases. This will be in fast a format, let's say. I had you reads. And this will be-- we'll have, say, 200 base pairs times 2 times 10 to the eighth different reads. And this will be in fast q format. The q means that there are-- it's like fast a except that our quality score's associated with each particular base position. And the PHRED score which is typically used for these sorts of qualities, is minus p minus 10 times log base 10 of the probability of an error.**

**Right, so a PHRED score of 10 means that there's a 1 in 10 chance that the bases**

7

**is an error, a PHRED score of 20 means it's one in a 100, and so forth. And then the goal is today if I give you these data on a hard drive, your job would be to produce a SAM file, a Sequence Alignment and Mapping file, which tells us where all these reads map in the genome. And more pictorially, the idea is that there are many different reasons why we want to do this mapping. So one might be to do genotyping. You and I differ in our genomes by about one base in a thousand. So if I sequence your genome and I map it back or align it to the human brain reference genome, I'm going to find differences between your genome and the human reference genome.**

**And you can see how this is done at the very top where we have the aligned reads and there's a G, let's say, in the sample DNA, and there's a C in the reference. But in order to figure out where the differences are, we have to take those short reads and align them to the genome. Another kind of experimental protocol uses DNA fragments that are representative of some kind of biological process. So here the DNA being produced are mapped back to the genome to look for areas of enrichment or what are sometimes called peaks.**

**And there we want to actually do exactly the same process, but the post processing once the alignment is complete is different. So both of these share the goal of taking hundreds of millions of short reads and aligning them to a very large genome. And you heard about Smith Waterman from Professor Berg, and as you can tell, that really isn't going to work, because its time complexity is not going to be admissible for hundreds of millions of reads.**

**So we need to come up with a different way of approaching this problem. So finding this alignment is really a performance bottleneck for many computational biology problems today. And we have to talk a little bit about what we mean by a good alignment, because we're going to assume, of course, fewer mismatches are better. And we're going to try and align to high quality bases as opposed to low quality bases and note that all we have in our input data are quality scores for the reads.**

**So we begin with an assumption that the genome is the truth and when we are**

8

**aligning, we are going to be more permissive of mismatches in read locations that have higher likelihood of being wrong. So is everybody OK with the set up so far? You understand what the problem is? Yes, all the way in the back row, my back row consultants, you're good on that? See, the back row is always the people I call on for consulting advice, right? So yeah. You're all good back there? Good, I like that, good, that's good, I like that, OK.**

**All right. So now I'm going to talk to you about what are the most amazing transforms I have seen. It's called the Burrows Wheeler Transform. And it is a transform that we will do to the original genome that allows us to do this look up very, very quickly. And it's worth understanding. So here's the basic idea behind the Burrows Wheeler Transform. We take the original string that we want to use as our target that we're going to look things up in, OK, so this is going to be the dictionary looking things up in and it's going to be the genome sequence.**

**And you can see the sequence on the left hand side, ACA, ACG, and the dollar sign represents the end of string terminator. OK. Now here's what we're going to do. We take all possible rotations of this string, OK? And we're going to sort them. And the result of sorting all the rotations is shown in the next block of characters. And you can see that the end of string character has the shortest sorting order, followed by A, C, and G and that all the strings are ordered lexically by all of their letters.**

**So once again, we take the original input string, we do all of the possible rotations of it, and then we sort them and wind up with this Burrows Wheeler Matrix as it's called in this slide, OK? And we take the last column of that matrix and that is the Burrows Wheeler Transform. Now yo might say, what on earth is going on here? Why would you want to take a string or even an entire genome? We actually do this on entire genomes, OK? Consider all the rotations of it, sort them, and then take the last column of that matrix. What could that be doing, OK?**

**Here's a bit of intuition for you. The intuition is that that Burrows Wheeler Matrix is representing all of the suffixes of t. OK, so all the red things are suffixes of t in the matrix. And when we are going to be matching a read, we're going to be matched it**

9

**from its end going towards the beginning of it, so we'll be matching suffixes of it. And I'm going to show you a very neat way of using this transform to do matching very efficiently. But before I do that, I want you to observe that it's not complicated. All we do is we take all the possible rotations and we sort them and we come up with this transform. Yes. AUDIENCE: What are you sorting them based on? PROFESSOR: OK, what was your name again? AUDIENCE: I'm Samona. PROFESSOR: Samona. What are we sorting them based upon? We're just sorting them alphabetically. AUDIENCE: OK. PROFESSOR: So you can see that if dollar sign is the lowest alphabetical character, that if you consider each one a word, that they're sorted alphabetically, OK? So we have seven characters in each row and we sort them alphabetically. Or a lexically. Good question. Any other questions like that? This is a great time to ask questions, because what's going to happen is that in about the next three minutes if you lose your attention span of about 10 seconds, you're going to look up and you'll say, what just happened? Yes. AUDIENCE: Could you explain the suffixes of t? PROFESSOR: The suffixes of t? Sure. Let's talk about the suffixes of tr. They're all of the things that end t. So a suffix of t would be G, or CG, or ACG, or AACG, or CAACG, or the entire string t. Those are all of the endings of t. And if you look over on the right, you can see all of those suffixes in red. So one way to think about this is that it's sorting all of the suffixes of t in that matrix. Because the rotations are exposing the suffixes, right, is what's going on. Does that make sense to you? Now keep me honest here in a minute, OK, you'll help me out? Yes. Your name first?**

10

**AUDIENCE: [INAUDIBLE]. [INAUDIBLE]. PROFESSOR: [INAUDIBLE]. AUDIENCE: What is dollar sign? PROFESSOR: Dollar sign is the end of string character which has the lowest lexical sorting order. So it's marking the end of t. That's how we know that we're at the end of t. Good question. Yes. AUDIENCE: Can you sort them non-alphabetically, just different ways to sort them [INAUDIBLE] algorithm? PROFESSOR: The question is, can you sort them non alphabetically. You can sort them any way as long as it's consistent, OK. But let's stick with alphabetical lexical order today. It's really simple and it's all you need. Yes. in red is the suffixes in the last colored group on the right? PROFESSOR: No, no. AUDIENCE: What's in red? PROFESSOR: What's in red are all the suffixes of T on the very far left. OK? AUDIENCE: On the right, last column group? PROFESSOR: The right last column group. That last column in red, that is the Burrows-Wheeler Transform, read from top to bottom. OK? And I know you're looking at that and saying, how could that possibly be useful? We've taken our genome. We've shifted it all around. We've sorted it, we take this last thing. It looks like junk to me, right? But you're going to find out that all of the information in the genome is contained in that last string in a very handy way. Hard to believe but true. Hard to believe but true. Yes. Prepare to be amazed, all right? These are all great questions. Any other questions of this sort? . OK. So, I'm going to make a very important observation here that is going to be crucial for your**

11

**understanding. So I have reproduced the matrix down on this blackboard. What? That's usually there under that board, you know that. You guys haven't checked this classroom before, have you? No. It's always there. It's such a handy transform.**

**So this is the same matrix as the matrix you see on the right. I'm going to make a very, very important assertion right now. OK? The very important assertion is that if you consider that this is the first a in the last column that is the same textual occurrence in the string as the first a in the first column. And this is the second a in the last column, that's the same as the second a in the first column. And you're going to say, what does he mean by that?**

**OK, do the following thought experiment. Look at the matrix. OK? And in your mind, shift it left and put all the characters on the right hand side. OK? When you do that, what will happen is that these things will be used to sort the occurrences a on the right hand side.**

**Once again, if you shift this whole thing left and these pop over to the right, then the occurrence of these a's will be sorted by these rows from here over. But these are alphabetical. And therefore they're going to certain alphabetical order. And therefore these a's will sort in the same order here as they are over there.**

**So that means that when we do this rotation, that this textual occurrence of a will have the same rank in the first column and in the last column. And you can see I've annotated the various bases here with their ranks. This is the first g, the first c, the first end of line, end of string character. First a, second a, third a, second c. And correspondingly I have the same annotations over here and thus the third a here is the same lexical occurrence as the third a on the left in the string, same text occurrence.**

**Now I'm going to let that sink in for a second, and then when somebody asks a question, I'm going to explain it again because it's a little bit counterintuitive. But the very important thing is if we think about textual recurrences of characters in that string t and we put them in this framework, that the rank allows us to identify identical textual recurrences of a character.**

12

**Would somebody like to ask a question? Yes. Say your name and the question, please. AUDIENCE: Dan. PROFESSOR: Dan. AUDIENCE: So in your original string though those won't correspond to the same order in the transformed string. So like the a's in the original string in their order, they don't correspond numerically to the transformed string. PROFESSOR: That's correct. Is that OK? The comment was that the order in BWT, the transform is not the same as the order in the original string. And all I'm saying is that in this particular matrix form, that the order on the last column is the same as the order in the first column for a particular character. And furthermore, that these are matching textual occurrences, right? Now if I look at a2 here, we know that c comes after it, then a, then a, and c and g, right? Right. OK, so did that answer your question that they're not exactly the same?**

**AUDIENCE: Yes. I don't understand how they're useful yet. PROFESSOR: You don't understand how it's useful yet. OK. Well, maybe we better get to the useful part and then you can-- OK. So let us suppose that we want to, from this, reconstruct the original string. Does anybody have any ideas about how to do that? OK.**

**Let me ask a different question. If we look at this g1, right? And then this is the same textual occurrence, right? And we know that this g1 comes right before the end of character, in end of string terminator, right? So if we look at the first row, we always know what the last character was in the original string. The last character is g1, right? Fair enough? OK**

**Where does g1 would occur over here? Right over here, right? What's the character**

13

**before g1? c2. where is c2 over here? What's the character before c2? a3. What's the character before a3? a1. Uh, oh.**

**Let me just cheat a little bit here. a1 a3 c2 g1 $. So we're at a1, right? What's the character before a1? c1, right? What's the character before c1? a2. And what's the character before a2? That's the end of string. Is that the original string that we had? Magic. OK? Yes.**

**AUDIENCE: Wouldn't it be simpler to look at-- to just remove the dollar sign [INAUDIBLE] or do you mean reconstruct from only the transformed? PROFESSOR: We're only using this. This is all we have. Because I actually didn't use any of these characters. I was only doing the matching so we would go to the right row. Right? I didn't use any of this. And so, but do people understand what's going on here? If anybody has any questions, now is a great time to raise your hand and say-- here we go. We have a customer. Say your name and the question, please.**

**AUDIENCE: My name is Eric.**

**PROFESSOR: Thanks, Eric. AUDIENCE: Can you illustrate how you would do this without using any of the elements to the left of the box? PROFESSOR: Absolutely, Eric. I'm so glad you asked that question. That's the next thing we're going to talk about. OK, but before I get to there, I want to make sure, are you comfortable doing it with all the stuff on the left hand side? You're happy about that? OK. if anyone was unhappy about that, now would be the time to say, I'm unhappy, help me. How about the details? Everybody's happy? Yes.**

**AUDIENCE: So, you have your original string in the first place, though, so why do you want to create another string of the same length? Like, how does this help you match your read?**

**PROFESSOR: How does this help you match your read? How does this help you match your read, was the question. What is was your name?**

14

---

[Up: contents](index.md) · [AUDIENCE →](02-audience.md)
