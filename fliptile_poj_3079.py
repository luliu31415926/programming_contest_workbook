#fliptile poj 3079 

#第一排的action定了以后, 后面的动作是determined. 
#字典序枚举第一排 
#根据上下左右中的五个flip action 决定此处的颜色 
M=4
N=4
tile=['1 0 0 1','0 1 1 0','0 1 1 0','1 0 0 1']
tile=[ list(map(int,row.split())) for row in tile]

def get(x,y,flip):
    DIRS=[(0,1),(1,0),(0,-1),(-1,0),(0,0)]
    c=tile[x][y]
    for u,v in DIRS:
        if 0<=x+u<M and 0<=y+v<N:
            if flip[x+u][y+v]: c^=1 
    return c 

def solve_rest(row1):
    flip=[[0]*N for _ in range(M)]
    # perform row1 
    for i in range(N):
        flip[0][N-i-1]= row1>>i &1 

    for i in range(1,M):
        for j in range(N):
            if get(i-1,j,flip)==1:
                flip[i][j]=1
    for j in range(N):
        if get(M-1,j,flip)!=0: return None 
    return flip 

for row1 in range(1<<N):
    flip=solve_rest(row1)
    if flip is not None: 
        break  
if flip is None : print ('IMPOSSIBLE')
else: 
    for row in flip:
        print (' '.join(map(str,row)))

