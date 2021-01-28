import heapq
heap=[]
while(1):
    if(len(heap)==0):
        size=0
        print("please enter the initial size of heap: ")
        size = int(input())
        for x in range(0,size):
            data=int(input())
            heap.append(data)
        heapq.heapify(heap)
    else:
        print("Please enter no as according to choice \n 1 : insert in heap. /n 2 : remove from heap. /n 3 : Replace from heap.")
        r = int(input())
        if (r == 1):
            print("please enter data:")
            data = int(input())
            heapq.heappush(heap,data)
        elif (r==2):
            heapq.heappop(heap)
        elif (r==3):
            print("please enter data:")
            data = int(input())
            heapq.heapreplace(heap,data)
    print(heap)

