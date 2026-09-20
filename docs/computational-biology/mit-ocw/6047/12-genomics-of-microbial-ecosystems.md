---
title: "12. Genomics of Microbial Ecosystems"
course: "MIT 6047"
chapter: 12
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Genomics of Microbial Ecosystems

## What this covers

This chapter asks what genomic data can tell us about bacteria not as isolated organisms but as
members of ecosystems — the trillions of cells living in and on a human body, or the whole tree of
prokaryotic life over geological time. It assumes basic familiarity with sequencing, phylogenetic
trees and simple classifiers (a random forest, a correlation matrix), but no prior microbiome
background. Rather than building one derivation, it walks through six case studies from a guest
lecture on bacterial genomics, each answering a different version of the question "what does the
*ecology* of a bacterial community explain that its taxonomy alone does not?"

## The microbiome as an ecosystem

An average human gut holds roughly $10^{14}$ microbial cells, against about $10^{13}$ human cells
in the whole body, plus another $10^{12}$ microbial cells on the skin. By cell count that is about
ten times more bacterial cells than human cells; by gene count, roughly a hundred times more genes
belong to our resident microbes than to our own genome. Those genes are not part of the human
genome, but they routinely affect human physiology — which is the argument for treating the
microbiome as an integral, if foreign, part of "what makes us human," and for bacterial genomics as
a place where a computational biologist can be directly useful.

Microbiome research has moved through three broad stages. Early work was descriptive: survey a
community, sequence it, assign the organisms present to groups. A second stage tried to infer
*rules* from those surveys — networks of co-occurrence, correlation, and (harder) causality between
bacterial groups. The most recent stage is predictive: model the change of a population through
time with an ordinary differential equation, and integrate it forward to forecast future abundance;
when enough data exists across both time and space, the natural extension is a partial differential
equation over a multivariate abundance function.

## From a sample to a data vector: OTUs and the 16S marker

A microbiome sample goes through a fairly standard pipeline: take the sample (skin swab, lake water,
stool), extract the DNA of everything living in it, sequence a marker gene, cluster the conserved
motifs of that gene into **operational taxonomic units (OTUs)**, and build a vector of OTU
abundances for the sample. Bacteria are grouped into OTUs by functional/sequence similarity rather
than by the biological-species concept, which does not transfer well to organisms that exchange DNA
horizontally.

The workhorse marker is the **16S rRNA gene**, for three reasons: it is short (about 1500 bases), so
cheap to sequence and analyze; it is highly conserved, because the ribosomal RNA it encodes has
strict folding requirements; and it is specific to prokaryotes, which lets it separate bacterial
signal from contaminating protist, fungal, plant or animal DNA in the same sample.

## Study 1: reading 2.5-billion-year-old ecology out of a gene tree

The first study opens from a line of Max Delbrück's: "any living cell carries with it the experience
of a billion years of experimentation by its ancestors." The claim behind it is that ancient,
large-scale environmental changes should leave a detectable signature in the genomes of organisms
alive today. The example used is the rise of atmospheric oxygen: oxygen, now essential to most
organisms, would have been acutely toxic to nearly all life before oxygenic photosynthesis
accumulated it, an event dated to roughly 2.4 billion years ago that reshaped life on Earth.

To read that history out of genomes, the study used a dynamic-programming algorithm that takes the
phylogeny of the species and the phylogeny of individual genes and infers, at every branch point,
the rates of four kinds of genetic change: gene birth, gene duplication, gene loss, and horizontal
gene transfer (HGT — a bacterium acquiring DNA from an unrelated lineage rather than from a parent
cell). Plotted as pie charts along the tree of prokaryotic life, the mix of events shifts sharply
over time: near the root, almost the whole pie is new-gene birth; from roughly 2.5 billion years ago
onward, duplication and horizontal transfer become the dominant slices. In other words, early
evolution reads as mostly *invention*, and later evolution as mostly *recombination and borrowing*
of genes that already exist.

