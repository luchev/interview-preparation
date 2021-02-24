# Complexity (n = string length)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        depth = 0
        total = 0
        for i, x in enumerate(S):
            if x == '(':
                depth += 1
            else:
                depth -= 1
                if S[i - 1] == '(':
                    total += 1 << depth
        return total
