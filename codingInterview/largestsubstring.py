def largsubstrlen(astr, bstr):
    maxlen = 0
    for i in range(len(astr)):
        for j in range(1,len(astr) + 1):
            if astr[i:j] in bstr and (len(astr[i:j]) > maxlen ):
                maxlen = len(astr[i:j])
    return maxlen

print(largsubstrlen('ABC', 'AC'))