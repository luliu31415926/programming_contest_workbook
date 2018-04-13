# aggressive cows poj2456
import bisect
N= 5
C= 3
pos=[1,2,8,4,9]
pos.sort()
def check(d):
    print ('checking',d)
    cur=0
    for c in range(1,C):
        cur=bisect.bisect_left(pos,pos[cur]+d)
        if cur==N: return False 
    return True 

lb=0
ub=max(pos)-min(pos)+1
while ub-lb>1:
    mid=int((lb+ub)/2)
    if check(mid):
        print ('ok')
        lb=mid
    else: ub=mid
print (lb) 