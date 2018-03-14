class Empty:
    pass


class ArrayStack:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Empty()
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()
        return self.array.pop(-1)

    def __repr__(self):
        return str(self.array)


def compute(left, right, operator):
    if operator == "*":
        return left * right
    elif operator == "/":
        return left / right
    elif operator == "+":
        return left + right
    elif operator == "-":
        return left - right


def evaluate(string):
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    table = {"+": 2, "-": 2, "*": 3, "/": 3, "(": 1, ")": 1}
    data = string.split()
    for i in data:
        if i not in table.keys():  # a number
            operand_stack.push(int(i))
        elif i == "(":
            operator_stack.push(i)
        elif i == ")":
            operator = operator_stack.pop()
            while operator != "(":
                number1 = operand_stack.pop()
                number2 = operand_stack.pop()
                operator = operator_stack.pop()
                operand_stack.push(compute(number2, number1, operator))
        else:
            while not operator_stack.is_empty() and table[operator_stack.top()
                                                          >= table[i]]:
                number1 = operand_stack.pop()
                number2 = operand_stack.pop()
                operator = operator_stack.pop()
                operand_stack.push(compute(number2, number1, operator))
        while not operator_stack.is_empty():
            number1 = operand_stack.pop()
            number2 = operand_stack.pop()
            operator = operator_stack.pop()
            operand_stack.push(compute(number2, number1, operator))
            return operand_stack.top()


print(evaluate("9 + 8 * ( 7 - 6 ) / ( 2 / 8 )"))  # 41
print(evaluate("9 + 8 * 7 / ( 6 + 5 ) - ( 4 + 3 ) * 2"))  # 0.0909090909
print(evaluate("9 + 8 * 7 / ( ( 6 + 5 ) - ( 4 + 3 ) * 2 )"))  # -9.66666666667
