x = 3;
sum = 0;
while(x<1000):
    if(x%3==0):
        sum+=x;
    elif(x%5==0):
        sum+=x;
    x+=1;
print ("Problem 1: " + str(sum));
