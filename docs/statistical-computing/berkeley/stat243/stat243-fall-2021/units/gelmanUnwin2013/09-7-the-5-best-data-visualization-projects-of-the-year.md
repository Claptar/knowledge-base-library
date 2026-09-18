---
title: 7. THE “5 BEST DATA VISUALIZATION PROJECTS OF THE YEAR”
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/gelmanUnwin2013.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/gelmanUnwin2013.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/gelmanUnwin2013.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/gelmanUnwin2013.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 7. THE “5 BEST DATA VISUALIZATION PROJECTS OF THE YEAR”

We illustrate our graphical ideas on the examples that motivated these thoughts, the list by statistician and Flowing Data blogger Nathan Yau of the best data visualizations of 2008. In using these examples to explore different perspectives on data graphics, we are not in any way trying to criticize the graphic design of these projects. We recognize that these projects look better and in many ways function better than most if not all of the graphics that we have made. One of our key goals in writing this article is ultimately to strengthen connections between statisticians and graphic designers. When we engage in criticism here, the purpose is to highlight our differences in perspectives.

## 7.1 WORDLE

This popular program created by Jonathan Feinberg (2009) for displaying word frequencies received Yau’s honorable mention. Figure 3 shows an example of Wordle in action.

Yau wrote, perceptively:

> It’s hard to say what exactly made Wordle so popular, but I [Yau] think it was a mix of randomness, aesthetics, and customization options.

From our perspective as creators and users of statistical graphics, we see Wordle as conveying a small but important amount of information (the most common words in a document and their approximate relative frequencies) in what we see as an eye-catching but confusing way. The advantages lie in the lack of ordering (you may see something you do not expect) and the fitting in of the most frequent substantive words. The disadvantages lie in the lack of ordering (every Wordle displays looks very different and you may miss important words due to color, orientation, or position) and fitting in of too many words. The alternative of listing the words in order of frequency and also using size and color would be consistent but would not encourage the kind of random word linking which Wordle encourages.

Figure 3. Wordle and other word/tag clouds have become a popular way to get a quick and attractive (if superficial) view of the content of a document. More frequently used words are presented in larger fonts; the colors and orientations of the words and the shape of the image convey no information.

Wordle certainly grabs attention and stimulates thought (goal 6) and it provides an overview (goal 1). To some extent, it encourages exploration (goal 3), since it is easy to try other variants, but the exploration is random rather than under the reader’s control. But our biggest problem with Wordle is that study of the image sends the viewer not toward a deeper understanding of the original data but rather toward engagement with Wordle itself. The how-did-they-do-it and how-does-it-work aspects of Wordle overwhelm the data it was intended to display.

For the purposes of the present article, what is relevant about Wordle is that the very features that work against it as a statistical graphic (randomness and difficulty of navigation) help make it effective for Infovis.

## 7.2 DECISION TREE THE OBAMA–CLINTON DIVIDE

Yau’s pick for fifth-best data visualization of 2008 came from Amanda Cox of the *New York Times* during the primary election season (see Cox 2008$^3$).

Both the authors of the present article dislike this graph. Unwin is unhappy because neither the relative importance of the splits in the tree nor their discriminating power is shown; thus it is difficult to assess how meaningful the tree is as a data summary. Gelman dislikes the tree because, as a political scientist, he dislikes the model it is based on, and he

---

$^3$Available at: http://graphics8.nytimes.com/images/2008/04/16/us/0416-nat-subOBAMA.jpg

thinks it leads people to a confused understanding of voting. Thus, he thinks the world would be better if nobody were to see this graph. He is not really complaining about the display, but more about what it is displaying. (Also, the title “decision tree” is misleading because the graph displays counties, but it is individual voters who are making the decisions. Counties do not “decide” how to allocate their votes.) This visualization gives a kind of overview (goal 1), though we have no idea how good it is. It does not encourage exploration and it implies that the divisions into groups are simpler than they really are, so we can strike goals 2 and 3. It does seem to be trying to tell a story (goal 5) and the photos probably help attract the reader’s attention (goal 6).

## 7.3 RADIOHEAD MUSIC VIDEO

