# 最小生成树 无向图
def prim(graph, root):
    nodes = list(graph.keys())
    nodes.remove(root)

    visited = [root]
    path = []
    end = None
    while nodes:
        distance = float("inf")
        for s in visited:
            for d in graph[s]:
                if d in visited or d == s:
                    continue

                if graph[s][d] < distance:
                    distance = graph[s][d]
                    end = d
        path.append((s, end))
        visited.append(end)
        nodes.remove(end)
    return path


if __name__ == '__main__':
    # graph_dict = {"s1": {"s1": 0, "s2": 6, "s10": 3, "s12": 4, "s5": 3},
    #               "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 3, "s5": 4},
    #               "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
    #               "s12": {"s1": 1, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
    #               "s5": {"s1": 3, "s2": 5, "s10": 7, "s12": 4, "s5": 0},
    #               }
    #
    # path = prim(graph_dict, 's12')
    # print(path)
    pass