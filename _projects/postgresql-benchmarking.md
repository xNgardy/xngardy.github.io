---
title: PostgreSQL Performance & Concurrency
description: An experimental comparison of database configuration and Python concurrency on a ten-million-row workload.
short_description: Benchmarked query performance and sequential, threaded, and asynchronous execution on two PostgreSQL configurations with ten million rows.
category: Systems / Performance analysis
filter: ml
period: AI specialization project
order: 5
role: Project developer
tools: Python · PostgreSQL 17 · Threading · Asyncio
repository: https://github.com/xNgardy/YZUP_Parallel_Programming_on_PostgreSQL_Servers
visual: database-visual
visual_label: 10M rows
visual_subtitle: Configuration × concurrency
---

## Configuration and concurrency together

This project examines how PostgreSQL server configuration affects query latency and throughput, and how **sequential execution, threading, and asyncio** behave under the tested workload.

I compared an optimized and a deliberately poorly configured PostgreSQL server using **10 million rows**. The test environment used Ubuntu 22.04 LTS with four CPUs and 8 GB of RAM.

## Experimental setup

The benchmarks included indexed ID lookups, email searches, date-range filters, and grouping and sorting queries. Separate Python benchmarks compared concurrency approaches across the two configurations.

## Observations

- Indexed ID lookups were approximately **4× faster** on the optimized configuration in the recorded tests.
- Threading reached a **4.08× speedup** on the optimized server.
- Asyncio achieved roughly **1.6–2.0×** speedup in the tested setup.
- Database configuration affected how much benefit the parallel workloads could obtain.

These results apply to the specific hardware, queries, drivers, and configurations tested. They do not establish that threading is faster than asyncio for every database workload.

Benchmark scripts, server configuration files, and project documentation are available in the [repository](https://github.com/xNgardy/YZUP_Parallel_Programming_on_PostgreSQL_Servers).
