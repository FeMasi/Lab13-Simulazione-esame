import networkx as nx

from database.DAO import DAO
class Model:
    def __init__(self):
        self._listShapes = []
        self._listSightings = []
        self._listStates = []
        self._graph = nx.Graph()
        self._nodes = []
        self._edges = []

        self.loadSightings()
        self.loadShape()
        self.loadStates()

    def loadShape(self):
        self._listShapes = DAO.getAllShapes()


    def loadSightings(self):
        self._listSightings = DAO.getAllSightings()

    def loadStates(self):
        self._listStates = DAO.getAllStates()

    @property
    def listSightings(self):
        return self._listSightings

    @property
    def listShapes(self):
        return self._listShapes

    @property
    def listStates(self):
        return self._listStates

    def buildGraph(self, s, a):
        self._graph.clear()
        self._nodes.clear()
        self._edges.clear()
        print(a, s)
        for p in self.listStates:
            self._nodes.append(p)

        self._graph.add_nodes_from(self._nodes)
        self.idMap = {}
        for n in self._nodes:
            self.idMap[n.id] = n

        tempEdges = DAO.getAllWeightedNeigh(a, s)

        for e in tempEdges:
            self._edges.append((self.idMap[e[0]], self.idMap[e[1]], e[2]))

        self._graph.add_weighted_edges_from(self._edges)

    def get_sum_weight_per_node(self):
        pp = []
        for n in self._graph.nodes():
            sum_w = 0
            for e in self._graph.edges(n, data=True):
                sum_w += e[2]['weight']
            pp.append((n.name, sum_w))
        return pp



    def get_num_of_nodes(self):
        return self._graph.number_of_nodes()

    def get_num_of_edges(self):
        return self._graph.number_of_edges()