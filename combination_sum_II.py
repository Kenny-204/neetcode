nums = [2, 5, 6, 9]


def combinationSum2(nums, target):
    res = []

    subset = []
    nums.sort()

    def dfs(i, total):
        if total == target:
            res.append(subset.copy())
            return

        if i == len(nums) or total > target:
            return

        subset.append(nums[i])
        dfs(i + 1, total + nums[i])

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        subset.pop()
        dfs(i + 1, total)

    dfs(0, 0)
    return res


print(combinationSum2(nums, 9))
