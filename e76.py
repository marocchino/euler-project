d = {}
def part(n):
	sum = 0
	for k in range(1,n/2+1):
		sum += p(k,n-k)
	return sum
def p(k,n):
	global d
	try:
		return d["%i:%i"%(k,n)]
	except:
		if(k>n):
			d["%i:%i"%(k,n)] = 0
			return 0
		elif(k==n):
			d["%i:%i"%(k,n)] = 1
			return 1
		else:
			d["%i:%i"%(k,n)] = p(k+1,n) + p(k,n-k)
			return d["%i:%i"%(k,n)]
print part(100)
#print d