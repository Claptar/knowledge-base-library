---
title: "17. Michaelis-Menten Kinetics and Cooperativity"
course: "MIT 8.591J 2004"
chapter: 17
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Michaelis-Menten Kinetics and Cooperativity

## What this covers

This chapter answers two related questions. First, why does an enzyme-catalysed reaction saturate —
why does its rate rise linearly with substrate at low concentration and then level off, rather than
keep climbing — and what does the resulting Michaelis–Menten law mean physically. Second, when a
protein has several binding sites for the same ligand, when does the binding curve stay a simple
hyperbola and when does it turn sigmoidal (the signature of cooperativity), and how many genuinely
different ways are there to produce that sigmoid. Both questions are answered the same way: write
mass-action kinetics for a small reaction scheme, then solve it either in a steady state
(Michaelis–Menten) or in full equilibrium (binding and cooperativity). The chapter assumes only that
a reaction rate is proportional to the product of the reactant concentrations, and comfort setting
time derivatives to zero to find a steady or equilibrium state.

## The enzyme–substrate reaction and its kinetics

Enzymes are proteins that bind a substrate — another protein, a nucleic acid, or a small molecule —
and catalyse its conversion to a product without being consumed themselves. Three examples the
lecture uses to show the same scheme recurring: hexokinase converting glucose into
glucose-6-phosphate; RNA polymerase binding a promoter and transcribing it into mRNA; and the
phosphate CheZ converting the flagellar-motor regulator CheY into its phosphorylated form CheY-P.
All three fit the same two-step scheme: reversible binding of substrate and enzyme, followed by an
irreversible conversion to product,

$$\mathrm{E} + \mathrm{S} \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} \mathrm{ES} \xrightarrow{k_2} \mathrm{E} + \mathrm{P}$$

Note $k_1$ and $k_{-1}$ carry different units ($1/(\mathrm{M\,s})$ and $1/\mathrm{s}$), because the
first step depends on the product of two concentrations and the second on one. Mass action —
reaction rate proportional to the product of the concentrations of the reactants — turns this
scheme into four coupled ODEs:

$$\begin{aligned}
\frac{\mathrm{d}[\mathrm{S}]}{\mathrm{d}t} &= -k_1[\mathrm{E}][\mathrm{S}] + k_{-1}[\mathrm{ES}] \\
\frac{\mathrm{d}[\mathrm{E}]}{\mathrm{d}t} &= -k_1[\mathrm{E}][\mathrm{S}] + (k_{-1} + k_2)[\mathrm{ES}] \\
\frac{\mathrm{d}[\mathrm{ES}]}{\mathrm{d}t} &= k_1[\mathrm{E}][\mathrm{S}] - (k_{-1} + k_2)[\mathrm{ES}] \\
\frac{\mathrm{d}[\mathrm{P}]}{\mathrm{d}t} &= k_2[\mathrm{ES}] \equiv v
\end{aligned}$$

with initial conditions $[\mathrm{S}]_{t=0}=S_o$, $[\mathrm{E}]_{t=0}=E_o$,
$[\mathrm{ES}]_{t=0}=0$, $[\mathrm{P}]_{t=0}=0$. The turnover rate $v$, by definition, is how fast
product accumulates, and it is directly proportional to how much enzyme is currently tied up as
complex.

Because the enzyme is a catalyst, it is neither created nor destroyed — only shuttled between free
and bound forms — so the total enzyme concentration $E_o=[\mathrm{E}]+[\mathrm{ES}]$ is a conserved
quantity. Using it to eliminate $[\mathrm{E}]$ collapses the system to three equations:

