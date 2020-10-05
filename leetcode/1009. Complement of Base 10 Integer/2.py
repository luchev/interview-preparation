# Complexity (n = input number)
# Time complexity: O( loglog(n) ) log(n) is the number of bits and the algorithm to construc the mask is loglog(n)
# Space complexity: O(1)

# Another approach is to use binary search on the bits to get the most significant bit in loglog time

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        bitmask = N
        for i in [1, 2, 4, 8, 16]:
            bitmask |= (bitmask >> i)
        return ~N & bitmask
