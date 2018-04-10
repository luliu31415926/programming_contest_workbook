# http://acm.sgu.ru/problem.php?contest=0&problem=194
# 194. Reactor Cooling
# find max circulation ( no source no sink), with both upper and lower limit on edge 
from Dinic import Graph

V,E=tuple(map(int,input().split()))
# index V and V+1 reserved for virtual source and sink 
res_graph=[[0]*(V+2) for _ in range(V+2)]
d=[0]*(V)
edges=[]
for _ in range(E):
    u,v,floor,ceil=tuple(map(int,input().split()))
    # convert to 0 indexed 
    edges.append((u-1,v-1,floor))
    res_graph[u-1][v-1]=ceil-floor 
    d[v-1]-=floor
    d[u-1]+=floor 
for i in range(V):
    if d[i]>0:#too much coming in, send extra to virtual sink
        res_graph[i][V+1]=d[i]
    elif d[i]<0:# too much going out, send extra into the vertex from virtual source
        res_graph[V][i]=-d[i]
g=Graph(res_graph)
g.Dinic(V,V+1)

    
if g.max_flow< sum(val for val in d if val>0):
    print ('No')
else:
    print ('Yes')
    for i in range(len(edges)):
        u,v,floor=edges[i]
        print (g.flow[u][v]+floor)


