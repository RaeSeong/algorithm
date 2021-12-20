while True:
    a = input()
    b = input()
    try:
        A = int(a)
        B = int(b)
        if len(a) == 3 and len(b) == 3:
            break
        else:
            print('Please input 100~999')
    except:
        print('Please input number')

print(A*int(list(b)[2]))
print(A*int(list(b)[1]))
print(A*int(list(b)[0]))
print(A*B)