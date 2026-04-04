class MyQueue(object):

    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def push(self, x):
        self.in_queue.append(x)

    def pop(self):
        if not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        return self.out_queue.pop()

    def peek(self):
        if not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        return self.out_queue[-1]

    def empty(self):
        return not self.in_queue and not self.out_queue

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()