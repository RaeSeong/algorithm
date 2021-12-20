import sys
N = int(sys.stdin.readline());
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)];
cell = 0;

def check(x,y,size):
    allsum = 0;
    for i in range(size):
        for j in range(size):
            allsum += paper[x+i][y+j];
    if allsum == 0:
        return 1;
    elif allsum == size**2:
        return 100000;
    else:
        half = int(size/2)
        return check(x,y,half) + check(x+half,y,half) + check(x,y+half,half) + check(x+half,y+half,half)

result = 0;
result = check(0,0,N)

white = result%100000;
print(white);
print(int((result-white)/100000));
