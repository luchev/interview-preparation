# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        buyOn = prices[0]
        profit = 0

        for index, price in enumerate(prices):
            if price <= buyOn:
                buyOn = price
            else:
                if index == len(prices) - 1 or prices[index] > prices[index + 1]:
                    profit += price - buyOn
                    buyOn = price

        return profit
