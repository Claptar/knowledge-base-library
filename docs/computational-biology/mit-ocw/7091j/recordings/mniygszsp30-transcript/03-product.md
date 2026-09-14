---
title: product.
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recordings/mniygszsp30-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# product.

**Source:** `recordings/mniygszsp30-transcript.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**So what we would like to do is this. We would like to find v sub i, which are vectors, to maximize variance of v sub i transpose x such that v sub i transpose v sub i is equal to 1. In other words, they're unit length vectors. So these are going to be called the eigenvectors.**

**And if we think about the structure that we desire, what we'll find is that they satisfy the constraint that the covariance matrix times an eigenvector is equal to the eigenvalue associated with that vector times the vector itself. And with a little manipulation-- if we multiply both sides by v sub i transpose-- v sub i equals v sub i transpose lambda sub i sigma squared v sub i-- and we move these guys around, v sub i transpose sigma v sub i is equal to-- these two guys, multiplied together, equal 1-- lambda sub i squared.**

**This, we see up above, is equal to the variance when it's projected in the direction of v. And so lambda sub i squared is simply the variance associated with that direction. So the question then becomes, how do we find these things. And how do we discover these magic eigenvectors that are directions in which this multivariate Gaussian has its variance maximized?**

**And we can do this by singular value decomposition. So we can compute this covariance matrix. So we compute sigma from the data. And then we do a singular value decomposition such that sigma is equal to U S U transpose.**

**And that's what the singular value decomposition does for us is it decomposes the sigma matrix into these components where S is a diagonal matrix that contains the eigenvalues and U is a column. Each column is an eigenvector. So in doing a singular value decomposition, we get the eigenvalues and the eigenvectors.**

**The other thing, you recall, was that sigma was equal to A A transpose when we started off. A was the matrix that we used to make our multivariate Gaussian out of our univariate Gaussians. And thus, what we can observe is that our multivariate Gaussian x is equal to U S to the 1/2 times z plus a mean. So here is what's going**

23

**when we make a multivariate Gaussian is we're taking a bunch of univariate Gaussians, we're scaling them, and we're rotating them. OK?**

**And that makes a multivariate Gaussian. And then we offset this whole thing by a mean. Because we also have to do rotations around the origin. So the way I think about multivariate Gaussians is that it is a scaling and a rotation of univariate Gaussians. And implicit in that scaling and rotation is the discovery of the major directions of variance in the underlying data as represented by the eigenvectors. And the eigenvalues tell you how much of the variance is accounted for in each one of those dimensions. Are there any questions about that? I hope there are. Yes.**

**AUDIENCE: How do you compute sigma from the data? Is it some magical process? PROFESSOR: The sigma of the value of decomposition? AUDIENCE: No. So-PROFESSOR: How do you compute sigma from the data? AUDIENCE: Yeah, the first step. PROFESSOR: That is shown in equation seven. So you can compute the means. And you know you have x, which are observed values. So you compute that expectation. And that is sigma. OK? Good question. Any other questions?**

**OK. So we have these eigenvectors and eigenvalues, which represent the vectors of maximum variance in the underlying data. And we can use these to organize data by projecting observations onto these eigenvectors-- or they're sometimes called principal components-- defined dimensions of variability that help us organize our underlying data. We'll come back to that in a moment. OK. Any other questions about principal component analysis? Yes. AUDIENCE: [INAUDIBLE] e was expectation when you were calculating the second?**

24

**PROFESSOR: Yes, e is the expectation is correct.**

**AUDIENCE: And also what that means.**

**PROFESSOR: It's the average expected value. So in the case of computing sigma, you would compute the expected value of that inner equation across all the data points that you see. So you'd sum up all the values and divide by the number of things that you had. Any other questions? OK.**

**So just for calibration for next year, how many people think they've got a general idea of what principal component analysis is-- a general idea? Uh-oh. How many people who thought it was really interesting were sort of completely baffled about halfway through? OK. All right.**

**Well, I think that recitation can help with some of those questions. But if anybody has a question they'd like to ask now-- No? It's that far gone? I mean, the thing with this sort of analysis is that if your matrix algebra is a little rusty, then, when you start looking at equations like that, you can get a little lost sometimes.**

**All right. Well, let's turn, then-- if there aren't any brave souls who wish to ask a question, we'll turn to single cell RNA-seq analysis. So I'm a firm believer that single cell analysis of biological samples is the next big frontier. And it's being made possible through devices like this.**

**This is a Fluidigm C1 chip, which has 96 different reaction wells, which allows you, in each well, to process a single cell independently. And the little winds are ways to get reagents into those cells to do things like produce RNA-seq ready materials. And when you do single cell analysis, you can take apart what's happening in a population.**

**So an early paper asked some fairly fundamental but simple questions. For example, if you take two 10,000 cell aliquots of the same culture, and you profile them independently, and you ask how well to the expression values for each gene agree between sample A and sample B, you expect there to be a very good agreement between sample A and sample B in these 10,000 cell cultures.**

25

**A second question is, now, if you take, say, 14 cells from those cultures and you profile them independently, and you ask, how well do they correlate with what you saw in the 10,000 cell experiment, that will tell you something about the population heterogeneity that you're observing. Because if they correlate perfectly with the 10,000 cell experiment, then you really know that there's no point in looking at individual cells in some sense, because they're all the same. Seen one, seem them all. Right? But if you find that each cell has its own particular expression fingerprint and what you're seeing in the 10,000 cell average experiment wipes out those fingerprints, then you know it's very important to analyze each cell individually.**

**So the analysis that was done asked exactly that question. So here's what I'll show you in these plots. So here is, on the upper left, the 10,000 cell experiment versus the 10,000 cell experiment. And as you can see, the correlation coefficient is quite high-- 0.98-- and looks very, very good of experiment one versus experiment two, or rep one, rep two. Here is a separate experiment which is looking at two individual cells and asking-- and plotting, for each gene, the expression in one cell versus the gene in the other cell.**

**And you can see that the correlation coefficient's 0.54. And there's actually a fairly wide spread. In fact, there are genes that are expressed in one cell that are not expressed in the other cell, and vice versa. So the expression of these individual cells it's quite divergent.**

**And the final panel shows how-- down here-- how a single cell average on the y-axis relates to the 10,000 cell experiment. But given the middle panel-- the panel B there-- that is showing the fact that two single cells don't really relate that well to another, it bags other questions. For example, are the isoforms of the genes that are being expressed the same in those distinct cells? And so panel D shows isoforms that are the same across each one of the single cells being profiled, which is the solid bar at the top. And the bottom couple of rows in figure D are the 10,000 cell experiment average.**

**But panel E is the most interesting, perhaps, which is that the isoforms for those**

26

**four genes are being differentially expressed in different individual cells. And that's further supported by taking two of those genes and doing fluorescent in situ histochemistry and microscopy, and looking at the number of RNA molecules for each one of those, and noting that it corresponds to what's seen in the upper right hand panel. So we see that in individual cells, different isoforms are being expressed.**

**Now these cells were derived from bone marrow. And they're exposed to lipopolysaccharide to activate an immune response. So they are clearly not all behaving exactly the same.**

**And to further elucidate this, the authors of this paper took the gene expressions that they saw for a given cell as a large vector and computed the principal components, and then projected the cells into the first and second principal component or eigenvector space. And as you can see, there is a distinct separation of three of the cells from the rest of the cells, where three of the cells, which correlate well with principal component one, are thought to be mature cells that express certain cell surface proteins whereas the ones on the left-- the maturing cells-- the triangle depicted cells-- express certain cytokines under the maturing legend there, on the clustergram on the right-hand side.**

**And thus, the first principal component was able to separate those two different broad classes of cells. So it looks like there are at least two different kinds of cells in this population. And then, the authors asked another question, which is, can they take individual cell data and look at the relationship between pairs of genes to see which genes are co-expressed.**

**And the hypothesis is that genes that are co-expressed in individual cells make up individual regulatory circuits. And so they hypothesize that the genes LRF7 and IFIT1 and STAT2 and LRF7 are all in an anti-viral regulatory circuit. They then ask the question, if they knocked out LRF7, which is the second panel on the right-hand side, would they oblate downstream gene expression.**

**And they partially did. And they thought that since STAT2 and LRF7 are both**

27

**thought to be regulators of the circuit and they're both downstream of the interfering receptor, they thought if they knocked out the interfering receptor, they would oblate most of the anti-viral cluster, which, in fact, they did.**

**So what this is suggesting is that, first, single cell analysis is extraordinarily important to understand what's going on in individual cells. Because in a cell culture, the cells can be quite different. And secondarily, it's possible, within the context of individual single cell analysis, to be able to pick out regulatory circuits that wouldn't be as evident when you're looking at cells en masse.**

**And finally-- I'll thank Mike for the next two slides-- I wanted to point out that quality metrics for RNA-seq data for single cells is very important. And we talked about library complexity earlier in the term. And here, you can see that as library complexity increases, expression of coefficient of variation, which is the standard deviation over the mean, comes down as you get sufficient library complexity. And furthermore, as library complexity increases, mean expression increases.**

**And the cells that are in red were classified as bad by microscopy, from the Fluidigm instrument processing step. So I think you can see that single cell analysis is going to be extraordinarily important and can reveal a lot of information that is not present in these large batch experiments. And it's coming to a lab near you.**

**So on that note, I'll thank you very much for today. And we'll see you later in the term. And Professor Burge will return at the next lecture. Thanks very much.**

28

---

[← AUDIENCE](02-audience.md) · [Up: contents](index.md)
