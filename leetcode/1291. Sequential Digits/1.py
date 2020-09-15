# Complexity ()
# Time complexity: O(1)
# Space complexity: O(1)
# The sequential number digits are 36 (8 with 2 digit + 7 with 3 digits + 6 + .. + 1 = 72 / 2 = 36)
# So we can compute them all and store them

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequentialNumbers = []
        for digits in range(2, 10):
            self.generateSequentialNumbers(digits, sequentialNumbers)

        result = []
        for number in sequentialNumbers:
            if low <= number <= high:
                result.append(number)
        return result

    def generateSequentialNumbers(self, digits, sequentialNumbers):
        for i in range(1, 9 - digits + 2):
            num = i

            for digit in range(i + 1, i + digits):
                num *= 10
                num += digit

            sequentialNumbers.append(num)
