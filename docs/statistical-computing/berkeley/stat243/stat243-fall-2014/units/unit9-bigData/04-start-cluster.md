---
title: start cluster
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# start cluster

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

./spark-ec2 -k ec2star -i ~/.ssh/ec2star.rsa --region=us-west-2 \ -s ${CLUSTER_SIZE} -w 300 -v ${SPARK_VERSION} launch sparkvm

---

[← Unit 09 — bigData Part 03 —](03-unit-09-bigdata-part-03.md) · [Up: contents](index.md) · [login to cluster →](05-login-to-cluster.md)
