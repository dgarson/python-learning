__author__ = 'dgarson'

class vertex:

    nextIdentity = 1;

    def __init__(self, graph):
        self.identity = vertex.nextIdentity;
        vertex.nextIdentity = vertex.nextIdentity + 1;
        self.graph = graph;
        self.connectedVerticies = [];

    def __add__(self, other):
        assert isinstance(other, vertex);
        if (other not in self.connectedVerticies):
            self.connectedVerticies.append(other)
            other.connectedVerticies.add(self)

    def __sub__(self, other):
        assert isinstance(other, vertex);
        if (other in self.connectedVerticies):
            self.connectedVerticies.remove(other)
            other.connectedVerticies.remove(self)

    def __contains__(self, item):
        return self.connectedVerticies.__contains__(item)


class edge:

    def __init__(self, v1, v2):
        self.v1 = v1;
        self.v2 = v2;

    def __eq__(self, other):
        return (self.v1 == other.v1 and self.v2 == other.v2) or (self.v1 == other.v2 and self.v2 == other.v1);

    def __contains__(self, item):
        return (self.v1 == item or self.v2 == item);

class graph:

    def __init__(self):
        self.vertices = [];
        self.edges = [];

    def __add__(self, other):
        assert isinstance(other, vertex);
        if (other not in self.vertices):
            self.vertices.append(other);
            self.addEdges(other);

    def addEdges(self, v):
        for cv in v.connectedVerticies:
            e = edge(v, cv);
            if (not e in self.edges):
                self.edges.append(e)
