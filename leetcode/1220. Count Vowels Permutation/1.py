# Complexity (n = desired length of strings)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        counts = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        
        for i in range(n - 1):
            counts = {
                'a': (counts['e'] + counts['i'] + counts['u']) % (10 ** 9 + 7),
                'e': (counts['a'] + counts['i']) % (10 ** 9 + 7),
                'i': (counts['e'] + counts['o']) % (10 ** 9 + 7),
                'o': (counts['i']) % (10 ** 9 + 7),
                'u': (counts['o'] + counts['i']) % (10 ** 9 + 7),
            }
        
        return sum(counts.values()) % (10 ** 9 + 7)