---
title: "44. Principles of Parallel Computing"
course: "Berkeley Stat 243 Fall 2024"
chapter: 44
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 44. Principles of Parallel Computing

## What this covers

Given a computation whose pieces don't depend on one another, this chapter answers the practical
question of how to actually put more hardware behind it — more cores on one machine, more nodes on
a cluster, or a GPU — and how to decide which of those to reach for. It assumes you can already
write a correct, reasonably efficient serial implementation of whatever you're parallelizing (that
efficiency question is the previous unit's territory; this one is purely about multiplying the
hardware behind a working computation). The running tool throughout is Python's `Dask`, with a
shorter look at R's `future` package near the end.

## Four ways to make a computation faster

Parallelism is one of exactly four ways to speed up a calculation, and it is worth placing it
alongside the other three so it doesn't get reached for as a universal fix:

- **better algorithms** — often the largest possible win, but not the subject here;
- **more efficient implementations of a given algorithm** — the subject of the previous unit;
- **faster computers** — this mattered enormously while Moore's Law was pushing CPU clock speeds up
  every year; that has largely stopped for CPUs, though GPU hardware is still improving quickly;
- **more computers** — exploiting more CPUs, more GPU threads, or more compute nodes for a single
  computation. This is the subject of the rest of the chapter.

## Embarrassingly parallel problems

Everything below only applies if a computation's pieces are genuinely independent: no piece needs
output from another, and the pieces can run as separate processes with no communication between
them. This is called an **embarrassingly parallel (EP)** problem — you solve it by farming out
independent tasks to separate processes and collecting the results afterward. In statistics, EP
problems are the rule rather than the exception:

- simulations with many independent replicates,
- bootstrapping,
- stratified analyses (e.g. fitting a model once per subgroup of a dataset),
- random forests,
- cross-validation.

The typical shape is the same code, run repeatedly on different pieces of data (different processes
may need distinct random-number streams — a subtlety picked up later in this chapter, and again in
the Simulation unit). Doing this requires control of multiple processes at once; on a shared cluster
running scheduling software, that means requesting a number of processors and then structuring the
job so that it actually uses all of them.

Ignoring some modest overhead, an EP problem with $p$ CPUs can ideally be solved in $1/p$ of the
serial time — a **linear speedup**, meaning any speedup of the form $kp$ for a constant $k$. That is
the best case, not the typical one; a good deal of this chapter is about the ways real hardware,
real schedulers, and real data volumes fall short of it.

## The vocabulary of parallel hardware

Modern personal computers usually have more than one processor chip, and each chip usually has more
than one **core** (the AMD EPYC 7763, for example, has 64 cores per chip). All the cores and
processors on a personal computer share the same memory. Supercomputers and clusters instead
consist of tens, hundreds, or thousands of **nodes** linked by a fast local network; each node is
essentially its own computer with its own processor(s) and its own memory, and memory is *local* to
each node. Communication between a processor and its own memory is always much faster than
communication between processors belonging to different nodes. As a sense of scale: Lawrence
Berkeley Lab's Perlmutter supercomputer has 3072 CPU-only nodes and 1792 GPU nodes — about 500,000
CPU cores in total — with 512 GB of memory per node, for 2.3 PB overall. For most practical purposes
there's little distinction between multi-processor and multi-core: what matters is whether processes
share memory, so the rest of this chapter just talks about the number of cores available on a given
machine or node.

A few more terms recur throughout:

- **processes**: running instances of a program; a given program can start several at once, and
  ideally there are no more processes than cores on a node.
- **workers**: the individual processes actually carrying out the parallelized computation —
  used interchangeably with *process* here.
- **tasks**: individual units of computation; a worker executes one or more tasks.
- **threads**: multiple paths of execution *within* a single process. The operating system sees the
  threads as one process, but they behave like lightweight processes; ideally the number of cores
  available matches the number of processes and threads combined.
- **forking**: spawning child processes identical to the parent but with their own process ID and
  (usually) their own memory. If an object is never modified, a forked child can sometimes keep
  referring back to the parent's copy instead of duplicating it.
- **scheduler**: the program managing users' jobs on a cluster — *Slurm* is a common one. (Dask and
  the `future` package also have something called a scheduler, in the different sense of "the thing
  that decides how your parallel code is actually run" — see below.)
