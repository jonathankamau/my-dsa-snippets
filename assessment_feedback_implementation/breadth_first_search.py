'''
Breadth First Search Implementation
'''
import pprint
from graph import graph

pp = pprint.PrettyPrinter(indent=2)


class BreadthFirstSearch:
    """Breadth First Search class initialization."""

    def __init__(self):
        self.graph = graph

    def bfs_search(self, start_node_num, search_term):
        """Breadth First Search with queue data structure."""
        start_node = self.graph.find_node(start_node_num)

        queue = [start_node]
        message = 'Search Item not found!'

        while queue:
            current_node = queue.pop(0)
            current_node.visited = True
            if self.graph.node_names[current_node.value] == search_term:
                message = 'Found the Search Item! ' + \
                    self.graph.node_names[current_node.value]
            else:
                try:
                    for edge in current_node.edges:
                        if (self.graph.node_names[
                                edge.node_to.value] == search_term):
                            message = 'Found the Search Item! ' + \
                                self.graph.node_names[edge.node_to.value]
                            break
                        elif not edge.node_to.visited:
                            edge.node_to.visited = True
                            queue.append(edge.node_to)
                except Exception as error:
                    return error

            return message


bfs = BreadthFirstSearch()
print "Breadth First Search with search item"
graph._clear_visited()
pp.pprint(bfs.bfs_search(2, 'Mombasa'))
