import math
n = 2
count = 9
while n < 100:
	x=2
	while n >= math.floor(n*math.log10(x))+1:
		if n == math.floor(n*math.log10(x))+1:
			count+=1
		x+=1	
	n+=1
print count
#len(str(x**n)):
#math.floor(n*math.log10(x))+1
#math.ceil(n*math.log10(x)):