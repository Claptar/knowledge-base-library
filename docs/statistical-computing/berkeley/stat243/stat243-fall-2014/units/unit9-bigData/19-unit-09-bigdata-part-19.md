---
title: Unit 09 — bigData Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — bigData Part 19 —

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

output = lines.map(computeKeyValue).groupByKey().cache() medianResults = output.map(medianFun).collect() medianResults[0:5] # [(u'DL-8-PHL-LAX', 85.0, 108.0), (u'OO-12-IAH-CLL', -6.0, 0.0), (u'AA-4-LAS-JFK',

#### **6.3.3 Using Spark for fitting models**

Here we’ll see the use of Spark to fit basic regression models in two ways. Warning: there may well be better algorithms to use and there may be better ways to implement these algorithms in Spark. But these work and give you the idea of how you can implement fitting within the constraints of a map-reduce paradigm.

Note that my first step is to repartition the data for better computational efficiency. Instead of having the data split into 22 year-specific chunks that vary in size (which is how things are initially because of the initial file structure), I’m going to split into a larger number of equal-size chunks to get better load-balancing.

**Linear regression via sufficient statistics** In the first algorithm we actually compute the sufficient statistics, which are simply _X_<sup>_⊤_</sup> _X_ and _X_<sup>_⊤_</sup> _Y_ . Because the number of predictors is small, these are miniscule compared to the size of the dataset. This code has two ways of computing the matrices. The first treats each line as an observation and sums the _Xi_<sup>_⊤Xi_and</sup><sup>_XiYi_values across</sup> all observations. The second uses a map function that can operate on an entire partition, iterating through the elements of the partition, and computing _Xk_<sup>_⊤Xk_and</sup><sup>_X_</sup> _k_<sup>_⊤Yk_for each partition,</sup><sup>_k_.The</sup> second way is rather faster.

32

lines = sc.textFile('/data/airline') def screen(vals): vals = vals.split(',') return(vals[0] != 'Year' and vals[14] != 'NA' and vals[18] != 'NA' and vals[3] != 'NA' and float(vals[14]) < 720 and float(vals[14]) > (-30) ) # 0 field is Year # 14 field is ArrDelay # 18 field is Distance # 3 field is DayOfWeek lines = lines.filter(screen).repartition(192).cache() # 192 is a multiple of the total number of cores: 24 (12 nodes * 2 n = lines.count() import numpy as np from operator import add P = 8 bc = sc.broadcast(P)

cores/node)

####################### # calc xtx and xty ####################### def crossprod(line): vals = line.split(',') y = float(vals[14]) dist = float(vals[18]) dayOfWeek = int(vals[3]) xVec = np.array([0.0] * P) xVec[0] = 1.0 xVec[1] = float(dist)/1000 if dayOfWeek > 1: xVec[dayOfWeek] = 1.0

33

xtx = np.outer(xVec, xVec) xty = xVec * y return(np.c_[xtx, xty]) xtxy = lines.map(crossprod).reduce(add) # 11 minutes # now just solve system of linear equations!! ####################### # calc xtx and xty w/ mapPartitions ####################### # dealing with x matrix via mapPartitions def readPointBatch(iterator): strs = list(iterator) matrix = np.zeros((len(strs), P+1)) for i in xrange(len(strs)): vals = strs[i].split(',') dist = float(vals[18]) dayOfWeek = int(vals[3]) xVec = np.array([0.0] * (P+1)) xVec[8] = float(vals[14]) # y xVec[0] = 1.0 # int xVec[1] = float(dist) / 1000 if(dayOfWeek > 1): xVec[dayOfWeek] = 1.0 matrix[i] = xVec return([matrix.T.dot(matrix)])

xtxyBatched = lines.mapPartitions(readPointBatch).reduce(add) # 160 seconds

mle = np.linalg.solve(xtxy[0:P,0:P], xtxy[0:P,P])

34

**Linear regression via cyclic coordinate descent** In the second algorithm we pretend that we don’t want to compute _X_<sup>_⊤_</sup> _X_ , mimicing the situation in which we have too many predictors to either store _X_<sup>_⊤_</sup> _X_ or to do linear algebra on _X_<sup>_⊤_</sup> _X_ . Instead we’ll have a vector of starting values for _β_ . Then we’ll cycle through each element of _β_ and optimize that element, holding the others constant. The individual update steps look like this:


where _ri_ the residual not including the _p_ th predictor:<sup>�</sup> _i_ � _yi −_<sup>�</sup> _j̸_ = _p_<sup>_x_</sup> _ij_<sup>_β_</sup> _j_<sup>_t_</sup> � and based on the current parameter values.

Once again, we’ll use _mapPartitions()_ to do the calculations we need for each step of the optimization piecewise on each partition (I use _batch_ to describe this in the code). Note that the result after 10 iterations here is not the MLE, though most of the day of week effects are all shifted by a common amount relative to the mean when compared to the MLE.

def readPointPartition(iterator): strs = list(iterator) matrix = np.zeros((len(strs), P+1)) print(len(strs)) for i in xrange(len(strs)): vals = strs[i].split(',') dist = float(vals[18]) dayOfWeek = int(vals[3]) xVec = np.array([0.0] * (P+1)) xVec[8] = float(vals[14]) # y xVec[0] = 1.0 # int xVec[1] = float(dist) / 1000 if(dayOfWeek > 1): xVec[dayOfWeek] = 1.0 matrix[i] = xVec return([matrix])

batches = lines.mapPartitions(readPointPartition).cache() # 3 min def denomSumSqPartition(mat):

35

