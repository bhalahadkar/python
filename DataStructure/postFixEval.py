class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

def postFixEval(postFixExp):
    evalStack = Stack()

    tokenlist = postFixExp.split()

    for token in tokenlist:
        if token in "0123456789":
            evalStack.push(token)
        elif token in "+-*/":
            operand1 = int(evalStack.pop())
            operand2 = int(evalStack.pop())
            eval = domath(token, operand1, operand2)

            evalStack.push(eval)

    return evalStack.pop()

def domath(oper, op1, op2):
    if oper == "+":
        eval = op1 + op2
    elif oper == "-":
        eval = op2 - op1
    elif oper == "*":
        eval = op1 * op2
    elif oper == "/":
        eval = op2 / op1
    return eval


print(postFixEval("7 8 + 3 2 + /"))


