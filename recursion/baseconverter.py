def baseConv(n, base):
    convertstring = "0123456789ABCDEFGH"

    if (n < base):
        return convertstring[n]
    else:
        return baseConv(n // base, base) + convertstring[n%base]

def reverseStr(expr):
    if len(expr) <= 1:
        return expr
    else:
        return  expr[len(expr)-1] +  reverseStr(expr[:len(expr)-1])

def checkpal(expr):
    return expr == reverseStr(expr)

print(baseConv(1453, 2))

print(reverseStr('abcdefgh'))

print(checkpal('aibohphobia'))