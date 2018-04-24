# geometry functions 
from math import * 
EPS=0.00001

class Vec:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def times(self,r):
        return Vec(self.x*r,self.y*r)

    def norm(self):
        return hypot(self.x,self.y)
    def normalize(self):
        return Vec(self.x/self.norm(),self.y/self.norm())
    def polar_angle(self):
        # 从正x轴到vector的角度in radian [0,2*pi) 
        return fmod(atan2(self.y,self.x)+2*pi,2*pi)

    def equal(self,vec):
        return self.x==vec.x and self.y==vec.y
    def smaller_than(self,vec):
        # return True if self is smaller than vec  
        if self.x==vec.x: return self.y<vec.y
        else: return self.x<vec.x 
    def add(self,vec):
        return Vec(self.x+vec.x,self.y+vec.y)
    def sub(self,vec):
        return Vec(self.x-vec.x,self.y-vec.y)

    def dot(self,vec):
        #uvcos(theta)
        return self.x*vec.x+self.y*vec.y
    def cross(self,vec):
        #uvsin(theta)
        #平行四边形面积，取绝对值
        # theta= 从u ->v ccw rotate
        # if >0, vec is within 180 degree ccw 
        return self.x*vec.y-self.y*vec.x
    def project(self,vec):
        # project self onto vec 
        r=vec.normalize()
        return r.times(r.dot(self))
    def ccw(self,vec):
        #if vec is at ccw direction or not 
        return self.cross(vec)
    def show(self):
        print (self.x,self.y)
    def find_angle(self,vec):
        # return ccw angle self to vec 
        return acos(self.cross(vec)/self.norm()/vec.norm())

def ccw(a,b,c):
    # connecting a,b,c in sequence, return whether turn left 
    #if positive, turn left, if 0, straight or reverse , if neg, turn right
    return (b.sub(a)).cross(c.sub(b))

def line_intersection(a,b,c,d):
    # return intersection point of (a,b) and (c,d)
    # if paralell  return None
    x=None
    det=(b.sub(a)).cross(d.sub(c))
    if fabs(det)>EPS: 
        p=(c.sub(a)).cross(d.sub(c))/det
        x=a.add((b.sub(a)).times(p))
    return x
def in_bounding_rectangle(a,b,x):
    if a.smaller_than(b): b,a=a,b
    return a.equal(x) ||b.equal(x)||(a.smaller_than(x) and x.smaller_than(b))
def parallel_segments(a,b,c,d):
    if b.smaller_than(a): a,b=b,a
    if d.smaller_than(c): c,d=d,c
    # dont overlap 
    if ccw(a,b,c)!=0 || b.smaller_than(c) ||d.smaller_than(a): return None 
    if a.smaller_than(c): return c 
    else: return a 

def segment_intersection(a,b,c,d):
    #return point of intersection 
    x=line_intersection(a,b,c,d)
    if x is None: return parallel_segments(a,b,c,d)
    if in_bounding_rectangle(a,b,x) and in_bounding_rectangle(c,d,x): return x
    return None 


def if_segment_intersect(a,b,c,d):
    ab=ccw(a,b,c)*ccw(a,b,d)
    cd=ccw(c,d,a)*ccw(c,d,b)
    if (ab==0 and cd==0):
        if b.smaller_than(a): a,b=b,a
        if d.smaller_than(c): c,d=d,c
        return not(d.smaller_than(a) || b.smaller_than(c))
    return ab<=0 and cd<=0

def perpendicular_foot(p,a,b):
    return a.add((p.sub(a)).project(b.sub(a)))


def point_to_line(p,a,b):
    # calc distance from point p to segment a,b
    return (p.sub(perpendicular_foot(p,a,b))).norm()










#########polygon ######################

def polygon_area(points):
    # points are ccw sorted 
    ret=0
    for i in range(len(points)):
        j=(i+1)%len(points)
        ret+=points[i].cross(points[j])
    return fabs(ret)/2.0


def polygon_perimeter(points):
    # points are ccw sorted 
    ret=0
    for i in range(len(points)):
        j=(i+1)%len(points)
        ret+=(points[j].sub(points[i])).norm()
    return ret

