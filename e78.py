d = {}
def drop(n):
	return n%1000000
def part(n):
	sum = 1
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
			d["%i:%i"%(k,n)] = drop(p(k+1,n) + p(k,n-k))
			return d["%i:%i"%(k,n)]
n = 4
while part(n) != 0:
	n+=5
print n
#print d

