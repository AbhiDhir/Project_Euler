def digital_root_sum(n):
    return 1+((n-1)%9);
array = [0,0];
for i in range(2,1000):
    array.append(digital_root_sum(i));
    for j in range(2,i/2+1):
        if(i%j==0 and array[i/j] + array[j] > array[i]):
            array[i] = array[i/j] + array[j];
print sum(array);
