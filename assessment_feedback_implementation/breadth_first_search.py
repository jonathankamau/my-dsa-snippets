def bfs(self, start_node_num, search_term):
        start_node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = [start_node.value]

        queue = [start_node]
        
        while queue:
            current_node = queue.pop(0)
            current_node.visited = True
            if self.node_names[current_node.value] == search_term:
                message = 'Found the Search Item! ' + self.node_names[current_node.value]
            for edge in current_node.edges:
                if not edge.node_to.visited:
                    edge.node_to.visited = True
                    queue.append(edge.node_to)
                    ret_list.append(edge.node_to.value)

        return ret_list