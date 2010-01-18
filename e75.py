#def is_one_angle(n):
#	if n%2==0:
#		array = []
#		for a in range(3,n/3):
#			for b in range(a+1,(n-a+1)/2):
#			#c = n - a - b
#			#if a+b>c and a*a + b*b == c*c:
#				if (a*b)%n==0 and a*b/n==(a+b)-n/2:
#					array.append(True)
#					if len(array)>1:
#						return 0
#		return len(array)
#	else:
#		return 0
#count = 2209
##for i in range(12,1001):
#for i in range(20001,1500001):
#	count +=is_one_angle(i)
#	if i%1000==0:
#		print i,count
#print count
def gcd(a, b):
  if a < 0:  a = -a
  if b < 0:  b = -b
  if a == 0: return b
  if b == 0: return a
  while b != 0: 
    (a, b) = (b, a%b)
  return a
 
limit = 1500000
sqrt_limit = int(limit**.5)
counter = [0]*limit
for i in range(1, sqrt_limit+1, 2):
  for j in range(2, sqrt_limit+1, 2):
    if gcd(i, j) == 1: 
      sum = abs(j*j - i*i) + 2*i*j + i*i + j*j
      for s in range(sum, limit+1, sum):
        counter[s-1]+=1
 
print counter.count(1)


