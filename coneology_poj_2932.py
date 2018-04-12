## coneology poj 2932
#平面扫描
inpt=iter([
'5',
'1 0 -2',
'3 0 3',
'10 0 0',
'1 0 1.5',
'10 50 50'
    ])
N=int(next(inpt))
y_bounds=dict()
points=[]
for i in range(1,N+1):
    r,p1,p2=tuple(map(float,next(inpt).split()))
    points.append((p1-r,i))
    points.append((p1+r,i))
    y_bounds[i]=((p2-r,p2+r))
points.sort() 
res=[]
not_res=set()
scan=set()
#print (points)
#print (y_bounds)

def is_inside(i,circle):
    return y_bounds[circle][0]<y_bounds[i][0] and y_bounds[circle][1]>y_bounds[i][1]
for x,i in points:
    #print (scan, res, not_res)
    if i in not_res: continue 
    if i in scan: # at the right point of circle i
        scan.remove(i)
    elif len(scan)>0 and any(is_inside(i,circle) for circle in scan):
        not_res.add(i)
    else: 
        scan.add(i)
        res.append(i)
print (res)