---
title: Question, yes.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/j1s9jfzkfqu-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question, yes.

**Source:** `recordings/j1s9jfzkfqu-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**AUDIENCE: How far away do we search for neighbors?**

11

**PROFESSOR:**

**That's the art of this process, so I gave you a straight answer. Different approaches will use different thresholds. Any other questions?**

**OK, so the key thing I want you realize, then, is there's this distinction between the minimization approach and simulated annealing approach. Minimization can only go from state one to the local free energy minimum, whereas the simulated annealing has the potential to go much further afield, and potentially to get to the global free energy minimum. But it's not guaranteed to find it.**

**OK, so let's say we start in state one and our neighbor state was state two. So we'd accept that with 100% probability, right? Because it's lower in energy. Then let's say the neighboring state turns out to be state three. that's higher in energy, so there's a probability that we'll accept it, based on the difference between the energy of state two and state three. Similarly from state three to state four, so we might drop back to state two. We might go up. And then we can eventually get over the hump this way with sum probability. It's a sum of each of those steps. OK?**

**OK, so if this is our function for deciding whether to accept a new state, how does temperature affect our decisions? What happens when the temperature is very, very high, if you look at that equation? So it's minus e to the delta. The difference in the energy over kT. So if t is very, very large, then what happens that exponent?**

**It approaches zero. So e to the minus zero is going to be approximately 1, right? So at very high temperatures, we almost always take the high energy state. So that's what allows us to climb those energetic hills. If I have a very high temperature in my simulated annealing, then I'm always going over those barriers.**

**So conversely, what happens, then, when I set the temperature very low? Then there's a very, very low probability of accepting those changes, right? So if I have a very low temperature-- temperature approximately zero-- then I'll never go uphill. Almost never go uphill. So we have a lot of control over how much of the space this algorithm explores by how we set the temperature.**

**So this is again a little bit of the art simulated annealing-- decide exactly what**

12

**annealing schedule to use, what temperature program you use. Do you start off high and go literally down? Do you use some other, more complicated function to decide the temperature? We won't go into exactly how to choose these. [INAUDIBLE] you could track some of these things down from the references that are in the notes.**

**So we have this choice. But the basic idea is, we're going to start at higher temperatures. We're going to explore most of the space. And then, as we lower the temperature, we freeze ourselves into the most probable confirmations.**

**Now, there's nothing that restricts simulated annealing to protein structure. This approach is actually quite general. It's called the Metropolis Hastings algorithm. It's often used in cases where there's no energy whatsoever and it's thought of purely in probabilistic terms.**

**So if I have some probabilistic function-- some probability of being in some state S-I can choose a neighboring state at random. Then I can compute an acceptance ratio, which is the probability of being a state S test over the probability of being in a current state.**

**This is what we did in terms of the Boltzmann equation, but if I some other formulation for the probabilities I'll just use that. And then, just like in our protein folding example, if this acceptance ratio is greater than 1, we accept the new state. If it's less than 1, then we accept it with a probabilistic statement.**

**And so this is a very general approach. I think you might see it in your problem sets. We certainly have done this on past exams-- asked you to apply this algorithm to other probabilistic settings. So it's a very, very general way to search the sample across a probabilistic landscape.**

**OK, so we've seen these three separate approaches, starting with an approximate structure and trying to get to the correct structure. We have energy minimization, which will move towards the local confirmation. So it's very fast compared the other two, but it's restricted to local changes. We have molecular dynamics, which actually**

13

**tries to simulate the biological process. Connotationally very intensive.**

**And then we have simulated annealing, which tries to shortcut the root to some of these global free energy minima by raising the temperature, pretending at this very high temperature so we can sample all the space, and then cooling down so we trap a high probability confirmation.**

**Any questions on any of these three approaches? OK.**

**All right, so I'm going to go through now some of the approaches that have already been used to try to solve protein structures. We started off with a sequence. We'd like to figure out what the structure is. And this field has had a tremendous advance, because in 1995 a group got together and came up with an objective way of evaluating whether these methods were working.**

**So lots of people have proposed methods for predicting protein structure, and what the CASP group did in '95 was they said, we will collect structures from crystallographers, NMR spectroscopists, that they have not yet published but they know they're likely to be able to get within the time scale of this project. We will send out those sequences to the modelers.**

**The modelers will attempt to predict the structure, and then at the end of the competition we'll go back to the crystallographers and the spectroscopists and say, OK, give us a structure and now we'll compare the predicted answers the real ones. So no one knows are the answer is until all the submissions are there, and then you can see objectively which of the approaches did the best.**

**And one of the approaches that's consistently has done very well, which we'll look at in some detail, is this approach called Rosetta. So you can look at the details online. They split this modeling problem into two types. There are ones for which you can come up with a reasonable homology model. This can be very, very low sequence homology, but there's something in the database of known structure that it's sequenced similarly to the query. And then ones where it's completely de novo.**

**So how do they go about predicting these structures? So if there's homology, you**

14

**can imagine the first thing you want to do is align your sequence to the sequence of the protein that has a known structure. Now, if it's high homology this is not a hard problem, right? We just need to do a few tweaks. But we get to places-- what's called the Twilight Zone, in fact-- where there's a high probability that you're wrong, that your sequence alignments could be to entirely the wrong structure. And that's where things get interesting.**

**So they've got high sequence similarity-- greater than 50% sequence similarity that are considered relatively easy problems. These medium problems that are 20% to 50% sequence similarity. And then very low sequence similar problems-- less than 20% sequence similarity.**

**OK, so you've already seen this course methods for doing sequence alignment, so we don't have to go into that in any detail. But there are a lot of different specific approaches for how to do those alignments. You could do anything from blast to highly sophisticated Markov models to try to decide what's most similar to your protein structure.**

**And one of the important things that Rosetta found was not to align on any single method but to try a bunch of different alignment approaches and then follow through with many of the different alignments. And then we get this problem of how do you refine the models, which is what we've already started to talk about.**

**So in the general refinement procedure, when you have a protein that's relatively in good shape they apply random perturbations to the backbone torsion angle. So this is again the statistical approach, the not allowing every atom to move. They're just rotating a certain number of the rotatable side chains. So we've got the fine psi angles in the backbone, and some of the side channels.**

**They do what's called rotamer optimization of the side chain. So what does that mean? Remember that we could allow the side chains to rotate freely, but very, very few of those rotations are frequently observed. So we're going to choose, as these three choices, among the best possible rotamers, rotational isomers. And then once we've found a nearly optimal side chain confirmation from those highly probable**

15

**ones, then we allow more continuous optimization of the side chains.**

**So when you have a very, very high sequence homology template, you don't need to do a lot of work on most of the structure. Right? Most of it's going to be correct. So we're going to focus on those places where the alignment is poor. That seems pretty intuitive.**

**Things get a little bit more interesting when you've got these medium sequence similarity templates. So here, even your basic alignment might not be right. So they actually proceed with multiple alignments and carry them through the refinement process.**

**And then, how do you decide which one's the best? You use the potential energy function. Right? So you've already taken a whole bunch of starting confirmations. We've taken them through this refinery procedure. You now believe that those energies represent the probability that the structure is correct, so you're going to choose which of those confirmations to use based on the energy.**

**OK, in these medium sequence similarity templates, the refinement doesn't do the entire protein structure, but it focuses on particular region. So places where there are gaps, insertions, and deletions in the alignment. Right? So your alignment is uncertain, so that's where you need to refine the structure. Places that were loops in the starting models, so they weren't highly constrained.**

**So it's plausible that they're going to be different in the starting structure from some homologous protein and in the final structure. And then, regions where the sequence conservation is low. So even if there is a reasonably good alignment, there's some probability that things have changed during evolution.**

**Now, when they do a refinement, how they do that? In these places that we've just outlined, they don't simply randomly perturb all of the angles. But actually, they take a segment of the protein, and exactly how long those segments are has changed over the course of the Rosetta algorithm's refinement. But say something on the order of three to six amino acids. And you look in the database for proteins that**

16

**have known structure that contain the same amino acid sequence.**

**So it could be completely unrelated protein structure, but you develop a peptide library for all of those short sequences for all the different possible structures that they've adopted. So you know that those are at least structures that are consistent with that local sequence, although they might be completely wrong for this individual protein. So you pop in all of those alternative possible structures.**

**So OK, we replace the torsion angles with those of peptides of known structure, and then we do a local optimization using the kinds of minimization algorithms we just talked about to see whether there is a structure that's roughly compatible with that little peptide that you took from the database that's also consistent with the rest the structure. And after you've done that, then you do a global refinement.**

**Questions on that approach?**

**OK, so does this work? One of the best competitors in this CASP competition. So here are examples where the native structure's in blue. The best model they produced was in red, and the best template-- that's the homologous protein-- is in green. And you can see that they agree remarkably well. OK?**

**So this is very impressive, especially compared to some of the other algorithms. But again, it's focusing on proteins where there's at least some decent homology to start with.**

**If you look here at the center of these proteins, you can see the original structure, I believe, is blue, and their model's in red. You can see they also get the side chain confirmations more or less correct, which is quite remarkable.**

**Now, what gets really interesting is when they work on these proteins that have very low sequence homologies. So we're talking about 20% sequence similarity or less. So quite often, you'll actually have globally the wrong fold-- a 20% sequence similarity.**

**So what do they do here? They start by saying, OK, we have no guarantee that our**

17

**templates are even remotely correct. So they're going to start with a lot of templates and they're going to refine all of these in parallel in hopes that some of them come out right at the other end.**

**And these are what they call more aggressive refinement strategies. So before, where did we focus our refinement energies? We focused on places that were poorly constrained, either by evolution or regions of the structure that weren't wellconstrained, or places where the alignment wasn't good.**

**Here, they actually go after the relatively well-defined secondary structure elements, as well. And so they will allow something that was a clear alpha helix in all of the templates to change some of the structure by taking peptides out of the database that have other structures. OK?**

**So you take a very, very aggressive approach to the refinement. You rebuild the secondary structure elements, as well as these gaps, insertions, loops, and regions with low sequence conservation. And I think the really remarkable thing is that this approach also works. It doesn't work quite as well, but here's a side by side comparison of a native structure and the best model.**

**So this is the hidden structure that was only known to the crystallographer, or the spectroscopist, who agreed to participate in this CASP competition. And here is the model they submitted blind without knowing what it was. And you can see again and again that there's a pretty good global similarity between the structures that they propose and the actual ones. Not always. I mean, here's an example where the good parts are highlighted and the not-so-good parts are shown in white so you can barely see them.**

---

[← PROFESSOR](05-professor.md) · [Up: contents](index.md) · [[LAUGHTER] →](07-laughter.md)
