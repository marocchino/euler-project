import urllib,math
d = urllib.urlopen("http://projecteuler.net/project/words.txt")
strs = d.read()
d.close()
array = strs[1:-1].split('","')
print len([[len(a),a] for a in array if len(a)>4])

# nums = []
# seed = 96
# 
# while 3 < 2*math.log10(seed) < 15:
# 	nums.append(seed ** 2) 
# 	seed += 1
# print len(nums)