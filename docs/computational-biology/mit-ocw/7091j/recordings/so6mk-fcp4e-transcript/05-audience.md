---
title: AUDIENCE
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/so6mk-fcp4e-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# AUDIENCE

**Source:** `recordings/so6mk-fcp4e-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR:**

**My question is, how would you go about determining how many clusters your want?**

**Oh, OK. So we'll come to that in a second. So hierarchical clustering, you don't actually have any objective way of doing that. But we'll talk about other means right now, where it's a little bit clearer. But actually fundamentally, there aren't a lot of good ways of knowing a priori what the right number of clusters is. But we'll look at some measures in a second that help.**

**So hierarchical clustering, as your question implies, doesn't really tell you how many clusters there are. Another approach is to decide in advance how many clusters you expect. And then see whether you can get the data of the group into that number or not. And an example of that is something called k-means clustering. So the nice thing about it, is it does give you the sharp divisions. But again if you chose k incorrectly, we'll see in a second, you will get-- you'll never less still get K-clusters. So K refers the number of clusters that you tell the algorithm you expect to get.**

**So you specify that in advance. And then you try to find a set of clusters that minimizes the distance. So everybody's assigned to a particular cluster, and the center of that cluster. Is that clear? So that's what these equations represent. So the center of the cluster, the centroid, is just the average coordinates, over all the components of that cluster. And we're trying to find this set of clusters, C, that minimizes the sum of the square of the distances between each member of that cluster and the centroid. Any questions on how we're doing this? OK. All right.**

**So what's the actual algorithm? That's remarkably simple. I'm choosing that initial set of random positions. And then I have the simple loop, I repeat until convergence. For every point, I assign it to the nearest centroid.**

**So if my starting centroids would be circles, I look at every data point, and I ask, how close is it to any one of these? That's what the boundaries are, defined by these lines. So everything above this line belongs to the centroid. Everything over here belongs to this centroid. So I divide the data up by which centroid you are closest to. And I assign you to that centroid. That's step one.**

15

**And step two, I compute new centroids. And that's what these triangles represent. So after I did that partitioning, it turns out that most of the things that were assigned to the triangular cluster live over here. So the centroid moves from being here to here. And I iterate this process. That's the entire K-means clustering algorithm.**

**So here's an example where I generated data from three [? calcines. ?] I chose initial data points, which are the circles. I follow that protocol. Here's the first step. It computes new triangles. Second step, and then it converges. The distance stops changing.**

**Now this question's already come up. So what happens if you choose the wrong K? So I believe there are three clusters. And really that's not the case. So what's going to happen?**

**So in this data set, there really were. How many, there really were five clusters. Here, they're clustered correctly. What if I told the algorithm to do K-means clustering with a K of three? It would still find a way to come up with three clusters. So now it's grouped these two things, which are clearly generated from different [? calcines ?] scenes together. It's grouped these two, which were generated from different [? calcines ?] together, and so on.**

**All right. So K-means clustering will do what you tell it to do, regardless of whether that's the right answer or not. And if you tell it there are more clusters than you expect-- than really are there, then it'll start chopping up well-defined clusters into sub-clusters. So here it split this elongated one into two sub-clusters. It split this one arbitrarily into two. Just so it gets the final number that we asked for.**

**Then how do you know what to do? Well, as I said, you don't-- there's no guarantee to know. But one thing you can do is make this kind of plot, which shows for different values of K on the x-axis, the sum of the distances within the cluster. So the distance to the centroid within each cluster on the y-axis.**

**And as I increase the number of K's, when I'm correctly [? purchasing ?] my data, when there really are more subgroups than I've already defined, then I'll see big**

16

**drops. So I go from saying there are two to three in that case. I get a big drop in the distance between members of the cluster. Because I'm no longer including a data point over here. And in this cluster, with a data point in that cluster.**

**But once I go beyond the correct number, which was five, you see that the benefits really start to trail off. So there's an inflection point here. There's an elbow-sometimes it's called an elbow plot. After I go past the right number, I get less and less benefit from each additional clustering. So this gives us an empirical way of choosing approximately a correct value for K. Any questions on K-means? Yes?**

**AUDIENCE: Does K-means recapitulate the clusters that you would get if you cut off your dendogram from hierarchical clustering at a certain level?**

**PROFESSOR: Not necessarily. AUDIENCE: OK. But maybe. I don't know. It sort of seems to me as if you picked a level where you have a certain number of clusters, that that's similar, at least by centroid, by using the center?**

**PROFESSOR: Yeah, I think because of the way that you do it, you're not even guaranteed to have a level, where you have exactly the right-- other questions? Yes? AUDIENCE: Could you just very quickly go over how you initialized where the starting points are, and the break ups? PROFESSOR: All right, so the question is how do you initialize the starting points? In fact, you have to make some arbitrary decisions about how the initialize the starting points. So they're usually chose in a random. And you will get different results, depending on how you do that. So that's another-- so when you do it, it's non-deterministic in that sense. And you often want to initialize multiple times. And make sure you get similar results. Very good question. And in fact, that was not a set up. But what happens if you choose pathologically bad initial conditions?**

**So you have the potential to converge to the right answer. But you're not guaranteed to converge to the right answer. So here's an example where I had-- I**

17

**guess there really are three clusters in the data. I chose [INAUDIBLE] three, but I stuck all my initial coordinates down in the lower right-hand corner. And then when I do the clustering, if things go well, I get the right answer. But we're not guaranteed.**

**But one thing we are guaranteed, is we always get convergence. So the algorithm will converge. Because at each step, it's either reducing the objective function, or it's leaving it the same. So we're guaranteed convergence. But it may be as we've seen previously in other settings, we may end up with local minimum, rather than the global optimum. And the way to fix that then would be to initialize again, with new starting positions. Other questions?**

**What about a setting like this? Where we've got two well-defined clusters, and somebody who lives straight in the middle. So what's the algorithm going to do? Well, sometimes it'll put it in one side, of one cluster. And sometimes it'll end up in the other side. So an alternative to K-means clustering, which has to make one or the other arbitrary decision, is something that's called fuzzy K-means, which can put something actually literally, membership into both clusters. And it's very similar in structure to the K-means, with one important difference, which is a membership variable, that tells you for every data point, how much it belongs to the cluster one, cluster two, cluster three, and so on.**

**So in both algorithms, we start off by choosing initial points as a cluster means, and looping through each of them. Now previously, we would make a hard assignment of each data point x sub i to a single cluster. And here we're going to calculate the probability that each data point belongs to a cluster. And that's where you get the fuzziness, because you could have a non unit, or a nonzero probability, belonging to any of the clusters. And now we're going, K-means, we recalculated the mean value, by just looking at the average of everybody in that cluster.**

**Now in fuzzy K-means, we don't have everybody in the cluster. Because everybody belongs partially to the cluster. So we're going to take a weighted average. So here are the details of how you do that. In K-means, we are minimizing this function. We were trying to decide the class structure, the class memberships, that would**

18

**minimize the distance of every member of that cluster, to the defined centroid of that cluster. Here it looks almost the same. Except we now have this new variable, mu, which is the membership. It's the membership of point j, in cluster i. So I'm trying to minimize a very similar function. But now if mu is one-- if all my mus are one, then what do I get? K-means, right? But as soon as the mus are allowed to vary from one, they can be between zero and one, then points can contribute more or less. So that point there was stuck in the middle of the two clusters, if it had a mu of 0.5 for each, it would contribute half to each. And then both the centroids would move a little bit towards the middle.**

**So what's the result of K-means-- I'm sorry, fuzzy K-means clustering? We still get K clusters. But now every gene or every object that we're clustering has a partial membership. So here's an example of that, where they did K-means clustering, with these six different clusters. But now every profile, every gene, has a color associated with it, that represents this mu value. Whether it goes from zero to one, with these rainbow colors, to the things that are reddish, or pink-- those are the high confidence things that are very strongly, only in that cluster. Whereas the things that are more towards the yellow end of the spectrum are partially in this cluster and partially in other clusters. Questions? Any questions?**

**So K-means, we've defined in terms of Euclidean distance. And that has clear advantages, in terms of computing things very easily. But it has some disadvantages as well. So one of the disadvantages is because we're using the squared distance, then outliers have a very big effect. Because I'm squaring the difference between vectors. That may not be the worst thing. But they also restrict us to things for which we can compute a centroid. We have to have data that are-four or more, you can actually compute the mean value of all members of the cluster.**

**Sometimes you want to cluster things that we only have qualitative data. Where instead of having a distance measure, we have similarity. This doesn't come up quite as often in-- well, it certainly doesn't come up in gene expression data or [? RNAC. ?] But you can imagine more qualitative data, where you ask people about**

19

**similarity between different things or behavioral features, where you know the similarity between two objects. But you have no way of calculating the average object.**

**One setting that you might [INAUDIBLE] have looked at-- if you're trying to cluster say, sequence motifs that you've computed with the EM algorithm. So what's the average sequence motif? That doesn't necessarily represent any true object, right? You might be better off-- you can calculate it. But it doesn't mean anything. You might be better off calculating using rather than the average motif, the most central of the motifs that you actually observed. So that would be called a medoid, or an exemplar. It's a member of your cluster that's closest to the middle, even if it it's not smack dab in the middle.**

**So instead of K-means, we can just think, well, K-medoids. So in K-means, we actually computed a centroid. And in medoids, we'll choose the existing data point that's most central. So what does that mean?**

**If these are my data, the true mean is somewhere over here. But this one is the medoid. It's an exemplar that's close to the central point. But if there actually isn't anything here, then there isn't. So we're going to use the thing that's closest. So if these were all sequence motifs, rather than using some sequence motif that doesn't exist as the center of your cluster, you would use a sequence motif that actually does exist, and it's close to the center.**

**So it's a simple variation on the K-means. Instead choosing K points in arbitrary space as our starting positions, we're going to choose K examples from the data as our starting medoids. And then we're going to place each point in the cluster that has the closest medoid, rather than median. And then when we do the update step, instead of choosing the average position to represent the cluster, we'll choose the medoid. The exemplar that's closest to the middle. Any questions on this? Yes?**

**AUDIENCE:**

**So if you use the medoid, do you lose the guaranteed convergence? Because I can picture a situation where you're sort of oscillating because now you have a discrete stack.**

20

**PROFESSOR:**

**That's a good question. That's probably right. Actually, I should think about that. I"m not sure. Yeah, that's probably right. Other questions? OK.**

**There are a lot of other techniques for clustering. Your textbook talks about self organizing maps, which were popular at one point quite a lot. And there's also a nice technique called affinity propagation, which is a little bit outside the scope of this course, but has proved quite useful for clustering.**

**OK. So why bother to do all this clustering? Our goal is to try to find some biological information, not just to find groups of genes. So what can you do with these things? Well, one thing that was identified early on, is if I could find sets of genes that behave similarly, maybe those could be used in a predictive way, to predict outcomes for patients, or some biological function.**

**So we're going to look at that first. So one of the early papers in this field did clustering of microarrays for patients who had B-cell lymphoma. The patients had different kinds of B-cell lymphomas. And so they took their data, they clustered it. Again, each row represents a gene. And each column represents a patient here.**

**And with this projector, it's a little bit hard to see. But when you look at the notes separately, you'll be able see that in the dendogram, there's a nice, sharp division between two large groups of patients. And it turns out that when you look at the pathologist's annotations for these patients, which was completely independent of the gene expression data, all of patients in the left hand group-- almost all the patients in the left hand group, had one kind of lymphoma. And all the patients in the right hand group had a different kind of lymphoma.**

**And this got people very excited. Because it suggested that the pure molecular features might be at least as good as pathological studies. So maybe you could completely automate the identification of different tumor types.**

**Now the next thing that got people even more excited, was the idea that maybe you could actually use these patterns not just to recapitulate what a pathologist would find, but go beyond it, and actually make predictions from the patients. So in these**

21

**plots-- I don't know if we've seen these before yet in the class. But on the x-axis is survival. In the y-axis are the fraction of patients in a particular group, who survived that long. So as the patient's die, obviously the curve is dropping down. Each one of these drops represents the death of a patient, or the loss of the patient to the study for other reasons.**

**And so in the middle, let's start with this one. This is what the clinicians would have decided. There are here, patients that they defined by clinical standards as being likely to do well, versus patients whom they defined by clinical standards, as likely to do poorly. And you could see there is a big difference in the plots for the low clinical risk patients at the top, and the high clinical risk patients at the bottom. On the left hand side, or what you get when you use purely gene expression data to cluster the patients into groups that you turn out to be high risk or low risk. And you can see that it's a little bit more statistically significant for the clinical risk. But it's pretty good over here, too.**

**Now the really impressive thing is, what if you take the patients that the clinicians define as low clinical risk? And then you look at their gene expression data. Could you separate out the patients in that allegedly low clinical risk who are actually at high risk? And maybe then they would be diverted to have more aggressive therapy than patients who really and truly are low risk patients. And what they will show with just barely statistical significance, is that even among the clinically defined low risk patients, there is-- based on these gene signatures-- the ability to distinguish patients who are going to do better, and patients who are going to do worse.**

**So this was over a decade ago. And it really set off a frenzy of people looking for gene signatures for all sorts of things, that might be highly predictive. Now the fact that something is correlated, doesn't of course prove any causality. So one of the questions is, if I find a gene signature that is predictive of an outcome in one of the studies, can I use it then to go backwards, and actually define a therapy? In the ideal setting, I would have these gene signatures. I'd discover that they are clinically associated with outcome. I could dig in and discover what makes the patients to do worse, worse. And go and treat that. So is that the case or not? So let me show you**

22

**some data from a breast cancer data set.**

**Here's a breast cancer data set. Again the same kind of plot, where we've got the survival statistic on the y-axis, the number of years on the x-axis. And based on a gene signature, this group has defined a group that does better, and a group that does worse, the p value is significant. And it has a ratio, the death rate versus control is approximately two. OK. So does this lead us to any mechanistic insight into breast cancer. Well, it turns out in this case, the gene signature was defined based on postprandial laughter. So after dinner humor.**

**Here's a gene set that defined something that has absolutely nothing to do with breast cancer, and it's predicting the outcome of breast cancer patients. Which leads to somewhat more of a joke that the testing whether laughter really is the best medicine. OK. So they went on-- they tried other genes sets. Here's the data set-gene set that's not even defined in humans. It's the homologs of genes that are associated with social defeat in mice. And once again, you get a statistically significant p-value, and good hazard ratios.**

**So what's going on? Well, these are not from a study that's actually trying to predict an outcome in breast cancer. It's a study that shows that most gene expression-most randomly selected sets of genes in the genome will give an outcome that's correlated-- a result that's correlated with a patient outcome in breast cancer. Yes?**

**AUDIENCE: I'm a little confused. In the previous graph, could you just explain what is the black and what is the red? Is that individuals or groups?**

**PROFESSOR: So the black are people that have the genes set signature, who have high levels of the genes that are defined in this gene set. And the red are ones have low, or the other way around. But it's defining all patients into two groups, based on whether they have a particular level of expression in this gene set, and then following those patients over time. Do they do better or worse? And similarly for all these plots.**

**And he had another one which is a little less amusing, location of skin fibroblasts. The real critical point is this. Here, they compared the probability based on**

23

**expectation an that all genes are independent of each other, the probability that that gene signatures correlated with outcome, for genes there were chosen at random or genes that were chosen from a database of gene signatures, that people have identified as being associated with pathways. And you get a very, very large fraction. So this is the p-value. So negative log of p-value, so negative values are more significant. A huge fraction of all genes sets that you pull at random from the genome, or that you pull from a compendium of known pathways, are going to be associated with outcome, in this breast cancer data set.**

**So it's not just well annotated cancer pathways, that are associated. Its gene sets associated as we've seen, with laughter or social defeat in mice, and so on-- all sorts of crazy things, that have no mechanistic link to breast cancer. Let's take a second for that to sink in. I pull genes at random from the genome. I define patients based on whether they have high levels of expression of a random set of genes, or low levels of expression of that random set of genes. And I'm extremely likely to be able to predict the outcome in breast cancer. So that should be rather disturbing, right?**

**So it turns out-- before we get to the answer then-- so this is not unique to breast cancer. They went through a whole bunch of data sets in the literature. Each row is a different previously published study, where someone had claimed to identify a signature for a particular kind of disease or outcome. And they took their random gene sets and asked how well the random genes sets did in predicting the outcome in these patients? And so these yellow plots represent the probability distribution for the random gene sets-- again on this projector, it's hard to see-- but there's a highlight in the left hand side at where the 5%, the best 5% of the random gene sets are. This blue line is the near measure of statistical significance. It turns out that a few of these studies didn't even reach a normal level of statistical significance, let alone comparing to random gene sets. But for most of these, you don't do better than a good fraction of the randomly selected gene sets.**

**So how could this be? So it turns out there is an answer to why this happens. And it's really quite fascinating. So here, we're using the hazard ratio, which is the death**

24

**rate for the patients who have the signature, over the control group. So high hazard ratio means it's a very, very dissociative outcome. And they've plotted that against the correlation of the genes in the gene signature, with the expression of a gene called PCNA, Proliferating Cell Nuclear Antigen**

**And it turns out a very, very large fraction of the genome is coexpressed. So genes are not expressed like random, completely independent random variables. There are lots of genes that show very similar expression levels, across all the data sets. Now PCNA is a gene that's been known by pathologists for a long time, as having higher levels than most digressive tumors. So a very, very large fraction of the genome is coexpressed with PCNA. Then high levels of randomly selected genes are going to be a very good predictor of tumor outcome. Because high levels of randomly expressed genes also means a very high probability of having a high level PCNA, which is a tumor marker.**

**So we have to proceed with a lot of caution. We can find things that are highly correlated with outcome, that could have good value in terms of prognostic indicators. But there are going to be a lot of possibilities for sets of genes that have that property, they're good predictors of outcome. And many of them will have absolutely nothing to causally, with the process of the disease. So at the very least, it means don't start a drug company over every set of genes, if you identify this as associated with outcome. But the worst case scenario, it also means that those predictions will break down under settings that we haven't yet examined. And so that's the real fear, that you have a gene set signature that you think has a highly predictive outcome. It's only because you looked at a particular set of patients. But you look at a different set of patients, and that correlation will break down.**

**So this is an area of research that's still quite in flux, in terms of how much utility there will be in identifying genes set signatures, in this completely objective way. And what we'll see in the course of this lecture and the next one, is it's probably going to be much more useful to incorporate other kinds of information that will constrain us to be more mechanistic. Any questions?**

25

**All right. So now we're going to really get into the meat of the identification of gene modules. And we're going to try to see how much we can learn about regulatory structure from the gene expression data. So we're going to move up from just the pure expression data-- say these genes at the bottom, to try to figure out what set of transcription factors we're driving, and maybe what signaling pathways lived upstream in those transcription factors, and turn them on. And the fundamental difference then between clustering-- which is what we've been looking in until now, and these modules, as people like to call them-- is that you can have a whole bunch of genes, and we've just seen that, that are correlated with each other, without being causally linked to each other. So we like to figure out which ones are actually functionally related, and not just statistically related.**

**And the paper that's going to serve as our organizing principle in the rest of this lecture, maybe bleeding into the next lecture, is this paper, recently published that's called The DREAM5 Challenge. And this, like some of these other challenges that we've seen before, is the case where the organizers have data sets, where are they know the answer to what the regulatory structure is. They send out the data. People try to make the best predictions they can. And then they unseal the data, to let people know how well they did. And so you can get a relatively objective view of how well different kinds of approaches work.**

**So this is the overall structure of this challenge. They had four different kinds of data. Three are real data sets from different organisms, E. coli, yeast, and Staphylococcus aureus. And then the fourth one, the one at the top here, is completely synthetic data that they generated it. And you get a sense of the scale of the data sets. So how many genes are involved, how many potential regulators. In some cases, they've given you specific information on knockouts, antibiotics, toxins, that are perturbing. And again here, the number of conditions that are being looked at, the number of arrays.**

**So then they provide this data in a way that's very hard for the groups that are analyzing to trace it back to particular genes. Because you don't want people to use external data necessarily, to make their predictions. So every makes their**

26

**predictions. They also, as part of this challenge, they actually they made their own metapredictions, based on the individual predictions by different groups. And we'll take a look at that in a second. And then they score how well they did.**

**Now we'll get into the details of the scoring a little bit later. But what they found at the highest levels, that different kinds of methods behaved similarly. So the main groups that they found were these regression-based techniques. We'll talk about those in a second. Bayesian networks, which we've already discussed in a different context. A hodgepodge of different kinds of things. And then mutual information and correlation. So we're going to look in each of these main categories of prediction methods.**

**So we're going to start with the Bayesian networks, which we just finished talking about in a completely different context. Here, instead of trying to predict whether interaction is true, based on the experimental data, we're going to try to predict whether a particular protein is involved in regulating a set of genes, based on the expression data. So in this context-- let's say I have cancer data sets, and I wanted to decide whether p53 is activated in those tumors, So this is a known pathway for p53. So if I told you the pathway, how might you figure out if p53 is active from gene expression data?**

**I tell you this pathway, give you this expression data-- what's kind of a simple thing that you could do right away, to decide whether you think p53 is active or not? p53 is a transcriptional activator, but it should be turning on the genes of its targets when its on. So what's an obvious thing to do?**

**AUDIENCE: Check the expression levels from the targets.**

**PROFESSOR: Thank you. Right, so we could check the expression levels. The targets compute some simple statistics, right? OK. Well, that could work. But of course there could be other transcriptional regulators that regulate a similar set of genes. So that's not a guarantee that p53 is on. It might be some other transcriptional regulator.**

**We could look for the pathways that activate p53. We could ask whether those**

27

**genes are on. So we've got in this pathway, a bunch of kinases, an ATM, CHK1, and so on, that activate p53. Now if we had proteomic data, we could actually look whether those proteins are phosphorylated.**

**But we have much, much less proteomic data. And most of these settings only have gene expression data. But you look at, is that gene expressed? Has the expression of one of these activating proteins gone up? And you can try to make an inference then. From whether there's more of these activating proteins, then maybe p53 is active. And therefore it's turning on it's targets. That's one step removed. So just the fact that there's a lot of ATM mRNA around doesn't mean that there's a lot of the ATM protein, which certainly doesn't mean that the ATM is phosphorylated and turning on its target. So again, we don't have a guarantee there.**

**We could look more specifically whether the genes are differentially expressed. So the fact that they're on may not be as informative as if they were uniquely on in this tumor, and not on in control cells from the same patient. So that can be informative. But again changes in gene expression are not uniquely related to changes in protein level. So we're going to have to behave with a bit of caution.**

**So the first step we're going to take in this direction, is try to build a Bayesian network. That's going to give us a way to reason probabilistically over all of these kinds of data, which by themselves are not great guarantees that we're getting the right answer. Just like in the protein prediction interaction problem, where individually coexpression wasn't all that great, essentiality wasn't all that great. But taken together, they could be quite helpful. So we want to compute the probability that the p53 pathway is active, given the data. And the only data we're going to have in the setting is gene expression data. So we're going to assume that for the targets of a transcription factor to be active, the transcription factor itself has to be expressed at a higher level. That's a restriction of analyzing these kinds of data that's very commonly used.**

**So we're going to try to compute the probability that p53 is activated, given the data. So how would I compute the probability, that given that some transcription factors**

28

**on, that I see expression from target genes? How would I do this? I would just go into the data, and just count in the same way that we did in our previous setting. We could just look over all the experiments and tabulate whether one of the targets is up in expression, how often is the transcription factor that's potentially activating it up? And how often are all the possible combinations the case? And then we can use Bayesian statistics to try to compute the probability that a transcription factor is up, activated, given that I've seen the gene expression data. Is that clear? Good.**

**So we want to try to not include just the down stream factors. Because that leads possibly, maybe there are multiple transcription factors that are equally likely to be driving expressions instead of genes. We want to include the upstream regulators as well.**

**And so here, we're going to take advantage of one of the properties of Bayesian nets at where we looked at, explaining a way. And you'll remember this example, where we decided that if see that the grass is wet, and I know that it's raining, then I can consider less likely that the sprinklers were on. Even though there's no causal relationship between them. So if I see that a set of targets of transcription factor A are on, and I have evidence that the pathway upstream of A is on, that reduces my inferred probability that the transcription factor B is responsible. So that's of the nice things about Bayesian networks that gives us a way of reasoning automatically, over all the data, and not just the down stream targets.**

**And the Bayesian networks can have multiple layers. So we can have one transcription factor turning another one, turns on other one, turns on another one. Again, we can have as many layers as necessary. But one thing we can't have are cycles. So we can't have a transcription factor that's at the bottom of this, going back and activating things that are at the top. And that's a fundamental limitation of Bayesian networks. We've already talked about the fact that in Bayesian networks, with these two problems that we to have to solve, we have to be able to define the structure. If we don't know any a priori. Here, we don't know what a priori. So we're going to have to learn the structure of the network. And then with the structure of the network, we're going to have to learn all the probabilities. So the conditional**

29

**probability tables that relate to each variable to every other one.**

**And then just two more small points about it. So if I just give you expression data, without any interventions-- just the observations, then I can't decide what is a cause and what is an effect. So here this was done in the context of proteomics, but the same is true for gene expression data.**

**If I have two variables, x and y, that are highly correlated, it could be that x activates y. It could be that y activates x. But if I perturb the system, and I block the activity of one of these two genes or proteins, then I can start to tell the difference. In this case, if you inhibit x, you don't see any activation of y. That's the yellow, all down here. But if you inhibit y, you see the full range of activity of x.**

**So that implies that x is the activator of y. And so in these settings, if you want to learn a Bayesian network from data, you need more than just a compendium of gene expression data. If you want to get the directions correct, you need perturbations where someone has actually inhibited particular genes or proteins.**

**Now, in a lot of these Bayesian networks, we're not going to try to include every possible gene and every possible protein. Either because we don't have measurements of it, or because we need a compact network. So there will often be cases where the true regulator in some causal chain, is missing from our data.**

**So imagine this is the true causal chain-- x activates y, which then activates z and w. But either because we don't have the data on y, or because we left it out to make our models more compact, it's not in the model. We can still pick up the relationships between x and z, and x and w. But the data will be much noisier. Because we're missing that information. In the conditional probability tables, relating x to y, and then y because it's too targets.**

**So Bayesian networks, we've already seen quite a lot. We now have some idea of how to transfer them from one domain to the domain of gene expression data. The next approach we want to look at is a regression-based approach.**

**So the regression-based approaches are founded on a simple idea, which is that**

30

**the expression gene is going to be some function of the expression levels of the regulator. We're going to actually try to come up with a formula that relates the activity levels of the transcription factors, and the activity level of the target. In this cartoon, I've got a gene that's on under one condition, that's off under some other conditions. What transforms it from being off to on, is the introduction of more of these transcription factors, that are binding to the promoter.**

**So in general, I have some predicted level of expression for the gene. It's called the predicted level y. And it's some function, unspecified at this point, f of g, of all the expression levels of the transcription factors that regulate that gene. So just again, nomenclature is straight, x sub g is going to be the expression of gene x-- I'm sorry, expression of gene g. This capital X, sub t of g is the set of transcription factors, that I believe are regulating that gene. And then f is an arbitrary function. We're going to have a noise term as well. Because this is the observed gene expression, not some sort of platonic view of the true gene expression.**

**Now frequently, we'll have a specific function. So the simplest one you can imagine, which is a linear function. So the expression of any particular gene is going to be a linear function, a sum, of the expression of all of it's regulators, where each one has associated with it a coefficient beta. And that beta coefficient tells us how much particular a regulator influences that gene.**

**So say, p53 might have a very large value. Some other transcriptional regulator might have a small value, representing their relative influence. Now, I don't know the beta values in advance. So that's one of the things that I need to learn. So I want to be able to find a setting that tells me what the beta values are for every possible transcription factor. If the algorithm sets the beta value to zero, what does that tell me? If a beta value is zero here, what does that tell me about that transcriptional regulator? No influence, right. And the higher the value, then the greater the influence.**

**OK. So how do we discover these? So the tip of the approach then is to come up with some objective function that we're going to try to optimize. And an obvious**

31

**objective function is the difference between the observed expression value for each gene, and the expected one, based on that linear function. And we're going to choose a set of data parameters that minimize the difference between the observed and the expected, minimize the sum of the squares. So the residual sum of the squares error, between the predicted and the observed.**

**So this is a relatively standard regression problem, just in different setting. Now one of the problems with a standard regression problem, is that we'll typically get a lot of very small values of beta. So we won't get all zeros or all ones, meaning the algorithm is 100% certain that these are the drivers and these are not. We'll get a lot of small values for many, many transcription factors. And OK, that could represent the reality. But the bad thing is that those data values are going to be unstable. So small changes in the training data will give you big changes, in which transcription factors have which values. So that not a desirable setting. There's a whole field built up around trying to come up with better solutions. I've given you some references here. One of them is to a paper that did well in the DREAM challenge. The other one is to a very good textbook, Elements of Statistical Learning. And there are various techniques that allow you to try to limit the number of betas that are nonzero. And by doing that, you get more robust predictions. At a cost, right, because there could be a lot of transcription factors that really do have small influences. But we'll trade that off, by getting more accurate predictions from the ones that have the big influences. Are there any questions on regression?**

**So the last of the methods that we're examining-- this is a mutual information. We've already seen mutual information in the course. So information content is related to the probability of observing some variable in an alphabet. So in most languages, the probability of observing letters is quite variable. So Es are very common in the English language. Other letters are less common. As anyone who plays Hangman or watches Wheel of fortune knows. And we defined the entropy as the sum over all possible outcomes. The probability of observing some variable, and the information on to that variable, we can define the discrete case, or in the continuous case. And the critical thing is to have mutual information between two variables. So that's the difference between the entropy of those variables independently, and then the joint**

32

---

[← AUDIENCE](04-audience.md) · [Up: contents](index.md) · [entropy. →](06-entropy.md)
