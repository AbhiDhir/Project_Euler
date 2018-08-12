from random import randint
sum = 0;
for i in range(0,10000):
    array = [16];
    num = 0;
    for x in range(0,16):
        if(len(array)==1):
            num += 1;
        rand = randint(0,len(array)-1);
        if(not (array[rand] == 1)):        
            val = array[rand]/2;
            while(not (val == 1/2)):
                array.append(val);
                array.append(val);
                array.remove(val*2);
                val = val / 2;
            array.remove(1);
        else:
            del array[rand];
    num-=2;
    sum += num;
print float(sum)/10000;
