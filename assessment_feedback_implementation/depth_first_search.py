'''
Depth First Search Implementation
'''
import pprint
from graph import graph

pp = pprint.PrettyPrinter(indent=2)


class DepthFirstSearch:
    """Depth First Search class initialization."""

    def __init__(self):
        self.graph = graph

    def dfs_search_with_stack(self, start_node_num, search_term):
        """Depth First Search Implementation (with stack data structure)."""
        start_node = self.graph.find_node(start_node_num)
        message = 'Search Item not found!'

        stack = [start_node]

        while stack:
            current_node = stack.pop()
            if self.graph.node_names[current_node.value] == search_term:
                message = 'Found the Search Item! ' + \
                    self.graph.node_names[current_node.value]
                break
            else:
                current_node.visited = True
                for edge in current_node.edges:
                    if not edge.node_to.visited:
                        edge.node_to.visited = True
                        stack.append(edge.node_to)
                    else:
                        message = 'Cannot find next node!'
       
        return message

    def dfs_search(self, start_node_num, search_term):
        """Depth First Search Implementation (recursive implementation)."""
        start_node = self.graph.find_node(start_node_num)
        message = 'Search Item not found!'
        # check if the search term is equal to the value of the start node
        # if not, mark the node as visited and move on to the next one.
        if self.graph.node_names[start_node.value] == search_term:
            message = 'Found the Search Item! ' + \
                self.graph.node_names[start_node.value]
        else:
            for edge in start_node.edges:
                if (self.graph.node_names[
                        edge.node_to.value] == search_term):
                    message = 'Found the Search Item! ' + \
                        self.graph.node_names[edge.node_to.value]
                    break
                elif not edge.node_to.visited:
                    edge.node_to.visited = True
                    self.dfs_search(edge.node_to.value, search_term)
                else:
                    message = 'Cannot find next node!'

        return message


dfs = DepthFirstSearch()
print "Depth First Search with search item (with stack)"
graph._clear_visited()
pp.pprint(dfs.dfs_search_with_stack(4, 'Mombasa'))

print "\nDepth First Search with search item (recursive implementation)"
graph._clear_visited()
pp.pprint(dfs.dfs_search(2, 'Lagos'))