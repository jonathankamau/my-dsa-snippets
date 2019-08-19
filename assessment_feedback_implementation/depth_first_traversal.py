'''
Depth First Traversal Implementation
'''

import pprint
from graph import graph

pp = pprint.PrettyPrinter(indent=2)


class DepthFirstTraversal:
    """Depth First Traversal class initialization."""

    def __init__(self):
        self.graph = graph

    def dfs_helper(self, start_node):
        """Recursive implementation of Depth First Traversal."""
        ret_list = [start_node.value]

        start_node.visited = True
        for edge in start_node.edges:
            if not edge.node_to.visited:
                edge.node_to.visited = True
                ret_list.extend(self.dfs_helper(edge.node_to))

        return ret_list

    def dfs(self, start_node_num):
        self.graph._clear_visited()
        start_node = self.graph.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self.graph.node_names[num] for num in self.dfs(start_node_num)]


dfs_traversal = DepthFirstTraversal()
print "Depth First Traversal"
pp.pprint(dfs_traversal.dfs_names(2))
