import copy
l=range(51)
m=[]
for y in l:
	for x in l:
		m.append([x,y])
m.remove([0,0])
pow=dict([(x, x**2) for x in l])
count = 0
mod=copy.deepcopy(m)
for _1 in m:
	mod.remove(_1)
	for _2 in mod:
		triangle = [pow[_1[0]]+pow[_1[1]],pow[_2[0]]+pow[_2[1]],pow[abs(_2[0]-_1[0])]+pow[abs(_2[1]-_1[1])]]
		triangle.sort()
		if triangle[0]+triangle[1]==triangle[2]:
			count+=1
print count