This cool 4-min video (http://www.youtube.com/watch?v=8nTFjVm9sTQ) displays a movie reconstructed from data from a three-dimensional scanner (Radiohead 2008).

This is pretty; we just would not call this sort of thing “data visualization.” Rather, it is a use of data visualization tools to make art, and it is also a demonstration of statistical methods of image reconstruction. Both of these are great but seem to us to fall into a different category than statistical graphics. Maybe the relevant point here is that graphics can be identified by their technical tools as much as by their statistical goals. In that sense, the Radiohead video, three-dimensional cartoons, and all sorts of computer graphics (many of which are statistically based) serve as baselines for us in thinking about the possibilities of modern imaging, of which statistical graphics are a small subset.

## 7.4 BOX OFFICE STREAMGRAPHS

Yau wrote this of Lee Byron’s fascinating-looking stacked graphs of movie ticket sales (Bloch et al. 2008; http://www.nytimes.com/interactive/2008/02/23/movies/20080223_REVENUE_GRAPHIC.html):

> Discussion burst out across the Web—about the technique and what people were seeing in the data—that I am convinced would not have come about if instead of a Streamgraph, they used say, a stacked bar chart.

The online graph has interactive features that allow you to scroll over time, search for movies, and click on parts of the image to get details. And the graph does convey information; as Yau (2008a) wrote “You can see Oscar contenders attract a smaller audience than the holiday and summer blockbusters and kind of slowly build an audience.” Well, does it really? How can you tell which films were Oscar contenders and whether they had that kind of pattern?

The visualization does indeed look cool, but the strategy of stacking the curves on top of each other makes the visuals for individual films almost impossible to interpret. We would prefer two graphs, one showing total movie sales over time (and thus capturing the overall shape of the curve) and another showing the trajectories for the individual movies, possibly identifying Oscar contenders by color.

In this case, we believe the designers made a common error of statistical graphics: trying to cram into a single graph what can be better displayed in two. On the other hand, they achieved the goal of grabbing attention superbly, it is just that they did not achieve any other goal.

Figure 4. This data-based video is visually appealing but does not give an overview of the quantitative information that is essential for a statistical graphic. Reproduced with permission by Jonathan Harris and Sep Kamvar (2008); view the entire video at http://iwantyoutowantme.org/index.html. See also http://kamvar.org/ and http://www.number27.org/.

## 7.5 I WANT YOU TO WANT ME

In featuring this image and an accompanying video by Jonathan Harris and Sep Kamvar (2008; see Figure 4), Yau wrote that “this blend of art, computer science, and mathematics is beautiful.”

We agree that the I Want You to Want Me video is visually appealing, but, again, we do not really see it as an effective way to convey the data. It is more of a way to get attention, but then we would want a pointer toward a better data visualization to learn more. Our point here is not to criticize this work as a graphic design or as art but rather to focus on the different goals that we have in data display.

That said, we only will learn by trying new things, and that, for graphics, it is good to have new tools. Who knows if the eye-catching graphics you display in I Want You to Want Me might be altered to display data in some informative way? So we do not want to discourage experimentation. The perils come when a snazzy display is used to obscure information. As statisticians, we should have a way of pointing this out—of connecting the visuals to the goals of subject-matter understanding—without alienating people and obscuring our own message.

## 7.6 BRITAIN FROM ABOVE

Nathan Yau selected this series of videos as the top visualization project from 2008 (BBC 2008$^4$).

The videos show air traffic over Britain, and they represent an impressive computing and statistical achievement, putting together information from satellite images to visualize the transportation network and, in Yau’s words, “bring data to life.” Although this work is not a statistical graphic in the traditional sense, we could imagine it being combined with

---

$^4$Available at: http://www.bbc.co.uk/britainfromabove/

some data reductions (e.g., average flows of different kinds) to achieve statistical goals of communication and discovery. From a statistical point of view, it is hard to argue in favor of the distortion that occurs when presenting Britain from an angle rather than directly from above, though the idea is presumably to suggest you are actually in a plane looking at the flight traces. At the end of the video, attention is drawn to areas where no flight paths cross, possibly locations of secret military installations or high-security prisons. This visualization certainly satisfies goals 5 (telling a story) and 6 (grabbing attention), and to some extent, it communicates some information (e.g., the gaps), but statistical goals are not met.

## 7.7 OVERVIEW

The “best data visualizations of the year” are eye-catching graphics that in several cases use state-of-the-art methods in statistics and computer science, while at the same time not attempting to achieve traditional goals of statistical graphics. We would characterize all these graphs as visually attractive and data related, so at the very least, they can serve as inspirations to statisticians and other designers who are thinking about future data display challenges.

---

[← 6. BACKGROUND](08-6-background.md) · [Up: contents](index.md) · [8. STATISTICAL PROBLEMS WITH OTHER HIGHLY PRAISED INFOGRAPHICS →](10-8-statistical-problems-with-other-highly-praised-infographic.md)
