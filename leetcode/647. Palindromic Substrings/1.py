# Complexity (n = length of input string)
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        nPalindromes = 0
        
        for i in range(len(s)):
            for k in range(min(i, len(s) - i - 1) + 1):
                if s[i - k] != s[i + k]:
                    break
                nPalindromes += 1
        
        for left in range(len(s) - 1):
            right = left + 1
            for k in range(min(left, len(s) - right - 1) + 1):
                if s[left - k] != s[right + k]:
                    break
                nPalindromes += 1
        
        return nPalindromes
