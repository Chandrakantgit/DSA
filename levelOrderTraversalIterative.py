class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def levelOrderTraversal(queue):
    if queue.len == 0:
        return None
    node = queue[0]
    queue.pop(0)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.apend(node.right)
    print(node.data)
    levelOrderTraversal(queue)

queue = list()
root = Node(4)
queue.append(root)
root.left = 3
root.right = 5
root.left.left = 44
root.right.right = 781

levelOrderTraversal(queue)