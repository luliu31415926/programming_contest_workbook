
#FordFulkerson O(max_flow * E)
import collections
 
# This class represents a directed graph using adjacency matrix representation
class Graph:
  
    def __init__(self,graph):
        self.graph = [row[:] for row in graph] # residual graph
        self.flow=[row[:] for row in graph]
        self.ROW = len(graph)
        self.max_flow=0
        
    def _DFS(self,u, t, f):
        '''Returns max path flow in residual graph. with upperbound f  '''
        if u==t: return f 
        self.visited[u]=True
        for v,cap in  enumerate(self.graph[u]):
            if not self.visited[v] and  cap>0:
                d=self._DFS(v,t,min(f,cap))
                if d>0:
                    self.graph[u][v]-=d 
                    self.graph[v][u]+=d
                    return d 
        return 0 
        
             
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        while 1 :
            self.visited=[False]*self.ROW 
            path_flow = self._DFS(source, sink, float("Inf"))
            if path_flow==0: 
                for i in range(self.ROW):
                    for j in range(self.ROW):
                        if self.flow[i][j]>0:
                            self.flow[i][j]=self.graph[j][i]
                return 
            self.max_flow+=path_flow 
