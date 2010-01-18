#print(str(28433*2**7830457+1)[-1:10])
result = 28433
for i in range(0,7830457):
	result = result*2%10000000000
result+=1
print result