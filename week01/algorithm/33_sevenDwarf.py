import sys
dwarfL = []
for i in range(9):
    dwarfL.append(int(sys.stdin.readline()))

def new_dwarfL(arr):
    lierV = sum(arr) - 100
    for j in range(8):
        for k in range(j+1,9):
            if arr[j] + arr[k] == lierV:
                x,y = arr[j],arr[k]
                arr.remove(x)
                arr.remove(y)
                return arr

realDwarf = sorted(new_dwarfL(dwarfL))
for l in realDwarf:
    print(l)