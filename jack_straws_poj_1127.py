# jack straws poj 1127 
inpt=iter([
'7',
'1 6 3 3 ',
'4 6 4 9 ',
'4 5 6 7 ',
'1 4 3 5 ',
'3 5 5 5 ',
'5 2 6 3 ',
'5 4 7 2' ,
'1 4 ',
'1 6 ',
'3 3 ',
'6 7 ',
'2 3 ',
'1 3 ',
'0 0'
])

# geometry functions 
import numpy as np

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

# geometry functions 
import numpy as np
eps=0.000001


def on_seg(p1,p2,q):
    # whether point q is on segment p1-p2 (including pint p1 and p2 )
    p1,p2,q=tuple(map(np.array,(p1,p2,q)))
    return abs(np.cross(p1-q,p2-q)-0)<eps and np.dot(p1-q,p2-q)<=0

def intersection(p1,p2,q1,q2):
    # calculate the intersection point of segment p1-p2 and q1-q2 
    p1,p2,q1,q2=tuple(map(np.array,(p1,p2,q1,q2)))
    if np.cross(q2-q1,p2-p1)==0: 
        # parallel lines 
        return None 
    return np.cross(q2-q1,q1-p1)/np.cross(q2-q1,p2-p1)*(p2-p1)+p1
def is_connected(p1,p2,q1,q2):
    inter=intersection(p1,p2,q1,q2)
    if inter is None: return False 
    else:
        return on_seg(p1,p2,inter) and on_seg(q1,q2,inter)


N=int(next(inpt))
uf=UF(N+1)
lines=[0]
for i in range(1,N+1):
    x1,y1,x2,y2=tuple(map(int,next(inpt).split()))
    for j in range(1,i):
        q1,q2=lines[j]
        if is_connected((x1,y1),(x2,y2),q1,q2):
            uf.union(j,i)
    lines.append(((x1,y1),(x2,y2)))
while 1:
    u,v=tuple(map(int,next(inpt).split()))
    if u==v==0: break 
    if uf.same(u,v):
        print ('CONNECTED')
    else:
        print ('NOT CONNECTED')