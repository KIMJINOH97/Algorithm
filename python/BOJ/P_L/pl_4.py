class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
def preorder(node):
    if not node == None:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if not node == None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def postorder(node):
    if not node == None:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

node = Node(15)
node.left = Node(1)
node.right = Node(37)
node.left.left = Node(61)
node.left.right = Node(26)
node.right.left = Node(59)
node.right.right = Node(48)
print("Preorder Traverse")
preorder(node)
print("Inorder Traverse")
inorder(node)
print("Postorder Traverse")
postorder(node)