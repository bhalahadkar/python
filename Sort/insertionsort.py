def insertsort(alist):
    for i in range(1, len(alist)):
        currentval = alist[i]
        pos = i

        while pos > 0 and alist[pos - 1] > currentval:
            alist[pos] = alist[pos -1]
            pos = pos - 1

        alist[pos] = currentval

alist = [54,26,93,17,77,31,44,55,20]
insertsort(alist)
print(alist)