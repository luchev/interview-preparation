# Complexity (n = input length)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = {}
        def minCost(index):
            if index >= len(cost):
                return 0
            if index not in memory:
                memory[index] = cost[index] + min(minCost(index + 1), minCost(index + 2))
            return memory[index]
        return min(minCost(0), minCost(1))