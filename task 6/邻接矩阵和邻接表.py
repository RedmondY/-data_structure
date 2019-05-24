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

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (vertex, neighbour) not in edges:
                    edges.append((vertex, neighbour))
        return edges

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


# 邻接矩阵
class Graph(object):
    def __init__(self, graph_matrix=None, vertices=None):
        assert graph_matrix or vertices

        if not graph_matrix:
            graph_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
            for vertex in range(vertices):
                graph_matrix[vertex][vertex] = 1
        self.__graph_matrix = graph_matrix

    def vertices(self):
        return list(i for i in range(len(self.__graph_matrix)))

    def edges(self):
        return self.__generate_edges()

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)

        self.__graph_matrix[vertex1][vertex2] = 1

    def __generate_edges(self):
        edges = []
        vertices = len(self.__graph_matrix)
        for vertex in range(vertices):
            for neighbour in range(vertices):
                if vertex != neighbour and self.__graph_matrix[vertex][neighbour] == 1 and (
                        vertex, neighbour) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def __str__(self):
        res = "vertices: "
        vertices = len(self.__graph_matrix)
        for vertex in range(vertices):
            res += str(vertex) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == '__main__':
    g = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    graph = Graph(g)
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Vertices of graph:")
    print(graph.vertices())

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge (1, 2) with new vertices:')
    graph.add_edge((1, 2))
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
