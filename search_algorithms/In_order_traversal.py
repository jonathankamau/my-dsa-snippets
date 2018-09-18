class Node: 
    def __init__(self, key): 
        self.left_node = None
        self.right_node = None
        self.node_value = key 
  

def printInorder(root): 
    
    if root: 
  
        printInorder(root.left_node) 
  
        print(root.node_value), 
  
        printInorder(root.right_node) 
