---
title: 3. Parallelization strategies
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Parallelization strategies

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Some of the considerations that apply when thinking about how effective
a given parallelization approach will be include:

-   the amount of memory that will be used by the various processes,
-   the amount of communication that needs to happen -- how much data
    will need to be passed between processes,
-   the latency of any communication - how much delay/lag is there in
    sending data between processes or starting up a worker process, and
-   to what extent do processes have to wait for other processes to
    finish before they can do their next step.

The following are some basic principles/suggestions for how to
parallelize your computation.

-   Should I use one machine/node or many machines/nodes?
    -   If you can do your computation on the cores of a single node
        using shared memory, that will be faster than using the same
        number of cores (or even somewhat more cores) across multiple
        nodes. Similarly, jobs with a lot of data/high memory
        requirements that one might think of as requiring Spark or
        Hadoop may in some cases be much faster if you can find a single
        machine with a lot of memory.
    -   That said, if you would run out of memory on a single node, then
        you'll need to use distributed memory.
-   What level or dimension should I parallelize over?
    -   If you have nested loops, you generally only want to parallelize
        at one level of the code. That said, in this unit we'll see some
        tools for parallelizing at multiple levels. Keep in mind whether
        your linear algebra is being threaded. Often you will want to
        parallelize over a loop and not use threaded linear algebra
        within the iterations of the loop.
    -   Often it makes sense to parallelize the outer loop when you have
        nested loops.
    -   You generally want to parallelize in such a way that your code
        is load-balanced and does not involve too much communication.
-   How do I balance communication overhead with keeping my cores busy?
    -   If you have very few tasks, particularly if the tasks take
        different amounts of time, often some processors will be idle
        and your code poorly load-balanced.
    -   If you have very many tasks and each one takes little time, the
        overhead of starting and stopping the tasks will reduce
        efficiency.
-   Should multiple tasks be pre-assigned (statically assigned) to a
    process (i.e., a worker) (sometimes called *prescheduling*) or
    should tasks be assigned dynamically as previous tasks finish?
    -   To illustrate the difference, suppose you have 6 tasks and 3
        workers. If the tasks are pre-assigned, worker 1 might be
        assigned tasks 1 and 4 at the start, worker 2 assigned tasks 2
        and 5, and worker 3 assigned tasks 3 and 6. If the tasks are
        dynamically assigned, worker 1 would be assigned task 1, worker
        2 task 2, and worker 3 task 3. Then whichever worker finishes
        their task first (it wouldn't necessarily be worker 1) would be
        assigned task 4 and so on.
    -   Basically if you have many tasks that each take similar time,
        you want to preschedule the tasks to reduce communication. If
        you have few tasks or tasks with highly variable completion
        times, you don't want to preschedule, to improve load-balancing.
    -   For R in particular, some of R's parallel functions allow you to
        say whether the tasks should be prescheduled. In the future
        package, `future_lapply` has arguments `future.scheduling` and
        `future.chunk.size`. Similarly, there is the `mc.preschedule`
        argument in `mclapply()`.

---

[← 2. Overview of parallel processing](03-2-overview-of-parallel-processing.md) · [Up: contents](index.md) · [4. Introduction to Dask →](05-4-introduction-to-dask.md)
