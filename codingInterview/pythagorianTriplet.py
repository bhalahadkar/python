def isTriplet(aList):
    sqList = [i * i for i in aList]
    rlist = []
    for i in range(len(sqList)-1):
        for j in range(1,len(sqList)):
            sum = sqList[i] + sqList[j]
            if sum in sqList:
                rlist.append(aList[i])
                rlist.append(aList[j])

            sum = 0

    return rlist

print(isTriplet([3, 2, 4, 6, 5]))