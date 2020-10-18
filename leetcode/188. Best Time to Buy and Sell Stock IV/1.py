# Complexity (n = length of prices, k = how many times we need to buy/sell)
# Time complexity: O(n * (n-k))
# Space complexity: O(n)

from typing import List
import math

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        intervals = [[prices[0]]]
        for i in range(1, len(prices)):
            if prices[i - 1] > prices[i]:
                intervals[-1].append(prices[i - 1])
                intervals.append([prices[i]])
        intervals[-1].append(prices[-1])

        intervals = [x for x in intervals if x[0] < x[1]]

        while len(intervals) > k:
            best_merge_value = math.inf
            best_merge_index = -1
            for i in range(1, len(intervals)):
                if intervals[i - 1][1] - intervals[i][0] < best_merge_value:
                    best_merge_value = intervals[i - 1][1] - intervals[i][0]
                    best_merge_index = i
                    print(best_merge_index, best_merge_value)

            best_remove_interval_index = 0
            best_remove_interval_value = math.inf
            for i in range(len(intervals)):
                if intervals[i][1] - intervals[i][0] < best_remove_interval_value:
                    best_remove_interval_index = i
                    best_remove_interval_value = intervals[i][1] - \
                        intervals[i][0]

            if best_merge_value > best_remove_interval_value:
                intervals.pop(best_remove_interval_index)
            else:
                intervals[best_merge_index -
                          1][1] = intervals[best_merge_index][1]
                intervals.pop(best_merge_index)

        return sum([x[1] - x[0] for x in intervals])
