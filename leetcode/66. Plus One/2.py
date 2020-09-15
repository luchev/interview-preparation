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
                return digits
        # If we leave the loop then we have 0000..00, so we put 1 in the front and add a 0 to the back
        digits[0] = 1
        digits.append(0)
        return digits
