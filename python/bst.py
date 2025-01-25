class Bst:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def insert(self,val):
        if val<self.val:
            if self.left is None:
                self.left=Bst(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right=Bst(val)
            else:
                self.right.insert(val)
    def search(self,val):
        if val<self.val:
            if self.left is None:
                return False
            else:
                return self.left.search(val)
        elif val>self.val:
            if self.right is None:
                return False
            else:
                return self.right.search(val)
        else:
            if self.val==val:
                return True
            else:
                return False
    def traverse(self,tab=" "):
        if self.left:
            self.left.traverse("\t"+tab)
        print(self.val)
        if self.right:
            self.right.traverse("\t"+tab)
    def dele(self,val):
        if self is None:
            return self
        if val<self.val:
            if self.left is None:
                return False
            else:
                return self.left.dele(val)
        elif val>self.val:
            if self.right is None:
                return False
            else:
                return self.right.dele(val)
        else:
            if not self.right and not self.left:
                return None
            if self.right and not self.left:
                return self.right
            if self.left and not self.right:
                return self.left
            pt=self.right
            while self.left:
                pt=self.left
            self.val=pt.val
            self.right=self.right.dele(val)
        
b=Bst(20)
b.insert(20)
b.insert(21)
b.insert(22)
b.insert(18)
b.insert(5)
b.insert(19)
print(b.search(17))
#b.dele(22)
b.traverse()