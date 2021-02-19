# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        leftRight = []
        openBrackets = 0
        for char in s:
            if char == '(':
                openBrackets += 1
            elif char == ')':
                if openBrackets == 0:
                    continue
                openBrackets -= 1
            leftRight.append(char)

        result = []
        openBrackets = 0
        for char in reversed(leftRight):
            if char == ')':
                openBrackets += 1
            elif char == '(':
                if openBrackets == 0:
                    continue
                openBrackets -= 1
            result.append(char)
        
        return ''.join(reversed(result))
