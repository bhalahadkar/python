def dynCoinChange(coinList, change, memo):
    minCoin = change
    if change in coinList:
        return 1
    elif memo[change] is not None:
        return memo[change]
    else:
        for i  in [c for c in coinList if c <= change]:
            numCoins = 1 + dynCoinChange(coinList, change - i, memo)
            memo[change] = numCoins
            if numCoins < minCoin:
                minCoin = numCoins

    return minCoin

def minNumCoin(coinList, change):
    memo = [None] * (change + 1)
    return dynCoinChange(coinList, change, memo)

print(minNumCoin([1, 5, 10, 25], 123))
#791374922