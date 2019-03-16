"""
Merge Sort 
"""
def merge(aList,bList):
    cList = []
    aList.append(9999999)
    bList.append(9999999)
    j = 0
    k = 0
    for i in range(0, len(aList) + len(bList) - 1):
        if aList[j] >= bList[k]:
            cList.append(bList[k])
            k = k + 1
        else:
            cList.append(aList[j])
            j = j + 1
    del cList[-1]
    return(cList)


def mergeSort(mSort):
    if len(mSort) <= 1:
        return mSort

    a = mSort[:len(mSort)//2]
    b = mSort[len(mSort)//2:]

    return(merge(mergeSort(a), mergeSort(b)))

a = [15, 20, 2, 0, 3, 5, 6, 10, 34, 24]
print(mergeSort(a))



#b = [2, 7, 8, 9, 11]

#sortList = merge(a, b)
#print(sortList)

