def plusOne(digits):
    num = ""
    for no in digits:
        num += str(no)
    num = str(int(num) + 1)
    numList = []
    for i in range(0, len(num)):
        numList.append(int(num[i]))
    return numList


digits = list(map(int, input().split()))
print(plusOne(digits))
