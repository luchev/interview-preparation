# Complexity (n = argument n)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        length = 0
        result = 0
        for i in range(1, n+1):
            if i & ( i - 1) == 0:
                length += 1
            result = ((result << length) | i) % (10 ** 9 + 7)
        return result
