---
title: 4. Final assignments of treatments
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/protocol.pdf
source_file: sources/berkeley-stat158/spring-2026/project/protocol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Final assignments of treatments

**Source:** [`project/protocol.pdf`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/protocol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

After you have 𝑛 from your power calculations, you should make your final assign­ ments of treatments to units so that you are completely ready to run the experiment. This should take the form of a data frame with one row per measurment unit and columns for the unit identifier and the treatment(s) assigned to that unit. You should also have a column for the block (if applicable).

## Experimental Proctocol (your writeup)

Your protocol should be in paragraph format, except where noted below. The proto­ col writeup should contain the following information:

1. Start with a short description of the basic experiment to remind me, like the design proposal. This should briefly (in 1 paragraph) describe the core parts of the experiment without getting into the detail described below. This can be copied from your earlier submissions and updated as relevant.

2. Describe your power calculation, and the results of your calculation (i.e. what does it tell you about how many observations you are going to run). In describing your power calculation, you should include:

   - a definition of how you have defined sample size (is it # subjects, # runs, # LS squares, etc?). It should be be a reasonable value for your experiment.

   - your estimate of 𝜎<sup>2</sup> and a description of how you estimated it, i.e. how you collected the data, how many observations it’s based on, what estimate you used. You can use the initial estimate of 𝜎<sup>2</sup> from your initial proposal, if that is still relevant to your current design, but you still need to describe how you got it.

   - A description of why you chose your alternative hypothesis. This should be based on your understanding of the problem, so your description is a justifi­ cation of why it made sense.

   - Power curves. You should have one for each experimental factor and interac­ tion term if you have them.

   - The final sample size you chose, and what specific power that gives you.

2

If your power curve gives you a sample size that is not feasible for this experiment, you should pick the largest feasible sample size, and then describe both:

   - what power you will have with this reasonable sample size for your original choice of effect size

   - what effect size you could actually find with good power (i.e. 0.7-0.9) with this reasonable sample size

3. Describe the finalized protocol of the experiment. This can be in list or bullet point format to indicate the steps to be followed, as appropriate. It should be written so that you could hand this off to someone else and they could run the experiment correctly. Think of it as a training guide for someone you’ve recruited to run the experiment for you.

4. “Preregister” your plan of analysis. This is a best practice in the scientific commu­ nity, and helps prevent “p­hacking” and other questionable research practices. You should give a complete list of all of the inferential procedures you intend to run (i.e. hypothesis tests and confidence intervals), and you should describe how you will interpret the results of those procedures. For example, if you are going to run an ANOVA, you should say something like “If the p­value for the main effect of factor A is less than 0.05, then we will conclude that there is evidence that factor A has an effect on the response variable.” You should do this for each test or confidence interval that you intend to run.

You should also include as appendices to your protocol the following information:

- The data frame with the final assignments of treatments to units.

- Code to perform the analysis outined in your preregistration so that it’s ready to go when you have the data. This should be well organized and commented so that it is clear which code corresponds to which part of the analysis. You can also include code for any data formatting or cleaning steps that you intend to perform before the analysis. Note that this code can be directly copied from the code you used to perform the power calculations.

- Describe your dry run and what changes were made from your first initial draft of the protocol based on your experiences (there should always be some changes).

- (if applicable) Copies of any materials you had to create (e.g. if you gave subjects a test, attach the questions that they answer; if they have to read a passage, attach the passage(s), etc.). If you used some existing tool (e.g. an online quiz or typing program) please provide screen snapshot(s) of it so it is clear how it works for someone trying to implement your procedure. If the materials are not feasible to attach (e.g. a 3D game that they played) please provide a photo of them `in action’.

3

---

[← 3. Power Calculations](03-3-power-calculations.md) · [Up: contents](index.md)
