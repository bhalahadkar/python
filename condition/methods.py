def sum_num(n1, n2):
    print(n1 + n2)

sum_num(5, 7)
sum_num(8,9)

def ret_sum(n1, n2):
    return(n1+n2)

x = ret_sum(2,3)

print(x)
print('*'*20)
def isMetro(city):
    l = ['sfo','nyc','la']
    if city in l:
        return('metro')
    else:
        return('notmetro')

x = isMetro('sfo')
y = isMetro('kc')

print(x)
print(y)

x = ret_sum('one', 'two')
print(x)