import heapq
V=?
G=[[] for _ in range(V)]


class Edge:
    def __init__(self,to,cap,cost,rev):
        self.to=to
        self.cap=cap
        self.cost=cost
        self.rev=rev
        
def add_edge(fro,to,cap,cost):
    G[fro].append(Edge(to,cap,cost,len(G[to])))
    G[to].append(Edge(fro,0,-cost,len(G[fro])-1))
    
def min_cost_flow(s,t,f):
    prevv=[-1]*V
    preve=[-1]*V
    res=0
    h=[0]*V
    while f>0:
        heap=[]
        dist=[float('inf')]*V
        dist[s]=0
        heapq.heappush(heap,(0,s)) #(dist, vertex)
        while heap:
            d,v=heapq.heappop(heap)
            if dist[v]<d: continue 
            for i in range(len(G[v])):
                e=G[v][i]
                if e.cap>0 and dist[e.to]>dist[v]+e.cost+h[v]-h[e.to]:
                    dist[e.to]=dist[v]+e.cost+h[v]-h[e.to]
                    prevv[e.to]=v
                    preve[e.to]=i
                    heapq.heappush(heap,(dist[e.to],e.to))
        if dist[t]==float('inf'):
            return -1
        for v in range(V):
            h[v]+=dist[v]
        d=f
        v=t
        while v!=s:
            d=min(d,G[prevv[v]][preve[v]].cap)
            v=prevv[v]
        f-=d
        res+=d*h[t]
        v=t
        while v!=s:
            e=G[prevv[v]][preve[v]]
            e.cap-=d
            G[v][e.rev].cap+=d
            v=prevv[v]
    return res