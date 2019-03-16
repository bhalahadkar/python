def minCoinChange(coinList, change):
    minChange = change
    if change in coinList:
        return 1
    else:
        for i in [c for c in coinList if c <= change]:
            numCoins = 1 + minCoinChange(coinList,change - i )
            if numCoins < minChange:
                minChange = numCoins

    return minChange

#print(minCoinChange([1, 5, 10, 25], 63))


def dynmincoinChange(coinList, change, memo):
    minChange = change
    if change in coinList:
        return 1
    elif memo[change] is not None:
        return memo[change]
    else:
        for i in [c for c in coinList if c <= change]:
            numCoins = 1 + dynmincoinChange(coinList, change - i, memo)
            memo[change] = numCoins
            if numCoins < minChange:
                minChange = numCoins

    return minChange

def fastminchange(coinList, change):
    memo = [None]*(change + 1)
    result = dynmincoinChange(coinList, change, memo)
    return result

print(fastminchange([1, 5, 10, 25], 63))

