class Node:
    #initial constructor takes data and initialises the tree
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,info):
        if self.data:
            if info < self.data :
                if self.left is None:
                    self.left = Node(info)
                else:
                    self.left.insert(info)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(info)
                else:
                    self.right.insert(info)
            elif info == self.data:
                print("already there!!!")
        else:
            self.data = info


    #function to find value in binarysearch tree
    def findval(self,tofind):
        if self.data == tofind:
            print("Yep! There.")
        elif tofind < self.data:
            if self.left is None:
                return str(tofind)+"Not Found!"
            return self.left.findval(tofind)
        elif tofind > self.data:
            if self.right is None:
                return str(tofind) + " Not found!"
            return self.right.findval(tofind)        

    def printTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Creating a Node object of class Node
instance = Node(int(input("Enter first element: ")))

while (1):
    print("Choose one of the following: \n 1 : Enter data in tree \n 2 : print Tree \n 3 : Find a Value\n")
    
    choice = int(input("Enter: "))
    if choice == 1:
        b = int(input())
        instance.insert(b)

    elif (choice == 2):
        instance.printTree()
    elif(choice == 3):
        a = int(input("Please enter the number to check"))
        instance.findval(a)
    else:
        print("Invalid input you stupid!\n")



    