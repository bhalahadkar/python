def isPalindrome(expr):
    return expr == expr[::-1]

def longpal(expr):
    maxLen = 0

    for i in range(len(expr)):
        for j in range(i+1,len(expr)+1):
            newexpr = expr[i:j]
            if isPalindrome(newexpr) and len(newexpr) > maxLen:
                maxLen = len(newexpr)
                newpal = newexpr

    return newpal

print(longpal('aaaabbaa'))