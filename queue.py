class Q:
    def __init__(self):
        #here we have created list
        self.queue = list() 

        #we will enter the data in this queue from left
    def enqueue(self,dataval):
        self.queue.insert(0,dataval)
        return True

    #to know what is the size of queue
    def size(self):
        return len(self.queue)

    #removing the element from right hand side of queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            return self.queue.pop()
instance = Q()
while (1):
    print("choose one of the following: \n 1 : pushing in queue \n 2 : length of queue \n 3 : removing an element from queue")
    a = int(input())
    
    print(instance.queue)
    if( a == 1):
        b = input()
        instance.enqueue(b)
    elif ( a == 2):
        print(instance.size())
    elif ( a == 3):
        instance.dequeue()
    else:
        print("invalid input you stupid! \n")
        


    

        
