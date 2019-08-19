'''
Depth First Search Implementation
'''
from graphs import graph
import pprint

pp = pprint.PrettyPrinter(indent=2)


def dfs_search(self, start_node_num, search_term):
    """Depth First Search Implementation."""
    start_node = graph.find_node(start_node_num)
    message = 'Search Item not found!'

    if graph.node_names[start_node.value] == search_term:
        start_node.visited = True
        message = 'Found the Search Item! ' + \
            graph.node_names[start_node.value]
    else:
        for edge in start_node.edges:
            if graph.node_names[edge.node_to.value] == search_term:
                message = 'Found the Search Item! ' + \
                    graph.node_names[edge.node_to.value]
                break
            elif not edge.node_to.visited:
                edge.node_to.visited = True
                graph.dfs_search(edge.node_to.value, search_term)

    return message


print "Depth First Search with search item"
graph._clear_visited()
pp.pprint(graph.dfs_search(2, 'Kigali'))
