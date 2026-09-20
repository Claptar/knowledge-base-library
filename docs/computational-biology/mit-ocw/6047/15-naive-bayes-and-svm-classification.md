---
title: "15. Naive Bayes and SVM Classification"
course: "MIT 6047"
chapter: 15
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. Naive Bayes and SVM Classification

## What this covers

This chapter covers **supervised learning** for biological classification: given data that is
already labeled by class, how do you build a rule that assigns a label to new, unlabeled data? It
develops two different answers — a generative model, **Naive Bayes**, and a discriminative model,
the **Support Vector Machine (SVM)** — together with two worked biological applications: predicting
which human proteins are targeted to the mitochondrion from seven genomic features, and classifying
tumor samples as one of two leukemia subtypes from gene expression data. It assumes comfort with
Bayes' rule and basic probability, and with vectors and dot products. It follows on from a previous
lecture on clustering, which is **unsupervised** — it groups data with no labels at all, whereas
classification uses pre-labeled data to learn rules for labeling more of it.

## Generative and discriminative classifiers

There are two general ways to approach classification, and they parallel a distinction that shows
up elsewhere in the course (in motif discovery, between HMMs and CRFs): a **generative** model
describes the probability that a given label is correct, and a **discriminative** model draws a
boundary that separates the classes without describing that probability explicitly. This chapter
develops one of each: a Bayesian (generative) classifier, applied to identifying mitochondrial
proteins, and a Support Vector Machine (discriminative), applied to classifying tumor samples from
microarray data.

## Bayes' rule as a classifier

**Motivating problem.** Given the human genome, how do you decide which proteins are targeted to
the mitochondrion? This matters because mitochondrial proteins mediate disease and metabolic
processes: mitochondria have their own genome, but it retains only about eleven of the genes needed
to run the organelle — the rest are encoded in the nuclear genome and imported after translation.
Finding them genome-wide is useful for studying diseases associated with the mitochondrion, such as
aging. One classification method for this problem considers seven features of every human protein:
targeting signal, protein domains, co-expression, mass spectrometry evidence, sequence homology,
induction, and motifs.

The general approach: work out how each feature is distributed among proteins of each class
(mitochondrial and non-mitochondrial), and then, given a new protein's feature values, use
probability to decide which class it more likely belongs to.

**A single feature.** Suppose there is a class-dependent distribution for one feature, estimated
from real data, and a prior — the a priori chance of drawing a sample of a given class before
looking at any data, i.e. the relative size of the class. It is not enough to look only at how
likely the observed feature value is under each class's distribution: if one class is far more
common a priori, only strong evidence should be allowed to overturn that prior. Bayes' rule is what
combines the two correctly, converting the forward, generative probabilities — how likely a feature
is under each class — into the posterior probability of the class given the feature:

$$P(\text{Class} \mid \text{feature}) = \frac{P(\text{feature} \mid \text{Class})\,P(\text{Class})}{P(\text{feature})}$$

with the usual names: $P(\text{Class}\mid\text{feature})$ is the **posterior**, $P(\text{Class})$
the **prior**, and $P(\text{feature}\mid\text{Class})$ the **likelihood**. For mitochondrial DNA,
the prior is small — on the order of $1500/21000$, well under 10% of the genome — so a classifier
should only call a gene mitochondrial when the observed features make a strong case, precisely
because the prior probability of being mitochondrial is so low.

**The decision rule.** Applying Bayes' rule to two candidate classes and choosing the more probable
one, choose Class 1 over Class 2 exactly when

$$\frac{P(\text{feature} \mid \text{Class1})P(\text{Class1})}{P(\text{feature})} > \frac{P(\text{feature} \mid \text{Class2})P(\text{Class2})}{P(\text{feature})}.$$

The denominator $P(\text{feature})$ is the same on both sides and cancels, so the rule reduces to
comparing $P(\text{feature}\mid\text{Class})\,P(\text{Class})$ across classes. Taking logs turns this
into a **discriminant function**: choose Class 1 over Class 2 exactly when

