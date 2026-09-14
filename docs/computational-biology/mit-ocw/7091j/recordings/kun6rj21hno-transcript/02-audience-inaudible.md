---
title: 'AUDIENCE: [INAUDIBLE]'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/kun6rj21hno-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE: [INAUDIBLE]

**Source:** `recordings/kun6rj21hno-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: Those are going to be hydrophobic. Exactly. And what about right where the helix emerges from the membrane? [INAUDIBLE] charge residue's there to kind of anchor it and prevent it from sliding back into membrane.**

**And then in general, both on the exterior and interior, you'll tend to have more hydrophilic residues. So that's sort of the basis of TMHMM.**

**So this is the structure. And you'll notice that these are not exactly the hidden states that correspond to individual amino acid residues. These are like meta states, just to illustrate the overall structure.**

**I'll show you the actual states on the next slide. But these were the types of states that the author, Anders [? Crow ?], decided to model. So he has sort of a-- focuses here on the helix core.**

**There's also a cytoplasmic cap and a non-cytoplasmic cap. Oops, didn't mean that. And then there's sort of a globular domain on each side-- both on the cytoplasmic side, or you could have one on the non-cytoplasmic side. OK, so there's going to be different compositions in each of these regions.**

**Now one of the things we talked about with HMMs is that if you were-- now let's**

4

**think about the helix core. The simplest model you might think of would be to have sort of a helix state, and then to allow that state to recur to itself. OK, so this type of thing where you then have some transition to some sort of cap state after, this would allow you to model helices of any length.**

**But now how long are transmembrane helices? What does that distribution look like? Anyone have an idea? There's a certain physical dimension. [INAUDIBLE]**

**It takes a certain number residues to get across here, and then that number is about 20-ish. So transmembrane helices tend to be sort of on the order of 20 plus or minus a few. And so it's totally unrealistic to have a transmembrane helix that's, like, five residues long.**

**So if you run this algorithm in generative mode, what distribution of helix lengths will you produce? We're running in generative mode where we're going to let, remember, to generate a series of hidden states and then associated amino acid sequences. It's coming from some, let's say-- I don't know. What kind of states are there here? [INAUDIBLE] plasmic.**

**Let's say goes into helix, hangs out here. I'm sorry, is there an answer to this question? Anyone? I don't know how long-- if I let it run, it'll generate a random number. It depends on what this probability is here.**

**Let's call this probability p, and then this would be 1 minus p. OK, so obviously if 1 minus p is bigger, it'll tend to produce longer helices. But in general, what is the shape of the distribution there of consecutive helical states that this model will generate?**

**AUDIENCE: Binomial.**

**PROFESSOR: Binomial. OK, can you explain why?**

**AUDIENCE: Because the helix would have to have probable-- the helix of length n would occur 1 minus p to the n power.**

**PROFESSOR: OK, so a helix of length 10 with a probability of then, say, let's call it L, for the length**

5

**of the helix, equals n is 1 minus p to the n, right? Is that binomial? Someone else?**

**AUDIENCE: Yeah. Is it a negative binomial?**

**PROFESSOR: Negative binomial. OK.**

**AUDIENCE: [INAUDIBLE] states and a helix state before moving out [INAUDIBLE].**

**PROFESSOR: Yeah. So the distribution is going to be like that. You have to stay in here for n and then leave. So this is the simplest-- you can have special cases of binomial and negative binomial. But in general, this distribution is called the geometric distribution. Or a continuous version would be the exponential distribution.**

**So what is the shape of this distribution? If I were to plot n down here on this axis, and the probability that L equals n on this axis, what kind of shape-- could someone draw in the air? So you had up and then down?**

**OK, so actually, it's going to be just down. Like that, right? Because as n increases, this goes down because 1 minus p is less than 1. So it just steadily goes down. And what is the mean of this distribution? Anyone remember this? Yeah, so there's sort of two versions of this that you'll see.**

**One of them is the 1 minus p n minus 1 p, and one of them is this. And so this is the number of failures before a success, if you will. Successes lead to the helix. And this is the number of trials till the first success. So one of them has a mean that's 1/p, and the other has a mean that's 1 minus p over p. So usually, p is small, and so those are about the same.**

**So 1/p. You could think that 1/p is roughly right. And so if we were to model transmembrane helices, and if transmembrane heresies are about-- I said about 20 residues long-- you would set p to what value to get the right mean?**

**AUDIENCE: 0.05.**

**PROFESSOR: Yeah. 0.05. 1/20, so that 1 over that will be about 20, right? And then 1 minus p**

6

**would, of course, be 0.9.**

**So if I were to do that, I would get a distribution that looks about like this with a mean of 20. But if I were to then look at real transmembrane helices and look at their distribution, I would see something totally different. It would probably look like that.**

**It would have a mean around 20. But the probability of anything less than 15 would be 0. That's too short. It can't go across the membrane.**

**And then again, you don't have ones that are 40. They don't kind of wiggle around in there and then come out. They tend to just go straight across.**

**So there's a problem here. You can see that if you want to make a more accurate model, you want to not only get the right emission probabilities with the right probabilities of hydrophobics and hydrophilics and the different states, but you also want to get the length right. And so the trick that-- well, actually, yeah. Can anyone think of tricks to get the right length distribution here?**

**How do we do better than this? Basically, hidden Markov models where you have a state that will recur to itself, it will always be a geometric distribution. The only choice you have is what is that probability. And so you can get any mean you want, but you always get this shape.**

**So if you want a more general shape, what are some tricks that you could do? How could you change the model? any ideas? Yeah, go ahead.**

**AUDIENCE: [INAUDIBLE] have multiple helix states.**

**PROFESSOR: Multiple helix states. OK. How many?**

**AUDIENCE: Proportional to the length we want, [INAUDIBLE]. PROFESSOR: Like one for each possible length.**

**AUDIENCE: It'd be less than one length.**

7

**PROFESSOR: Or less than one. OK. So you could have something like-- I mean, let's say you have like this. Helix begin-- or, helix 1, helix 2. You allow each of these to recur to themselves. What does that get you?**

**This actually gets you something a little bit better. It gives you a little bit about of-it's more like that. So that's better.**

**But if I want to get the exact distribution, then actually one-- so this is the solution that the authors actually used. They made essentially 25 different helix states, and then they allowed various different transitions here. So it's a larger arbitrary here, but they have this special state three that can kind of take a jump.**

**So it can just continue on to four, and that'll make your maximum length helix core. Or it can skip one, go to five, and that'll make a helix core that's one residue shorter than that, or it can skip two, and so forth. And you can set any probabilities you want on these transitions.**

**As so you can fit basically an arbitrary distribution within a fixed range of lengths that's determined by how many states you have. OK, so they really wanted to get the length distribution right, and that's what they did. What's the cost of this? What's the downside? Simona?**

**AUDIENCE: I was just going to ask, it looks like from this your minimum helix length could be four.**

**PROFESSOR: Yeah. That's a good question. Well, we don't know what the probabilities-- they say said on that. Well, did they really mean that? And also, that's only the core, and maybe these cap things can be-- yeah, that seems a little short to me. So yeah, I agree. I'm not sure. It could just be for the sake of illustration, but they don't actually use those. But anyway, I'll probably have to read the paper. I haven't read this paper for many years so I don't remember exactly the answer to that.**

**But I have a citation. You can look it up if you're curious. But the main point I wanted to make with this is just that by setting an arbitrary number of states and putting in**

8

**possible transitions between them, you can actually construct any length of distribution you want. But there is a downside, and what is that downside?**

**AUDIENCE: Computational cost.**

**PROFESSOR: Yeah, the computational cost. Instead of having one helix state, now we've got 25 or something. So and the time goes up by the square of the number of states, so it's going to run slower. And you also have to estimate all these parameters.**

**OK, so here's an example of the output of the TMHMM program for a mouse chloride channel gene, CLC6. So the program predicts that there are seven transmembrane helices, as shown by these little red blocks here. You can see they're all about the same-- about 20 or so-- and that the program starts outside and ends inside.**

**So let's say you were going to do some experiments on this protein to test this prediction. So one of the types of experiments people do is they put some sort of modifiable or modified residue into one of the spaces between the transmembrane helices. And then you can test, by modifying this cell with something that's a nonpermeable chemical, can you modify that protein? So only if that stretches on the outside of the cell will you be able to predict it.**

**So that's a way of testing the topology. So if you were doing those types of experiments, you might actually-- like maybe you're not sure if every transmembrane helix is correct. There could be some where the boundaries were a little off, or even a wrong helix.**

**And so one of the things that you often want with a prediction is not only to know what is the optimal or most likely prediction, but also how confident is the algorithm in each of the parts of its prediction. How confident is it in the location of transmembrane helix three or the probability that actually there is a transmembrane helix three. And so the way that this program does that is using something called the forward-backward algorithm.**

**So those of you who read the Rabener tutorial, it's described pretty well there. The**

9

**basic idea is that I mentioned that this Po-- the probability of the observable sequence summing over all possible HMM structures or all possible sequences of hidden states-- that is possible to calculate.**

**And the way that you do it is you run an algorithm that's similar to the Viterbi, but instead of taking the maximum entering each hidden state at intermediate positions, you sum those inputs. So you just do the sum at every point. And it turns out that will calculate the sum of the two values at the end-- or the k values at the end will be equal to the sum of the probabilities of generating the observable sequence over all possible sequences of hidden states. OK, so that's useful.**

**And then you can also run it backwards. There's no reason it has to be only going in one direction. And so what you do is you run these sort of summing versions of the Viterbi in both the forward direction and also run one in the backward direction.**

**And then you take a particular position here-- like let's say this is your helix state, for example. And we're interested in this position somewhere in the middle of the protein. Is that a helix or not?**

**And so basically you take the value that you get here from the forward in your forward algorithm and the value that you get here in the backward algorithm, and multiply those two together, and divide by this Po. And that gives you the probability. So that ends up being a way of calculating the sum of all the parses that go through this particular position i in the sequence in that particular state.**

**I mean, I realize that may not have been totally clear, and I don't want to take more time to totally go into it, but it is pretty well described and Rabener. And I'll just give you an example. So if you're motivated, please take a look at that. And if you have further questions, I'd be happy to discuss during office hours next week.**

**And this is what it looks like for this particular protein. So you get something called the posterior probability, which is the sum of the probabilities of all the parses. And they've plotted it for the particular state that is in the Viterbi path, that is in the optimal parse-- so for example, in blue here.**

10

**Well, actually, they've done it for all the different states here. So blue is the probability that you're outside. OK, so it's very, very confident that the end terminus of the protein is outside the cell. It's very, very confident in the locations of transmembrane helices one and two.**

**It actually more often than not thinks there's actually a third helix right here, but that didn't make it in the optional parse. That actually occurs in the majority of parses, but not in the optimal. And it's probably because it would then cause other things to be flipped later on if you had transmembrane helix there.**

**It's not sure whether there's a helix there or not, but then it's confident in this one. OK, so this gives you an idea. Now if you wanted to do some sort of test of the prediction, you want to test probably first the higher confidence predictions, so you might do something right here.**

**Or if maybe from experience you know that when it has a probability that's that high, it's always right, so there's no point testing it. So you should test one of these kind of less confident regions. So this actually makes the prediction much more useful to have some degree of confidence assigned to each part of the prediction.**

**So for the remainder of today, I want to turn to the topic of RNA secondary structure. So at the beginning, I will sort of get through some nomenclature. And then to motivate the topic, give some biological examples of RNA structure. Gives me an excuse to show some pretty pictures of structure.**

**And then we'll talk about two approaches which are two of the most widely used approaches toward predicting structure. So using evolution to predict structure by method of co-variations, which works well when you have many homologous sequences. And then using sort of first principles thermodynamics to predict secondary structure by energy minimization where obviously you don't need to have a homologous sequence present. And the nature biotechnology primer on RNA folding that I recommended is a good intro to the energy minimization approach.**

**So what is RNA secondary structure? So you all know that RNAs, like proteins, have**

11

**a three-dimensional tertiary fold structure that, in many cases, determines their function. But there's also sort of a simpler representation of this structure where you just describe which pairs of bases are hydrogen bonded to one other.**

**OK, and so for RNA-- so it's a famous example of an RNA structure, this sort of clover leaf structure that all tRNAs have. The secondary structure of the tRNA is the set of base pairs. So it's this base pair here between the first base and this one toward the end, and then base right here, and so forth.**

**And so if you specify all those base pairs, then you can then draw a picture like this, which gives you a good idea of what parts of the RNA molecule are accessible. So for example, it won't tell you where the anticodon loop is, which is sort of the business end of the tRNA. But it narrows it down to three possibilities.**

**You might consider that, or that, or down here. It's unlikely to be something in here because these bases are already paired. They can't pair to message. So it gives you sort of a first approximation toward the 3D structure, and so it's quite useful.**

**So how do we represent secondary structure? So there's a few different common representations that you'll see. So one is-- and this is sort of a computer-friendly but not terribly human-friendly representation, I would say-- is this sort of dot in parentheses notation here.**

**So the dot is an unpaired base and the parenthesis is a paired base. And how do you know-- chalk is sort of non-uniformly distributed here-- so if you have a structure like this and you have these three parentheses, what are they paired to? Well, you don't know yet until you get further down.**

**And then each left parenthesis has to have a right parenthesis somewhere. So now if we see this, then we know that there are two unpaired bases here, and then there's going to be three in a row that are paired-- these guys. We don't know what they're paired to yet.**

**Then there's going to be a five base pair loop, maybe a little pentagon type thing. Two, three, four-- oops-- four, five. And this one would be the right parentheses that**

12

**pair with the left parentheses over here. I should probably draw this coming out to make it clearer that it's not paired. So this notation you can convert to this. So after a while, it's relatively easy to do this, except when they're super long.**

**So that's what the left part of that would look like. So what about the right part? So the right part, we have something like one, two, three, four, bunch of dots, and then we have two, and then a dot, and then two. What does that thing look like?**

**So that's going to look like four bases here in a stem. Big loop, and then there's going to be two bases that are paired, and then a bulge, and then two more that are paired. These things happen in real structures.**

**OK and then the arced notation is a little more human-friendly. It actually draws an arc between each pair of bases that are hydrogen bonded. So I'm sure you can imagine what those structures would look like.**

**And it turns out that the arcs are very important. Like whether those arcs cross each other or not is sort of a fundamental classification of RNA secondary structures, into the ones that are tractable and the ones that are really difficult. So pretty pictures of RNA.**

**So this is a lower resolution cryo-EM structure of the bacterial ribosomes. Remember, ribosomes have two sub-units-- a large sub-unit, 50S, and a small subunit, 30S. And if you crack it open-- OK, so you basically split. You sort of break the ribosome like that, and you look inside, they're full of tRNAs.**

**So there are three pockets that are normally distinguished within ribosomes. The A site-- this is the site where the tRNA enters that's going to add a new amino acid to the growing peptide chain. The P site, which is this tRNA will have it [INAUDIBLE] with the actual growing peptide. And then the exit tunnel where this tRNA will eventually-- the exit, the E site, which is the one that was added a couple of residues ago.**

**So people often think of RNA structure just in terms of these secondary structures because they're much easier to generate than tertiary structures, and they give you-**

13

**- like for tRNA, it gives you some pretty good information about how it works. But for a large and complex structure like the ribosome, it turns out that RNA is actually not bad at building complex structures. I would say it's not as good as protein, but it is capable of constructing something like a long tube.**

**And in fact, in the ribosome, you find such a long tube right here. That is where the peptide that's been synthesized exits the ribosome. And you'll notice it's not a large cavity in which the protein might start folding.**

**It's a skinny tube that is thin enough that the polypeptide has to remain linear, cannot start folding back on itself. So you sort of extrude the protein in a linear, unfolded confirmation, and let it fold outside of the ribosome. If it could fold inside that, that might clog it up. That's probably one reason why it's not designed that way. I'm sure that was tried bye evolution and rejected.**

**So if you look at the ribosome-- now remember, the ribosome is composed of both RNA and protein-- you'll see that it's much more of one than the other. And so it's really much more of the fettuccine, which is the RNA part, than the linguini of the protein. And if you also look at the distribution of the proteins on the ribosome, you'll see that they're not in the core.**

**They're kind of decorated around the edges. It really looks like something that was originally made out of RNA, and then you sort of added proteins as accessories later. And that's probably what happened. This is based on the structures that were solved a few years ago.**

**If you then look at where the nearest proteins are to the active site-- actual catalytic site-- remember, the ribosome catalyzes peptide in addition to an amino acid to a growing peptide, so peptide bond formation-- you'll find that the nearest proteins are around 18 to 20 angstroms away. And this is too far to do any chemistry, so the active site residues or molecules need to be within a few angstroms to do any useful chemistry. And so this basically proves that the ribosome. Is a ribozyme. That is, it's an RNA enzyme. RNAs is [INAUDIBLE].**

14

**So here is the structure of a ribosome. It's very kind of beautiful, and it's impressive that somebody can actually solve the structure of something this big. But what is actually the practical use of this structure? Turns out there's quite an important practical application of knowing the structure. Any ideas?**

**AUDIENCE: Antibiotics.**

**PROFESSOR: Antibiotics. Exactly. So many antibiotics work by taking advantage of differences between the prokaryotic ribosome structure and eukaryotic ribosome structure. So if you can make a small molecule-- these are some examples-- that will inhibit prokaryotic ribosomes but hopefully not inhibit eukaryotic ribosome, then you can kill bacteria that might be infecting you.**

**So non-coding RNA. So there's many different families of non-coding RNAs, and I'm going to list some in a moment. And I'm going to actually challenge you, see if you can come up with any more families of non-coding RNAs.**

**But they're receiving increasing interest, I would say, ever since micro RNA's were discovered. Sort of a boom in looking at different types of non-coding RNAs. Link RNA is also important and interesting, as well as many of the classical RNA's like tRNAs and rRNAs and snoRNAs.**

**There may be new aspects of their regulation and function that will be interesting. And so when you're studying a non RNA, it's very, very helpful to know its structure. If it's going to base pair in trans with some other RNA-- as tRNAs do, as micro RNA's do, for example, or snRNAs and snoRNAs-- then you want to know which parts of the molecule are free and which are internally based paired.**

**And if you want to predict non RNAs genes in a genome, you may want to look for regions that are under selection for conservation of RNA structure, for conservation of the potential to base pair at some distance. If you see that, it's much more likely that that region of the genome encodes a non-coding RNA than it codes, for example-- there's a coding axon or that it's a transcription factor binding site or something like that that functions at the DNA level. So having this notion of**

15

**structure-- even just secondary structure-- is helpful for that application as well, and predicting functions as well, as I mentioned.**

**So co-variation. So let's take a look at these sequences. So imagine you've discovered a new class of mini micro RNA's. They're only eight bases long, and you've sequence five homologues from your five favorite mammals.**

**And these are the sequences that you get. And you know that they're homologous by [? a centimeter ?], they're in the same place in the genome, and they seem to have the same function. What could you say about their secondary structure based on this multiple alignment? You have to stare at it a little bit to see the pattern. There's a pattern here.**

**Any ideas? Anyone have a guess about what the structure is? Yeah, go ahead.**

**AUDIENCE: There's a two base pair stem, and then a four base loop.**

**PROFESSOR: Two base pair stem, four base loop, and you have of the stem. So how do you know that? AUDIENCE: So if you look at the first two and last two bases of each sequence, the first and the eighths nucleotide can pair with each other, and so can the second and the seventh.**

**PROFESSOR: Yeah. Everyone see that? So in the first column you have AUACG, and that's complementary to UAUGC. Each base is complementary. And the second position is CAGGU complementary to GUCUA. There's one slight exception there.**

**AUDIENCE: [INAUDIBLE]**

**PROFESSOR: Yeah. Well, it turns out that that RNA-- although the Watson Crick pairs GC and AU are the most stable-- GU pairs are only a little bit less stable than AU pairs, and they occur in natural RNA molecules. So GU is allowed in RNA even though you would never see that in DNA. OK, so everyone see that?**

16

**So the structure is-- I think I have it here. This would be co-variation You're changing the bases, but preserving the ability to pair. So when one base change-when the first base changes from A to U, the last base changes from U to A in order to preserve that pairing.**

**You wouldn't know that if you just had two sequences, but once you get several sequences, it can be pretty compelling and allow you to make a pretty strong inference that that is the structure of that molecule. So how would you do this? So imagine you had a more realistic example where you've got a non-coding RNA that's 100 or a few hundred bases long, and you might have a multiple alignment of 50 homologous sequences.**

**You want something, you're not going to be able to see it by eye. You need sort of a more objective criterion. So one method that's commonly used is this statistic IX mutual information.**

**So if you look in your multiple alignment-- I'll just draw this here. You have many sequences. You consider every pair of columns-- this is a multiple alignment, so this column and this column-- and you calculate what we're going to call-- what are we going to call it? f ix.**

**That would be the frequency of a nucleotide x. You're in column i, so you just count how many A's, C's, G's, and T's there are. And similarly, f jy for all the possible values of x and all the possible values of y.**

**So these are the base frequencies in each column. And then you calculate the dinucleotide frequencies xy at each pair of columns. So in this colony, you say if there's an A here and a C here, and then there's another AC down here, and there's a total of one, two, three, four, five, six, seven sequences, then f AC ij is 2/7.**

**So you just calculate the frequency of each dinucleotide. These are no longer consecutive dinucleotides in a sequence necessarily there. They can be in arbitrary spacing.**

17

**OK, so you calculate those and then you throw them into this formula, and out comes a number. So what does this formula remind of? Have you seen a similar formula before? AUDIENCE: [INAUDIBLE] PROFESSOR: Someone said [INAUDIBLE] Yeah, go ahead. AUDIENCE: It reminds me of the Shannon entropy [INAUDIBLE]. PROFESSOR: Yeah, it looks like Shannon entropy, but there's a log of a ratio in there, so it's not exactly Shannon entropy. So what other formula has a log of a ratio in it? AUDIENCE: [INAUDIBLE] PROFESSOR: Relative. So it actually looks like relative entropy. So relative entropy of what versus what? Who can sort of say more precisely if it's-- we'll say it's relative entropy of something versus a p versus q. And what is p and what is q? Yeah, in the back. AUDIENCE: Is it relative entropy of co-occurrence versus independent occurrence? PROFESSOR: Good. Yeah. co-occurence-- everyone get that? Co-occurrence of a pair of nucleotide xy at positions ij. Versus q is an independent occurrence. So if x and y occurred independently, they would have this frequency. So if you think about it, you calculate the frequency of each base at each column in the multiple alignment. And this is like your null hypothesis. You're going to assume, what if they're evolving independently? So if it's not a folded RNA-- or if it's a folded RNA but those two columns don't happen to interact-- there's no reason to suspect that those bases would have any relationship to each other. So this is like your expected value of the frequency of xy in position ij. And then this p is your observed value. So you're taking relative entropy of basically observed over expected.**

**And so relative entropy has-- I haven't proved this, but it's non-negative. It can be 0,**

18

**and then it goes up to some maximum, a positive value, but it's never negative. And what would it be if, in fact, p were equal to q? What would this formula give?**

**This is where we're saying suppose. Suppose this. In general, this won't be sure, but suppose it was equal to that. We've got mi ij equals summation of what?**

**That log of this, which is equal to this, so it's fx i fy j over the same thing-- hope you can see that-- log of-- log of 1 is 0, right? So it's just 0.**

**So if the nucleotides of the two columns occur completely independently, mutual information is 0. And that's one reason it's called mutual information. There's no information. Knowing what's in column i gives you no information about column j. So remember, relative entities are measures of information, not entropy.**

**And what is the maximum value that the mutual information could have? Any ideas on that? Any guesses? Joe, yeah.**

**AUDIENCE: You could have log base 2 log over f sub x, f sub y.**

**PROFESSOR: Of 1? OK, so you're saying if one of the particular dinucleotides had a frequency of 1?**

**AUDIENCE: Yeah. So if they're always the same whenever there's-- like an A, there's always going to be a T.**

**PROFESSOR: Right. So whenever there's an A, there's always a G or a T.**

**AUDIENCE: So then you'd get a 1 in the numerator, and they're relative probably in the bottom, which would be maximized if they were all even.**

**PROFESSOR: If they were all?**

---

[← PROFESSOR](01-professor.md) · [Up: contents](index.md) · [[INTERPOSING VOICES] →](03-interposing-voices.md)
