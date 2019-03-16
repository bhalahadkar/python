class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def balancestr(expr):
    s = stack()
    balance = False

    for i in expr:
        if i in "([{":
            token = i
            s.push(token)
        elif i in ")]}" and not s.isEmpty():
            token = i
            s.pop()

    if s.isEmpty():
        return True
    else:
        return False

def reversesentence(expr):
    s = stack()
    alist = expr.split('.')
    blist = alist[::-1]
    return ".".join(blist)

def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

#print(balancestr('{([])}'))

#print(reversesentence('i.like.this.program.very.much'))
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)