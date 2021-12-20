import sys
from collections import deque
strpar = sys.stdin.readline().rstrip()
parset = deque([])
def calc(l):
    cnt = 0
    
    while cnt < len(l):
        a = list(l)[cnt]
        result = 1
        if a == '(':
            parset.append(2)
        elif a == '[':
            parset.append(3)
        else:
            if a == ')':
                try:
                    if parset.pop() == 2:
                        value = 2
                        result = 2
                    else:
                        result = 0
                except:
                    result = 0
            else:
                try:
                    if parset.pop() == 3:
                        value = 3
                        result = 3
                    else:
                        result = 0
                except:
                    result = 0
        print(cnt,result)
        cnt +=1

calc(strpar)