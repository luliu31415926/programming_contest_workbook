# flow problem with lower and upper bound 
from Dinic import Graph
class LowerUpper:
    def __init__(self,V,edges,source=None,sink=None):
        self.graph=[[0]*(V+2) for _ in range(V+2)]
        self.source=source
        self.sink=sink
        self.edges=edges
        self.meta_source=V
        self.meta_sink=V+1
        self.d=[0]*V
        for u,v,low,high in edges:
            self.graph[u][v]=high-low
            self.d[u]+=low
            self.d[v]-=low 
        for i,val in enumerate(self.d):
            if val>0: #too much coming in, send extra to virtual sink
                self.graph[i][self.meta_sink]=val
            elif val<0:
                self.graph[self.meta_source][i]=-val
        if source is not None:
            self.graph[sink][source]=float('inf')

    def find_feasible_flow(self):
        # find out if a flow is feasible to satisfy constraints
        # return dictionary of the feasible flow 
        self.dinic=Graph(self.graph)
        max_flow=self.dinic.Dinic(self.meta_source,self.meta_sink)
        if max_flow!=sum(val for val in self.d if val>0):
            return None 
        else:
            self.feas_flows=dict()
            for u,v,low,high in edges:
                self.feas_flows[u,v]=self.dinic.graph[v][u]+low 
            return self.feas_flows 
    def find_max_flow(self):
        #return max flow,
        #store flows of each edge in self.max_flows
        if self.source is None: 
            return None 
        else:
            self.dinic.graph[self.sink][self.source]=0
            self.dinic.graph[self.source][self.sink]=0
            max_flow=self.dinic.Dinic(self.source,self.sink)
            self.max_flows=dict()
            for u,v,low,high in edges:
                self.max_flows[u,v]=self.dinic.graph[v][u]+low 
            return max_flow 
    def find_min_flow(self):
        # return min flow 
        # store flows of each edge in self.min_flows
        if self.source is None: return None
        self.graph[self.sink][self.source]=0
        self.dinic=Graph(self.graph)
        max_flow=self.dinic.Dinic(self.meta_source,self.meta_sink)
        self.dinic.graph[self.sink][self.source]=float('inf')
        max_flow=self.dinic.Dinic(self.meta_source,self.meta_sink)
        if max_flow==sum(val for val in self.d if val>0):
            self.min_flows=dict()
            for u,v,low,high in edges:
                self.min_flows[u,v]=self.dinic.graph[v][u]+low 
            return self.dinic.graph[self.source][self.sink]
        else:
            return None