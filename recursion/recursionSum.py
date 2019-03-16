def recursioSum(sumList):
    if len(sumList) == 1:
        return sumList[0]
    else:
        return (sumList[0] + recursioSum(sumList[1:]))

print(recursioSum([1, 2, 3, 4, 5]))