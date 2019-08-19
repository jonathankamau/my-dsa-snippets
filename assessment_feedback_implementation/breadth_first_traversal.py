'''
Breadth First Traversal Implementation
'''

import pprint
from graph import graph

pp = pprint.PrettyPrinter(indent=2)


class BreadthFirstTraversal:
    """Breadth First Traversal class initialization."""

    def __init__(self):
        self.graph = graph

    def bfs(self, start_node_num):
        start_node = self.graph.find_node(start_node_num)
        self.graph._clear_visited()
        ret_list = [start_node.value]

        queue = [start_node]

        while queue:
            current_node = queue.pop(0)
            current_node.visited = True
            for edge in current_node.edges:
                if not edge.node_to.visited:
                    edge.node_to.visited = True
                    queue.append(edge.node_to)
                    ret_list.append(edge.node_to.value)

        return ret_list

    def bfs_names(self, start_node_num):
        """Return the results of bfs with numbers converted to names."""
        return [self.graph.node_names[num] for num in self.bfs(start_node_num)]


bfs_traversal = BreadthFirstTraversal()
print "Breadth First Traversal"
pp.pprint(bfs_traversal.bfs_names(2))
