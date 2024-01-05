def maxSumWithK(a, n, k):
    maxTerm = -9999
    for i in range(0, n):
        for j in range(i+k-1, n):
            Total = 0
            for index in range(i, j+1):
                Total += a[index]
            if Total > maxTerm:
                maxTerm = Total
    return maxTerm


n = int(input())
a = list(map(int, input().split()))
k = int(input())

print(maxSumWithK(a, n, k))
