inpt=iter(['5 5','XDXXX','X.X.D','XX.XX','D.X.X','XXXDX'])
import collections 
# Evacuation poj 3057 
R,C=tuple(map(int,next(inpt).split()))
people=[]
door=[]
graph=[]
for i in range(R):
    line=next(inpt)
    graph.append(line)
    for j,c in enumerate(line):
        if c=='D':
            door.append((i,j))
        if c=='.':
            people.append((i,j))
# give each person and door a vertex number            
v_hash=dict()
for i,p in enumerate(people):
    v_hash[p]=i
for i,d in enumerate(door):
    v_hash[d]=i+len(people)


dist=collections.defaultdict(list)

def bfs(dx,dy):
    visited=[[False]*C for _ in range(R)]
    t=0
    DIRS=[(0,1),(1,0),(0,-1),(-1,0)]
    q=collections.deque()
    q.append((dx,dy))
    while q:
        cur_x,cur_y=q.popleft()
        visited[cur_x][cur_y]=True
        t+=1
        for u,v  in DIRS:
            if 0<= cur_x+u<R and 0<=cur_y+v<C and \
            graph[cur_x+u][cur_y+v]=='.' and not visited[cur_x+u][cur_y+v]:
                q.append((cur_x+u,cur_y+v))
                dist[t].append((v_hash[dx,dy],v_hash[cur_x+u,cur_y+v]))
    return 

# find the distance of each person to each door 
for dx,dy in door:
    bfs(dx,dy)  


MAX_V=len(people)+len(door)

MAX_T=max(dist.keys())

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

t=1
res=0
while 1:
    #for every new second rematch newly escapable people with doors  
    G=[[] for _ in range(MAX_V)]
    match=[-1]*MAX_V
    for u,v in dist[t]:
        add_edge(u,v)
    for u,v in dist[t]:
        if match[u]<0:
            used=[False]*MAX_V
            if dfs(u):res+=1
        if match[v]<0:
            used=[False]*MAX_V
            if dfs(v):res+=1

    print (t,res)
    if res==len(people): 
        print (t)
        break
    if t==MAX_T:
        print ('impossible')
        break
    t+=1
        