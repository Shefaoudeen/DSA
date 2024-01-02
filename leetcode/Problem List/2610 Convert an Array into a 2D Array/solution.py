def findMatrix(nums):
    answer = []

    functionStatus = True
    while (functionStatus):
        array = []
        new = []
        for i in range(0, len(nums)):
            if (nums[i] not in array):
                array.append(nums[i])
            else:
                new.append(nums[i])
        nums = new
        answer.append(array)
        if (len(nums) == 0):
            functionStatus = False
    return answer


nums = list(map(int, input().split()))

print(findMatrix(nums))

## FINISHED##
