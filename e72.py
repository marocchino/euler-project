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
for m in range(2,1000001):
	fact = factor(m)
	curr = m
	for i in fact:
		curr = curr/i*(i-1)
	count+= curr
print count