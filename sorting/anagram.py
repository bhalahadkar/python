def anagram(s1, s2):
    alist = list(s1)
    blist = list(s2)
    sum1 = 0
    sum2 = 0

    for i in range(len(alist)):
        print(alist[i] + '->' + str(ord(alist[i])))
        sum1 = sum1 + ord(alist[i])

    for j in range(len(blist)):
        print(blist[j] + '->' + str(ord(blist[j])))
        sum2 = sum2 + ord(blist[j])

    print(sum1)
    print(sum2)

    if sum1 == sum2:
        return True
    else:
        return False


print(anagram('rail safety','fairy tales'))
