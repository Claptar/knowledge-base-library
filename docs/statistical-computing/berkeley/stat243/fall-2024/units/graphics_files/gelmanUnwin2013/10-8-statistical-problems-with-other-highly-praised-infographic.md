---
title: 8. STATISTICAL PROBLEMS WITH OTHER HIGHLY PRAISED INFOGRAPHICS
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/gelmanUnwin2013.pdf
source_file: sources/berkeley-stat243/fall-2024/units/graphics_files/gelmanUnwin2013.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/graphics_files/gelmanUnwin2013.pdf`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/graphics_files/gelmanUnwin2013.pdf) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 8. STATISTICAL PROBLEMS WITH OTHER HIGHLY PRAISED INFOGRAPHICS

Even infographics that are clever and beautiful can have problems when viewed as statistical data visualizations. We illustrate this with some examples that have appeared recently in the press.

## 8.1 PLANE CRASHES

Created by David McCandless (2009$^5$), this graphic was part of a series of graphs that won the *Guardian* newspaper’s Visualization Contest.

As Daniel Lakeland notes,

> The map appears to plot numbers of plane crashes per country, totally missing the point of expressing these as a rate ... . Another visualization from the same site has a more subtle problem, comparing things that don’t have the same units. Some of these are dollars per year, some are total dollars ever spent on some thing, some of these are dollars of capitalization per company.

Even though we agree fully with Lakeland’s comments, we are wary of criticizing this sort of visualization. For the goal of conveying information, it is horrible, but for sparking interest in their topics and motivating readers to look carefully at the numbers, maybe it is still useful. To give it a prize in a visualization contest, though ... well, we would not do that. That would be like deciding who won the Indy 500 by picking the car with the snazziest paint job. Might it help to shade the circles according to their accident rate? Even then we would still be left with the problem that the graphic shows the density by country,

---

$^5$Available at: http://www.informationisbeautiful.net/visualization/reduce-your-chances-of-dying-in-a-plane-crash/

not by location, so the circle for the United States does not even include any of the East coast, where probably many of the accidents occurred. In the case of Russia, it may even be the case that none of the Russian accidents occurred at locations covered by its circle! This display grabs attention but does little else.

## 8.2 FLORENCE NIGHTINGALE’S COXCOMB

Consider the famous image drawn by Florence Nightingale (1858), which is often considered as an exemplar of data display (see Figure 5). In a recent discussion of the coxcomb plot, Rehmeyer (2008) wrote

> The conventional way of presenting this information would have been a bar graph, which William Playfair had created a few decades earlier. Nightingale may have preferred the coxcomb graphic to the bar graph because it places the same month in different years in the same position on the circle, allowing for easy comparison across seasons. It also makes for an arresting image. She said her coxcomb graph was designed “to affect thro’ the Eyes what we fail to convey to the public through their word-proof ears.”

Given the context, the graph is impressive and important [see Small (1998) for further background on this and other work of Nightingale]. But given what we know today, we

Figure 5. Florence Nightingale’s celebrated circular plot of Crimean War mortality is a landmark in infographics, but a modern-day statistician would prefer to display such data using simple time-series plots such as shown in Figure 6. The ability of the circular plot to line up months in different years obscures the patterns in the data and offers little if any benefit in this example. At the same time, the attractive and unusual appearance of Nightingale’s graph—even its puzzle-like nature—might well have helped draw attention to the public health problems she was working on. This illustrates the differing goals of statistical graphics (intended for understanding patterns in data and departures from these patterns) and information visualization (intended to attract attention and stimulate thought in people who might otherwise not have been interested in the topic). Reproduced with permission by Hugh Small, from *Florence Nightingale: Avenging Angel*, http://www.florence-nightingale-avenging-angel.co.uk/.

would prefer it as a line plot (not a bar graph, which, as Rehmeyer notes, unfortunately is indeed the default choice for many if not most producers of graphs).

In theory, the circular plot could have advantages for displaying monthly regularities, but, first, such regularities are not so strong in this dataset (or, if they are, the circular plot is not a good way to reveal them!), and second, one could always do the comparisons by month better by overlaying several years with line plots. We find it surprising that Rehmeyer claims the display allows “easy comparison across seasons.” The circular structure of the above image is indeed beautiful but we do not think it conveys the information very well. In addition, each color is measured from the center, so that the total numbers of deaths per month from the three causes are impossible to determine. Overlaps complicate the interpretation further. It is also unusual that the data for the first 12 months are drawn in the right plot and the data for the second 12 months in the left plot. Conventions help and should only be disregarded for very good reason.

Figure 6 shows an alternative we prepared. The upper graphs show the dramatic rise and fall in the death rates from “zymotic” (basically, infectious) diseases while emphasizing the comparatively low rates of deaths from other causes. The lower graph shows that the army size varied, but not nearly as much. The time series for the army size has purposely

Figure 6. The Crimean War mortality data as time series graphs. The use of different forms (line plot for death rates and bars for army size) is a visual cue that two sorts of data are being presented: monthly rates (multiplied by 12 to be annualized, following Nightingale’s calculations) and absolute numbers.

been drawn as a bar graph as it represents counts and also because this makes it clear that we are dealing with a different kind of series.$^6$

Our point here is not to claim that our plots are optimal but rather to contrast the virtues of Nightingale’s display—its unique appearance and the visual appeal of the areas and the 12-month circles—with our strategy, characteristic of statistical graphics, to choose a bland, conventional background to allow the reader to more clearly see the changes within and between the time series.

In the language of the present article, the Nightingale graph is an excellent example of “infographics”—it is attractive, grabs one’s attention, and gets you thinking—but it is not so great as “statistical graphics” in that it does not directly facilitate a deeper understanding of the data. In Nightingale’s political context, the goal of attracting attention was arguably much more important than the goal of understanding and communicating subtle patterns in the data.

If we were presenting these alternatives on the Web, it could be appealing to offer both the Infovis and statistical graphics. The display would start with the Nightingale plot to draw attention. Then, clicking on the coxcomb would switch the display to a more statistical graphic such as our Figure 6. Finally, another click could bring up a spreadsheet with the data. Another option could be to include decoration to draw attention and have it fade away on clicking to enable the reader to concentrate on the data information.

We do not claim that our graphs are better than Nightingale’s classic; rather the two displays serve different purposes, and in the modern high-bandwidth era, there is room for both. The first step is to understand the different goals involved in a graphical display.

## 8.3 HEALTH-CARE SPENDING AND LIFE EXPECTANCY

A graphic produced by Oliver Uberti in 2009$^7$ for *National Geographic* dramatizes that Americans spend much more on health care, compared with residents of a range of other countries, without seeing any apparent benefit in terms of life expectancy.

Figure 7 (from Gelman 2009b) contains the same information while following the standard principles of statistical graphics. The standard way to display two variables is a scatterplot, in this case health-care spending versus life expectancy. (The original display also contains information on the frequency of doctor visits, but this third variable appears to be a minor part of the story.) The scatterplot reveals the arbitrariness of the scaling of the parallel coordinate plot in this example. In particular, the original graph gives a sense of convergence that spending is all over the map but all countries have pretty much the same life expectancy—look at the way the lines converge to a narrow zone as you follow the lines from the left to the right of the plot.

But once you remove the United States, there is a strong correlation between spending and life expectancy, and this jumps out of the scatterplot, much more than in that eye-catching parallel coordinate plot. (For simplicity, we have removed the data on doctor visits from our plot; a display of that additional information reveals no particular relation with the two major variables.)

---

$^6$The data used in Nightingale’s graph are available at http://understandinguncertainty.org/node/214.
$^7$Available at: http://blogs.ngm.com/blog_central/2009/12/the-cost-of-care.html

Figure 7. A scatterplot that displays the health-spending/life-expectancy data shown at http://blogs.ngm.com/blog_central/2009/12/the-cost-of-care.html, but more transparently, more informatively, and in less space. The *National Geographic* blog graphic is a dramatic display, while this figure shows the pattern of the two variables more clearly. The two displays serve different goals, and an online display might start with the *National Geographic* figure and then reveal Figure 7 with a click. The online version of this figure is in color.

But data graphs are not just judged on informativeness. Another consideration is novelty. The scatterplot in Figure 7 looks like lots of other graphs we have all seen. This is a plus—familiar graphical forms are easier to read—but also a minus, in that it probably looks boring to many readers. The parallel-coordinate plot at http://blogs.ngm.com/blog_central/2009/12/the-cost-of-care.html is not really the right choice for the goal of conveying information in this case, but it is exciting and new to many people, and that is maybe why one of the commentators at the *National Geographic* website hailed it as “a masterpiece of succinct communication.” The goal is not just to display information but also to grab the eye.

Ultimately, we think the solution is to do both—in this case, to make a scatterplot in some pretty, eye-catching way. Not being experts on graphic design, we just did the first part and will leave it to others to figure out good ways of making the display more eye catching.

Figure 8. This flowchart—part of a PowerPoint presentation from a military contractor—effectively displays the complexity of planning during the Afghan war but would not be good if the goal is data or model visualization, in the public domain.

## 8.4 HOW TO WIN IN AFGHANISTAN

The graph reproduced in Figure 8 was prepared by a military contractor for the Office of the Joint Chiefs of Staff. Neither of us has ever been involved in any planning more complicated than setting up an M.A. program, and that had a budget approximately one-zillionth that of the Afghan war. Without any experience in large projects, we will limit our comments to the graph itself.

To start, we think the graph would be improved by making the arrows lighter—gray rather than black—and maybe reducing the number of arrows overall. We understand the goals of showing the connections between the nodes, but as it is, the graph is dominated by the tangle of lines.

A larger problem is that the picture gives no sense of priorities. All the items are the same size and it is not clear where the focus should be. The full presentation (PA Consulting Group 2008, http://msnbcmedia.msn.com/i/MSNBC/Components/Photo/_new/Afghanistan_Dynamic_Planning.pdf) puts all the nodes in context and makes the story clearer. But we can not really see what is gained from the image. We can understand the value of a complicated graph showing suppliers and contractors and purchasers and so forth, but we do not see what you get out of this sort of map where most of the nodes are vaguely defined concepts.$^8$

---

$^8$We looked carefully at the graph and could only find one node that is an orphan (i.e., with no arrows pointing toward it). This node is “Media Sensationalism Bias.” Perhaps there could be another node leading to it, labeled “Pay \$\$ to friendly journalists.”

As noted above, we are complete strangers to the world of military planning, and we are reacting based on our understanding of graphical display. We are suspicious of the combination of a complex display and lack of precision in the details. Similarly, we suspect the graph displayed above does not do much to directly help the planning for Afghanistan, but it certainly does a good job of conveying the complexity of the situation! Maybe that was the point.

As statisticians, one might simply label Figure 8 as “junk” and leave it at that. Our point, though, is not merely to offer judgment (although we are happy to use our professional expertise in that way as necessary) but to use this example, quite different from the usual histograms and scatterplots of statistical texts, to consider the goals of graphical displays.

The Afghanistan flow chart is neither a data visualization nor a statistical graph, but it raises a point that is relevant to our discussion: this display is not useful for conveying information, but it is useful for giving context. If someone mentions a concept, then you find it on the display and see what other concepts are related to it. In that sense, it is more like a (nonstatistical) map than a graph. At least, that is the theory. In practice, we are skeptical that the above display is useful even as a conceptual map, but we will leave that for the subject-matter experts to judge. Our point here is to connect the visual format of the image to the goals that motivated its creation. It is through considering these goals that we as statisticians can better offer constructive criticism.

---

[← 7. THE “5 BEST DATA VISUALIZATION PROJECTS OF THE YEAR”](09-7-the-5-best-data-visualization-projects-of-the-year.md) · [Up: contents](index.md) · [9. STATIC STATISTICAL GRAPHICS: TIMELESS OR SIMPLY OLD FASHIONED? →](11-9-static-statistical-graphics-timeless-or-simply-old-fashion.md)
