for a in range(1,1001):
    for b in range(a+1,1001):
        c = 1000 - a - b;
        if (a**2 + b**2==c**2):
            print ("Problem 9: " + str(a*b*c));