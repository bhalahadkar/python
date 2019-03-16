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

starttime = datetime.datetime.now()
print (fib_bottom_up(100))
endtime = datetime.datetime.now()
timetaken = endtime - starttime
print("Program run time:" + str(timetaken))
