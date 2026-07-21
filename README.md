# DAA-EX-3
# Implementation of Kruskal's and Prim's Algorithms for Minimum Spanning Tree

## Overview

This project implements Kruskal's and Prim's algorithms to construct the Minimum Spanning Tree (MST) of a weighted undirected graph containing seven vertices and nine edges. The implementation verifies that both algorithms produce the same minimum total weight and compares their time complexities.

## Problem Statement

Given a weighted undirected graph with 7 vertices (0–6) and 9 edges, find the Minimum Spanning Tree using both Kruskal's and Prim's algorithms. Verify that both algorithms produce the same total minimum weight and analyze their time complexity.

## Graph Specifications

* Number of Vertices: 7
* Number of Edges: 9
* Graph Type: Weighted Undirected Graph

### Edge List

| Edge | Weight |
| ---- | ------ |
| 0-1  | 4      |
| 0-2  | 3      |
| 1-2  | 1      |
| 1-3  | 2      |
| 2-3  | 4      |
| 2-4  | 2      |
| 3-5  | 3      |
| 4-5  | 2      |
| 5-6  | 1      |

## Algorithms Used

### Kruskal's Algorithm

* Uses Disjoint Set Union (Union-Find).
* Sorts edges according to their weights.
* Adds the smallest edge that does not create a cycle.

#### Time Complexity

* Sorting Edges: O(E log E)
* Union-Find Operations: O(E)
* Overall Complexity: O(E log E)

### Prim's Algorithm

* Uses a Priority Queue (Min Heap).
* Expands the MST by selecting the minimum weighted adjacent edge.

#### Time Complexity

* Priority Queue Implementation: O(E log V)

## Performance Analysis

| Algorithm | Time Complexity |
| --------- | --------------- |
| Kruskal   | O(E log E)      |
| Prim      | O(E log V)      |

## Output Verification

Both algorithms produce:

* Total Minimum Weight = 12

This confirms the correctness of the implementations.

## Project Structure

```text
MST-Analysis/

│── mst_analysis.py
│── index.html
│── README.md
```

## Applications

* Computer Networks
* Transportation Systems
* Circuit Design
* Image Segmentation
* Network Optimization
* Resource Allocation Problems

## Conclusion

The comparative study demonstrates that both Kruskal's and Prim's algorithms correctly generate the Minimum Spanning Tree with the same minimum total weight. Kruskal's algorithm is particularly suitable when the graph is represented as an edge list, whereas Prim's algorithm performs efficiently when adjacency lists and priority queues are employed.

## Technologies Used

* Python 3
* Heap Queue (heapq)
* Disjoint Set Union (DSU)

### Author

**Akash N**

* B.E. Computer Science and Engineering (AI)
* Chennai Institute of Technology, Chennai
