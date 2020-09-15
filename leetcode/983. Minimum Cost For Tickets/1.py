# Complexity(n = length of days array, k = number of total days = 365 in this problem)
# Time complexity: O(k + n)
# Space complexity: O(k + n)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        cost = [0]
        for i in range(1, 365 + 1):
            if i in days:
                cost.append(min([
                    cost[-1] + costs[0],
                    cost[max(0, len(cost) - 1 - 6)] + costs[1],
                    cost[max(0, len(cost) - 1 - 29)] + costs[2]
                ]))
            else:
                cost.append(cost[-1])
        return cost[365]
