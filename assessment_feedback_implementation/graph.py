"""Graph initialization."""


class Node(object):
    """Create a new node object."""

    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    """Create a new edge object."""

    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    """Create a new graph object."""

    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """
        The Nth name corresponds to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        """Insert a new node with value new_node_val."""
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        """Insert a new edge, creating new nodes if necessary."""
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def find_node(self, node_number):
        """Return the node with value node_number or None."""
        return self._node_map.get(node_number)

    def _clear_visited(self):
        """Set all visited nodes back to False."""
        for node in self.nodes:
            node.visited = False


graph = Graph()

graph.set_node_names(('Kisumu',
                      'Nakuru',
                      'Mombasa',
                      'Nairobi',
                      'Lagos',
                      'Kigali',
                      'Kampala'))

graph.insert_edge(51, 0, 1)
graph.insert_edge(51, 1, 0)
graph.insert_edge(9950, 0, 3)
graph.insert_edge(9950, 3, 0)
graph.insert_edge(10375, 0, 5)
graph.insert_edge(10375, 5, 0)
graph.insert_edge(9900, 1, 3)
graph.insert_edge(9900, 3, 1)
graph.insert_edge(9130, 1, 4)
graph.insert_edge(9130, 4, 1)
graph.insert_edge(9217, 2, 3)
graph.insert_edge(9217, 3, 2)
graph.insert_edge(932, 2, 4)
graph.insert_edge(932, 4, 2)
graph.insert_edge(9471, 2, 5)
graph.insert_edge(9471, 5, 2)
