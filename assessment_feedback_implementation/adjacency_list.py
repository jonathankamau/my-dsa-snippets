"""Adjacency List implementation"""

from graph import graph


class AdjacencyList:
    def __init__(self):
        self.graph = graph

    def get_adjacency_list(self):
        """Create adjacency list."""
        max_index = self.find_index()
        adjacency_list = [None] * (max_index+1)
        for edge in self.graph.edges:
            if adjacency_list[edge.node_from.value]:
                adjacency_list[edge.node_from.value].append(
                    [(edge.node_to.value, edge.value)])
            else:
                adjacency_list[edge.node_from.value] = [
                    (edge.node_to.value, edge.value)]

        return adjacency_list

    def find_index(self):
        index = -1
        if len(self.graph.nodes):
            for node in self.graph.nodes:
                if node.value > index:
                    index = node.value

        return index


adjacency_list = AdjacencyList()
print adjacency_list.get_adjacency_list()
