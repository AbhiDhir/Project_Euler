import math         
list = [False, False];
primes = [];
for x in range(2,18): #originally (2,500)
    list.append(True);
for y in range(2,int(math.sqrt(18)+1)):
    if (list[y]):
        j = int(y**2);
        while(j<18):
            list[j] = False;
            j += y;
for z in range(2,18):
    if (list[z]):
        primes.append(z);
blank = [];
for z in range(0,len(primes)):
    blank.append(0);
table = [];
divisors = 1;
n = 0;
sum = 0;
while(divisors <= 500):
    for x in range(0,len(blank)):
        blank[x] = 0;
    n += 1;
    sum += n;
    divisors = 1;
    temp = sum;
    x = 0;
    while(x < len(primes) and primes[x]<=temp):
        if(temp%primes[x]==0):
            temp = temp/primes[x];
            blank[x]+=1;
            x = -1;
        x+=1;
    for x in range(0,len(blank)):
        divisors *= (blank[x] + 1);
print ("Problem 12: " + str(sum));