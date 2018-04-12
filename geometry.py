# geometry functions 
 
######### integration using simpson formula ########
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
###############points and lines ########################

import numpy as np
eps=0.00001

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



############## convex hull ########################

def graham_scan(points):
    #O(nlogn)
    '''Graham scan to find upper and lower convex hulls of a set of 2d points.'''
    U = []
    L = []
    points.sort()
    for p in points:
        while len(U) > 1 and orientation(U[-2],U[-1],p) <= 0: U.pop()
        while len(L) > 1 and orientation(L[-2],L[-1],p) >= 0: L.pop()
        U.append(p)
        L.append(p)
    return U+L[1:-1][::-1]
########## rotating calipers ############# 
# convex hull (Graham scan by x-coordinate) and diameter of a set of points

# input representation: a point is a pair (x-coordinate,y-coordinate)
# the input to the hull and diameter problems is a list of points
# hulls() outputs two lists: the vertices of the upper and lower parts of the hull.
# If you want a single list, reverse the lower part and concatenate.

from __future__ import generators

def orientation(p,q,r):
    '''Return positive number if p-q-r are clockwise, neg if ccw, zero if colinear.'''
    return (q[1]-p[1])*(r[0]-p[0]) - (q[0]-p[0])*(r[1]-p[1])

def hulls(Points):
    '''Graham scan to find upper and lower convex hulls of a set of 2d points.'''
    U = []
    L = []
    Points.sort()
    for p in Points:
        while len(U) > 1 and orientation(U[-2],U[-1],p) <= 0: U.pop()
        while len(L) > 1 and orientation(L[-2],L[-1],p) >= 0: L.pop()
        U.append(p)
        L.append(p)
    return U,L

# U,L = hulls([(0,0),(1,1),(0,1),(1,0),(1,3),(3,1),(2,2)])
# returns
# U = [(0, 0), (0, 1), (1, 3), (3, 1)]
# L = [(0, 0), (1, 0), (3, 1)]

def rotatingCalipers(Points):
    '''Given a list of 2d points, finds all ways of sandwiching the points between
two parallel lines that touch one point each, and yields the sequence of pairs of
points touched by each pair of lines.'''
    U,L = hulls(Points)
    i = 0
    j = len(L) - 1
    while i < len(U) - 1 or j > 0:
        yield U[i],L[j]
        
        # if all the way through one of top or bottom, advance the other
        if i == len(U) - 1: j -= 1
        elif j == 0: i += 1
        
        # still points left on both lists, compare slopes of next hull edges
        elif (U[i+1][1]-U[i][1])*(L[j][0]-L[j-1][0]) > \
                (L[j][1]-L[j-1][1])*(U[i+1][0]-U[i][0]):
            i += 1
        else: j -= 1

# rotatingCalipers([(0,0),(1,1),(0,1),(1,0),(1,3),(3,1),(2,2)])
# yields:
# (0, 0) (3, 1)
# (0, 1) (3, 1)
# (1, 3) (3, 1)
# (1, 3) (1, 0)
# (1, 3) (0, 0)

def diameter(Points):
    '''Given a list of 2d points, returns the pair that's farthest apart.'''
    bestPair = None
    bestDist = 0
    def square(x): return x*x
    for p,q in rotatingCalipers(Points):
        dist = square(q[0]-p[0]) + square(q[1]-p[1])
        if dist > bestDist:
            bestDist = dist
            bestPair = (p,q)
    return bestPair,bestDist

# diameter([(0,0),(1,1),(0,1),(1,0),(1,3),(3,1),(2,2)])
# returns: ((0, 0), (3, 1))