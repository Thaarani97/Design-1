# TC
# add ,remove, contains O(1)

class MyHashSet:

    def __init__(self):
        self.bucketlen = 1000
        self.bucket = [None] * self.bucketlen
    
    def hash(self, key: int):
         return key % self.bucketlen
    
    def doublehash(self, key: int):
        return key // self.bucketlen
          
    def add(self, key: int) -> None:
        hashind = self.hash(key)
        doublehash = self.doublehash(key)
        if not self.bucket[hashind] and hashind==0:
            self.bucket[hashind] = [False] * (self.bucketlen+1)
        if not self.bucket[hashind]:
             self.bucket[hashind] = [False] * (self.bucketlen)
                
        self.bucket[hashind][doublehash] = True
            
    def remove(self, key: int) -> None:
        hashind = self.hash(key)
        doublehash = self. doublehash(key)
        if self.bucket[hashind]:
            self.bucket[hashind][doublehash] = False
        
    def contains(self, key: int) -> bool:
        hashind = self.hash(key)
        doublehash = self.doublehash(key)
        if self.bucket[hashind]:
            return self.bucket[hashind][doublehash]