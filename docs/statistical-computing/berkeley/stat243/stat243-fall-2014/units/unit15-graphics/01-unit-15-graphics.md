---
title: 'Unit 15: Graphics'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit15-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit15-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 15: Graphics

**Source:** [`units/unit15-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit15-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

November 25, 2014

This unit first discusses some general concepts and principles of graphics relevant more broadly than R, and then provides implementation details for graphics in R.

References:

- Adler

- Chambers

- Venables and Ripley, Modern Applied Statistics with S

- Murrell, R Graphics (available electronically through OskiCat: http://uclibs.org/PID/110697)

- R intro manual (R-intro) on CRAN

- There is a nice overview on creating good graphics in R at http://teachpress.environmentalinformaticsmarburg.de/2013/07/creating-publication-quality-graphs-in-r-7

R has several general graphics packages: _graphics_ , _grid_ , _lattice_ , and _ggplot2_ . _graphics_ is the original graphics package. _grid_ is more object-oriented, and is quite powerful and useful if you’re involved in serious graphics programming. _lattice_ and _ggplot2_ are more recent packages that use _grid_ to provide the user with high-level graphics capabilities. More details on _grid_ can be found in Murrell’s _R Graphics_ and more details on _ggplot2_ can be found in Hadley Wickham’s _ggplot2: Elegant Graphics for Data Analysis._

### **1 Good practices for graphics**

There are a number of principles that can be used in developing and critiquing graphics. But first let’s see some examples that show those principles being violated.

1

#### **1.1 Some example graphics**

1. The file _shell.pdf_ in the repository has an example of a crazy pie chart from the NY Times from a week ago.

2. In Figure 1, you can see a graph that we’ll discuss in class. What aspects of the graph could be improved? What aspects do you like?

3. The article _wainer1984.pdf_ in the repository is rather old but the ideas are still relevant and while the example figures are dated in terms of appearance, the same issues arise with more modern-looking graphics.

4. The article _gelmanUnwin2013.pdf_ in the repository presents a modern-day reinterpretation of a famous graphic from Florence Nightingale regarding causes of death in the British Army during the Crimean War in the 1850s.

#### **1.2 Best practices**

Here’s a list of some guidelines to consider in creating graphics.

1. Have a high density of information to space

2. Avoid 3-d graphics unless they truly add information

3. Strategies for going beyond two dimensions

   - (a) Use color, but avoid if unnecessary (saves printing costs in journal articles)

   - (b) Use varying symbol or line types

   - (c) Use multiple panel plots

4. Avoid stacked barplots (see demo code) as it’s hard to assess anything except the total and the baseline category.

5. Studies indicate that humans have a hard time comparing areas, volumes, or angles, so try to avoid plots that represent data using any of these, including pie charts. Instead use position or length (horizontal is better than vertical) to display data values

6. Label axes

7. Keep the range of axes (and other features) the same for multiple panels, when possible

8. Use a legend where appropriate

2


_Figure 1. Example graphic indicated in Section 1.1, item #2.._

3

9. Use vector graphics formats such as PDF or Postscript/EPS as these scale without pixelation when resized. Raster formats such as JPEG, PNG, BMP, TIFF don’t rescale well and when they have high resolution also have large file sizes. See Section 6.

Rob Hyndman has a list of 20 rules for good graphics, including some of the ones above.

### **2 Base R graphics (the** **_graphics_ package)**

The material here mainly gives high-level information and information on adjusting your graphics, rather than telling you how to make particular plots using R’s base graphics. The _graphicsCommands.pdf_ file in the github repository and Chapter 14 of Adler provide information about many of the core plotting functions. These include high-level functions such as _plot()_ , _matplot()_ , _pairs()_ , _coplot()_ , _hist()_ , _density()_ , and _boxplot()_ , as well as low-level functions for adding information to a plot such as _lines()_ , _points()_ , _abline()_ . Adler goes into great detail on many of these, both in the context of the _graphics_ package and that of the _lattice_ package.

#### **2.1 Background**

The basic components of R base graphics are

1. high-level functions (e.g., _plot()_ , _boxplot()_ , etc.) for producing an entire plot

2. low-level functions for adding components to existing plots. The ability to build up a complicated plot piecewise is one of the strengths of R’s graphics. These low-level functions include _abline()_ , _arrows()_ , _axis()_ , _legend()_ , _lines()_ , _points()_ , _rug()_ , _text()_ , _mtext(), title()_ , _symbols()_ .

3. graphics parameters controlled through (1) _par()_ or (2) as arguments to a graphics function call. These parameters change the appearance of a plot or plots (e.g., _mai_ , _pch_ , _col_ )

R graphics work by sequentially plotting graphics elements, so subsequent items may paint over initial elements. One technique when this is an issue is making your colors transparent - see the color subsection below.

Note that as we saw when talking about OOP, the core _plot()_ function does both scatterplots and is a generic method used for plotting a wide variety of objects, e.g., _plot.lm()_ .

I won’t say much about the high-level and low-level functions, but a wide range of these exist. In particular low-level functions allow you to add almost anything you might want to add: arbitrary lines, polygons, symbols, text, arrows, boundary lines in maps, etc.

4

#### **2.2 Graphics parameters**

We can set graphics parameters through various plotting functions (for temporary changes applying only to the current plotting command) or through the _par()_ function (for a permanent change), allowing us to customize the layout or appearance of a plot. Let’s take a look at some of these and what they mean.

Most of you know how to create a multi-panel plot:

**<mark>par</mark>** <mark>(mfrow=</mark> **<mark>c</mark>** <mark>(4, 2))</mark> _<mark># 4 rows, 2 columns of subplots</mark>_

Changing the margin sizes (and axis information spacing) is one of the most common modifications one needs to do, particularly when producing a multi-panel plot and when creating an output file. One often wants to reduce the size of the inner margins. This helps maximize the information to white space and increase the resolution of your plot. Sometimes one needs extra space in the outer margin of a multi-panel plot. Positioning and lengths within the graphics window can occur with relative units; i.e., the device domain is (0 _,_ 1) _×_ (0 _,_ 1), or in physical units (commonly inches), or in “lines” of text. Some values I commonly use are

**par** (mai = **c** (.5, .5, .1, .1)) _# manipulate inner margins of subplots_ **par** (mgp = **c** (1.8, .7, 0)) _# manipulate spacing of axis ticks, labels, text_ **par** (omi = **c** (0, 0, .3, 0)) _# manipulate outer margin of full plot_

Here for the margins, the first number is the bottom, the next the left, the third the top, and the fourth the right margin, so with _omi_ , I’ve made some space (0.3 inches) in the outer margin at the top.

Note that if you change graphics options using _par()_ (including within a function call!), the values change permanently (so it’s like pass by reference). One way to be able to go back is

oldpar = **par** (no.readonly = TRUE) **par** (cex = 3); **plot** (x, y) **par** (oldpar); **plot** (x, y)

So if you create a function that changes the graphics parameters, you should use the above strategy to reset so you don’t surprise your users.

Here are the various layout parameters and their units: _din_ (device size, inches), _pin_ (plot size, inches), _fin_ (figure size, inches), _mai_ (margin size, inches) or _mar_ (margin size, lines), _omi_ (outer margin, inches) or _oma_ (outer margin, lines), _mex_ (# text lines per interline spacing), and _plt_ (plot region as fraction of figure region). _cex_ controls size of points and text in general when called

5

through _par()_ , but only controls the size of points when called within a plotting function, while _cex.lab_ , _cex.axis_ , and _cex.main_ control the size of axis labels, axis values, and the title. Similarly for _col_ , _col.lab_ , _col.axis_ and _col.main_ .

Here are some other things you can control: text justification ( _adj_ ), font size ( _cex_ , _csi_ ), font type ( _font_ ), rotation of text ( _srt_ ), color ( _col_ ), line type ( _lty_ ), line width ( _lwd_ ), plotting character symbol ( _pch_ ), type/presence of boundary box ( _bty_ ), log-scale axes ( _log_ ), axis labels ( _{x,y}lab_ ), axis limits ( _{x,y}lim_ ), a variety of details about the axis limits, labels, and ticks ( _lab_ , _las_ , _tck_ , _{x,y}axp_ , _{x,y}axs_ , _{x,y}axt_ ), and whether to plot axes ( _axes_ ).

**Some additional tidbits** You can force subplots to have the same axis ranges by manipulating _xlim_ and _ylim_ .

It can be handy to put axis labels in the outer margin of a multi-panel plot:

x = **rnorm** (10); y = **rnorm** (10); **par** (mfrow = **c** (2, 2)) **for** (i **in** 1:4) **plot** (x, y, xlab = '', ylab = '') **mtext** ("my x variable", 1, line = -1, outer = TRUE) **mtext** ("my y variable", 2, line = -1, outer = TRUE)

Note if we wanted to put the label further towards the edge of the plot, we’d need to use _omi_ or _oma_ to create an outer margin, and then we could use a value of _line_ that is greater than -1 to put the text further away from the plotting regions.

You can create multi-line text by just using “ _\n_ ” in your character string.

To plot outside the plot region, set xpd = TRUE - otherwise anything outside the region is “clipped”.

#### **2.3 Adding information to a plot sequentially**

There are lots of low-level functions you can use to add components to a plot. These include _abline()_ , _arrows()_ , _axis()_ , _legend()_ , _lines()_ , _points()_ , _rug()_ , _text()_ , _mtext(), title()_ , _symbols()_ , _hline()_ , _vline()_ . A basic strategy for customizing components of a plot is to use the high-level function to plot the basics, specifying parameter arguments that leave out some components (e.g., xaxt = ’n’, bty = ’n **’,** xlab = **”** ). At its most extreme, you can create the structure of a plot without plotting any data for customizing everything:

**<mark>plot</mark>** <mark>(x, y, type= 'n')</mark>

With _title()_ , you can add main and subtitles and axis labels, as we saw in the demo code for the previous subsection. This gives you control over positioning using the _line_ and _outer_ arguments.

6

_rug()_ will add tick marks for each observation along a chosen axis. _locator()_ allows you to choose a location for certain items (e.g., a legend) with your mouse.

You an create custom axes with the _axis()_ function, adding the axis, ticks, and axis value labels. Here’s an example of plotting two sets of data with different axis values. It also shows the use of the new argument to overplot on an existing plot. Often one would initially exclude (some) axes and a boundary box from the plot:

x = **rnorm** (10); y = **rnorm** (10); z = **rnorm** (10, 0, 5) **plot** (x, y, yaxt = 'n', bty = 'n', col = 'blue') **box** () _# add box in black_ **axis** (side = 2, col = 'blue') _# add y-axis, but in blue_

**par** (new = TRUE) _# this tells R to overplot the next plot on the current_ **plot** (x, z, col = 'red', bty = 'n', ann = FALSE, xaxt = 'n', yaxt = 'n') **axis** (side = 4, col = 'red') _# add right-side y axis_


<!-- Start of picture text -->
GG<br>G GG<br>G G<br>G G G<br>G<br>G<br>G G<br>G<br>G G<br>G<br>GG<br>−1 0 1 2<br>x<br>1.0 2<br>0.5 0<br>y<br>0.0<br>−2<br>−4<br>−1.0<br>−6<br><!-- End of picture text -->

**Adding an additional dimension** Let’s consider other ways to pack information on another dimension into a plot:

7

**par** (mfrow = **c** (1,2)) groups = **sample** (1:3, 10, replace = TRUE) _# simulated strata_ **plot** (x, y, col = groups) **plot** (x, y, pch = groups)


<!-- Start of picture text -->
G<br>G<br>G<br>G G<br>G G G<br>G<br>G<br>G<br>−1 0 1 2 −1 0 1 2<br>x x<br>1.0 1.0<br>y y<br>0.0 0.0<br>−1.0 −1.0<br><!-- End of picture text -->

You can also use this approach with different line widths ( _lwd_ ) and line styles/types ( _lty_ ) when that is relevant.

#### **2.4 Interacting with graphics**

R is not well set up for interactive work, but one handy function is _identify()_ , which is handy for both identifying points (such as outliers) and marking a specific point.

**plot** (x, y) **identify** (x, y) _# now left-click on individual points and # R will tell you the index of the point_

If you want to do more with interactive graphics (which can be very helpful for high dimensional data), check out the _GGobi_ software.

#### **2.5 Using mathematical expressions in plots**

We can use Greek letters and mathematical symbols in labels using _expression()_ to enclose the mathematical expression and paste() to combine elements _._

8

**par** (mai = **c** (1, 1, .1, .1))

**plot** (x, y, xlab = **expression** (lambda),

ylab = **expression** ( **paste** (E[lambda]^(2-Lambda), "(deviance)-", **Var** (phi) )))


<!-- Start of picture text -->
G<br>G<br>G<br>G G<br>G G<br>G<br>G<br>G<br>−1 0 1 2<br>λ<br>1.0<br>0.5<br>0.0<br>−0.5<br>()2−Λ()(deviance)−Varφ<br>Eλ<br>−1.0<br><!-- End of picture text -->

Here’s an example of using a variable within an expression. This is quite powerful if you are producing multiple plots and the text changes for each plot:

**plot** (1:10, type='n', xlab='', ylab='', main = "plot math & numbers") theta <- 1.23

**mtext** ( **bquote** ( **hat** (theta) == **.** (theta)), side = 3, line= 0.25) _# alternative:_

**mtext** ( **substitute** ( **paste** ('Estimate: ', **hat** (theta) == thetaVal), **list** (thetaVal = theta)), side = 1, line= 2)

9

#### **plot math & numbers**


<!-- Start of picture text -->
θ ^ = 1.23<br>2 4 6 8 10<br>Estimate: θ ^ = 1.23<br>8<br>6<br>4<br>2<br><!-- End of picture text -->

_bquote()_ treats its argument as an R language object but substitutes in for terms wrapped in “ _.()_ ”, behaving somewhat like _substitute()_ . An alternative approach uses _substitute()_ :

For a full set of mathematical syntax and examples of such substitutions, see ?plotmath as well as example(plotmath) and demo(plotmath).

For plotting text, it’s helpful to keep in mind that we can choose a display of text based on the encoding of the characters and a font in which to display the characters. So if you need characters not in the standard Latin character scheme, it should be doable by choosing a different encoding.

#### **2.6 Laying out panels (subplots)**

We can create more complicated arrangements of panels than the rectangular layout of _mfrow_ and _mfcol_ .

One approach is use _layout()_ . Here we give it a matrix with as many rows and columns as we want in the plot and assign values, 1, 2, ... to the appropriate rows and columns of the matrix, with the values serving to identify each panel.

**layout** ( **matrix** ( **c** (1, 1, 0, 2), nr = 2, byrow = TRUE)) **layout.show** (n = 2) **layout** ( **matrix** ( **c** (1, 1, 1, 1, 4, 3, 2, 2), nr = 2, byrow = TRUE)) **layout.show** (n = 4)

Let’s see the example from ?layout, which slickly plots a scatterplot with marginal histograms.

10

We can use _split.screen()_ as an alternative to _layout()_ . Here’s a basic example that allows us to choose which panel to plot in:

**split.screen** (figs = **c** (2, 3)) **screen** (3) **plot** (x, y) **hist** (x) _# so we need to change screens manually_

_split.screen()_ can be used with a 4-column matrix where each row indicates the xrange and yrange _(xl, xu, yl, yu)_ of the given subplot where _xl_ and _xu_ are the lower and upper x-axis values and _yl_ and _yu_ for the y-axis values. The values should all be in between 0 and 1. Note that overplotting is possible.

**split.screen** (figs = **matrix** ( **c** (0, .4, 0, .5, .7, 1, .7, 1, .7, 1, .4, .7, .2, 1, 0, .4, 0, .4, .7, 1), nc = 4, byrow = TRUE)) ## [1] 1 2 3 4 5 **screen** (1); **plot** (x, y); **screen** (2); **hist** (x); **screen** (3); **hist** (y); **screen** (4); **plot** (1: **length** (x), x, type = 'l') **screen** (5) **split.screen** (figs = **matrix** ( **c** (0, .5, 0, 1, .5, 1, 0, 1), nr = 2, byrow = TRUE)) ## [1] 6 7 _# you can continue subdividing, but need to be careful # that the margins don't get too big for the remaining # space (and that text is not too large)_ **screen** (6); **par** (mai = **c** (.05, .05, .05, .05), cex = .7); **hist** (x); **screen** (7); **par** (mai = **c** (.05, .05, .05, .05), cex = .7); **hist** (y)

11


<!-- Start of picture text -->
Histogram of x Histogram of y<br>Histogram of x<br>−2 0 2<br>x<br>−2 −1 0 1 2 3 −1.5 −0.5 0.5 1.5<br>Histogram of y<br>−1.5 0.5<br>y<br>G<br>G<br>G<br>G G<br>G G<br>G<br>G<br>G<br>−1 0 1 2 2 4 6 8 10<br>x 1:length(x)<br>5<br>4<br>3 4<br>0<br>2<br>Frequency<br>1<br>0<br>5<br>0<br>Frequency<br>1.0<br>2<br>y<br>0.0<br>1<br>x<br>−1.0 −1<br><!-- End of picture text -->

**<mark>close.screen</mark>** <mark>(all = TRUE)</mark>

In the _grid_ package, positioning subpanels is done via _viewports_ .

#### **2.7 Plotting in three dimensions and mapping**

In general for plotting _z ~ x + y_ , either in an actual spatial setting or as a function of two variables, I prefer the _image()_ function ( _levelplot()_ in lattice), which uses color to represent different levels. _image.plot()_ from the fields package nicely adds a color bar legend. _contour()_ and _persp()_ are other options but I personally find them less informative most of the time: _contour()_ because it requires

12

the viewer to read the contour line values and _persp()_ because some of the features often hide other features.

n = 20; xs = ys = 1:n; gr = **expand.grid** (xs, ys); U = **chol** ( **exp** (- **rdist** (gr)/6)) **image.plot** (1:n, 1:n, **matrix** ( **crossprod** (U, **rnorm** (n^2)), n, n), col = **tim.colors** (32))

If you do want to make a 3-d plot of a surface, _persp()_ will do it, with x, y, z arguments similar to _image()_ and also having arguments for the angle of view (the rotation around the z-axis – _theta_ ) and the viewing angle (up or down – _phi_ ). You may be able to choose a set of angles that show the surface with the least amount of hidden material. See the demo code for using _image()_ , _contour()_ , and _persp()_ to show topography in a mapping context.

R has a lot of tools for mapping in a variety of packages. In particular you can import standard GIS shape files and overlay boundaries on a map using the _spdep_ package. R also has state and national boundaries as part of the _maps_ package (see the demo code for more examples). If you like _ggplot2_ (see the next section), check out Hadley Wickham’s _ggmap_ package.

**plot** (x, y) **map** ('state', add = TRUE) _# adds state boundaries_

If you’re using color in maps, _RColorBrewer_ package is good for choosing colors for unordered levels, sequential ordering, and two-way diverging color ordering (see ?display.brewer.all) and the _ColorBrewer_ website provides recommendations.

### **3 Lattice and ggplot2**

Here we’ll see some of the main kinds of graphs, contrasting the syntax in _lattice_ and _ggplot2_ .

The _lattice_ package provides an alternative set of graphics functions based on the Trellis graphics system. _ggplot2_ is another popular alternative developed by Hadley Wickham. In both packages, the style is prescriptive, which in some cases is good (think _L_<sup>_A_</sup> _TEX_ vs. _Microsoft Word_ ). Both packages are well set up for dealing with conditioning either through sets of panels or through grouping by color or symbol. In the case of multi-panel plots, the style exploits the inter-relatedness of the information, with ’strips’ giving labelling information, and avoidance of repetition of axis information.

Here are the basic relationships amongst variables that we can represent graphically:

• _y_ # distribution of y

13

- _y ~ x_ # relationship between x and y, considering y as a function of x

- _y ~ x | A_ # relationship between x and y conditional on the values of A

- _y ~ x | A * B_ # relationship between x and y conditional on combinations of A and B

- _z ~ x * y_ # 3D relationship between x, y, and z, with z a function of x and y

Let’s see the two packages in action. We’ll use the _Comparative Political Data Set_ , which contains data on some political/economic variables for some of the industrialized countries. In the data file, _vturn_ is voter turnout, _realgdpgr_ is growth in GDP (the size of the country’s economy), _outlays_ is government spending as a percentage of GDP, and _unemp_ is the unemployment rate. Metadata are available at

http://www.ipw.unibe.ch/content/team/klaus_armingeon/comparative_political_data_sets/index_eng.html.

Both _lattice_ and _ggplot2_ work by adding layers to a base plot. In both cases, you produce an object with multiple layers and then a _print()_ method applied to the object produces the plot.

#### **3.1 Comparing** **_lattice_ and** **_ggplot2_ by example**

##### **3.1.1 Basic intro to** **_ggplot2_**

Here’s a schematic of the _ggplot_ syntax::

ggplot(data= , aes(x= ,y= , [options]))+geom_xxxx()+...+...+... The variables are part of the “aesthetic” argument. You can see the layering effect by comparing the same graph with different colors for each layer

**library** (ggplot2)

cpds <- **read.csv** ('../data/cpds.csv') usa <- cpds[cpds$country == "USA", ] **ggplot** (data = usa, **aes** (x = year, y = vturn)) + **geom_point** (color = "black") + **geom_point** (data = usa, **aes** (x = year, y = outlays), color = "red")

14


<!-- Start of picture text -->
GG<br>60 GG<br>GG<br>GG GG<br>GG<br>GG GG GG<br>50 GG GG<br>GG<br>GG<br>GG<br>GG GG<br>GG<br>GG<br>40 G<br>G<br>GG G GG GG<br>G G GGG G G G GG GG GGGGG GG GGGG GG GGG G GG G GGG GGG<br>G G G G GGG<br>G G G G<br>30 GG G GGGG<br>1960 1970 1980 1990 2000 2010<br>year<br>vturn<br><!-- End of picture text -->

Here’s another example where we layer on a bunch of features and create two versions of the plot as different objects. This also shows how to create a multipanel plot in _ggplot2_ .

**require** (gridExtra, quietly=TRUE)

dat <- **data.frame** (treatment = **c** ('control', '1x', '2x'),

mean = **c** (1.3, 1.7, 1.9), se = **c** (.2, .13, .11))

fig1 <- **ggplot** (dat, **aes** (x = treatment, y = mean)) +

**geom_bar** (position = **position_dodge** (), stat="identity", fill="grey") +

**geom_errorbar** ( **aes** (ymin=mean-2*se, ymax=mean+2*se), width = 0.25) + **ggtitle** ("Bar plot with 95% confidence intervals") _# plot title_ fig2 <- fig1 +

**theme_bw** () + _# remove grey background (because Tufte said so)_ **theme** (panel.grid.major = **element_blank** ()) _# remove x and y major grid lines (because Tufte said so)_ **grid.arrange** (fig1, fig2, nrow = 1, ncol = 2)

15

#### Bar plot with 95% confidence intervalsBar plot with 95% confidence inter


<!-- Start of picture text -->
Bar plot with 95% confidence intervalsBar plot with 95% confidence inter<br>2.0 2.0<br>1.5 1.5<br>1.0 1.0<br>0.5 0.5<br>0.0 0.0<br>1x 2x control 1x 2x control<br>treatment treatment<br>mean mean<br><!-- End of picture text -->

Here’s a bit more syntax for modifying labels and axis limits and what-not.

**ggplot** (data = cpds, **aes** (x = year, y = vturn)) + **geom_point** () + **xlab** (label = "The X Label") + **ylab** (label = "The Y Lab") + **xlim** (1980, 1989) + **ggtitle** (label = "The Title")

##### **3.1.2 Density plots**

**<mark>densityplot</mark>** <mark>(~vturn, data = cpds, xlab = 'voter turnout')</mark>

16


<!-- Start of picture text -->
0.03<br>0.02<br>0.01<br>0.00 G G GG GGGG G G GG GG G G G GG G G G G G GG G G GG GGGG GGG G GG G G G G G G G GG G GG G G G G G GGG GG GGG G GG G G G GGGGG G GGGGG G G G G G G GGGGGGGGG G G GG G G GG G G G G G G G G G G G G G G G GGGGGG G G G GG GGGG G GGGGG G GGG GG G GG GG GG GG G G G G GGGGGGGGGGGGGGGGGG G GGGGGGGGG G G GGG G G G G G GGGGGG G GGG G GGG G GG G GGGGGGGGG GGG GG G GG GG GG G GGG G GGGGGGGGGG G GGG G GGGG GG G GGGG G G G G<br>40 60 80 100<br>voter turnout<br>Density<br><!-- End of picture text -->

**ggplot** (data = cpds, **aes** (x = vturn)) + **geom_density** () + **xlab** (label = "voter turnout")

## Warning: Removed 39 rows containing non-finite values (stat_density).


<!-- Start of picture text -->
0.03<br>0.02<br>0.01<br>0.00<br>40 60 80<br>voter turnout<br>density<br><!-- End of picture text -->

##### **3.1.3 Scatterplots**

In addition to seeing how to do scatterplots, we also see how to do built-in subsetting here.

17

**<mark>xyplot</mark>** <mark>(vturn ~ year, data = cpds, subset = country == "France")</mark>


<!-- Start of picture text -->
GGG<br>G GGGGG<br>80 GGGGG<br>GG<br>GG<br>75<br>GGGGG<br>70 GGGG<br>GGGGG<br>GGGGG<br>GGGGG<br>65 GGGGG<br>60 GGGG<br>1960 1970 1980 1990 2000 2010<br>year<br>vturn<br><!-- End of picture text -->

**ggplot** (data = **subset** (cpds, subset = country == "France"), **aes** (x = year, y = vturn)) + **geom_point** () + **geom_line** ()


<!-- Start of picture text -->
GGG<br>G GGGGG<br>80 GGGGG<br>GG<br>GG<br>75<br>GGGGG<br>70 GGGG<br>GGGGG<br>GGGGG<br>GGGGG<br>65 GGGGG<br>60 GGGG<br>1960 1970 1980 1990 2000 2010<br>year<br>vturn<br><!-- End of picture text -->

_ggpairs()_ in _ggplot2_ produces a scatterplot matrix showing the relationships of all pairs of a set of variables that deals with both continuous and discrete variables.

##### **3.1.4 Conditioning**

Here’s how we create so-called trellis graphics, which create a series of plots, stratified by some conditioning variable, in this case by country. In ggplot terminology, this is called “faceting”.

18

This is a powerful approach to dealing with multivariate data and is often useful for revealing patterns in data.

**<mark>xyplot</mark>** <mark>(vturn ~ year | country, data = cpds, ylab = 'voter turnout'</mark> )


<!-- Start of picture text -->
1960 1980 2000<br>Switzerland UK USA<br>90<br>807060 GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGG GGGGGG<br>50 GGGGGGGGGGGGGGGGGGGGGGGGGG<br>40 GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGG<br>New Zealand Norway Portugal Spain Sweden<br>GGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG G GGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGG GGGG GGGG GG GGGG GGGG GGGGGG GGG GGGG GGGGGGG GGGGGGGG GGGGGGGGGGGGGGGGGGGG GGG GGGGGGG GGGGGGGGGGGGG 9080<br>GGG GGGGGGG GGGG 70<br>GGGGGGGGGGGGGGGGGGGGGGGGGGGG 60<br>50<br>40<br>Ireland Italy Japan Luxembourg Netherlands<br>GGGGGGGGGGG<br>908070 GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGG GGGGGGG GGGGGGG GGGGGGG GGG GGGG GG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGG GGGG GGG GGGGGGGGGGGGGG GGGGGGG G<br>GGGGG GGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG<br>60 GGGG GGGGG<br>50<br>40<br>Finland France Germany Greece Iceland<br>GGGGGGGGGGGGGGG GG GGGGGGGGGGG GGG GG GGGGGGGGGGGG GGGGGGGGGGG GGGGGGGGGGG GGGGGGGGGGG GGGG GGG G GGG GGG GGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGG GGGGGGGG GGG GGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG 9080<br>GGGGG GGGGG GG 70<br>GGGG GGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG<br>GGGGG GGGGGGGGG GGGGGGGGG 60<br>50<br>40<br>Australia Austria Belgium Canada Denmark<br>90 GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGG GGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGG<br>8070 GGGGG GGGG GGG GGGG GGGGG GGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGG GGGGGG GGGGGGGGGGGGG GGGGG GGGG GGGGGGGGGGGGG GGGG GG GGGG<br>60 GGGGGG GG GGG<br>50<br>40<br>1960 1980 2000 1960 1980 2000 1960 1980 2000<br>year<br>voter turnout<br><!-- End of picture text -->

**ggplot** (data = cpds, **aes** (x = year, y = vturn)) + **geom_point** () + **facet_wrap** (~country, ncol = 3) + **ylab** (label = 'voter turnout')

## Warning: Removed 7 rows containing missing values (geom_point). ## Warning: Removed 15 rows containing missing values (geom_point).

19

<mark>## Warning: Removed 17 rows containing missing values (geom_point</mark> ).


<!-- Start of picture text -->
Australia Austria Belgium<br>80 GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGG GGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGG GGGG GGGGGG GGGGGGGGGGGGGGGGGGGGGGGG<br>60<br>40<br>Canada Denmark Finland<br>80 GGGGGG GGGGGGGGGGGGG GGGGG GGG GGGGGGGGGGGGGG GGGG GGGGGG GG<br>60 GGGGGGGGGGGGGG GGGGG G GGGG GGGGGGGGG GGGGGGG GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG GGGG<br>40<br>France Germany Greece<br>8060 GG GGGGG GGGGGGGGGGG GGG GGGGG GG GGGGG GGGGGGGGG GGGGGGGGG GGGGG GGGGGGG GGGGGGGG GGGGGGG GGGGGGGGGGGGGGGGGGGGGG GG G GGGGGG GGG GGGGGGGGGGGGGGGG GGGGGGGGGGG GGG GGGG<br>40<br>Iceland Ireland Italy<br>80 GGGGGGG GGGG GGG GGGG GGGGGGGGGGGGGGGGGGGGG GGGG GGGG GGGG GGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGG<br>GGGGG GGGGGGGGGGGGGGGGG GGGGGGG GGGGGGGG GGGGGGGGGG GGGG<br>60<br>40<br>Japan Luxembourg Netherlands<br>GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGG GGGGGGG GGGGGGGGGGG<br>80 G GGGGG GGGGG GGGGGGGGGGGG GGGG GGGG GGGG GGGG G<br>60 GGG GGGG GG GGGGGGGGGGG GGG GGGGGGGGGGGGG GGGGGGGGG GGGGGG<br>40<br>New Zealand Norway Portugal<br>G<br>8060 GGGGGG GGG GGGGGG GGGGGG GGG GGG GGG GGGGGG GGG GGGGGGGGGGGG GGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGG G GGG GGGG GGGGGGGG GGGGGGGGGGGGGGGG<br>40<br>Spain Sweden Switzerland<br>8060 GG GGG GGGG GGGGGGG GGGGGGG GGGG GGGGGGG GGGGGGGG GGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGG<br>40 GGG GGGGGGGGGGGG GGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG GGGG<br>UK USA<br>80 GGGGGGGGGG GGGGGGGGG GGGG GGGG GGGGGGGGGG GGGG<br>60 GGGG GGGGGG GG GG GGGGGGGG GG GG GG GG GG GG GG GG GG<br>40 GG GG GG GG GG GG GG GG GG GG G<br>1960 1970 1980 1990 2000 20101960 1970 1980 1990 2000 2010<br>year<br>voter turnout<br><!-- End of picture text -->

In ggplot2, here’s how we condition by using different colors or symbols within a single panel. Note the third plot in which we annotate the symbols based on a fourth variable - unemployment in this case.

countrySet <- **c** ("USA", "Germany", "France", "Spain") sub <- **subset** (cpds, subset = country %in% countrySet)

fig1 <- **ggplot** (data = sub,

20

**aes** (x = year, y = vturn, color = )) + **geom_line** ( **aes** (color = country))

fig2 <- **ggplot** (data = sub, **aes** (x = year, y = vturn, linetype = )) + **geom_line** ( **aes** (linetype = country))

**grid.arrange** (fig1, fig2, nrow = 1, ncol = 2)

## Warning: Removed 17 rows containing missing values (geom_path). ## Warning: Removed 17 rows containing missing values (geom_path).


<!-- Start of picture text -->
90 90<br>80 80<br>70 70<br>France France<br>Germany Germany<br>60 Spain 60 Spain<br>USA USA<br>50 50<br>40 40<br>196019701980199020002010 196019701980199020002010<br>year year<br>vturn vturn<br><!-- End of picture text -->

**ggplot** (data = sub, **aes** (x = year, y = vturn, color = , size = )) + **geom_point** ( **aes** (color = country, size = unemp))

## Warning: Removed 17 rows containing missing values (geom_point).

21


<!-- Start of picture text -->
G G G G G G G G<br>90<br>G G G G G G G G GG G G<br>G G G G G G G<br>G G G<br>G G G<br>GGGG<br>G G G G G G<br>80 G G G G G GGGG<br>G G G G GG G G G G GGGG GGGGGGG G France<br>GGG GGGG GGGG<br>GGG G<br>Germany<br>G G GGG G G<br>70 G G G G G GGG GGGGGGGGGGGGGGGGGGGG G Spain<br>GGGGG G USA<br>GGGGG<br>60 G G G G G GGG<br>G G G 5<br>G G G G GG G 10<br>50 G G G G G G G G G G G 15<br>G G<br>G G G G G G G G G 20<br>40 GG G<br>G G G G<br>G G<br>G G G G G G G G G G<br>1960 1970 1980 1990 2000 2010<br>year<br>vturn<br><!-- End of picture text -->

##### **3.1.5 Contour plots**

In general, I advise people to stay away from plots that attempt to show three dimensions, because it is very hard to see the whole plot without some of the features hiding other parts of the plot. Rather, contour and image plots are generally a better choice.

Here are contour plots:

**require** (reshape, quietly = TRUE) _## ## Attaching package: ’reshape’ ## ## The following object is masked from ’package:plyr’: ## ## rename, round_any_ **data** (volcano) volcano3d <- **melt** (volcano)

22

**names** (volcano3d) <- **c** ("xvar", "yvar", "zvar") **contourplot** (zvar ~ xvar + yvar, data = volcano3d)


<!-- Start of picture text -->
60 120<br>140<br>160<br>50<br>180<br>40<br>30 160 180<br>20<br>10<br>20 40 60 80<br>xvar<br>100<br>100<br>yvar<br>100<br><!-- End of picture text -->

**ggplot** (data = volcano3d, **aes** (x = xvar, y = yvar, z = zvar)) + **geom_contour** ()


<!-- Start of picture text -->
60<br>40<br>20<br>0<br>0 25 50 75<br>xvar<br>yvar<br><!-- End of picture text -->

and here are image plots, which show surfaces based on variations in color:

**levelplot** (zvar ~ xvar + yvar, data = volcano3d, col.regions = **terrain.colors** (20))

23


<!-- Start of picture text -->
60 200<br>50 180<br>40 160<br>30 140<br>20<br>120<br>10<br>100<br>20 40 60 80<br>xvar<br>yvar<br><!-- End of picture text -->

**ggplot** (data = volcano3d, **aes** (x = xvar, y = yvar, z = zvar)) + **geom_tile** ( **aes** (fill = zvar)) +

**scale_fill_gradient** (low = 'green', high = 'brown', guide = 'legend')


<!-- Start of picture text -->
60<br>zvar<br>40 100<br>125<br>150<br>20<br>175<br>0<br>0 25 50 75<br>xvar<br>yvar<br><!-- End of picture text -->

_######################################### ### 3.2: Some other details on lattice #########################################_

I’m not a fan of that color scheme for the ggplot2 graphic, but didn’t have time to figure out something better.

24

#### **3.2 Some other details on** **_lattice_**

The analog of _par()_ for lattice is _trellis.par.set()_ and _trellis.par.get()_ . Often you can get a nice lattice graphic without much work, but modifying aspects of a lattice graphic may take some work. Chapter 7 of the Chambers book discusses this to some degree. Note that _lattice_ graphics are based on the _grid_ package, so serious monkeying may require learning something about _grid_ .

**Modularity and the** **_panel()_ function** _Lattice_ functions are highly modular and have consistent argument names (see p. 308 of Adler), unlike in _graphics_ . The high-level functions take care of the overall logistics while low-level panel functions do the actual plotting within each panel. To add features to the panels, you need to do it through the _panel()_ function argument:

**library** (MASS) out = **xyplot** (time ~ dist, data = hills, panel = **function** (x, y, ...){ **panel.xyplot** (x, y, ...) **panel.lmline** (x, y, type = 'l') **panel.loess** (x, y, ...) }) **splom** ( ~ hills, panel = **function** (x, y, ...){ **panel.xyplot** (x, y, ...) **panel.loess** (x, y, ...) })

We can manipulate subpanels in a lattice graphic:

**xyplot** (Petal.Length ~ Sepal.Length | Species, iris, layout = **c** (2, 2)) **trellis.focus** ("panel", 1, 2) **do.call** ("panel.lmline", **trellis.panelArgs** ())

### **4 Animations and interactive graphics on the web**

To create animations, check out the _animation_ package for animations that can run in R or in HTML.

To create interactive graphics that users can interact with on the web, check out the Shiny.

25

### **5 Graphics devices**

Graphics are plotted on a _device_ . In the old days when computer monitors were not high resolution or in color, this referred to a physical device, but nowadays this is a general term that denotes the context in which the plot is being made: typically on screen or as a file in a particular file format. The standard device in a UNIX environment is X11, basically a graphics window set up in the X11 windowing system. On-screen plotting is generally done with R interacting with a window manager for the operating system, so R is not interacting directly with the physical display. Often one needs to iterate to get a plot to look good when printed to a file; in particular the aspect (width to height ratio) (e.g., you can specify width and height in _pdf()_ ), the margin sizes relative to the size of the core plot, and size of plotting symbols and text relative to the size of the plot. That is the relative sizes when seen in a graphics window on the screen may be very different when printed to a file.

You can have multiple graphics windows open at once; you’ll need to explicitly call the function for opening a device to set up any additional ones. _dev.cur()_ tells the number of the active one and _dev.set()_ allows to change it.

### **6 Graphics file formats**

We’ve already seen _pdf()_ in Unit 4. Analogues of _pdf()_ include _postscript()_ , _png()_ , _tiff()_ , _bmp()_ , and _jpeg()_ . If you have already made the plot in the graphics window and want to export it, you can use _dev.copy2pdf()_ .

Note: Lattice graphics are optimized for the current plotting device, so using _dev.copy2pdf()_ and the like is a bad idea since the graphic will have been optimized for the computer screen window. Instead use _pdf()_ and the like to make the plot within the device.

#### **6.1 Vectorized vs. rasterized file formats**

pdf and postscript images are vectorized - in general elements of the image are symbolic objects (such as points, text, symbols, line segments, etc.) and when an image is resized, the items rescale appropriately for the new size without losing resolution. In contrast, with a rasterized format such as JPEG, individual pixels are plotted, and when an image is rescaled, in particular enlarged, one is stuck with the resolution that one used in plotting the figure (i.e., one has the original pixels but if you zoom, you only show some of them, losing resolution). One downside to vectorized images is that with a lot of points or line segments, they can be very large. For 2-d images such as created by _image()_ , rasterized formats do make some sense inherently, though the other features in the file

26

(such as any text) is also rasterized.

#### **6.2 File formats for journal articles**

For inserting into Latex files for journal articles, I typically use _pdf()_ in combination with _pdflatex_ to compile the Latex file. In some cases for large images I will use _jpeg_ or _png_ files for figures in a paper.

Journals sometimes request either _postscript_ or _encapsulated postscript_ (EPS) format images. If you create a single R plot (as opposed to multiple pages), using _postscript()_ , the result should be EPS compatible. You can do this with the arguments

horizontal = FALSE, onefile = FALSE, paper = "special"

or by calling _setEPS()_ . If you have a postscript file that is not EPS, _ps2epsi_ is a Ghostscript tool that can do the conversion from _ps_ to _eps_ (i.e., _epsi_ ). EPS is a standardized form of postscript and contains a bounding box describing the bounds of the image. EPSI files contain a bitmapped preview image in the “Interchange” format that systems can use to show an approximation of the image even if they can’t render (i.e., display) postscript.

Discussing much about postscript is beyond our scope, but note that postscript files are just text in a particular language that the printer uses for generating a printout. So you can use _less_ or _emacs_ to view the file in UNIX. You’ll see that it says that it’s EPS and has a bounding box. It’s occasionally handy to search for and replace text in a postscript file manually rather than regenerating the file. For example I could search for ’ _noise_ ’ in _example.eps_ (created in the demo code) and replace with something else. I could also monkey with the positioning, which should involve the numbers just before the text string. You can also do this sort of thing in pdf files as well.

#### **6.3 Conversion utilities**

UNIX has a lot of utilities for converting between image formats. Windows and Mac also have GUI-style programs for doing this.

In UNIX, _pdftops_ will convert pdf to postscript and with the optional argument _-eps_ to encapsulated postscript, while _ps2epsi_ will create encapsulated postscript. _gs_ (Ghostscript) will do a lot of different manipulations of ps and pdf files, including converting to jpeg and other formats and merging and splitting pages of pdf files. Here are some examples of command-line calls from within a UNIX shell:

---

[Up: contents](index.md) · [convert from ps to jpeg →](02-convert-from-ps-to-jpeg.md)
