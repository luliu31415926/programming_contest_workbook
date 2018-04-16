# 区间第k个数 
A=[1,5,2,6,3,7,4]
queries=[(2,5,3),(4,4,1),(1,7,3)]

import bisect
class RangeTree:
    def __init__(self,nums):
        self.N=1<<len(nums).bit_length()
        # index 1 ~ 2N-1 store the tree 
        # root node is tree[1]
        self.tree=[[] for _ in range(self.N<<1)]
        self._build(nums)
    def _merge(self,l,r):   
        pl,pr=0,0
        ret=[]
        while pl<len(l) and pr<len(r):
            if l[pl]<=r[pr]:
                ret.append(l[pl])
                pl+=1 
            else:
                ret.append(r[pr])
                pr+=1 
        if pl!=len(l):
            ret+=l[pl:]
        else:
            ret+=r[pr:]
        return ret


    def _build(self,nums):
        for i, n in enumerate(nums):
            self.tree[i+self.N]=[n]
        for i in range(self.N-1,0,-1):
            self.tree[i]=self._merge(self.tree[i<<1],self.tree[(i<<1)|1])
    def query(self,i,j,v):
        # 区间[i,j]中<=v的个数
        cnt=0
        l=i+self.N
        r=j+self.N
        while l<=r:
            if l&1: 
                cnt+=bisect.bisect_right(self.tree[l],v)
                l+=1
            if r&1==0: 
                cnt+=bisect.bisect_right(self.tree[r],v)
                r-=1
            l>>=1
            r>>=1 
        return cnt

def solve(A,queries):
    rt=RangeTree(A)
    for i,j,k in queries:
        lb,ub=0,len(A)-1
        while ub-lb>1:
            mid=(ub-lb)//2
            x=rt.tree[1][mid]
            cnt=rt.query(i,j,x) #<=x 的个数
            if cnt>=k: ub=mid
            else:lb=mid 
        print (i,j,k,rt.tree[1][ub])


    