$$G(X) = \log\left(\frac{P(X \mid \text{Class1})P(\text{Class1})}{P(X \mid \text{Class2})P(\text{Class2})}\right) > 0.$$

Working with the log-ratio rather than the raw probabilities has three practical advantages:
numerical stability (probabilities of many features multiplied together underflow quickly), easier
arithmetic (sums of logs instead of products), and a discriminator that is a monotonic function of
the underlying probability ratio, so it makes exactly the same decisions.

**Loss and misclassification cost.** This discriminant treats every misclassification the same,
which is not always right. If a patient is classified as healthy when they in fact have cancer, they
go untreated; if a healthy patient is classified as having cancer, the cost is emotional distress
without the same risk to life — the two errors are not equally bad. A **loss function** $L_{kj}$
formalizes this by assigning a cost to labeling an object as class $j$ when its true class is $k$,
so that the classifier can be tuned to penalize the more dangerous error more heavily (a specific
example of such a loss function appears in this course's second problem set, not reproduced here).

## Building the classifier from data

Everything above assumes the priors and the class-conditional feature distributions are already
known. In practice they must be estimated from a **training set** — data whose true classes are
already known. A large, unbiased training set is the single most important ingredient of a good
classifier.

**How much training data is enough?** There is no exact answer, but a practical diagnostic exists:
hold out part of the labeled data as a **test set** (also called a holdout set) that the algorithm
never trains on, and measure accuracy on it as the size of the remaining training set is varied.
Enough training data has been collected once this accuracy curve flattens — additional data then
buys only marginal improvement.

**Modeling $P(X \mid \text{Class})$.** As with clustering, one option is to model a feature as
Gaussian and fit its mean and variance by maximum likelihood. A simpler alternative, used in the
mitochondrial protein study described below, is **density estimation by binning**: divide the range
of a feature into a fixed number of bins (say five), and estimate, from the training data, the
probability that a feature from a given class falls into each bin. This is still a maximum-likelihood
estimate, just for a multinomial distribution over bins rather than a Gaussian. Binning is attractive
because directly fitting a continuous distribution can be harder, at the cost of losing some
resolution within a bin.

Binning has one sharp failure mode: if a bin has zero training samples, its estimated probability is
zero, and a single zero probability in a product overrides everything else — the classifier treats
the bin as *impossible* rather than merely unlikely. The standard fix is the **Laplace correction**:
add a small pseudo-count (e.g. one) to every bin, pulling every estimate slightly toward uniform and
avoiding zero probabilities. An alternative is simply to choose bins coarse enough that none are
empty in practice — more bins resolve the distribution more finely but risk overfitting when data is
limited.

**Estimating the priors $P(\text{Class})$.** Three approaches:

1. **Count relative frequencies in the training data.** This is prone to bias, because available
   data is often skewed toward less common classes (they tend to be specifically sought out and
   studied), but works well when the training sample is genuinely representative.
2. **Use expert or external knowledge** — an independent estimate of the class proportions, obtained
   by other means, used as a prior. This is the approach actually used for mitochondrial DNA, since
   independent estimates of the mitochondrial protein fraction were already available.
3. **Assume all classes equally likely**, when there is no other information. This is effectively
   what maximum-likelihood clustering does implicitly; it is a strong assumption, but the best
   available one in the absence of data.

## Naive Bayes: combining many features

The mitochondrial classifier uses seven features, not one, and the binning approach does not scale
naively to many features at once: joint binning over two five-bin features already needs 25 bins,
and over all seven features, roughly 80,000 — far more than there is training data to fill, so most
bins would be empty and the zero-probability problem would dominate.

The fix is the **Naive Bayes assumption**: once the class is known, the features are conditionally
independent of one another. This is almost never exactly true — features can be correlated overall —
but the assumption only requires that any such correlation is explained by the class itself, with no
further dependence *within* a class. It is nearly always false in the strict sense, yet used anyway
because it is easy to work with and often close enough to give a useful classifier. (If particular
features are known to be coupled, their joint distribution can be modeled together for just that
pair, relaxing independence only where it is needed.)

Under this assumption the joint likelihood factors into a product:

$$P(f_1, f_2, \dots, f_N \mid \text{Class}) = P(f_1 \mid \text{Class})\,P(f_2 \mid \text{Class}) \cdots P(f_N \mid \text{Class}),$$

and the discriminant function becomes a ratio of these products times the priors:

$$G(f_1, \dots, f_N) = \log\left(\frac{\prod_i P(f_i \mid \text{Class1})\,P(\text{Class1})}{\prod_i P(f_i \mid \text{Class2})\,P(\text{Class2})}\right).$$

## Evaluating a classifier

A classifier must always be tested on data outside its training set: an algorithm that simply
memorizes its training data, then behaves arbitrarily elsewhere, scores perfectly on the training
set while revealing nothing about real performance — hence the holdout/test set introduced above.

For a binary classifier (in the target class, or not), there are four outcomes: true positive (TP),
true negative (TN), false positive (FP), false negative (FN). Two standard summaries:

- **Sensitivity** — the fraction of objects truly in the class that are correctly labeled as such
  (the true positive rate). Low sensitivity means too many false negatives.
- **Specificity** — the fraction of objects truly *not* in the class that are correctly labeled as
  not in it (the true negative rate). Low specificity means too many false positives.

These trade off against each other: labeling everything as the target class gives 100% sensitivity
but 0% specificity, which is useless. Most classifiers expose a threshold (in the Bayesian case, the
cutoff on the discriminant function $G$); raising it trades sensitivity for specificity and lowering
it does the reverse.

## Case study: MAESTRO and mitochondrial proteins

Calvo et al. built high-confidence predictions of mitochondrial localization by combining several
genome-scale evidence sources into a single Naive Bayes classifier, MAESTRO. For each human gene
product, they computed a score from each of seven data sets — targeting signal, protein domain,
cis-motif, yeast homology, ancestry, coexpression, and induction — each of which is individually only
a weak predictor of mitochondrial localization on its own. Performance was assessed against curated
gold-standard sets: 654 known mitochondrial proteins (from the MitoP2 database) and 2,847 proteins
known to localize elsewhere. Integrating the seven weak scores with a Naive Bayes classifier gave
99% specificity and 71% sensitivity — a case where combining several individually weak classifiers,
even under the (false) assumption that the seven scores are independent given the class, produces a
substantially stronger one. Applied genome-wide, MAESTRO predicted 1,451 mitochondrial proteins,
450 of them novel.

## Support vector machines: maximum-margin classification

The Bayesian approach is generative: it models the full probability of the data under each class,
which requires more information than classification strictly needs. A **discriminative** approach
instead asks only for a function that separates the classes, without modeling how the data was
generated.

A **Support Vector Machine** finds a **hyperplane** that separates two classes of training points,
choosing, among the (generally many) hyperplanes that do this, the one that maximizes the **margin**
— the distance from the hyperplane to the nearest point of either class. Equivalently: surround the
hyperplane with margins of equal width on each side, containing no training points, and make those
margins as wide as possible. The points that end up exactly on the boundary of the margin are the
ones constraining how wide it can be — the **support vectors** — and they are what determine the
hyperplane: adding new points outside the margin, or removing points that are not support vectors,
does not change the maximum-margin solution at all.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A maximum-margin hyperplane separating two classes, with the two support vectors and the vector w perpendicular to the hyperplane">
  <line x1="39.4" y1="175.4" x2="259.4" y2="15.4" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="50" y1="190" x2="270" y2="30" stroke="currentColor" stroke-width="1.8"/>
  <line x1="60.6" y1="204.6" x2="280.6" y2="44.6" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <circle cx="150" cy="190" r="4" fill="currentColor"/>
  <circle cx="200" cy="160" r="4" fill="currentColor"/>
  <circle cx="90" cy="170" r="4" fill="currentColor"/>
  <circle cx="90" cy="170" r="8" fill="none" stroke="currentColor" stroke-width="1"/>
  <circle cx="130" cy="90" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="180" cy="50" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="70" cy="60" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="70" cy="60" r="8" fill="none" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="110" x2="183" y2="142" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="183,142 176,133 187,133" fill="currentColor" transform="rotate(35 183 142)"/>
  <text x="205" y="100" font-size="12" fill="currentColor">hyperplane</text>
  <text x="235" y="60" font-size="11" fill="currentColor" opacity="0.75">margin</text>
  <text x="188" y="150" font-size="12" fill="currentColor">w</text>
  <text x="95" y="185" font-size="11" fill="currentColor">support vector</text>
</svg>
<figcaption>The separating hyperplane (solid), flanked by margins of equal width (dashed) touching
the nearest point of each class. The circled points are support vectors — they alone fix the margin.
The vector $w$, perpendicular to the hyperplane, is the direction a new point is compared against.</figcaption>
</figure>

**Why only dot products matter.** Write $w$ for the vector perpendicular to the hyperplane, with the
hyperplane sitting at distance $b/|w|$ from the origin along $w$. A point $x$ is classified positive
if $w \cdot x > b$, and negative otherwise. It can be shown that the optimal (maximum-margin) $w$ is
always expressible as a linear combination of the training vectors, $w = \sum_i \alpha_i x_i$, so
classifying a new point $x$ reduces to

$$w \cdot x = \sum_i \alpha_i\,(x_i \cdot x),$$

which depends on the training data only through pairwise dot products $x_i \cdot x$. Correspondingly,
it can be shown that finding the maximum-margin hyperplane itself amounts to solving a linear program
whose objective depends on the training points only through their pairwise dot products. This matters
because it means the cost of finding the hyperplane does not depend on the dimension of the data at
all — only on the precomputed table of pairwise dot products.

## The kernel trick

Because everything above depends only on dot products, a nonlinear transformation $\phi$ of the data
can be introduced almost for free, *provided* the dot product $\phi(v_1) \cdot \phi(v_2)$ in the
transformed (possibly very high-dimensional) space can be computed directly from $v_1$ and $v_2$ in
their original, lower-dimensional form. A **kernel** $K$ is exactly such a shortcut:

$$K(v_1, v_2) = \phi(v_1) \cdot \phi(v_2).$$

The left side is a function of two low-dimensional vectors; the right side is a dot product in a
high-dimensional (even infinite-dimensional) space — but $K$ lets that dot product be computed
without ever forming $\phi(v)$ explicitly. For the transformation $\phi(x) = (x, x^2)$, for instance,

$$K(x_1, x_2) = (x_1, x_1^2) \cdot (x_2, x_2^2) = x_1 x_2 + (x_1 x_2)^2.$$

**Common kernels:**

1. **Linear**: $K(v_1,v_2) = v_1 \cdot v_2$ — the trivial mapping $\phi(x) = x$.
2. **Polynomial**: $K(v_1,v_2) = (1 + v_1\cdot v_2)^n$ — the example above uses $n=2$.
3. **Radial basis (RBF)**: $K(v_1,v_2) = \exp(-\beta\lVert v_1-v_2\rVert^2)$. This corresponds to
   mapping each point to a Gaussian function centered on it — a point in an infinite-dimensional
   function space (Hilbert space) — and combining these functions to build the decision boundary.
4. **Sigmoid**: $K(v_1,v_2) = \tanh[\beta(v_1^T v_2 + r)]$, popular because it connects SVMs to
   two-layer perceptron neural networks; it has been noted that the resulting kernel matrix may fail
   to be positive semi-definite for some parameter choices, though it is still used in practice.

**Which functions are valid kernels?** A kernel is valid exactly when it satisfies **Mercer's
condition**: $K(x,y)$ is a valid kernel if and only if, for every function $g$ with
$\int g(x)^2\,dx$ finite,

$$\iint K(x,y)\,g(x)\,g(y)\,dx\,dy \;\ge\; 0.$$

**A worked example.** Take two classes of one-dimensional points,

$$\{-5,-4,-3,3,4,5\} \quad\text{and}\quad \{-2,-1,0,1,2\},$$

which are not linearly separable on the line. Applying $\phi(x) = (x, x^2)$ sends them to

$$\{-5,-4,-3,3,4,5\} \to \{(-5,25),(-4,16),(-3,9),(3,9),(4,16),(5,25)\}$$

$$\{-2,-1,0,1,2\} \to \{(-2,4),(-1,1),(0,0),(1,1),(2,4)\}$$

and in this lifted space the two classes are cleanly separated by $y > 6.5$. Pulled back into the
original one-dimensional space, this separating rule reads $x^2 < 6.5$, a condition that cuts the
number line at two points rather than one — a curve rather than a line. In general, the higher the
dimension of the space the data is lifted into, the more intricate the boundary that results when
the classifier is translated back down to the original space.

<figure>
<svg viewBox="0 0 340 260" role="img" aria-label="One-dimensional points from two interleaved classes become linearly separable after lifting through x maps to (x, x squared)">
  <line x1="38" y1="45" x2="302" y2="45" stroke="currentColor" stroke-width="1"/>
  <circle cx="60" cy="45" r="4" fill="currentColor"/>
  <circle cx="82" cy="45" r="4" fill="currentColor"/>
  <circle cx="104" cy="45" r="4" fill="currentColor"/>
  <circle cx="126" cy="45" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="148" cy="45" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="170" cy="45" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="192" cy="45" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="214" cy="45" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="236" cy="45" r="4" fill="currentColor"/>
  <circle cx="258" cy="45" r="4" fill="currentColor"/>
  <circle cx="280" cy="45" r="4" fill="currentColor"/>
  <text x="170" y="68" text-anchor="middle" font-size="12" fill="currentColor">x (not separable by a single cut)</text>
  <line x1="170" y1="100" x2="170" y2="232" stroke="currentColor" stroke-width="1"/>
  <line x1="38" y1="232" x2="302" y2="232" stroke="currentColor" stroke-width="1"/>
  <line x1="45" y1="200" x2="295" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="298" y="197" font-size="11" fill="currentColor" text-anchor="end">y = 6.5</text>
  <circle cx="60" cy="115" r="4" fill="currentColor"/>
  <circle cx="82" cy="156" r="4" fill="currentColor"/>
  <circle cx="104" cy="189" r="4" fill="currentColor"/>
  <circle cx="148" cy="212" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="170" cy="225" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="192" cy="232" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="214" cy="225" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="236" cy="212" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="258" cy="189" r="4" fill="currentColor"/>
  <circle cx="280" cy="156" r="4" fill="currentColor"/>
  <text x="170" y="252" text-anchor="middle" font-size="12" fill="currentColor">after x maps to (x, x^2)</text>
</svg>
<figcaption>Top: two classes on the line, one nested inside the other, with no single threshold
separating them. Bottom: the same points lifted by $\phi(x)=(x,x^2)$ into the plane, where the rule
$y > 6.5$ separates them cleanly.</figcaption>
</figure>

**Overfitting and the cost parameter.** Lifting to a high enough dimension makes almost any data
separable, including noise — in the RBF kernel, raising $\beta$ enough eventually puts every point
in its own private region, defeating the purpose of classifying at all. SVMs resist overfitting
better than this suggests, because they maximize the margin rather than merely finding *some*
separator, but the risk does not disappear and is normally controlled with cross-validation when
choosing kernel parameters. For training sets that are not cleanly separable, a **cost parameter**
$C$ introduces a *soft margin*: it trades off the width of the margin against the number of training
points allowed to fall on the wrong side, with larger $C$ penalizing misclassification more heavily
and forcing a tighter (and possibly less generalizable) fit.

## Case study: classifying leukemia from expression data

Golub et al. classified two types of acute leukemia — acute myeloid (AML) and acute lymphoid (ALL)
— from gene expression, addressing three questions: (1) is there a gene expression pattern
correlated with the AML/ALL distinction at all, (2) how can known samples be turned into a predictor
for new ones, and (3) how should that predictor be validated?

(1) was answered with a "neighborhood analysis" comparing observed gene–class correlations to what
chance would produce, identifying around 1,100 genes more correlated with the AML/ALL distinction
than expected by chance. For (2), a fixed panel of these "informative" genes was chosen, and each
gene cast a weighted vote for one class or the other — weighted by its expression level in the new
sample and by how strongly that gene correlates with the class distinction overall — with the class
receiving the larger total vote winning. For (3), the predictor was cross-validated on the original
data and then tested on an independent sample set. It correctly classified 36 of 38 training samples
(all 36 confidently made predictions were correct), and on the independent set, 29 of 34 samples
were predicted confidently, all correctly, with the remaining 5 left unclassified rather than risking
an error.

Mukherjee et al. applied an SVM to the same problem. A plain SVM only outputs a binary label, which
is a problem when the classifier should be allowed to abstain on samples it is unsure about — as in
the Golub study's 5 unclassified samples — so the authors added a confidence measure on top of the
SVM's output, allowing low-confidence points to be rejected rather than forced into a class, and
identified which genes drove the classification, as Golub et al. had done. Trained on the same 38
samples and tested on the same independent 34, the results (with $|d|$ the rejection cutoff) were:

| Genes | Rejects | Errors | Confidence level | $\lvert d \rvert$ |
| :--- | :--- | :--- | :--- | :--- |
| 7129 | 3 | 0 | 93% | 0.1 |
| 40 | 0 | 0 | 93% | 0.1 |
| 5 | 3 | 0 | 92% | 0.1 |

Zero errors across all three gene-set sizes was a meaningful improvement over previously reported
techniques, and is offered as evidence that SVMs are well suited to classification from large data
sets such as those DNA microarray experiments generate.

## Semi-supervised learning

Some data sets have only a few labeled points, many unlabeled ones, and real underlying structure —
a setting where neither pure clustering nor pure classification performs well on its own. One
hybrid strategy is to cluster the data first, and then classify the resulting clusters.

## Sources

This chapter is drawn entirely from one source: the compiled course notes chapter
"GENE REGULATION 2 – CLASSIFICATION" (`docs/computational-biology/mit-ocw/6047/compiled/compiled-compiled/06-gene-regulation-2-classification.md`),
from MIT OpenCourseWare 6.047 (Computational Biology, Fall 2015), licensed CC BY-NC-SA 4.0. No
slide deck, transcript, or exercise set was supplied for this lecture — the note file itself flags
that it was reconstructed by a model from a PDF with no text layer, so its prose is a paraphrase in
places and every equation in it is unverified; it should be treated as a pointer into the original
course text rather than a citable source in its own right.

The chapter names sources it does not itself contain, in case they are worth following up: the
loss-function example referenced in this course's second problem set; Calvo, S. et al. (2006),
"Systematic identification of human mitochondrial disease genes through integrative genomics,"
*Nat. Genet.* 38, 576–582 (the MAESTRO classifier); Golub, T.R. et al. (1999), "Molecular
classification of cancer: class discovery and class prediction by gene expression monitoring,"
*Science* 286, 531–537; Mukherjee, S. et al. (1998), "Support vector machine classification of
microarray data," MIT AI Memo 1677; Schölkopf, B. et al. (1997), "Comparing support vector machines
with Gaussian kernels to radial basis function classifiers," *IEEE Trans. Signal Processing*;
Burges, C.J.C. (1998), "A tutorial on support vector machines for pattern recognition," *Data
Mining and Knowledge Discovery* 2, 121–167; and Duda, R.O., Hart, P.E., and Stork, D.G. (2001),
*Pattern Classification*, 2nd ed., Wiley.

---

[← 14. Clustering Gene Expression Data](14-clustering-gene-expression-data.md) · [Contents](index.md) · [16. Motif Discovery: EM and Gibbs →](16-motif-discovery-em-and-gibbs.md)
