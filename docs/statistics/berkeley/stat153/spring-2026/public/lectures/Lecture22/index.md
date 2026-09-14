---
title: Lecture 22 - Kalman Filter and 2D Tracking
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture22.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 22 - Kalman Filter and 2D Tracking

**Source:** [`public/lectures/Lecture22.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Split into 20 sections.

1. [Lecture 22 - Kalman Filter and 2D Tracking](01-lecture-22---kalman-filter-and-2d-tracking.md)
2. [def gentruth(N=60)](02-def-gentruth-n-60.md)
3. [Lecture 22 — Part 03 —](03-lecture-22-part-03.md)
4. [Generate a more complex trajectory](04-generate-a-more-complex-trajectory.md)
5. [Lecture 22 — Part 05 —](05-lecture-22-part-05.md)
6. [s = np.linspace(0, 1, N)](06-s-np-linspace-0-1-n.md)
7. [x = 2 np.cos(2.3 np.pi s) + 1 s](07-x-2-np-cos-2-3-np-pi-s-1-s.md)
8. [y = 2 np.sin(1.3 np.pi s) - 1 s](08-y-2-np-sin-1-3-np-pi-s---1-s.md)
9. [return np.stack([x, y], axis=1)](09-return-np-stack-x-y-axis-1.md)
10. [def gentruth(N=60)](10-def-gentruth-n-60.md)
11. [Lecture 22 — Part 11 —](11-lecture-22-part-11.md)
12. [Linear trajectory (constant velocity)](12-linear-trajectory-constant-velocity.md)
13. [Lecture 22 — Part 13 —](13-lecture-22-part-13.md)
14. [s = np.linspace(0, 1, N)](14-s-np-linspace-0-1-n.md)
15. [x = s](15-x-s.md)
16. [y = 3x + 0.3](16-y-3x-0-3.md)
17. [return np.stack([x,y], axis=1)](17-return-np-stack-x-y-axis-1.md)
18. [Filler text](18-filler-text.md)
19. [This seems to help make the figure not jump around](19-this-seems-to-help-make-the-figure-not-jump-around.md)
20. [This is a duplicate, keeping in here to avoid plots jumping around! (mpl bug)](20-this-is-a-duplicate-keeping-in-here-to-avoid-plots-jumping-a.md)

---

[Up: contents](../../../index.md)
