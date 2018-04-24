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

def polygon_area(points):
    # points are ccw sorted 
    ret=0
    for i in range(len(points)):
        j=(i+1)%len(points)
        ret+=points[i].cross(points[j])
    return fabs(ret)/2.0

clip_p=[(26, 34), (76, 34), (76, 72), (26, 72)]
subject_p=[(41, 52),
 (50, 71),
 (42, 87),
 (26, 84),
 (16, 58),
 (33, 33),
 (51, 23),
 (64, 32),
 (73, 17),
 (86, 14),
 (91, 38),
 (92, 68),
 (82, 79),
 (68, 45),
 (61, 58)]
clip_p=[Vec(a,b) for a,b in clip_p]
subject_p=[Vec(a,b) for a,b in subject_p]
clipped_polygon=sutherland_hodgman(clip_p,subject_p)
result=polygon_area(clipped_polygon)