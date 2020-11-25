# Complexity (k = number to find a divident)
# Time complexity: O(k) removed int overflowing into big int
# Space complexity: O(k)

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        n = 1
        n_len = 1
        remainders = set()
        while True:
            rem = n % K
            if rem == 0:
                return n_len
            if rem in remainders:
                return -1
            remainders.add(rem)
            n = (n * 10 + 1) % K
            n_len += 1
