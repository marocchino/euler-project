import urllib,copy
d = urllib.urlopen("http://projecteuler.net/project/poker.txt")
strs = d.read()[:-2]
d.close()
array = [i.split(' ') for i in strs.split('\r\n')]
card_value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
def hand(a):
	p1 = a[:5]
	p2 = a[5:]
	if count(p1) > count(p2):
		return True
	else:
		return False
def count(a):
	nums = [card_value[i] for i in [i[0] for i in a]]
	suits = [i[1] for i in a]
	nums.sort()
	suits.sort()
	point = []
	rank = [royalflush,straightflush,fourofakind,fullhouse,flush,straight,threeofakind,twopair,onepair,highcard]
	for r in rank:
		point += [r(nums,suits)]
	return point
def highcard(nums,suits):
	return max(nums)
def onepair(nums,suits):
	count = 0
	for i in range(1,len(nums)):
		if nums[i]==nums[i-1]:
			count+=1
			curr = nums[i]
	if count == 1:
		return curr
	else:
		return 0
def twopair(nums,suits):
	count = 0
	a = []
	for i in range(1,len(nums)):
		if nums[i]==nums[i-1]:
			count+=1
			a.append(nums[i])
	a.sort()
	if count == 2 and a[0]!=a[1]:
		return a[1],a[0]
	else:
		return 0,0
def threeofakind(nums,suits):
	count = 0
	a = []
	for i in range(1,len(nums)):
		if nums[i]==nums[i-1]:
			count+=1
			a.append(nums[i])
	a.sort()
	if count == 2 and a[0]==a[1]:
		return a[0]
	else:
		return 0
def straight(nums,suits):
	curr = nums[0]
	count = 0
	for i in nums[1:]:
		if curr + 1 == i:
			count += 1
		curr += 1
	if count==4:
		return nums[4]
	return 0
def flush(nums,suits):
	count = 0
	for i in range(1,len(suits)):
		if suits[i-1] == suits[i]:
			count +=1
	if count == 4:
		return 1
	else:
		return 0
def fullhouse(nums,suits):
	count = 0
	a = []
	for i in range(1,len(nums)):
		if nums[i]==nums[i-1]:
			count+=1
			a.append(nums[i])
	a.sort()
	if count == 3:
		if a[0]==a[1]!=a[2]:
			return a[0],a[2]
		elif a[0]!=a[1]==a[2]:
			return a[2],a[0]
	return 0,0
def fourofakind(nums,suits):
	count = 0
	a = []
	for i in range(1,len(nums)):
		if nums[i]==nums[i-1]:
			count+=1
			a.append(nums[i])
	a.sort()
	if count == 3 and a[0]==a[1]==a[2]:
		return a[0]
	else:
		return 0
def straightflush(nums,suits):
	if straight(nums,suits) > 0 and flush(nums,suits) > 0:
		return nums[4]
	else:
		return 0
def royalflush(nums,suits):
	if nums == [10,11,12,13,14] and flush(nums,suits) > 0:
		return nums[4]
	else:
		return 0
w1 = 0
for s in array:
	if hand(s):
		w1 += 1
print w1