$$\begin{aligned}
\frac{\mathrm{d}[\mathrm{S}]}{\mathrm{d}t} &= -k_1 E_o [\mathrm{S}] + (k_1[\mathrm{S}] + k_{-1})[\mathrm{ES}] \\
\frac{\mathrm{d}[\mathrm{ES}]}{\mathrm{d}t} &= k_1 E_o [\mathrm{S}] - (k_1[\mathrm{S}] + k_{-1} + k_2)[\mathrm{ES}] \\
\frac{\mathrm{d}[\mathrm{P}]}{\mathrm{d}t} &= k_2[\mathrm{ES}]
\end{aligned}$$

This system can be integrated exactly, and the lecture does so numerically (feeding
$k_1=10^3\,\mathrm{M^{-1}s^{-1}}$, $k_{-1}=1\,\mathrm{s^{-1}}$, $k_2=0.05\,\mathrm{s^{-1}}$,
$E_o=0.5\times10^{-3}\,\mathrm{M}$, $S_o=10^{-3}\,\mathrm{M}$ into an ODE solver) to see what the
concentrations actually do over time. The regime plotted is $k_1[S_o]\approx k_{-1}\gg k_2$ — binding
and unbinding equilibrate on a timescale much faster than turnover into product — which is also the
biologically relevant regime, since it is what makes an enzyme useful as a catalyst rather than a
one-shot reagent. Plotted on a log time axis, $[\mathrm{ES}]$ and $[\mathrm{E}]$ shoot to a plateau
almost immediately and then stay nearly flat while $[\mathrm{S}]$ slowly drains and $[\mathrm{P}]$
slowly fills — two clearly separated timescales.

There is a true equilibrium at $t\to\infty$: $[\mathrm{S}]=[\mathrm{ES}]=0$, $[\mathrm{E}]=E_o$,
$[\mathrm{P}]=S_o$ — everything has been converted. That end state is uninteresting; the useful
regime is the long, flat middle stretch where $[\mathrm{ES}]$ and $[\mathrm{E}]$ have already
settled down but $[\mathrm{S}]$ has barely moved. This is the **quasi-equilibrium** or
**pseudo-steady state**: after a short initial transient, complex is formed exactly as fast as it
breaks apart (in either direction), so $[\mathrm{ES}]$ holds nearly constant even while $[\mathrm{S}]$
and $[\mathrm{P}]$ are still slowly evolving.

## The quasi-steady-state approximation and the Michaelis–Menten law

Setting $\mathrm{d}[\mathrm{ES}]/\mathrm{d}t=\mathrm{d}[\mathrm{E}]/\mathrm{d}t=0$ in the reduced
system gives the complex concentration and turnover rate directly in terms of the *instantaneous*
substrate level:

$$[\mathrm{ES}] = \frac{k_1[\mathrm{S}]E_o}{k_1[\mathrm{S}] + k_{-1} + k_2}, \qquad
v = \frac{\mathrm{d}[\mathrm{P}]}{\mathrm{d}t} = \frac{k_2[\mathrm{S}]E_o}{\dfrac{k_{-1}+k_2}{k_1} + [\mathrm{S}]}$$

If substrate is in large excess over enzyme ($S_o\gg E_o$), this pseudo-steady state is reached
before any appreciable amount of substrate has been consumed, so $[\mathrm{S}]\approx S_o$ throughout
the approach to it. Substituting gives the **Michaelis–Menten equation** for the initial turnover
rate as a function of the initial substrate concentration:

$$v_o = \frac{v_{\max}S_o}{K_m+S_o}, \qquad K_m=\frac{k_{-1}+k_2}{k_1}, \qquad v_{\max}=k_2E_o$$

