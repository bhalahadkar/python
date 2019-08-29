def groupAnagram(aList):
    hashit = {}
    result = []
    for i in range(len(aList)):
        tmplst = list(aList[i])
        tmplst.sort()
        tmpstr = toString(tmplst)
        if tmpstr in hashit:
            hashit[tmpstr].add(aList[i])
        else:
            hashit[tmpstr] = {aList[i]}

    for i in hashit:
        result.append(list(hashit[i]))

    return result


def groupAnagram2(aList):
    result = []
    hashit = {}
    for i in range(len(aList)):
        tmplst = list(aList[i])
        tmplst.sort()
        tmpstr = toString(tmplst)
        if tmpstr in hashit:
            hashit[tmpstr].add(aList[i])
        else:
            hashit[tmpstr] = {aList[i]}

    for i in hashit:
        result.append(list(hashit[i]))
    return result

def toString(s1):
    return ''.join(s1)


Input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(Input))
print(groupAnagram2(Input))

