_12 = 0.5
_13 = 1.0/3.0
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
count = 0
for m in range(1,12001):
	fact = factor(m)
	for n in range(m/3+1,m/2+1):
		curr = 1.0*n/m
		if _12 > curr > _13:
			flag = True
			for i in fact:
				if n%i==0:
					flag = False
			if flag:
				count+=1
				#print "%s/%s"%(n,m)
print count
