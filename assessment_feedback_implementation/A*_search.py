'''
Breadth First Search Implementation
'''
import pprint
from graph import graph

pp = pprint.PrettyPrinter(indent=2)


class AStarSearch:

    def __init__(self):
        self.graph = graph

    def search_algorithm(self, start_node_num, end_node_num, search_term):
        start_node = self.graph.find_node(start_node_num)
        end_node = self.graph.find_node(end_node_num)

        open_list = []
        open_list.append(start_node)

        while open_list:
            current_node = start_node
            open_list.pop(0)
            current_node.visited = True

            if self.graph.node_names[current_node.value] == search_term:
                message = 'Found the Search Item! ' + \
                    self.graph.node_names[current_node.value]
                break
            else:
                for edge in current_node.edges:
                    if edge.node_to.visited == True:
                        continue
                    if edge.node_to.visited = False:
                        open_list.append(edge.node_to)
                    if edge.node_to.heuristic < edge.node_to.distance_from_start:
                        edge.node_to.distance_from_start = current_node.total_cost + edge.value
                        edge.node_to.heuristic = edge_value + end_node.total_cost
                        edge.node_to.total_cost = edge.node_to.distance_from_start + edge.node_to.heuristic

        return message
