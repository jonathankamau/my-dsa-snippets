from data_structures import Graph


class BreadthFirstSearch:
    def __init__(self):
        self.graph = Graph()

    def BFS(self, s):
 
        visited = [False] * (len(self.graph))
 
        queue = []

        queue.append(s)
        visited[s] = True
 
        while queue:
 
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


bfs = BreadthFirstSearch()
print("Following is Breadth First Traversal (starting from vertex 2)")
bfs.BFS(2)
