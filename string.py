### KMP####
def get_partial_match(S):
	n=len(S)
	pi=[0]*n
	begin=1
	matched=0
	while (begin+matched<n):
		if S[begin+matched]==S[matched]:
			matched+=1 
			pi[begin+matched-1]=matched
		else:
			if matched==0: begin+=1
			else:
				begin+=matched-pi[matched-1]
				matched=pi[matched-1]
	return pi 

