# beauty contest poj 2187
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
points=[(0,5),(1,8),(3,4),(5,0),(6,2),(6,6),(8,3),(8,7)]
diameter(points)