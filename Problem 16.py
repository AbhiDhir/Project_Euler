num = 2**1000;
def sum(n):
    answer = 0;
    while(n>0):
        answer += int(n%10);
        n = n/10;
    return answer;
print ("Problem 16: " + str(sum(num)));