- **load-balanced**: a computation where every core involved is kept busy for the whole run.
- **sockets**: the communication technology some of R's parallel functionality uses to talk to new R
  processes it starts (e.g. via `Rscript`).

### Shared vs. distributed memory

Leaving GPUs aside for a moment, there are two basic flavors of parallelism, and almost everything
else in this chapter is a consequence of which one you're in.

<figure>
<svg viewBox="0 0 480 150" role="img" aria-label="Four cores all reaching one shared memory directly, versus three nodes each with its own local memory, connected only by a slower network">
  <text x="125" y="16" text-anchor="middle" font-size="12" fill="currentColor">Shared memory (one node)</text>
  <rect x="30" y="26" width="40" height="22" fill="none" stroke="currentColor"/>
  <rect x="80" y="26" width="40" height="22" fill="none" stroke="currentColor"/>
  <rect x="130" y="26" width="40" height="22" fill="none" stroke="currentColor"/>
  <rect x="180" y="26" width="40" height="22" fill="none" stroke="currentColor"/>
  <text x="50" y="41" text-anchor="middle" font-size="10" fill="currentColor">core</text>
  <text x="100" y="41" text-anchor="middle" font-size="10" fill="currentColor">core</text>
  <text x="150" y="41" text-anchor="middle" font-size="10" fill="currentColor">core</text>
  <text x="200" y="41" text-anchor="middle" font-size="10" fill="currentColor">core</text>
  <line x1="50" y1="48" x2="50" y2="80" stroke="currentColor"/>
  <line x1="100" y1="48" x2="100" y2="80" stroke="currentColor"/>
  <line x1="150" y1="48" x2="150" y2="80" stroke="currentColor"/>
  <line x1="200" y1="48" x2="200" y2="80" stroke="currentColor"/>
  <rect x="30" y="80" width="190" height="26" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="125" y="97" text-anchor="middle" font-size="11" fill="currentColor">shared memory</text>
  <text x="125" y="122" text-anchor="middle" font-size="10" fill="currentColor">every core reaches memory directly</text>

  <text x="365" y="16" text-anchor="middle" font-size="12" fill="currentColor">Distributed memory (cluster)</text>
  <rect x="270" y="30" width="60" height="46" fill="none" stroke="currentColor"/>
  <text x="300" y="47" text-anchor="middle" font-size="10" fill="currentColor">core(s)</text>
  <line x1="280" y1="53" x2="320" y2="53" stroke="currentColor"/>
  <text x="300" y="68" text-anchor="middle" font-size="10" fill="currentColor">memory</text>
  <rect x="345" y="30" width="60" height="46" fill="none" stroke="currentColor"/>
  <text x="375" y="47" text-anchor="middle" font-size="10" fill="currentColor">core(s)</text>
  <line x1="355" y1="53" x2="395" y2="53" stroke="currentColor"/>
  <text x="375" y="68" text-anchor="middle" font-size="10" fill="currentColor">memory</text>
  <rect x="420" y="30" width="50" height="46" fill="none" stroke="currentColor"/>
  <text x="445" y="47" text-anchor="middle" font-size="9" fill="currentColor">core(s)</text>
  <line x1="428" y1="53" x2="462" y2="53" stroke="currentColor"/>
  <text x="445" y="68" text-anchor="middle" font-size="9" fill="currentColor">memory</text>
  <line x1="300" y1="76" x2="300" y2="95" stroke="currentColor"/>
  <line x1="375" y1="76" x2="375" y2="95" stroke="currentColor"/>
  <line x1="445" y1="76" x2="445" y2="95" stroke="currentColor"/>
  <line x1="300" y1="95" x2="445" y2="95" stroke="currentColor"/>
  <text x="372" y="110" text-anchor="middle" font-size="10" fill="currentColor">network (slower)</text>
  <text x="372" y="130" text-anchor="middle" font-size="10" fill="currentColor">each node's memory is local to it alone</text>
</svg>
<figcaption>Shared memory: every core on a node can reach the same memory directly. Distributed
memory: each node has its own memory, and reaching another node's data means crossing the network.</figcaption>
</figure>

