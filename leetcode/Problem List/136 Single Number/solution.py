class Solution:
    def singleNumber(nums):
        nums.sort()
        i = 0
        while (i < len(nums) and (i+1 < len(nums))):
            if nums[i] == nums[i+1]:
                pass
            else:
                return nums[i]
            i += 2
        if (i == len(nums)-1):
            return nums[i]


nums = list(map(int, input().split()))
print(Solution.singleNumber(nums))

## FINISHDED##