A second figure zooms into the **Archean genetic expansion**, a spike of unusually large genetic
change during the Archean eon. Restricting to genes born specifically in that spike and asking what
enzymatic activities they carry (via enrichment of the metabolites those genes act on) points
overwhelmingly at oxidation-reduction chemistry and electron transport. Read together with dates,
the study's proposal is that life invented the modern electron transport chain around 3.3 billion
years ago, and by about 2.8 billion years ago had repurposed the same class of proteins used to
*produce* oxygen (photosynthesis) to instead *consume* it (respiration) — the genomic footprint of
learning to breathe the gas that had previously been a poison.

## Study 2: can community structure diagnose disease?

Inflammatory bowel disease (IBD) is dangerous to leave undiagnosed — untreated cases can end in
colon removal — but the most reliable diagnostic, colonoscopy, is invasive. The question this study
asks is whether the bacterial community composition of a stool sample can substitute.

105 stool samples were collected across a pediatric cohort with Crohn's disease (CD), ulcerative
colitis (UC), or neither (control). Abundance was compared group-by-group at two taxonomic
resolutions, phylum and genus. Only one single organism stood out as a candidate biomarker,
*E. coli*: essentially absent in control and CD samples, but present in roughly a third of UC
samples. That is not a usable diagnostic on its own — a marker with that little sensitivity
misclassifies most true cases. But feeding the *entire* abundance vector into a random forest
classifier, rather than looking for a single discriminating species, reached about 90% cross-validated
accuracy at telling diseased from healthy — competitive with the existing non-invasive tests,
which tend to be highly specific but not very sensitive.

The more general point sits underneath the classification result: the clearest difference between
healthy and diseased communities was not the presence of any one organism but a *drop in overall
ecosystem diversity*. That argues for thinking of IBD as a loss of ecosystem robustness and
resilience — many species interacting — rather than as an infection by a single germ.

## Study 3: perturbation and equilibrium in the Human Gut Ecology project

Because a direct signal between microbiome composition and disease is often weak, the Human Gut
Ecology (HuGE) project tried to remove one source of noise — diet and environment — by tracking it
directly. Two donors logged more than three hundred dietary and environmental variables daily
through a phone app (food eaten, sleep, mood, and so on) and gave a stool sample every day for a
year, so that a specific day's bacterial abundances could be tied to that day's recorded conditions.
With only two subjects, nothing here reaches population-level statistical significance, but the
design turns up two kinds of result: a quantitative dietary correlation, and two informative natural
perturbations.

The dietary result: fiber intake correlated with the abundance of specific taxa — Lachnospiraceae,
Bifidobacteria, and Ruminococcaceae. In one donor, a 10 g increase in daily fiber tracked with an
11% increase in the combined abundance of those groups. More generally, each donor's community
composition was stable over the course of the year but markedly different from the other donor's —
individuals carry a distinctive, largely self-similar microbial signature through time.

Reading hundreds of taxa's abundance across a year of daily samples is a plotting problem in its own
right, and the lecture's answer is the **horizon plot**: take one taxon's abundance deviation from
its own baseline over time, and instead of drawing it as a tall line that swings above and below
zero, fold it into a single thin strip. Bigger deviations get shaded more strongly; deviations below
baseline are folded up to sit on top of the baseline too, keeping only a marker of their original
sign. Doing this per taxon turns dozens of separate time-series plots into stacked rows that can be
scanned together.

