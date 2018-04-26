from exceptions import Empty

class Queue:
    def __init__(self):
        self.myQueue = []

    def __len__(self):
        return len(self.myQueue)

    def is_empty(self):
        return len(self.myQueue) == 0

    def enqueue(self, e):
        self.myQueue.append(e)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.myQueue.pop(0)

    def front(self):
        if self.is_empty():
          raise Empty('Stack is empty')
        return self.myQueue[0]

    def __repr__(self):
        return str(self.myQueue)

queue2 = Queue()

queue2.enqueue(2)
queue2.enqueue(8)
queue2.enqueue(16)
queue2.enqueue(32)
queue2.enqueue(64)

print(queue2)

print(queue2.dequeue())
print(queue2.dequeue())
print(queue2.dequeue())

print(queue2)
