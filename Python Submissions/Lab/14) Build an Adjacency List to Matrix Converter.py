def adjacency_list_to_matrix(adjancency_list):
    n = len(adjancency_list)
    matrix = [[0] * n for _ in range(n)]

    for node, neighbor_list in adjancency_list.items():
        for neighbor in neighbor_list:
            matrix[node][neighbor] = 1

    for node in range(n):
        print(matrix[node])

    return matrix
