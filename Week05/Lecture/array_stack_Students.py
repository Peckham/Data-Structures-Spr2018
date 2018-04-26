from exceptions import Empty


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self.myStack = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self.myStack)

    def isEmpty(self):
        return len(self.myStack) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.myStack.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.myStack[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.isEmpty():
            raise Empty('Stack is empty')
        else:
            return self.myStack.pop()

    def __repr__(self):
        """ Return a string of current elements of of Stack """
        return str(self.myStack)


if __name__ == '__main__':
    S = ArrayStack()                 # contents: [ ]
    S.push(5)                        # contents: [5]
    S.push(3)                        # contents: [5, 3]
    print(S)                         # print current contents of Stack S
    print(len(S))                    # contents: [5, 3];    outputs 2
    print(S.pop())                   # contents: [5];       outputs 3
    print(S.isEmpty())              # contents: [5];       outputs False
    print(S.pop())                   # contents: [ ];       outputs 5
    print(S.isEmpty())              # contents: [ ];       outputs True
    S.push(7)                        # contents: [7]
    S.push(9)                        # contents: [7, 9]
    print(S.top())                   # contents: [7, 9];    outputs 9
    S.push(4)                        # contents: [7, 9, 4]
    print(len(S))                    # contents: [7, 9, 4]; outputs 3
    print(S.pop())                   # contents: [7, 9];    outputs 4
    S.push(6)                        # contents: [7, 9, 6]
    S.push(8)                        # contents: [7, 9, 6, 8]
    print(S.pop())                   # contents: [7, 9, 6]; outputs 8
