from primecheck import checker as isPrime
class Hash:
    def __init__(self,expectedSize):
        size=expectedSize*2+1
        while not isPrime(size):
            size+=2
        self.table=[None]*size
    def Exists(self,item):
        key=int(item)
        index=key%len(self.table)
        while True:
            if self.table[index] is None:        #if it dosent exist, return False
                return False
            if self.table[index] and self.table[index]==item:      #check to see if not None or False, and it equals item
                return True
            index+=1
            if index>=len(self.table):               #if it reaches the end, restart at the beginning
                index=0
    def Insert(self,item):
        if self.Exists(item):
            return False
        key=int(item)
        index=key%len(self.table)
        while True:
            if not self.table[index]:                #if the slot is empty, or has a None type, set to the new item
                self.table[index]=item
                return True
            index+=1
            if index>=len(self.table):
                index=0
    def Traverse(self,callback):
        for i in range(len(self.table)):
            if self.table[i]:
                callback(self.table[i])
    def Retrieve(self,item):
        if not self.Exists(item):
            return None
        key=int(item)
        index=key%len(self.table)
        while True:
            if self.table[index] and self.table[index]==item:   #making sure it is equal to item and there is not a None or False there
                return self.table[index]
            index+=1
            if index>=len(self.table):
                index=0
    def Size(self):
        size=0
        for i in range(len(self.table)):
            if self.table[i]:
                size+=1
        return size
    def Delete(self,item):
        key=int(item)
        index=key%len(self.table)
        while True:
            if self.table[index] is None:
                return False
            if self.table[index] and self.table[index]==item:
                self.table[index]=False
                return True
            index+=1
            if index>=len(self.table):
                index=0