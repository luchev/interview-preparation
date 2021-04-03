# Complexity (n = number of ones, m = number of zeroes, k = strs length)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            counts = countDigits(s)
            for zeroes in range(m, counts[0] - 1, -1):
                for ones in range(n, counts[1] - 1, -1):
                    dp[zeroes][ones] = max(dp[zeroes][ones], 1 + dp[zeroes - counts[0]][ones - counts[1]])

        return dp[m][n]

def countDigits(s: str) -> List[int]:
    digits = [0] * 2
    zero = ord('0')
    for x in s:
        digits[ord(x) - zero] += 1
    return digits