$K_m$, the **Michaelis constant**, has units of concentration and sets the scale of the curve: it
is the substrate concentration at which the rate is exactly half its maximum, $v(K_m)=\tfrac12
v_{\max}$. A *small* $K_m$ means strong affinity — the enzyme reaches half-saturation at low
substrate — and a large $K_m$ means weak affinity. $v_{\max}=k_2E_o$ is the rate once every enzyme
molecule is permanently tied up as complex, so it scales linearly with how much enzyme is present
and with how fast the catalytic step itself runs.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Michaelis-Menten rate as a saturating function of substrate concentration, with the half-maximal point at Km">
  <defs>
    <marker id="mmarrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="180" x2="308" y2="180" stroke="currentColor" stroke-width="1.5" marker-end="url(#mmarrow)"/>
  <line x1="40" y1="180" x2="40" y2="14" stroke="currentColor" stroke-width="1.5" marker-end="url(#mmarrow)"/>
  <text x="298" y="200" text-anchor="middle" font-size="12" fill="currentColor">[S]</text>
  <text x="22" y="24" text-anchor="middle" font-size="12" fill="currentColor">v</text>
  <line x1="40" y1="30" x2="300" y2="30" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="303" y="34" font-size="12" fill="currentColor">v_max</text>
  <line x1="40" y1="105" x2="92" y2="105" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="92" y1="105" x2="92" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <circle cx="92" cy="105" r="2.5" fill="currentColor"/>
  <text x="92" y="195" text-anchor="middle" font-size="12" fill="currentColor">K_m</text>
  <path d="M40,180 L53,150 L66,130 L79,115.7 L92,105 L118,90 L144,80 L170,73 L196,67.5 L222,63.3 L248,60 L274,57.3 L300,55" fill="none" stroke="currentColor" stroke-width="2"/>
</svg>
<figcaption>The Michaelis-Menten rate law: v rises almost linearly at low [S], then bends over toward
v_max as the enzyme runs out of free sites to bind more substrate. K_m is read off as the
substrate concentration at half-height.</figcaption>
</figure>

## Multiple binding sites and Adair's equation

The Michaelis–Menten picture has one substrate per enzyme. Many proteins carry several binding
sites for the same ligand — haemoglobin's four oxygen sites are the standard example — and here the
question shifts from *kinetics* (how fast does turnover happen) to *equilibrium binding* (how much
ligand is bound at a given free ligand concentration). Write $\mathrm{P}_j$ for the protein bound to
$j$ of its $n$ sites, so ligand binds and unbinds one at a time,

$$\mathrm{S} + \mathrm{P}_{j-1} \leftrightarrow \mathrm{P}_j, \qquad j=1,\dots,n$$

For the first step, mass action gives $\mathrm{d}[\mathrm{P}_0]/\mathrm{d}t = -k_{+1}[\mathrm{P}_o][\mathrm{S}] + k_{-1}[\mathrm{P}_1]$,
and at steady state this defines an association constant $K_a=k_{+1}/k_{-1}=[\mathrm{P}_1]/([\mathrm{P}_o][\mathrm{S}])$
(its reciprocal, $K_d$, is the dissociation constant). More generally each of the $n$ steps has its
own **stepwise association constant**

$$K_j = \frac{[\mathrm{P}_j]}{[\mathrm{P}_{j-1}][\mathrm{S}]}, \qquad j=1,\dots,n$$

The individual $[\mathrm{P}_j]$ are hard to measure directly; what an experiment actually reports is
the average number of ligands bound per protein,

$$r = \frac{[\mathrm{P}_1]+2[\mathrm{P}_2]+\dots+n[\mathrm{P}_n]}{[\mathrm{P}_o]+[\mathrm{P}_1]+\dots+[\mathrm{P}_n]}$$

Substituting the $K_j$'s expresses $r$ purely in terms of the association constants and the free
ligand concentration — **Adair's equation**:

$$r = \frac{K_1[\mathrm{S}] + 2K_1K_2[\mathrm{S}]^2 + \dots + nK_1K_2\cdots K_n[\mathrm{S}]^n}
{1 + K_1[\mathrm{S}] + K_1K_2[\mathrm{S}]^2 + \dots + K_1K_2\cdots K_n[\mathrm{S}]^n}$$

Since $0<r<n$, it is common to normalise to the **saturation function** $Y=r/n\in(0,1)$, the
fraction of all sites occupied. Adair's equation is the exact, general statement for $n$ sites; the
rest of the chapter is about what happens to it under different assumptions about how the $K_j$
relate to one another.

## Identical, independent binding sites

Suppose the $n$ sites are chemically identical and bind completely independently — occupying one
site has no effect on any other. Then a single pair of rate constants $k_+,k_-$ describes binding
and unbinding at *any* site, and the stepwise constants $K_j$ differ from each other only through
combinatorics: going from $\mathrm{P}_0$ to $\mathrm{P}_1$, there are $n$ empty sites the incoming
ligand could land on, but only one way to leave $\mathrm{P}_1$ back to $\mathrm{P}_0$; going from
$\mathrm{P}_1$ to $\mathrm{P}_2$ there are $(n-1)$ empty sites left but $2$ ways to lose one of the
two occupied ones. Writing the intrinsic constant as $K\equiv k_+/k_-$, steady state at each step
gives $K_1=nK$, $K_2=(n-1)K/2$, and in general

$$K_j = \frac{(n-j+1)K}{j}, \qquad j=1,\dots,n$$

Feeding this into Adair's equation and summing the resulting binomial series (the lecture points to
Bisswanger 2002, p. 11–16 for the algebra) collapses the whole sum to one hyperbola:

