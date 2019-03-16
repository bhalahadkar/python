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

def recursioSum(sumList):
    if len(sumList) == 1:
        return sumList[0]
    else:
        return (sumList[0] + recursioSum(sumList[1:]))

def anagram(s1, s2):
    alist = list(s1)
    blist = list(s2)
    sum1 = 0
    sum2 = 0

    for i in range(len(alist)):
        print(alist[i] + '->' + str(ord(alist[i])))
        sum1 = sum1 + ord(alist[i])

    for j in range(len(blist)):
        print(blist[j] + '->' + str(ord(blist[j])))
        sum2 = sum2 + ord(blist[j])

    print(sum1)
    print(sum2)

    if sum1 == sum2:
        return True
    else:
        return False