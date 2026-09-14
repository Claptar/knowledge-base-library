---
title: 3.1 The birthday problem and its relatives
source: https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf
source_file: sources/berkeley-stat150/aldous-legacy/coincidence_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.1 The birthday problem and its relatives

**Source:** [`coincidence_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The birthday problem– often called the _birthday paradox_ – is described in almost every textbook and popular science account of probability. My students know the conclusion

with 23 people in a room, there is roughly a 50% chance that some two will have the same birthday.

Rather than repeat the usual “exact” calculation I will show how to do some back-of-an-envelope calculations, in section 3.2 below. Starting from this result there are many directions we could go, so let me point out five of these.

**It really is a good example** of a quantitative prediction that one could bet money on. In class, and in a popular talk, I show the active roster of a baseball team<sup>1</sup> which conveniently has 25 players and their birth dates. The predicted chance of a birthday coincidence is about 57%. With 30 MLB teams one expects around 17 teams to have the coincidence; and one can

> 1e.g. atlanta.braves.mlb.com/team/roster ~~a~~ ctive.jsp?c ~~i~~ d=atl; each MLB team has a page in the same format

35

36 _CHAPTER 3. COINCIDENCES, NEAR MISSES AND ONE-IN-A-MILLION CHANCES_

readily check this prediction in class in a minute or so (print out the 30 pages and distribute among students).

**It’s fun to ask students to suggest circumstances where the prediction might not be accurate.** This is, if you actually see a group of strangers in a room and know roughly why they are there – people rarely go into rooms “at random” – what might make you unsure of the validity of the standard calculation? Two common suggestions are (i) if you see identical twins

(ii) that the calculation in general may be inaccurate because of non-uniformity of population birth dates over the year.

Point (i) is clear and point (ii) is discussed in the next section (plausible levels of non-uniformity turn out to have negligible e↵ect). Other circumstances involve very creative imagination or arcane knowledge (a party of Canadian professional ice hockey players<sup>2</sup> ). As mentioned above, it is a rare example of a mathematically simple yet reliable model!

**It illustrates the theme “coincidences are more likely than you think”.** This is an important theme as regards people’s intuitive perception of chance. But the birthday problem and other “small universe” settings, where one can specify in advance all the possible coincidences and their probabilities, are very remote from our notion of weird coincidences in everyday life. A typical blurb for popular science books is “. . . explains how coincidences are not surprising” while the author merely does the birthday problem. This is surely not convincing to non-mathematicians. I will repeat this critique more forcefully in section 3.9. My own (unsuccessful) attempt to do better is recounted in section 3.5.

**One can invent and solve a huge number of analogous math probability problems** and I show a glimpse of such problems in section 3.2. These can be engaging as recreational math and for illustrating mathematical techniques – but I find it almost impossible to produce novel interesting data to complement such theory.

There is an opposite problem with sports data on “hot hands” for individual players, or winning/losing streaks for teams. Here there is plenty of data, but coming up with an accurate chance model is difficult; saying that

> 2who have substantial non-uniformity of birthdays. A 1985 paper _Birthdate and success in minor hockey_ by Roger Barnsley and A. H. Thompson and subsequent work, popularized in Gladwell’s _Outliers_ , attributes this to the annual age cuto↵for starting minor hockey.

#### _3.2. USING THE POISSON APPROXIMATION IN SIMPLE MODELS_ 37

we see streaks longer than predicted in an oversimplified chance model is not telling us anything concrete about the world of sports.

---

[Up: contents](index.md) · [3.2 Using the Poisson approximation in simple models →](02-3-2-using-the-poisson-approximation-in-simple-models.md)
