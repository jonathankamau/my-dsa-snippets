class Edge:

    def __init__(self, end_vertex, weight=None):
        self.end_vertex = end_vertex
        self.weight = weight

    def get_end_vertex(self):
        return self.end_vertex
