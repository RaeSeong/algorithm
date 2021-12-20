import sys
input = int(sys.stdin.readline())


def NQ(N):
    pos = [0]*N
    flag_a = [False]*N
    flag_b = [False]*(2*N-1)
    flag_c = [False]*(2*N-1)
    for i in range(N):
        for j in range(N):
            if not flag_a[i] and not flag_b[i+j] and not flag_c[N-1-i+j]:
                # print(list(flag_a),list(flag_b),list(flag_c))

                pos[j] = i
                flag_a[i] = True
                flag_b[i+j] = True
                flag_c[N-1-i+j] = True

                print(list(pos))
                

NQ(input)