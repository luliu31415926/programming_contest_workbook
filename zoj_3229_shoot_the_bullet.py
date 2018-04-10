from Dinic import Graph
# zoj 3229 shoot the bullet 
# http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3229
# max flow with source and sink  and lower and upper bound 
n,m=tuple(map(int,next(inpt).split()))
#n+m+2, n+m+3 reserved for meta source and meta sink 
V=n+m+2 #number of vertices 
source=0
sink=n+m+1
meta_source=n+m+2
meta_sink=n+m+3
graph=[[0]*(V+2) for _ in range(V+2)]
G=list(map(int,next(inpt).split()))
d=[0]*V
for i,g in enumerate(G):
    #girl to sink
    graph[n+1+i][sink]=float('inf')
    d[n+1+i]+=g
    d[sink]-=g
edges=[]
for day in range(1,n+1):
    C,D=tuple(map(int,next(inpt).split()))
    graph[source][day]=D
    for _ in range(C):
        girl,low,high=tuple(map(int,next(inpt).split()))
        edges.append((day,n+girl+1,low))
        graph[day][n+girl+1]=high-low
        d[n+girl+1]-=low 
        d[day]+=low 
for i in range(n+m+2):
    if d[i]>0:# send extra to meta sink
        graph[i][meta_sink]=d[i]
    elif d[i]<0:# send extra from meta source
        graph[meta_source][i]=-d[i]
graph[sink][source]=float('inf')
dinic=Graph(graph)
max_flow1=dinic.Dinic(meta_source,meta_sink)

if max_flow1<sum(val for val in d if val>0):
    print (-1)
else:
   
    dinic.graph[sink][source]=0
    dinic.graph[source][sink]=0
    #new_graph=[row[:V] for row in dinic.graph[:V] ]
    #dinic=Graph(new_graph)
    max_flow2=dinic.Dinic(source,sink)
    print (max_flow1+max_flow2)
    for u,v,low in edges:
        print (dinic.graph[v][u]+low)
        

