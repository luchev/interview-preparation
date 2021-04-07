# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return countVowels(s[:len(s) // 2].lower()) == countVowels(s[len(s) // 2:].lower())
        
def countVowels(s: str) -> int:
    return sum(char in ('a', 'e', 'i', 'o', 'u') for char in s)
