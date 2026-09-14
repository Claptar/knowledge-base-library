---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/p3orbmon8aw-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/p3orbmon8aw-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Dan.**

**PROFESSOR: That's right, Dan. That's a great question. I'm so glad you asked it. First we'll get to Eric's question and then we'll get to yours. Because I know if I don't give you a good answer that you're going to be very mad, right? OK?**

**Let's talk about the question of how to do this without the other things. So we're going to create something called the last to first function that maps a character in the last row, column, I should say, to the first column. And there is the function right there. It's called LF.**

**You give it a row number. The rows are zero origined. And you give it a character and it tells you what the corresponding place is in the first column. And it has two components. The first is Occ, which tells you how many characters are smaller than that character lexically. So tells you where, for example, the a's start, the c's start, or the g's start.**

**So in this case, for example Occ of c is 4. That is the c's start at 0, 1,2, 3, the fourth row. OK? And then count tells you the rank of c minus 1. So it's going to essentially count how many times c occurs before the c at the row you're pointing at. In this case, the answer is 1 and you add 1 and that gets you to 5, which is this row.**

**So this c2 maps here to c2 as we already discussed. So this LF function is a way to map from the last row to the first row. And we need to have two components. So we need to know Occ, which is very trivial to compute. There are only five elements, one for each base and one for the end of line terminator, which is actually zero. So it will only have integers and count, which is going to tell us the rank in the BWT transform and we'll talk about how to do that presently.**

**OK. So did that answer your question, how to do this without the rest of the matrix? Eric?**

**AUDIENCE: Could you show us step by step on the blackboard how you would reconstruct it?**

15

|**PROFESSOR:**|**How do we reconstruct it?**|
|---|---|
|**AUDIENCE:**|**Yeah.**|
|**PROFESSOR:**|**You mean something like this? Is this what you're suggesting?**|
|**AUDIENCE:**|**Somehow I get a feeling that the first column doesn't help us in understanding how**<br>**the algorithm work only using the last column.**|
|**PROFESSOR:**|**OK. Your comment, Eric, is that you feel like the first column doesn't help us**<br>**understand how the algorithm works, only using the last column, right? OK.**|
|**AUDIENCE:**|**[INAUDIBLE] going back to the first column of data.**|
|**PROFESSOR:**|**OK. Well let's compute the LF function of the character and the row for each one of**<br>**these things, OK? And that might help you, all right? Because that's the central part**<br>**of being able to reverse this transform. So this is, to be more clear, I'll make it more**<br>**explicit. This is LF of I and BWT of i, where i goes from 0 to 6. So what is that value**<br>**for this one right here? Anybody know? Well it would be Occ of g, which is 6, right?**<br>**Plus count of of 6 n g, which is going to be 0.**|


**Or I can look right over here and see that in fact it's 6, right? Because this occurrence of g1 is right here. So this LF value is, it's 6 4 0 a1 is in 1, a2 is in 2, a3 is in 3, c2 is in 5. So this is the LF function, 6 4 0 1 2 3 5. And I don't need any of this to compute it. Because it simply is equal to, going back one slide, it's equal to Occ of c plus count. So it' going to be equal to where that particular character starts on the left hand side and its rank minus 1.**

**And so these are the values for LF. This is what I need to be able to take this string and recompute the original string. If I can compute this, I don't need any of that. And to compute this, I need two things. I need Occ and I need count. All right? Now, I can tell you're not quite completely satisfied yet. So maybe you can ask me another question and it would be very helpful to me.**

**AUDIENCE: How did you get G1's last and first functions score being 6?**

16

**PROFESSOR: OK. Let's take that apart. We want to know what LF of 6 and where was that G1? G1 is 1 and 0, right? Sorry. LF of 1 and g is equal to, right? Is that g and 1 or 0? Oop, sorry it's in 0. So this is what you like me to compute, right?**

**OK what's Occ of g? It's how many characters are less than g in the original string? I'll give you a clue. It's 1, 2, 3, 4, 5, 6.**

**AUDIENCE: [INAUDIBLE]. PROFESSOR: No, it's how many characters are less than g in the original string. How many things are going to distort underneath it? Where do the g's begin in the sorted version? The g's begin in row 6. OK? So OCC of g is 6. Is that-- are you getting hung up on that point?**

**AUDIENCE: Yes. How do you know that without ever referencing back to the first 5 columns? PROFESSOR: Because when we build the index we remember.**

**AUDIENCE: Oh, OK.**

**PROFESSOR: So we have to, I haven't told you this, but I need to compute, I need to remember ways to compute Occ and count really quickly. Occ is represented by four values only. They're where the a's start, the c's start, the t's start, and the g's start. That's all I need to know, four integers. OK? Are you happy with that?**

**Occ, the a's start at 1. The c's start at 4 and the g's start at 6. OK? That's all I need to remember. But I precompute that. OK? Remember it. Are you happy with that no?**

- **AUDIENCE: Yes.**

**PROFESSOR: OK. And then this business over here of count of zero and g. Right? Which is how many g's, what's the rank of this g in the right hand side? 1. Minus 1 is 0. So that's 0. That's how we computed it. OK?**

