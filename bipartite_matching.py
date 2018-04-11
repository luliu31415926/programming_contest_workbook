# bipartite matching 
G=[[] for _ in range(MAX_V)]
used=[False]*MAX_V
match=[-1]*MAX_V
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