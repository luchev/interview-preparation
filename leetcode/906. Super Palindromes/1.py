# Complexity (n = left, k = right)
# Time complexity: O(100000)
# Space complexity: O(1n)

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        result = 0
        left = int(left)
        right = int(right)
        
        for x in range(100000):
            x = str(x)
            pal = int(x + x[::-1]) ** 2
            if left <= pal <= right and is_palindrome(str(pal)):
                result += 1

        for x in range(100000):
            x = str(x)
            pal = int(x + x[-2::-1]) ** 2
            if left <= pal <= right and is_palindrome(str(pal)):
                result += 1
        
        return result

def is_palindrome(x):
    return x == x[::-1]