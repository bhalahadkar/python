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