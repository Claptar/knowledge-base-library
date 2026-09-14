---
title: 'Submitting jobs: accounts and partitions'
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s07/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Submitting jobs: accounts and partitions

**Source:** [`section/s07/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

All computations are done by submitting jobs to the scheduling software that manages jobs on the cluster, called SLURM.

When submitting a job, the main things you need to indicate are the project account you are using (for most of you this will only be ic_stat243, in which case you don't need to specify the account as it will be set by default)  and the partition.

You can see what accounts you have access to and which partitions within those accounts as follows:

```
sacctmgr -p show associations user=SAVIO_USERNAME
```

Here's an example of the output for a user who has access to various accounts. For your account you'll only see 'ic_stat243' as the accounts (in the second column) you have access to.


```
Cluster|Account|User|Partition|Share|GrpJobs|GrpTRES|GrpSubmit|GrpWall|GrpTRESMins|MaxJobs|MaxTRES|MaxTRESPerNode|MaxSubmit|MaxWall|MaxTRESMins|QOS|Def QOS|GrpTRESRunMins|
brc|co_stat|paciorek|savio2_gpu|1||||||||||||savio_lowprio|savio_lowprio||
brc|co_stat|paciorek|savio2_htc|1||||||||||||savio_lowprio|savio_lowprio||
brc|co_stat|paciorek|savio|1||||||||||||savio_lowprio|savio_lowprio||
brc|co_stat|paciorek|savio_bigmem|1||||||||||||savio_lowprio|savio_lowprio||
brc|co_stat|paciorek|savio2|1||||||||||||savio_lowprio,stat_normal|stat_normal||
brc|fc_paciorek|paciorek|savio2|1||||||||||||savio_debug,savio_normal|savio_normal||
brc|fc_paciorek|paciorek|savio|1||||||||||||savio_debug,savio_normal|savio_normal||
brc|fc_paciorek|paciorek|savio_bigmem|1||||||||||||savio_debug,savio_normal|savio_normal||
brc|ac_scsguest|paciorek|savio2_htc|1||||||||||||savio_debug,savio_normal|savio_normal||
brc|ac_scsguest|paciorek|savio2_gpu|1||||||||||||savio_debug,savio_normal|savio_normal||
brc|ac_scsguest|paciorek|savio2|1||||||||||||savio_debug,savio_normal|savio_normal||
brc|ac_scsguest|paciorek|savio_bigmem|1||||||||||||savio_debug,savio_normal|savio_normal||
brc|ac_scsguest|paciorek|savio|1||||||||||||savio_debug,savio_normal|savio_normal||
```

---

[← Software modules](11-software-modules.md) · [Up: contents](index.md) · [Interactive jobs →](13-interactive-jobs.md)
