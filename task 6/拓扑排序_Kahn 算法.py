def Khan(graph):
    in_degree = {}
    result = []
    for u in graph:
        if u not in in_degree:
            in_degree[u] = 0
        for v in graph[u]:
            if v not in in_degree:
                in_degree[v] = 0
            in_degree[v] += 1

    while in_degree:
        for u in in_degree.copy():
            if in_degree[u] == 0:
                in_degree.pop(u)
                result.append(u)
                for v in graph[u]:
                    in_degree[v] -= 1
    print(result)


G = {
    'a': {'b', 'c', 'd', 'e', 'f'},
    'b': {'c', 'd', 'e', 'f'},
    'c': {'d', 'e', 'f'},
    'd': {'e', 'f'},
    'e': {'f'},
    'f': {}
}

Khan(G)
