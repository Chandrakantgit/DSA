class stack:

    def __init__(self):
        self.stack = []

    def add(self,dataval):
        #use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
        #use peek to look at the top of the stack
    def peek(self):
        if len(self.stack) == 0:
            print("nothing there")
            return False
        else:
            return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the stack")
        else:
            return self.stack.pop()

while (1):
    print("choose one of the following: \n 1 : pushing in stack \n 2 : peeking in stack \n 3 : poping from stack")
    a = int(input())
    Astack = stack()
    if( a == 1):
        b = input()
        Astack.add(b)
    elif ( a == 2):
        Astack.peek()
    elif ( a == 3):
        Astack.remove()
    else:
        print("invalid input you stupid! \n")
        
