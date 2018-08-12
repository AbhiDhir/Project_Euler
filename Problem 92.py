answer = 0;
def sum(a):
	ans = 0;
	for i in range(len(str(a))):
		ans += int(str(a)[i])**2
	return ans;
def recurse(a):
	if(a==1):
		return False
	if(a==89):
		return True
	return recurse(sum(a))
for x in range(1,10000000):
	if(recurse(x)):
		answer+=1
print answer