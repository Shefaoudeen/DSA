def minOperations(nums):
    nums.sort()
    temp = nums
    operation = 0

    while 1:
        count = 1
        for j in range(1, len(nums)):
            if (nums[0] == nums[j]):
                count += 1
            else:
                break
        if (len(nums) == 0):
            return operation
        if count == 1:
            return -1
        while count > 1:
            if (len(nums) == 0):
                return operation
            if (count % 3 == 0 or count > 4):
                temp.remove(nums[0])
                temp.remove(nums[0])
                temp.remove(nums[0])
                operation += 1
                count -= 3

            elif (count % 2 == 0):
                temp.remove(nums[0])
                temp.remove(nums[0])
                operation += 1
                count -= 2

            new = temp
            nums = new
        if (len(nums) == 0):
            return operation
    if (len(nums) == 0):
        return operation
    else:
        return -1


nums = list(map(int, input().split()))

print(minOperations(nums))

## FINISHED##
