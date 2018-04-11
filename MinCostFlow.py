class MinCostFlow:
    def __init__(self,V,edges,source,sink):
        self.graph=[[0]*(V) for _ in range(V)]
        self.source=source
        self.sink=sink
        self.edges=edges
        