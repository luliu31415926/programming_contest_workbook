def binary_search():
	#整数
	lb=
	ub=
	while ub-lb>1:
		mid=int((lb+ub)/2)
		if check(mid): lb=mid
		else ub=mid
	return lb 

	#float
	while ub-lb>eps:
		mid=(lb+ub)/2
		if check(mid): lb=mid
		else ub=mid
	return ub 
