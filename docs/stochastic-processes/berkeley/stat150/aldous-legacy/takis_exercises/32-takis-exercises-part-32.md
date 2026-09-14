---
title: Takis exercises Part 32 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 32 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the previous problem: If there are 9 balls and 3 colours (Red, Green, Blue) and we initially start with 3 balls of each colour, how long will it take on the average till we see again the same configuration? (Suppose that 1 step = 1 minute.) If we start we all balls coloured Red, how long will it take on the average till we see the same again? Solution.


Hence the average number of steps between two successive occurrences of the state (3, 3, 3) is 6561/560 ≈ 11.72 minutes. Next,


Hence the average number of steps between two successive occurrences of the state (9, 0, 0) is 19683 minutes = 328.05 hours ≈ 13 and a half days.

100.

Consider a random walk on a star-graph that has one centre vertex 0 and N legs emanating from 0. Leg i contains ℓi vertices (in addition to 0) labelled


The vertices are in sequence: 0 is connected to vi,1 which is connected to vi,2, etc. till the end vertex vi,ℓi. (i) A particle starts at 0. Find the probability that it reaches the

72


<!-- Start of picture text -->
v<br>2,2<br>v<br>v 2,1<br>3,2<br>v 0<br>3,1<br>v v 1,1 v 1,2<br>4,1 v 5,1<br>v<br>5,2<br><!-- End of picture text -->

end of leg i before reaching the end of any other leg. (ii) Suppose N = 3, ℓ1 = 2, ℓ2 = 3, ℓ3 = 100. Play a game as follows: start from 0. If end of leg i is reached you win ℓi pounds. Find how much money you are willing to pay to participate in this game. Solution. Let ϕi(x) be the probability that end of leg i is reached before reaching the end of any other leg. Clearly,


Now, if vi,r is an interior vertex of leg i (i.e. neither 0 nor the end vertex), then


This means that the function


must be linear for each k (for the same reason that the probability of hitting the left boundary of an interval before hitting the right one is linear for a simple symmetric random walk). Hence


where ai,k, bi,k are constants. For any leg we determine the constants in terms of the values of ϕi at the centre 0 and the end vertex. Thus,


Now, for vertex 0 we have


whence


(ii)


The average winnings are:


74

---

[← and](31-and.md) · [Up: contents](index.md)
