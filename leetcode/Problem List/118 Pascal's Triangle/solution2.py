import math


class Solution:
    def generate(rowIndex):
        answer = []
        finalAnswer = []
        for i in range(0, rowIndex+1):
            row = []
            row.append(1)
            if i > 0:
                for j in range(1, i+1):
                    if (j == i):
                        row.append(1)
                    else:
                        row.append(int(answer[i-1][j] + answer[i-1][j-1]))
            answer.append(row)
            if (i == rowIndex):
                for element in row:
                    finalAnswer.append(element)
        return finalAnswer


rowIndex = int(input())
print(Solution.generate(rowIndex))
