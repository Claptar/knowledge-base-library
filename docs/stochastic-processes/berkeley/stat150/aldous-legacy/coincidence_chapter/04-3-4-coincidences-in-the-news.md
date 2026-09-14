---
title: 3.4 Coincidences in the news
source: https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf
source_file: sources/berkeley-stat150/aldous-legacy/coincidence_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.4 Coincidences in the news

**Source:** [`coincidence_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/150/coincidence_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Every time I teach the course I see relevant examples in current or recent news or in my email inbox that I can use. Here are two examples from the 2014 course.

#### 42 _CHAPTER 3. COINCIDENCES, NEAR MISSES AND ONE-IN-A-MILLION CHANCES_

**Plane crash cluster.** There were 3 passenger jet crashes in 8 days in summer 2014 (Air Algerie July 24th, TransAsia July 23rd, Malaysian Airlines July 17). How unusual is this?

The relevant data is that over the last 20 years, crashes with substantial fatalities have occurred at rate 1/40 per day, so under the natural IID probability model the number _N_ of crashes in a given 8 days has approximately Poisson(0.2) distribution, for which

P( _N_ = 3) _⇡_ 0 _._ 2<sup>3</sup> _/_ 6 _⇡_ 1 _._ 33 _⇥_ 10<sup>_−_3</sup> _._

A calculation outlined here, which accounts for overlaps of 8-day intervals, shows that in the model such a cluster will occur “by chance” about once every 10 years. So this coincidence is not terribly unlikely.

This setting provides a concrete context for the section 3.3 general discussion. We have a context – plane crashes – and we model an observed coincidence as an instance of some “specific coincidence type” – here “3 crashes in 8 days”. But there are many other “specific coincidence types” that might have occurred, in the context of plane crashes. We could consider a longer window of time – a month or a year – and could consider coincidences involving the same airline or the same region of the world or the same airplane model. Even if a coincidence within any one “specific type” were unlikely, the chance that there is a coincidence in some one of them – somewhere within the context of plane crashes – may be large. In other words, claims that “what happened is so unlikely that it couldn’t be just chance” typically rely on an analysis of the specifics of what did happen, but a meaningful analysis needs also to consider other types of coincidences that didn’t happen.

**Assignment of court cases.** U.S. District Court Judge (Washington DC) Richard Leon handled 3 cases involving the FDA and tobacco companies.

- In January 2010 he prevented the Food and Drug Administration from blocking the importation of electronic cigarettes.

- In February, 2012 he blocked a move by the FDA to require tobacco companies to display graphic warning labels on cigarette packages.

- In July 2014 he ruled in favor of tobacco companies and invalidated a report prepared by an FDA advisory committee on menthol.

A journalist emailed me the question:

_3.5. COINCIDENCES IN WIKIPEDIA_

43

What are the chances that one judge would pull these major cases when cases are supposedly assigned randomly?

In other words, is this just coincidence, or does it suggest maybe these cases were not assigned randomly? Note that we are not discussing the _merits of the judgments_ – it would be nonsensical to model the judgements as random.

It turns out there are e↵ectively<sup>7</sup> 17.5 judges in this court, so (if random assignment) the chance all 3 cases go to the same judge is 1 _/_ 17 _._ 5 _⇥_ 1 _/_ 17 _._ 5 _⇡_ 1 _/_ 300.

But there were over 10,000 cases in the period. Imagine looking at all those cases and looking to see where there is a group of 3 cases which are ”very similar” in some sense. The sense might be “same plainti↵and same issue”, as here, but one can imagine many other types of possible similarity. Guessing wildly, suppose there are 100 such groups-of-3. Then because, for each such group, there is the same 1/300 chance of all going to the same judge, then the chance that this happens for **some** group amongst the 100 groups is a little smaller than 100 _/_ 300 = 1 _/_ 3, so would not be surprising.

Now of course the FDA-tobacco issue is unusually interesting. A more precise analysis would to go through the 10,000+ cases and find out the number of groups-of-3 that were “very similar” in some sense _of interest to a journalist_ . This is some (presumably not very large) number _n_ , and the chance that some group “of interest to a journalist” were all assigned to the same judge (by pure chance) is around _n/_ 300. Now I have no idea what _n_ is, but

experience with other kinds of coincidence says that there are many more occurrences and more types of ”very similar in an interesting way” than you would imagine

and the next section provides a further illustration of this point.

---

[← 3.3 Coincidences in everyday life](03-3-3-coincidences-in-everyday-life.md) · [Up: contents](index.md) · [3.5 Coincidences in Wikipedia →](05-3-5-coincidences-in-wikipedia.md)
