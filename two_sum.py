def twoSum(nums, target):
    map = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if nums[i] in map:
            return [map[nums[i]],i]
        else: map[difference] = i