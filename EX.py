import heapq

# ----------------------------
# Graph Representation
# ----------------------------

vertices = 7

edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (2, 4, 2),
    (3, 5, 3),
    (4, 5, 2),
    (5, 6, 1)
]


# ----------------------------
# Disjoint Set for Kruskal
# ----------------------------

class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u, v):

        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v

        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u

        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


# ----------------------------
# Kruskal's Algorithm
# ----------------------------

def kruskal():

    mst = []
    total_weight = 0

    ds = DisjointSet(vertices)

    sorted_edges = sorted(edges, key=lambda x: x[2])

    for u, v, weight in sorted_edges:

        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# ----------------------------
# Prim's Algorithm
# ----------------------------

def prim():

    graph = [[] for _ in range(vertices)]

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False] * vertices

    pq = [(0, 0, -1)]

    mst = []
    total_weight = 0

    while pq:

        weight, node, parent = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        total_weight += weight

        if parent != -1:
            mst.append((parent, node, weight))

        for neighbour, w in graph[node]:

            if not visited[neighbour]:
                heapq.heappush(
                    pq,
                    (w, neighbour, node)
                )

    return mst, total_weight


# ----------------------------
# Display Results
# ----------------------------

print("\nKRUSKAL'S ALGORITHM\n")

mst1, weight1 = kruskal()

for u, v, w in mst1:
    print(f"{u} -- {v} = {w}")

print("\nTotal Weight =", weight1)


print("\nPRIM'S ALGORITHM\n")

mst2, weight2 = prim()

for u, v, w in mst2:
    print(f"{u} -- {v} = {w}")

print("\nTotal Weight =", weight2)


print("\nVerification")

if weight1 == weight2:
    print("Both algorithms produce the SAME MST weight.")
else:
    print("Weights are different.")
