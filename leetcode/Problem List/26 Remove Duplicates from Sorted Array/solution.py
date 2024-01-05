def removeDuplicates(nums):
    new = []
    for element in nums:
        if element not in new:
            new.append(element)
    for i in range(0, len(new)):
        nums[i] = new[i]

    return (len(new))


nums = list(map(int, input().split()))
print(removeDuplicates(nums))
