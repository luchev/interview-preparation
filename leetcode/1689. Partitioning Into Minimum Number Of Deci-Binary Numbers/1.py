# Complexity (n = input string length)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(x) for x in n)