# Complexity (n = length of strings to generate)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
