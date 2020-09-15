# Complexity (n = input string length)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        whitespaceRemoved = False
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                whitespaceRemoved = True
                length += 1
            else:
                if whitespaceRemoved:
                    break
        return length
