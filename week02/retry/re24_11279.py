import sys
N = int(sys.stdin.readline())
command = [int(sys.stdin.readline()) for _ in range(N)]
heap = [0]
lastnode = 0

def heapsort(num):
    if num > 1:
        parent = num//2
        if heap[parent] < heap[num]:
            tmp = heap[num]
            heap[num] = heap[parent]
            heap[parent] = tmp
            heapsort(parent)

def heappop():
    global lastnode
    if lastnode == 0:
        print(0)
    else:
        print(heap[1])
        if lastnode > 1:
            heap[1] = heap.pop()
        else:
            heap.pop()
        lastnode -= 1
        parent = 1
        child = 2
        while child <= lastnode:
            if child + 1 <= lastnode:
                child = child if heap[child] > heap[child+1] else child+1
            if heap[child] > heap[parent]:
                tmp = heap[parent]
                heap[parent] = heap[child]
                heap[child] = tmp
                parent = child
                child = child*2

for i in command:
    if i == 0:
        heappop()
    else:
        heap.append(i)
        lastnode += 1
        heapsort(lastnode)