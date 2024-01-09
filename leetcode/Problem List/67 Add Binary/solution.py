class Solution:
    def addBinary(a, b):
        num1 = Solution.deciamalConvertion(a)
        num2 = Solution.deciamalConvertion(b)
        total = num1+num2
        total = str(Solution.binaryConvertion(total))
        return total

    def deciamalConvertion(binary):
        return int(binary, 2)

    def binaryConvertion(decimal):
        return bin(decimal).replace("0b", "")


a = str(input())
b = str(input())
print(Solution.addBinary(a, b))

## FINISHED##
