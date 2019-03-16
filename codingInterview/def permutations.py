def permutations(string, step = 0):
    if step == len(string):
        print("".join(string))
    for i in range(step, len(string)):
        string_copy = [c for c in string]
        string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
        permutations(string_copy, step + 1)

#print (permutations ('one'))


def groupAnagram(aList):
    result = []
    hashit = {}
    found = False
    for i in range(len(aList)):
        tmplst = toMutable(alist[i])
        tmplst.sort()
        tmpstr = toString(tmplst)
        if tmpstr in hashit:
            hashit[tmpstr].add(alist[i])
        else:
            hashit[tmpstr] = {alist[i]}

    for i in hashit:
        result.append(hashit[i])
    return result

def toMutable(string):
    temp = []
    for x in string:
        temp.append(x)
    return temp


# Utility function to convert string to list
def toString(List):
    return ''.join(List)


alist = ['act', 'fast', 'dog', 'fish', 'cat', 'fats', 'eng']
print(groupAnagram(alist))