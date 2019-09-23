class BinarySearchTree:
    def __init__(self, value):  # We're just using value, so key is value
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_value = BinarySearchTree(value)
        if value < self.value:
            if self.left == None:
                self.left = new_value
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = new_value
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                return self.left.contains(target)
            else:
                if self.right == None:
                    return False
                return self.right.contains(target)

    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()


    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
