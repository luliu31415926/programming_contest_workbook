class BIT():
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



a=[3,1,4,2]
nums=[0]*(len(a)+1)
bit=BIT(nums)
res=0
for i,num in enumerate(a):
    #逆数组= 已scan过的数 -  所有比num小的已scan过的数 
    res+=(i-bit.get_sum(num-1))
    bit.update(num,1)

print (res)