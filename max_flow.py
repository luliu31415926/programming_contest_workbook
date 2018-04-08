
#EdmondsKarp O(VE**2)
#FordFulkerson O(max_flow * E)
import collections
 
# This class represents a directed graph using adjacency matrix representation
class Graph:
  
    def __init__(self,graph):
        self.graph = graph # residual graph
        self.ROW = len(graph)
  
    def _BFS(self,s, t, parent):

        '''Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path '''
        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)
        
        # Create a queue for BFS
        queue = collections.deque()
         
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
         
        # Standard BFS Loop
        while queue:
            u = queue.popleft()
         
            # Get all adjacent vertices's of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]
             
    # Returns the maximum flow from s to t in the given graph
    def EdmondsKarp(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self._BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s !=  source:
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v !=  source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow
        
    def _DFS(self,u, t, f):
        '''Returns path flow in residual graph. with upperbound f  '''
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
 
        max_flow = 0 # There is no flow initially
 
        while 1 :
            self.visited=[False]*self.ROW 
            path_flow = self._DFS(source, sink, float("Inf"))
            if path_flow==0: return max_flow
            max_flow+=path_flow 