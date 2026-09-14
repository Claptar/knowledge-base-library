---
title: this type of--
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/i59jdq9hk10-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# this type of--

**Source:** `recordings/i59jdq9hk10-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**And this shows if we actually put in some more arcs that tried to capture some more data, yes we decrease the false negatives, but, in fact, we increase the false positives. We actually shift ourselves on this curve. And so you decide whether that's desirable or not. Where you'd like to live. So you can analyze what you like about your best fit class of models in this kind of way.**

**OK, so now we have some confidence in this. What are you going to do with it? And one thing I'd like to do is just make a priori predictions. Say I now believe that on these hepatocytes or tumor cells stimulated with these kind of things, I can calculate what the experimental signaling activities should be.**

**All right. Let's see if we do that a priori. So let's now use new inhibitors that hadn't been used before. Combination of inhibitors, especially in cancer. People are always interested in combinatorial drugs. Experimentally it's prohibitive to run through all possible combinations. So this is one thing in the pharmaceutical field people believe these kind of models are really useful for. Let's try all possible drug combinations and see which ones are most promising.**

**And instead of just one ligand growth factor cytokine at a time, do different combinations. So this is all an entirely new data set. So different treatments that are different combinations, different inhibitors, different combinations of inhibitors.**

**And now you just run the model-- it's not trained on this. It was trained on the previous data. And now a priori predicts this data set. And now, again, you look for the model fit in the bottom. And again, you want the smallest number of red and pink boxes.**

**In effect it predicted to within about 11% error. About 11% of the boxes didn't fit well, but 89% percent did. And that's, in fact pretty close to the 9% that was on the original training model. So in terms of this, in this realm of studies, these a priori treatment conditions-- drug combinations, growth factors, cytokine combinations-this is a pretty good validation that this model wasn't just kind of trained and fit.**

23

**That it, in fact, could predict then what was happening in these pathways.**

**And then of course, what it allows you to do, where all the red boxes are-- it say, OK, that's where we need more intensive study. Now maybe we go back to the literature and say, is there more known about those nodes that was captured in whatever our interactive database that we started with?**

**Maybe we need to supplement the scaffold with more information. That's out in the literature where more and more dedicated experiments are done. So it narrows down where the next set of investigations need to be, whether from the literature or from yourself.**

**OK. So this is just then some biological results. If you do this for the four different hepatocellular lines. Some of the signaling activities are the same, and some are different. I think I'll skip that.**

**All right, let me show this. So this says, where are the similarities and differences between the normal hepatocytes versus the tumor lines. Because this is where you would want to get the ideas for where the right drugs would be. Where is the logic different, between a normal liver cell and one of these transformed types.**

**So, this is the same kind of scaffold. It'll get us the consensus models and the thickness of the line is how strong-- what proportion of the models did that arc show up in? Along the best. If it's black, the arc was in the primary hepatocytes and all the cell lines. So black is just sort of consensus core. This is just invariably there.**

**The blue was in the models for the primary hepatocytes, but for some reason didn't exist in the tumor cell lines. So we're signaling logic that normal hepatocytes use, that the tumor cell lines have somehow lost.**

**Red, are arcs that weren't in the primary cells, but showed up in the tumor cell lines. So was logic that the normal liver cells apparently didn't use, but now showed up in the tumor cell lines.**

**And why would there be these differences? Well this is where it goes back to then**

24

**the genetic mutations and variations. Because going from a primary to some tumor cell line, there's enough of the genetic mutations, that in this case said, OK, I've got some genetic mutation that interrupts the link between map three kinase and Ikk.**

**There was some docking protein or something that's now missing, not expressed as highly. It's got a mutation of amino acids and no longer docks right. It has a lower enzymatic activity.**

**So now you can go back and trace. Can I find some genetic mutation that has to do with the loss of that arc? Or if I've got a red arc that shows up-- like I said because there was something in my genetic mutations that now adds an activity here that wasn't there.**

**Maybe something is now constituently active. Maybe something is just expressed at a higher level. And all of a sudden that pathway comes into play. So that's the cool thing. You can trace what's actually in the genetic mutations if you have some methodology for that, to what's actually been altered in the network logic. Yeah?**

**AUDIENCE: Are the primary lines considered healthy lines? Or are they--**

**DOUG Yes. LAUFFENBURGER: AUDIENCE: OK, so the-DOUG Yeah. So they're from donors but they're mainly like motorcycle accident donors LAUFFENBURGER:that don't either liver anymore but the liver was fine. So, yeah, they're from healthy donors. AUDIENCE: [INAUDIBLE]. DOUG Yeah. Yeah. It was the lines at some point came from a tumor and have been LAUFFENBURGER:propagated in a culture, yeah.**

**OK. What do I want to-- got a little bit more time. Let me do this. OK.**

25

**So here's another interesting thing that can happen. If you take these models seriously, it can tell you something about the biochemistry, perhaps of what's going on.**

**So see there's this dashed line here that I want to emphasize and we'll emphasize it again on another slide. That was one that had to be added. It just wasn't in the Ingenuity pathway, scaffold. Actually couldn't find it in any literature anywhere. But nonetheless you needed it to fit some data.**

**So we kind of kept our eye on that one. What the heck is going on here? This dashed line from I kappa kinase up to step three. No evidence for that signaling linkage in the literature anywhere. What could that tell you?**

**All right. Well, you go back to the data now and you say, well what of the data set, of the experimental measurements that we made, caused that arc to have to be there to fit the data well? OK. You can now ask that kind of question.**

**Well remember I said in the data set were inhibitors. Some small molecule inhibitors against this kinase or that kinase or that kinase that would perturb the network and then give us relationships at the logic model and had to account for.**

**Well, this one had to be there, mainly to account for data that came from an inhibitor of Ikk. That one of the kinases that we had a small molecule inhibitor for, inhabited this kinase. And somehow there turned out to be an effect on staph 3 phosphorylation. And so you needed that arc to be there.**

**So either the explanation that either there's, in fact, some real mechanism going on here. It might have been transcriptional that somehow the activity of this kinase affects the levels of expression and the responsiveness of staph 3.**

**Or you say, ah, maybe it's a problem with the drug? It's a problem with the inhibitor. That, in fact, what you thought was an inhibitor that just affected this kinase, has an off-target target effect on that kind of that kinase. And it's just an artifact. That's an alternative explanation.**

26

**Right, so that's the sort of thing you can test. And we did test it. And here's the data here. At the bottom is the kinase that you wanted the inhibition 2. And in the blue was the inhibitor that was actually used in the study, both in vivo and en vitro and it inhibited that kinase.**

**But then we looked at the potential off target effect on that other-- the JAK2 [? stat ?] 3 and it also did have activity on that. So it meant that that inhibitor had an effect, not just on the Ikk, but also on the JAK [? stat ?] 3.**

**And so that's why that arc had to be there, is because, in fact, that inhibitor, inhibited this kinase as well. So if we took that into account in terms of the algorithm, then we wouldn't have to have that arc because it was spurious and came from the arc, in fact, of that inhibitor.**

**But the interesting thing is that, by taking the model seriously, we can actually find that. Because it was not previously known that this inhibitor had an off-target effect on that kinase.**

**In effect, the interesting thing, pharmacologically, was that this small molecule that was aimed to be an inhibitor against this kinase was the best by far in treating lung airway inflammation, compared against a whole other set of other types of inhibitors for the same kinase.**

**So now the reason might be is, it's better because it's also hitting this other kinase. That this off-target effect actually is therapeutically efficacious and in fact a combination of drugs against this kinase and the other kinase is what's required for the therapeutic benefit. So that's something that could be explored. And that's the sort of thing this model leads to.**

**OK. Let me end by digging into this difference a little bit. Because I said, you see these differences between primary hepatocytes and the tumor cell lines. And the model said, just from examining the data sets, that the logic is different. OK. Is there any validation for that?**

**Well, so let's go back and look at those differences with respect to literature. So if**

27

**you just blow up that part of the model, there's eight edges that are strongly disparate between the primary, normal cell types and the tumor cells and they're all enumerated here. One, two, three, four, five, six, seven, eight.**

**And they're essentially in three different pathways. So what the model is telling you is that there's three different pathways that are substantially different between a normal liver cell and a liver tumor cell. OK.**

**So is there any evidence that this is really true? So let's look at one. On to this pathway that I've got differences. And you see blue here and red here.**

**It says that this particular signaling node in normal cells is activated by this pathway. In the tumors, that regulation is lost and that actually comes through another pathway.**

**And it turns this is consistent with literature that, in fact, in the tumor cells, you get a higher activity of this downstream node. And now I've lost my light again. This HSP27.**

**Even though it's over expressed, you get less activation because this pathway is less strongly activated in red than the blue pathway is. So if you went by gene expression, you'd think in the tumor cells, this is a higher activated pathway.**

**Turns out the logic is different, and you actually get less activation of it because it's coming from a different pathway. So that turns out to be true in the liver tumor literature.**

**Another one-- I find this one really interesting. That in normal liver cells, to activate this Ikk pathway-- that's a very important kinase pathway, governing the transcription factor of NF Kappa b. In a primary cell, I need this combined logic between a pathway downstream of insulin receptor and a pathway downstream of a cytokine. Only if both of those pathways are on, do I now turn this on.**

**In the tumor cells, that check is lost. Only one pathway is required. OK. If this one is activated, I'm going to get this transcription factor activated. I don't have to wait**

28

**for simultaneous activation of this pathway. Where as a normal says I have to. OK. That turns out to be true that in the liver cells, the progression is associated with a looser regulation of this transcription factor.**

**And one more. I won't go into too much detail, but again, you see reds and blues here. In the tumor cell lines, you've now got activities downstream of insulin. That's normally just a survival factor, that's just not found in the primary cells.**

**And that, in fact, is shown in the literature too, that insulin signaling shifts from metabolism to proliferation. It's mainly metabolic, stimulus. In the normal cells it turns into a proliferative stimulus in the tumor cells.**

**OK. So, what this says is, just by mapping this logic scaffold, the scaffold against empirical data, developing a logic model, you in fact can find loci of differences between the normal cell signaling logic and tumor cells signalling logic for which there's evidence in the literature, none of which was in the original databases.**

**Finally, I'm going I'm just going to say that it turns out in another study, what you could show is those three pathways that the model predicts are the differences between the liver tumor cells and the normal cells.**

**That in order to kill these liver tumor cells, you need inhibitors against all three pathways simultaneously. You actually need combination drugs of three different pathway inhibitors to kill these cells. And it's exactly the three pathways that the model predicted of the differences between the normals and the tumor cells.**

**OK. All right, so I will end here and then see if there's any more questions. Something that comes up a lot is-- there's discomfort with Boolean logic because of zero, one. It's off, on, and of course we know biology, biochemistry doesn't work that way.**

**And so there can be so many artifacts, so many places that you can get things wrong, because you're trying to fit a model where the measurement is supposed to be either zero or one, and you're comparing it against a measurement that might**

29

**be 0.6.**

**Well, 0.6, is that closer to 1, is it closer to 0? Is there some normalization that would shift it from one to the other. And instead of being a correct fit, it's now an incorrect fit. So you can see the room for artifacts by mapping quantitative data against a qualitative model.**

**So, one thing done more recently is to admit that and say, well, let's say just relax this a bit. And instead of having step functions from off to on, that they're more graded. It's like an analog transfer function.**

**So what you've essentially done is add one more parameter to every node, to every gate. Because of Boolean logic, there's essentially one hidden parameter. That's where you shift from off to on, right? There's some location of the level of the signal that you've decided is 0 or 1. So there's some parameter that you shift from, saying it's off to on.**

**Well here now in this formalism there's that, but there's also then the slope of shifting from off to on. Is it still fairly steep? Is it really mild? Is it someplace in between? OK? And this can go with AND and OR gates too. Now, instead of just one dimension, one component being off to on or on to off, now you got AND and OR gates that have these slopes as well.**

**So what this means is you require more data to fit this-- we call it a constrained fuzzy logic model because you've got-- if I've got 50 nodes in my system, I've got 50 more parameters I've got to fit. OK, so that requires more data.**

**What's the benefit of it, is that your predictions now, in fact, can be quantitative. So you can go into the model and say here's a transcription factor CREB. I'm going to predict its phosphorylation state and its transcriptional activity, perhaps, based on the activities of two upstream kinases.**

**And so if I had had an inhibitor for one of these kinases or another, how much would I shift the phosphorylation of this transcription factor? And what you actually see is these gradual curves, that if I start to inhibit [INAUDIBLE], OK, it gradually**

30

**changes the phosphorylation of CREB.**

**Or if I inhibit the activity of P38, it even more gradually effects the activity of CREB. So you can turn these into quantitative predictions of strong effects, weak effects. And again, look at drug combinations.**

**So that's the advantage of going to this more analog transfer function logic model. You can deal with quantification much better, but at the cost of requiring more data.**

**OK, I think I'll leave it here. It's about 3:15 and so if there's more questions we can take them about any aspect of this. Most of you have stayed awake, I think that's a good thing. OK. More questions?**

---

[← DOUG](02-doug.md) · [Up: contents](index.md) · [AUDIENCE →](04-audience.md)
