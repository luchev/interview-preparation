# Complexity (n = input length)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        s.append(' ')
        left = 0
        for right in range(len(s)):
            if s[right] == ' ':
                s[left:right] = s[left:right][::-1]
                left = right + 1
        s.pop()