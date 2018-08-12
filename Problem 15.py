grid = [[0 for x in range(21)] for y in range(21)];
r = 20;
while(r>=0):
    c = 20;
    while(c>=0):
        num = 0;
        if(c+1<21):
            num+=grid[r][c+1];
        if(r+1<21):
            num+=grid[r+1][c];
        grid[r][c]=num;
        grid[20][20]=1;
        c -=1;
    r -= 1;
    for x in range(0,21):
        print grid[x];
    print " ";
print ("Problem 15: " + str(grid[0][0]));
