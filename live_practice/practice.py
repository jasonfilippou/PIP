def create_adj_list(edge_list, num_nodes, is_directed=True):
    adj_list = [[] for _i in range(num_nodes)]
    for (i, j) in edge_list:
        adj_list[i].append(j)
        if not is_directed and i != j:
            adj_list[j].append(i)
    return adj_list


def create_adj_map(edge_list, num_nodes, is_directed=True):
    adj_mat = [[0] * num_nodes] * num_nodes
    for (i, j) in edge_list:
        adj_mat[i][j] = 1
        if not is_directed and i != j:
            adj_mat[j][i] = 1
    return adj_mat


def to_adj_mat(adjacency_list, is_directed = True):
    num_nodes = len(adjacency_list)
    adj_mat = [[0] * num_nodes] * num_nodes
    for (node, neighbors) in enumerate(adjacency_list):
        for x in neighbors:
            adj_mat[node][x] = 1
            if not is_directed and node != x:
                adj_mat[x][node] = 1
    return adj_mat

def _to_adj_list(adjacency_map, is_directed = True):
    num_nodes = len(adjacency_map)
    adj_list = [[] for _i in range(num_nodes)]
    for i in range(len(adjacency_map)):
        for j in range(len(adjacency_map[i])):
            if adjacency_map[i][j] == 1:
                adj_list[i].append(j)
                if not is_directed and i != j:
                    adj_list[j].append(i)