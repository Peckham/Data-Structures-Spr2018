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
        if not self.is_empty():
            return self._data[-1]
        else:
            return None

    def pop(self):
        if not self.is_empty():
            return self._data.pop(-1)

    def __repr__(self):
        return str(self._data)


def infix_to_postfix(string):
    output = []
    stack = ArrayStack()
    tokens = string.split(" ")
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
    for i in tokens:
        if i in list(precedence.keys()):
            if stack.is_empty():
                stack.push(i)
            elif i is "(" or precedence[stack.top()] < precedence[i]:
                stack.push(i)
            elif i is ")":
                while stack.top() is not "(":
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack.top() is not None and precedence[stack.top()] >= precedence[i]:
                    output.append(stack.pop())
                stack.push(i)
        else:
            output.append(i)
    while not stack.is_empty():
        output.append(stack.pop())
    print("".join(output))


infix_to_postfix("( 3 + 2 ) / 4 + ( 3 * 2 + 4 )")  # 3 2 + 4 / 3 2 * 4 + +
infix_to_postfix("X + Y / ( 5 * Z ) + 10")  # X Y 5 Z * / + 10 +
infix_to_postfix("( ( ( X + Y ) * Z ) + 2 ) * 3 - 2")  # X Y + Z * 2 + 3 * 2 -
