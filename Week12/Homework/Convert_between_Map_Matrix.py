from graph import Graph  # import the Adjacency Map


class AdjacencyMatrix():
    # ------------------------- nested Vertex class -------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._element = x

        def element(self):
            """Return element associated with this vertex."""
            return self._element

        def __hash__(self):         # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

        def __repr__(self):
            return str(self._element)

        def __eq__(self, other):  # You may modify this to: return self is other
            return self._element == other._element

    # ------------------------- nested Edge class -------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return (self._origin, self._destination)

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin
            raise ValueError('v not incident to edge')

        def element(self):
            """Return element associated with this edge."""
            return self._element

        def __hash__(self):         # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

        def __repr__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

    def __init__(self):
        self._vertices = []
        self._table = []

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._table)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._vertices

    def edge_count(self):
        """Return the number of edges in the graph."""
        count = 0
        for each_row in self._table:
            for each_cell in each_row:
                if each_cell is not None:
                    count += 1
        return count

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()       # avoid double-reporting edges of undirected graph
        for each_row in self._table:
            for each_cell in each_row:
                if each_cell is not None:
                    result.add(each_cell)    # add edges to resulting set
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        return self._table[self._vertices.index(u)][self._vertices.index(v)]

    def degree(self, v):
        """Return number of (outgoing) edges incident to vertex v in the graph."""
        count = 0
        for each_cell in self._table[self._vertices.index(v)]:
            if each_cell is not None:
                count += 1
        return count

    def incident_edges(self, v, outgoing=True):
        """ Return all (outgoing) edges incident to vertex v in the graph."""
        if outgoing:
            for each_cell in self._table[self._vertices.index(v)]:
                if each_cell is not None:
                    yield each_cell
        else:
            for i in range(len(self._vertices)):
                if (self._table[i][self._vertices.index(v)]) is not None:
                    yield self._table[i][self._vertices.index(v)]

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self._vertices.append(v)
        self._table.append([])
        for i in range(len(self._vertices) - 1):    # each old row should get a new cell
            self._table[i].append(None)

        for i in range(len(self._vertices)):        # Fill new row with None
            self._table[-1].append(None)
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""

        if self.get_edge(u, v) is not None:
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._table[self._vertices.index(u)][self._vertices.index(v)] = e

    def __str__(self):
        result = []
        result.append("Vertices are:\n")
        result.append(str(self._vertices))
        result.append("\nTable looks like:\n")
        for each in self._table:
            result.append(str(each) + "\n")
        return "".join(result)


def convert_map_to_matrix(adj_map):
    ''' Given an Adjacency Map, convert it to equivalent Adjacency Matrix.
        @adj_map: class Graph, the code is given in recitation, adjacency map representation

        Feel free to modify/use private variables, since our classes does not have getters and setters.

        # Hint 1: To avoid type error, if you want to call insert_vertex/insert edge:
        # Avoid type error!
        # insert_vertex takes 1 vertex name
        # insert edge takes 1 vertex reference, 1 vertex reference, 1 auxiliary element.

        return: a new instance of class AdjacencyMatrix, that is virtually the same as @adj_map
    '''
    # Your code

    pass


def convert_matrix_to_map(adj_matrix):
    ''' Given an Adjacency Matrix, convert it to equivalent Adjacency Map.
        @adj_matrix: class AdjacencyMatrix, implemented in this file.

        Feel free to modify/use private variables, since our classes does not have getters and setters.

        # Super hint:
        Our textbook graph.py has checking, which means we have to pass in vertices that belong to this graph.
        Make sure when you insert edges, first two parameters are vertex references that belong to the Adjacency Map.
        Using vertex references that belong to the AdjacencyMatrix will fail.

        Use directed graph!

        return: a new instance of class Graph, that is virtually the same as @adj_matrix
    '''
    # Your code

    pass


def main():
    # ----------------- Demo code ----------------------
    matrix = AdjacencyMatrix()
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
    print("Original", matrix)

    # ----------------- Test code ----------------------

    a = Graph(True)    # Mark True so the graph is directed.
    va = a.insert_vertex("A")
    vb = a.insert_vertex("B")
    vc = a.insert_vertex("C")
    vd = a.insert_vertex("D")
    ve = a.insert_vertex("E")

    a.insert_edge(va, vb, ("b", 20))
    a.insert_edge(va, vd, ("a", 5))
    a.insert_edge(vd, va, ("a", 5))
    a.insert_edge(vb, vd, ("c", 12))
    a.insert_edge(vb, vc, ("d", 7))
    a.insert_edge(vd, vc, ("e", 11))
    a.insert_edge(vc, ve, ("f", 9))

    matrix2 = convert_map_to_matrix(a)
    print(matrix2)
    '''
    Vertices are:
    [A, B, C, D, E]
    Table looks like:
    [None, (A,B,('b', 20)), None, (A,D,('a', 5)), None]
    [None, None, (B,C,('d', 7)), (B,D,('c', 12)), None]
    [None, None, None, None, (C,E,('f', 9))]
    [(D,A,('a', 5)), None, (D,C,('e', 11)), None, None]
    [None, None, None, None, None]
    '''
    map2 = convert_matrix_to_map(matrix2)
    print(map2)
    '''
    {A: {D: (A,D,('a', 5)), B: (A,B,('b', 20))}, B: {C: (B,C,('d', 7)), D: (B,D,('c', 12))}, C: {E: (C,E,('f', 9))}, D: {C: (D,C,('e', 11)), A: (D,A,('a', 5))}, E: {}}
    {A: {D: (D,A,('a', 5))}, B: {A: (A,B,('b', 20))}, C: {B: (B,C,('d', 7)), D: (D,C,('e', 11))}, D: {A: (A,D,('a', 5)), B: (B,D,('c', 12))}, E: {C: (C,E,('f', 9))}}
    '''


main()
