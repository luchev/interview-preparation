# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ones = 0
        zeros = 0
        result = 0
        current = 'x'
        for char in s:
            if char != current:
                result += min(ones, zeros)
                current = char
                if char == '1':
                    ones = 0
                elif char == '0':
                    zeros = 0
            
            if char == '0':
                zeros += 1
            elif char == '1':
                ones += 1
        
        result += min(ones, zeros)
        return result
