---
title: "16. Drosophila Morphogen Gradients and Robustness"
course: "MIT 8.591J 2004"
chapter: 16
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Drosophila Morphogen Gradients and Robustness

## What this covers

This is the closing lecture of the course, and it does two things at once: it steps back to name the
methodological pattern the whole term has been an example of, and it applies that pattern to a new setting —
a multicellular embryo rather than a single reacting or gradient-sensing cell. The worked example is
*Drosophila* early development: how a single fertilized egg reads spatial information laid down by its
mother, and how that reading is made to be either dosage-sensitive or dosage-robust depending on the
molecular circuit doing the reading. The chapter assumes the reaction-diffusion language used earlier for
chemotaxis and gradient sensing — a partial differential equation with a diffusion term and reaction terms —
and the general idea of a steady-state gradient set up by production, degradation and diffusion.

## The course's throughline, recapped

The course is organized around three successively larger pictures of a cell:

- **The cell as a well-stirred biochemical reactor** (13 lectures): chemical kinetics, equilibrium binding
  and cooperativity; the lambda phage switch; stability analysis; genetic switches; *E. coli* chemotaxis;
  genetic oscillators; stochastic chemical kinetics.
- **The cell as a compartmentalized system with concentration gradients** (9 lectures): diffusion and
  Fick's equations with boundary and initial conditions; local-excitation/global-inhibition theory; models
  of eukaryotic gradient sensing; center-finding algorithms; cytoskeleton dynamics.
- **The cell in a social context, communicating with its neighbours** (2 lectures): quorum sensing, and
  *Drosophila* development — the subject of this chapter.

Across all three, the lecture names the same four-step pattern as the actual content of the course, not
just its structure:

1. **Translate the biology into a quantitative model** — given the biological phenomenon, write down the
   coupled differential equations that capture its essence. This step is not mechanical: four different
   papers can propose four different models of the *same* phenomenon, because which simplifying assumptions
   to make is itself the hard, and consequential, decision.
2. **Analyze the resulting system** — stability analysis, in both space and time.
3. **Interpret the mathematical analysis biologically** — for instance, what does a nonzero imaginary part
   of an eigenvalue mean for the underlying biology (oscillation, in the usual case)?
4. **Build a general taste for when this kind of approach is worth reaching for**, on problems not yet
   encountered.

The rest of this chapter is one worked pass through that pattern, on a system where the answer to step 1
turns out to matter enormously.

## From single cells to a developing embryo

*Drosophila melanogaster* — the fruit fly — is the model organism for this last topic. Its major experimental
advantage is that the body plan is laid down as a series of visible stripes in the early embryo, and each
stripe corresponds to a recognizable body segment in the adult fly: patterning can be watched directly,
rather than inferred. (The lecture points to the recommended book, *The Making of a Fly* by Peter Lawrence,
and to a movie resource at flymove.uni-muenster.de, for the developmental sequence itself — neither is
reproduced here.)

## The bicoid gradient and its zygotic reading

The idea that a spatial concentration gradient of a single molecule could specify position along an embryo
goes back to pioneering ligation and transplantation experiments — Klaus Sander's 1958 work on leafhoppers is
cited as the origin. Cutting an embryo and moving or removing material from its poles changed the resulting
pattern in a way that pointed to **morphogens**: substances created and destroyed at the embryo's poles,
whose local concentration tells a cell where it is.

The first morphogen actually identified in *Drosophila* is **bicoid**, and it is a *maternal* factor — its
mRNA is deposited in the egg by the mother, not transcribed by the embryo itself. Two pieces of evidence
make the case:

- Transplanting bicoid can rescue development in embryos that otherwise lack it.
- Increasing the number of bicoid gene copies in the mother shifts the position of the resulting head fold.
  The pattern boundary moves with the *dose* of the gradient-forming gene — direct evidence that concentration,
  not just presence or absence, carries positional information.

The embryo itself then has to *read* this maternally supplied gradient. That reading is a **zygotic** effect
— gene expression carried out by the embryo's own genome, in response to the graded maternal signal — and the
gene doing the reading is **hunchback**, whose expression domain is set by the local bicoid concentration.

