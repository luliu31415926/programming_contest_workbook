'''
S: set of tickets not used 
v: current vertex 
dp[S][v] ： 达到此状态最短的时间 
for ticket in S: 
	for u in neighbors[v]:
		dp[S-{ticket}][u]= min(dp[S][v]+d[v][u]/t[i])


'''