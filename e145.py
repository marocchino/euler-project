def reverse(n):
	curr = n
	result = 0
	while curr > 0:
		result += curr%10
		result *= 10
		curr /= 10
	result /= 10
	return result
def entirely_odd(n):
	if n%2==0:
		return False
	curr = n
	while curr > 0:
		if curr%2==0:
			return False
		curr /= 10
	return True
count = 0
#for　i in range(1,10**9):
i = 1
while i < 1000000000:
	if i%10>0 and entirely_odd(i+reverse(i)):
		count+=1
	i+=1
print count