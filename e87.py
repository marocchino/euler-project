# fast prime number list generator using a sieve algorithm
def primes(n):
	""" returns a list of prime numbers from 2 to < n """
	if n < 2: return []
	if n == 2: return [2]
	# do only odd numbers starting at 3
	s = range(3, n, 2)
	# n**0.5 may be slightly faster than math.sqrt(n)
	mroot = n ** 0.5
	half = len(s)
	i = 0
	m = 3
	while m <= mroot:
		if s[i]:
			j = (m * m - 3)//2
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i + 1
		m = 2 * i + 3
	# make exception for 2
	return [2]+[x for x in s if x]
max_num = 50000000
num = int(max_num**0.5)
primeList = primes(num)
#print primeList
a = []
for i in primeList:
	if i**4 < max_num:
		for j in primeList:
			if i**4+j**3 < max_num:
				for k in primeList:
					curr = i**4+j**3+k**2
					if curr < max_num:
						a.append(curr)
					else: break			
			else: break
	else: break
a.sort()
count = 0
for i in range(1,len(a)):
	if a[i-1] == a[i]:
		count+=1
print len(a) - count