With **shared memory**, every core is accessing the same memory, so there is no need to pass
messages between machines. That said, unless you're specifically using threading (or, in some
cases, forked processes), objects are still *copied* when new processes are created to do the work
— threads are the exception, since multiple threads can read and write the same object without an
explicit copy (at the cost of needing to be careful that threads on different cores don't overwrite
memory another thread is using; this is generally not something you need to worry about yourself in
R or Python). Two shared-memory approaches appear later in this chapter: threaded linear algebra,
and multicore/multiprocess functionality.

If you watch CPU usage (`top`, on Linux or a Mac) while a threaded job runs, you'll see the process
using *more than 100%* of a CPU — it looks like a single process, but it's using several cores. This
is a different phenomenon from a *hyperthreaded* core, where the operating system is shown two cores
where there is physically one.

With **distributed memory**, parallel code has to pass messages between nodes explicitly. The
standard protocol for this is MPI (`openMPI` being one implementation). Several Python and R
packages use MPI under the hood, but this chapter only covers distributed-memory parallelization via
`Dask`, which does not use MPI.

## GPUs

GPUs (Graphics Processing Units) were originally built to render graphics quickly, which they do
with a very large number of simple processing units working in parallel. General-purpose GPU
(GPGPU) computing exploits that same capability for computation unrelated to graphics. Most
researchers never program a GPU directly; instead they use software (machine-learning libraries such
as PyTorch or Tensorflow, or software like JAX that reaches for the GPU automatically) that has
already been written to use one when available. Computation that runs on the GPU runs in *kernels* —
functions launched onto the GPU — while the overall workflow still runs on the CPU and only hands off
the computationally heavy parts. GPUs (and similar devices such as TPUs) are accordingly often called
**co-processors**.

A GPU's memory is physically separate from the computer's main memory, so code that uses a GPU
should avoid shuttling large amounts of data back and forth between the two. There is also overhead
in launching a kernel, so it pays to avoid launching many small kernels relative to the amount of
work each one does.

## Other approaches, briefly

Two more approaches are worth naming even though they get fuller treatment elsewhere:

- **Spark and Hadoop** implement computation in a distributed-memory environment using the
  MapReduce approach — covered in the following unit on data at scale, not here.
- **Cloud computing** (Amazon EC2, Google Compute Engine, Microsoft Azure) rents out virtual
  machines on a pay-as-you-go basis: you choose the number of cores, configure the machine with
  whatever software and data you need, and then use it like any other remote machine — including
  assembling several virtual machines into your own virtual cluster.

## Choosing a parallelization strategy

Before reaching for a specific tool, a few questions decide whether a given parallelization will
actually help:

- **How much memory will the various processes use?** How much data has to be communicated between
  them, and with how much latency? How much does one process have to wait on another before it can
  proceed?
- **One node, or many?** If a computation fits on the cores of a single node with shared memory,
  that will beat spreading the same (or even somewhat more) cores across multiple nodes — the same
  is true of jobs with heavy memory demands that seem to call for Spark or Hadoop but might run much
  faster on a single machine with enough memory. Distributed memory only becomes necessary once a
  single node's memory genuinely isn't enough.
- **Which loop do I parallelize?** With nested loops, you generally only want to parallelize at one
  level — usually the outer loop — though later in this chapter there are tools for parallelizing
  at more than one level at once. The goal is a load-balanced computation that doesn't require much
  communication. Watch out for parallelizing a loop whose body *also* calls threaded linear algebra:
  usually you want one or the other, not both competing for the same cores.
- **How do I balance communication overhead against keeping every core busy?** Too few tasks — or
  tasks of very different lengths — and some cores sit idle while others are still working: poor
  load-balancing. Too many (small) tasks and the overhead of starting and stopping each one erodes
  the benefit of parallelizing at all.

That last trade-off has a name. Should the tasks be handed to workers all at once in advance
(**static allocation**, or *prescheduling*), or should each worker be given a new task only once it
finishes the last one (**dynamic allocation**)? Concretely: with 6 tasks and 3 workers, static
allocation might assign worker 1 tasks 1 and 4 up front, worker 2 tasks 2 and 5, and worker 3 tasks 3
and 6. Dynamic allocation instead starts worker 1 on task 1, worker 2 on task 2, worker 3 on task 3,
and only hands out task 4 once *some* worker (not necessarily worker 1) actually finishes — so tasks
aren't tied to particular workers in advance.

