def squre_root(a):
	if a[0] >= a[1]:
		return [a[0]-a[1],a[1]+10]
	else:
		return [a[0]*100,a[1]*10-45]

count = 0
for i in range(1,101):
	if i**0.5%1!=0:
		curr = [5*i,5]
		while len(str(curr[1])) < 104:
			curr = squre_root(curr)
		count += sum([int(c) for c in list(str(curr[1])[:100])])

print count