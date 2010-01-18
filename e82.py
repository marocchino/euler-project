import urllib,math
d = urllib.urlopen("http://projecteuler.net/project/matrix.txt")
strs = d.read()[:-2]
d.close()
#matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]#
matrix = [[int(j) for j in i.split(',')] for i in strs.split('\r\n')]
end = len(matrix)-1
result = [[0 for j in range(0,end+1)] for i in range(0,end+1)]
print "--------------------"
# for i in matrix:
# 	print i

def sum_matrix(i,j):
	global matrix,result
	if(result[i][j]>0):
		pass
	elif(j==0):
		result[i][j] = matrix[i][j]
	else:
		min_sum = sum_matrix(i,j-1)
		for k in range(0,len(matrix)):
			curr = sum_matrix(k,j-1)
			if i > k :
				curr += sum([matrix[l][j] for l in range(k,i)])				
			elif k > i :
				curr += sum([matrix[l+1][j] for l in range(i,k)])
				#print [matrix[l+1][j] for l in range(i,k)],sum_matrix(k,j-1)
			else :
				curr = min_sum
			#print "i:",i,"j:","k:",k,curr
			if curr < min_sum:
				min_sum = curr
		result[i][j] = matrix[i][j] + min_sum
	return result[i][j] 

print min([sum_matrix(i,end) for i in range(0,end+1)])
