from enum import Enum

import dfs
from adjacency_matrix import AdjacencyMatrix
from arraystack import ArrayStack
from graph import Graph


class AdjacencyMatrixMissingDegree(AdjacencyMatrix):

    def degree(self, v, outDegree=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.

        If graph is directed, optional parameter used to count incoming edges """
        # Task 1
        degree = 0
        degree = 0
        for i in self.edges():
            if outDegree is True:
                if i.endpoints()[1] is v:
                    degree += 1
            elif v in i.endpoints():
                degree += 1


def recursive_dfs(g):
    """ Perform recursive DFS for entire graph.
        For simplicity, you can return a **list** of vertices only.
        Our textbook returns a **dictionary** of vertices & corresponding edge

        Define as many new functions as you like!

        @g: the graph ADT

        return: list of vertices. Their order should follow DFS property.
    """
    # Task 2
    pass


def iterative_DFS(g):
    """ Perform iterative DFS for entire graph.
        For simplicity, you can return a **list** of vertices only.
        Our textbook returns a **dictionary** of vertices & corresponding edge

        @g: the graph ADT

        return: list of vertices. Their order should follow DFS property.
    """
    # Task 3
    pass


class Color(Enum):
    Black = 1
    Red = 2


def two_colorable(g):
    """ returns True if graph g is two_colorable.
        returns False if graph g is not two_colorable.

        @g: the graph ADT

        return: True or False
    """

    # Task 4
    pass


def main():
    # --------------------------- Task 1 tests -------------------------------
    matrix = AdjacencyMatrixMissingDegree()
    va = matrix.insert_vertex("A")
    vb = matrix.insert_vertex("B")
    vc = matrix.insert_vertex("C")
    vd = matrix.insert_vertex("D")
    ve = matrix.insert_vertex("E")

    matrix.insert_edge(va, vb, 20)
    matrix.insert_edge(va, vd, 5)
    matrix.insert_edge(vd, va, 5)
    matrix.insert_edge(vb, vd, 12)
    matrix.insert_edge(vb, vc, 7)
    matrix.insert_edge(vd, vc, 11)
    matrix.insert_edge(vc, ve, 9)
    matrix.insert_edge(vb, va, 4)
    matrix.insert_edge(vb, ve, 6)
    print("Original", matrix)
    print("\n------------------------- Task 1 tests ------------------------")

    print("Outgoing degree for vertex B:", matrix.degree(
        vb, outDegree=True), "expected 4")
    print("Incoming degree for vertex B:", matrix.degree(
        vb, outDegree=False), "expected 1")

    # --------------------------- Task 2 tests -------------------------------
    g = Graph()  # Undirected
    va = g.insert_vertex("A")
    vb = g.insert_vertex("B")
    vc = g.insert_vertex("C")
    vd = g.insert_vertex("D")
    ve = g.insert_vertex("E")
    vf = g.insert_vertex("F")
    vg = g.insert_vertex("G")

    g.insert_edge(va, vc, "a")
    g.insert_edge(va, vd, "b")
    g.insert_edge(vc, vb, "d")
    g.insert_edge(vc, vd, "c")
    g.insert_edge(vc, ve, "e")
    g.insert_edge(ve, vf, "f")
    g.insert_edge(vb, vf, "j")
    g.insert_edge(vd, vg, "h")
    g.insert_edge(vg, vf, "g")

    print("\n------------------------- Task 2 tests ------------------------")
    print("Textbook's DFS result: ")
    print(dfs.DFS_complete(g))
    print("Your recursive DFS result: ")
    print(recursive_dfs(g))
    # --------------------------- Task 3 tests -------------------------------
    print("\n------------------------- Task 3 tests ------------------------")
    print("Your iterative DFS result: ")
    print(iterative_DFS(g))
    # --------------------------- Task 4 tests -------------------------------
    g = Graph()  # Undirected
    v0 = g.insert_vertex("0")
    v1 = g.insert_vertex("1")
    v2 = g.insert_vertex("2")
    v3 = g.insert_vertex("3")
    v4 = g.insert_vertex("4")
    v5 = g.insert_vertex("5")
    v6 = g.insert_vertex("6")
    v7 = g.insert_vertex("7")
    v8 = g.insert_vertex("8")
    g.insert_edge(v0, v3)
    g.insert_edge(v3, v4)
    g.insert_edge(v4, v5)
    g.insert_edge(v5, v2)
    g.insert_edge(v1, v2)
    g.insert_edge(v6, v7)
    g.insert_edge(v4, v7)
    g.insert_edge(v7, v8)
    g.insert_edge(v5, v8)
    print("\n------------------------- Task 4 tests ------------------------")
    print("Is the graph two-colorable? Your result: ")
    print(two_colorable(g), "expected True")
    g.insert_edge(v1, v3)

    print("Is the graph two-colorable? Your result: ")
    print(two_colorable(g), "expected False")


main()
