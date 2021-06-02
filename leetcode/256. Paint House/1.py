# Complexity (n = input list size)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [costs[0][0], costs[0][1], costs[0][2]]
        nextDp = [0, 0, 0]
        for i in range(1, len(costs)):
            nextDp[0] = costs[i][0] + min(dp[1], dp[2])
            nextDp[1] = costs[i][1] + min(dp[0], dp[2])
            nextDp[2] = costs[i][2] + min(dp[0], dp[1])
            dp = nextDp
            nextDp = [0, 0, 0]
        return min(dp)

# r 1 4 1 7
# g 3 3 3 3
# b 0 5 5 2