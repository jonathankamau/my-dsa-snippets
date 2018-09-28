class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next_node

    def setNext(self, next_node):
        self.next_node = next_node


node = Node(1)

node.next_node = Node(2)

print(node.getData())
print(node.getNext().getData())