return((mat*mat).sum(axis=0)) def getNumPartition(mat): beta[p] = 0 sumXb = mat[:, 0:P].dot(beta) return(sum((mat[:,P] - sumXb)*mat[:,p])) sumx2 = batches.map(denomSumSqPartition).reduce(add) beta = np.array([0.0] * P) p = 0 oldBeta = beta.copy() # otherwise a shallow (i.e., pointer) copy! it = 0 tol = .001 maxIts = 10 crit = 1e16 while crit > tol and it <= maxIts: #for it in range(1,6): for p in xrange(P): # distribute current beta and current coordinate bc = sc.broadcast(beta) bc = sc.broadcast(p) # get numerator as product of residual and X for coordinate sumNum = batches.map(getNumPartition).reduce(add) beta[p] = sumNum / sumx2[p] print("Updated var " + str(p) + " in iteration ", str(it), ".") crit = sum(abs(beta - oldBeta)) oldBeta = beta.copy() print("-"*100) print(beta) print(crit) print("-"*100)

36

it = it+1 # 7 s per iteration; ~9 minutes for 10 iterations beta #array([ 6.59246803, 0.76054724, -0.92357814, 0.16881708, 2.00073749, # 2.66270618, -2.65116571, -0.36017589])

We’ve only done linear regression here, but similar coordinate descent computations can be done for GLMs and for Lasso type problems, and probably for other types of models. In fact coordinate descent is a (the?) standard algorithm for Lasso as discussed in this paper, which describes the methods in the _glmnet_ package.

**Linear regression via gradient descent** Cycling through each coefficient has the obvious disadvantage of having to cycle through each coefficient, which would become particularly problematic in a model with more predictors. An alternative is to do gradient descent on the entire vector of coefficients at once. For this problem the update at each step looks like this


where _∇L_ ( _β_<sup>_t_</sup> ) is the gradient vector of the log-likelihood evaluated at the current value, _β_<sup>_t_</sup> . A key issue here, which we’ll discuss in detail in the Unit on optimization is the step size, _α_ , also known as the learning rate. Here’s the code for doing gradient descent on the entire set of coefficients.

alpha = .4 def sumVals(mat): return(sum(mat[:,P]))

beta = np.array([0.0] * P) beta[0] = batches.map(sumVals).reduce(add) / n oldBeta = beta.copy() bc = sc.broadcast(P) bc = sc.broadcast(beta) def getGradBatch(mat):

37

sumXb = mat[:, 0:P].dot(beta) return( ((sumXb - mat[:,P])*((mat[:, 0:P]).T)).sum(1) ) def ssqObj(mat): return ( (pow(mat[:,P] - mat[:, 0:P].dot(beta), 2)).sum() ) objValue = batches.map(ssqObj).reduce(add) nIts = 100 storeVals = np.zeros((nIts, P+2)) tol = .001 maxIts = 100 crit = 1e16 while crit > tol and it < maxIts: gradVec = batches.map(getGradBatch).reduce(add) beta = beta - alpha*gradVec / n crit = sum(abs(beta - oldBeta)) bc = sc.broadcast(beta) objValue = batches.map(ssqObj).reduce(add) oldBeta = beta.copy() storeVals[it, 0] = pow(objValue/n,0.5) storeVals[it, 1] = crit storeVals[it, 2:(P+2)] = beta print("-"*100) print(it) print(beta) print(crit) print(pow(objValue/n,0.5)) print("-"*100) it = it + 1 # 15 min #[ 6.57348292 0.75335604 -0.9251238 0.16222806 1.98565752 2.64468325 # -2.63650861 -0.36507276]

38

Note that I’m recording the value of the objective function to make sure that it is decreasing in every iteration, as one could set the learning rate such that that does not happen.

#### **6.3.4 Final comments**

**Running a batch Spark job** We can run a Spark job using Python code as a batch script rather than interactively. Here’s an example, which computes the value of _π_ by Monte Carlo simulation (more on the general technique in the Unit on simulation). Assuming the script is named _piCalc.py_ , we would call the script like this: spark-submit piCalc.py 100000000 1000

import sys from pyspark import SparkContext if __name__ == "__main__": sc = SparkContext() # use sys.argv to get arguments # for example: total_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000 num_slices = int(sys.argv[2]) if len(sys.argv) > 2 else 2 samples_per_slice = round(total_samples / num_slices) def sample(p): rand.seed(p) x, y = rand.random(samples_per_slice), rand.random(samples_per_slice) # x, y = rand.random(samples_per_slice), # rand.random(samples_per_slice) return sum(x*x + y*y < 1)

count = sc.parallelize(xrange(0, num_slices), num_slices).map(sample).reduce(lambda #count = sc.parallelize(xrange(0, num_slices), num_slices). # map(sample).reduce(lambda a, b: a + b) print "Pi is roughly %f" % (4.0 * count / (num_slices*samples_per_slice))

This code again uses the idea that it’s computationally more efficient to have each operation occur on a batch of data rather than an individual data point. So there are 1000 tasks and the total number of samples is broken up amongst those tasks. In fact, Spark has problems if the number of tasks gets too large.

39

**Python vs. Scala/Java** Spark is implemented natively in Java and Scala, so all calculations in Python involve taking Java data objects converting them to Python objects, doing the calculation, and then converting back to Java. This process is called serialization and takes time, so the speed when implementing your work in Scala (or Java) may be faster. Here’s a small bit of info on that.

**sparkR** Finally, there is an R interface for Spark, but it’s pretty new and not mature, so I didn’t think it worth covering.

40

---

[← Unit 09 — bigData Part 18 —](18-unit-09-bigdata-part-18.md) · [Up: contents](index.md)
