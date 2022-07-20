#TC
# push, peek, empty O(1)
# pop O(n)

class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []
        

    def push(self, x: int) -> None:
        self.instack.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.outstack.pop()
        

    def peek(self) -> int:
        if len(self.outstack) == 0:
            while self.instack:
                self.outstack.append(self.instack.pop())
              
        return self.outstack[-1]
        
    def empty(self) -> bool:
        if len(self.instack) + len(self.outstack) == 0:
            return True
        else:
            return False