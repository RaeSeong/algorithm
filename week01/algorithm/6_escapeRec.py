x,y,w,h = map(int,input().split())

if w >= 2*x:
    hor = x
else:
    hor = w - x

if h - y >= y:
    ver = y
else:
    ver = h - y

if hor > ver:
    print(ver)
else:
    print(hor)