'''
取i位:  mask>>i &1 
赋值i位 : mask |1<<i 
delete 1 from ith: mask & ~(1<<i)
取最低位的1 ： mask & -mask    -x = ~x+1 
flip bit: ^1 
'''
# 枚举n bits 所有子集
for s in range(1<<n):


# 枚举sub of sup set 
sup=int('01101101',2)
def get_subsets(sup):
    sub=sup
    ret=[]
    while 1:
        sub=(sub-1)&sup
        ret.append(sub)
        # -1 & sup == sup 
        if sub==sup: break 
    return ret

# 枚举n bits 所有k 大小的子集
def get_subsets(n,k):
    #字典升序
    comb=(1<<k)-1 #smallest combo
    ret=[comb]
    while comb<1<<n:
        #最右边的1
        x=comb & -comb  
        #最低位的1开始的连续的1 将这区间变成0， 区间左侧的0变成1 
        y=comb+ x
        # 取得最右边连续的1 的区间
        z=comb & ~y 
        #区间右移直到减少一个1 (除上最低位的1)
        z=(z//x)>>1
        #与y合并
        comb=z|y
        ret.append(comb)
    return ret