# Complexity (n = length of digits list, k = max length of representation (4 in our case))
# Time complexity: O(n * 4^n)
# Space complexity: O(n * 4^n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []
        
        keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        frontier = []
        nextFrontier = list(keys[int(digits[0])])
        for digit in digits[1:]:
            frontier = nextFrontier
            nextFrontier = []
            for char in keys[int(digit)]:
                for word in frontier:
                    nextFrontier.append(word + char)
        
        return nextFrontier