import math


class Solution:
    def generate(numRows):
        answer = []
        for i in range(0, numRows):
            row = []
            row.append(1)
            if i > 0:
                for j in range(1, i+1):
                    if (j == i):
                        row.append(1)
                    else:
                        row.append(int(answer[i-1][j] + answer[i-1][j-1]))
            answer.append(row)
        return answer


numRows = int(input())
print(Solution.generate(numRows))
