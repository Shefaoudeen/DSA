
N = int(input())
Array = list(map(int, input().split()))
missing = None
for i in range(1, N+1):
    if (i not in Array):
        missing = i
        break
print(missing)
