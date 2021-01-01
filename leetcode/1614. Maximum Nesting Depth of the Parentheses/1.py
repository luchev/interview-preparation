# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxDepth(self, s: str) -> int:
        open_paren = 0
        max_open = 0
        for char in s:
            if char == '(':
                open_paren += 1
                max_open = max(max_open, open_paren)
            elif char == ')':
                open_paren -= 1

        return max_open
