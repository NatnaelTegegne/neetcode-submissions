class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.minStack:
            
            min_ = min(val, self.stack[-1])
            self.stack.append(min_)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(val)
        
        
        
        
    def pop(self) -> None:
        if(len(self.minStack) != 0):
            self.minStack.pop()
            self.stack.pop()
        

    def top(self) -> int:
        if(len(self.minStack) != 0):
            return self.minStack[-1]

    def getMin(self) -> int:
        if(len(self.minStack) != 0):
            return self.stack[-1]
        
