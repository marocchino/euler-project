def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)-n+1):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
def contain(x,y,array):
	"""docstring for contain"""
	return (x in array[0] and y in array[1]) or (x in array[1] and y in array[0])
a=xuniqueCombinations(range(10),6)
dice = [i for i in a]
_2dice = xuniqueCombinations(dice,2)
count = 0
for i in [i for i in _2dice]:
	if contain(0,1,i) and contain(0,4,i) and (contain(0,9,i) or contain(0,6,i)) and (contain(1,9,i) or contain(1,6,i)) and contain(2,5,i) and (contain(3,9,i) or contain(3,6,i)) and (contain(4,9,i) or contain(4,6,i)) and contain(8,1,i):
		count +=1
print count