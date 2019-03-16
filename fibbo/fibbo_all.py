import  datetime
def fibbo(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fibbo(n-1) + fibbo(n-2)

    return result

starttime = datetime.datetime.now()
print (fibbo(10))
endtime = datetime.datetime.now()
timetaken = endtime - starttime
print("Program run time:" + str(timetaken))

import datetime
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    fib_list = [None] * (n + 1)
    fib_list[1] = 1
    fib_list[2] = 1
    for i in range(3, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]

import datetime
def memofibbo(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = memofibbo(n-1, memo) + memofibbo(n-2, memo)
        memo[n] = result
        return result

def fibbo(n):
    memo = [None] * (n + 1)
    return (memofibbo(n, memo))