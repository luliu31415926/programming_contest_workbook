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