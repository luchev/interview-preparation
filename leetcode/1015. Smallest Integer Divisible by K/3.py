# Complexity (k = number to find a divident)
# Time complexity: O(k)
# Space complexity: O(1)

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        n = 0
        for n_len in range(1, K+1):
            n = (n * 10 + 1) % K
            if n == 0:
                return n_len
        return -1