If many tasks all take about the same time, prescheduling reduces communication overhead (each
worker is only contacted once, for its whole batch, rather than once per task) with little
load-balancing cost. If there are few tasks, or their running times vary a lot, prescheduling risks
an unlucky batch — several slow tasks landing on one worker while the others sit idle after finishing
their own batches — so dynamic allocation is the safer choice. R's parallel tools generally let you
choose: the `future` package's `future_lapply` takes `future.scheduling` and `future.chunk.size`
arguments, and `mclapply()` has `mc.preschedule`. The worked example later in this chapter (Scenario
4) makes the cost of getting this wrong concrete.

## Dask: separating what to parallelize from how

Before working through case studies, it's worth setting out the key idea behind `Dask` (which mirrors
R's `future` package, and Python's `ray`): **abstract the specification of what should be
parallelized away from the computational resources it will actually run on** — sometimes called the
*backend*. The point is to write the computation once and let different users, or the same user on
different days, run it on whatever hardware happens to be available without touching the code that
does the computing itself. (There are many other Python packages for this — `ipyparallel`, `ray`,
`multiprocessing`, `pp` — Dask is simply the one used throughout this course, partly because it also
handles distributed *datasets*, covered in the following unit.)

You choose Dask's *scheduler* to control whether code runs across multiple cores, multiple machines,
and how many cores per machine:

```python
import dask
dask.config.set(scheduler='processes', num_workers=4)
```

| Scheduler | Description | Multi-node? | Copies objects? |
|---|---|---|---|
| `synchronous` | not parallel at all (serial) | no | no |
| `threads` | threads inside the current Python session | no | no |
| `processes` | background Python sessions | no | yes |
| `distributed` | Python sessions across multiple nodes | yes | yes |

Two caveats on that table matter in practice. First, Python's Global Interpreter Lock (GIL) prevents
threading of pure Python code, so `threads` mostly helps computation that's already handed off to
C/C++/Cython — numeric work in `numpy` arrays or `pandas` dataframes, for instance — not ordinary
Python loops. Second, `distributed` is entirely fine to use on a single machine (even a laptop): per
Dask's own documentation it has advantages over `processes`, including a diagnostic dashboard and
better handling of when copies actually need to be made — and it's required for a parallel *map*
(Scenario 3 below).

Dask (like `future`) is usually good at figuring out which packages and global variables your
parallelized code needs, and shipping those to the workers automatically — in other contexts you may
need to *export* variables and load packages on the workers yourself. Work is flagged for
parallelization with the `@dask.delayed` decorator (or, equivalently, by wrapping the call as
`dask.delayed(myfun)(i)`), and nothing actually runs until `dask.compute(...)` is called:

```python
import dask
dask.config.set(scheduler='processes', num_workers=4, chunksize=1)

@dask.delayed
def myfun(idx):
    return np.random.normal(size=n)

tasks = [myfun(i) for i in range(p)]
results = dask.compute(tasks)   # nothing has run until this line
```

