---
title: DOUG
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/i59jdq9hk10-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DOUG

**Source:** `recordings/i59jdq9hk10-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**OK, good. And have you seen databases like that?**

**LAUFFENBURGER:**

**AUDIENCE: Several of them have come up.**

**DOUG OK. Are you the only one who's seen them? Or is there anybody else that kind of LAUFFENBURGER:noticed them in passing too? OK, good. Second, third, fourth, all right. That's a critical mass if I ever saw one.**

**OK. So, I'm just going to allude to those. So there are pathway databases. And this is actually an old slide of a few years ago, so I'm sure the numbers are all different. And, in fact, there's new ones. I just haven't taken to updating the slide.**

**But we'll, based on literature, take certain numbers of gene products, a few hundred of them, and organize them into pathways based on biological knowledge.**

**There's other databases that are more interactomes, usually based on other kinds of experimental data-- yeast II hybrid, mass spectrometry, literature curation, that also tries to say who's physically interacting.**

**So these node-- these pathway databases don't necessarily say, somebody's physically interacting, they say somebody might be upstream and downstream and so forth.**

**And then they interactome databases say, component a and component b, there's some evidence that they have a physical association someplace along the way.**

**So these are two complementary types of databases that, in fact, can be put together.**

**OK. So an interesting thing about these-- there's a number of these databases. And so in principle you could say, well if I want then to start-- if I want to generate a logic model for signaling networks, all I have to do is take what's in the database and say what pathways are there and what's known with their interactions, and now I've got a starting point. You know, I can actually draw a graph with lots of**

8

**molecular nodes and lots of molecular interactions.**

**So, you can do that. And so you can choose one of these databases and say I'm going to draw a graph that has what's believed to be true about nodes and pathways and interactions and signaling networks. But then you choose a different database and another database. And you'll actually get different information.**

**OK. We actually did a study on this-- I probably should have given you the citation of that-- that said if you look at six or seven of these databases, they are not coincident. They have a very small intersections. Most of their information is nonredundant.**

**And so you could try to put it all together. And we did this, again, in this paper that I'm not giving you a citation for. And so here's a number of nodes and signaling pathways downstream of receptors.**

**And all the colored nodes are those in which they appear in only one of these-one, two three, four, five, six databases. So if something's colored green, it's only in GeneGo and it's not in any of the others. If something's colored purple, it's in PANTHER and none of the others. OK.**

**If they're gray-- some of these gray ones, they're in at least two. But out of these six, there's an exceedingly small number of nodes interactions that are in all six databases. Which was a real surprise to us when we did this.**

**So what this means is, if you want to start with some prior knowledge graph that you're now going to fit a logic model to by mapping it against data, you first even have the choice, well, what am I going to start with?**

**What is my prior knowledge? There;s not really consensus prior knowledge. So you can start with six different interaction graphs. Or you could try to put them all together and get a consensus graph.**

**So you have all these choices. And right now, it's not as if is there's detailed analysis of what the best choice would be for your starting point.**

9

**But I want to stress that, with respect to our approach, this is a starting point because one of the issues with the database information is that it's typically very diverse with respect to contact.**

**What cell type did this information come from? What treatment conditions did it come from? If there's different cell types, different species, different mutations.**

**So if I see interactions or if I don't see interactions, are they in conflict? Or they're just-- this one was in a lymphocyte, this one was in a hypatocye, this one was in a cardiac myocyte, and they're actually different.**

**OK, so if I had a cell type specific database, or pulled that information out, that would be good. It would be a smaller number of things. But then under what treatment conditions?**

**Because remember I said starting with the genomic content, what you actually see in terms of molecular interactions will be very strongly affected by what matrix were the cells growing on? Or was this in vivo? Was this in a multicellular culture situation?**

**So, that's why this is a starting point and can't really be used to describe any particular experimental situation with much confidence.**

**The other thing-- and this is what I've been trying to emphasize from the start-- is that there's no calculation you can do on this. There's a group of folks in this field who propose some ideas that I think are very intriguing, but which, at least to me personally, there's not that much evidence for.**

**And that is, that there's topological characteristics of these graphs, that then tell you what's important. So if I have a node that's somehow connected to more other nodes, that is going to be a more important node, and might be associated with the disease, versus a node that's connected to fewer.**

**OK. Some of these are very, very appealing ideas conceptually. If you actually look for the experimental evidence that they're valid notions, it's very thin.**

10

**But, that's where some folks would claim, oh, you can do predictions on the hypotheses based on these graphs because there are these graph theory characteristics that somehow might be biologically meaningful. OK. But I'd say, jury's out on whether, in fact, any of that is true.**

**So, our view is-- OK, this is a good starting point, but in fact, needs to be mapped to empirical data in order to gain confidence about calculations you can do.**

**So that's the goal of this kind of approach, is to say, let's stipulate that we start with some prior knowledge scaffold. This particular one is from the Ingenuity database. You could get one from any other database.**

**You could get a consensus one from three or four if you want. And so it has, up here, extracellular stimuli, growth factors, cytokines. They're connected in their interactome II receptors. They're connected to scaffolding proteins and signaling proteins and kinases and so forth. They're connected to transcription factors, metabolic enzymes. So you can draw this graph. Say this might be what's going on in my cell.**

**And then what we'd like to do is to turn this into a formal logic framework that's capable of then fitting experimental data, predicting new experimental data, and giving you a chance at biological hypothesis and testing. All right, so conceptually you get it? Two aspects-- some kind of starting prior knowledge, that's kind of a scaffold, a graph, for your network. And now you're going to turn it into a computable logic model by mapping it against empirical data.**

**So, merely what it takes is the kind of conceptual diagram you see in any cell biology paper, any signaling paper, that says, well, a and b both influence e positively, and b influences f negatively, and c influences f positively. Then there's a feedback from g to a. That's inhibitory. You can draw those. But now, how do you turn it into a computable algorithm?**

**So, what I'm going to spend most of the day on is, just conversion of this to a Boolean logic model that any one of these interactions is and-- a and b being**

11

**active makes e active. c being active, but b not being active, allows f to be active, and so forth. You turn these into formal logic statements that you can compute on.**

**At the very end, if we have time, I'll show how to relax this from a Boolean framework that's just on off, to something that can be more quantitative.**

**All right. So that's the notion. Now what I'm going to do for the rest of the time is go through the specific example paper that says, OK, how do we in fact do this? What is a way to accomplish this?**

**So now let's go back to a biological problem where there's going to be empirical, experimental data that we're now going to map against one of these prior knowledge interactome graphs.**

**This particular study-- this was done with Peter Sorger, who's now at Harvard Medical School-- had to do with liver cells. Liver cancer-- you'll see some application of that at the end-- that says we have liver cell hepatocytes.**

**And we want to know how they respond to different growth factors, in cytokines in their environment. How that'll change their proliferation or death? Or the inflammatory cytokines that they produce. And we'd like to take-- this is just a pictorial diagram that could be in any cell biology paper, and make this calculable.**

**So we could say what's different from a primary normal hepatocyte liver cell that's not cancerous? It might have a signaling logic. But if then we compare the signaling logic to a liver tumor cell type, or four different liver tumor cell types, what's different?**

**If we can find some logic that's different for the tumor cell lines versus the normal primary lines-- some logic from here to there or to there-- that now tells you biologically, where the differences might be that have arisen from the genetic mutations.**

**And where good drug targets might be, or predictions if I intervene here, if there's no difference in that logic, between normal and tumor, well then that won't have**

12

**any effect. I want to look for the places where there is a difference in the signaling logic. And that would be a better drug target.**

**OK, so the measurements are made in across 17 of these different signaling molecules here, pretty much all by measurement of a phosphorylation state. So if you've done cell biology or biochemistry-- in these signaling pathways, many of the activities in these kinds of pathways that regulate this kind of cell behavior are kinases that end up affecting transcription factor activities and so forth.**

**And it's the phosphorylation state of any these proteins that matters. If a phosphate is on some particular amino acid, the enzyme might be active. If it's not there it might be inactive and so forth. So, just measurement of phosphorylation states of 17 different proteins in these pathways distributed across multiple pathways.**

**I've made these measurements on five different cell types, four tumor cell types, and the primaries in order to try to see what's different between primary and tumor. And then what might be different, patient to patient.**

**In response to seven different extracellular stimuli, some of them growth factors, some of them cytokines, some of them actually bacterial metabolic products. We all know about the effects of microbiome these days.**

**And, to further populate a database that might be capable of helping validate a model, a number of seven, in fact-- intercellular inhibitors. A small molecule, these things in black. One that might inhibit this kinase. One might inhibit that kinase. One might inhibit that kinase.**

**So now if you add all those inhibitors too, then you start to change the network activities and the downstream behavior. So that's how extensive the data is. And this is actually for a few different time points.**

**So the data looks something like this. Let's focus on the one on the left. This is just the primary, normal, human cells. It came from a liver donor. OK.**

**Each row is one of the 17 different signals, essentially measurement of the**

13

**phosphorylation state of Akt or CREB or P52 of staph 3. OK?**

**So measurements of its phosphorylation state that has something to do with its signaling activity. Each of the big columns are the seven different treatments-- the different growth factors and cytokines and so forth. And the control. No stimulation.**

**And within each one of these treatments, in each one of these stimuli, then there's seven different inhibitors that were used for the different pathways. So seven stimuli by seven inhibitors plus controls. And then three different time points. Sort of zero, 30 minutes, and three hours.**

**So the data looks something like this. If there's really no change, due to the stimulation or the inhibitor, you'll see something in gray. So in these gray bars, there was already phosphorylation of this transcription factor [INAUDIBLE] and it didn't really change under most treatments.**

**If it was yellow, what it meant was, whatever the treatment was, you got a quick activation of that signal and then it went away. If it's late-- purple, then it didn't happen in the first half hour, but it started to show up a few hours later. And if it's green it showed up in the first half hour and it stayed sustained. So that's what the color means. But this is the real experimental data.**

**And over here on the right is one of the tumor cell lines. And you can just see by inspection, it's different, right. The colors here are different from the colors there. All the same treatments, stimuli inhibitors. The colors are very different. You know, therefore that the signaling activities are very different. OK. Just by visual inspection.**

**OK. So what we're going to try to do is build a logic model for this. A logic model for this. Compare them and say, oh where are the key differences in how the signaling pathways are getting activated? Downstream of the same stimuli.**

**So, we start with our prior knowledge. This is from the Ingenuity database, which actually happened to be missing, even basic information about insulin signaling. So we just added our own information about what the insulin receptor does. It's kind of**

14

**hard to believe. This is a database that cost a lot of money and they didn't have really much information about insulin receptor signaling. Very strange.**

**So, downstream of our seven stimuli, down to the transcription factors of interest, there are about 82 molecular nodes and a hundred some edges that you'd pull out of the Ingenuity database. So here's our starting guess at what this looks like. There's no logic in here, but this is just, potentially, the things that the logic might operate on, downstream of stimuli, and when inhibited, and so forth.**

**All right. So here's the process. This was the actual algorithmic process that I'll walk you through. On the left-hand side is the computer part.**

**It said, OK, from the Ingenuity database, we had this prior knowledge about who was upstream, downstream, who affected whom. We strip this down some, because in terms of the measurements on the perturbations, there are some of the nodes that you just would not be able to see any measurable difference.**

**OK, there was no stimulus upstream, or no perturbation. And it was not measured so you really wouldn't be able to tell if it changed or not. So you just take those out.**

**Of everything remaining, now you don't know the logic. You know the potential. And so you say, well, of all the nodes and interactions remaining, I could have AND gates, I could have OR gates, you could have NOTS.**

**And you say, OK, in principle, I could have, then, many, many, many, many, many different logic models that could work. So how do I know which one? Well now you skip over to the other side and say, well, but we have all this experimental data. We have the data from all the different stimuli and all the different inhibitors for any given cell type.**

**And so, we have that data under all these different conditions. And what we're going to do is just run hundreds or thousands of these potentially appropriate models. Compare them to the data of whether any given node is activated or not, activated under treatment conditions, stimuli inhibitors. And we'll calculate the air. How good was any one of those models at actually matching those data? Simple**

15

**as that.**

**And then it's a matter of finding what are the best fit ones from the best fit ones. Could you improve them and make them fit even better? And in the end, how did you go from an initial prior knowledge scaffold to something that, in fact, fit the data really well, from which you could make new predictions. OK. So you get the approach here? All right, good.**

**Now, in terms of figuring out how well any given model matches the data and how to go through model selection, there's a myriad of different approaches to this. And I'm not claiming that what we did was the absolute best approach. There's alternatives to it that one could consider and then perhaps could work even better. If you read the paper, you'll read the reasons for these choices. OK. So I'll let you do that.**

**The way the model quality was calculated was to have an objective function that said we want to minimize some number, theta. And how do we calculate theta? Well, first of all, for whatever that model is, we're going to fit-- whether the model says some nodes should be on or off, one or zero. And we're going to compare it to the experimental data.**

**Now the experimental data, I need to emphasize, isn't one or zero, it's normalized to go between one and zero. But the actual measurement might be 0.7 or 0.25. OK, so you're going to have error against the Boolean model even if all the edges are absolutely correct you'll still going to get some quantitative error.**

**So you calculate that. The Boolean model says zero or one. The experimental data says 0.250, 0.7. And you say, OK, I'll calculate that. But then you might think, all right, well, somehow I've got to penalize bigger models with more nodes and more edges because surely the more nodes and edges I put in, I could capture more of the data. And I don't want to make the model infinitely large just to get the best fit. So I need to penalize that. Turns out it's not true, but nonetheless it's worth doing.**

**So, you take a parameter that's the size of the model. It's basically just the number**

16

**of nodes. The more nodes in it, the more you would be suspicious of the model for just fitting because it has too many components. And you multiply that size by a penalty parameter, alpha.**

**So you have a bad objective function if there's a lot of error with the data, or if your model's too big. A better model would be, better fit to the data and smaller. That's the calculation. OK.**

**And in the end-- and I'm going to show you how we did this. And I think the field is now really believing this. That what you're not after is a single best fit model. That one single model that gives you the very smallest data. Because honestly, within the uncertainty of the experimental data-- OK, there's a substantial number of models that could fit the data within that noise.**

**So if you demanded the single best one, you say, well, but these other 50 actually fit it almost as good and within the uncertainty of the data. How can you really reject them? And you can't.**

**So in the end, what's being striven for in most of the field is a family of models. And then you see what the consensus is and the differences within that family. The particular algorithm for generating and running through different potential models-because you just can't exhaustively sample all of them.**

**OK, these networks are so large, that you can't exhaustively test all possibilities of all their logic and so forth. It's really prohibitive.**

**So there's many different ways you can go about it. This particular method maybe you've already learned this in class for other applications as a genetic algorithm.**

**So you start with some population. You start with your Ingenuity scaffold and then you randomly remove or take edges and things like that. So that if you've got a whole family, that's slightly different.**

**For each one of them you evaluate the objective function against the data. And you get some of those that then are the most attractive. They seem to be the best fit.**

17

**But, by no means would you imagine they are yet optimal.**

**So, now you create a next generation from this population by the analog of genetics. Some of the very best-- you say, OK, they're going to survive so I'm just going to take them as is.**

**Some I'm going to mutate, I'm going to have a probability of mutating an edge here or there. You can have crossover, actually mating between one model and another model, so that the daughter model gets some of the arcs from the mother model and some of the arcs from the father model.**

**So you just generate an ex-population, do it again. And once you've reached a set of models that fit your data within the criteria that you want, then you say, this is now my population.**

**And these are now my best-fit models. So it's not exhaustive. You can definitely find local minimum here. There's no question about that. Yeah?**

**AUDIENCE: Do you always take the best model into the next round? Or do you--**

**DOUG Yeah, that's the elite survival. If you don't incorporate that, you might lose the best LAUFFENBURGER:ones in any given round. But this ensures you take the best subset. Let them go for it.**

**AUDIENCE: Is there a worry that you might get stuck in [INAUDIBLE]?**

**DOUG Yes. Yes, absolutely. So now you run this with a number of different starting LAUFFENBURGER:populations. And you see if you get to similar consensus models. Yeah, because absolutely, this does not guarantee any kind of a global minimum. You will always get local. So you have to condition it on a different set of initial populations.**

**OK. Once you do this-- I'm going to show you some results first and then dig into some other ways to think about it.**

**So it's plotted here. This is one of the tumor cell lines. What's plotted here, is again, all the rows or all the signals that were measured. All the big columns or all the**

18

**different stimuli, and all the little columns are the different inhibitors. And I should point out, this is only for the 30 minute data. OK. This isn't for the three hour or both, this is just the 30 minute data.**

**And basically where there's green, the model and data fit was considered OK. Where it's red, it's not OK. Where it's pink it's less bad. So by the shaded. And the yellow actually, the model really couldn't make a prediction.**

**Now, why that's the case is what's showing up here is just the initial Ingenuity scaffold. The very best one that didn't add or remove any arcs or nodes from the Ingenuity prior knowledge.**

**It's that all we're going to do is just run the best fit Boolean logic model we can on that. And it wasn't very good. It was about 45% error. Almost half of the nodes it got wrong.**

**So what that tells you if you just take a scaffold from one is interactive databases and without adulterating it, just fit the best logic model to some data-- OK, at least in this case, and we've done a number of others, it actually doesn't fit very well.**

**And the reasons being, you're trying to fit this now to a very specific biological context. Hepatocyte tumor cells under these grow factor and cytokine treatments. That network is likely very different from whatever aggregate you got from literature curation and so forth in a database.**

**There's going to be a lot of stuff in the database that's not applicable, because it came from a different cell type, a different condition, or there just wasn't enough experiments in the literature for hypatocytes.**

**Maybe it was never measured under treatment with interferon gamma. So there's data here that the database never had access to literature that it had explored. So lots of reasons.**

**Now when you go through the processes we just talked about, and in the end, the best fit models give you something like less than 10% error. So less than 10% of**

19

**these squares are red or pink.**

**OK, so that's the kind of improvement that you can take by generating an improved model. By adding and subtracting arcs and nodes.**

**So this is what the model looks like in the end for this tumor cell line. And this is a consensus model from the 20 or so best fit.**

**And so the thickness of a line is how strong the consensus was. The strongest would be all 20 had it. And the point here being, you see some purple.**

**And I wish my pen wasn't fading in and out. If anybody has a pointer I'll be happy to have it. Where you see purple, those were arcs that weren't in the Ingenuity database and had to be put in to get the data to fit this well.**

**And it turns out, if you actually go back to the literature, you find that those purple arcs were already described in the literature. It's just that they weren't captured in that database.**

**Well that's green and purple. Then you see some blue and they were in some of the other tumor cell types but now in this particular hep G2 But you can generate a model that works very well.**

**And see that it's consistent with much of literature. It's a more stripped down than what's in the databases. And there's some new things in it, that in fact, if you go back to the literature you can find, because they just were captured in the database.**

**All right. A few insights about the analysis. So I want to show you, here is the objective function. How well the model fit and that's in red. OK. And in blue is the actual fit to the experimental data. And again, the hirer it is the worse it is. And the green gives you essentially the size. And this is plotted against the size penalty.**

**And what's very interesting, is even for very small size penalties, almost negligible, that the size of the model that turns out to be best fit is substantially smaller than what was in the database.**

20

**OK, so you actually generate a small model immediately. A smaller model immediately, even without any size penalty. So your intuition that a bigger model was going to be better actually turns out to be incorrect. That even without a size penalty, the model strips down.**

**And why is that? Why is that? Let me make that question number two. Just to see who's still awake. Why, in fitting this hepatocyte data, would a model that leaves out a lot of stuff in the Ingenuity database that's presumably going on actually fit the data better? A smaller model fits better? Why is that? Yeah.**

**AUDIENCE:**

**This is a [INAUDIBLE]. Maybe the strength of the attractions aren't really taken into account here? And so the moving things out, essentially means that you're not sealing everything in the [INAUDIBLE]. You're just taking one.**

**DOUG**

**DOUG Yeah. That's essentially it. I think you've casted it an almost quantitative term, but I LAUFFENBURGER:think it's true even in qualitative terms. And one way to think about it is-- let's say I have an extra arc or extra node. OK.**

**I might capture some more true positives. I might actually capture more of my data, but I could actually now, gain more complex with my data. Because now I've put in logic that, yes, it captures this measurement, but now maybe it messes up these other two or three measurements.**

**So you actually can make your model worse trying to capture some small piece, that in fact, adversely influences the effects on the other measurements.**

**So you get you get false positives, false negatives, along with anything and that's true. And it just so happens that in these kind of situations those can outweigh.**

**Then of course, as you increase the size penalty you can drive your model to be even smaller, fewer arcs, and now that of course does come at the expense of not fitting the data better. OK.**

**So where we decided that the size penalty best lived was where it was large**

21

**enough to ensure stripping down of nonessential nodes and arcs, but not large enough to start compromising the actual experimental fit. OK. And so that lived someplace around there.**

**OK. An important thing-- and this goes back to the consensus model. If you think about, quote, model identification, can you uniquely specify one model a best fit model? You really can't. What's plotted here is for any of the arcs that would end up in a model.**

**Let's say we let's say we numbered them from one to I think it was 113 in the first place. One arc, another arc, another arc, another arc. And you say, how frequently did they end up in the best fit models?**

**Basically, only a small proportion of them were in all the best fit models. Some of them were in some models and some not.**

**Of course the higher the tolerance, the more air you allowed and now you started to get models that all fit to within whatever that criteria was in which most of their arcs weren't the same. You could have a lot of different network structures that give you that same fit. If you require a very, very tiny fit, compared to air, something like this, then more of the arcs in the models have to be in common. OK. So that makes some sense. But you can't really completely identify a unique model. That goes to what I said before.**

**OK. I was talking before about trade-offs between false positives and false negatives. You must know, I'm sure from previous things in this class, the receiver operating characteristic curves, where for every of your model parameter choices, you say, what are my results in terms of false positives versus true positives? And you're trying to find the optimal location along this type of path.**

**And so, what's shown here is that the best predictive model, in fact, is the one where we have the size penalty to be right on the edge of not making the experimental data fit worse, but still strips out the most arcs. So again, that demonstrates that the smaller model actually is in fact better, in terms of finding**

22

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [this type of-- →](03-this-type-of.md)
