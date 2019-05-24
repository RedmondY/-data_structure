# 邻接表
class Graph(object):
    def __init__(self, graph_dict=None):
        if not graph_dict:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
        if vertex2 not in self.__graph_dict:
            self.__graph_dict[vertex2] = []

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (vertex, neighbour) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def depth_first_search(self, root=None):
        order = []
        visited = []

        def dfs(node):
            order.append(node)
            visited.append(node)
            for neighbour in self.__graph_dict[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        if root:
            dfs(root)
        for node in self.vertices():
            if node not in visited:
                dfs(node)
        return order

    def breadth_first_search(self, root=None):
        queue = []
        order = []
        visited = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)
                visited.append(node)
                for neighbor in self.__graph_dict[node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        order.append(neighbor)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.vertices():
            if node not in visited:
                queue.append(node)
                order.append(node)
                bfs()

        return order

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == '__main__':
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("Add an edge:")
    graph.add_edge({"a", "z"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge ("x","y") with new vertices:')
    graph.add_edge(("x", "y"))
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

    print(graph.depth_first_search("a"))
    print(graph.breadth_first_search("a"))
