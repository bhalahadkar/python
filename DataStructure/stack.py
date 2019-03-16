class stack:
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


s=stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

def parChecker(s1):
    st=stack()
    balanced = True
    index = 0

    while index < len(s1) and balanced:
        if s1[index] == "(":
            st.push(s1[index])
        elif s1[index]== ")":
            st.pop()
        elif st.isEmpty():
            balanced = False

        index = index + 1

    if balanced and st.isEmpty():
        return True
    else:
        return False


def parChecker2(s1):
    st=stack()
    balanced = True
    index = 0

    while index < len(s1) and balanced:
        if s1[index] in "([{":
            st.push(s1[index])
        elif s1[index] in ")]}":
            st.pop()
        elif st.isEmpty():
            balanced = False

        index = index + 1

    if balanced and st.isEmpty():
        return True
    else:
        return False

def divideBy2(decNumber):
    remstack = stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remstack.isEmpty():
        pop = str(remstack.pop())
        binString = binString + pop

    return binString

def baseconverter(dec , base):
    digits = "0123456789ABCDEF"

    remstack = stack()

    while dec > 0:
        rem = dec % base
        remstack.push(rem)
        dec = dec // base

    newStr = ''

    while not remstack.isEmpty():
        newStr = newStr + digits[remstack.pop()]

    return newStr


print(parChecker("(((8789)))"))
print(parChecker('((9988)'))

print(parChecker2('{{([][])}()}'))
print(parChecker2('[{()]'))

print(divideBy2(42))


print(baseconverter(25,2))
print(baseconverter(198,16))















