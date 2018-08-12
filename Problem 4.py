answer = 0;
for x in range(100,1000):
    for y in range(100,1000):
        if(str(x*y)==(str(x*y)[::-1])):
            if((x*y)>answer):
                answer = x*y;
print ("Problem 4: " + str(answer));
