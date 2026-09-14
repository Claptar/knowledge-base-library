---
title: PROFESSOR
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/6udqou3vmng-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROFESSOR

**Source:** `recordings/6udqou3vmng-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Yeah, so that's a good idea. BLAST, as it turns out-- is pretty fast. So you could shuffle your RNA molecule, randomly permute the nucleotides many times, maybe even like 1,000 times, search each one against the mouse genome, and get a distribution of what's the best score-- the top score-- that you get against a genome, look at that distribution and say whether the score of the actual one is significantly higher than that distribution or just falls in the middle of that somewhere. And that's reasonable.**

**You can certainly do that, and it's not a bad thing to do. But it turns out there is an analytical theory here that you can use. And so that you can determine significance more quickly without doing so much computation. And that's what we'll talk about. But another issue, before we get to the statistics, is how do you actually find that alignment? How do you find the top scoring match in a mouse genome?**

**So let's suppose this guy is your RNA. OK, of course, we're using T's, but that's just because you usually sequences it at the DNA level. But imagine this is your RNA. It's very short. This is like 10 or so, I think. And this is your database. But it goes on a few billion more. Several more blackboards. And I want to come up with an algorithm that will find the highest scoring segment of this query sequence against this database.**

**Any ideas? So this would be like our first algorithm. And it's not terribly hard, so that's why it's a good one to start with. Not totally obvious either. Who can think of an algorithm or something, some operation that we can do on this sequence compared to this sequence-- in some way-- that will help us find the highest scoring match? I'm sorry. Yeah?**

**AUDIENCE: You have to consider insertion and deletion.**

16

**PROFESSOR: Yeah, OK. So we're going to keep it simple. That's true, in general. But we're going to keep it simple and just say no insertions and deletions. So we're going to look for an ungapped local alignment. So that's the algorithm that I want. First, no gaps. And then we'll do gaps on Tuesday. Tim?**

**AUDIENCE: You could just compare your [INAUDIBLE] to [INAUDIBLE] all across the database and turn off all the [INAUDIBLE] on that [INAUDIBLE], and then figure out [INAUDIBLE].**

**PROFESSOR: Yeah, OK. Pretty much. I mean, that's pretty much right. Although it's not quite as much of a description as you would need if you want to actually code that. Like, how would you actually do that? So, I want a description that is sort of more at the level of pseudocode. Like, here's how you would actually organize your code.**

**So, let's say you entertain the hypothesis that the alignment can be in different registers. The alignment can correspond to base one of the query and base one of the subject. Or it could be shifted. It could be an alignment where base 1 of the query matches these two, and so forth. So there's sort of different registers. So let's just consider one register first. The one where base 1 matches.**

**So let's just look at the matches between corresponding bases. I'm just going to make these little angle bracket guys here. Hopefully I won't make any mistakes. I'm going to take this. This is sort of implementing Tim's idea here. And then I'm going to look for each of these-- so consider it going down here. Now we're sort of looking at an alignment here. Is this a match or a mismatch?**

**That's a mismatch. That's a match. That's a mismatch. That's a mismatch. That's a match. Match Match. Mismatch. Mismatch. Mismatch. So where is the top scoring match between the query and the subject? Tim? Anyone?**

**AUDIENCE: 6, 7, 8. PROFESSOR: 6, 7, 8. Good. Oh-AUDIENCE: 5, 6, 7.**

17

**PROFESSOR: 5, 6, 7. Right. Right here. You can see there's three in a row. Well, what about this? Why can't we add this to the match? What's the reason why it's not 2, 3, 4, 5, 6, 7?**

**AUDIENCE: Because the score for that is lower.**

- **PROFESSOR: Because the score for that is lower. Right. We defined top scoring segment. You sum up the scores across the map. So you can have mismatches in there, but this will have a score of 3. And if you wanted to add these three bases, you would be adding negative 2 and plus 1, so it would reduce your score. So that would be worse.**

   - **Any ideas on how to do this in an automatic, algorithmic way? Yeah? What's your name?**

**AUDIENCE: Simon. So if you keep shifting the entire database, [INAUDIBLE].**

**PROFESSOR: OK so you keep shifting it over, and you generate one of these lines. But imagine my query was like 1,000 or something. And my database is like a billion. How do I look along here? And here it was obvious what the top scoring match is. But if I had two matches here, then we would've actually had a longer match here.**

**So in general, how do I find that that top match? For each of those registers, if you will, you'll have a thousand long diagonal here with 1's and minus 1's on it. How do I process those scores to find the top scoring segment? What's an algorithm to do that?**

**It's kind of intuitively obvious, but I want to do something with, you define a variable and you update it, and you add to it, and subtract. Something like that. But, like a computer could actually handle. Yeah? What was your name? Julianne?**

**AUDIENCE: Could you keep track of what the highest total score is, and then you keep going down the diagonal, And then you update it?**

**PROFESSOR: OK. You keep track of what the highest total score was? AUDIENCE: Yeah. The highest test score.**

18

**PROFESSOR: The highest segment score? OK. I'm going to put this up here. And we'll define max s. That's the highest segment score we've achieved to date. And we'll initialize that to zero, let's say. Because if you had all mismatches, zero would be the correct answer. If your query was A's and your subject was T's. And then what do you do? AUDIENCE: As you go down the diagonal, you keep track of--**

**PROFESSOR: Keep track of what? AUDIENCE: So you look at 1 in 1 first. And then you go 1 in 2, and you find a score of zero. But that's higher than negative 1. PROFESSOR: But the score of the maximum segment at that point, after base 2, is not zero. It's actually 1. Because you could have a segment of one base alignment. The cumulative score is zero. I think you're onto something here that may be also something useful to keep track of. Let's do the cumulative score and then you tell me more. We'll define cumulative score variable. We'll initialize that to zero. And then we'll have some for loops that, as some of you have said, you want to loop through the subject. All the possible registers of the subject. So that would be maybe j equals 1 to subject length minus query length. Something like that. Don't worry too much about this. Again, this is not real code, obviously. It's pseudocode.**

**So then this will be, say, 1 to query language. And so this will be going along our diagonal. And we're going to plot the cumulative score. So here you would you have an update where cumulative score plus equals the score of query position i matched against subject position j. And update that. So that's just cumulative score.**

**So what will it look like? So in this case, I'll just use this down here. So you have zero, 1, 2, minus 1, minus 2. So you'll start at position zero in the sequence. At position 1 you're down here at minus 1 because it was a mismatch.**

**Then at position 2, as you said, we're back up to zero. And then what happens? Go**

19

**down to minus 1, down to minus 2. Then we go up three times in a row until we're up here to 1. And then we go down after that. So where is your highest scoring match in this cumulative score plot? People said it was from 5 to 7. Yeah, question?**

**AUDIENCE: So would it be from like a local minimum to a local maximum? PROFESSOR: Yeah. Exactly. So, what do you want to keep track of? AUDIENCE: You want to keep track of the minimum and the maximum. And look for the range which you maximize to different-PROFESSOR: Yeah, so this is now sort of more what I was looking for in terms of-- so this was the local minimum, and that's the local maximum. This is the score. That's your mass s there. And you also want to keep track of where that happened in both the query and the subject. Does that make sense? So you would keep track of this running cumulative score variable. You keep track of the last minimum. The minimum that you've achieved so far. And so that would then be down here to minus 2. And then when your cumulative score got up to plus 1, you always take that cumulative score, minus the last minimum cumulative score. That gives you a potential candidate for a high scoring segment. And if that is bigger than your current max high scoring segment, then you update it and you would update this. And then you would also have variables that would store where you are. And also, where did that last minimum occur. So I'm not spelling it all out. I'm not going to give you all the variables. But this is an algorithm that would find the maximum score. Yeah, question? AUDIENCE: So you're keeping track of the global maximum, local minimum, so that you can accept the most recent local minimum following the global maximum? PROFESSOR: I'm not sure I got all that. But you're keeping track of the cumulative score. The minimum that that cumulative score ever got to. And the maximum difference, the maximum that you ever in the past have gone up. Where you've had a net**

20

**increment upwards.**

**Like here. So this variable here, this max s, it would be initialized to zero. When you got to here, your last minimum score would be minus 1. Your cumulative score would be zero. You would take the difference of those, and you'd be like, oh I've got a high scoring segment of score one. So I'm going to update that.**

**So now, that variable is now 1 at this point. Then you're going down, so you're not getting anything. You're just lowering this minimum cumulative score down to minus 2 here. And then when you get to here, now you check the cumulative score minus the last minimum. It's 1. That's a tie. We won't keep track of ties.**

**Now at here, that difference is 2. So now we've got a new record. So now we update this maximum score to 2 in the locations. And then we get here, now it's 3, and we update that. Does that make sense?**

**AUDIENCE: Imagine the first dip-- instead of going down to negative 1, it went down to negative 3. PROFESSOR: Negative 3? AUDIENCE: That first dip. PROFESSOR: Right here? So we started back a little bit. So back here, like this? AUDIENCE: No. PROFESSOR: Down to negative 3? AUDIENCE: No.**

**PROFESSOR: But how do we get to negative 3? Because our scoring is this way. You want this dip to minus 3? AUDIENCE: No PROFESSOR: This one minus 3? Imagine we are at minus 3 here?**

21

**AUDIENCE: Yeah. Imagine it dipped to minus 3. And then the next one dipped to higher than that, to minus 2. And then it went up to 1. And so, would the difference you look at be negative 2 to 1, or negative 3 to 1? PROFESSOR: Like that, right? So, minus 3, let's say, minus 2, 1. Something like that. What do people think? Anyone want to--? AUDIENCE: Minus 3 to 1. PROFESSOR: Minus 3 to 1. It's the minimum that you ever got to. This might be a stronger match, but this is a higher scoring match. And we said we want higher scoring. So you would count that.**

**AUDIENCE: So you keep track of both the global minimum and the global maximum, and you take the difference between them. PROFESSOR: You keep track of the global minimum and the current cumulative score, and you take the difference. AUDIENCE: The global maximum-PROFESSOR: It's not necessarily global maximum because we could be well below zero here. We could do like this. From here to here. So this is not the global maximum. This just happens to be, we went up a lot since our last minimum. So that's your high scoring segment. Does that make sense?**

**I haven't completely spelled it out. But I think you guys have given enough ideas here that there;s sort of the core of an algorithm. And I encourage you to think this through afterwards and let me know if there are questions. And we could add an optional homework where I ask you to do this, that we've sometimes had in the past. It is a useful thing to look at.**

**This is not exactly how the BLAST algorithm works. It uses some tricks for faster speed. But this is sort of morally equivalent to BLAST in the sense that it has the same order of magnitude running time.**

22

**So this algorithm-- what is the running time in Big-O notation? So just for those who are non-CS people, when you use this Big-O notation, then you're asking, how does the running time increase in the size of the input? And so what is the input? So we have two inputs. We have a query of length. And let's say subject of length n. So clearly, if those are bigger, it'll take longer to run. But when you compare different algorithms, you want to know how the run time depends on those lengths. Yes. What's your name?**

**AUDIENCE: Sally. m times n. PROFESSOR: So with this, this is what you would call an order mn algorithm. And why is that? How can you see that? AUDIENCE: You have two for loops And for each length, essentially, you're going through everything in the query. And then, for everything that you go through in the query, you would [INAUDIBLE]. PROFESSOR: Right. In this second for loop here, you're going through the query. And you're doing that nested inside of a for loop that's basically the length of the subject. And eventually you're going to have to compare every base in the query to every base in the subject. There's no way around that. And that takes some unit of time. And so the actual time will be proportional to that. So the bigger n gets and m gets, it's just proportional to the product. Does that make sense?**

**Or another way to think about it is, you're clearly going to have to do something on this diagonal. And then you're going to have to do something on this diagonal, and this one, and this one. And actually, you have to also check these ones here. And in the end, the total number of computations there is going to be this times that. You're basically doing a rectangle's worth of computations. Does that makes sense? So that's not bad, right? It could be worse. It could be, like, mn squared or something like that. So that's basically why BLAST is fast.**

**So what do these things look like, in general? And what is the condition on our score**

23

**for this algorithm to work? What if I gave a score of plus 1 for a match, and zero for a mismatch? Could we do this? Joe, you're shaking your head.**

**AUDIENCE: It would just be going up. PROFESSOR: Yeah. The problem is, it might be flat for a while, but eventually it would go up. And it would just go up and up and up. And so your highest scoring segment would, most of the time, be something that started very near the beginning and ended very near the end. So that doesn't work. So you have to have a net negative drift. And the way that's formalized is the expected score has to be negative. So why is the expected score negative in this scoring system that has plus 1 for a match, and minus 1 for a mismatch? Why does that work? AUDIENCE: It should be wrong three quarters of the time. PROFESSOR: Yeah. You'll have a mismatch three quarters of the time. So on average, you tend to drift down. And then you have these little excursions upwards, and those are your high scoring segments. Any questions about that? AUDIENCE: Question. Is there something better than m times n? PROFESSOR: We've got some computer scientists here. David? Better than m times n? I don't think so, because you have to do all those comparisons. And so there's no way around that, so I don't think so. All right. But the constant-- you can do better on the constant than this algorithm thing. AUDIENCE: With multiple queries--**

**PROFESSOR: With multiple queries, yeah. Then you can maybe do some hashing or find some-to speed it up. OK, so what about the statistics of this? So it turns out that Karlin and Altschul developed some theory for just exactly this problem. For searching a query sequence. It can be nucleotide or protein as long as you have integer scores and the average-- or the expected-- score is negative, then this theory tells you how**

24

**often the highest score of all-- across the entire query database comparison-exceeds a cut off x using a local alignment algorithm such as BLAST.**

**And it turns out that these scores follow what's called an extreme value or Gumbel distribution. And it has this kind of double exponential form here. So x is some cut off. So usually x would be the score that you actually observed when you searched your query against the database. That's the one you care about.**

**And then you want to know, what's the probability we would've seen something higher than that? Or you might do x is one less than the score you observed. So what's the chance we observed something the same, as good as this, or better? Does that make sense? And so this is going to be your P value then.**

**So the probability of S. The score of the highest segment under a model where you have a random query against a random database of the same length is 1 minus e to the minus KMN e to the minus lambda x. Where M and N are the lengths of the query and the database. x is the score. And then K and lambda are two positive parameters that depend actually on the details of your score matrix and the composition of your sequences.**

**And it turns out that lambda is really the one that matters. And you can see that because lambda is up there in that exponent multiplying x. So if you double lambda, that'll have a big effect on the answer. And K, it turns out, you can mostly ignore it for most purposes.**

**So as a formula, what does this thing look like? It looks like that. Kind of a funny shape. It sort of looks like an umlauf a little bit, but then has a different shape on the right than the left. And how do you calculate this lambda? So I said that lambda is sort of the key to all this because of its uniquely important place in that formula, multiplying the score.**

**So it turns out that lambda is the unique positive solution to this equation here. So now it actually depends on the scoring matrix. So you see there's sij there. It depends on the composition of your query. That's the pi's. The composition of your**

25

**subject, that's the rj's. You sum over the i and j equal to each of the four nucleotides. And that sum has to be 1. So there's a unique positive solution to this equation.**

**So how would we solve an equation like this? First of all, what kind of equation is this, given that we're going to set the sij, and we're going to just measure the pi and the rj? So those are all known constants, and lambda is what we're trying to solve for here. So what kind of an equation is this in lambda? Linear? Quadratic? Hyperbolic? Anybody know what this is?**

**So this is called a transcendental equation because you have different powers. That sounds kind of unpleasant. You don't take a class in transcendental equations probably. So in general, they're not possible to solve analytically when they get complicated. But in simple cases, you can solve them analytically. And in fact, let's just do one.**

**So let's take the simplest case, which would be that all the pi's are a quarter. All the ri's are a quarter. And we'll use the scoring system that we came up with before, where sii is 1, and sij is minus 1. If i does not equal j.**

**And so when we plug those in to that sum there, what do we get? We'll get four terms that are one quarter, times one quarter, times e to the lambda. There's four possible types of matches, right? They have probability one quarter times a quarter. That's pi and rj. And the e to the lambda sii is just e to the lambda because sii is 1. And then there's 12 terms that are one quarter, one quarter, e to the minus lambda. Because there's the minus 1 score. And that has to equal 1.**

**So cancel this, we'll multiply through by 4, maybe. So now we get e to the lambda plus 3. e to the minus lambda equals 1. It's still a transcendental equation, but it's looking a little simpler. Any ideas how to solve this for lambda? Sally?**

**AUDIENCE: Wouldn't the 1 be 4?**

**PROFESSOR: I'm sorry. 4. Thank you. Yeah, what's your name?**

26

**AUDIENCE: [INAUDIBLE] I think [INAUDIBLE] quadratic equation. If you multiply both sides by [INAUDIBLE] then [INAUDIBLE].**

**PROFESSOR: OK, so the claim is this is basically a quadratic equation. So you multiply both sides by e to the lambda. So then you get e to the 2 lambda plus 3. And then it's going to move this over and do minus 4 e to the lambda equals zero. Is that good?**

**So how is it quadratic? What do you actually do to solve this?**

**AUDIENCE: Well, [INAUDIBLE].**

**PROFESSOR: Change the variable, x equals e to the lambda. Then it's quadratic in x. Solve for x. We all know how to solve quadratic equations. And then substitute that for lambda. OK, everyone got that?**

**If you use 16 different scores to represent all the different types of matches and mismatches, this will be very unpleasant. It's not unsolvable, it's just that you have to use computational numerical methods to solve it. But in simple cases where you just have a couple different types of scores, it will often be a quadratic equation.**

**All right. So let's suppose that we have a particular scoring system-- particular pi's, rj's-- and we have a value of lambda that satisfies those. So we've solved this quadratic equation for lambda. I think we get lambda equals natural log 3, something like that. Remember, it's a unique positive solution. Quadratic equations are two solutions, but there's going to be just one positive one. And then we have that value. It satisfies this equation.**

**So then, what if we double the scores? Instead of plus 1 minus 1, we use plus 2 minus 2? What would then happen? You can see that the original version of lambda wouldn't necessarily still satisfy this equation. But if you think about it a little bit, you can figure out what new value of lambda would satisfy this equation.**

**We've solved for the lambda that solves with these scores. Now we're going to have new scores. sii prime equals 2. sij prime equals minus 2. What is lambda prime? The lambda that goes with these scores? Yeah, go ahead.**

27

**AUDIENCE: Half of the original? PROFESSOR: Half of the original? Right. So you're saying that lambda prime equals lambda over 2. And why is that? Can you explain? AUDIENCE: Because of the [INAUDIBLE]. PROFESSOR: Yeah, if you think about these terms in the sum, the s part is all doubling. So if you cut the lambda apart, and the product will equal what it did before. And we haven't changed the pi's and rj's, so all those terms will be the same. So therefore, it will still satisfy that equation. So that's another way of thinking about it. Yes, you're correct. So if you double the scores, lambda will be reduced by a factor of 2. So what does that tell us about lambda? What is it? What is its meaning? Yeah, go ahead, Jeff. AUDIENCE: Scale of the distribution to the expectant score? Or the range score? PROFESSOR: Yeah. It basically scales the scores. So we can have the same equation here used with arbitrary scoring. It just scales it. You can see the way it appears as a multiplicative factor in front of the score. So if you double all the scores, will that change what the highest scoring segment is? No, it won't change it because you'll have this cumulative thing. It just changes how you label the y-axis. It'll make it bigger, but it won't change what that is. And if you look at this equation, it won't change the statistical significance. The x will double in value, because all the matches are now worth twice as much as what they were before. But lambda will be half as big, and so the product will be the same and therefore, the final probability will be the same. So it's just a scaling factor for using different scoring systems. Everyone got that? All right. So what scoring matrix should we use for DNA? How about this one? So this is now a slight generalization. So we're going to keep 1 for the matches. You don't lose any generality by choosing 1 here for matches, because if you use 2, then lambda is just going to be reduced to compensate.**

28

**So 1 for matches. And then we're going to use m for mismatches. And m must be negative in order to satisfy this condition for this theory to work, that the average score has to be negative. Clearly, you have to have some negative scores.**

**And the question then is, should we use minus 1 like we used before? Or should we use like minus 2 or minus 5, or something else? Any thoughts on this? Or does it matter? Maybe it doesn't matter. Yeah, what's your name?**

**AUDIENCE: [INAUDIBLE]. Would it make sense to not use [INAUDIBLE], because [INAUDIBLE].**

**PROFESSOR: Yeah, OK. So you want to use a more complicated scoring system. What particular mismatches would you want to penalize more and less?**

**AUDIENCE: [INAUDIBLE] I think [INAUDIBLE] needs to be [INAUDIBLE].**

**PROFESSOR: Yeah, you are correct in your intuition. Maybe one of the biologists wants to offer a suggestion here. Yeah, go ahead.**

**AUDIENCE: So it's a mismatch between purine and pyrimidine [INAUDIBLE].**

**PROFESSOR: OK so now we've got purines and pyrimidines. So everyone remember, the purines are A and G. The pyrimidines are C and T. And the idea is that this should be penalized, or this should be penalized less than changing a purine to a pyrimidine. And why does that makes sense?**

**AUDIENCE: Well, structurally they're--**

**PROFESSOR: Structurally, purines are more similar to each other than they are to pyrimidines. And? More importantly, I think. In evolution?**

**AUDIENCE: [INAUDIBLE].**

**PROFESSOR: I'm sorry, can you speak up?**

**AUDIENCE: C to C mutations happen spontaneously in [INAUDIBLE] chemistry.**

**PROFESSOR: Yes. So C to C mutations happen spontaneously. So basically, it's easier because**

29

**they look more similar structurally. The DNA polymerase is more likely to make a mistake and substitute another purine. The rate of purine, purine or pyrimidine, pyrimidine to transversions which switch the type is about three to one, or two to one in different systems. So yeah, that's a good idea.**

**But for simplicity, just to keep the math simple, we're just going to go with one mismatch penalty. But that is a good point. In practice, you might want to do that.**

**So now, I'm saying I'm going to limit you to one mismatch penalty. But I'm going to let you choose any value you want. So what value should you choose? Or does it matter? Or maybe different applications? Tim, yeah?**

**AUDIENCE: I've just got a question. Does it depend on pi and ri? For example, we could use all these numbers. But if the overall wants to be negative, then you couldn't use negative .1.**

**PROFESSOR: Right, that's a good point. You can't make it too weak. It may depend on what your expected fraction of matches is, which actually depends on pi and ri. So if you have very biased sequences, like very AT rich, your expected fraction of matches is actually higher. When you're researching an AT rich sequence against another AT rich sequence, it's actually higher than a quarter.**

**So even minus one might not be sufficient there. You might need to go down more negative. So you may need to use a higher negative value just to make sure that the expected value is negative. That's true. And yeah, you may want to adjust it based on the composition.**

**So let's just do a bit more. So it turns out that the Karlin and Altschul theory, in addition to telling you what the p value is of your match-- the statistical significance-it also tells you what the matches will look like in terms of what fraction of identity they will have. And this is the so-called target frequency equation.**

**The theory says that if I search a query with one particular composition, p, subject meta-composition r-- here, I've just assumed they're the same, both p just for simplicity-- with a scoring matrix sij, which has a corresponding of lambda. Then,**

30

**when I take those very high scoring matches-- the ones that are statistically significant-- and I look at those alignments of those matches, I will get values qij, given by this formula.**

**So look at the formula. So it's qij. So pipj e to the lambda sij. So it's basically the expected chance that you would have base i matching based j just by chance. That's pipj. But then weighted by e to the lambda sij. So we notice for a match, s will be positive, so e to the lambda will be positive. So that will be bigger than 1. And you'll have more matches and you'll have correspondingly less mismatches because the mismatch has a negative. So get the target value score.**

**And that also tells you that the so-called natural scores are actually determined by the fraction of matches that you want in your high scoring segments. If we want 90% matches, we just set qii to be 0.9, and use this equation here. Solve for sij.**

**For example, if you want to find regions with R% identities. Little r is just the r as a proportion. qii is going to be r over 4. This assumes unbiased base composition. A quarter of the matches are acgt. Qij, then, is 1 minus r over 12. 1 minus r is a fraction of non-matching positions. They're 12 different types.**

**Set sii equal to 1, that's what we said we normally do. And then you do a little bit of algebra here. m is sij. And you sort of plug in this equation twice here. And you get this equation. So it says that m equals log of 4 1 minus r over 3 over log 4 r.**

**And for this to be true, this assumes that both the query and the database have uniform composition of a quarter, and that r is between a quarter and 1. The proportion of matches in your high scoring segment-- you want it to be bigger than a quarter. A quarter is what you would see by chance. There's something wrong with your scoring system if you're considering those to be significant. So it's something above 25%.**

**And so it's just simple algebra-- you can check my work at home-- to solve for m here. And then this equation then tells you that if I want to find 75% identical matches in a nucleotide search, I should use a mismatch penalty of minus 1.**

31

**And if I want 99% identical matches, I should use a penalty of minus 3. Not minus 5, but minus 3. And I want you to think about, does that make sense? Does that not make sense? Because I'm going to ask you at the beginning of class on Tuesday to explain and comment on this particular phenomenon of how when you want higher percent identities, you want a more negative mismatch score. Any last questions? Comments?**

32

---

[← AUDIENCE](04-audience.md) · [Up: contents](index.md)
