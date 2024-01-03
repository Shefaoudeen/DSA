def singleElement(arr, N):
    arr.sort()
    new = []
    count = 1
    for element in arr:
        if (element not in new):
            new.append(element)
        else:
            count += 1
        if count == 3:
            new.pop()
            count = 1
    return (new[0])


N = int(input())
arr = list(map(int, input().split()))

print(singleElement(arr, N))

## FINISHED##
