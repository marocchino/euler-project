import math
def find(k):
	return math.sqrt(1+8*k*(k-1))%1!=0

def find_(k):
	return math.sqrt(1+8*k*(k-1))


k = int(math.sqrt(1000000000000**2/2))
print k
while find(k):
	k += 1
print k
print type(find_(85))
print math.sqrt(1000000000000**2)