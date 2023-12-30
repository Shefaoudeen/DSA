def winner(arr, n):
    names = []
    count = []
    for i in range(0, n):
        if (arr[i] not in names):
            names.append(arr[i])
    for i in range(0, len(names)-1):
        count.append(0)
    for i in range(0, n):
        for j in range(0, len(names) - 1):
            if (arr[i] == names[j]):
                count[j] += 1
    maxTerm = count[0]
    maxIndex = 0
    for i in range(1, len(names)-1):
        for j in range(i+1, len(names)-1):
            if (count[i] > maxTerm):
                maxIndex = int(i)
    return (f"{names[maxIndex]} {count[maxIndex]}")


n = int(input())
array = list(map(str, input().split()))
print(winner(array, n))
