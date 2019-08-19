'''
Breadth First Search Implementation
'''
from graphs import graph
import pprint

pp = pprint.PrettyPrinter(indent=2)


def bfs(self, start_node_num, search_term):
    """Breadth First Search with queue data structure."""
    start_node = graph.find_node(start_node_num)

    queue = [start_node]
    message = 'Search Item not found!'

    while queue:
        current_node = queue.pop(0)
        current_node.visited = True
        if self.node_names[current_node.value] == search_term:
            message = 'Found the Search Item! ' + \
                graph.node_names[current_node.value]
        for edge in current_node.edges:
            if not edge.node_to.visited:
                edge.node_to.visited = True
                queue.append(edge.node_to)

        return message


print "Depth First Search with search item"
graph._clear_visited()

