nums = [1, 2, 3]


def subsets(nums):
    res = []

    subsets = []

    def dfs(i):
        if i == len(nums):
            res.append(subsets.copy())
            return

        subsets.append(nums[i])
        dfs(i + 1)

        subsets.pop()
        dfs(i + 1)
    dfs(0)
    return res


print(subsets(nums))
