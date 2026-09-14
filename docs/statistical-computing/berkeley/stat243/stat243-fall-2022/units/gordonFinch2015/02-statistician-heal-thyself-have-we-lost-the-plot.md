---
title: 'Statistician Heal Thyself: Have We Lost the Plot?'
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/gordonFinch2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2022/units/gordonFinch2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Statistician Heal Thyself: Have We Lost the Plot?

**Source:** [`units/gordonFinch2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/gordonFinch2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## Ian GORDON and Sue FINCH

In 1984, Cleveland suggested that statisticians have an important role in changing the use of graphics in science for the better. Thirty years later, we compared graphs published in top-rated applied science and statistics journals, evaluated for overall quality and against five principles of graphical excellence. Nearly 40% of the 97 graphs we sampled were rated as poor, with no striking differences between the applied science and statistics graphs. Better use of graphs requires better definition of variables, units of measurement, scales, groups, and other graphical elements, and more routine use of grid lines on a “standard” set of graphical forms. Progress over the next 30 years needs to be supported by changes in software defaults.

**Key Words:** Chartjunk; Statistical communication; Statistical graphics.

## **1. THE REVOLUTION IN GRAPHICS?**

Those of us who believe graphing to be important and even essential to research would be well advised to think hard about why visual displays are not used more extensively in serious applied research.

Gelman (2011, p. 4)

The art and science of making good graphs in statistics was elucidated by John Tukey (1972, 1977). The ideas of Tukey’s colleagues and successors including key figures Bill Cleveland (1985) and Edward Tufte (1983) have influenced the development of graphs in statistical software, making powerful tools for graphing data widely available today. In 1984, Howard Wainer showed us the “dirty dozen” for displaying data badly (Wainer 1984), but it remains very easy to find poorly constructed and badly documented graphs in both lay and academic publications and presentations. In the same year, Cleveland concluded that “statisticians can play _. . ._ the leading role, in effecting an improvement of graphical communication in science” (Cleveland 1984, p. 265).

Other important reviews and commentary on graphics include the historical archive of Friendly and Denis (2014) and Wickham’s (2013) survey of the literature on the design of statistical graphics. More than 60 years ago, a remarkable series of articles by Haemer

Ian Gordon (E-mail: _irg@unimelb.edu.au_ ), and Sue Finch (E-mail: _sfinch@unimelb.edu.au_ ), Statistical Consulting Centre, The University of Melbourne, Victoria 3010, Australia.

> ⃝C _2015 American Statistical Association, Institute of Mathematical Statistics, and Interface Foundation of North America_

> _Journal of Computational and Graphical Statistics, Volume 24, Number 4, Pages 1210–1229 DOI: 10.1080/10618600.2014.989324_

> Color versions of one or more of the figures in the article can be found online at _www.tandfonline.com/r/jcgs_ .

**1210**

**1211**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?

in _The American Statistician_ made numerous cogent points that have been reemphasized in the modern era (Haemer 1947a, b, 1948a, b, c, 1949a, b, c, 1950a, b, 1951), including problems with double scales, attempts at using a third dimension, and the unhelpful use of color.

It is true that graphs in different contexts serve different purposes, and sometimes graphs unsuitable for scientific purposes may, in nonscience publications, attract people to a topic (Gelman and Unwin 2013). However, the purpose of statistical graphics, especially in scientific discourse, remains vitally important.

Every budding statistician is routinely taught statistical graphics, and the reforms begun by Tukey are generally applauded. There is, however, a contradiction. In his tongue-in-check old-school defense of tables over graphs, Gelman (2011) suggested that there are many applied scientists who remain unconvinced about the value of graphs. Feinberg and Wainer (2011) found a strong preference for tables rather than graphs as a display format in three high-ranking journals from applied disciplines as well as in the _Journal of Computational and Graphical Statistics_ . Gelman and others (Cleveland 1984; Gelman, Pasarica, and Dodhia 2002; Kastellec and Leoni 2007) have identified a need for greater use of graphs in statistics and allied disciplines literature. Cook and Teo (2011) recommended the use of graphs over tables based on the speed and accuracy with which information about statistical simulation studies could be decoded. However, the skeptics or “table people” (Friendly and Kwan 2011) are unlikely to be convinced of the power of graphics without examples of graphical excellence.

This raised questions for us. Have statisticians taken up the leading role Cleveland advocated? Are statisticians any good at making graphs? In particular, are graphs published in statistics journals consistent with principles of good graphics? Is the quality of graphs in academic journals in statistics any better than in allied applied science disciplines?

## **2. PRINCIPLES OF GRAPHICAL EXCELLENCE**

Cleveland (1984), for example, provided guidelines for authors after reviewing hundreds of graphs in scientific publications. We draw on the work of Cleveland and Tufte to provide a framework for evaluating the quality of statistical graphics, and for educating students. This framework integrates the principled insights of Cleveland and Tufte with practical rules of thumb. A good graph will be consistent with all the principles, a poor graph will fail in several ways. The same rule of thumb can follow from more than one principle.

While graphs are perhaps under-used, there is a strong convention dictating the production of _some_ graph in many contexts. Conference presentations of applied science research, for example, frequently include graphics. A picture may be worth a thousand words; but a picture is not necessarily worth one or two words. We should first ask if the space required for a graph is justified. If the answer is yes, then an overall standard should guide the production—does this graph stand alone? While aspects of the context (the text of an article, the verbal presentation) can clarify features of the graph, a high quality graph should be able to be interpreted without elaboration. This should be the goal.

Principle 1 is _Show the data clearly._ This is Tufte’s maxim: “Above all else show the data” (Tufte 1983, p. 92).

**1212**

I. GORDON AND S. FINCH


Figure 1. Scatterplot of lifespan variation versus average lifespan (van Raalte et al. 2011). The original caption reads: _“Relationship between lifespan variation (SD at age 35 years) and average lifespan (conditional upon survival to age 35 years) by sex and education. All data points in Tables 1 and 2 are plotted, but some are not labeled to avoid clutter._ ” © International Epidemiological Association. Reprinted with permission from International Epidemiological Association. Permission to reuse must be obtained from the rightsholder.

Detection refers to the fundamental question of whether the important properties of the data can be detected by the visual system (Cleveland and McGill 1985, 1987). In print, the space devoted to a graph might simply be inadequate. Cleveland (1984) advised assessing how well a graph can stand reduction. A graph might be otherwise well constructed but if many of the elements of the graph overlap, individual elements may not be able to be detected. The data will not be shown clearly, and the graph fails.

Figure 1 is an example taken from a recent issue of the _International Journal of Epidemiology_ (van Raalte et al. 2011). It shows the lifespan variation (standard deviation) versus average lifespan in 10 European countries. For each country separate points are provided according to gender and education level (high, medium, or low). The authors had the challenge of representing five variables and distinguishing six groups (gender by education level) without using color. They chose to label points to draw attention to countries of interest. The data are, however, not shown clearly because clutter has not been avoided and the main patterns are not clear.

**1213**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?


Figure 2. Scatterplot with panels, which shows the data from Figure 1 clearly.

Figure 2 shows these data more clearly; our thinking in the construction of Figure 2 was as follows. We considered redesign of the original figure, keeping in mind the original authors’goal of illustrating the relationship between average lifespan and lifespan variation for different genders and education level. Hence, a scatterplot is an appropriate choice. We also chose to restrict our figure to gray scale, as the original figure has no color. The authors followed a natural approach in trying to represent groups in terms of symbols (and in other contexts, colors). However this approach fails to show the data clearly, and to allow easy identification of different countries, we introduced country panels. This choice means that the data are no longer aligned on single common _x_ and _y_ axes, but rather on multiple identical _x_ and _y_ axes. This is an example where the third principle discussed below— alignment on common scales—is not entirely maintained, to achieve clarity. The choice of symbols and gray scale colors to represent gender and education groups is challenging. Symbol intensity is increased to show higher levels of education, and two different symbols types are used to identify gender. This is a relatively complex encoding of two factors, so faint lines are added to join education levels for each gender; the purpose of this is to make the encoding of factors more transparent.

There is often more than one useful way to represent data. To illustrate this, Figure 3 shows the data of Figures 1 and 2 from a different perspective. This is a panel plot with the panels defined by gender and education level. In this plot, countries are not identified. Figure 3 shows the negative relationship between average lifespan and the standard deviation of lifespan within each combination of gender and education level. This plot clearly shows that average lifespan increases as education level increases, lifespan variation decreases as education level increases, average lifespan is longer for females than for males, and lifespan variation is greater for males than for females.

**1214**

I. GORDON AND S. FINCH


Figure 3. Alternative panel plot for the data from Figure 1. Each data point represents a country; the countries are not labeled.

Principle 2 is _Use simplicity in design._ Good graphics have a high data-to-ink ratio. Tufte argues that “Every bit of ink on a graphic requires a reason. And nearly always that reason should be that the ink presents new information” (Tufte 1983, p. 96). This is one aspect of creating a simple design.

The burgeoning field of infographics is replete with offerings for the bad graphics hobbyist where the temptation to embellish graphs is all too strong. Pictograms are also making a comeback, particularly on the Internet. Simplicity in design does not imply simplicity in data represented or that a graph should be limited to small datasets. Tufte’s (1983) work on small multiples, and recent developments in dynamic graphics (Rosling 2008) show rich data with simple designs.

Principle 3 is _Use good alignment on a common scale for quantities to be compared._ Our third and fourth principles arise from the framework developed by Cleveland and McGill (1985, 1987) for statistical graphics that integrates thinking about human perception. A graph _encodes_ quantitative and categorical information using symbols, geometry, and color. Graphical perception is the _visual decoding_ of the encoded information. An empirical study of elementary graphical-perception tasks (Cleveland and McGill 1985, 1987) showed that the most accurate decoding arose when graphical elements to be judged or compared were positioned along a common scale; next was position along identical, nonaligned scales. Figure 1 represents all data points with reference to a common scale (one for each axis) whereas Figure 2 uses position along identical, nonaligned scales. Good graphs maintain constant measurement scales, within reason. This is usually possible.

The ubiquitous pie chart does not conform to Principle 3; the human eye is bad at comparing angles. Pie charts are often presented with the percentages made explicit; this

**1215**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?

acknowledges the failure of the graphic to accurately communicate quantitative information. Stacked bar charts fail in the same way; only one category is aligned against the common scale and often the percentages are printed on the graph for clarity.

In our view, accurate decoding should support accurate estimation of the quantities represented. We do not agree with Ehrenberg’s (1978) assertion that “Graphs usually fail if they do not have a simple story-line to tell. This restricts them to communicating qualitative aspects of the data.” (p. 87) Nor with a more recent expression of the same view:

Unlike data tables, graphs are not meant to provide precise quantitative values. Graphs reveal patterns, trends, relationships and exceptions via the shape of the data that would be difficult to discern from a table of values. Grid lines are rarely needed in graphs to help readers assign accurate numeric values to the data; the approximate values that can be perceived without the aid of grid lines are almost always adequate. (Few 2005)

Following this recommendation, echoed by Bigwood and Spore (2003, p. 44), entails an unnecessary loss. A good graph can communicate the broad pattern _and_ some details of the data. Often a scatterplot with suitable grid lines can actually represent the individual observations quite precisely. Light grid lines can help guide the comparisons, and can assist with accurate estimation of the values represented by the data points.

It is perhaps unfortunate that Tufte (1983) discussed the use of grid lines in his chapter on chartjunk, as his discussion is sometimes taken as supporting the removal of grid lines. Consider this advice on graph construction: “Chartjunk consists of unnecessary and distracting elements. The most common of these are grid lines _. . ._ ” (Bigwood and Spore 2003, p. 43), and “Grid lines are commonplace in business graphs today but they are almost always chartjunk—visual content that adds no value, serves no purpose and distracts from the real data” (Few 2005).

Here are Tufte’s (1983) thoughts: “A gray grid works well and, with a delicate line, may promote more accurate data reconstruction than a dark grid” [p.116]. To Tufte, grid lines are not chartjunk; they can facilitate estimation of _quantity_ . Note how the grid lines facilitate comparisons of interest in Figure 2.

Principle 4 is _Keep the visual encoding transparent._ Building on the insight of Cleveland and McGill’s (1987) regarding visual encoding and decoding, we have suggested the principle of “transparent visual encoding” (Finch and Gordon 2014): the creator of a graph should aim to make the viewer’s task—visual decoding—as simple as possible. If possible, the decoding necessary should be transparent: the viewer should be barely aware of doing it. If it is hard work to understand and explain a graph, the visual encoding is not transparent.

There are many ways in which it can be difficult for the reader to decode a graph. Again, simplicity in design and clear labeling of the graph contribute to easier decoding. All elements of the graph must be defined; for example, bars around point estimates might be used to show a standard deviation or a standard error, or a confidence interval. This should be stated explicitly.

The practical use of the graph must be considered: color is only useful if the reader will see the graph in color. Some form of gray scale tonal variation is an alternative to color. Another option is to use different shaped symbols.

Poorly designed plots of time series data that are difficult to decode are easy to find, such as two time series shown as bars, super-imposed, leading to masking: a detection problem.

**1216**

I. GORDON AND S. FINCH

Generally, the use of bars in situations where points might be used creates unhelpful decoding complexity.

When modern graphs use two scales on the same graph, even when these are clearly identified, there is scope for confusion, or for being misled, particularly if the reader looks at the plot casually.

Cleveland and McGill’s (1985, 1987) notion of detection is important in ensuring transparent visual encoding, and in some cases ensuring that the data are detected will mean that data may need to be presented on common but nonaligned scales. In effect, this means using a panel plot. Panel plots violate Principle 3, since some of the data that we wish to compare are no longer aligned on a common linear scale, although the second best option is used, and they are sometimes the best design. This is illustrated in Figure 2.

Cleveland (1985) also discussed the role of distance in visual perception. Distance refers to the proximity of data items to be compared on the graph (other than on the measurement scale). As the distance between items to be compared increases, the accuracy with which comparisons are made decreases. The idea can be taken further: often we want to compare quantities in different graphs, and the ease with which this can be done is certainly affected by how close the two graphs are together, even if they are not lined up. On an individual graph, faint grid lines can help reduce the problem caused by distance. Ordering the quantities by magnitude, if appropriate, can also help in graphs, as it can in tables (Feinberg and Wainer 2011).

Principle 5 is _Use graphical forms consistent with Principles 1 to 4._ A set of standard and effective graphical forms can cover the majority of graphing needs, and are consistent with our first four principles. These are: histograms, dotplots, boxplots, line plots, bar or dot charts, and scatterplots. The addition of panels to extend these is often powerful and appropriate. These are the types of graphs modeled, for example, by Cleveland (1984) and Tufte (1983).

Consider the scatterplot. A symbol represents a pair of observations simultaneously, one on the _x_ -axis and one on the _y_ -axis. This is an example of encoding: it is a longestablished convention that the _x_ and _y_ values can be read off the graph by projecting onto the relevant axis: this is the decoding process. It is reasonably obvious, making it relatively transparent.

On the other hand, the rules for the boxplot are quite detailed and complicated. Users come to learn them and internalize the encoding involved. But it is not at all uncommon for a boxplot viewer to be uncertain about the way the whiskers are constructed. This is associated with wrongly constructed boxplots, or unhelpful variations.

The imperative to be creative in producing a good graph does not mean nonstandard graphical forms should be used. Accurate decoding relies on standard forms.

The five principles provide a framework for evaluation of the graphs in our study. For each principle, a set of questions about features of a graph was articulated.

## **3. OUR STUDY**

Are statisticians leaders in graphical excellence as Cleveland suggested we should be? We examined published graphs in the scientific literature drawing from highly

**1217**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?

regarded academic journals. Our focus is on this source of static graphs, arguably more important in practice than dynamic graphics. The form and structure of static graphs provide a basis for excellence in dynamic graphs where the design can be more challenging.

The Australian Research Council’s 2010 “Excellence in Research Australia” evaluation provided ordinal rankings of academic journals across all disciplines, with the best journals receiving an A<sup>∗</sup> rating. In all 1030 academic journals received this rating; this was the top 5% of journals. We expect articles published in statistics, applied science and social science journals rated A<sup>∗</sup> to be a source of quality graphics, given competition to publish in these journals and the rigorous review processes.

### **3** **_._ 1 SAMPLING AND EVALUATION**

The Australian Research Council classifies journals according to one or more field of research (FOR) codes. We identified A<sup>∗</sup> journals publishing work in statistics and allied applied science disciplines by considering the first and second FOR codes.

There were 327 A<sup>∗</sup> journals with FOR codes in the environmental sciences, agricultural and veterinary sciences, medical and health sciences, education, economics, psychology, but not statistics. We took our applied science sample from these journals. There were 17 A<sup>∗</sup> journals with a FOR code in statistics; we took our statistics sample from these journals.

We sampled from all 17 statistics A<sup>∗</sup> journals. We chose a random starting page within the most recently available issue online and sampled the first page with at least one graph starting from the randomly selected page. If necessary, we randomly sampled one of the _k_ graphs on a page. We worked through from the random starting point to the end of the issue and then started at the first page and continued back to the start point, if required. We examined the three most recent issues of each journal in this way. One journal had no graphs in the three issues we examined, and one issue of another journal had no graphs. We therefore found 47 statistics graphs.

We took a simple random sample of journals from among the 327 applied science A<sup>∗</sup> journals. A graph from a selected journal was sampled by finding the most recently available issue online. Within the chosen issue, the process was as for the statistics graphs. We sampled 55 applied science journals, and found 50 graphs; five journals had no graphs in the issue sampled. A list of the A<sup>∗</sup> applied science and statistics journals from which we sampled graphs is in Appendix A.

Over 60 different features of each graph were coded; both authors reviewed all the graphs. The coded features related to the five principles of good graphics. For the principle _Show the data clearly_ , we recorded, for example: Did the graph have detection problems? Are there undefined graphical elements? Are the axes labeled appropriately? Without direct reference to these features, each graph was also assigned an overall quality rating: poor, adequate, good, or exemplary. Any disagreements between the authors were resolved by discussion. Examples of some of the coding for two graphics in our study are given in Appendix B.

**1218**

I. GORDON AND S. FINCH


Figure 4. Quality rating of graphs sampled from A* journals in statistics ( _n_ = 47) and applied science ( _n_ = 50).

## **4. OUR FINDINGS**

### **4** **_._ 1 OVERALL QUALITY**

No graphs in our sample were rated as exemplary; 39% overall were poor, with a higher proportion in the applied science graphs than in the statistics graphs (Figure 4). Many of the features of graphs we coded were undesirable. We counted the number of undesirable features identified for each graph. Figure 5 shows dotplots of the number of undesirable features by the overall quality rating in each group. This illustrates that graphs with better overall quality ratings had fewer poor features, on average. This provides evidence of the coherence of the subjective quality ratings.


Figure 5. Number of poor features in graphs by overall quality rating and discipline.

**1219**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?


Figure 6. Percentage of graphs sampled from A* journals in statistics ( _n_ = 47) and applied science ( _n_ = 50) with various features.

The overall quality was slightly lower for the applied science graphs than for the statistics ones (Figure 5). However, fewer of the statistics graphs (13%) than applied science graphs (26%) stood alone. We also coded if the graph had an obvious statistical problem; by this we mean, something which was a violation of standard theory and practice, wrong, internally inconsistent, or impossible, from a statistical point of view. This was true for 10% of the applied science graphs and 4% of the statistics graphs. For example, one graph showed a two-dimensional “scatterplot” where the _x_ -axis was unlabeled, had no tick marks, and no apparent meaning. Another graph claimed to present quarterly data; the _x_ -axis showed yearly labels but there appeared to be variable numbers of quarters (sometimes more than four) in each year. Captions of these graphs provided no clarification.

### **4** **_._ 2 REPRESENTING DATA AND INFERENCE**

Most graphs represented data and/or estimates; see Figure 6. Only 4% of the applied science graphs represented something other than data and/or estimates, compared with one quarter of the statistics sample. Statistics graphs included more examples of fitted models and theoretical distributions.

The principles of simplicity and transparency imply that point estimates should be represented graphically as points (rather than bars). Twelve graphs, all from the applied science sample, used bars instead. This was 41% of the applied science graphs that represented estimates.

**1220**

I. GORDON AND S. FINCH

Inferential results can be encoded graphically as point estimates with “error bars” representing uncertainty; preferably the “error bars” are confidence intervals rather than standard errors (Cleveland 1985). Cleveland saw that “the difficulty _. . ._ is that we are visually locked into what is shown by the error bars; it is hard to multiply the bars visually by some constant to get a desired visual confidence interval on the graph. Another difficulty, of course, is that confidence intervals are not always based on standard errors” (p. 219).

In 13/29 (45%) of the applied science graphs with estimates, a representation of uncertainty was included; this compares with 4/20 (20%) in the statistics sample.

Only five out of the 17 graphs with “error bars” showed confidence intervals; another five did not specify the meaning of bars. Visual decoding can be challenging with bars on bars—point estimates shown as bars with “error” bars; half of the 12 applied science graphs with point estimates as bars had this feature.

In our view, inference is best represented graphically by plotting confidence intervals. There is a tradition in some disciplines of providing information relating to _p_ -values on a graph; this includes exact _p_ -values, relative _p_ -values (e.g., _p <_ 0 _._ 05), and star ratings (e.g., *, **, ***) corresponding to relative _p_ -values. Relative _p_ -values are relatively uninformative. _p_ -Values were reported in some form in 10/50 (20%) applied science graphs and one statistics graph; only three gave _p_ -values to some decimal places.

### **4** **_._ 3 WHAT WAS DONE WELL?**

Most graphs conformed to the principle of aligning elements to be compared along a common scale (78%). In 19% of graphs we judged that the data could be shown more clearly if panels were used—in some cases the use of a single common scale reduced the clarity of the data.

Cross-hatching, a source of visual noise, is now out of vogue (2% of graphs) presumably because of improvements in printing, and the use of color. Similarly use of the principle of “Anaheim first” (Feinberg and Wainer 2011) (alphabetical order) was rare; we judged only 4% of graphs could be improved with a reordering of elements.

### **4** **_._ 4 WHAT NEEDS IMPROVING?**

Many problems with the graphs related to detection—and just under half (45%) of all the graphs had detection problems. More than half (53%) the graphs had undefined abbreviations and 23% had undefined graphical elements. One example of an undefined graphical element was an interaction plot where the groups (lines) were not labeled; the reader had to infer them from the information in the body of the article. Another example is undefined “error” bars; they could be standard errors, standard deviations, or confidence intervals.

Only around one-third (35%) of the graphs provided suitable axis labels and in 14% of all graphs at least one of the axis labels referred to the variable measured rather than a point estimate relating to the variable measured. This can be ambiguous when, for example, the proportion of correct responses to a set of questions is measured for individuals and the average proportion is plotted but not clearly labeled. Ideally the tick mark labels on all axes should be horizontal—a simple instantiation of the principle of showing the data

**1221**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?

clearly. In 30% of all graphs, labels for at least one of the axes were not horizontal, a likely consequence of software defaults.

There were a number of ways in which Tufte’s principle of simplification could be adopted. One quarter of the graphs used color, but in almost half of these the use of color was redundant. A legend was provided in 42% of the graphs but in one-third of these we judged that direct labeling would have been a better option as it can reduce the amount of decoding the reader needs to do.

Only 31% of graphs used grid lines. This is likely to be partly due to software defaults. In 30% (9/30) of the graphs with grid lines, the grid lines were too heavy. We judged that some/additional grid lines could be used in 84% of all the graphs. Some examples from our sample illustrate the importance of grid lines. One graph showed a time series of estimates of proportions (on a percentage scale); the final point estimate appeared to be plotted higher on the _y_ -scale than the tick mark corresponding to 100%, and the upper bound of the confidence interval plotted around the point estimate was clearly over 100%. If the authors had added a grid to their graph, these problems would have become transparent. Another graph compared performance under two different conditions over time; under one condition the outcome was initially poor but improved over time whereas in the other condition initial performance was good but declined over time. An important question in this context is about the point of intersection of the two lines on this graph: at what time is the performance equivalent? Without grid lines, this was quite difficult to approximate.

There were 18 graphs that did not correspond to one of the recommended graphical forms; all but one came from an applied science journal. Many of the nonstandard forms plotted point estimates as bars, sometimes with error bars. We found “innovation” at its worst in the representation of a simple distribution. We have already mentioned an example where a simple distribution was represented in two dimensions—the second dimension was meaningless and unexplained. Another example showed an “empirical distribution;” it was described as a histogram but the bars plotted were not contiguous and the tick mark labels were not evenly spaced. A footnoted explanation suggested that the values on the _x_ -axis corresponded to various percentiles of the distribution. This confusing representation of a simple distribution may have been produced with naive use of an Excel histogram function.

### **4** **_._ 5 APPLIED SCIENCE DISCIPLINES VERSUS STATISTICS**

The differences between the applied science and statistics graphs based on overall quality ratings and the number of undesirable features were small. In a number of, but not all, aspects of detail, the statistics graphs appeared to be better. Figure 7 provides a caricature of graphs of estimates from an applied scientist (left panel) and a statistician (right panel), based on differences we observed between the applied science and statistics samples. The estimates plotted are the mean number of undesirable features in our study— broken down by the overall quality rating of the graph and the discipline (applied science or statistics).

The statistician sticks to a standard form (98% of statistics (S) graphs compared with 66% of applied science (AS) graphs) and avoids redundant use of color (S: 6%, AS: 16%). When graphing estimates he labels his axes appropriately (axis labeled as variable rather than parameter estimate: S: 5%, AS: 41%), but generally uses nonhorizontal tick marks

**1222**

I. GORDON AND S. FINCH


Figure 7. Caricature of graphs produced by an applied scientist (left panel) and a statistician (right panel); see the text for details.

(S: 55%, AS: 6%). The statistician’s graph of estimates uses points rather than bars (S: 100%, AS: 59%). The applied scientist presents estimates as bars and includes a representation of the uncertainty of the estimates (S: 20%, AS: 45%). In graphing estimates as bars, the applied scientist also represents uncertainty as a bar (50% AS graphs with estimates as bars).

## **5. CONCLUSIONS**

In the best academic journals in 2012, we failed to find exemplars of graphical excellence. Graphs produced by statisticians and applied scientists left much to be desired and there is no clear evidence that the graphs in (high quality) statistics journals are better than the graphs in (high quality) applied science journals.

Generally, the cost of producing excellent graphics is small and the potential benefit of statisticians providing models for their applied colleagues to follow is large. Why is there no strong connection between valued principles (Tufte’s work, e.g., has been cited thousands of times) and actual practice? Is there a failure of understanding, of practice, or of both?

In our introduction we argued that an excellent graph stands alone—it can be accurately decoded without reference to text or verbal explanations. In many of the graphs we examined, there was a communication gap as the reader is challenged to unambiguously decode details, perhaps because the person encoding the graph was too familiar with the data and its context. This may be a failure of practice and attention to detail. Here, we provide a checklist to elucidate all the important points of detail. While other checklists have been produced (e.g., Duke 2014; Government Digital Service no date), ours is explicitly related to the goal of graphical excellence, and developed from the findings of this study. Editors and reviewers, as well as authors, could make good use of this checklist. The graphs we sampled had survived the editing and review process.

This study examined graphs that authors have included in their articles. Often, however, graphs are simply omitted. This can be an important obstacle to communication, when insights of inferences or other results could be shown in a visually incisive way. In a sense, these omitted graphs are “missing values” in our study; examining this issue systematically would be a worthwhile sequel to this work.

**1223**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?

Authors of journal articles should not regard the process of graph creation as straightforward and benign. They should understand that skill and expertise are needed, and that these can be acquired. At the very least, those producing graphs should familiarize themselves with the thinking and insights of the key works of Cleveland (1985) and Tufte (1983, 1997); the simple books by Robbins (2005) and Evergreen (2014) are useful sources for novices. Wong’s (2010) book is more suitable for those in the information graphics world, including the media.

The ease of producing a graph consistent with our principles from a software default varies substantially from package to package. Many of the graphs we reviewed were plausibly produced with little effort by the encoder to change software defaults. Examples of such defaults that are not conducive to excellent graphics are the use of gray backgrounds in Minitab, the absence of grid lines in several packages (R, Minitab, SPSS), and the production of tick labels on the _y_ -axis that are not horizontal (R). There was an absence of grid lines in many graphs, for example, that appear to have been produced using standard R functions. In many software packages, it is straightforward for the user to make changes to the default graphical style. This does not, however, appear to be the statistician’s or the applied scientist’s routine practice.

Many graphical faults would disappear if software packages came with defaults that were consistent with principles of good graphics. _ggplot2_ (Wickham 2009, 2011; Chang 2012), provides an excellent model of this; for example, a background grid is the default. Statisticians who care about quality graphics should focus some of their lobbying efforts on software producers. Software tools can make the production of good graphics hard work. If our defaults look more Tufte-esque, perhaps the steps to excellence would be easier to take.

## **6. A CHECKLIST FOR GOOD GRAPHICAL PRACTICE**

How clear is your purpose in communication?

- What relationships or patterns can you identify in the graph?

- Are these the relationships or patterns you intended to represent?

- Can the viewer identify the patterns you wish to illustrate?

- Are the important comparisons you wish to show salient?

Make clarity a high priority.

- Does the graph have a clear title?

- Are the axes labeled?

- Are the units of the variables measured defined?

- Are the units of observation clear?

- Is the graph large enough?

- Would ordering groups or variables plotted improve the graph?

- Are all the graph labels horizontal?

**1224**

I. GORDON AND S. FINCH

- Use points to plot estimates (e.g., means, proportions) rather than bars.

Choose standard forms fit for your purpose.

- Use bars around points to indicate the precision of the estimates.

- Plot the estimates of interest (e.g., mean differences with confidence intervals) rather than standard summary statistics (group means).

- Plot inferences to support stories about models.

- Plot data to support stories about distributions and variation.

Consider detection issues.

- Can all the data points be seen?

- Are patterns in the data clear?

- Are the fonts large enough?

- Would it help to use jittering, or another form of representing multiple, identical values?

Would panels help?

- Are there grouping variables that can be used to panel the graph?

- Do the grouping variables correspond to the variation of interest?

- Would additional panels help?

Align quantities to be compared on a common scale.

- Has distortion of the data been avoided by using the same scales for the same measurement?

- Are measurements made on the same scale plotted on the same scale?

- Would transposition improve the graph?

Does the graph have grid lines?

- Light gray grid lines will help with accurate interpretation.

Are all the elements of the graph defined?

- What do points on the graph correspond to?

- Are estimates (e.g., means, proportions) plotted on the graph clearly defined?

- Are bars around points on the graph clearly defined?

How much decoding work does the viewer have to do?

- Is it easy for someone unfamiliar with your data to interpret your graph?

**1225**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?

- Does the graph stand alone?

- Try it on a friend!

## **APPENDIX A: JOURNALS IN OUR SAMPLE**

#### **Applied science journals**

Advances in Agronomy American Journal of Transplantation Annual Review of Neuroscience Arthritis and Rheumatism Behavioral and Brain Sciences Brain Cell Metabolism Cochrane Database of Systematic Reviews Cognition Cognitive Science Diabetes Educational Administration Quarterly Educational Researcher Endocrine Reviews Environment International Fish and Fisheries Health Psychology IEEE Transactions on Evolutionary Computation IEEE Transactions on Image Processing IEEE Transactions on Information Technology in Biomedicine Immunity Indoor Air: international journal of indoor air quality and climate International Endodontic Journal International Journal for Parasitology Investigative Ophthalmology and Visual Science JAMA: Journal of the American Medical Association Journal of Abnormal Psychology Journal of Accounting and Economics Journal of Biomechanics Journal of Bone and Joint Surgery-American Volume Journal of Cognitive Neuroscience Journal of Educational Psychology Journal of Endodontics Journal of Experimental Psychology: Animal Behavior Processes Journal of Experimental Psychology: General Journal of Law Economics and Organization Journal of Phonetics Journal of Political Economy

**1226**

I. GORDON AND S. FINCH

Journal of Thrombosis and Haemostasis Lancet Oncology Midwifery Molecular Nutrition and Food Research Molecular Pharmacology Morphology Psychological Science Sports Medicine The Economic Journal The Linguistic Review The Review of Financial Studies Trends in Ecology and Evolution **Statistics journals** Annals of Applied Probability Annals of Applied Statistics Annals of Probability Annals of Statistics Bioinformatics Biometrics Biometrika Biostatistics Epidemiology International Journal of Epidemiology Journal of Business and Economic Statistics Journal of Computational and Graphical Statistics Journal of the American Statistical Association Journal of the Royal Statistical Society Series A (Statistics in Society) Journal of the Royal Statistical Society Series B (Statistical Methodology) Probability Theory and Related Fields<sup>∗</sup> Statistics in Medicine

∗This journal was eligible according to the study protocol, but no graphs were found in the issues sampled.

An Excel file containing exact references to the 97 plots assessed in this study is available from the authors on request.

## **APPENDIX B: EXAMPLE OF CODING IN OUR STUDY**

The coding of some of the features of graphs is illustrated in the table below, for two graphs in our study.

The first is Figure 2 from “More variation in lifespan in lower educated groups: evidence from 10 European countries” ( _International Journal of Epidemiology_ (2011), 40, 1703–1717, used with permission). This graph is Figure 1 in the main part of this article.

The second graph is Figure 1 from “A survival analysis approach to modeling human fecundity” ( _Biostatistics_ (2012), 13, 4–17, used with permission). This is shown below.

**1227**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?


Figure 1. Plot of _λ_<sup>(</sup><sup>_k_)</sup> ( _j_ ) for the New York State Angler Prospective Pregnancy Cohort Study for an average-age nonsmoking couple by parity for (a) cycle 1, (b) cycle 2, (c) cycle 3, and (d) cycle 4. © Oxford University Press. Reprinted with permission from Oxford University Press. Permission to reuse must be obtained from the rightsholder.

Example of some coding for the figures shown

|Scatterplot, first graph|Line plot, second graph|
|---|---|
|Adequate caption|Inadequate caption|
|Suitable axis label(s)|Poor axis label(s)|
|Detection problems|No detection problems|
|Undefined graphical elements|Undefined graphical elements|
|Graph does not stand alone|Graph does not stand alone|
|Elements to be compared are aligned|Elements to be compared are aligned|
|Gridlines could be added|Gridlines could be added|
|Graph is a standard form|Graph is a standard form|
|Panels could be used|No additional panels needed|
|Summary statistics/estimates shown|Summary statistics/estimates shown|
|Uncertainty on estimates not shown|Uncertainty on estimates not shown|
|No obvious statistical problem|No obvious statistical problem|
|Overall rating: Adequate|Overall rating: Poor|


_[Received August 2013. Revised November 2014.]_

**1228**

I. GORDON AND S. FINCH

## **REFERENCES**

- Bigwood, S., and Spore, M. (2003), _Presenting Numbers, Tables, and Charts_ , New York: Oxford University Press. [1215]

- Chang, W. (2012), _R Graphics Cookbook_ , Sebastopol, CA: O’Reilly Media, Inc. [1223]

- Cleveland, W. (1984), “Graphs in Scientific Publications,” _The American Statistician_ , 38, 261–269. [1210,1211,1216]

- ——— (1985), _The Elements of Graphing Data_ , New York: Chapman and Hall. [1210,1216,1220,1223]

- Cleveland, W., and McGill, R. (1985), “Graphical Perception and Graphical Methods for Analyzing Scientific Data,” _Science_ , 229, 828–833. [1212,1214,1216]

- ——— (1987), “Graphical Perception: The Visual Decoding of Quantitative Information on Graphical Displays,” _Journal of the Royal Statistical Society,_ Series A, 150, 192–229. [1212,1214,1215,1216]

- Cook, A. R., and Teo, S. W. (2011), “The Communicability of Graphical Alternatives to Tabular Displays of Statistical Simulation Studies,” _PloS One_ , 6, e27974. [1211]

- Duke, S. (2014), “Best Practices Recommendations,” available at _https://www.ctspedia.org/do/view/ CTSpedia/BestPractices_ . [1222]

- Ehrenberg, A. S. C. (1978), “Graphs or Tables?” _The Statistician_ , 27, 87–96. [1215]

- Evergreen, S. D. (2014), _Presenting Data Effectively: Communicating Your Findings for Maximum Impact_ , Thousand Oaks, CA: SAGE Publications. [1223]

- Feinberg, R. A., and Wainer, H. (2011), “Extracting Sunbeams From Cucumbers,” _Journal of Computational and Graphical Statistics_ , 20, 793–810. [1211,1216,1220]

- Few, S. (2005), “Grid Lines in Graphs are Rarely Useful,” available at _http://www.perceptualedge.com/ articles/dmreview/grid_lines.pdf_ . [1215]

- Finch, S., and Gordon, I. (2014), “The Development of a First Course in Statistical Literacy for Undergraduates,” in _Topics from Australian Conferences on Teaching Statistics_ , eds. H. MacGillivray, M. A. Martin, and B. Phillips, New York: Springer, pp. 73–98. [1215]

- Friendly, M., and Denis, D. J. (2014), “Milestones in the History of Thematic Cartography, Statistical Graphics, and Data Visualization,” available at _http://datavis.ca/milestones//_ . [1210]

- Friendly, M., and Kwan, E. (2011), Comment on “Why Tables are Really Much Better Than Graphs” by A. Gelman, _Journal of Computational and Graphical Statistics_ , 20, 18–27. [1211]

- Gelman, A. (2011), “Why Tables are Really Much Better Than Graphs” (with discussion), _Journal of Computational and Graphical Statistics_ , 20, 3–7. [1210,1211]

- Gelman, A., Pasarica, C., and Dodhia, R. (2002), “Let’s Practice What We Preach: Turning Tables Into Graphs,” _American Statistician_ , 56, 121–130. [1211]

- Gelman, A., and Unwin, A. (2013), “Infovis and Statistical Graphics: Different Goals, Different Looks,” _Journal of Computational and Graphical Statistics_ , 22, 2–28. [1211]

- Government Digital Service (no date), “Data Visualisation: Creating Valuable and Meaningful Graphics to Help Analyse Data,” available at _http://www.gov.uk/service-manual/user-centred-design/data-visualisation.html_ . [1222]

- Haemer, K. W. (1947a), “Hold that Line,” _The American Statistician_ , 1, 25. [1211]

- ——— (1947b), “The Perils of Perspective,” _The American Statistician_ , 1, 19. [1211]

- ——— (1948a), “Double Scales are Dangerous,” _The American Statistician_ , 2, 24. [1211]

- ——— (1948b), “Question 9: Negative Numbers and Semilog Paper,” _The American Statistician_ , 2, 18. [1211]

- ——— (1948c), “Range-Bar Charts,” _The American Statistician_ , 2, 23. [1211]

- ——— (1949a), “Presentation Problems: Area Bias in Map Presentation,” _The American Statistician_ , 3, 19. [1211]

- ——— (1949b), “Presentation Problems: The Supplementary-Scale Chart: Two Charts for the Price of One,” _The American Statistician_ , 3, 11. [1211]

**1229**

STATISTICIAN HEAL THYSELF: HAVE WE LOST THE PLOT?

——— (1949c), “Question 23: Graphic Presentation,” _The American Statistician_ , 3, 10. [1211]

- ——— (1950a), “Presentation Problems: A Simplified Ranking Chart,” _The American Statistician_ , 4, 21. [1211]

- ——— (1950b), “Presentation Problems: Color in Chart Presentation,” _The American Statistician_ , 4, 20. [1211]

- ——— (1951), “The Pseudo Third Dimension,” _The American Statistician_ , 5, 28. [1211]

- Kastellec, J. P., and Leoni, E. L. (2007), “Using Graphs Instead of Tables in Political Science,” _Perspectives on Politics_ , 5, 755–771. [1211]

- Robbins, N. B. (2005), _Creating More Effective Graphs_ , Hoboken, NJ: Wiley-Interscience. [1223]

Rosling, H. (2008), “Gapminder,” available at _http://www.gapminder.org/_ . [1214]

- Tufte, E. R. (1983), _The Visual Display of Quantitative Information_ , Cheshire, CT: Graphics Press. [1210,1211,1214,1215,1216,1223]

——— (1997), _Visual Explanations_ , Cheshire, CT: Graphics Press. [1223]

- Tukey, J. W. (1972), “Some Graphic and Semigraphic Displays,” in _Statistical Papers in Honor of George W. Snedecor_ , ed. T. Bancroft, Iowa: Iowa State University Press, pp. 293–316. [1210]

- ——— (1977), _Exploratory Data Analysis_ , Reading, MA: Addison-Wesley. [1210]

- van Raalte, A., Kunst, A., Deboosere, P., Leinsalu, M., Lundberg, O., Martikainen, P., Strand, B., Artnik, B., Wojtyniak, B., and Mackenbach, J. (2011), “More Variation in Lifespan in Lower Educated Groups: Evidence from 10 European Countries,” _International Journal of Epidemiology_ , 40, 1703–1714. [1212]

- Wainer, H. (1984), “How to Display Data Badly,” _The American Statistician_ , 38, 137–147. [1210]

- Wickham, H. (2009), _ggplot2: Elegant Graphics for Data Analysis_ , New York: Springer. [1223]

- ——— (2011), “ggplot2,” _Wiley Interdisciplinary Reviews: Computational Statistics_ , 3, 180–185. [1223]

- ——— (2013), “Graphical Criticism: Some Historical Notes,” _Journal of Computational and Graphical Statistics_ , 22, 38–44. [1210]

- Wong, D. (2010), _The Wall Street Journal Guide to Information Graphics: The Dos and Don’ts of Presenting Data, Facts and Figures_ , New York: Norton and Company. [1223]

---

[← Statistician Heal Thyself: Have We Lost the Plot?](01-statistician-heal-thyself-have-we-lost-the-plot.md) · [Up: contents](index.md)
