# def is_relatively_prime(x,y):
# 	"""docstring for totient"""
# 	if x%y==0:
# 		return 1!=1
# 	else :
# 		return (2*sum([i*y/x for i in range(1,x)]) + x + y - x*y)==1
# max = 1
# for i in range(2,1000001):
# 	curr = 1.0*i/len([1]+[j for j in range(2,i) if is_relatively_prime(i,j)])
# 	if curr > max :
# 		max = curr
# 		print str(i)+":"+str(max)

print 2*3*5*7*11*13*17