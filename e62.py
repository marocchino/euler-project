def make_list(x):
	"""docstring for make_list"""
	list = str(x**3)
	return str(sorted([list[i] for i in range(0,len(list))]))
a = {}
x = 345
while 1==1:
	curr=make_list(x)
	#if(len(curr)==8):
	try:
		a[curr][1]+=1
		if(a[curr][1]==5):
			print a[curr][0]**3
			break
	except Exception, e:
		a[curr]=[x,1]
	x+=1