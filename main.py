def twoSum(self, nums, target):
    for num in nums:
        for num2 in range(0, len(nums)):
            new_num2 = nums[num2]
            if (num + new_num2 == target and nums.index(num) != num2):
                return [nums.index(num), num2]