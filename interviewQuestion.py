def removeDups(aList):
    aList.sort()
    cur_pos = 1
    place_hold = 1
    
    while cur_pos < len(aList):
        if aList[cur_pos] != aList[cur_pos -1]:
            aList[place_hold] = aList[cur_pos]
            place_hold = place_hold + 1
        
        cur_pos = cur_pos + 1
        
    return aList[0:place_hold]

print(removeDups([2,2,2,4,5,4,7,7,8]))
    
def missinNumber(aList):
    aList.sort
    missing_number = []
    i = 0
    while i < len(aList)-1:
        nextNum = aList[i] + 1
        if nextNum != aList[i+1]:
            missing_number.append(nextNum)
        i = i + 1
    return missing_number

print(missinNumber([4,5,6,8,9,11,12]))

def sumSubarray(aList, n):
    
    subarray = []
    pair = []
    for i in range(len(aList) - 1):
        for j in range(i+1,len(aList)):
            if (aList[i] + aList[j]) == n:
                pair = [aList[i], aList[j]]
                subarray.append(pair)
    
    return subarray

def sumSuarray2(aList, n):
    subarray = []
    pair = []
    for i in range(len(aList) - 1):
        if aList[i] < n and (n - aList[i]) in aList[i:]:
            pair = [aList[i], (n - aList[i])]
            subarray.append(pair)
    return subarray

def arrayOfsum(n):
    
    array = []
    i = 1
    while i < n:
        pair = n - i
        if pair not in array:
            array.append(i)
            array.append(pair)
        i = i + 1
    return array

def printDup(aList):
    dup = []
    for i in range(len(aList)-1):
        for j in range(i+1,len(aList)):
            if aList[i] == aList[j] and aList[i] not in dup:
                dup.append(aList[i])
    return dup

def reverseStr(astr):
    if len(astr) == 1:
        return astr
    else:
        return reverseStr(astr[-1]) + reverseStr(astr[0:len(astr)-1])