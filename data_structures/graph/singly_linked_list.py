from node import Node


class SinglyLinkedList:

    def __init__(self, node=None):
        self.head = node

    def prepend(self, data):
        node = Node(data)

        node.setNext(self.head)
        self.head = node

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current_node = self.head
        
        while current_node.getNext():
            current_node = current_node.getNext()
        
        current_node.setNext(node)
    
    def getHead(self):
        return self.head


singly_list = SinglyLinkedList(Node(1))

singly_list.append(2)
singly_list.append(3)
singly_list.append(4)
singly_list.append(5)
singly_list.prepend(0)

head = singly_list.getHead()

while head:
    print(head.getData())

    head = head.getNext()
