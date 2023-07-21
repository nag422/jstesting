class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.data == value: # to remove duplicates
            return
        if self.data < value:
            if self.left:
                self.left.insert(value)  # have to insert data
            else:
                self.left = BinaryTree(value)
        else:
            if self.right:
                self.right.insert(value) # have to insert data
            else:
                self.right = BinaryTree(value)
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            # print("self.left",self.left.in_order_traversal())
            elements += self.left.in_order_traversal()


        elements.append(self.data)

        if self.right:
            # print("self.right", self.right)
            elements += self.right.in_order_traversal()

        return elements
    def search(self,val, numbers):
        if self.data == val:
            return
        if val < self.data:
            if self.left:
                return self.left.search(val, numbers)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val,numbers)
            else:
                return False, numbers.index(val)
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
                print(self.left)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self



def build_tree(elements):
    root = BinaryTree(elements[0])
    for i in range(1, len(elements)):
        root.insert(elements[i])
    return root

# def print_recursion(value):
#     print("printed at", value)
# def check_recursion(value):
#     print("value is started", value)
#     data=[]
#     if value <= 10:
#         value+=1
#         return check_recursion(value)
#         data+[value]
#         print_recursion(value)
#     print("inside",data)    

#     print("end recursion")

#     return data


if __name__ == "__main__":
    numbers = [17, 4, 1, 28, 4, 9, 18, 34]
    # numbers = [425, 4, 16457, 2248, 9684, 9462, 16028, 3454]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree)
    # print(numbers_tree.search(28, numbers))
    print(numbers_tree.delete(34))
    print("deleted one", numbers_tree.in_order_traversal())
# check_recursion(1)