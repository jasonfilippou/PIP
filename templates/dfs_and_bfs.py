from typing import List
from collections import deque

def dfs(G: List[List[int]], start:int) -> List[bool]:
    n = len(G)
    visitation_list = [False for _ in range(n)]

    def visit(node:int):
        for nbr in G[node]:
            if not visitation_list[nbr]:
                visitation_list[nbr] = True
                visit(nbr)
    visitation_list[start] = True
    visit(start)
    return visitation_list  # Or whatever else you want to return

def bfs(G: List[List[int]], start:int) -> List[bool]:
    n = len(G)
    visitation_list = [False for _ in range(n)]
    queue = deque([])
    queue.append(start)
    visitation_list[start] = True
    while len(queue) > 0:
        top_node = queue.popleft()
        for neighbor in G[top_node]:
            if not visitation_list[neighbor]:
                visitation_list[neighbor] = True
                queue.append(neighbor)
    return visitation_list  # Or whatever else you want to return

# Getting the minimum distances from a given node in an unweighted, directed graph using BFS:
def minimum_distances(G: List[List[int]], start:int) -> List[int]:
    n = len(G)
    dist = [-1 for _ in range(n)]       # You will use this as a kind of visitation list. See loop.
    queue = deque([])
    queue.append(start)
    dist[start] = 0
    while len(queue) > 0:
        top_node = queue.popleft()
        for neighbor in G[top_node]:
            if dist[neighbor] == -1:        # Equivalent to "not in set"
                dist[neighbor] = dist[top_node] + 1
                queue.append(neighbor)
    return dist

# In the minimum length path that connects the "start" node to any other node, store the predecessor of every node.
# This allows you to reconstruct the path from any node to the start node.
def get_predecessors(G: List[List[int]], start:int) -> List[int]:
    n = len(G)
    pred = [- 1 for _ in range(n)]
    queue = deque([])
    queue.append(start)
    pred[start] = 0
    while len(queue) > 0:
        top_node = queue.popleft()
        for neighbor in G[top_node]:
            if pred[neighbor] == -1:    # unvisited neighbor
                pred[neighbor] = top_node
                queue.append(neighbor)
    return pred

# Path reconstruction given `pred` array that the method above returns:"
def reconstruct_path(pred: List[int], end:int)->List[int]:
    path = []
    curr_node = end
    path.insert(0, curr_node)       # This better be a linked list...
    while pred[curr_node] > 0:      # As long as we haven't reached the start node
        path.insert(0, curr_node)
        curr_node = pred[curr_node]