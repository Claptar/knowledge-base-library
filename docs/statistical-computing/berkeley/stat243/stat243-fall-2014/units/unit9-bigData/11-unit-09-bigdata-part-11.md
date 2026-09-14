---
title: Unit 09 — bigData Part 11 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — bigData Part 11 —

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# We can view system status through a web browser interface # on master node of the EC2 cluster, do: MASTER_IP=`cat /root/ephemeral-hdfs/conf/masters` echo ${MASTER_IP} # Point a browser on your own machine to the result of the next command # you'll see info about the "Spark Master", i.e., the cluster overall echo "http://${MASTER_IP}:8080/" # Point a browser on your own machine to the result of the next command # you'll see info about the "Spark Stages", i.e., the status of Spark tasks echo "http://${MASTER_IP}:4040/" # Point a browser on your own machine to the result of the next command # you'll see info about the HDFS" echo "http://${MASTER_IP}:50070/"

---

[← Unit 09 — bigData Part 10 —](10-unit-09-bigdata-part-10.md) · [Up: contents](index.md) · [Unit 09 — bigData Part 12 — →](12-unit-09-bigdata-part-12.md)
