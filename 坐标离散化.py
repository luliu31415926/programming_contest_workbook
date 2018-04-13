import bisect 
def compress(xs,W):
    # return new coordinate and new width 
    # 0 indexed 
    coord_map=list({p for point in xs for p in point})
    coord_map.sort()
    l=len(coord_map)
    p=0
    while p<l-1:
        if coord_map[p+1]-coord_map[p]>1:
            coord_map.append(coord_map[p]+1)
        p+=1
    coord_map.sort()
    new_coord=[(bisect.bisect_left(coord_map,l),bisect.bisect_left(coord_map,r))  for l,r in xs]
    return new_coord,len(coord_map)

xs=[(0,5),(0,9),(3,3),(8,8),(9,9)]
ys=[(3,3),(7,7),(0,9),(0,4),(5,9)]
w=10
h=10
xs,w=compress(xs,w)
ys,h=compress(ys,h)


# 标注直线位置
grid=[[0]*w for _ in range(h)]
visited=[[False]*w for _ in range(h)]
for (x1,x2),(y1,y2) in zip(xs,ys):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            grid[y][x]=1


import collections 
# 区域个数
def bfs():
    DIRS=[(1,0),(0,1),(-1,0),(0,-1)]
    ans=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not visited[i][j]:
                #print ('visiting',i,j)
                ans+=1 
                #bfs(i,j)
                q=collections.deque()
                q.append((i,j))
                visited[i][j]=True 
                while q:
                    x,y=q.popleft()
                    for u,v in DIRS:
                        if 0<=x+u<h and 0<=y+v<w and grid[x+u][y+v]==0 and not visited[x+u][y+v]:
                            q.append((x+u,y+v))
                            visited[x+u][y+v]=True # if already in que, dont add again 
