class MinStack(object):

    def __init__(self):
        self.min_value = float('inf')
        self.min_stack = []
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
             self.min_stack.append(val)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()