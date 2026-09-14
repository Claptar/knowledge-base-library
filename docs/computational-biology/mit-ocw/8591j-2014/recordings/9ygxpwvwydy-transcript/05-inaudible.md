---
title: '[INAUDIBLE]?'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/recordings/9ygxpwvwydy-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [INAUDIBLE]?

**Source:** `recordings/9ygxpwvwydy-transcript.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**PROFESSOR: OK, so actually, one of these curves-- so the triangle, the sort of teal triangle, it is indeed higher up. And it's kind of here. So they do have a data point that is further beyond and is, again, above that curve. So that does provide somewhat further support for a non-linear model.**

**But again, there's a question of how strong that should be and so forth. And indeed, I'd say, for example, Terry Hwa has spent a lot of time characterizing growth rates as a function of many, many things.**

**And if you measure the relative growth rate as a function of a non-useful protein expression-- and what he finds is that this thing basically looks like a line in this axis.**

**And it saturates at around if you're at 30% maybe of total protein expression. So this is a lot. But this is kind of where the cell just can't handle that.**

**So Terry Hwa has recently been exploring a lot of these sort of phenomenological growth laws, where he imposes costs of various sorts and then looks at how the cell kind of responds.**

**And what he finds is just a remarkably large number of lines in various spaces that I find very surprising, but that he can understand using kind of some phenomenological modeling. But this is one of like a dozen lines that he sees of various axes doing things.**

**But the point here is that, as a function of the level of expression of these non-useful proteins, what he sees is that for a variety of different proteins-- including beta-gal but also beta-lactamase and other proteins that are not being used in that particular environment-- what he sees is that there's basically a linear cost growth, as you impose this non-useful protein expression.**

**So I'd say that this basic statement of it being not-- the statement of cost being super linear, I think, ends up not being true. Now, what does it mean for this paper? AUDIENCE: I mean, they still presented with same hypothesis and had these data to back up**

20

**some of it.**

**PROFESSOR: Yeah, right. So it's a very interesting hypothesis. They did nice evolution experiments, where they saw the population adapt to different levels. But what does it mean about the predictions, in particular, in the sense that if you measure cost and benefits, then you want to predict where it's going to evolve. What happens? If it's the case that cost as a function of expression is actually linear, then what does that mean for their ability to predict what's going to happen? AUDIENCE: Seems like if they use their same model for the benefit in this linear cost, that their predictions would be really off [INAUDIBLE]. PROFESSOR: Yeah, right. So the problem is that if you actually use a linear function here, then their model doesn't even predict that there should be an optimum, because their benefit function ends up also being essentially linear with the amount of this protein expressed. So if you have two lines-- so overall growth is something like goes as benefits minus costs. And maybe this is a relative growth. So if you have a line here and a line here, no optimum. So that's kind of a bummer. But it doesn't mean that that's-- in biology, eventually things are non-linear, so there should be some optimum. And actually, what I would say is that I think that the nonlinearity is probably actually here. That's the non-linearity that's relevant, maybe, is dominated on the benefit side rather than the cost side. My guess as to what's going on here is that rather than the costs growing super linearly with the expression level, rather the benefits will be sub-linear with the expression level. And why might that be? AUDIENCE: We're just seeing them apart, splitting up more lactose that's useful, just so it can't metabolize more of it.**

**PROFESSOR: Right, you know, at some point, it's just that the cell doesn't need more sugar. And**

21

**then it's not going to be as useful.**

**And even before you get to that regime, I think there are various ways in which cells may be able to use the sugar more or less efficiently, depending on how much they have it, which means that as-- and this is just like for us, the first slice of pizza is great. But then once you're at the fifth one, you start to feel a little bit full.**

**So in general benefits as a function of anything, should have some saturating behavior. And my sense is that this is basically why there's an optimum here.**

**Now, of course, I'd say that all these cost functions behave very similarly in here. So the predictions that they make in here are really not very sensitive to which of the cost functions they use. And those are all still then relevant and valid.**

**The question is just trying to predict what happens beyond the range that you have data is very hard, because it depends very much on what your curve does past that region.**

**So I guess I've made an argument that I think that maybe what's happening is that the benefit function here is non-linear. But what did they actually do to measure the benefits, because this is not I think totally obvious either?**

**So what should I be plotting? Well, this is still a relative growth rate. And here, this was actually lactose concentrations. So this is not lac expression, which is the most obvious thing that you would want to do, but that's harder.**

**And what they show is that their model is sort of consistent on this axis. This is external lactose. And the idea is that-- here is 0-- in the absence of any lactose, if you induce the lac operon, then you're at this minus 4 and 1/2% or whatnot.**

**So it kind of starts out down here. And then up here, it comes out up to above 0.1. So this is the first 4, maybe 4.5%. This is up here at 10%. And you end up with a curve that kind of goes from 4% or 5% deficit up to 10% or 11% advantage.**

**And this is at full induction of the lac operon. What this is saying is that if you're making the proteins to break down and consume lactose, then there's a cost. That's**

22

**just how they plotted it.**

**But that the benefits do indeed outweigh the costs at some concentration of lactose. But then here, there's a saturation. And here, the saturation in their model-- they get a saturation just because of the dynamics of import.**

**So what they assume is that there's a Michaelis-Menten kinetics for import. So the import rate kind of goes as the concentration of the lactose divided by some k plus the concentration again of lactose, so Michaelis-Menten dynamics.**

**But of course, if you have more of the protein lacY, then you'll be able to import more. So just because you have saturation as a function of lactose does not mean that you'll have saturation in terms of the number of proteins that you're making. Do you understand why I'm saying that?**

**And indeed, I would say that many underlying models could have been consistent with this data as well. So I'd say that their data does not reject the hypothesis that the benefit function is sublinear. Yeah.**

**AUDIENCE: So that you just said if you have more lacY and import more and it would saturate to an [INAUDIBLE]. So you could imagine that by evolution something happened there. So why would you even expect the prediction of this cost-benefit analysis? You see what I mean?**

**PROFESSOR: OK, so you're saying that evolution might be able to change other things as well to kind of fiddle-- yeah. I think this is an important question. I think the basic answer is that there are some things that are easier for evolution to do than others. And also that somethings have maybe already been optimized.**

**Now, relevant to this point, so they did these laboratory evolution experiments, and there was one category of mutation that they did not see. Does anybody remember what that was?**

**What's the most straightforward way of kind of getting around all this cost-benefit discussion that we've just had?**

23

**So the one thing that they did not see was significant improvements in the enzyme. So they checked, and they found that they did not see any increase the lacZ activity normalized by the amount of the lacZ that was being made.**

**Now, that might make sense, because if this enzyme has already been gone through millions of years of optimization to break down lactose, then it's reasonable to say, oh, well, in the next five generations in the lab, it maybe won't improve.**

**Of course, you always have to be careful about this, because it could be that some sequence slash structure is best when you're thinking about-- when is it that E. coli might see lactose? Our gut.**

**So you imagine you have bacteria in the gut. That's a different environment than in the lab. So it could be very well that the enzyme, because of the pH and all these other things, the enzyme actually could adapt to the lab, even though it may have already been adapted to our gut.**

**So you have to got to be careful about this kind of argument always. But of course, once you see the result, then you say, oh, well, that's because of this.**

**So I just want to make sure that we know what these experiments look like. So they went for 500 generations. So it's useful to ask how long this experiment should have taken.**

**Is it closest to three days, three weeks? Anytime you read about an experiment, it's useful just to have some notion of what the authors went through in order to bring you the results you're reading about.**

**If you are not sure, you can just make a guess. OK, ready, 3, 2, 1. All right, so we have some number of A's, some number of B's, and a couple of C's.**

**Well, one thing you might say is, how fast can E. coli divide? OK, on one level, you may say oh, about 20 minutes. That should give us what? 75-ish generations a day. So we should be able to get here in a week or something, maybe.**

24

**But that's not what they did, for several reasons. First of all, this would be in rich media. In the environment that they are doing this in, it's a bit slower. But that would get you maybe to the two or three-week mark.**

**But that still is not what happened. They actually had to go for three months. And this is because experiments are not always keeping cells constantly dividing at their maximal rates.**

**The standard way that we do this is what's known as kind of daily batch culture. And does anybody know how much they diluted by each day? Yeah, so I think it was diluting by a factor of 100.**

**So it's daily batch culture with 100x dilution, which corresponds to about 6.6 generations per day. So this is very far from what you would think of as kind of the best they could possibly do. And what it means is that, yeah, it does take about three months for them to have done this experiment.**

**It also means that if you look at the number over the course of each day, this is n max. And they dilute-- this is n max over 100-- so they dilute by a factor of 100.**

**When you transfer cells from a saturated state into new environment, do they start dividing immediately, for those of you who have done this experiment? No. It's going to take an hour or two for them to get going.**

**But then they're going to start dividing. And this on a log scale maybe-- log N. And what you'll see is they kind of go-- they're dividing exponentially and then they saturate.**

**Indeed, they're going to saturate for about a fair amount of time. So this might be an hour or two. This might be say five hours.**

**But then you still have another roughly 20 hours to go before the next dilution. And then we repeat. So they actually saturated for a fair fraction of the day.**

**Now, in all these discussions of laboratory evolution-- and in many of the calculations we're going to be doing over the next couple of weeks-- we'll typically**

25

**assume that what is being optimized is the growth rate, the rate of division. But you can imagine there being other things that might possibly be optimized in the course of these sorts of experiments. Can somebody volunteer what are other things?**

**AUDIENCE: Maximum density? PROFESSOR: Right, so you could imagine, if you could just eke out one more division out there, then you could get an advantage. And there's a whole set of interesting things, these growth advantage. It's stationary phase or the GASP mutants, where the focus is on trying to do well here. And also you can imagine related maybe, if you do better out for this period, cells will start dying eventually. So if you have a lower rate of death at saturation, then you can also spread. Other-- yep.**

- **AUDIENCE: Sorry, can I ask a quick question? What's a possible reason for the initial [INAUDIBLE] used [INAUDIBLE] at the beginning?**

- **PROFESSOR: Yeah, right. So I think it's basically that when the cells are saturated, they generally enter a rather distinct physiological state, as compared to the dividing state. And I think the longer they sit in this saturated phase, the longer it's going to take them to get going in the next day, for example.**

**And it's also the case that cells in saturated culture tend to be more resistant to a variety of perturbations of various sorts-- so if you're talking about heat, salt, this, that, and the other thing. What's something else they could be optimized here? If you were imagining you're a cell, you want to spread, what would you do?**

**AUDIENCE: [INAUDIBLE]. PROFESSOR: OK, right. So we're saying that the media is specified by the experimentalist. So you're the cell in this Gedanken experiment. AUDIENCE: You'd divide yourself.**

26

- **PROFESSOR: Right, so you can eat the other cells, yeah. Well, and in particular, actually out here, this is part of how the GASP mutants spread, is that when other cells start to die, they lyse their contents. And then the cells that are surviving can actually eat the contents, yeah.**

- **AUDIENCE: Is this a way to coordinate between different cells, so that they can sort of evenly distribute themselves in the media, so you don't have to many--**

- **PROFESSOR: OK, right. So I'm actually assuming here it's well mixed, so that in principle would not be an issue. But yeah, so you can imagine spatial effects of various sorts being relevant. I guess I just drew this up here to highlight that, in principle, you can also decrease the lag time. So if you start dividing more rapidly at the beginning of the day, then you'll get to spread before your neighbors and your genotypes will indeed spread. Yep.**

- **AUDIENCE: So I just know so little about cells, but is it true that a lot of the cells could survive and be the same cell for that whole duration when they were in the stationary phase?**

- **PROFESSOR: You're asking whether the-AUDIENCE: Yeah, whether a cell that entered the beginning of the stationary phase, that same cell would have a pretty good chance of--**

- **PROFESSOR: Yeah, over I think this sort of 12-hour type period, I think the answer is yes. But if you go for an extra day or two, then I think you can start getting extensive cell death.**

- **AUDIENCE: Because then who knows? Maybe long enough, though, they would develop a little clock to let them know that it was about to split.**

- **PROFESSOR: Yes, right. Yeah, so people have thought about-- and I'm not sure if this--**

27

**AUDIENCE: And it seems like it would.**

**PROFESSOR: --particular effect is-- yeah, right. But I just want to mention that this is something that you kind of maybe would expect, indeed, you see in these-- so they're a famous set of experiments done by Richard Lenski at Michigan State, where he's been dividing six or eight-- doing daily batch dilutions of equal E. coli cultures now for decades.**

**So he started, I don't know, late '80s or so. I don't know if you guys remember. So he's gone tens of thousands of generations and has seen a bunch of remarkable things. One of the things that he has seen, as you might have expected, is a decrease in the lag time of the vector area.**

**So what we have now is a situation where they add IPTG, so that all the cells are in principle start out expressing the lac operon. And then they grow the cells over time. And what they see is that the lacZ activity, it starts out at being 1, normalized, for all the cultures, because there's IPTG, so it doesn't matter how much lactose there is. But what they see is that over time, they see things that look like this.**

**So the 0.5 millimolar lactose didn't change very much. But if you look at some of the others, like no lactose, there was significant decrease in expression. Whereas, up here at, for example, 2 millimolar lactose, they see an increase.**

**So what you see is that there really are evolutionary changes of these strains, because-- and it's very, very relevant that they had IPTG in the media. So if they did this experiment without IPTG, do you have any sense of what would kind of happen to the cells? I mean, how would that change the results? Yep.**

**AUDIENCE: The expression level would be determined by [INAUDIBLE].**

**PROFESSOR: Right, so the expression would be determined by the lactose. But let's say that after 500 generations, we put them all in a millimolar lactose. How different do you think they're going to be?**

**I mean, do think that the culture grown, for example, in the absence of lactose, do**

28

**you think that it would still be able to eat lactose after 500 generations in that experiment? Hm?**

**AUDIENCE: Yes. PROFESSOR: Yes, OK. And yeah, so what's the difference? I mean, why are you saying yes or what's the-AUDIENCE: [INAUDIBLE]. I don't know how hard it is-PROFESSOR: Well, yeah, right. So this is an experiment with IPTG. And now, I'm just trying to think about or imagine what would have happened if they had done the same experiment without IPTG just growing in that environment, in particular, if you grow minus IPTG and then minus lactose for 500 generations?**

**And then what I want to ask is, OK, let's say that you go over there and you just add lactose. Will the cells, do you think, be able to grow and the lactose? OK. And so why is it that here the answer seems to be no? So here, we have evolved a population that not only it's not expressing the lacZ activity here. But indeed, if you put lactose in there, it doesn't express. So these cells can no longer grow on lactose. So what's the key difference here? Yep. AUDIENCE: So I mean, there's no [INAUDIBLE] in this case. PROFESSOR: Right. Now I think this is just really important. So in this case, there is approximately, we'll say, no cost to having the lac operon on there, because it's just not being expressed. So then the only cost is associated with DNA replication. So the advantage associated with shutting off or removing the ability to grow on lactose is just really minimal. And indeed, in this culture, the authors did say, what happened. AUDIENCE: Yeah, the entire gene is diluted, right? PROFESSOR: Yeah, right. So it was almost a kB was just removed from the genome. And that kB**

29

**included the promoter. And so that it just-- yeah. So it's not going to be able to grow on lactose anymore.**

**But the key thing is here, these cells were subject to this 5% cost associated with making the lac operon, which means that that mutant that appeared, it had a 5% advantage, and so it was able to spread throughout the population.**

**Whereas, what they could see is that the evolved lacZ activity indeed was different, depending on how much lactose they had in the culture. And this is in the presence by IPTG, so they removed that feedback loop.**

**And in these experiments, anyway you slice it, the normalized lacZ activity did not go above around 1.2 or 1.3. So there is some non-linearity that is somehow constraining those cells from going up to increased expression very much beyond the wild type.**

**We are out of time, but on Tuesday, we'll start talking about evolution, and in particular, in the context of neutral evolution, as kind of a null model to try to understand these dynamics.**

**And we will also talk more about why it takes as long as it does before you start seeing anything happening here. If you have any questions, please feel free to come on up.**

30

---

[← [INTERPOSING VOICES].](04-interposing-voices.md) · [Up: contents](index.md)
