---
title: Final Report Guidelines
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/final-report.pdf
source_file: sources/berkeley-stat158/spring-2026/project/final-report.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Final Report Guidelines

**Source:** [`project/final-report.pdf`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/final-report.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Your final report is expected to convey the design and results of your experiment in a polished and professional format of similar to one that you would submit to a scientific journal or to your supervisor at work. This is an exercise in communication as much as it is an exercise in data analysis.

A few practical guidelines:

- The page limit is ten pages, not including appendices. Points will be deducted for overly long reports.

- This is a written report in paragraph form. You should make tables and figures but you should refer to them in the text. You should not be giving lists of things in the main body of the report, and code chunks should only be shown if they are very brief and highly salient to a point made in the text, otherwise they should be hidden.

- Don’t give any lists or bullet points, but make a paragraph description of everything except equations. If you feel a list is needed (e.g. levels of your conditions, what units go with what factors, etc.) then format it into a reasonable looking table and reference it.

- Tables and figures should be given numbers so that you can clearly refer to them in the text.

- Run spell check and grammar check. The use of AI is permitted as long as you fully document where and how it was used (see description of Appendix below). Note that when working in an area that you’re very familiar with (like your experiment), prompting and revising the output from an LLM is often more time consuming and less coherent than writing without an LLM.

- You can reuse any text or material from earlier work, but make sure you correct any errors!

## The Structure

The report should consist of the following sections:

1. Introduction: give a birds-eye overview of the problem, the experiment and the results, in broad strokes. You should generally not have to refer to tables, plots or other details for this material. If there are previous published studies that you consulted when planning your experiment, cite them here.

2. Methodology: describe your experiment in more detail. Here is the place to outline the specific levels of the condition, the nature of the response, etc. You should

1

summarize the rationale for the choices you made in the design (why this design, why these number of samples, why these levels, why this response, etc.) Much of the material from the proposal(s) will go here; however, you should make sure that it is in report format and fits into a single description. Here is also the time to reflect on any possible shortcomings of the design, both in principle (e.g. validity and replicability, power, etc.) and also in practice (e.g. any problems seen after running the experiment that might effect the results, mistakes, etc.).

You should give summary details about decisions you made in the protocol, but the nitty-gritty should be in the protocol you should have already turned in. The level of detail should be similar to what you gave in the design proposal and/or initial proposal. For example, you can say “We controlled for the possibility of temperature changing over time by closely monitoring the temperature every five minutes and correcting it as necessary”, but don’t give the detail that person A checked the temperature every five minutes, each time reported it to person B, who then recorded it, etc. This level of detail should be in the protocol. Similarly, you should describe the randomization procedure (“we permuted the 16 treatment combinations and assigned them at random to the 16 runs for each subject”). You can refer to the protocol in your text as if it were an attached appendix to your report. However, don’t assume the reader is familiar with it in your text.

If you made significant changes to your procotol after submission, please include those changes as an appendix.

You should also give a table of your data at the end of this section, organized in a compact, readable format. If you have a large amount of data it is permissible to put this table in the appendix instead but please include it.

3. Results: this should discuss the results of analyzing the data, as well as any possible problems. It should form a logical narrative, not be a series of plots or statistics. You do not need to follow the order you do the analysis. You should give 1-3 plots, and again they should be a logical part of the narrative of your results and appropriate to the analysis. Computational results of an analysis (e.g. summary statistics / output of tests) should be included interspersed in the text or in a well-formatted table, not as code output.

The text describing the results of the analysis should be readable and complete without looking at the plots or the tables. The plots and tables support your conclusions in your text – they are evidence backing up your claims – but the text should be able to stand alone. You should not say “Figure 2 shows that there is little reason to believe interactions are present,” because this sentence doesn’t explain what Figure 2 is or what it is supposed to demonstrate. A figure shows a pattern, it does not give the conclusions you can draw from those points. A better

2

way to write this would be “As we can see in the interaction plot (Figure 2), the differences in group means across levels of factor A are similar across levels of factor B, which is consistent with an absence of interactions.” However, please use your own words rather than copying this sentence verbatim.

4. Discussion or Conclusion: you should draw a birds-eye view of the results, as well as any further questions your results suggests. Here is the time to discuss things one could do in a follow-up study.

5. Appendix

6. (If applicable) An appendix called “Use of AI” that describes which LLM you used in creating your final report, if any, and precisely what it was used for. Note that this is an increasingly common required component of submissions to scientific journals.

7. (If applicable) An appendix with any significant changes that you made to the protocol that you submitted.

8. Appendix with your lab notes taken when you recorded the data. This should have all of the raw data in it, in the order that the experiments were run, with any comments you made.

9. Appendix of R code, organized and commented so that it is possible to quickly find the code that goes with the discussion. For example,

```
###############

---

[Up: contents](index.md) · [Reading in and formatting data →](02-reading-in-and-formatting-data.md)
