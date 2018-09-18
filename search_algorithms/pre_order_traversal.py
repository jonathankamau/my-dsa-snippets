class Node: 
    def __init__(self, key): 
        self.left_node = None
        self.right_node = None
        self.node_value = key 

def printPreorder(root): 
  
    if root: 

        print(root.node_value), 
  
        printPreorder(root.left_node) 
  
        printPreorder(root.right_node) 