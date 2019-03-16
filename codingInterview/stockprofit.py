class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

def stockprofit(alist):
    s = stack()
    prfitdays = []
    i = 0
    start = alist[i]
    s.push(alist[i])
    while i < len(alist):
        if alist[i] < start:
            s.push(alist[i-1])
            s.push(alist[i])
            start = alist[i]
        elif alist[i] > start and i == (len(alist)-1):
            s.push(alist[i])
        i = i + 1

    while not s.isEmpty():
        prfitdays.insert(0,s.pop())
    return prfitdays

print(stockprofit([100, 180, 260, 310, 40, 535, 695]))