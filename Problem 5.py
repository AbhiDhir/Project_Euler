def gcd(a, b):
    if (b == 0):
       return a; 
    else:
       return gcd(b, a%b);
def lcm(a, b):
    return (a*b)/gcd(a,b);
answer = 1;
for x in range(1,21):
    answer = lcm(answer,x);
print ("Problem 5: " + str(answer));
