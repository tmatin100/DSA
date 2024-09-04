class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.stack = []

    def push(self, value):
        if self.size == self.capacity:
            print("Stack is full cannot push")
        else:
            self.stack.append(value)
            self.size += 1
            print("pushed", value)

    def peek(self):
        if self.size == 0:
            print("Nothing to do becasue stack is empty")
        else:
            print("top most element is", self.stack[-1])

    def pop(self):
       if self.size == 0:
            print("Nothing to pop, stack is empty")
        else:
            topElement = self.stack.pop()
            self.size -= 1
            print("popped", topElement)
            return topElement


stack1 = Stack(3)
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)

stack1.peek()

stack1.pop()
stack1.peek()

stack1.pop()
stack1.peek()

stack1.pop()
stack1.peek()

stack1.pop()
stack1.peek()