$$r = \frac{nK[\mathrm{S}]}{1+K[\mathrm{S}]}$$

This has exactly the shape of the Michaelis–Menten curve, but it is a fundamentally different
object: it is an **equilibrium** relation between bound ligand and free ligand concentration, not a
**steady-state kinetic** rate. The same result falls out with no combinatorics at all if the sites
are treated as an undifferentiated pool rather than as clustered on one protein — which is legitimate
precisely because they are independent. Let $[\mathrm{F}]$ and $[\mathrm{B}]$ be the concentrations
of free and bound sites; the association constant for this one-site-at-a-time equilibrium is
$K=[\mathrm{B}]/([\mathrm{F}][\mathrm{S}])$, and with $n[\mathrm{P}]=[\mathrm{F}]+[\mathrm{B}]$ as
the total site count, $r=[\mathrm{B}]/[\mathrm{P}]$ reduces to the same hyperbola. The two
derivations agreeing is itself informative: independence is what let the many-site problem collapse
back to a one-site problem.

## Non-identical, independent binding sites

If instead the $n$ sites fall into families — $n_1$ sites with constant $K_1$, $n_2$ with $K_2$, and
so on — independence still lets each family be treated on its own, and $r$ is just their sum:

$$r = \frac{n_1K_1[\mathrm{S}]}{1+K_1[\mathrm{S}]} + \frac{n_2K_2[\mathrm{S}]}{1+K_2[\mathrm{S}]} + \dots$$

At low ligand concentration the high-affinity family fills first; only at higher $[\mathrm{S}]$ does
the low-affinity family start to fill. The binding curve is still a sum of hyperbolas — never
sigmoidal — because nothing here couples one site's occupancy to another's.

## Two interacting sites: cooperativity

Sigmoidal binding needs sites that talk to each other: occupying one site changes the affinity of
the others. Restrict to the simplest case, $n=2$, with both sites identical. There are three states
— $\mathrm{P}_0$, $\mathrm{P}_1$, $\mathrm{P}_2$ — and now *two* intrinsic constants: $K=k_+/k_-$ for
the empty-to-singly-bound transition, and $K^*=k_+^*/k_-^*$ for the singly-bound-to-doubly-bound
transition, allowed to differ because the second binding event happens on a protein already
occupied at the other site. The combinatorial factors from the identical-independent case still
apply ($K_1=2K$, $K_2=\tfrac12K^*$), so Adair's equation for $n=2$ gives

