class Node: 
    def __init__(self, key): 
        self.left_node = None
        self.right_node = None
        self.node_value = key 


def printPostorder(root): 
  
    if root: 
  
        printPostorder(root.left_node) 
  
        printPostorder(root.right_node) 
  
        print(root.node_value), 