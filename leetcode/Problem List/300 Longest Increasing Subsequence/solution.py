def lengthOfLIS(nums):
    lis = []
    for element in nums:
        lis.append(1)

    for i in range(1, len(nums)):
        for j in range(0, i):
            if (nums[i] > nums[j] and lis[i] < lis[j]+1):
                lis[i] += 1

    maxTerm = max(lis)
    return maxTerm


nums = list(map(int, input().split()))
print(lengthOfLIS(nums))

## FINISHED##
