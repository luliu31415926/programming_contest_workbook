class BIT:
    def __init__(self,nums):
        self.length=len(nums)
        self.tree=[0]*(self.length+1)
        for i in range(self.length):
            idx=i+1
            while idx<=self.length:
                self.tree[idx]+=nums[i]
                idx+=(idx&-idx)
    def add(self,i,val):
        idx=i+1
        while idx<=self.length:
            self.tree[idx]+=val
            idx+=(idx&-idx)
            
    def update(self,i,val):
        
        old_val=self.get_sum(i)-self.get_sum(i-1)
        idx=i+1
        while idx<=self.length:
            self.tree[idx]+=(val-old_val)
            idx+=(idx&-idx)
        
    def get_sum(self,i):
        res=0
        idx=i+1
        while idx>0:
            res+=self.tree[idx]
            idx-=(idx&-idx)
        return res


MOD = 10**9 + 7
 
class SegmentTree(object):

    def __init__(self, nums):
        self.N=1<<len(nums).bit_length()
        # use 1 to 2N-1 to store the tree 
        self.tree=[0]*(self.N<<1)
        self._build(nums)
    def _build(self,nums):
        for i, n in enumerate(nums):
            self.tree[i+self.N]=n 
        for i in range(self.N-1,0,-1):
            self.tree[i]=self.tree[i<<1]+self.tree[(i<<1)|1]
    def update(self, i, val):
        self.add(i, val-self.tree[i+self.N])
         
    def add(self,i,diff):
        cur=self.N+i
        while cur>0:
            self.tree[cur]+=diff
            cur>>=1  
    def sumRange(self, i, j):
        res=0
        l=i+self.N
        r=j+self.N
        while l<=r:
            if l&1: 
                res+=self.tree[l]
                l+=1
            if r&1==0: 
                res+=self.tree[r]
                r-=1
            l>>=1
            r>>=1 
        return res

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
    

 