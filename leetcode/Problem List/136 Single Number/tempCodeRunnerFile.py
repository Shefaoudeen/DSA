        nums.sort()
        i = 0
        while (i < len(nums)):
            if nums[i] == nums[i+1]:
                pass
            else:
                return nums[i]
            i += 2
        if (i == len(nums)):
            return nums[i]