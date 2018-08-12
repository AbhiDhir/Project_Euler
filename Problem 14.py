def length(x):
    if (x==1):
        return 1;
    elif(x%2==0):
        return length(x/2) + 1;
    else:
        return length(3*x+1) + 1;
answer = 0;
num = 0;
for x in range(837700,840000): #originally (1,1000000)
    a = length(x);
    if (a>answer):
        answer = a;
        num = x;
print ("Problem 14: " + str(num));
