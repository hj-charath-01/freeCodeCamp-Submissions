def dfs(adj_mat, start_node):
    n = len(adj_mat)
    visited = [False] * n

    reachable = []

    stack = [start_node]
    while stack:
        curr = stack.pop()
        visited[curr] = True
        for node, adj in enumerate(adj_mat[curr]):
            if visited[node] or adj == 0:
                continue
            stack.append(node)
        reachable.append(curr)

    return reachable
