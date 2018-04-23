class Graph:
    def __init__(self,V):
        self.G=[[] for _ in range(V)]
        self.used=[False]*V
        self.match=[-1]*V
        self.V=V
    def add_edge(self,u,v):
        self.G[u].append(v)
        self.G[v].append(u)
    def dfs(self,v):
        self.used[v]=True
        for i in range(len(self.G[v])):
            u=self.G[v][i]
            w=self.match[u]
            if w<0 or (not self.used[w] and self.dfs(w)):
                self.match[v]=u
                self.match[u]=v
                return True
        return False
    def bipartite_matching(self):
        res=0
        for v in range(self.V):
            if self.match[v]<0:
                self.used=[False]*self.V
                if self.dfs(v):res+=1 
        return res 