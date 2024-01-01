n = int(input())
arr = list(map(int, input().split()))
answer = []

for i in range(1, n+1):
    if (arr[i-1] == i):
        answer.append(i)

print(answer)

## FINISHED##
