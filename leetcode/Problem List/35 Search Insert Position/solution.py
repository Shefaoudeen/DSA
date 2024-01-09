def searchInsert(nums, target):
    if (target in nums):
        return (nums.index(target))
    else:
        for element in nums:
            if target < element:
                return (nums.index(element))
        return (len(nums))


nums = list(map(int, input().split()))
target = int(input())
print(searchInsert(nums, target))

## FINISHED##
