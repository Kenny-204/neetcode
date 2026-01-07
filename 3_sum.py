# nums =[-4,-1,-1,0,1,2]
nums = [1, 2, -2, -1]


# left = 0
# right = 5
# i = 0
# len = 6

# -1,-4,2 =-3
# -4,0,2 = -2
# -4, 1, 2 = -1

# i =1
# -4,-1,2 = -3
# -1,-1,2 = 0


def three_sum(nums):
    output = []
    seen = set()

    i = 0
    sorted_nums = sorted(nums)

    while i < len(sorted_nums):
        left = i + 1
        right = len(sorted_nums) - 1
        while left < right:
            total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            elif total == 0:
                candidate = [sorted_nums[i], sorted_nums[left], sorted_nums[right]]
                canon = tuple(candidate)
                if canon not in seen:
                    seen.add(tuple(candidate))
                    output.append(
                        [sorted_nums[i], sorted_nums[left], sorted_nums[right]]
                    )
                left += 1
                right -= 1
        i += 1
    return output


print(three_sum(nums))
