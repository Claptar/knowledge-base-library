---
title: 3.7 Near misses
source: https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf
source_file: sources/berkeley-stat150/aldous-legacy/coincidence_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.7 Near misses

**Source:** [`coincidence_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Closely related to coincidences are a range of events that one might view as _near-misses_ . That phrase originated in the setting a physically aiming at a target (I’ll call that the _geometric_ setting) but is also used in other settings I will call _combinatorial_ – see examples below. The message of this section will be

_3.7. NEAR MISSES_

47

In combinatorial (rather than geometric) settings, near-misses may be much more likely than exact hits, and this phenomenon is exploited by designers of Lotto-like games.

Here is our exemplar, which will be familiar to players of Scrabble-like word games. If we pick 5 letters of the alphabet, what are the chances that (a) The letters can be arranged to form an English word? (b) The letters can be arranged to form an English word, if we are allowed to change one letter (our choice of letter) into any other letter we choose? As intuition suggests, (a) is unlikely but (b) is likely. The numerical chances depend on how exactly you pick the random letters and how large your vocabulary or dictionary is, but in our small experiment chance (a) was about 18% and chance (b) was about 94%.

**Near misses in geometric settings.** Before trying to explain what “combinatorial settings” means, it may help (and is easier) to illustrate the opposite notion of “geometric setting”. On a dartboard there is a small “bulls eye” (scoring 50 points in the traditional British game) surrounded by a ring (scoring 25 points) of twice the radius. If you have some small probability _p_ of hitting the 50, then you will have probability about 3 _p_ of hitting the 25, because the area is three times larger. Similarly in the asteroid example from (xxx) section 8.7, the chance an asteroid comes within 4,000 miles (the Earth’s radius) of the Earth’s surface will be about three times the chance of actually hitting the Earth. This is just the local uniformity principle from Lecture 8, the point being that the ratio “3” of probabilities depends only on the fact that we’re dealing with a problem in two dimensions. In contrast, if we view 10 out of 10 Heads in coin tossing as a “coincidence” and 9 out of 10 as a near miss, then the ratio of probabilities is 10. But here, “10” isn’t a magic number associated with coin-tossing; if we had chosen a di↵erent, rarer coincidence we would get a larger ratio.

**Near-misses in Lotto picks.** Instead of Scrabble or coin tossing, a more common occurrence of “combinatorial” near-misses is in Lotto-type games. If you pick 6 numbers out of 51, then when the lottery picks 6 numbers, the chance you get 5 out of 6, relative to 6 out of 6, is now 6 _⇥_ 45 = 270 to 1. This is dramatically di↵erent from the ratio “3” we saw in geometric examples. And indeed, part of the reason for designing lotteries in this “pick _k_ numbers out of _n_ ” format is to ensure many near-misses, on the reasonable assumption that observing near-misses will encourage gamblers

48 _CHAPTER 3. COINCIDENCES, NEAR MISSES AND ONE-IN-A-MILLION CHANCES_

to continue playing<sup>8</sup> If, instead, lottery tickets simply represented each of the 18 million possibilities as a number like 12 _,_ 704 _,_ 922 between 1 and 18 million, then (counting a near-miss as one digit o↵) there would be only around 64 near-misses.

A typical student project is to study near-misses in bingo with many players – when one person wins, how many others will have lines with 4 out of 5 filled?

**Manipulation of near-misses.** Exploiting mathematics to design games with many near-misses is generally considered to be within ethical boundaries (every game has rules designed to make it interesting), but other schemes have arguably crossed the boundary. The 2005 book _License to Steal_ by Je↵Burbank devotes a chapter to the following story, (summary from an amazon.com review).

. . . a slot machine manufacturer had programmed its machines to make it look as if losing spins had just missed being winners – “near misses.” The owners claimed that the machine wheels would spin randomly, as they are supposed to, but that once the spin had randomly been determined to be a loser, the wheels would re-adjust to show a near miss. This made it more exciting for the player, who would play more. But the regulators thought it might compromise the appearance of randomness. They decided the near miss feature would not be allowed, but when the company appealed on the grounds that retrofitting thousands of machines would be too expensive, the [Nevada Gaming] Commission cut them some slack. They still went bankrupt.

---

[← 3.6 Classifying coincidences in everyday life](06-3-6-classifying-coincidences-in-everyday-life.md) · [Up: contents](index.md) · [3.8 What really has a 1 in a million chance? →](08-3-8-what-really-has-a-1-in-a-million-chance.md)
