def binarySearch(aList, search):
    found = False
    start = 0
    last = len(aList) - 1

    while start < last and not found:
        midpt = (start + last) // 2
        if aList[midpt] == search:
            return True
        elif search > midpt:
            start = midpt + 1
        else:
            last = midpt

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))



