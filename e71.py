def is_relatively_prime(x,y):
	"""docstring for totient"""
	if x%y==0:
		return 1!=1
	else :
		return (2*sum([i*y/x for i in range(1,x)]) + x + y - x*y)==1

max = 3.0/8.0
_37 = 3.0/7.0

ll = range(1,1000001)
ll.reverse()
for m in ll:
	n = 3*m/7
	curr = 1.0*n/m
	if _37 > curr > max and is_relatively_prime(m,n):
		max = curr
		print str(n)+"/"+str(m)
