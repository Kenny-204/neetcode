prices = [10, 1, 5, 6, 7, 1]


def maxProfit(prices):
    left, right = 0, 1
    maxval = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit > maxval:
            maxval = profit
        elif profit < 0:
            left = right
            right += 1
        elif profit >= 0:
            right += 1

    return maxval


print(maxProfit(prices))