<figure>
<svg viewBox="0 0 340 230" role="img" aria-label="How a horizon plot folds an abundance time series into a single coloured strip">
  <defs>
    <marker id="hp-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="70" x2="305" y2="70" stroke="currentColor" stroke-width="1"/>
  <text x="305" y="65" text-anchor="end" font-size="11" fill="currentColor">time</text>
  <rect x="45" y="40" width="30" height="30" fill="currentColor" fill-opacity="0.45"/>
  <rect x="85" y="70" width="30" height="20" fill="currentColor" fill-opacity="0.3"/>
  <rect x="125" y="15" width="30" height="55" fill="currentColor" fill-opacity="0.75"/>
  <rect x="165" y="70" width="30" height="35" fill="currentColor" fill-opacity="0.5"/>
  <rect x="205" y="55" width="30" height="15" fill="currentColor" fill-opacity="0.2"/>
  <rect x="245" y="70" width="30" height="15" fill="currentColor" fill-opacity="0.2"/>
  <text x="172" y="118" text-anchor="middle" font-size="11" fill="currentColor">raw abundance series</text>
  <line x1="172" y1="128" x2="172" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#hp-arrow)"/>
  <text x="185" y="142" font-size="11" fill="currentColor">fold</text>
  <rect x="45" y="160" width="30" height="25" fill="currentColor" fill-opacity="0.45"/>
  <rect x="85" y="160" width="30" height="25" fill="currentColor" fill-opacity="0.3"/>
  <rect x="125" y="160" width="30" height="25" fill="currentColor" fill-opacity="0.75"/>
  <rect x="165" y="160" width="30" height="25" fill="currentColor" fill-opacity="0.5"/>
  <rect x="205" y="160" width="30" height="25" fill="currentColor" fill-opacity="0.2"/>
  <rect x="245" y="160" width="30" height="25" fill="currentColor" fill-opacity="0.2"/>
  <circle cx="100" cy="167" r="2.5" fill="currentColor"/>
  <circle cx="180" cy="167" r="2.5" fill="currentColor"/>
  <circle cx="260" cy="167" r="2.5" fill="currentColor"/>
  <text x="172" y="205" text-anchor="middle" font-size="11" fill="currentColor">horizon plot: one strip per taxon</text>
</svg>
<figcaption>A horizon plot compresses one bacterial group's abundance deviation over time into a
single coloured strip: darker shading marks a bigger swing away from baseline, and a dot marks a
swing that was a decrease rather than an increase. Stacking one strip per taxon is how the lecture's
donor time-course figures (Figs. 6.4–6.7 in the source) fit hundreds of taxa on one page.</figcaption>
</figure>

Two events in the year of data illustrate different kinds of perturbation. One donor traveled to
Thailand; during the trip a large number of resident bacterial groups disappeared and several groups
normally considered pathogenic appeared, and on returning to the US the community reverted close to
its pre-trip state. The day-to-day correlation matrix confirms this: the pre-trip and post-trip
periods correlate strongly with *each other*, and only the trip itself stands apart — a temporary
displacement that springs back.

The other donor was infected with salmonella, and here the community did not revert. A large
fraction of resident groups went permanently extinct, and other bacteria took over their vacated
ecological niches; even though salmonella itself briefly dominated the population, total bacterial
counts before and after the infection were similar; what changed was *which* organisms held which
niche. The correlation matrix shows two internally-correlated blocks, pre-infection and
post-infection, with almost no correlation between them — the community moved to a genuinely
different equilibrium rather than being pushed and released. The general lesson: a perturbation can
either displace an ecosystem temporarily (it relaxes back once the perturbing factor is removed) or
tip it into a different stable configuration altogether (competitors permanently occupy the emptied
niches), and a strong enough shock does the latter.

## Study 4: the microbiome as a courier between diet and phenotype

A separate line of work asks whether the microbiome is the mechanism connecting diet to a downstream
phenotype, rather than just a bystander correlated with both. A cohort study of over a hundred
thousand patients modeled long-term weight change against reported food intake and found fast-food
items (processed meats, potato chips, sugar-sweetened drinks) positively correlated with obesity,
and yogurt consumption inversely correlated with it — in both a fast-food-heavy and a control diet
group, more yogurt tracked with less weight gain.

