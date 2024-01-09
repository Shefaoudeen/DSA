class Solution:
    def merge(nums1, m, nums2, n):
        index = 0
        for i in range(m, m+n):
            nums1[i] = nums2[index]
            index += 1
        nums1.sort()


nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
n = int(input())

Solution.merge(nums1, m, nums2, n)

print(nums1)

## FINISHED##
