# 起始点到任意一点的最短路径
def dijkstra(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    visited = [start]
    distance_graph = {start: 0}

    while nodes:
        distance = float("inf")
        for v in visited:
            for d in nodes:
                new_distance = graph[start][v] + graph[v][d]
                if new_distance < distance:
                    distance = new_distance
                    next_node = d
                    graph[start][d] = new_distance
        distance_graph[next_node] = distance
        visited.append(next_node)
        nodes.remove(next_node)

    return distance_graph


if __name__ == '__main__':
    # graph_list = [   [0, 2, 1, 4, 5, 1],
    #         [1, 0, 4, 2, 3, 4],
    #         [2, 1, 0, 1, 2, 4],
    #         [3, 5, 2, 0, 3, 3],
    #         [2, 4, 3, 4, 0, 1],
    #         [3, 4, 7, 3, 1, 0]]

    graph_dict = {"s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4, "s5": 3},
                  "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
                  "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1, "s5": 4},
                  "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 1},
                  "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
                  }

    # distance, path = dijkstra(graph_list, 2)
    # print distance, '\n', path
    distance = dijkstra(graph_dict, 's1')
    print(distance, '\n')
