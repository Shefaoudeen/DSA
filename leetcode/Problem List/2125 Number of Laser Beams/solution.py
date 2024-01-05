bank = list(map(str, input().split()))

number = []

for laser in bank:
    count = 0
    for i in range(0, len(laser)):
        if (laser[i] == '1'):
            count += 1
    number.append(count)

beam = 0
n = len(number)
answer = 0
for i in range(0, n):
    for j in range(i+1, n):
        if (number[j] != 0):
            answer += (number[i]*number[j])
            break

print(answer)
