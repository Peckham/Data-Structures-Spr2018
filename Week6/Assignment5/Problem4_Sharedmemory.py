class SharedMemoryStack():

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * SharedMemoryStack.DEFAULT_CAPACITY
        self.stack1_size = 0
        self.stack2_size = 0

    def pushStack1(self, e):
        pass

    def pushStack2(self, e):
        pass

    def popStack1(self):
        pass

    def popStack2(self):
        pass

    def is_full(self):
        pass

    def is_empty1(self):
        pass

    def is_empty2(self):
        pass

    def peekStack1(self):
        pass

    def peekStack2(self):
        pass

    def __str__(self):
        result = []
        result.append("Stack 1: ")
        # Your code 1 to show stack 1
        result.append("STack 2: ")
        # Your code 2 to show stack 2

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
