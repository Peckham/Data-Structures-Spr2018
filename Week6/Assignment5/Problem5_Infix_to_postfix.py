class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop(-1)

    def __repr__(self):
        return str(self._data)


def infix_to_postfix(string):
    stack = ArrayStack()
    tokens = string.split(" ")
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
    # To do
    pass


# OUTPUTS: 3 2 + 4 / 3 2 * 4 + +
infix_to_postfix("( 3 + 2 ) / 4 + ( 3 * 2 + 4 )")
infix_to_postfix("X + Y / ( 5 * Z ) + 10")  # OUTPUTS: X Y 5 Z * / + 10 +
