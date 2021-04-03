# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stak = [-1]
        best = 0
        for index,char in enumerate(s):
            if char == '(':
                stak.append(index)
            elif char == ')':
                stak.pop()
                if len(stak) == 0:
                    stak.append(index)
                else:
                    best = max(best, index - stak[-1])

        return best
