def findMedianSortedArrays(nums1, num2):
    nums = nums1+nums2
    nums.sort()
    length = len(nums)
    if (length % 2 == 1):
        return (nums[int(length/2)])
    else:
        return ((nums[int(length/2)]+nums[int(length/2)-1])/2)


nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(findMedianSortedArrays(nums1, nums2))

## FINISHED##