**These are great questions because I think they're foundational. Yeah.**

17

**AUDIENCE: Occ and count are both precomputed as you're building on this last column [INAUDIBLE]. PROFESSOR: They are precomputed and well, I have not told you, see, you're sort of ahead of things a little bit in that I'd hoped to suspend disbelief and that I could actually build these very efficiently. But yes, they're built at the same time as the index is built. OK? But yes. OK and if I have Occ and count and I have the string, then I can get this. But I can still need to get to Dan's question because he has been very patient over there. He wants to know how I can use this to find sequence region of genome. And he's just being so good over there. I really appreciate that, Dan. Thanks so much for that. Are you happier? OK you're good. All right. So and this is what we just did. The walk left algorithm actually inverts the BWT by using this function to walk left and using that Python code up there, you can actually reconstruct the original string you started with. So it's just very simple. And we went through it on the board. Are there any questions about it at all?**

**AUDIENCE: Yes. Can you actually do this any column? Like, why are you using the last column instead of like, why can't you just change it like the [INAUDIBLE], the equation and make it work for--**

**PROFESSOR: Because a very important thing is that this is actually a very important property right? Which is all the suffixes are sorted here. And if we didn't do that though, I couldn't answer Dan's question. And he'd be very upset. So please be respectful of his interest here. Now, the thing is, the beauty of this is, is that I have all these suffixes sorted and what you're about to see is the most amazing thing, which is that we're going to snap our fingers and, bang, we can map 200 million reads in no time at all.**

**You like that? You're laughing. Oh, oh, that's not a good That's not a good sign. Let's press ahead fearlessly, OK? And talk about how we're going to use this to map read. So we're going to figure out how to use this index and this transform to rapidly**

18

**aligned reads to a reference genome. And we're not talking about one read or 10 reads or 1 million reads. We're talking about hundreds of millions of reads. So it has be very efficient indeed, OK?**

**So here's the essential idea. There's the core algorithm on the slide. Which is that what we do is we take the original query that we have the read that we're trying to match and we're going to process it backwards from the end of the read forwards. And we begin by considering all possible suffixes from row zero to, in this case, it would be row seven. Which is the length of the entire transform.**

**And we iterate and in each iteration we consider suffixes that match the query. So in the first step, right here, let me see if I can get my point working, there we are. So in the first step here, we matching this c. OK? And we compute the LF of the top, which is this row and of the bottom, which is down here pointing off the end, and that takes us to the first d here and to this point.**

**Here are the two c's that could be possible matches to our query, which ends in a c. We then say, oh, the next character we have to match is an a. So we look here at the a we need to match, and starting from this row, which is row four, and this row, which is row six, we compute the LF of each one of these to figure out what rows in a precedes these c's.**

**And the way we compute the LF is that we use the character a to be able to figure out which rows have the a preceding the c. You can see, when we compute those LF functions, what we wind up with are these rows where we have a followed by c. So we're beginning to match the end of our read, as we go from right to left.**

**We then compute the same thing once again, considering the first a and ask what rows are going to allow us to put this a in front of the ac to form our entire read. And we compute the LF once again of these things. And you can see that here it takes us to this specific row aac. So that row represents a suffix that is matching our query exactly.**

**So we iterate this loop to be able to match a read against the index. And we're using**

19

**the LF function to do it. And it's a really beautiful algorithm. And remember, we only have the transform. We don't have the rest of this matrix.**

**So before I press ahead and talk about other details, I think it's important to observe a couple of things that are a little bit counterintuitive about this. One counterintuitive aspect of it is, that when I'm over here for example, and for example when I'm computing the LF here, I'm computing the LF of row two with respect to a. But there's a dollar sign there. Right?**

**So I'm using this to the LF function, to tell me where a suffix would be that actually follows my constraint of having to have an a be the prefix of ac, where I am right now. This code is actually not fake code. It's the actual code that's in a matcher, for matching a read against the index.**

**Now let me just stop right here for a second and see if there any other questions. Dan is getting now his answer to his question, right? About how you actually use this for matching reads. You do this once for every read. And it is linear time. Right? It's the length of the read itself is all the time it takes to match in a huge genome.**

**So once we've built the index of the genome, in fact, most of the time when you're doing this sort of mapping, you don't build the index. You download the index off of a website. And so you don't have to pay for the time to build this index. You just download the index and you take your reads and the time to match all of your sequencing reads against a certain build of whatever genome you're using is simply linear in the number of bases you have. Questions? Yes. And say your name and the question, please.**

**AUDIENCE: How did [INAUDIBLE] come up with intuition [INAUDIBLE]? It seems like they just pulled it out of a hat.**

**PROFESSOR: You know, I asked Mike that the other day. I saw him in a meeting and he sort of surprised at how this has taken off. And he told me some other interesting facts about this, which you probably could deduce. Which is that if you only want to match reads that are four long, you only have to sort this matrix by the first four characters.**

20

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [But there are other little tricks you can play here. →](03-but-there-are-other-little-tricks-you-can-play-here.md)
