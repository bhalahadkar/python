def checkpalindrome(expr):
    revexpr = expr[::-1]
    return expr == revexpr

print(checkpalindrome('malayalam'))