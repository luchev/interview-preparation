# Complexity (n = string length)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if 1 <= int(s[0]) <= 9:
            dp[1] = 1

        for i in range(2, len(dp)):
            s_index = i - 1
            if 1 <= int(s[s_index]) <= 9:
                dp[i] = dp[i - 1]

            if 10 <= int(s[s_index - 1: s_index + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
