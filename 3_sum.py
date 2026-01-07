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

    left = 0
    right = len(nums) - 1
    i = 0
    sorted_nums = sorted(nums)

    while i < len(sorted_nums):
        while left < right:
            sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            elif sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            elif sum == 0:
                canon = tuple(
                    sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                )
                if canon not in seen:
                    seen.add(
                        tuple(
                            sorted(
                                [
                                    sorted_nums[i],
                                    sorted_nums[left],
                                    sorted_nums[right],
                                ]
                            )
                        )
                    )
                    output.append(
                        [sorted_nums[i], sorted_nums[left], sorted_nums[right]]
                    )
                left += 1
                right -= 1
        left = 0
        right = len(nums) - 1
        i += 1
    return output


print(three_sum(nums))
