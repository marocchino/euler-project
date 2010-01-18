import urllib,copy
d = urllib.urlopen("http://projecteuler.net/project/sudoku.txt")
strs = d.read()
d.close()
a = strs.split("\r\n")
array = []
for i in range(50):
	array.append([[int(i) for i in list(line)] for line in a[i*10+1:i*10+10]])

s = """003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300"""
sudoku = [[int(i) for i in list(line)] for line in s.split("\n")]
def cell(sudoku,y,x):
	_y = sudoku[y]
	_x = [i[x] for i in sudoku]
	_area = [] 
	for i in sudoku[y-y%3:y-y%3+3]:
		_area += i[x-x%3:+x-x%3+3]
	result = []
	for i in _y + _x + _area:
		if i > 0 and not i in result:
			result.append(i)
	if len(result) == 8:
		return 45 - sum(result)
	return 0
def doku(sudoku):
	for line in sudoku:
		print line
	while True:
		count = 0
		for	y in range(9):
			for	x in range(9):
				if sudoku[y][x]==0:
					count += 1
					sudoku[y][x] = cell(sudoku,y,x)
		if count == 0:
			break
		print "-"*27
		for line in sudoku:
			print line
	return sum(sudoku[0][0:3])
doku(array[1])
# count = 0
# for sudoku in array:
#  	count += doku(sudoku)
# print count