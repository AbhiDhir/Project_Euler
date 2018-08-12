import math
list = [False, False];
for x in range(2,2000000):
    list.append(True);
for y in range(2,int(math.sqrt(2000000)+1)):
    if (list[y]):
        j = int(y**2);
        while(j<2000000):
            list[j] = False;
            j += y;
sum = 0;
for z in range(2,2000000):
    if (list[z]):
        sum += z;
print ("Problem 10: " + str(sum));
