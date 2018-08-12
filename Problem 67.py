file = open("p067_triangle.txt");
grid = [];
sums = [];
for i in range(0,100):
    temp = file.readline().strip().split(" ");
    temp2 = [0 for x in range(len(temp))];
    grid.append(temp);
    sums.append(temp2);
for i in range(0,100):
    sums[len(grid)-1][i] = int(grid[len(grid)-1][i]);
r = len(grid)-2;
while(r>=0):
    c = 0;
    while(c<=r):
        if(sums[r+1][c] > sums[r+1][c+1]):
            sums[r][c] = int(grid[r][c]) + sums[r+1][c];
        else:
            sums[r][c] = int(grid[r][c]) + sums[r+1][c+1];
        c += 1;
    r -= 1;
##    for x in range(0,len(grid)):
##        print sums[x];
##    print " ";
print ("Problem 67: " + str(sums[0][0]));
