import urllib
d = urllib.urlopen("http://projecteuler.net/project/roman.txt")
s = d.read()
b = s.split('\r\n')
s = s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
a = s.split('\r\n')
d = {}
d["I"] = 1
d["V"] = 5
d["X"] = 10
d["L"] = 50
d["C"] = 100
d["D"] = 500
d["M"] = 1000
d[0] = 0
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 2
d[5] = 1
d[6] = 2
d[7] = 3
d[8] = 4
d[9] = 2
def roman(s):
	curr = 0
	for i in s:
		curr += d[i]
	return curr/1000+d[curr%1000/100]+d[curr%100/10]+d[curr%10]
count = 0
print b
for i in b:
	count += len(i)
for i in a:
	count -= roman(i)
print count