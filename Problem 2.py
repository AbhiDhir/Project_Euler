x = 1;
y = 1;
sum = 0;
while(x<4000000):
    if(x%2==0):
        sum+=x;
    temp = y;
    y = x;
    x += temp;
print ("Problem 2: " + str(sum));
