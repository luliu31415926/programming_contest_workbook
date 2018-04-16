# traveling sales man
''' 
visited set of vertex S, currently at v
dp[S][v] 
shortest distance to get back to source after visiting all rest vertex 
dp[V][source]=0
for all u not in S: 
	dp[S][v]=min(dp[S][v],dp[S+{u}][u]+d(v,u))
'''