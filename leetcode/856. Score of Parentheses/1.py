# Complexity (n = string length)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stak = [0]
        for x in S:
            if x == '(':
                stak.append(0)
            else:
                top = stak.pop()
                stak[-1] += max(top * 2, 1)
        return stak[0]
