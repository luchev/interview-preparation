# Complexity (n = n, k = k)
# Time complexity: O(n * k)
# Space complexity: O(n * k)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 1000000007
        dp = [[0] * (k+1) for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(0, k+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    if j - i >= 0:
                        dp[i][j] = (dp[i][j-1] + dp[i-1][j] - dp[i - 1][j - i]) % mod
                    else:
                        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % mod
        if k > 0:
            return (dp[n][k] + mod - dp[n][k - 1]) % mod
        return 1