Controlled experiments push the correlation toward causation. Giving female mice purified
*Lactobacillus reuteri* — a bacterium found in yogurt — while letting them eat as much regular or
fast food as they liked produced significant weight loss relative to untreated mice on the same
diet, isolating the bacterium itself as sufficient to shift the phenotype, independent of the rest of
the diet. An unplanned second phenotype turned up alongside the weight effect: yogurt-fed mice (and
dogs) developed visibly shinier coats, and skin histology showed their hair follicles were more
actively cycling than controls' — a second, unrelated phenotype apparently mediated by the same
bacterial exposure.

## Study 5: horizontal gene transfer tracks ecology, not phylogeny

A striking single case sets up the general question: a gene that digests a sulfonated carbohydrate
found only in seaweed used to wrap sushi turns up in the gut microbiome of Japanese individuals but
not North Americans. The inferred history is that the gene moved from the alga itself into bacteria
living on the alga, and from there, by horizontal transfer, into the human gut microbiome of people
who eat it. The broader point is that a bacterial lineage resident in someone's gut for a lifetime is
not evolutionarily static — it can acquire new functions across that lifetime by picking up genes
tied to what its host eats.

To turn that anecdote into a systematic result, a related study screened roughly 2,000 published
bacterial genomes for genes that are essentially 100% identical between organisms classified in
different taxonomic groups — since two lineages that diverged long enough ago to look different by
16S sequence should not otherwise carry an *identical* gene, an exact match is strong evidence of a
recent horizontal transfer between them. This turned up around 100,000 such instances. Cross-referencing
the transfers against where each genome was isolated gave the paper's central finding: bacteria
isolated from humans share genes mostly with other human-associated bacteria; narrowing further,
gut-isolated bacteria share mostly with other gut bacteria, and skin-isolated bacteria mostly with
other skin bacteria. Quantitatively, two bacterial groups from humans that are at least 3% apart in
16S sequence (different taxonomic groups) still have roughly a 23% chance of sharing an identical
gene; if they were additionally isolated from the *same* body site, that rises to over 40%. Geography
is comparatively weak: bacteria sampled from the same continent transfer genes at roughly the same
rate as bacteria sampled from different continents. Taken together, these numbers argue that shared
*ecological niche* — not shared ancestry and not shared geography — is what predicts whether two
bacterial groups will exchange genes.

That framework has a direct public-health reading. Looking at transfer rates across a matrix of
human and non-human environments, transfers between the human microbiome and bacteria associated
with farm animals are somewhat elevated, and among *those specific transfers*, over 60% of the
genes involved are antibiotic-resistance genes — a genomic trace of subtherapeutic antibiotic use in
livestock feeding into resistance genes circulating in bacteria associated with humans.

## Study 6: the same signature nominates virulence genes in meningitis

Bacterial meningitis can be caused by a taxonomically diverse set of bacteria that share the ability
to enter the bloodstream and cross the blood-brain barrier; the goal here is to find what makes a
strain capable of that. The dataset was 70 strains isolated from meningitis patients, carrying
175,172 genes between them, of which about 24,000 had no known function — a pool of candidates that
could include both the drivers of meningitis-causing behavior and plausible drug targets.

Applying the same "exact match across distant taxa" screen used in Study 5 flagged 82 genes as
recent horizontal transfers. 69 of those had known functions, spanning antibiotic resistance,
detoxification, and recognizable virulence factors: hemolysin, which helps the bacterium survive in
the bloodstream, and adhesin, which lets it latch onto and cross the vein wall toward the blood-brain
barrier. The remaining 13 fell inside the 24,000 unannotated genes — so the HGT signature also serves
as a way of nominating candidate virulence genes among a genome's functionally unlabeled "dark
matter," rather than requiring that a gene's function be known before it can be flagged as
interesting.

## From the discussion

Three questions from the Q&A sharpen points made above.

