import math

# piles = [1, 4, 3, 2]
# h = 9

piles = [1, 1, 1, 999999999]
h = 10


def minEatingSpeed(piles, h):
    maxK = max(piles)
    res = maxK
    left, right = 1, maxK

    while left <= right:
        middle = (left + right) // 2
        totalHours = 0
        for j in range(len(piles)):
            totalHours += math.ceil(piles[j] / middle)
            if totalHours > h:
                left = middle + 1
                break
        if totalHours <= h:
            if middle < res:
                res = middle
            right = middle - 1
    return res


print(minEatingSpeed(piles, h))
