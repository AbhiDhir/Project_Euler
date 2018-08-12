file = open("p079_keylog.txt");
arr = [[],[],[],[],[],[],[],[],[],[]];
for i in range(0,50):
	a = file.readline()
	a = [int(a[0]),int(a[1]),int(a[2])]
	if(not a[1] in arr[a[0]]):
		arr[a[0]].append(a[1])
	if(not a[2] in arr[a[0]]):
		arr[a[0]].append(a[2])
	if(not a[2] in arr[a[1]]):
		arr[a[1]].append(a[2])
print arr;
#73162890