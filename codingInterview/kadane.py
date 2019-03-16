def kedane(aList):
    curr_sum = 0
    newList = []
    newList.append(aList[0])

    for i in range(len(aList)):
        curr_sum = curr_sum + aList[i]
        newList.append(curr_sum)

    max_sum = newList[0]
    for j in range(1, len(newList)):
        if newList[j] > max_sum:
            max_sum = newList[j]

    return max_sum

print(kedane([1, 2, 3, -2, 5]))
print(kedane([-1, -2, -3, -4]))

