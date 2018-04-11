# dual core cpu poj 3469
# min cut , separate all vertices into two separate groups 
# let cut be the cost of execution 
from Dinic import Dinic
inpt=iter(['3 1',
'1 10',
'2 10',
'10 3',
'2 3 1000'])
N,M=tuple(map(int,next(inpt).split()))
dinic=Dinic(N+2)
source=0
sink=N+1
for i in range(1,N+1):
	a,b=tuple(map(int,next(inpt).split()))
	dinic.add_edge(source,i,a)
	dinic.add_edge(i,sink,b)
for _ in range(M):
	a,b,w=tuple(map(int,next(inpt).split()))
	dinic.add_edge(a,b,w)
	dinic.add_edge(b,a,w)
print (dinic.max_flow())

