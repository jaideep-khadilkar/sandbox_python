

class Stack:
    A = [None]*1000
    index = -1
    def push(self,key):
        self.index = self.index + 1
        self.A[self.index] = key
        return
    def pop(self):
        if(self.index>0):
            self.index = self.index-1
            return self.A[self.index]
    def display(self):
        for i in range(0,self.index+1):
            print self.A[i]

print 'test'
stack = Stack()
stack.push(10)
stack.push(30)
stack.pop()
stack.push(40)
stack.push(50)
stack.push(60)
stack.display()