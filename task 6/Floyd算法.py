# 任意两点的最短路径
def floyd(graph):
    path = {}

    for start in graph:
        path.setdefault(start, {})
        for end in graph[start]:
            if start == end:
                continue

            path[start].setdefault(end, [start, end])
            new_node = None

            for mid in graph:
                if mid == end:
                    continue

                new_distance = graph[start][mid] + graph[mid][end]
                if new_distance < graph[start][end]:
                    graph[start][end] = new_distance
                    new_node = mid
            if new_node:
                path[start][end].insert(-1, new_node)
    return graph, path


if __name__ == '__main__':
    ini = float('inf')
    # graph_list = [[0, 2, 1, 4, 5, 1],
    #               [1, 0, 4, 2, 3, 4],
    #               [2, 1, 0, 1, 2, 4],
    #               [3, 5, 2, 0, 3, 3],
    #               [2, 4, 3, 4, 0, 1],
    #               [3, 4, 7, 3, 1, 0]]

    graph_dict = {"s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4},
                  "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2},
                  "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1},
                  "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0},
                  }

    new_graph, path = floyd(graph_dict)
    # new_graph, path = floyd(graph_list)
    print(new_graph, '\n\n\n', path)
