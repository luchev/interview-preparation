# Complexity(n = length of days array, k = max ticket duration = 30 for this problem)
# Time complexity: O(max(day in days))
# Space complexity: O(k + n) can be reduced to O(k) if we keep a pointer for the current day

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        startDay = days[0]
        endDay = days[-1]
        days = set(days)

        cost = [0 for x in range(0, 30)]  # rolling window for the last 30 days
        for day in range(startDay, endDay + 1):
            if day in days:
                cost[(day) % 30] = min([
                    # always >= 0 because days start from 1
                    cost[(day - 1) % 30] + costs[0],
                    cost[max(0, (day - 1 - 6) % 30)] + costs[1],
                    cost[max(0, (day - 1 - 29) % 30)] + costs[2]
                ])
            else:
                cost[(day) % 30] = cost[(day - 1) % 30]

        return max(cost)
