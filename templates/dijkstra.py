# In the absence of a heap that allows us an efficient implementation of decrease_priority, we will
# implement lazy dijkstra. This version of dijkstra adds neighbors in the priority queue after it updates its
import math
from typing import List
from heapq import heappush, heappop
from collections import deque       # For efficient reconstruction of the path, avoiding reversals or O(n) front insertions encountered with raw lists.


# Input: A graph in the form of an adjacency list with weighted but NON-NEGATIVE edges.
def lazy_dijkstra(G: List[List[tuple[int, int]]], source: int) -> (List[int], List[int]):
    dist = [math.inf for _ in range(len(G))]
    prev = [-1 for _ in range(len(G))]
    dist[source] = 0
    heap = []
    heappush(heap, (0, source))  # Put the distance first so that the pushing and popping happen over it.
    while heap:
        min_dist, node = heappop(heap)
        if min_dist == dist[node]:    # Only continue if you haven't visited the node before.
            for neighbor, edge_weight in G[node]:
                new_dist = dist[node] + edge_weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = node
                    heappush(heap, (new_dist, neighbor))
    return dist, prev


def reconstruct_path(prev: List[int], end: int) -> List[int]:
    curr = end
    path = deque([])
    while prev[curr] != -1:
        path.appendleft(curr)
        curr = prev[curr]
    path.appendleft(curr)
    return list(path)


if __name__ == '__main__':

    # Graph taken from Fiset's video here: https://www.youtube.com/watch?v=pSqmAO-m7Lk

    G = [
            [(1, 5), (2, 1)],
            [(3, 3), (2, 2), (4, 20)],
            [(1, 3), (4, 12)],
            [(2, 3), (4, 2), (5, 6)],
            [(5, 1)],
            []
        ]

    dist, prev = lazy_dijkstra(G, 0)
    for i in range(1, len(G)):
        print(f"For node {i}, minimum distance of {dist[i]} attained through path: {reconstruct_path(prev, i)}.")
