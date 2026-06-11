nums = [1, 2, 1]


def subsets(nums):
    res = []

    subsets = []
    nums.sort()

    def dfs(i):
        if i == len(nums):
            res.append(subsets.copy())
            return

        subsets.append(nums[i])
        dfs(i + 1)

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        subsets.pop()
        dfs(i + 1)

    dfs(0)
    return res


print(subsets(nums))
