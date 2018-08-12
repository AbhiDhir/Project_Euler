dict = {str(x): float(x)/10 for x in range(2,10)};
dict['T'] = 1;
dict['J'] = 1.1;
dict['Q'] = 1.2;
dict['K'] = 1.3;
dict['A'] = 1.4;

def same_suit(arr):
    for i in range(len(arr)):
        if not(arr[0] == arr[i]):
            return False;
    return True;

def straight(arr):
    start = arr[0];
    for i in range(len(arr)):
        if not(float(i)/10+start==arr[i]):
            return False;
    return True;

def multiple(arr):
    answer = [];
    num = [float(x)/10 for x in range(0,15)];
    count = [0 for x in range(0,15)];
    for i in range(len(arr)):
        for x in range(len(num)):
            if num[x] == arr[i]:
                count[x] += 1;
    if 4 in count:
        answer.append(True);
    else:
        answer.append(False);
    if 3 in count:
        answer.append(True);
    else:
        answer.append(False);
    if count.count(2)==2:
        answer.append(True);
    else:
        answer.append(False);
    if 2 in count:
        answer.append(True);
    else:
        answer.append(False);
    return answer;

def calculate(arr):
    nums = [];
    suits = [];
    for i in range(0,5):
        nums.append(dict[arr[i][0]]);
        suits.append(arr[i][1]);
    nums.sort();
    if(nums[0]==1 and straight(nums) and same_suit(suits)):
        return 1000000000;
    elif(straight(nums) and same_suit(suits)):
        return 100000000*nums[4];
    elif(multiple(nums)[0]):
        return 10000000*nums[1];
    elif(multiple(nums)[1] and multiple(nums)[3]):
        return 1000000*nums[2];
    elif(same_suit(suits)):
        return 100000*nums[4]+10000*nums[3]+1000*nums[2]+100*nums[1]+10*nums[0];
    elif(straight(nums)):
        return 10000*nums[4];
    elif(multiple(nums)[1]):
        return 1000*nums[2];
    elif(multiple(nums)[2]):
        return 100*nums[3]+10*nums[1];
    elif(multiple(nums)[3]):
        index = 0;
        answer = 0;
        for i in range(len(nums)):
            if nums.count(nums[i])==2:
                index = i;
                break;
        mult = nums[index];
        answer+=mult;
        filter(lambda a: a != mult, nums);
        answer += .1*nums[2] + .01*nums[1] + .001*nums[2];
        return answer;
    else:
        return .1*nums[4]+.01*nums[3]+.001*nums[2]+.0001*nums[1]+.00001*nums[0];
    
file = open("p054_poker.txt");
wins = 0;
for i in range(0,1000):
    temp = file.readline().strip().split(" ");
    p1 = temp[0:5];
    p2 = temp[5:10];
    if(calculate(p1)>calculate(p2)):
        wins+=1;
print wins-3;