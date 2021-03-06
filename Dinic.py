
#Dinic O(EV**2)
import collections
 
# This class represents a directed graph using adjacency matrix representation
class Dinic:
  
    def __init__(self,V):
        self.graph = [[0]*V for _ in range(V)] # residual graph
        self.ROW = V
        self.level=[0]*self.ROW
        self.flows=dict()
    def add_edge(self,u,v,c):
        self.graph[u][v]=c
        self.flows[u,v]=0

    def _BFS(self,s, t):

        # Create a queue for BFS
        queue = collections.deque()
        self.level=[0]*self.ROW
        # Mark the source node as visited and enqueue it
        queue.append(s)
        self.level[s]=1
         
        # Standard BFS Loop
        while queue:
            u = queue.popleft()
         
            for ind, val in enumerate(self.graph[u]):
                if self.level[ind]==0 and val > 0 :
                    queue.append(ind)
                    self.level[ind] = self.level[u]+1
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return self.level[t]>0
    def _DFS(self,u,t,f):
        if u==t: return f 
        for i,cap  in enumerate(self.graph[u]):
            if self.level[i]==self.level[u]+1 and cap>0:
                d=self._DFS(i,t,min(f,cap))
                if d>0:
                    self.graph[u][i]-=d
                    self.graph[i][u]+=d
                    if (u,i) in self.flows:
                        self.flows[u,i]+=d
                   
                    return d 
        return 0 
             
    # Returns the maximum flow from s to t in the given graph
    def max_flow(self, source, sink):
 
        # This array is filled by BFS and to store path
        #flow_matrix = [[0]*self.ROW for _ in range(self.ROW)] 
 
        max_flow=0
        # Augment the flow while there is path from source to sink
        while self._BFS(source, sink) :
            max_flow+=self._DFS(source, sink, float('inf'))
        
        return max_flow
    