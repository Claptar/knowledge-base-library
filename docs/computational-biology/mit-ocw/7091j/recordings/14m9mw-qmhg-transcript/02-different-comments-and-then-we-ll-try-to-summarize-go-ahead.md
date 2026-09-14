---
title: different comments. And then we'll try to summarize. Go ahead.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/14m9mw-qmhg-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# different comments. And then we'll try to summarize. Go ahead.

**Source:** `recordings/14m9mw-qmhg-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**STUDENT: So we're still only filling out an n by n matrix at any given time. PROFESSOR: You're still filling out an n by n matrix, right. There happen to be a few more things. The recursion is slightly more complicated. But there's a few more things you have to calculate to fill in each. But it's like three things, or four things. It's not-- so it doesn't grow with the size. So it's just still n squared, but with a larger constant. OK, good. And then if you did affine gap penalty, remember where you had a gap opening penalty and a gap extension, what then? Does that make it worse? Or is it still n squared? STUDENT: I think it's still n squared. PROFESSOR: Why is that? STUDENT: Computing the affine gap penalty is no more than o of n, right? PROFESSOR: Yeah, basically with the affine you have to keep track of two things at each place. So yeah, it is. You're right. It's still n squared. It's just you got to keep track of two numbers in each place there. OK, good. And so what about when we go to three proteins? So how would you generalize, let's say, the Needleman-Wunsch algorithm to align three proteins? Any ideas? What structure would you use, or what-- analogous to a matrix-- yeah, in the back. STUDENT: Another way to do this would be have a 3D matrix. PROFESSOR: OK, a 3D matrix, like a cube. And can everyone visualize that? So yeah, basically you could have a version of Needleman-Wunsch that was on a cube. And it started in the 0, 0, 0 corner and went down to the n, n, n corner, filling in in 3D. OK so what kind of computational complexity do you think that algorithm would have? STUDENT: n cubed?**

6

**PROFESSOR: n cubed. Yeah, makes sense. There would be a similar number, a few operations to fill in each element in the cube. And there's n cubed. So the way that the problem grows with n is as n cubed.**

**And what about in general, if you have k sequences?**

**STUDENT: n to the k?**

**PROFESSOR: n to the k. So is this practical? With three proteins and modern computers you could do it. You could implement Needleman-Wunsch on a cube. But what about with 20 proteins? Is that practical? So it's really not. So if proteins are 500 residues long and there's 500 to the 20th, right. It starts to explode. So that approach really only works in two dimensions and a little bit in three dimensions. And it becomes impractical. So you need to use a variety of shortcuts. And so this is, again, described pretty well in chapter six of the text.**

**And a commonly used-- if you're looking for a default multiple sequence aligner, CLUSTALW is a common one. There's a web interface if you just need to do one or two alignments. That works fine. You can also download a version called CLUSTALX and run it locally.**

**And it does a lot of things with pairwise alignments and then combining the pairwise alignments. It aligns the two closest things first and then brings in the next closest, and so forth. And it does a lot of tricks that are-- they're basically heuristics. They're things that usually work, give you a reasonable answer, but don't necessarily guarantee that you will find the optimal alignment if you were to do it on a 20 dimensional cube, for example. So they work reasonably well in practice. And then there's a variety of other algorithms.**

**OK, good. So that's a review of what we've mostly been talking about. And now I want to introduce a couple of new topics. So we're going to briefly talk a little bit more about Markov models of sequence evolution. And these are closely related to some classic evolutionary theory from Jukes-Cantor and Kimura. So we'll just briefly**

7

**mention that. And we'll talk a little bit about different types of selection that sequences can undergo-- so neutral, negative, and positive-- and how you might distinguish among those for protein coding sequences.**

**And this will basically serve as an intro into the main topic today, which is comparative genomics. And comparative genomics-- it's not really a field, exactly. It's more of an approach. But I wanted to give you some actual concrete examples of computational biology research, successful research that has led to various types of insights into gene regulation, in this case, mostly to emphasize that computational biology is not just a bag of tools. We've mostly been talking about tools. We introduced tools for local alignment and multiple alignment and statistics and so forth. But really it's a living, breathing field with active research.**

**And even using-- comparative genomics is one of my favorite areas within this field. Because it's very powerful. And you can often use very simple ideas. And simple algorithms can sometimes give you a really interesting biological result, if you have the right sequences and ask the question the right way. So I have posted a dozen of my favorite comparative genomics papers in a special section on the website.**

**Obviously I'm not asking you to read all of these. But I'm going to give you a few insights and approaches that were used in each of these papers here, just to give you a flavor of some of the things that you can do with comparative genomics, in the hopes that this might inspire some of your projects. So hopefully you're going to start thinking about finding teammates and thinking about projects. And this will hopefully help in that direction.**

**Of course, they don't have to be comparative genomics projects. You could do anything in computational biology or systems biology in this class. But that's just one area to start thinking about. Yeah, I'll also-- I'm sorry, I think I haven't posted this yet. But I will also post this review by Sabeti that has a good discussion of positive selection a little bit later. Again, not required.**

**All right, so let's go back to this question that I posed earlier. We have a Markov model of DNA sequence evolution. And we-- sn is the base at generation n. And**

8

**then what happens after a long time? If you take any vector-- q, to start with, might be a known base, for example-- and apply that matrix many times, what happens as n goes to infinity. And so it turns out that there's fairly classical theory here that gives us an answer. This is not all the theory that exists, but this describes the typical case.**

**So the theory says that if all of the elements in the matrix are greater than 0, and then of course all of the-- pij's, when you sum over j, they have to equal 1. That's just for it to be a well-defined Markov chain. Because you're going from i to j. And so from any base you have to go-- the probability of going to one of those four bases has to sum to 1.**

**And so if those conditions hold, then there is a unique vector r such that r equals r times p. And the limit of q times p to the n equals r, independent of what q was. So basically, wherever you were starting from-- you could have been starting from 100% g, or 50% a, 50% g, or 100% c-- you apply this matrix many, many times, you will eventually approach this vector r.**

**And the theory doesn't say what r is, exactly. But it says that r equals r times p. And that turns out to basically implicitly define what r is. That is, you can solve for r using that equation. And r, for this reason, because the matrix doesn't move r, r is called the stationary distribution. And it's often also called the limiting distribution, for obvious reasons. And if you want to read more, like where this theory comes from, here's a reasonable reference. So any questions about this theory?**

**All the elements in the matrix have to be strictly greater than 1-- I'm sorry, strictly greater than 0. Otherwise, really no conditions. All right, question? Yeah, go ahead.**

**STUDENT: Does the [INAUDIBLE] distribution ever change, based on the sequence, or are we assuming that it doesn't?**

**PROFESSOR: The theory says it only depends on p. It doesn't depend on q. So it depends on the model of how the changes happen, the conditional probability of what the base will be at the next generation given what it is at the current generation. It doesn't**

9

**depend where you start. q is what your starting point is, what base you're initially at. Does that make sense?**

**And this is obviously a very simplified case, where we're just modeling evolution of one base, and we're not thinking about whether the rates vary at different positions or within-- this is the simplest case. But it's important to understand the simplest case before you start to generalize that.**

**OK, so let's do some examples here. So here are some matrices. So it turns out the math is a lot easier if you limit yourself to a two-letter alphabet instead of four. So that's what I've done here. So let's look at these matrices and think about what they mean. So we have two-letter alphabet. R is purine. Y is pyrimidine.**

**These matrices describe the conditional probability that, at the next generation, you'll be, for example-- oops, here we go. That, for example, if you start at purine, that you'll remain purine at the next generation. That would be 1 minus P. And the probability that you'll change to pyrimidine is P. And the probability of pyrimidine will remain as a pyrimidine is 1 minus P.**

**So what is the stationary distribution of this matrix? OK, so if p is small, this describes a typical model, where most of the time you remain-- DNA replication and repair is faithful. You maintain the same base. But occasionally a mutation happens with probability p.**

**Anyone want to guess what the stationary distribution is or describe a strategy for finding it? Like what do we know about this distribution? Or imagine you start with a purine and then you apply this matrix many times to that vector that's 1 comma 0, what will happen? Yeah, Levi.**

**STUDENT: Probably 50-50 because any other that way you skew it it would be pushed towards the center because there's more [INAUDIBLE] the other.**

**PROFESSOR: OK, everyone get that? So Levi's comment was that it's probably 50-50. Because mutation probabilities are symmetrical. Purine-pyrimidine and pyrimidine-purine are the same. So if you were to start with say, lots of purine, then there will be more**

10

**mutation toward pyrimidine in a given generation.**

**So if you think about this is your population of R and that's your population of Y, then if this is bigger than that, you'll tend to push it more that way. And there will be less mutation coming this way, until they're equal. And then you'll have equal flux going both directions.**

**So that's a good way to think about it. And that's correct. Can you think of how would you show that? What's a way of solving for the stationary distribution? Anyone? So remember, we'll just get back one. The theory says that R equals RP. That's the key. R equals RP. So what is R?**

**Well we don't know R. So we let that be a general vector. So notice there's only one free parameter. Because the two components have to sum to 1. It's a frequency vector, so x and 1 minus x.**

**And we just multiply this times the matrix. So you take x comma 1 minus x. And you multiply it by this matrix. The matrix is 1 minus P P. I'm using too much space here. I'll just make it a little smaller-- P 1 minus P. And that's going to equal R. And so we'll get x times 1 minus P plus-- remember, it's dot product of this times this column, right? So x times 1 minus P plus 1 minus x times P.**

**That's the first component. And the second component will be xp plus 1 minus x times 1 minus p. OK, everyone got that? So now what do we do?**

**STUDENT: r.**

**PROFESSOR: What's that?**

**STUDENT: Make that equal to the initial r.**

**PROFESSOR: Yeah, make that equal to the initial r. So it's two equations and-- well, you really only need one equation here. Because we've already simplified it. In general there will be two equations. There will be one equation that says that the components of the vector sum to 1.**

11

**And there will be another equation coming from here. But we can just use either one, either term. So we know that the first component of a vector-- if this vector is equal to that vector, then the first components have to be equal, right? So x equals x times-- times what? Times 1 minus p, just combining these two.**

**And then plus what are all the-- I'm sorry, that's 1 minus p-- 1 minus p here. And then there's another term here, minus another p. And then there's a term that's just p. And so then what do you do? You just solve for x.**

**And I think when you work this out you'll get two p x equals p, so x equals 1/2. Right, everyone got that? OK, so yeah. So if x is 1/2, then the vector is 1/2 comma 1/2, which is the unbiased.**

**All right, what about this next matrix, right below-- 1 minus p 1 minus q. p and q are two positive numbers that are different. So now there's actually a different probability of mutating purine to pyrimidine and pyrimidine to purine. So Levi, can we apply your approach to see what the answer is?**

**STUDENT: Not exactly.**

**PROFESSOR: Not exactly? OK, yeah, it's not as obvious. It's not symmetrical anymore. But can anyone guess what the answer might be? Yeah, go ahead Diego.**

**STUDENT: It'll go either all the way to one side or depending on q and d.**

**PROFESSOR: All the way to one side or all the way to the other? So meaning it'll be all purine or all pyrimidine again.**

**STUDENT: Yeah, depending on which--**

**PROFESSOR: Which is bigger? OK, anyone else have an alternative theory? Yeah, go ahead. What was your name again?**

- **STUDENT: Daniel.**

**PROFESSOR: Sorry, Daniel?**

12

|**STUDENT:**|**Daniel, yeah.**|
|---|---|
|**PROFESSOR:**|**Daniel. OK, go ahead.**|
|**STUDENT:**|**It'll reach some intermediate equilibrium once they balance each other out. And that**<br>**would be exactly-- I'm not sure-- some ratio of q to p.**|
|**PROFESSOR:**|**OK. How many people think that might happen? OK, some people. OK Daniel has**<br>**maybe slightly more supporters. So let's see. So how are we going to solve this?**<br>**How do we figure out what the stationary distribution is? You just use that same**<br>**approach. So you can do-- you have x 1 minus x times that matrix, which is got the**<br>**1 minus p p q 1 minus q. OK, and so now you'll get x 1 minus p.**<br>**Anyway, go through the same operations. Solve for x. And you will get-- I think I put**<br>**the answer on the slide here. You will get q over p plus q. So as Danny predicted,**<br>**some ratio involving q's and p's. And does this make sense? Seeing what the**<br>**answer is, can you rationalize why that's true?**|
|**STUDENT:**|**It's like a kind of equilibrium. You have one mode of force play pushing one way and**<br>**another different one in this case pushing the other.**|
|**PROFESSOR:**|**Yeah, that's basically the same idea. And so they have to be in balance. So the one**<br>**that has less, where the mutation rate is a lower, will end up being bigger, so that**<br>**the amount that flows out will be the same as the amount that flows in. You can**<br>**apply Levi's idea of thinking about how much flux is going in each way. So there's**<br>**going to be some flux p in one direction, q in the other direction. And you want x**<br>**times p to equal 1 minus x times q. And this is the value of that works.**<br>**OK, good? What about this guy down here? So this is a very special matrix called**<br>**the identity matrix. And what kind of model of evolution is this?**|
|**STUDENT:**|**There's no mutation.**|
|**PROFESSOR:**|**There's no evolution. This is like a perfect replication repair system. The base never**<br>**changes. So what's a stationary distribution?**|


13

**STUDENT: It's all-PROFESSOR: What's that? STUDENT: It'll just stay where it is. PROFESSOR: It'll stay where it is. That's right. So any vector is stationary for this matrix. Remember that the theory said there's a unique stationary distribution. This seems to be inconsistent. Why is it not inconsistent? Sally? STUDENT: We defined all of the variables to be greater than 0. So when you have anything that's [INAUDIBLE] that is equal to 0. PROFESSOR: Right, so a condition of the theorem is that all the entries be strictly greater than 0. And this is why. If you have 0s, in there then crazy things can happen. Wherever you start, that's where you end up with this matrix. So every vector is stationary. And what about this crazy matrix over here, matrix q? What does it do? Joe. STUDENT: It's going to swap them back and forth. PROFESSOR: It swaps them back and forth. So this is like a hyper mutable organism that has such a high mutation rate that it always mutates every base to the other kind. It's never happy with its genome. It always wants to switch it, get something better. And so what can you say about the stationary distribution for this matrix? Jeff? STUDENT: There isn't going to be one. PROFESSOR: There isn't going to be one? Anyone else? STUDENT: Well, actually, I guess 1, 1, like 0.5, 0.5. PROFESSOR: 0.5, 0.5 would be stationary. Because you're-STUDENT: But you won't converge to it. PROFESSOR: But you won't converge to it. That's right. it's stationary, but not limiting. And again, the theory doesn't apply. Because there's some 0s in this matrix. But you can still**

14

**think about that. OK, everyone got that? All right, good.**

**OK so let's talk now about Jukes-Cantor. So Jukes-Cantor is very much a Markov model of DNA sequence evolution. And it simply has-- now we've got four bases. It's got probability alpha of mutating from each base to any other base. And so the overall mutation rate, or probability of substitution, at one generation is three alpha. Because from the base G there's an alpha probability mutate to A, an alpha probability to C, an alpha to T, so the three alpha.**

**And you can basically write a recursion that describes what's going on here. So if you start with a G at time 0, the probability of a G at time 1 is 1 minus 3 alpha. It's a probability that you didn't mutate. But then, at generation two, you have to consider two cases really.**

**First of all, if you didn't mutate, that's PG1. Then you have a 1 minus alpha probability of not mutating again, so remaining G. But you might have mutated. With probability 1 minus PG 1 you mutated. And then whatever you were-- might be a C-you have an alpha probably of mutating back to G. Does that make sense? Everyone clear why there's a 3 in one place and only a 1 alpha in the other?**

**All right, so you can actually solve this recursion. And you get this expression here, P G of t equals 1/4 plus 3/4 E to the minus 4 alpha t. OK so what does that tell you about-- we know from our previous discussion what the stationary distribution of this Markov chain is going to be. What will it be? What's the stationary distribution?**

**STUDENT: 1/4 of each.**

**PROFESSOR: 1/4 of each. And why, Daniel, is that?**

**STUDENT: Because the probability of them moving to any base is the same?**

**PROFESSOR: Right, it's totally symmetrical. So that has to be the answer by symmetry. And you could solve it. You could use this same approach with defining a value-- the theory applies if alpha is greater than 0 and less than 1-- or less than-- I think it has to be less than a quarter, actually, or something like that.**

15

**And you can apply the theory. So there will be a stationary distribution. You can set up a vector. Now you have to have four terms in it and multiplication. And then you'll get a system of basically four equations and four unknowns. And you can solve that system using linear algebra and get the answer. And yeah, the answer will be 1/4, as you guessed.**

**And so what this Jukes-Cantor expression tells you is how quickly does it get to that equilibrium. We're thinking about G. You can start at 100% G. And it will then approach 1/4. You can see 1/4 is clearly what's going to happen in the limit. Because as t gets big that second term is going to 0. And so what does the distribution look like? How rapidly do you approach 1/4?**

**You approach it exponentially. So you start at 1 here. And this is 0. This is 1/4. You'll start here. And you'll go like that. You go rapidly at the beginning. And then you get just very gradual approach 1/4.**

**So you can do a little bit more algebra with this expression. And here's where the really useful part comes in. And you can show that K, which we'll define as the true number of substitutions that have occurred at this particular base that we're considering, is related to D, where D is the fraction of positions that differ when you just take say the parental sequence and the daughter sequence, the eventual sequence that you get to.**

**You just match those two. And you count up the differences. That's D. And then K is the actual number of substitutions that have occurred. And those are related by this equation, K equals minus 3/4, natural log, 1 minus 4/3 d.**

**So let's try to think about, first of all, what is the shape of that curve? What does that look like? Here's 0. I'll put 1 over here. So we all know that log-- if it was just simply log of something between 0 and 1, it would look like what-- look like that. Starts from negative infinity and comes up to 0 at 1. But it's actually not log of D. It's log of 1 minus D, or 1 minus a constant times D. So that will flip it. So the minus infinity will be there. It will come in like that.**

16

**And then we also have minus 3/4. There's a minus in front of this whole thing. So all these logs are of numbers that are less than 1. So they're all negative. But then it'll get flipped. So it'll actually look like that.**

**And it will go to infinity where? Where does this go to infinity? So if this is now K is on this axis. And yeah, sorry if that wasn't clear. D is here.**

**So this is just again, this is if we did log of D it would look like this. If we do log of 1 minus something times D, that'll flip it. And then if we do minus that, it'll flip it again that way. OK so now K, as a function of D, is going to look like this.**

**Sometimes people like to put-- anyway, but let's just think about this. So it's going to go to up to infinity somewhere. And where is that?**

**STUDENT: 3/4. PROFESSOR: 3/4. So does that make sense? Can someone tell us what's going on and what is the use of this whole thing here? Yeah, in the back. What's your name? STUDENT: Julianne.**

**PROFESSOR: Yeah, Julianne. Go ahead. STUDENT: [INAUDIBLE] 0. So part, it would give you negative infinite. And so you just solve for D in there. PROFESSOR: OK, so when D is 3/4 you'll get 1 minus 1. You get 0. That'll be negative infinity. And then there's a minus in front, so it'll be constant infinity. So that's true. And does that intuitively make sense to you? We have a sequence. It's evolving randomly, according to this model.**

**And then we have that ancestral sequence. And then we have a modern descendant of that sequence, millions of generations-- or maybe thousands of generations, or some large number of generations away. We line up those two sequences. We count how many matches and how many mismatches. What's the fraction of mismatches, of differences we have? Basically if that-- let's look at a**

17

**different case. What if d is very small? What if it's like 1%. Then what happens?**

**If d is small, turns out k is pretty much like d. It grows linearly with d in the beginning. So does that make sense? That makes sense. Because k is the true number of substitutions that happen. When you go one generation, the true number of substitutions and the measured number of substitutions is the same.**

**Because there's no back mutations. But when you go further, there's an increasing chance of a back-- there's an increasing chance of a mutation, therefore increasing chance that you also have a back mutation. And so this is what happens at long time.**

**So basically this is linear here and then goes up like that. And so what this allows you to do is d something that you can measure. And then k is something that you want to know. The point is, if I measure the difference between human and chimp sequence, it might be only 1% different. And if I have an idea of mutation rate per generation, I configure out how many generations apart, or how much time has passed, since humans split from chimp.**

**But if I go to mouse, where the average base might be-- there might be only a 50% matching-- if that's true, there have been a lot of changes there. There will be a lot of bases that have changed once, as well as a lot that may have changed twice, and may have actually changed back.**

**And so that let's say human and mouse are 50% identical. That 50% identical-- I can't just compare it to let's say the 1% with chimp and say it's 50 times longer. That 50% will be an underestimate of the true difference. Because there's been some back mutations as well. And so you have to use this formula to figure out what the true evolutionary time is, the true number of changes that happened. Yeah, go ahead.**

**STUDENT: Does simple count refer to just the difference in the amount of mutations? Or what's--**

**PROFESSOR: The simple count is what you actually observe. So you have a stretch of sequence--**

18

**let's say the beta globin genomic locus in human. You line it up to the beta globin locus in chimp. You count what fraction of positions differ? What fractions are different? That's d.**

**And then k is-- actually, it's slightly complicated here. Because if this is human and that's chimp, then k is more like-- because you don't actually observe the ancestor. You observe chimp. So you have to go back to the ancestor and then forward. So that's the relevant number of generations. And so k will tell you how many changes must have occurred to give you that observed fraction of differences. And for short distances, it's linear. And then for long, it's logarithmic, basically. Yeah, question.**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [STUDENT →](03-student.md)
