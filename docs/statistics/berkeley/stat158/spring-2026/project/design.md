---
title: Design Proposal Guidelines
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/design.pdf
source_file: sources/berkeley-stat158/spring-2026/project/design.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Design Proposal Guidelines

**Source:** [`project/design.pdf`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/design.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Stat 158, Spring 2026

In this proposal, you should now give a specific description of the design you will use to carry out your experiment. Your options for random assignment include:

1. Completely Randomized (CR)

2. Block Design (CB or GCB)

3. Latin Square (LS)

4. Crossover Design / Repeated Measures

5. Split Plot Design<sup>1</sup>

You’re encouraged to consider multiple experimental factors (a factorial design). If you use a CR design, it is required that you use at least 3 factors.

Your proposal should be in paragraph format. You should not include lists or bullet points unless you are describing steps in a process; if you want to briefly summarize material, make it into a nicely formatted table to which you can refer in your text. You can put headers to separate sections, but do not give your proposal in a list format (i.e. don’t write down numbers with the response to the below, but write it all as a report). You can make sections to correspond to the elements below, as relevant.

Any text that is relevant can be copied from your previous proposal.

## Structure

- Start with a short description of the basic experiment to remind me. This should briefly (in 1 paragraph) describe the core parts of the experiment without getting in to the detail described below (e.g. “We plan to run a complete block experiment in which we evaluate the effect of x, y, and z on a subject’s ability to xxx.”). It should give also a brief description of a single run, again to refresh my memory (“At each run, a subject will …”). If you have dramatically changed your idea from your initial proposal, you should make that clear here and describe your new experiment in a bit greater detail so that it is clear.

- Describe the design of the experiment which should include the following infor­ mation. Some may be replicated information from your previous submission but you should check and make sure that the specifics of your design do not alter any

> 1We will not cover split plot designs in class, but they are a common design in many fields. If you want to use a split plot design, you can read about them here and here. Course staff is happy to help you implement this design if it seems like a good fit for your research question.

1

of the answers, e.g. units. Make sure you cover all of the following elements (they do not have to be in this order):

   - ‣ The name of the design.

   - ‣ The conditions of interest and the treatment combinations that will be applied to the units. If you did not use all of your original factors from your initial proposal, explain why you made a change.

   - ‣ Any blocking factors.

   - ‣ The nature of the response.

   - ‣ What the experimental units are and how the units will be assigned to treatments. This should include what the units are for each condition and a general descrip­ tion of the randomization procedure (in a general sense, do not give the specific assignment).

- Convince me you’ve picked the right design for your experiment. Specifically, de­ scribe why this design is well­suited to the questions you want to ask. Remember most designs are chosen because of inherent constraints or inconveniences you face in making the design. Describe those constraints and how this design gets around them.

- Include a dataframe with a row for every unit in your study and a column for every factor, both blocking factors and factors of interest. You’ll be deciding your number of replicates and thus the total number of units in the your Procotol (the next assignment), so for now select a stand­in value. Either 0 or 1 replicates is fine.

Fill in the values (i.e. levels) for each of these factors; since as the experimenter you will be assigning these, you can determine them ahead of the experiment. When you conduct the experiment, you’ll just add on an additional column for the recorded response.

You can produce tables in Quarto documents either using Markdown tables or by making a dataframe in R and then turning it into table by using either the <mark>`kable()`</mark> function in the <mark>`knitr`</mark> package or the <mark>`gt()`</mark> function in the `gt` package.

- Provide the linear model that you will use to decompose the data into various meaningful components, for example: 𝑦𝑖𝑗 = 𝜇+ 𝛼𝑖 + 𝜖𝑖𝑗. Describe what each sym­ bol represents, both the Greek and the subscripts. Also include the formulae that you will use to estimate each parameter using your data.

Note that you can include mathematical symbols in a Quarto document using latex in forms: inline math and display math. The previous equation is inline math as was created using <mark>`$y_{ij} = \mu + \alpha_i + \epsilon_{ij}$` .</mark> The following is display math (which appears in its own paragraph)

𝑦𝑖𝑗 = 𝜇+ 𝛼𝑖 + 𝜖𝑖𝑗

2

### and was created using:

```
$$
y_{ij} = \mu + \alpha_i + \epsilon_{ij}
$$
```

3

---

[Up: contents](../index.md)
