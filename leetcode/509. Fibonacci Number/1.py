# Complexity (n = input parameter)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def fib(self, n: int) -> int:
        cur = 0
        nxt = 1
        for _ in range(n):
            cur, nxt = nxt, cur + nxt
        return cur