Will the salmonella-infected donor's ecosystem eventually return to its pre-infection state? Not
without another large-scale change: the niches vacated during infection are now occupied by
competing bacterial groups, and those incumbents block the original occupants from simply moving
back in. This is the same competitive-exclusion logic that made the post-infection correlation block
different from the pre-infection one.

Did the salmonella infection kill off resident bacteria directly, or was it an immune response
fighting the infection that did so? The single observational dataset in Study 3 cannot distinguish
the two — it is one realized trajectory, not an experiment with a control. Settling it would need a
study that also tracks the immune system directly, for instance by drawing blood during the
infection.

Do twins have similar gut ecosystems because they share genes? The data argue against a genetic
explanation: monozygotic and dizygotic twins resemble each other to the same degree, and both
resemble their mother's community as well — regardless of whether the twins currently live together.
That pattern points instead to an early-life window in which the gut ecosystem is seeded and
"programmed," largely independent of host genotype.

## Current research directions

The lecture's own suggestion for extending Study 3 is to reproduce the salmonella perturbation in
mice, where higher temporal and spatial resolution sampling is feasible, in order to directly observe
the process of resident bacterial groups going extinct and being replaced by competitors occupying
their vacated niches — watching the equilibrium shift in Study 3 happen, rather than inferring it
from before-and-after snapshots.

## Sources

This chapter is drawn entirely from one document: the scribed notes for a guest lecture on
"Bacterial Genomics – Molecular Evolution at the Level of Ecosystems" by Eric Alm (scribed by Deniz
Yorukoglu, 2011), Chapter 6 of the compiled lecture-note volume for MIT OpenCourseWare 6.047/6.878
Computational Biology (Fall 2015). No separate slide deck, transcript, or problem set was supplied
for this chapter, and no exercises accompany it in the source, so none are added here.

The source file itself is a model's reconstruction of a PDF with no text layer (`fidelity:
reconstructed` in its front matter), so its prose is a paraphrase in places; this chapter follows
its content but should not be read as a verbatim quotation of the original scribed notes.

Figures the lecture displayed but that are not reproducible here: the tree-of-life pie-chart figure
of gene birth/duplication/loss/HGT rates and the Archean-expansion enrichment figure (Figs. 6.1–6.2);
the IBD phylum/genus abundance heatmap (Fig. 6.3); the donor abundance time courses, horizon-plot
legend, and day-to-day correlation matrices from the HuGE project, credited to the David lab
(Figs. 6.4–6.8); and the human/non-human horizontal-transfer rate matrices (Figs. 6.9–6.11), for
which the source points to Smillie et al., "Ecology drives a global network of gene exchange
connecting the human microbiome," *Nature* 480 (2011): 241–244, as showing comparable figures.

Studies cited by number in the original notes, carried through here: [1] The Human Microbiome
Jumpstart Reference Strains Consortium, "A Catalog of Reference Genomes from the Human Microbiome,"
*Science* 328 (2010): 994–999 (Study 5's genome set); [2] Lawrence A. David and Eric J. Alm, "Rapid
evolutionary innovation during an Archaean genetic expansion," *Nature* 469 (2011): 93–96 (Study 1);
[3] Hehemann et al., "Transfer of carbohydrate-active enzymes from marine bacteria to Japanese gut
microbiota," *Nature* 464 (2010): 908–912 (the seaweed-gene case in Study 5); [4] Mozaffarian et al.,
"Changes in diet and lifestyle and long-term weight gain in women and men," *New England Journal of
Medicine* 364 (2011): 2392–2404 (Study 4). The notes also point to the Human Microbiome Project
overview (commonfund.nih.gov/hmp) and a 16S rRNA tutorial (greengenes.lbl.gov) as further reading,
neither of which is reproduced here.

---

[← 11. Genome Alignment and Evolution](11-genome-alignment-and-evolution.md) · [Contents](index.md) · [13. HMM Posterior Decoding and Learning →](13-hmm-posterior-decoding-and-learning.md)
