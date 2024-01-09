class Solution:
    def generate(numRows):
        answer = []
        for i in range(0, numRows):
            row = []
            for j in range(0, i+1):
                row[0] = 1
                row[i] = 1
                if i > 1:
                    for k in range(1, i):
                        row[k] = answer[i-1][k-1]+answer[i-1][k]
            answer.append(row)
        return (answer)


numRows = int(input())
print(Solution.generate(numRows))
