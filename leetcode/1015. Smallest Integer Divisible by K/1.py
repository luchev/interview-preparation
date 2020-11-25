# Complexity (k = number to find a divident)
# Time complexity: O(k^2) because of using big int
# Space complexity: O(k)

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        n = 1
        remainders = set()
        while True:
            rem = n % K
            if rem == 0:
                return len(str(n))
            if rem in remainders:
                return -1
            remainders.add(rem)
            n = n * 10 + 1
