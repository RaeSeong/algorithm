import sys
cnt = int(sys.stdin.readline())
wordL = []
for i in range(cnt):
    wordL.append(sys.stdin.readline().rstrip())

#중복 제거
wordL = list(set(wordL))

#정렬
wordL.sort(key = lambda x:(len(x),x))

for k in wordL:
    print(k)
# #글자 수 정렬
# lenL = []
# for j in range(len(wordL)):
#     lenL.append(len(wordL[j]))
# lenL.sort()



# print(list(wordL))
