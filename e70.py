def factor(n):
	if n == 1: return [1]
	i = 2
	limit = n**0.5
	while i <= limit:
		if n % i == 0:
			ret = factor(n/i)
			if ret.count(i)==0:
				ret.append(i)
				
			return ret
		i += 1
	return [n]
def is_permutation(a,b):
	list_a = list(str(a))
	list_a.sort()
	list_b = list(str(b))
	list_b.sort()
	return list_b==list_a
min = 99.0
m = 1514419
fact = factor(m)
curr = m
for i in fact:
	curr = curr/i*(i-1)
print 1.0*m/curr

m = 8319823
fact = factor(m)
curr = m
for i in fact:
	curr = curr/i*(i-1)
print 1.0*m/curr
# 
# ll = range(1460203,10000000)
# ll.reverse()
# for m in ll:
# 	fact = factor(m)
# 	curr = m
# 	for i in fact:
# 		curr = curr/i*(i-1)
	# if(is_permutation(curr,m)):
	# 	if min > 1.0*m/curr:
	# 		print m
	# 		min = 1.0*m/curr
	# 		print min
