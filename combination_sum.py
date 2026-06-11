nums = [2, 5, 6, 9]


def combinationSum(nums, target):
    res = []

    subset = []

    def dfs(i, total):
        if total == target:
            res.append(subset.copy())
            return

        if i == len(nums) or total > target:
            return

        subset.append(nums[i])
        dfs(i , total + nums[i])

        subset.pop()
        dfs(i + 1, total)

    dfs(0, 0)
    return res


print(combinationSum(nums, 9))
