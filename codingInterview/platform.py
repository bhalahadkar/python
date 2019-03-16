def platformneed(arr, dep):
    n = len(arr)
    arr.sort()
    dep.sort()
    i = 1
    j = 0
    platform_need = 1
    result = 1

    while i < n and j < n:
        if arr[i] < dep[j]:
            platform_need += 1
            i += 1

            if (platform_need > result):
                result = platform_need
        else:
            j += 1
            platform_need -= 1

    return result

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(platformneed(arr, dep))