class TreeNode:
    def __init__(self, value):
        self.value =  value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                print("tree",self.left)
                self.left = TreeNode(value)
            else:
                print("tree",self.left)
                self.left.insert(value)
        else:
            if self.right is None:
                print("tree right", self.right)
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    def inorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.inorder_traversal()
        
        if self.right:
            self.right.inorder_traversal()
    
    def preorder_traversal(self):
        
        if self.left:
            self.left.preorder_traversal()      
        print(self.value)  
        if self.right:
            self.right.preorder_traversal()
        
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()        
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True



tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

tree.preorder_traversal()
print(tree.find(5))
# array

# def inOrderTraverse(tree, array = []):
#     # To-Do
#     # add array
#     if tree is not None:
#         inOrderTraverse(tree.left, array)
#         array.append(tree.value)
#         inOrderTraverse(tree.right, array)
#     return array
      
