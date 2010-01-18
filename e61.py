import math;
import copy;
def p3(n):
	return n*(n+1)/2

def p4(n):
	return n*n

def p5(n):
	return n*(3*n-1)/2

def p6(n):
	return n*(2*n-1)

def p7(n):
	return n*(5*n-3)/2

def p8(n):
	return n*(3*n-2)

	
def is_cyclic(a,b):
	return a%100==b/100

def make_pn_array(pn):
	n= 10
	while math.log10(pn(n)) < 3:
		n+=1
	a = []
	while 3 <= math.log10(pn(n)) < 4:
		a.append(pn(n))
		n+=1
	return a

def cyclic(r,a):
	if len(a)==0:
		if is_cyclic(r[-1],r[0]):
			print sum(r)
	else:
		for l in a:
			for n in l:
				if is_cyclic(r[-1],n):
					result = copy.deepcopy(r)
					array = copy.deepcopy(a)
					result.append(n)
					array.remove(l)
					cyclic(result,array)

a3 = make_pn_array(p3)
a4 = make_pn_array(p4)
a5 = make_pn_array(p5)
a6 = make_pn_array(p6)
a7 = make_pn_array(p7)
a8 = make_pn_array(p8)

for i8 in a8:
	cyclic([i8],[a3,a4,a5,a6,a7])

