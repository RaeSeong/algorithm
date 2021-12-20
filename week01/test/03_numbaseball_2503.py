import sys
cnt = int(sys.stdin.readline())
probable = []
x = y = z = [True]*9
print(x,y,z)
for i in range(cnt):
    test,S,B = map(int,sys.stdin.readline().split())
    seper = list(str(test))

def addpro(s,b,case = []):
    if s == 0:
        if b == 0:
            x[case[0]] = y[case[0]] = z[case[0]] = x[case[1]] = y[case[1]] = z[case[1]] = x[case[2]] = y[case[2]] = z[case[2]] = False
        elif b == 1:
            probable.append([case[1],0,0])
            probable.append([case[2],0,0])
            probable.append(0,[case[0],0])
            probable.append(0,[case[2],0])
            probable.append(0,0,[case[0]])
            probable.append(0,0,[case[1]])
        elif b == 2:
            probable.append([case[1],case[2],0])
            probable.append([case[2],case[0],0])
            probable.append(0,[case[2],case[1]])
        elif b == 3:
            probable.append([case[1],case[2],case[0]])
            probable.append([case[2],case[0],case[1]])
    elif s == 1:
        if b == 0:
            probable.append([case[0],0,0])
            probable.append(0,[case[1],0])
            probable.append(0,0,[case[2]])
    case[0]