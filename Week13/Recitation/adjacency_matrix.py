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

    def degree(self, v, outDegree=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges """
        degree = 0
        for i in self.edges():
            if outDegree is True:
                if i.endpoints()[1] is v:
                    degree += 1
            elif v in i.endpoints():
                degree += 1

    def incident_edges(self, v, outgoing=True):
        """ Return all (outgoing) edges incident to vertex v in the graph."""
        if outgoing:
            for each_cell in self._table[self._vertices.index(v)]:
                if each_cell is not None:
                    yield each_cell
        else:
            for i in range(len(self._vertices)):
                if (self._table[self._vertices.index(v)][i]) is not None:
                    yield self._table[self._vertices.index(v)][i]

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
