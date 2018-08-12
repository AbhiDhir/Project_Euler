list = [False, False];
for x in range(2,105000): #originally (2,1000000)
    list.append(True);
for y in range(2,int(math.sqrt(105000)+1)):
    if (list[y]):
        j = int(y**2);
        while(j<105000):
            list[j] = False;
            j += y;
number = 0;
answer = 0;
for z in range(2,105000):
    if (list[z]):
        number += 1;
    if (number == 10001):
        answer = z;
        break;
print ("Problem 7: " + str(answer));
