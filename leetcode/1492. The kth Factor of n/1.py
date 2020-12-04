# Complexity (n = number to find factors for, k = Kth factor to find)
# Time complexity: O(n)
# Space complexity: O(sqrt(n))

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for x in range(1, n+1):
            if n % x == 0:
                factors.append(x)

        if k <= len(factors):
            return factors[k-1]
        else:
            return -1