This is **lazy evaluation**: a `delayed` object just represents a computation still to be done, and
Dask works out the computational graph connecting a set of such objects before running any of it.
`dask.compute` then executes **synchronously** — the main process blocks until it's finished — which
is why this style of call is also called a *blocking* call. (The opposite, where control returns to
the caller before the workers are done, is *asynchronous*/*non-blocking*.)

### R's `future` package, briefly

The `future` package plays the same role in R (alongside older, less unified approaches:
`parallel::parLapply`, `parallel::mclapply`, `foreach` without `future`, and `partools`, which tries
to take just the distributed file system and distributed data ideas from Spark/Hadoop and discard
the fault-tolerance machinery). A *future* is a flag on an expression saying that when and where it
gets evaluated is controlled elsewhere: it's an abstraction for a value that will be available
later, whose state is either unresolved or resolved. As with Dask, the point is to write generic
code and set the *plan* for how it runs separately:

```r
plan(multisession)               # or: plan(multisession, workers = 4)
```

| Plan | Description | Multi-node? | Copies objects? |
|---|---|---|---|
| `multisession` | additional R sessions as workers | no | yes |
| `multicore` | forked R processes as workers | no | not if the object is unmodified |
| `cluster` | R sessions on other machine(s) | yes | yes |

`future` (via the `globals` package) automatically finds and ships the packages and global variables
a parallelized function needs, much as Dask does:

```r
library(future); library(future.apply)
plan(multisession)
library(MASS)
n <- nrow(geyser)
myfun <- function(idx) sum(geyser$duration) / n   # geyser found automatically
future_sapply(1:5, myfun)
```

One difference worth flagging against the strategy discussion above: `future`'s default is static
allocation (prescheduling), whereas Dask's `processes` scheduler defaults to a chunk size of 6 tasks
per batch and its `distributed` scheduler is always dynamic.

## Case studies

The rest of the chapter works through the scenarios a statistician actually runs into, roughly in
order of how many independent tasks there are — from one, to a handful, to thousands — since that's
what decides which of the tools above actually applies.

### Fitting a single model

If a model implementation was written to be parallel already, the job is just to find the argument
that turns it on — usually named with some combination of *threads*, *processes*, *cores*, *cpus*,
or *jobs* (scikit-learn's `RandomForestClassifier` takes `n_jobs`, for example).

Failing that, if the method does heavy linear algebra, both Python and R hand matrix operations off
to a **BLAS** (Basic Linear Algebra Subprograms) library, and several fast BLAS implementations —
Intel's MKL, the open-source OpenBLAS, Apple's Accelerate/vecLib on Macs — are themselves *threaded*:
given free cores, they'll use more than one automatically, provided the program is linked against a
threaded BLAS and the shell variable `OMP_NUM_THREADS` isn't set to 1 (Macs use
`VECLIB_MAXIMUM_THREADS`; MKL uses `MKL_NUM_THREADS`). The effect is real: computing $X^\top X$ and
its Cholesky factor for a $6000 \times 6000$ matrix took 6.6 seconds on a single thread and 3 seconds
using 8, in one test run. It isn't guaranteed, though — for smaller matrices, threaded linear algebra
can show no speedup, or even come out slower, since setting up the parallelization has its own cost
and the threaded algorithm sometimes does strictly more arithmetic than the serial one.

Large matrix operations are also a good fit for a **GPU**. Multiplying two $10000 \times 10000$
matrices with PyTorch took 100–200 milliseconds on a GPU against about 18 seconds on the CPU — more
than 100 times faster — though a fair comparison would also need to account for the GPU using 4-byte
(rather than 8-byte) floats and would want to control how many CPU cores were used for the CPU side
of the comparison. The same pattern shows up one level up, for *vectorized* (not just linear-algebra)
calculations: JAX applied to $y = e^x + 3\sin(x)$ over $5\times 10^8$ values took 4.7 seconds on the
CPU (already using several threads under the hood) and 0.015 seconds on a GPU.

### A handful of independent tasks

Fitting three different models to the same data is small-scale parallelism: with three or more free
cores, the obvious approach is one core per model (with access to a cluster and each model's own
parallelized implementation, one *node* per model instead). Using Dask's `processes` scheduler with
three `dask.delayed` tasks and `dask.compute` is enough to run all three fits at once. The lecture
that develops this example doesn't get a clean three-fold speedup and poses the question worth
sitting with: *why might parallelizing three independent, equally-sized model fits not give a
perfect three-fold speedup?* (`chunksize=1` was needed here to force Dask to start one task per
worker immediately, rather than batching a handful of tasks in a way that defeats the purpose when
there are only three of them — the general issue is Scenario 4, below.)

### A parallel map over many independent tasks

Ten-fold cross-validation, with a fit-and-predict function of one argument (the fold index), is the
natural case for a **parallel map**: run the same function over a range of inputs, spread across
however many workers are available.

```python
n_cores = 2
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers=n_cores)
c = Client(cluster)
tasks = c.map(cv_fit, range(n_folds))
results = c.gather(tasks)
```

A parallel map needs the `distributed` scheduler (which, as noted above, is fine on a single
machine). Note that the results come back and typically need to be re-sorted to line back up with
the folds they came from. With more folds than cores — say 10 folds and 4 cores — this simple
approach no longer divides evenly, which is exactly the situation the next scenario is about.

### Tasks with unequal running time: static vs. dynamic allocation, concretely

Set up an artificial mix of 4 slow tasks and 12 fast ones, and compare running them under a
dynamically-allocated scheduler (`distributed`, via `c.map`) against a statically-allocated one
(`processes`, whose default batches tasks in groups of 6). In one run of this experiment the dynamic
version finished in about 0.8 seconds, while the static version — whose default batching happened to
put all four slow tasks in the very first chunk, the worst possible draw — took about 2.6 seconds.
Re-running the same comparison another time gave much less clear-cut numbers: the point isn't the
exact ratio, which depends on how the batching happens to fall, but that static allocation can be
badly unlucky in a way dynamic allocation structurally cannot. Forcing Dask's `processes` scheduler
into dynamic allocation just means setting `chunksize=1`:

```python
dask.config.set(scheduler='processes', num_workers=4, chunksize=1)
```

The corresponding rule of thumb: with the `distributed` scheduler, Dask always starts each delayed
task separately (dynamic), and there's no way to ask it to batch tasks into chunks; if you want
static allocation you either use the `processes` scheduler on a single machine, or break the tasks
into batches by hand before handing them to `distributed`. If every task is fast and there are many
of them, static allocation is worth using deliberately, since it avoids paying the roughly
one-millisecond-per-task overhead of starting each one separately — the same trade-off as at the end
of the "Choosing a strategy" section above, now with numbers attached.

<figure>
<svg viewBox="0 0 460 235" role="img" aria-label="Static allocation leaves two workers idle after an unlucky batch of slow tasks lands on a third worker, while dynamic allocation keeps all three workers busy and finishes sooner">
  <text x="10" y="14" font-size="12" fill="currentColor">Static: batches fixed before any task starts</text>
  <text x="10" y="34" font-size="11" fill="currentColor">W1</text>
  <text x="10" y="59" font-size="11" fill="currentColor">W2</text>
  <text x="10" y="84" font-size="11" fill="currentColor">W3</text>
  <rect x="40" y="24" width="220" height="14" fill="currentColor" fill-opacity="0.3" stroke="currentColor"/>
  <text x="150" y="35" text-anchor="middle" font-size="10" fill="currentColor">two slow tasks land here</text>
  <rect x="40" y="49" width="60" height="14" fill="currentColor" fill-opacity="0.3" stroke="currentColor"/>
  <rect x="100" y="49" width="160" height="14" fill="none" stroke="currentColor" stroke-dasharray="3,2"/>
  <text x="180" y="60" text-anchor="middle" font-size="10" fill="currentColor">idle</text>
  <rect x="40" y="74" width="55" height="14" fill="currentColor" fill-opacity="0.3" stroke="currentColor"/>
  <rect x="95" y="74" width="165" height="14" fill="none" stroke="currentColor" stroke-dasharray="3,2"/>
  <text x="177" y="85" text-anchor="middle" font-size="10" fill="currentColor">idle</text>
  <line x1="260" y1="20" x2="260" y2="92" stroke="currentColor" stroke-dasharray="2,2"/>
  <text x="260" y="104" text-anchor="middle" font-size="10" fill="currentColor">all done</text>

  <text x="10" y="134" font-size="12" fill="currentColor">Dynamic: next task starts as soon as a worker frees up</text>
  <text x="10" y="154" font-size="11" fill="currentColor">W1</text>
  <text x="10" y="179" font-size="11" fill="currentColor">W2</text>
  <text x="10" y="204" font-size="11" fill="currentColor">W3</text>
  <rect x="40" y="144" width="120" height="14" fill="currentColor" fill-opacity="0.3" stroke="currentColor"/>
  <rect x="160" y="144" width="20" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="40" y="169" width="65" height="14" fill="currentColor" fill-opacity="0.3" stroke="currentColor"/>
  <rect x="105" y="169" width="65" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="40" y="194" width="70" height="14" fill="currentColor" fill-opacity="0.3" stroke="currentColor"/>
  <rect x="110" y="194" width="70" height="14" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <line x1="180" y1="140" x2="180" y2="212" stroke="currentColor" stroke-dasharray="2,2"/>
  <text x="180" y="224" text-anchor="middle" font-size="10" fill="currentColor">all done, sooner</text>
</svg>
<figcaption>The same four slow and twelve fast tasks under prescheduled batches versus
one-at-a-time assignment. Static allocation can strand idle workers behind whichever worker got
unlucky; dynamic allocation cannot, at the cost of contacting every worker once per task instead of
once per batch.</figcaption>
</figure>

### Nested loops and multiple nodes

With nested loops — folds within methods, say — you can always flatten the indices to turn the
nested loop into one long loop over `n * M` items:

```python
for idx in range(n * M):
    fold, method = idx // M, idx % M
    # ... code here
```

but you don't strictly have to: you can equally well generate the `delayed` tasks from inside the
nested loops directly, without flattening anything, as long as you're not relying on a parallel
*map* (which does need a flat range of inputs). R's `future` package has built-in support for
parallelizing nested loops without either workaround.

Once there's more than one machine involved, the same `map`/`gather` pattern from the parallel-map
scenario extends across nodes — the only change is how the cluster of workers is constructed:

```python
from dask.distributed import Client, SSHCluster
cluster = SSHCluster(["host1", "host2", "host2", "host3", "host3"])  # first host runs the scheduler
c = Client(cluster)
tasks = c.map(fun, range(n_tasks))
results = c.gather(tasks)
```

(On a cluster managed by Slurm, the list of allocated machine names can be recovered with
`srun hostname`, prepending the first machine's name again to account for the scheduler process.)

### Avoiding unnecessary copies of a large dataset

Stratified analysis of a very large dataset raises a different problem: even on a single node with
shared physical memory, most parallelization tools still make each worker its own *copy* of the
data, because separate processes don't share access to each other's objects even while the
underlying RAM is physically shared. Tagging each task with the id of the data object and the
process id that handled it shows this directly with Dask's `processes` scheduler — one copy is made
per *task* here, the worst case:

```python
dask.config.set(scheduler='processes', num_workers=4, chunksize=1)
tasks = [dask.delayed(do_analysis)(i, x) for i in range(8)]
results = dask.compute(tasks)
```

Switching to the `threads` scheduler removes the copying entirely, since threads share memory
directly — at the cost that you can no longer safely *modify* the shared object from within a task
without risking interference between tasks. Using the `distributed` scheduler instead, applying
`dask.delayed()` to the data object itself before passing it into the tasks gets down to one copy
per *worker* rather than one per task — though the `distributed` scheduler's own optimizations
around which worker gets which task make it harder to predict or verify exactly how many copies get
made in a given run.

### Parallel random number generation

Running $n = 1000$ replicates of a simulation, each fitting a couple of models, is again a case
where you just parallelize across replicates directly (short of access to hundreds of cores). What
needs care is the random numbers: a pseudo-random generator produces a long but finite,
eventually-repeating sequence, and setting a seed just chooses where in that sequence to start.
Setting a different (arbitrary) seed per replicate risks two replicates' subsequences overlapping —
probably unlikely if you're not drawing huge numbers of random values per replicate, but not
something you can easily be sure of.

`numpy`'s PCG64 and MT19937 generators solve this properly with a `jumped()` method, which advances
the generator's state as if a very large number of values (on the order of $2^{128}$) had already
been drawn — the same jump advances the state by the same amount every time, so `jumped(2)` and two
successive `jumped(1)` calls land in the same place:

```python
bitGen = np.random.PCG64(1)
rng = np.random.Generator(bitGen.jumped(1))
```

giving a simple recipe for parallel-safe streams: seed every task identically, then call
`bitGen.jumped(i)` with the task's own index `i`. (Exactly why `jumped(1)` advances the state by
something close to the generator's *entire period* is not obvious, and is flagged in the lecture as
something the instructor doesn't fully understand either — treat the recipe as reliable, not
necessarily the explanation for why the jump size is what it is.) `numpy`'s own documentation
recommends a related but more direct approach, using `SeedSequence` to *spawn* independent
generators rather than relying on `jumped()` at all:

```python
sg = np.random.SeedSequence(1)
rngs = [np.random.Generator(np.random.PCG64(s)) for s in sg.spawn(n_tasks)]
```

R's `rlecuyer` package solves the same problem using the L'Ecuyer algorithm, whose period of
$2^{191}$ is divided into subsequences of length $2^{127}$ — one per stream. This chapter only
introduces the problem; the fuller treatment is in the Simulation unit.

## Some further details

Two smaller points round out the chapter, both about squeezing out overhead rather than about a new
scenario:

- **Do all the work inside one `compute()` call.** Dask generally doesn't keep every piece of a
  distributed dataset in memory, so computing several separate quantities from data that's read off
  disk (say, both the minimum and the maximum of a column) can mean re-reading the data once per
  call if each is computed with its own `.compute()`. Combining everything needed into a single
  computational graph — one call to `dask.compute(a, b)` instead of two calls to `a.compute()` and
  `b.compute()` — can be far cheaper, since the whole graph is figured out once and the data is only
  touched once.
- **Threads and the parallel tools don't compose for free.** Threaded code (BLAS included) detects
  and uses however many cores are free by default, but the number of threads can also be set
  explicitly via the `OMP_NUM_THREADS` environment variable (`VECLIB_MAXIMUM_THREADS` on a Mac),
  e.g. `export OMP_NUM_THREADS=4` before starting a session, or `OMP_NUM_THREADS=4 R CMD BATCH ...`
  when launching a job directly. If you're already using the tools above to run many independent
  tasks at once — one task per core — it's usually better to give each individual task exactly one
  thread (`OMP_NUM_THREADS=1`) rather than let a threaded BLAS inside each task compete with the
  outer, task-level parallelism for the same cores.

## Sources

- Berkeley STAT 243, Unit 6 ("Parallel processing"/"Parallel computation"), fall-2026 offering,
  used as the primary text: `units/unit6-parallel/01-overview.md` (motivation, the four routes to a
  faster computation); `02-1-some-scenarios-for-parallelization.md` (embarrassingly parallel
  problems, linear speedup); `03-2-overview-of-parallel-processing.md` (hardware vocabulary,
  shared/distributed memory, threading, GPUs, Spark/Hadoop, cloud computing);
  `04-3-parallelization-strategies.md` (choosing a strategy, static vs. dynamic allocation);
  `05-4-introduction-to-dask.md` (the backend-abstraction idea, scheduler table, `@delayed`);
  `06-5-illustrating-the-principles-in-specific-case-studies.md` (all of the worked scenarios: BLAS
  and GPU timings, the parallel map, static-vs-dynamic with concrete numbers, nested loops and
  multiple nodes, avoiding copies, parallel RNG); `07-6-additional-details-and-topics-optional.md`
  (single-`compute()` pattern, `OMP_NUM_THREADS`); `08-7-introduction-to-r-s-future-package-optional.md`
  (R's `future`, `plan()`, the `multisession`/`multicore`/`cluster` backends).
- The fall-2024 offering of the same unit (CC BY 4.0) was consulted alongside fall-2026 and is
  essentially the same lecture; the one substantive difference used here is in the static-vs-dynamic
  allocation example, where fall-2024 reports concrete timings (0.8 s dynamic vs. 2.6 s static) that
  fall-2025/fall-2026 do not reproduce as cleanly — both are cited since the point of the example is
  that the outcome depends on how the batching happens to fall, which the discrepancy between the
  two runs itself illustrates. The fall-2025 offering is textually identical to fall-2026 apart from
  source metadata.
- `stat243-fall-2021/units/unit6-numbers.md` was supplied alongside the above but is a naming
  collision rather than another treatment of this material: in that year's offering, "Unit 6" covered
  floating-point number representation, a different subject, and it is not used here.
- Two tutorials referenced by the unit are not contained in the supplied material and so are not
  reproduced: a tutorial on parallel processing with Dask and `future`
  (`computing.stat.berkeley.edu/tutorial-dask-future`), and a tutorial on parallelization across
  languages including PyTorch and JAX (`computing.stat.berkeley.edu/tutorial-parallelization`). The
  unit's own pointers to Unit 5 (efficient implementation, JAX JIT compilation), Unit 7 (Spark,
  Hadoop, distributed datasets), and the Simulation unit (random number generation in full) refer to
  material outside this chapter's scope. No exercises were supplied with this unit.

---

[← 43. Programming Language Mechanics](43-programming-language-mechanics.md) · [Contents](index.md) · [45. Preparatory Notes on Big Data →](45-preparatory-notes-on-big-data.md)
