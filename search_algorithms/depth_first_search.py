from data_structures import Graph

class DepthFirstSearch:
    def __init__(self):
        self.graph = Graph()

    def DFSUtil(self,v,visited):
        visited[v]= True
        print(v),


        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)


    def DFS(self,v):
        print(self.graph)
        visited = [False]*(len(self.graph))


        self.DFSUtil(v,visited)
        print(self.graph)

dfs = DepthFirstSearch()
print("Following is DFS from (starting from vertex 2) ", dfs.DFS(2))