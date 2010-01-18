pow = [i*i for i in range(10)]
next = {}
def getNext(n):
	try:
		return next[n]
	except:
		global pow
		result = 0
		i=n
		while i > 0:
			curr = i%10
			result += pow[curr]
			i /= 10
		next[n] = result
		return result
count=0
for	i in range(1,10000001):
	while True:
		if i == 1:
			break
		elif i == 89:
			count+=1
			break
		i=getNext(i)
print count