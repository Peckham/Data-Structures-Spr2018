class SharedMemoryStack():

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * SharedMemoryStack.DEFAULT_CAPACITY
        self.stack1_size = 0
        self.stack2_size = 0

    def pushStack1(self, e):
        if not self.is_full():
            self._data[self.stack1_size] = e
            self.stack1_size += 1

    def pushStack2(self, e):
        if not self.is_full():
            self.stack2_size += 1
            self._data[-self.stack2_size] = e

    def popStack1(self):
        if not self.is_empty1():
            toReturn = self._data[self.stack1_size - 1]
            self.stack1_size -= 1
            return toReturn

    def popStack2(self):
        if not self.is_empty2():
            toReturn = self._data[-self.stack2_size]
            self.stack2_size -= 1
            return toReturn

    def is_full(self):
        if self.stack1_size + self.stack1_size == len(self._data):
            raise Full()

    def is_empty1(self):
        return self.stack1_size == 0

    def is_empty2(self):
        return self.stack2_size == 0

    def peekStack1(self):
        return self._data[self.stack1_size]

    def peekStack2(self):
        return self._data[-self.stack2_size]

    def __str__(self):
        result = []
        result.append("Stack 1: ")
        for i in range(self.stack1_size):
            result.append(str(self._data[i]) + " ")
        result.append("Stack 2: ")
        for i in range(1, self.stack2_size + 1):
            result.append(str(self._data[-i]) + " ")
        return "".join(result)


stack = SharedMemoryStack()
stack.pushStack1(1)
stack.pushStack1(2)
stack.pushStack1(3)
stack.pushStack1(4)
stack.pushStack2(5)
stack.pushStack2(6)
stack.pushStack2(7)
stack.pushStack2(8)
stack.pushStack2(9)
stack.pushStack2(10)
print(stack)  # Stack 1: 1, 2, 3, 4; Stack 2: 5, 6, 7, 8, 9, 10
print("Popping: ", stack.popStack1())  # popped 4
stack.pushStack2(11)  # Stack 1: 1, 2, 3; Stack 2: 5, 6, 7, 8, 9, 10, 11
print(stack)
print("Popping: ", stack.popStack2())  # popped 11
print("Popping: ", stack.popStack2())  # popped 10
print(stack)
