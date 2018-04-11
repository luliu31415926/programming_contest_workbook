#dining poj 3281
# convert to max flow 
# s=> (limit each food used once) food =>(foods cows like) cows => (only cows with matched food can flow over) cows => (match cows with drinks) drink=>( limit each drink use once) sink 


inpt=iter(['4 3 3','2 2 1 2 3 1','2 2 2 3 1 2','2 2 1 3 1 2','2 1 1 3 3'])
N,F,D=tuple(map(int,next(inpt).split()))
dinic=Dinic(2+F+D+N*2)
source=0
sink=1+F+D+N*2
for food in range(1,F+1):
    dinic.add_edge(source,food,1)
for drink in range(F+1,F+1+D):
    dinic.add_edge(drink,sink,1)
for i in range(1,N+1):
    dinic.add_edge(F+D+i,F+D+N+i,1)
for i in range(1,N+1):
    line=list(map(int,next(inpt).split()))
    f,d=line[:2]
    for food in line[2:2+f]:
        dinic.add_edge(food,F+D+i,1)
    for drink in line[-d:]:
        dinic.add_edge(F+D+N+i,drink+F,1)
max_flow=dinic.max_flow(source,sink)
print (max_flow)