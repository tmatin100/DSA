class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.que = []

    def enqueue(self, value):
        if self.size == self.capacity:
            print("the que is full, wait for space")
        else:
            enqueueElement = self.que.insert(0,value)
            print("enqueueing", value)
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("The que is empty")
        else:
            dequeueElement = self.que.pop()
            print("dequeuing", dequeueElement)
            self.size -= 1

que1 = Queue(3)

que1.enqueue(10)
que1.enqueue(20)
que1.enqueue(30)
que1.enqueue(40)

que1.dequeue()
que1.dequeue()
que1.dequeue()
que1.dequeue()







