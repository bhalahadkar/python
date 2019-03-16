class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def parChecker(expr):
    s = Stack()
    balance = True
    index = 0
    while index < len(expr) and balance:
        symbol = expr[index]
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            s.pop()
        elif s.isEmpty():
            balance = False

        index = index + 1

    if balance and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def baseConverter(n, base):
    newnum = ''
    baseList = '0123456789ABCDEFG'
    s = Stack()
    while n > 0:
        rem = n % base
        s.push(rem)
        n = n // base

    while not s.isEmpty():
        newnum = newnum + str(baseList[s.pop()])

    return newnum


def infixToPostfix(infixexpr):
    dec = {}
    dec["*"] = 3
    dec["/"] = 3
    dec["+"] = 2
    dec["-"] = 2
    dec["("] = 1
    dec[")"] = 1

    opStack = Stack()
    postfix = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfix.append(token)
        elif token in "*/+-()":
            if not opStack.isEmpty() and (dec[opStack.peek()] > dec[token]):
                postfix.append(opStack.pop())
                opStack.push(token)
            else:
                opStack.push(token)

    while not opStack.isEmpty():
        postfix.append(opStack.pop())

    return " ".join(postfix)


def postfixeval(expr):
    opStack = Stack()
    postfix = expr.split()

    for token in postfix:
        if token in "0123456789":
            opStack.push(int(token))
        else:
            operand2 = opStack.pop()
            operand1 = opStack.pop()
            eval = domath(operand1, operand2, token)
            opStack.push(eval)

    return (opStack.pop())


def domath(operand1, operand2, operator):
    if operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 // operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "+":
        return operand1 + operand2


# print(infixToPostfix("5 * 7 + 2 * 4"))

print(postfixeval('7 8 + 3 2 + /'))

# print(baseConverter(45, 16 ))


# a * b + c * D
#
#
#
#
#


