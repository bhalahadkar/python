def recfibbo(n):
    if n <= 1:
        return n
    else:
        result = recfibbo(n-1) + recfibbo(n-2)
    return result

def recur_fibo(n):

   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


def forloopfib(n):

    if n == 0:
        return "Invalid value"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fiblist = [None] * (n)
        fiblist[0] = 0
        fiblist[1] = 1
        fiblist[2] = 1
        for i in range(3, n):
            fiblist[i] = fiblist[i-1] + fiblist[i-2]

    return fiblist

nterms = 0
for i in range(0):
    print(recfibbo(i))

print (forloopfib(10))