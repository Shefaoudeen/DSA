    nums.sort()
    temp = nums
    operation = 0
    status = True
    while status:
        while 1:
            count = 1
            for j in range(1, len(nums)):
                if (nums[0] == nums[j]):
                    count += 1
            if (len(nums) == 0):
                return operation
            if (count % 2 == 0 or count % 3 == 0):
                if (count % 3 == 0):
                    temp.remove(nums[0])
                    temp.remove(nums[0])
                    temp.remove(nums[0])
                    operation += 1
                else:
                    temp.remove(nums[0])
                    temp.remove(nums[0])
                    operation += 1
            else:
                return -1
            exit
        print(temp)
        new = temp
        nums = new
        if (len(nums) == 0):
            return operation