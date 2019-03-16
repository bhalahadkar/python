mystring = 'abcabc'
for c in mystring:
    if c=='a':
        print(c.upper(),end=' ')
    else:
        print(c, end=' ')

print('\n')

cars = ['bmw','benz','audi']
for car in cars:
    print(car)

print('*'*20)
d = {'one':1,'two':2, 'three':3}
for k in d:
    print(k + ' '+ str(d[k]))

print('-'*20)
for k,v in d.items():
    print(k+'--'+str(v))
print(str(d.items()))

l1 = [1,2,3]
l2 = [5,6,7,8,9]
for a,b in zip(l1, l2):
    print(str(a) + '---' + str(b))
print('*'*40)
print('|'*40)
print('*'*40)
print(list(range(0,10)))
a =range(0,10)
print(a)
print(type(a))

for num in range(3):
    print(num)