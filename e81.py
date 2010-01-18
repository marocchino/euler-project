import urllib,math
d = urllib.urlopen("http://projecteuler.net/project/matrix.txt")
strs = d.read()[:-2]
d.close()
matrix = [[int(j) for j in i.split(',')] for i in strs.split('\r\n')]
end = len(matrix)-1
result = [[0 for j in range(0,end+1)] for i in range(0,end+1)]
def sum_matrix(i,j):
	global matrix,result
	if(result[i][j]>0):
		pass
	elif(i==0):
		result[i][j] = matrix[i][j] + sum_matrix(i,j-1)
	elif(j==0):
		result[i][j] = matrix[i][j] + sum_matrix(i-1,j)
	else:
		result[i][j] = matrix[i][j] + min(sum_matrix(i,j-1),sum_matrix(i-1,j))
	return result[i][j]

result[0][0]=matrix[0][0]
print sum_matrix(end,end)
