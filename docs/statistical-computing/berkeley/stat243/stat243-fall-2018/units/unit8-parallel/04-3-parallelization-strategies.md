---
title: 3 Parallelization strategies
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit8-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit8-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Parallelization strategies

**Source:** [`units/unit8-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit8-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some of the considerations that apply when thinking about how effective a given parallelization approach will be include:

- the amount of memory that will be used by the various processes,

- the amount of communication that needs to happen – how much data will need to be passed between processes,

- the latency of any communication - how much delay/lag is there in sending data between processes or starting up a worker process, and

- to what extent do processes have to wait for other processes to finish before they can do their next step.

The following are some basic principles/suggestions for how to parallelize your computation.

- Should I use one machine/node or many machines/nodes?

   - If you can do your computation on the cores of a single node using shared memory, that will be faster than using the same number of cores (or even somewhat more cores) across multiple nodes. Similarly, jobs with a lot of data/high memory requirements that one might think of as requiring Spark or Hadoop may in some cases be much faster if you can find a single machine with a lot of memory.

   - That said, if you would run out of memory on a single node, then you’ll need to use distributed memory.

- What level or dimension should I parallelize over?

   - If you have nested loops, you generally only want to parallelize at one level of the code. That said, there may be cases in which it is helpful to do both. Keep in mind whether your linear algebra is being threaded. Often you will want to parallelize over a loop and not use threaded linear algebra.

   - Often it makes sense to parallelize the outer loop when you have nested loops.

6

   - You generally want to parallelize in such a way that your code is load-balanced and does not involve too much communication.

- How do I balance communication overhead with keeping my cores busy?

   - If you have very few tasks, particularly if the tasks take different amounts of time, often some processors will be idle and your code poorly load-balanced.

   - If you have very many tasks and each one takes little time, the communication overhead of starting and stopping the tasks will reduce efficiency.

- Should multiple tasks be pre-assigned to a process (i.e., a worker) (sometimes called _prescheduling_ ) or should tasks be assigned dynamically as previous tasks finish?

   - Basically if you have many tasks that each take similar time, you want to preschedule the tasks to reduce communication. If you have few tasks or tasks with highly variable completion times, you don’t want to preschedule, to improve load-balancing.

   - For R in particular, some of R’s parallel functions allow you to say whether the tasks should be prescheduled. E.g., the _mc.preschedule_ argument in _mclapply()_ . For _parLapply()_ the documentation would suggest _parLapplyLB()_ is the way to do this but there appears to be a bug in _parLapplyLB()_ such that no load-balancing is done.

---

[← 2 Overview of parallel processing](03-2-overview-of-parallel-processing.md) · [Up: contents](index.md) · [4 Illustrating the principles in specific case studies →](05-4-illustrating-the-principles-in-specific-case-studies.md)
