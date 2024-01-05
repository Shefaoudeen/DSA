def addTwoNumbers(l1, l2):
    l1.reverse()
    l2.reverse()
    Num1 = ""
    Num2 = ""
    for num in l1:
        Num1 += str(num)
    for num in l2:
        Num2 += str(num)
    answer = int(Num1)+int(Num2)
    answer = str(answer)
    answerList = []
    for i in range(0, len(answer)):
        answerList.append(int(answer[i]))
    answerList.reverse()
    return (answerList)


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(addTwoNumbers(l1, l2))
