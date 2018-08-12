list = [0 for x in range(0,5)];
list[0] = 1;
for x in range(1,len(list)-1):
	for y in range(x,len(list)):
		list[y] += list[y-x];
print list[100]-1;