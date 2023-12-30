n = int(input())

array = list(map(str, input().split()))

names = []
count = []


for i in range(0, n):
    if (array[i] not in names):
        names.append(array[i])

for i in range(0, len(names)-1):
    count.append(0)

for i in range(0, n):
    for j in range(0, len(names) - 1):
        if (array[i] == names[j]):
            count[j] += 1

maxTerm = count[0]
maxIndex = 0

for i in range(1, len(names)-1):
    for j in range(i+1, len(names)-1):

        if (count[i] > maxTerm):
            maxIndex = int(i)

print(f"{names[maxIndex]} {count[maxIndex]}")
