nums = [-1, 0, 2, 4, 6, 8]
target = 4


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
    return -1


print(search(nums, target))
