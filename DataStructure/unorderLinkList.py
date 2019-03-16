class Node:
    def __init__(self, itemdata):
        self.head = itemdata
        self.next = None

    def getData(self):
        return self.head

    def setData(self,data):
        self.head = data

    def getNext(self):
        return self.next

    def setNext(self, data):
        self.next = data


class UnorderList:
    def __init__(self):
        self.head = None

    def add(self,data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count +1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        found = False
        previous = None

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def getHead(self):
        return self.head



def findmiddle(linked):
    length = linked.size()
    i = 1
    current = linked.getHead()
    while i < length//2:
        current = current.getNext()
        i = i +1
    return current.getData()

mylist = UnorderList()


mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(findmiddle(mylist))
