arr1 = [1]
for n in range(2,101):
	sum = 0
	for k in range(0,n-1):
		sum+=(k+1)*arr1[k]
	arr1.append(sum%n)
print arr1

# a_6n = 3n
# a_6n+1 = 4n + 1
# a_6n+2 = 3n + 1
# a_6n+3 = n
# a_6n+4 = 6n + 3
# a_6n+5 = n

# arr2 = []
# n = 0
# while(6*n < 10**12+1):
# 	arr2.append(3*n)
# 	arr2.append(4*n+1)
# 	arr2.append(3*n+1)
# 	arr2.append(n)
# 	arr2.append(6*n+3)
# 	arr2.append(n)
# 	n+=1