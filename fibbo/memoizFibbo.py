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

starttime = datetime.datetime.now()
print (fibbo(37))
endtime = datetime.datetime.now()
timetaken = endtime - starttime
print("Program run time:" + str(timetaken))


