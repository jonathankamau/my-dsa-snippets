from data_structures import Graph

class Dijsktra:
    def __init__(self):
        self.graph = Graph()

    def dijsktra(self):
    visited = {initial: 0}
    path = {}

    nodes = set(self.graph.nodes)

    while nodes: 
        min_node = None
        for node in nodes:
        if node in visited:
            if min_node is None:
            min_node = node
            elif visited[node] < visited[min_node]:
            min_node = node

        if min_node is None:
        break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
        weight = current_weight + graph.distance[(min_node, edge)]
        if edge not in visited or weight < visited[edge]:
            visited[edge] = weight
            path[edge] = min_node

        return visited, path


print()