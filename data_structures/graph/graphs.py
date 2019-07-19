from singly_linked_list import SinglyLinkedList
from edge import Edge
from node import Node

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencyList = {}
        self.initialize_graph()

    def initialize_graph(self):

        for vertex in self.vertices:
            self.adjacencyList[vertex] = SinglyLinkedList()

    def add_edge(self, start_vertex, end_vertex, weight=None):
        self.adjacencyList[start_vertex].prepend(Edge(end_vertex, weight))

    def get_adjacent_vertices(self, vertex):
        return self.adjacencyList[vertex]

    def getAdjacencyList(self):
        return self.adjacencyList


graph = Graph(['Nairobi', 'Thika', 'Machakos', 'Mombasa'])

graph.add_edge('Nairobi', 'Thika')
graph.add_edge('Nairobi', 'Machakos')
graph.add_edge('Nairobi', 'Mombasa')
graph.add_edge('Mombasa', 'Nairobi')
graph.add_edge('Machakos', 'Nairobi')

mylist = graph.getAdjacencyList()

for value in mylist:
    print(value)

    if mylist[value].getHead():
        node = mylist[value].getHead()

        while node:
            edge = node.getData()

            print(value + '=>' + edge.get_end_vertex())

            node = node.getNext()