A quantitative study of exactly this bicoid–hunchback relationship is cited: Houchmandzadeh et al., *Nature*
415, 798 (2002). The lecture poses the question the paper is aimed at, and leaves it open: bicoid concentration
is a noisy signal, egg to egg and even within one egg, so **how does a noisy, continuously graded bicoid
profile get converted into a sharp step in hunchback expression, positioned reliably at the middle of the
embryo?** As the slide puts it — nobody knows.

## A gradient built to be robust: Sog, Scw and Tld

The bicoid/hunchback story is one instance of reading a morphogen gradient; a second example, from Eldar et
al., *Nature* 419, 304 (2002), asks a related but different question — not how a gradient is read, but how a
gradient's *shape* can be made insensitive to changes in the amounts of the molecules that build it. This is
the same robustness question the course raised earlier for *E. coli* chemotaxis (L9–10): a circuit is
"robust" if its output pattern is unchanged even when the underlying reaction rates or protein doses vary.

Three molecules are involved:

- **Scw** — a BMP (bone morphogenetic protein) ligand: the actual signal.
- **Sog** — a BMP inhibitor: it binds Scw and blocks its signalling.
- **Tld** — a protease: it cleaves Sog, and in doing so can free the ligand it was holding.

<figure>
<svg viewBox="0 0 420 230" role="img" aria-label="Reaction scheme linking free Sog, free Scw and the Sog–Scw complex, with Tld acting on both">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="95" width="90" height="40" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="65" y="119" text-anchor="middle" font-size="13" fill="currentColor">Sog</text>
  <rect x="310" y="95" width="90" height="40" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="355" y="119" text-anchor="middle" font-size="13" fill="currentColor">Scw</text>
  <rect x="150" y="20" width="120" height="40" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="210" y="44" text-anchor="middle" font-size="13" fill="currentColor">Sog&#8211;Scw complex</text>
  <line x1="110" y1="105" x2="150" y2="45" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="112" y="65" font-size="11" fill="currentColor">k_b [Sog][Scw]</text>
  <line x1="200" y1="60" x2="140" y2="112" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="140" y="88" font-size="11" fill="currentColor">k&#8722;b</text>
  <line x1="270" y1="45" x2="330" y2="105" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="295" y="65" font-size="11" fill="currentColor">&#955;[Tld]</text>
  <text x="295" y="80" font-size="10" fill="currentColor">releases Scw</text>
  <line x1="65" y1="135" x2="65" y2="185" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="70" y="205" font-size="11" fill="currentColor">&#945;[Tld][Sog]: Sog degraded directly</text>
</svg>
<figcaption>The three reaction terms in the model: Sog and Scw bind reversibly ($k_b$, $k_{-b}$) into a
complex; Tld can cleave that complex, freeing active Scw ($\lambda$ term); and Tld can also degrade free
Sog directly ($\alpha$ term). Each species also diffuses in space (not shown).</figcaption>
</figure>

Each of the three species — free Sog, free Scw, and the Sog–Scw complex — both diffuses in space and
reacts, giving the full model:

$$
\frac{\partial [Sog]}{\partial t} = D_S \frac{\partial^2 [Sog]}{\partial x^2} - k_b [Sog][Scw] + k_{-b}[Sog\text{-}Scw] - \alpha [Tld][Sog]
$$

$$
\frac{\partial [Scw]}{\partial t} = D_{BMP} \frac{\partial^2 [Scw]}{\partial x^2} - k_b [Sog][Scw] + k_{-b}[Sog\text{-}Scw] + \lambda [Tld][Sog\text{-}Scw]
$$

$$
\frac{\partial [Sog\text{-}Scw]}{\partial t} = D_C \frac{\partial^2 [Sog\text{-}Scw]}{\partial x^2} + k_b [Sog][Scw] - k_{-b}[Sog\text{-}Scw] - \lambda [Tld][Sog\text{-}Scw]
$$

Read term by term: Sog is lost by binding Scw, gained back when the complex unbinds, and lost again by
being directly degraded by Tld. Scw is lost by binding Sog, gained back by unbinding, and — crucially —
also *gained* when Tld cleaves the complex and releases active ligand. The complex is gained by binding and
lost by unbinding or by Tld cleavage.

The question the lecture asks of this model is why the resulting Scw gradient should be *robust* — insensitive
to changes in how much Sog or Scw is produced. The slide answers it by passing to an idealized limit: set
$D_{BMP} = 0$ (free ligand does not diffuse on its own — only the complex carries it through the tissue),
$\alpha = 0$ (Tld does not degrade free Sog directly), and $k_{-b} = 0$ (binding of Sog to Scw is effectively
irreversible on the relevant timescale). In that limit the steady-state ($\partial/\partial t = 0$) balance
equations reduce to

$$
0 = D_S \frac{\partial^2 [Sog]}{\partial x^2} - k_b [Sog][Scw]
$$

$$
0 = -k_b [Sog][Scw] + \lambda [Tld][Sog\text{-}Scw] \;\longrightarrow\; \frac{\partial^2}{\partial x^2}\frac{1}{[Scw]} = \frac{k_b}{D_S}
$$

$$
0 = D_C \frac{\partial^2 [Sog\text{-}Scw]}{\partial x^2} + k_b [Sog][Scw] - \lambda [Tld][Sog\text{-}Scw]
$$

The point of that middle line is what carries the argument: the curvature of $1/[Scw]$ in space is set
entirely by $k_b/D_S$ — a ratio built only from Sog's own diffusion constant and its binding rate to Scw. It
does not involve the total amount of Sog, Scw or Tld present. Scaling the production of Sog and Scw up or
down together (a change in gene dosage) changes their absolute levels but not this ratio, so the *shape* of
the resulting Scw gradient is unchanged. That is the sense in which the circuit is robust — and it is a
direct structural consequence of the assumption that the ligand only moves through the tissue while bound to
its own inhibitor, rather than diffusing freely on its own.

(The slide does not show the algebra connecting the general model to this reduced pair of equations, and the
source markdown for this lecture flags every displayed equation as unverified — treat the derivation above
as the conclusion the lecture states, not as a step-by-step proof to reproduce independently.)

Set side by side, the two case studies in this chapter make almost opposite points about morphogen gradients:
bicoid is read in a way that is exquisitely *sensitive* to dose — an extra gene copy visibly shifts the
pattern — while the Sog/Scw/Tld circuit is built, by the shuttling logic above, to be *insensitive* to dose.
Which behaviour a real gradient shows is a property of the circuit reading or building it, not of gradients
in general.

## Sources

- Course roadmap, module structure and the four take-home messages:
  `lectures/25-notes` (slide 1), "I Systems Microbiology (13 Lectures)" / "II Systems Cell Biology (9
  Lectures)" / "III Systems Developmental Biology (2 Lectures)".
- *Drosophila* introduction, Sander's leaf-hopper experiments, bicoid, hunchback, and the open question about
  a noisy gradient producing a sharp boundary: `lectures/25-notes` (slide 2), "Developmental Systems Biology".
- Cited papers, referred to but not contained in the slides: Houchmandzadeh, Wieschaus, Leibler et al.,
  *Nature* 415, 798 (2002), on the bicoid–hunchback relationship; Eldar et al., *Nature* 419, 304 (2002), on
  robustness of *Drosophila* dorsal–ventral patterning.
- Also referred to but not contained: *The Making of a Fly*, Peter Lawrence (recommended book), and the
  developmental-sequence movie at flymove.uni-muenster.de.
- No transcript, written notes, or exercises were supplied for this lecture; the source slide markdown notes
  that it was reconstructed by a model from a PDF with no text layer and that every displayed equation is
  unverified, which this chapter has followed but not independently checked.

---

[← 15. Quorum Sensing and Cell-Cell Communication](15-quorum-sensing-and-cell-cell-communication.md) · [Contents](index.md) · [17. Michaelis-Menten Kinetics and Cooperativity →](17-michaelis-menten-kinetics-and-cooperativity.md)
