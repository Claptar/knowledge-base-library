---
title: Unit 09 — bigData Part 18 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — bigData Part 18 —

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

lines.filter(lambda line: "SFO" in line.split(',')[16]).saveAsTextFile('/data/airline-SFO') ## make sure it's all in one chunk for easier manipulation on master lines.filter(lambda line: "SFO" in line.split(',')[16]).repartition(1).saveAsTextFile('/data/airline-SFO2') #lines.filter(lambda line: "SFO" in line.split(',')[16]).repartition(1). #saveAsTextFile('/data/airline-SFO2')

Let’s consider some of the core methods we used. The Spark programming guide discusses these and a number of others.

- _map()_ : take an RDD and apply a function to each element, returning an RDD

- _reduce()_ and _reduceByKey()_ : take an RDD and apply a reduction operation to the elements, doing the reduction stratified by the key values for _reduceByKey()_ . Reduction functions need

30

to be associative and commutative and take 2 arguments and return 1, all so that they can be done in parallel in a straightforward way.

- _filter()_ : create a subset

- _collect()_ : collect results back to the master

- _cache()_ : tell Spark to keep the RDD in memory for later use

- _repartition()_ : rework the RDD so it is in the specified number of chunks

Question: how many chunks do you think we want the RDD split into? What might the tradeoffs be?

Here’s an example where we don’t have a simple commutative/associative reducer function. Instead we group all the observations for each key into a so-called iterable object. Then our second map function treats each key as an element, iterating over the observations grouped within each key.

def computeKeyValue(line): vals = line.split(',') # key is carrier-month-origin-destination keyVals = '-'.join([vals[x] for x in [8,1,16,17]]) if vals[0] == 'Year': return('0', [0,0,1,1]) cnt1 = 1 cnt2 = 1 # 14 and 15 are arrival and departure delays if vals[14] == 'NA': vals[14] = '0' cnt1 = 0 if vals[15] == 'NA': vals[15] = '0' cnt2 = 0 return(keyVals, [int(vals[14]), int(vals[15]), cnt1, cnt2]) def medianFun(input): if len(input) == 2: # input[0] should be key and input[1] set of values if len(input[1]) > 0:

31

---

[← mapper def stratify(line): vals = line.split(',') return(vals[16], 1)](17-mapper-def-stratify-line-vals-line-split-return-vals-16-1.md) · [Up: contents](index.md) · [Unit 09 — bigData Part 19 — →](19-unit-09-bigdata-part-19.md)
