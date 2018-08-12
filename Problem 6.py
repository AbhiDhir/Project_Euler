x = int(((100*101)/2)**2);
y = 0;
for i in range(1,101):
    y += int(i**2);
print ("Problem 6: " + str(x-y));