$$r = \frac{2K[\mathrm{S}]+2KK^*[\mathrm{S}]^2}{1+2K[\mathrm{S}]+KK^*[\mathrm{S}]^2}, \qquad
Y=\frac{r}{2}=\frac{K[\mathrm{S}]+KK^*[\mathrm{S}]^2}{1+2K[\mathrm{S}]+KK^*[\mathrm{S}]^2}$$

If $K=K^*$ — the second site is exactly as easy to bind as the first — this reduces to the ordinary
hyperbola $\tilde Y=K[\mathrm{S}]/(1+K[\mathrm{S}])$, the $n=2$ independent case. The deviation from
that hyperbola is what cooperativity is:

$$Y-\tilde Y = \frac{(K^*-K)K[\mathrm{S}]^2}{(1+K[\mathrm{S}])(1+2K[\mathrm{S}]+KK^*[\mathrm{S}]^2)}$$

**Positive cooperativity** is defined as $Y>\tilde Y$, equivalently $K^*>K$: binding the first
ligand makes the second site *more* attractive. **Negative cooperativity** is $Y<\tilde Y$, i.e.
$K^*<K$ — the first binding event makes the second harder.

## Two ways to define cooperativity: affinity shift versus sigmoidicity

The affinity-shift definition above ($K^*$ vs $K$) is not the only one in use. A second, older
definition calls a curve cooperative when it is genuinely **sigmoidal** — S-shaped — which happens
exactly when the second derivative of $Y$ with respect to $[\mathrm{S}]$ changes sign. Writing
$x=K[\mathrm{S}]$ and $\beta=K^*/K$ as dimensionless variables,

$$Y=\frac{x(1+\beta x)}{1+2x+\beta x^2}, \qquad
\frac{\mathrm{d}Y}{\mathrm{d}x}=\frac{1+2\beta x+\beta x^2}{(1+2x+\beta x^2)^2}, \qquad
\frac{\mathrm{d}^2Y}{\mathrm{d}x^2}=2\,\frac{\beta-2-\beta x\left[3+3\beta x+\beta x^2\right]}{(1+2x+\beta x^2)^3}$$

Working through when the numerator of the second derivative can change sign shows it needs
$\beta>2$, not merely $\beta>1$. So the two definitions genuinely disagree: by the affinity-shift
definition any $K^*>K$ ($\beta>1$) counts as cooperative, but the curve is only visibly sigmoidal
once $\beta>2$. The chapter — and the rest of the course — sticks with the first, affinity-shift
definition, but it is worth knowing the second exists and sets a stricter bar.

## The Hill limit and the Hill number

A useful limiting case is when the singly-bound state is so unstable that it is essentially never
observed — binding is effectively all-or-nothing, $\mathrm{P}_0+2\mathrm{S}\leftrightarrow
\mathrm{P}_2$ directly. Then

$$Y = \frac{K[\mathrm{S}]^2}{1+K[\mathrm{S}]^2}, \qquad K=\frac{[\mathrm{P}_2]}{[\mathrm{P}_o][\mathrm{S}]^2} \ \ (\text{units } \mathrm{M}^{-2})$$

Hill's device for reading off this kind of relation from data is the **Hill plot**: plot
$\ln[Y/(1-Y)]$ against $\ln[\mathrm{S}]$. Its slope is the **Hill number** $n_H$, which for the
all-or-nothing limit above is exactly $2$ — matching the number of sites, which is exactly why the
Hill number is often quoted as an *estimate* of site count. That estimate is only as good as the
all-or-nothing assumption behind it. Allowing the intermediate, singly-bound state back in (the full
two-site cooperative model above) gives instead

$$n_H = \frac{\mathrm{d}}{\mathrm{d}(\ln[\mathrm{S}])}\ln\!\left[\frac{Y}{1-Y}\right]
= x\frac{\mathrm{d}}{\mathrm{d}x}\ln\!\left[\frac{Y}{1-Y}\right]
= 1+\frac{(\beta-1)x}{(1+x)(1+\beta x)}$$

