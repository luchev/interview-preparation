# Complexity (n = number of items in the list)
# Time complexity: O(log(n))
# Space complexity: O(log(n))

from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        str_n = str(n)
        dp = [0] * (len(str_n) + 1)
        dp[0] = 1

        for i in range(len(str_n)):
            n_digit = str(str_n[len(str_n) - i - 1])
            for d in digits:
                if d < n_digit:
                    dp[i+1] += len(digits) ** i
                elif d == n_digit:
                    dp[i+1] += dp[i]

        shorter_numbers = sum(len(digits) ** i for i in range(1, len(str_n)))
        return dp[-1] + shorter_numbers
