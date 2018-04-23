#### shortest path #### 
# single source # 
# bellman ford # 

class Edge:
	def __init__(self,fro,to,cost):
		self.fro=fro
		self.to=to
		self.cost=cost
edges=[]
def add_edge(fro,to,cost):
	edges.append(Edge(fro,to,cost))
 # vertices are 0~V-1 
def bellman_ford(source,V,edges):
	#O(VE)
	#shortest distances from source to each vertex after using x edges 
	dist=[float('inf')]*V  
	predecessor=[None]*V
	dist[source]=0
	#max V-1 times, if contain negative cycle, can still update at V-1 round  
	for i in range(V):  
		update=False 
		for e in edges:
			if dist[e.to]>dist[e.fro]+e.cost:
				dist[e.to]=dist[e.fro]+e.cost
				update=True 
				predecessor[e.to]=e.fro
				if i==V-1: 
					# contains negative cycle 
					return None 
		if not update: break 
	return dist,predecessor
def path(source,u,predecessor):
	if predecessor[u] is None: return [] 
	path=[]
	while u!=source:
		path.append(u)
		u=predecessor[u]
	path.append(source)
	return path[::-1]

# dijkstra # 
# O(ElogV)
import heapq
class Edge:
	def __init__(self,fro,to,cost):
		self.fro=fro
		self.to=to
		self.cost=cost 
class Dijkstra:
	def __init__(self,V):
		self.V=V
		self.edge_dict=collections.defaultdict(list)
	def add_edge(self,fro,to,cost):
		self.edge_dict[fro].append(Edge(fro,to,cost))
	def dijkstra(self,source):
		dist=[-1]*V
		dist[source]=0
		predecessor=[None]*V
		visited=[False]*V
		visited[source]=True
		heap=[]
		for e in self.edge_dict[source]:
			heapq.heappush(heap,(e.cost,e.fro,e.to))
		while heap:
			cost,fro,to=heapq.heappop(heap)
			dist[to]=dist[fro]+cost 
			predecessor[to]=fro 
			for e in self.edge_dict[to]:
				if not visited[e.to]:
					heapq.heappush(heap,(e.cost,e.fro,e.to))
			visited[to]=True 
		self.predecessor=predecessor
		self.dist=dist
		return dist, predecessor 
	def path(self,source,u):
		if self.predecessor[u] is None: return [] 
		path=[]
		while u!=source:
			path.append(u)
			u=self.predecessor[u]
		path.append(source)
		return path[::-1]

## multi source #### 
# floyd-warshall # 
# O(V**3) 
# Run dijkstra for every vertex O(VElogV) better than floyd warshall
# But dijkstra does not allow negative weighted edges
dp=[[float('inf')]*V for _ in range(V)]
nxt=[[None]*V for _ in range(V)]

def add_edge(u,v,cost):
	dp[u][v]=cost 
	nxt[u][v]=v
def warshall_floyd(dp,nxt,V):
	for k in range(V):
		for i in range(V):
			for j in range(V):
				if dp[i][k]+dp[k][j]<dp[i][j]:
					dp[i][j]=dp[i][k]+dp[k][j]
					nxt[i][j]=nxt[i][k]
				if i==j and dp[i][j]<0:
					#contain negative cycle  
					return None

	return dp,nxt
def path(u,v,nxt):
	if nxt[u][v]==None: return []
	path=[u]
	while u!=v:
		u=nxt[u][v]
		path.append(u)
	return path 

##### Minimimum spanning tree #########
'''
UNIQUE: If each edge has a distinct weight then there will be only one, unique minimum spanning tree.
CUT: Any cut set 里面最小的edge 都属于MST
Contraction If T is a tree of MST edges, then we can contract T into a single vertex while maintaining the invariant that the MST of the contracted graph plus T gives the MST for the graph before contraction
'''
# prim # for dense graph
# O(ElogV)
import heapq
class Edge:
	def __init__(self,fro,to,cost):
		self.fro=fro
		self.to=to
		self.cost=cost 
edge_dict=collections.defaultdict(list)
def add_edge(fro,to,cost):
	edge_dict[fro].append(Edge(fro,to,cost))
def prim(V,edge_dict):
	visited=[False]*V
	MST=set()
	for i in range(V):
		if not visited[i]:
			source=i
			visited[source]=True 
			heap=[]
			for e in edge_dict[source]:
				heapq.heappush(heap,(e.cost,e.fro, e.to))
			while heap:
				cost,fro,to=heapq.heappop(heap)
				visited[to]=True 
				MST.add(Edge(fro,to,cost))
				for e in edge_dict[to]:
					if not visited[e.to]:
						heapq.heappush(heap,(e.cost,e.fro,e.to))
	return MST 

# kruskal: for sparse graph 
# O(ElogE)
class UF:
	def __init__(self,n):
		self.parent=[i for i in range(n)]
		self.rank=[0]*n
		self.cnt=n
	def find(self,x):
		p=self.parent[x]
		if p==x: return x
		else: self.parent[x]=self.find(p)
		return self.parent[x]
	def union(self,x,y):
		x=self.find(x)
		y=self.find(y)
		if x==y: return 
		if self.rank[x]<self.rank[y]:
			self.parent[x]=y
		else:
			self.parent[y]=x
			if self.rank[x]==self.rank[y]: self.rank[x]+=1 
		self.cnt-=1 
	def same(self,x,y):
		return self.find(x)==self.find(y)

class Edge:
	def __init__(self,fro,to,cost):
		self.fro=fro
		self.to=to
		self.cost=cost
edges=[]
def add_edge(fro,to,cost):
	edges.append(Edge(fro,to,cost))
def kruskal(edges,V):
	MST=set()
	edges.sort(key=lambda x:x.cost)
	uf=UF(V)
	for e in edges:
		if uf.same(e.fro,e.to): continue 
		else:
			uf.union(e.fro,e.to)
			MST.add(e)
	return kruskal 
	