which only *approaches* $2$ in the double limit of large $\beta$ and small $x$, and sits below $2$
everywhere else — reaching $1$ (no cooperativity) when $\beta=1$. So a measured Hill number between
$1$ and the true site count is completely normal for a real, intermediate-allowing cooperative
protein; it is a lower bound on cooperativity, not a literal site count, unless the all-or-nothing
assumption actually holds.

## Non-identical, interacting sites

The most general two-site case drops both simplifications at once: the two sites can differ *and*
interact. There are still four states, but now the two singly-bound states — call them
$\mathrm{P}_1$ (site 1 occupied) and $\mathrm{P}_1'$ (site 2 occupied) — are distinct, each reachable
from $\mathrm{P}_0$ by binding at one particular site, and each able to proceed to the fully-bound
state $\mathrm{P}_2$ by binding at the other. Four intrinsic constants $K_1,K_2,K_3,K_4$ describe the
four edges of this diagram:

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Four-state binding diagram for two non-identical interacting sites, showing the two routes from empty to fully bound protein">
  <defs>
    <marker id="diamondarrow" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
      <polygon points="0,0 7,3.5 0,7" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="160" cy="190" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="194" text-anchor="middle" font-size="12" fill="currentColor">P_0</text>
  <circle cx="60" cy="105" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="109" text-anchor="middle" font-size="12" fill="currentColor">P_1</text>
  <circle cx="260" cy="105" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="260" y="109" text-anchor="middle" font-size="12" fill="currentColor">P_1'</text>
  <circle cx="160" cy="25" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="29" text-anchor="middle" font-size="12" fill="currentColor">P_2</text>
  <line x1="146" y1="174" x2="76" y2="122" stroke="currentColor" stroke-width="1.3" marker-end="url(#diamondarrow)"/>
  <text x="90" y="158" font-size="12" fill="currentColor">K_1</text>
  <line x1="174" y1="174" x2="244" y2="122" stroke="currentColor" stroke-width="1.3" marker-end="url(#diamondarrow)"/>
  <text x="215" y="158" font-size="12" fill="currentColor">K_2</text>
  <line x1="76" y1="88" x2="146" y2="38" stroke="currentColor" stroke-width="1.3" marker-end="url(#diamondarrow)"/>
  <text x="90" y="58" font-size="12" fill="currentColor">K_3</text>
  <line x1="244" y1="88" x2="174" y2="38" stroke="currentColor" stroke-width="1.3" marker-end="url(#diamondarrow)"/>
  <text x="205" y="58" font-size="12" fill="currentColor">K_4</text>
</svg>
<figcaption>Two routes from empty (P_0) to fully-bound (P_2): via site 1 first (K_1 then K_3) or via
site 2 first (K_2 then K_4). Detailed balance forces the product around the loop to agree either
way, K_1K_3 = K_2K_4, so only three of the four constants are independent.</figcaption>
</figure>

