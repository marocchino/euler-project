p=[1] 
h={}
for n in range(1,10):
	p.append(p[n-1]*n)

def sum_of_factorial(n):
	global h,p
	try:
		return h[n]
	except Exception, e:
		sum = 0
		num = n
		while n!= 0:
			sum += p[n%10]
			n/=10
		h[num]=sum
		return sum
		
count = 0
for i in range(1,1000001):
	next = sum_of_factorial(i)
	array=[i]
	while array.count(next)==0:
		array.append(next)
		next = sum_of_factorial(next)
	if (len(array)==60):
		print "%i %i"%(i,len(array))
		count+=1
print count
