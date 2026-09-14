---
title: Unit 07 — bigData Part 21 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — bigData Part 21 —

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

lines.filter(lambda line: "SFO" in line.split(',')[16]).saveAsTextFile('/data/airline-SFO') ## make sure it's all in one chunk for easier manipulation on master lines.filter(lambda line: "SFO" in line.split(',')[16]).repartition(1).saveAsTextFile('/data/airline-SFO2') #lines.filter(lambda line: "SFO" in line.split(',')[16]).repartition(1). #saveAsTextFile('/data/airline-SFO2')

Let’s consider some of the core methods we used. The Spark programming guide discusses these and a number of others.

- _map()_ : take an RDD and apply a function to each element, returning an RDD

- _reduce()_ and _reduceByKey()_ : take an RDD and apply a reduction operation to the elements, doing the reduction stratified by the key values for _reduceByKey()_ . Reduction functions need to be associative and commutative and take 2 arguments and return 1, all so that they can be done in parallel in a straightforward way.

- _filter()_ : create a subset

- _collect()_ : collect results back to the master

- _cache()_ : tell Spark to keep the RDD in memory for later use

- _repartition()_ : rework the RDD so it is in the specified number of chunks

32

Question: how many chunks do you think we want the RDD split into? What might the tradeoffs be?

Here’s an example where we don’t have a simple commutative/associative reducer function. Instead we group all the observations for each key into a so-called iterable object. Then our second map function treats each key as an element, iterating over the observations grouped within each key.

def computeKeyValue(line): vals = line.split(',') # key is carrier-month-origin-destination keyVals = '-'.join([vals[x] for x in [8,1,16,17]]) if vals[0] == 'Year': return('0', [0,0,1,1]) cnt1 = 1 cnt2 = 1 # 14 and 15 are arrival and departure delays if vals[14] == 'NA': vals[14] = '0' cnt1 = 0 if vals[15] == 'NA': vals[15] = '0' cnt2 = 0 return(keyVals, [int(vals[14]), int(vals[15]), cnt1, cnt2]) def medianFun(input): if len(input) == 2: # input[0] should be key and input[1] set of values if len(input[1]) > 0: # iterate over set of values # input[1][i][0] is arrival delay # input[1][i][1] is departure delay m1 = np.median([val[0] for val in input[1] if val[2] == 1]) m2 = np.median([val[1] for val in input[1] if val[3] == 1]) return((input[0], m1, m2)) # m1, m2)) else: return((input[0], -999, -999))

33

else: return((input[0], -9999, -9999))

output = lines.map(computeKeyValue).groupByKey() medianResults = output.map(medianFun).collect() medianResults[0:5] # [(u'DL-8-PHL-LAX', 85.0, 108.0), (u'OO-12-IAH-CLL', -6.0, 0.0), (u'AA-4-LAS-JFK',

#### **6.3.3 Using Spark for fitting models**

Here we’ll see the use of Spark to fit basic regression models in two ways. Warning: there may well be better algorithms to use and there may be better ways to implement these algorithms in Spark. But these work and give you the idea of how you can implement fitting within the constraints of a map-reduce paradigm.

Note that my first step is to repartition the data for better computational efficiency. Instead of having the data split into 22 year-specific chunks that vary in size (which is how things are initially because of the initial file structure), I’m going to split into a larger number of equal-size chunks to get better load-balancing.

**Linear regression via sufficient statistics** In the first algorithm we actually compute the sufficient statistics, which are simply _X_<sup>_⊤_</sup> _X_ and _X_<sup>_⊤_</sup> _Y_ . Because the number of predictors is small, these are miniscule compared to the size of the dataset. This code has two ways of computing the matrices. The first treats each line as an observation and sums the _Xi_<sup>_⊤Xi_and</sup><sup>_XiYi_values across</sup> all observations. The second uses a map function that can operate on an entire partition, iterating through the elements of the partition, and computing _Xk_<sup>_⊤Xk_and</sup><sup>_X_</sup> _k_<sup>_⊤Yk_for each partition,</sup><sup>_k_.The</sup> second way is rather faster.

lines = sc.textFile('/data/airline') def screen(vals): vals = vals.split(',') return(vals[0] != 'Year' and vals[14] != 'NA' and vals[18] != 'NA' and vals[3] != 'NA' and float(vals[14]) < 720 and float(vals[14]) > (-30) ) # 0 field is Year

34

---

[← Unit 07 — bigData Part 20 —](20-unit-07-bigdata-part-20.md) · [Up: contents](index.md) · [14 field is ArrDelay # 18 field is Distance # 3 field is DayOfWeek →](22-14-field-is-arrdelay-18-field-is-distance-3-field-is-dayofwe.md)
