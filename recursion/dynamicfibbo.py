def dynfib(n, memo):
    if memo[n] is not None:
        return memo[n]

    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = dynfib(n-1, memo) + dynfib(n -2, memo)

    return memo[n]

def fibbo(n):
    memo = [None] * (n+1)
    dynfib(n, memo)
    return memo

print(fibbo(3))


towerFrom = 3, 2, 1
towerint =
towertp =

towerFrom = 3
towerint = 1
towertp = 2

towerFrom = 3, 1
towerint = 2
towertp =

towerFrom = 3
towerint = 2, 1
towertp =

towerFrom =
towerint = 2, 1
towertp = 3

towerFrom = 1
towerint = 2
towertp = 3

towerFrom = 1
towerint =
towertp = 3, 2

towerFrom =
towerint =
towertp = 3, 2, 1











