---
title: L9 syllabus transcript
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l9-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# L9 syllabus transcript

**Source:** `recordings/l9-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **VII Biological Oscillators**

During class we consider the following two coupled differential equations:


From the phase plane analysis (see L9_notes.pdf) it was clear that for certain values of a and b this system exhibits periodic oscillations as a function of time. Let us analyze [VII.1] in more detail. The nullclines are:


**[VII.2]**

There is only one fixed point (x<sup>*</sup> ,y<sup>*</sup> ):


**[VII.3]**

The matrix A is (using [V.4] and [V.5]):


**[VII.4]**

The determinant and trace are:


The fixed point is stable when τ < 0. The region in a-b-parameter space where the system is oscillating (stable limit cycle) and is not oscillating (stable fixed point) is illustrated in Fig. 10.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

35


**Figure 11.** a-b-parameter space indicating for which values of a and b the system exhibits stable oscillations and a stable fixed point

**MATLAB code 5** : Limit cycle

% filename: cyclefunc.m function dydt = f(t,y,flag,a,b) dydt = [-y(1)+a*y(2)+y(1)*y(1)*y(2); b-a*y(2)-y(1)*y(1)*y(2)]; plot(y(1),y(2),'.'); drawnow; hold on; axis([0 2 0 2]);

% filename: limitcycle.m close; clear; a=0.1; b=0.5; options=[]; [t y]=ode23('cyclefunc',[0 50],[0.6 1.4],options,a,b); plot(y(:,1),y(:,2));

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

36

---

[Up: contents](../index.md)
