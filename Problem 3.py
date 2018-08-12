a = 10086647;
x = 2;
while(x<a):
    if(a%x==0):
        a = a/x;
        x = 1;
    x+=1;
print ("Problem 3: " + str(a));
