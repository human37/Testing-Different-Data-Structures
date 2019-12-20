class Node:
    def __init__(self, item):
        self.item = item
        self.Left = None
        self.Right = None
class BST:
    def __init__(self):
        self.mRoot = None
    def Exists(self, item):
        return self.ExistsR(item, self.mRoot)
    def ExistsR(self, item, current):
        if current is None:
            return False
        elif current.item == item:
            return True
        elif item < current.item:
            return self.ExistsR(item, current.Left)
        else:
            return self.ExistsR(item, current.Right)
    def Insert(self, item):
        if self.Exists(item):
            return False
        else:
            self.mRoot = self.InsertR(item, self.mRoot)
            return True
    def InsertR(self, item, current):
        if current is None:
            current = Node(item)
        elif item < current.item:
            current.Left = self.InsertR(item, current.Left)
        else:
            current.Right = self.InsertR(item, current.Right)
        return current
    def Retrieve(self, item):
        return self.RetrieveR(item, self.mRoot)
    def RetrieveR(self, item, current):
        if current is None:
            return None
        elif current.item == item:
            return current.item
        elif item < current.item:
            return self.RetrieveR(item, current.Left)
        else:
            return self.RetrieveR(item, current.Right)
    def Traverse(self, callbackFunction):
        return self.TraverseR(callbackFunction, self.mRoot)
    def TraverseR(self, callbackFunction, current):
        if current is None:
            return None
        callbackFunction(current.item)
        self.TraverseR(callbackFunction, current.Left)
        self.TraverseR(callbackFunction, current.Right)
    def Size(self):
        return self.SizeR(self.mRoot)
    def SizeR(self, current):
        if current is None:
            return 0
        return 1 + self.SizeR(current.Left) + self.SizeR(current.Right)
    def Delete(self, item):
        if not self.Exists(item):
            return False
        self.mRoot = self.DeleteR(item, self.mRoot)
        return True
    def DeleteR(self, item, current):
        if item < current.item:
            current.Left = self.DeleteR(item, current.Left)
        elif item > current.item:
            current.Right = self.DeleteR(item, current.Right)
        else:  # Delete the item of this node
            if current.Left is None and current.Right is None:  # leaf node
                current = None
            elif current.Left is None:  # one right child
                current = current.Right
            elif current.Right is None:  # one left child
                current = current.Left
            else:  # two children
                s = current.Right
                while s.Left:
                    s = s.Left
                current.item = s.item
                current.Right = self.DeleteR(s.item, current.Right)
        return current
