# Complexity (n = input number)
# Time complexity: O(log(n))
# Space complexity: O(log(n))

class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum(int(digit) ** len(str(n)) for digit in str(n)) == n