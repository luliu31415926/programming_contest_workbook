# ASTEROID POJ 3041 
# 最小顶点覆盖： 每个边都至少与其中一个顶点相交 
# 二分图中 最小顶点覆盖数= 最大匹配数 
# after max flow, s 到不了的u +s 到的了的 v


# bipartite matching 

def add_edge(u,v):
    G[u].append(v)
    G[v].append(u)
def dfs(v):
    used[v]=True
    for i in range(len(G[v])):
        u=G[v][i]
        w=match[u]
        if w<0 or (not used[w] and dfs(w)):
            match[v]=u
            match[u]=v
            return True
    return False
def bipartite_matching():
    res=0
    for v in range(MAX_V):
        if match[v]<0:
            used=[False]*MAX_V
            if dfs(v):res+=1 
    return res 


N,K=tuple(map(int,input().split()))
MAX_V=2*N
G=[[] for _ in range(MAX_V)]
used=[False]*MAX_V
match=[-1]*MAX_V

for _ in range(K):
	u,v=tuple(map(int,input().split()))
	add_edge(u-1,N+v-1)
print ((bipartite_matching()))