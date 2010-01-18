import re
_100 = range(2,100)
min = [8000000,0,0]
for n in _100:
	_k = range(2,n)
	for k in _k:
		curr = abs(n*k*(n+1)*(k+1)-8000000)
		if min[0] > curr:
			min = [curr,n,k]
print min[1]*min[2]


#def squre_root(a):
#	if a[0] >= a[1]:
#		return [a[0]-a[1],a[1]+10]
#	else:
#		return [a[0]*100,a[1]*10-45]
#
#count = 0
#for i in range(1,101):
#	curr = [5*i,5]
#	while len(str(curr[1])) < 104:
#		curr = squre_root(curr)
#	count += sum([int(c) for c in list(str(curr[1])[:100])])
#
#print count