def is_inside(q, p):
    # points are ccw sorted 
    # count how many times the ray starting from q, point horizontally right crosses the polygon
    crosses=0
    N=len(p)
    for i in range(N):
        j=(i+1)%N
        if (p[i].y>q.y)!=(p[j].y>q.y):
        # if the segment crosses the ray vertically
        # parallel doesnt count  
            # find the x coordinate of the crossing 
            atx=(p[j].x-p[i].x)*(q.y-p[i].y)/(p[j].y-p[i].y)+p[i].x
            if q.x<atX: crosses+=1 

    return crosses%2>0 
def polygon_intersect(p,q):
    n=len(p)
    m=len(q)
    for i in range(n):
        for j in range(m):
            if if_segment_intersect(p[i],p[(i+1)%n],q[j],q[(j+1)%m]):
                return True 
    if (is_inside(p[0],q) or is_inside(q[0],p)): return True 
    return False 
#########polygon clipping ##########
def ccw(a,b,c):
    # connecting a,b,c in sequence, return whether turn left 
    #if positive, turn left, if 0, straight or reverse , if neg, turn right
    return (b.sub(a)).cross(c.sub(b))
def line_intersection(a,b,c,d):
    # return intersection point of (a,b) and (c,d)
    # if paralell  return None
    x=None
    det=(b.sub(a)).cross(d.sub(c))
    if fabs(det)>EPS: 
        p=(c.sub(a)).cross(d.sub(c))/det
        x=a.add((b.sub(a)).times(p))
    return x
def cut_polygon(polygon,a,b):
    # use line a,b clip polygon, return left side polygon 
    N=len(polygon)
    ret=[]
    inside=[ccw(a,b,p)>=0 for p in polygon] #whether p is on the left of a,b 
    for i in range(N):
        j=(i+1)%N
        if inside[i]: ret.append(polygon[i])
        if inside[i]!=inside[j]: #if intersect, include the intersection point 
            intersect=line_intersection(polygon[i],polygon[j],a,b)
            assert intersect is not None
            ret.append(intersect)
    return ret 

def sutherland_hodgman(clip_p,subject_p):
    # use convex polygon clip_p to clip polygon subject_p
    # return a polygon 
    N=len(clip_p)
    ret=subject_p[:]
    for i in range(N):
        j=(i+1)%N
        ret= cut_polygon(ret,clip_p[i],clip_p[j])
    return ret 

######### integration using simpson formula ########
def simpson(func,a,b):
    return (b-a)/6*(func(a)+4*func((a+b)/2)+func(b))





############## convex hull ########################
def ccw(a,b,c):
    # positive if a-b-c turn left, negtive if turn right, zero if colinear 
    return (b.sub(a)).cross(c.sub(b))
def graham_scan(points):
    #O(nlogn)
    '''Graham scan to find upper and lower convex hulls of a set of 2d points.'''
    U = []
    L = []
    points.sort(key=lambda p: (p.x,p.y))
    for p in points:
        while len(U) > 1 and ccw(U[-2],U[-1],p) >= 0: U.pop()
        while len(L) > 1 and ccw(L[-2],L[-1],p) <= 0: L.pop()
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



def hulls(Points):
    '''Graham scan to find upper and lower convex hulls of a set of 2d points.'''
    U = []
    L = []
    Points.sort()
    for p in Points:
        while len(U) > 1 and ccw(U[-2],U[-1],p) >= 0: U.pop()
        while len(L) > 1 and ccw(L[-2],L[-1],p) <= 0: L.pop()
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
        elif (U[i+1].y-U[i].y)*(L[j].x-L[j-1].x) > \
                (L[j].y-L[j-1].y)*(U[i+1].x-U[i].x):
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
        dist = (p.sub(q)).norm()
        if dist > bestDist:
            bestDist = dist
            bestPair = (p,q)
    return bestPair,bestDist

# diameter([(0,0),(1,1),(0,1),(1,0),(1,3),(3,1),(2,2)])
# returns: ((0, 0), (3, 1))