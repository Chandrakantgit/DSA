class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    """We will compare the new values to the parent node if they
     are small we will put in left node and similarly"""
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        
        print(self.data)

        if self.right:
            self.right.printTree()


    #Inorder traversal
    #left-> Root -> Right
    def inOrderTraversal(self,root):
        res=[]
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
    
    #preorderTraversal
    #Left -> center -> right
    def preorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    #postOrderTraversal
    #right -> center -> left
    def postOrderTraversal(self,root):
        res = []
        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res
        



# Creating a Node object of class Node
instance = Node(int(input("Enter first element: ")))

while (1):
    print("Choose one of the following: \n 1 : Enter data in tree \n 2 : print Tree \n 3 : PreOrder Traversal \n 4 : InOrder Traversal \n 5 : PostOrderTraversal \n")
    
    choice = int(input("Enter: "))
    if choice == 1:
        b = int(input())
        instance.insert(b)

    elif (choice == 2):
        instance.printTree()
    elif(choice == 3):
        print(instance.preorderTraversal(instance))
    elif(choice == 4):
        print(instance.inOrderTraversal(instance))
    elif(choice == 5):
        print(instance.postOrderTraversal(instance))
    else:
        print("Invalid input you stupid!\n")
