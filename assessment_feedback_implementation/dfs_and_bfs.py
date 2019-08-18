class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

# You only need to change code with docs strings that have TODO.
# Specifically: Graph.dfs_helper and Graph.bfs
# New methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
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
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)
    
    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def dfs_helper(self, start_node):
        """
        """
        ret_list = [start_node.value]
        
        start_node.visited = True
        print(self.node_names[start_node.value])
        for edge in start_node.edges:
            if not edge.node_to.visited:
                edge.node_to.visited = True
                ret_list.extend(self.dfs_helper(edge.node_to))
                 
        return ret_list

    def dfs_search(self, start_node_num, search_term):
        
        start_node = self.find_node(start_node_num)
        
        message = 'Search Item not found!'
        
        if self.node_names[start_node.value] == search_term:
            start_node.visited = True
            message = 'Found the Search Item! ' + self.node_names[start_node.value]
        else:
            for edge in start_node.edges:
                if self.node_names[edge.node_to.value] == search_term:
                    message = 'Found the Search Item! ' + self.node_names[edge.node_to.value]
                    break
                elif not edge.node_to.visited:
                    edge.node_to.visited = True
                    self.dfs_search(edge.node_to.value, search_term)

        return message

    def dfs(self, start_node_num):
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self, start_node_num):
        start_node = self.find_node(start_node_num)
        self._clear_visited()
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
        return [self.node_names[num] for num in self.bfs(start_node_num)]


graph = Graph()

# You do not need to change anything below this line.
# You only need to implement Graph.dfs_helper and Graph.bfs

graph.set_node_names(('Mountain View',
                      'San Francisco',
                      'London',       
                      'Shanghai',     
                      'Berlin',       
                      'Sao Paolo',    
                      'Bangalore'))    

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


import pprint
pp = pprint.PrettyPrinter(indent=2)

# print "Edge List"
# pp.pprint(graph.get_edge_list_names())

# print "\nAdjacency List"
# pp.pprint(graph.get_adjacency_list_names())

# print "\nAdjacency Matrix"
# pp.pprint(graph.get_adjacency_matrix())

# print "\nDepth First Search"
pp.pprint(graph.dfs_names(2))

# print "\nDepth First Search with search item"
graph._clear_visited()
pp.pprint(graph.dfs_search(2, 'Berlin'))

# Should print:
# Depth First Search
# ['London', 'Shanghai', 'Mountain View', 'San Francisco', 'Berlin', 'Sao Paolo']

print "\nBreadth First Search"
pp.pprint(graph.bfs_names(2))
# test error reporting
# pp.pprint(['Sao Paolo', 'Mountain View', 'San Francisco', 'London', 'Shanghai', 'Berlin'])

# Should print:
# Breadth First Search
# ['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco']