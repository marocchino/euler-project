sum = 0
def rec(k,n):
	global sum
	m = min(k,n)
	for x in [97,89,83,79, 73,71,67,61,59,53,47,43,41,37,31,29,23,19,17,13,11,7,5,3,2]:
		if x<=m:
			if k == x:
				sum += 1
			rec(k-x, min([n,x]))
n = 71
rec(n,n)
print(sum)
