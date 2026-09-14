---
title: 2. Molecular Dynamics
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Molecular Dynamics

**Source:** `recitations/2014-04-02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Calculate   force   field   between   all   atoms   in   protein   and surrounding   environment   (solvent,   lipid   bilayer,   etc.)

- From   force   field,   can   calculate   velocity, and   use   this   to   update   posi'ons   over very   small   'mescale (ti-­‐ti-­‐1   ~   femtoseconds):


( _t_ i ) = _x_ ( _t_ i-1) + _v_ ( _t_ i-1) × ( _t_ i �� _t_ i-1) � _U_ <u>(</u> _ti_ � <u>1)</u> _v_ ( _ti_ ) � _v_ ( _ti_ � 1) � � ( _ti_ � _ti_ � 1) _~~m~~_ • Then   recalculate   force   field   based   on

   - new   atomic   posi'ons, repeat…

- Very   computa' ~~onally exp~~ ensive   since pairwise   interac'ons   between thousands   of   atoms   at   each   'mestep   x billions   or   mo ~~re 'mesteps~~

Courtesy of Elmar Krieger, Yasara. Used with permission.

hRp://www.yasara.org/dhfr.gif

23

---

[← 1. Energy Minimiza'on](11-1-energy-minimiza-on.md) · [Up: contents](index.md) · [3. Simulated Annealing →](13-3-simulated-annealing.md)
