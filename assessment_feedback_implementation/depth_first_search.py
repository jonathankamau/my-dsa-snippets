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