$$K_1=\frac{[\mathrm{P}_1]}{[\mathrm{P}_o][\mathrm{S}]}, \quad
K_2=\frac{[\mathrm{P}_1']}{[\mathrm{P}_o][\mathrm{S}]}, \quad
K_3=\frac{[\mathrm{P}_2]}{[\mathrm{P}_1][\mathrm{S}]}, \quad
K_4=\frac{[\mathrm{P}_2]}{[\mathrm{P}_1'][\mathrm{S}]}$$

Because this is a true thermodynamic equilibrium, there can be no net circulation around the loop —
the two routes from $\mathrm{P}_0$ to $\mathrm{P}_2$ must be consistent, which forces
$K_1K_3=K_2K_4$: only three of the four constants are free. Writing the saturation function out and
using that constraint to eliminate $K_4$,

$$Y = \frac{K_1[\mathrm{S}]+K_2[\mathrm{S}]+2K_1K_3[\mathrm{S}]^2}{1+K_1[\mathrm{S}]+K_2[\mathrm{S}]+K_1K_3[\mathrm{S}]^2}$$

which, as detailed balance guarantees, does not depend on $K_4$ at all. Defining effective constants

$$J=\tfrac12(K_1+K_2), \qquad J^*=\frac{2K_1K_3}{K_1+K_2}, \qquad x'=J[\mathrm{S}], \qquad \beta'=\frac{J^*}{J}$$

puts $Y$ back into exactly the same universal shape as the identical-sites case,
$Y=x'(1+\beta'x')/(1+2x'+\beta'x'^2)$. Two limits check that this is the right generalisation: if
$K_1=K_2$ the two sites are equally easy to bind first, and $x'=x$, $\beta'=\beta$ recovers the
identical-interacting-sites result exactly; if instead $K_1=K_3$ and $K_2=K_4$ — each site's affinity
is unaffected by whether the other is occupied — the whole thing collapses back to the sum of two
independent hyperbolas, $Y=K_1[\mathrm{S}]/(1+K_1[\mathrm{S}])+K_2[\mathrm{S}]/(1+K_2[\mathrm{S}])$
divided appropriately, and in that case

$$\beta' = \frac{4K_1K_2}{(K_1+K_2)^2} = \frac{4K_1K_2}{4K_1K_2+(K_1-K_2)^2} \le 1$$

with equality only when $K_1=K_2$. This is the sting in the tail: $\beta'<1$ — which reads as
*negative* cooperativity under the affinity-shift definition — is exactly what two genuinely
**independent but non-identical** sites also produce. A binding curve that looks like mild negative
cooperativity cannot, from its shape alone, distinguish "two sites that don't talk to each other but
have different affinities" from "two sites that do talk to each other and the second binding event
is discouraged." Telling those apart needs more than the equilibrium binding curve.

## Sources

- MIT OCW 8.591J *Systems Biology* (Fall 2004), lecture 2 handout, reconstructed transcript,
  section **I "Michaelis-Menten kinetics"** — the enzyme–substrate scheme, the reduced ODEs, the
  quasi-steady-state derivation and the Michaelis–Menten law (equations I.1–I.6 in the source), plus
  the MATLAB simulation described there
  (`docs/computational-biology/mit-ocw/8591j-2004/recordings/l2-syllabus-transcript/01-i-michaelis-menten-kinetics.md`).
- Same lecture, section **II "Equilibrium binding and cooperativity"** — multiple binding sites,
  Adair's equation, identical/non-identical and independent/interacting sites, the two definitions
  of cooperativity, the Hill limit and Hill number, and the non-identical interacting-sites diagram
  (equations II.1–II.31 in the source)
  (`docs/computational-biology/mit-ocw/8591j-2004/recordings/l2-syllabus-transcript/02-ii-equilibrium-binding-and-cooperativity.md`).
- Both files are model reconstructions of a PDF with no text layer; their own banner flags every
  equation in them as unverified, so this chapter should be read as a guide back to the original
  8.591J lecture 2 handout, not as a citable derivation in its own right.
- The lecture points to, but does not itself reproduce, the combinatorial derivation of the
  identical-independent-sites result: H. Bisswanger, *Enzyme Kinetics* (Wiley-VCH, 2002), pp. 11–16.
  It also names, without drawing on directly, D. Fell, *Understanding the Control of Metabolism*
  (Portland Press, 1997); J. D. Murray, *Mathematical Biology* (Springer-Verlag, 1989); and L. A.
  Segel, *Biological Kinetics* (Cambridge University Press, 1991), as further reading on enzyme
  kinetics and cooperativity.
- No slides, written notes or exercise sets were supplied for this lecture, so there is no
  Exercises section.

---

[← 16. Drosophila Morphogen Gradients and Robustness](16-drosophila-morphogen-gradients-and-robustness.md) · [Contents](index.md) · [18. Genetic Switch in Phage Lambda →](18-genetic-switch-in-phage-lambda.md)
