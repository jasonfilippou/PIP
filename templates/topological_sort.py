def _topologicalSort(G):               # It is assumed that we get the graph in an adjacency list format.
    inDegrees = _calculateInDegrees(G)
    zeroInDegreeNodes = [node for (node, inDegree) in enumerate(inDegrees) if inDegree == 0]
    ordering = []
    while zeroInDegreeNodes:
        node = zeroInDegreeNodes.pop()
        ordering.append(node)
        for neighbor in G[node]:
            inDegrees[neighbor] -= 1
            if inDegrees[neighbor] == 0:
                zeroInDegreeNodes.append(neighbor)
    return ordering if len(ordering) == len(G) else []

def _calculateInDegrees(G):      # Once again, assumed that we get the graph in an adjacency list format.
    inDegrees = [0 for _ in range(len(G))]
    for neighborNodes in G:
        for node in neighborNodes:
            inDegrees[node] += 1
    return inDegrees