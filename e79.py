
def cutoff(x):
	"""docstring for cutoff"""
	if(len(x)>0 and x[0]==max_num):
		x=x[1:]
	return x
nums="""319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716""".split('\n')
result = ''
for i in range(1,10):
	max_count = -1
	max_num=''
	a= {}
	for x in nums:
		for i in range(0,len(x)):
			try:
				a[x[i]]+=-i
			except Exception, e:
				a[x[i]]=-i
	for x in a:
		if max_count < a[x]:
			max_count = a[x]
			max_num = x
	result += max_num
	#for x in nums:
	nums = map(cutoff,nums)
print result