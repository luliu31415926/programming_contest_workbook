# intersection of two prisms aoj 1313
# use simpson integration function 
inpt=iter([
'4 3',
'7 2',
'3 3',
'0 2',
'3 1',
'4 2',
'0 1',
'8 1'
    ])
m,n=tuple(map(int,next(inpt).split()))
def simpson(func,a,b):
    return (b-a)/6*(func(a)+4*func((a+b)/2)+func(b))

def width(points,x):
    #计算x 切过polygon的宽度
    # points are sorted ccw 
    lb=float('inf')
    ub=float('-inf')
    n=len(points)
    for i in range(n):
        x1,y1=points[i]
        x2,y2=points[(i+1)%n]
        if (x1-x)*(x2-x)<=0 and x1!=x2:
            y=y1+(y2-y1)*(x-x1)/(x2-x1)
            lb=min(lb,y)
            ub=max(ub,y)
    return max(0,ub-lb)

xs=[] # record every change of x 
z_polygon=[] 
for _ in range(m):
    point=tuple(map(int,next(inpt).split()))
    z_polygon.append(point)
    xs.append(point[0])
y_polygon=[]
for _ in range(n):
    point=tuple(map(int,next(inpt).split()))
    y_polygon.append(point)
    xs.append(point[0])

func=lambda x:width(z_polygon,x)*width(y_polygon,x)
xs.sort()
res=0
for i in range(len(xs)-1):
    a=xs[i]
    b=xs[i+1]
    res+=simpson(func,a,b)

print (res)
