import sys
T = int(sys.stdin.readline())
paStr = []
for i in range(T):
    paStr.append(list(sys.stdin.readline().rstrip()))
for j in range(T):
    VPS = []
    for k in range(len(paStr[j])): 
        if paStr[j][k] == '(':
            VPS.append('(')
        elif paStr[j][k] == ')':
            if VPS == []:
                print('NO')
                VPS.append('NO')
                break
            else:
                del VPS[len(VPS)-1]
    if VPS == []:
        print('YES')
    elif VPS == ['NO']:
        pass
    else:
        print('NO')
