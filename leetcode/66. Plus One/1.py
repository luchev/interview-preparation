# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
