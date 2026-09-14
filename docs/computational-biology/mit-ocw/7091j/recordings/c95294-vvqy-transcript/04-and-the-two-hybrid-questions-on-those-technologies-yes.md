---
title: and the two-hybrid. Questions on those technologies? Yes.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/c95294-vvqy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# and the two-hybrid. Questions on those technologies? Yes.

**Source:** `recordings/c95294-vvqy-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: Could another control be for the mass spec purification just to subtract out everything that alludes non-specifically.**

- **PROFESSOR: The question was, could you subtract out anything that's nonspecific. And yes, if you've got what you might call frequent flyers, proteins that show up in every single purification, then you can simply ignore those. And that is often done. So that'll help you with things that are very nonspecific for the surface.**

**What's more of a problem are proteins that have some affinity for your protein x but are not really highly specific for it. So they tend to bind in certain kinds of patches. Those would be harder to figure out because they won't stick to everything. Good question. Other questions?**

**All right. So we've got these different technologies. What we'd really like to be able do is we know that there are problems in each approach. We'd like to be able to compute the probability that two proteins interact based on the data. So now we're turning back to the more mathematical computational approaches.**

**So if we just consider one experiment-- and we're going to talk about gold standard. So what's a gold standard? It's a set of proteins that we have extremely high confidence interact because it was analyzed by some other technology. Not twohybrid, non-affinity capture mass spec, but much, much more direct interactions. By physical measurements, maybe the structural work. So the number of criteria that go into it.**

**So we have this gold standard data set where we know the proteins definitely interact, and we have our experiment. So clearly anything in the overlap, we can count as true positives, right? We detected it. It's in the database of gold standards. And things that are in the gold standard that we missed are obviously false negatives. We report them as non-interacting, but in fact they do.**

**The question is, how much of this is true positive? Everything that's detected in the experiment but we have no information for it in the database. So that could be for**

15

**one of two reasons, right? That could be that they really don't interact. Or it could be that no one's measured it. The whole point of this experiment is to find new things.**

**So is there any way to estimate what fraction of all the things that are unique to this experiment are true positives, and what fraction are false positives? Those we'd like to try to figure out.**

**Now, if we just had one experiment, that would be very challenging. But what happens when we've got two experiments? So we have these two affinity capture mass spec experiments, or maybe affinity capture mass spec and a two-hybrid. So now let's think about the overlap of those two experiments with the gold standard.**

**So I've got this region of overlap between experiment 1 and experiment 2, and then this region that's overlapping between all three things. Experiment 1, experiment 2, and the gold standard. So these clearly are two positives, right? They're high confidence because I picked them up in both experiments, and they're in the gold standard.**

**What about all these things in what I've labeled here region 2? Well, if we believe that these two experiments are independent of each other in a rigorous way-- so let's say one's a two-hybrid and one's an affinity capture mass spec, there's no particular reason that the false positives for one would be false positives in the other. In that case, I can call this region 2 my consensus true positives. I have a very high confidence that these are true interactors. Everyone buy that? Seem reasonable?**

**OK. So here's where the trick comes in. What fraction of all these consensus true positives are picked up in the gold standard? This ratio, right? Region 1 over region 2. OK.**

**So now I've got this region of things that are picked up-- the true positives from this experiment, then the gold standard. And then I've got this region that's unique to experiment 2 and it's going to be some mix of true positives and false positives. And the authors of this paper that are cited here make the following argument.**

16

**We're going to assume that the ratio of I to II is the same as the ratio of III to IV. So the fraction of consensus true positives that are picked-- these are independent experiments. So the fraction of true positives that are picked up in the gold standard is going to be constant, whether they're in the consensus or not.**

**So the fraction at ratio of I to II is going to be the same as the ratio of III to IV. So by that then, I can figure out how much of this region consists of true positives and how much consists of false positives. Everyone buy that? Yeah.**

**AUDIENCE: Can I check-- are we not saying that the gold standard represents all true positives?**

**PROFESSOR: Correct. Well, we're saying that the gold standard consists of things that we know to interact--**

**AUDIENCE: But there may be more.**

**PROFESSOR: But there may be more. And the goal of our experiment is to find those other ones. All right. So if you accept that premise, which seems plausible, then you can compute what fraction of all the things that are picked up in each of these experiments are likely to be true positives.**

**So drum roll please. It turns out that the number's not that high. So the fraction of things in the consensus was 347 out of almost 2000. And if you do the math then, what you end up with is that the true fraction in this region, for which we have no data, is 1,123 out of-- and the false piece in this is going to be almost 15,000.**

**And they went ahead and did this for a number of different experiments and computed the fraction of derived false positives for these data-- might be a little bit hard to see on this screen. But the numbers range from 50% false positives to, in some cases, over 90% false positives. That's a little disturbing, right? So these technologies are good at picking up interactions, but there's reason to be very skeptical.**

**OK. So now we've got a serious problem, because how are we going to figure out which of these interactions to trust when we know that a very, very large fraction of**

17

**them are false positives? So what could you do? Well, you could take only the little bit of overlap. You could say, I have that Venn diagram-- method 1, method 2. They did agree on a bunch of things. So I could take only those.**

**That obviously throws away a lot. Someone else suggested we could throw away the sticky proteins, right? So maybe there are nonspecific proteins that don't show up in every experiment, but they show up in a very, very large fraction of all experiments. Maybe I toss those out. That's another possibility.**

**But what we really want to do is actually come up with a probability estimate. To not have to make a hard decision, but come up with an estimate of the probability that things interact based on all the data. So how do we go about doing that?**

**So first of all, what happens if you just require a consensus? So this plot shows accuracy and coverage of the gold standard for individual experiments with different thresholds for deciding what's interacting, different cutoffs and things. So the individual experiments are shown here.**

**And then if you acquire two methods to pick something up, or three methods to pick something up, you can get better and better in your accuracy. This is a log-log plot. So if you require three methods to agree before you call something a true positive, you can get up to-- I'm not sure exactly what this is, but 80%, 90% possibly. Right? But look at where you at the y-axis. You'd only get about less than 1% coverage of the gold standard. So that's not a great approach.**

**So what we really want to do, as I said, is to try to estimate the probability that proteins interact given all of our available data. And the data could be specific experiments. Say the two different mass spec experiments we just referred to. Or as we'll see a little bit later in this lecture and possibly the next one, other kinds of extraneous data that are not direct physical measurements of interaction, but might give us confidence that things interact based on similarity in annotation, or similarity in gene expression, and so on. And we'll get into details of that.**

**OK. So to do this, we need to have a little bit of a refresher on Bayesian statistics.**

18

**So I want to measure the probability that an interaction is true given the available data. Right? And I can estimate that based on the probability of observing the data for things that I know to be true and these prior estimates. So what's the prior probability that an interaction is true and the prior probability of observing a particular data set.**

**Now, this by itself isn't really that helpful. I haven't told you yet how to calculate any of the terms on the right. But bear with me. If I want to decide the likelihood that a protein interacts-- how likely is it? Is it more likely that it interacts or not? I can compute this ratio. The probability that the interaction is true given the data over the probability an interaction is false given the data. That's the likelihood ratio.**

**So by this formula, I then cancel out this probability of the data, the prior probability of the data. And if I had a way of calculating this, and we'll get to it in a second, then if it's more likely than not to be a true interaction, I can call it an interaction, right, if it's less likely. So if this ratio is greater than 1, I accept it as a true interaction. If this ratio is less than 1, then I reject it.**

**OK. So now our challenge is to figure out how to compute these terms. One more thing to note is if all I want to do is be able to rank every interaction by this likelihood ratio, rather than coming up with a hard threshold, then I actually don't need all these terms. So this is the likelihood ratio. I can convert it to a log space. So it's going to be the sum of these two terms.**

**And if I'm simply ranking everything by this log likelihood ratio, this term is the same for every interaction. It's just composed of prior probabilities. So it's not going to affect the ranking at all. Any questions on that? Is that clear? Good.**

**So if I just want to come up with a ranking function, all I need to do-- all-- I need to do is to be able to estimate the probability of observing data for true interactions and the probability of observing that set of data for false interactions. Everybody buy that? Yes, please.**

**AUDIENCE: When you say that prior probability is the same for all interactions, we're saying**

19

**we're assuming the same prior probability for all, or is this [INAUDIBLE]?**

**PROFESSOR: That's its definition. We mean, what is the prior probability that proteins interact versus the prior probability? So it's independent of the proteins that we're looking at. Other questions?**

**All right. So we need a way of computing this piece of all the things we've looked at before. So how do we get an estimate of the probability observing a particular configuration of the data? Meaning, I detect it in experiment 1 and not in experiment 2, but in experiment 3. What's the probability of that given it's a true interaction? So that's what we're going to dive into right now.**

**OK. So one thing we could do to make life simpler, and then we'll remove this simplification later, but let's, for the time being, assume that all of my data are independent. So the two-hybrid is going to have completely different mistakes than the affinity capture mass spec. So those two data sets are going to be completely independent of each other.**

**So I can write this as a product of a particular observation-- a particular mass spec experiment and a particular two-hybrid experiment for true attractions and false interactions. So it's the product of the probability that a particular experiment would detect an interaction if the interaction is true over the probability that that particular experiment would detect it if there was no interaction. I'm just going to multiply all of those probabilities. Yes.**

**AUDIENCE: [INAUDIBLE]. This is one interaction pair?**

**PROFESSOR: That's right.**

**AUDIENCE: And you take the product over all the interaction pairs within one run of the experiment. Is that correct?**

**PROFESSOR: If I want to determine whether a particular interaction pair-- I want to compute this log likelihood ratio, or this, actually, ranking ratio, because I've thrown away the priors. I want to compute this ranking ratio for a particular pair. So I've got protein A**

20

**and protein B. And I want to determine whether I believe it to be more likely to interact or not, and rank it with all the others, right? So I'm doing this for a pair of proteins now. So far so good?**

**Now, for that pair of proteins, I have a series of observations, or lack of observations, right? I have a whole bunch of experiments. This experiment detected it, that experiment didn't detect it, this one did. So what's the probability of these proteins-- these A and B really interact given that yes, no, yes in my experiments? And then for new protein, it might be no, no, yes, and what I want to figure out the probability for this pair.**

**AUDIENCE: So is the scale of the big letter M, is it on the order of like 10 experiments, 100 experiments, or thousands of experiments?**

**PROFESSOR: Ah. So the question is, what's the scale of this. So obviously, that's going to depend on what kind of data I bring in, but in these cases, it's small. So we have a handful of these high throughput experiments over entire genomes and proteomes. So there's not to be a lot. So in some of these early papers, there were four interaction experiments that they were looking at. Now the numbers might be a little bit bigger, but not significantly greater.**

**All right. So now to compute this, we need a set of gold standards. But now we don't just need gold standard positive interactions, proteins that we know really do interact. We also need proteins that we know really don't interact. Because I want to compute the probability of an observation given that some interaction is definitely wrong.**

**So precisely how I compute these terms is going to depend on the kinds of data. The experiments I've just been talking about, these high throughput mass spec, which were the ones which we looked at the ratio of the consensus, true positives, and estimated that 96% of all the data were possibly in error. The details of how to do those calculations are here. I leave you to look that up if you're interested.**

**But now what we're going to do is we're going to see how, if we were to rank**

21

**interactions based on this term, we can avoid having to throw out most of our data. So we said if we require all the experiments to agree, we're going to have very, very low coverage. Now we're instead going to rank everything based on this likelihood ratio, or something derived from the likelihood ratio.**

**So in this paper where they were simply looking at the protein-protein interaction data sets to compute these interactions, they ranked everything based on that ranking function we just described. And then as you vary your threshold, you can figure out how many true positives you have and how many false positives you have in the gold standard. True interactors and false interactors. And you can compute this curve, right? For any particular value of that ranking ratio, what's my sensitivity and what's my specificity? Are you clear what this plot means?**

**And here they've plotted the values for individual experiments. And this is the value for an independent database of gold standard interactions. And so now, where do they come up with their true positives and their false positives? A lot of this is going to depend on how representative those are. And all these numbers are subject to revision if you decide that the true positives and false positives that people are using are not accurate enough.**

**So they used two well annotated databases of interactions. One from MIPS and one from SGD. And you can play those off against each other as the database of true positives. In some ways, that's the easier thing because people like to report that proteins interact. They tend not to like to report the proteins don't interact. You don't see a lot of nature papers saying protein x doesn't interact with protein y.**

**So how are you going to figure out, then, what are your true negatives? So the strategies that they used-- well, one possibility is they're annotated to be in complexes, and those complexes are different from each other. That's not bad, right? But it's not a guarantee either.**

**Or this is a little bit better. They're annotated to be in different parts of the cell. Of course, if those annotations aren't perfect, low concentrations, you could still be wrong. Or that they have anti-correlated gene expression. I kind of like this one. So**

22

**it's one thing to be not correlated, but if you're anti-correlated, seems pretty suggestive that these two proteins are never in a complex together.**

**Again, it's no guarantee because, as we'll talk about in some detail later, RNA levels are not very good predictors of protein levels. But if you apply enough of these criteria, you can come up with a set of proteins that you have fairly high confidence really don't interact. You combine that with the databases of proteins with very high confidence that they do interact, and you can get the true positives and false positives that you need for this analysis.**

**all right. So that's a way of combining some information. We're going to see a generalization of that called Bayesian networks. We've mentioned this already in at least two different contexts, and it'll come up again later in the course as well.**

**So these are very general methods for reasoning probabilistically. We will see them in the context here of predicting interactions. We'll see them later in the context of gene regulation and signaling as well.**

**What we fundamentally need to do a Bayesian network is a graphical structure that represents our understanding what the relationship is between causes and effects. And a set of probabilities that allow us to compute things on this network. We'll show you examples where those networks are derived from our prior understanding of the problem, but also ones where the structure of the network is learned from the data.**

**And we're going to see two primary contexts. First we have this question of whether proteins interact. That's what we've just been talking about. So here are four experiments, the in vitro pulldown experiments and yeast two-hybrid experiments, that give us relatively independent information about whether proteins interact. And we're going to look at a paper that used those data with a Bayesian network to compute the probability that two proteins really do interact based on the combination of all the data, rather than throwing out anything that doesn't fall in the overlap, which could be a very, very small number.**

23

**And then later on we'll see examples of using Bayesian networks to understand biological networks. So this might be a set of transcription factors that are regulating a set of differentially expressed genes. And the structure of the graphical network for a Bayesian network has a lot of similarities to the way we normally think about transcriptional regulatory networks. So there's sort of a natural way of transferring our regulatory problem into a graphical network problem.**

**But we're going to focus on these prediction problems for protein-protein interactions first. Now, if I just want to compute the probability of detecting an interaction in various experiments, given that it's true or false, I could explicitly compute that probability. And we saw examples of that just now.**

**But some of these Bayesian network problems become much, much too large to do that. This is a little tiny piece of a Bayesian network that is supposed to represent I believe it's transcriptional regulatory network. You could never possibly write down all of the terms in this probability, where every node could, in principle depend on every other node in the network. It would just be a ridiculously large problem.**

**In fact, how large would it be if I've got N binary variables, my gene is on or off, my interaction is true or false, I have 2 to the N possible states? Right? And the only constraint I have, in principle, is that all the probabilities have to add up to one. So I have 2 to the N minus 1. 2 to the N minus 1 possible variables that I need to set. So that's a ridiculously large number in most contexts.**

**So how do Bayesian networks help us solve this problem? Well, we represent our understanding of the problem in a graphical structure where we have causes and effects. And there'll be a direct arrow from a cause to an effect. I don't always know the cause. So in our context, we were trying to figure out whether two proteins interact. What do we measure?**

**We actually don't measure interactions. We measure the result of a particular experiment, which is a combination of whether interacted and all sorts of noise that we've just discussed. So the effects that we observe are detected in experiment one or detected in experiment two. The cause is, did it interact or not? So the cause is**

24

**hidden, the effects are observed.**

**Now, in the case we were looking at before, we treated all these probabilities as being independent. But we might know something about the structure of our experiments, the kinds of experiments we're doing, that might lead us to have a different structure. So we could have an interaction that gives rise to all different kinds of data.**

**But depending on whether the protein's a membrane protein or highly expressed, it might influence the results of certain experiments and not influence the results of others, right? So like a two-hybrid would be very biased by which one of these? The membrane, right? And then the affinity capture mass spec could be very influenced by proteins that are expressed at very high levels or very low levels.**

**If we assume that all the interactions are independent, then we multiply probabilities. And we'll go into more detail, but this is what we're looking at up until now. In cases where we believe that all the observations are not independent, then we're not going to simply multiply things. We'll see there's a more precise way of computing the probabilities.**

**Now in this case, I've drawn the graphical structure because I believe that I know what's going on. But in the more general case that we'll look at, we'll actually derive the structure from the data.**

**One of the nice things about Bayesian networks is that it removes the need to have all 2 to the N minus 1 possible parameters, because it tells us there are certain independence conditions. So node is independent of its ancestors given its parents. What does that mean?**

**If I'm trying to reason about the expression of one of the genes down here, and I know that this transcription factor is on, I don't really care what the probability is that any particular parent of that transcription factor is on, right? So I don't need to know anything of transcription factor B1 if I know the state of B2. If this is on, then that's the only thing that's going to affect whether it's turning on these genes, regardless**

25

**of what the activation state of its parent was. Is that clear? Yes.**

**AUDIENCE: The slide's saying TF B1. [INAUDIBLE] TF B2? It says TF A1.**

**PROFESSOR: Yeah, sorry. That should say TF B1. Thank you. OK. So we'll do a little example. It's admission season both for graduate school and undergraduate. So let's do a little toy example where we're going to get rid of the admissions committees and just do automated admissions.**

**So we're going to collect various data about students, and then we're going to build a Bayesian network. And that network is going to decide whether to admit students into this simplified version. And the only information that will go into our decision will be the grades on the transcript and the GREs. Hopefully that's not the case.**

**And we believe that certain things influenced your grades and your GREs. Whether or not the student is smart certainly should have some influence, but also the great inflation at their school will have some influence.**

**So a prediction problem in a Bayesian network is going from the causes to the effects. So if I want to predict whether a student's admitted, I only need to look upstream. So we want to predict-- we observe the things on the top. Say, grades and GREs, and we want to predict whether this student should be admitted or not.**

**There's another problem called an inference problem, which is when we observe the effect and we want to make inferences about the causes. So an example of that would be, you apply for an internship and they say, oh, she's a student at MIT. I bet she's smart. Right? They're doing an inference problem.**

**We'll leave it for you to decide whether you and your colleagues are as smart as everyone thinks, but hopefully you are. OK. So we've got these two different kinds of problems. We've got prediction problems from top to bottom, and inference problems from bottom to top.**

**And we're going to talk about conditional probability. So if I've got some very small piece of this network with just two nodes, I could write out all the possible**

26

**probabilities for any pair of those nodes. So the probability that a student is not smart given that that student has low grades, the probability that the student is not smart given that the student has good grades, and so on, for all possible pairwise comparisons.**

**Or I could write this as a conditional probability, which tends to be an easier way to think about the problem. What's the conditional probability of a student being smart given that they've got good grades or given that they have bad grades? They have the same information. For this one, I need additional information about the total probability of students being smart or not.**

**And the total number of variables, as I said, in either case is the same. So these are completely interchangeable, but it's a lot easier to reason with conditional probabilities than with the joint probability tables. Those we'll see in a second.**

**So as I've said, you don't need a full probability table for a Bayesian network. You don't need two N to the minus 1 variables. And the fundamental reason for that is that the joint probability is only going to depend on the parents. So in this toy example, the GRE scores over here are not dependent on grade inflation.**

**Now, that all hopefully makes sense. Questions? Bayesian networks get a little murky next, so I'm going to try to give you into-- oh, yes. Question, please.**

**AUDIENCE: You said that the parents don't affect their children, but if grade inflation affects the grades, how does that influence-- will that influence the grade [INAUDIBLE]?**

**PROFESSOR: Sorry, can you say the question again?**

**AUDIENCE: I guess I'm just confused by this particular example. What do you mean by the joint probability? The joint probability of what?**

**PROFESSOR: So if I want to figure out the probability of some particular configuration of all the nodes in my network, I don't necessarily need to consider all possibilities. Because for example, if I want to consider all of the joint probability samples with settings for the GREs, whether the student had good GRE scores or not, that's not going be**

27

---

[← questions?](03-questions.md) · [Up: contents](index.md) · [influenced by the student's school's grade inflation policies. →](05-influenced-by-the-student-s-school-s-grade-inflation-policie.md)
