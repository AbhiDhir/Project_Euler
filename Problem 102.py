import math

def polar(arr):
	x = float(arr[0]);
	y = float(arr[1]);
	if x>=0 and y>=0:
		return math.degrees(math.atan(y/x));
	elif x>=0 and y<=0: 
		return math.degrees(math.atan(y/x)) + 360;
	else:
		return math.degrees(math.atan(y/x)) + 180;

file = open("p102_triangles.txt");
total = 0;
for i in range(0,1000):
	temp = file.readline().strip().split(",");
	p1 = [temp[0],temp[1]]
	p2 = [temp[2],temp[3]]
	p3 = [temp[4],temp[5]]
	degrees = [(180+polar(p1))%360,(180+polar(p2))%360]
	degrees.sort();
	if((degrees[1]-degrees[0]<=(360-degrees[1])+degrees[0] and polar(p3)>degrees[0] and polar(p3)<degrees[1]) or (degrees[1]-degrees[0]>(360-degrees[1])+degrees[0] and (polar(p3)>degrees[1] or polar(p3)<degrees[0]))):
		total += 1;
print total;