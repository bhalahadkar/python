lass Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postFix = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postFix.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            toptoken = opStack.pop()
            while toptoken != "(" and (not opStack.isEmpty()):
                postFix.append(toptoken)
                toptoken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token] ):
                postFix.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postFix.append(opStack.pop())

    return " ".join(str(v) for v in postFix)

print(infixToPostfix("A * B + C * D"))

def checkpalindrome(expr):
    revexpr = expr[::-1]
    return expr == revexpr

print(checkpalindrome('malayalam'))