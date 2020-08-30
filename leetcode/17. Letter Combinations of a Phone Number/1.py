# Complexity (n = length of digits list, k = max length of representation (4 in our case))
# Time complexity: O(n * 4^n)
# Space complexity: O(n) for the recursion stack, this excludes the space for the output array

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []
        result = []
        self.generateCombinations(digits, digitMap, "", result)
        return result

    def generateCombinations(self, digits: str, digitMap: dict, currentCombination: str, result: List[str]) -> None:
        if len(digits) == 0:
            result.append(currentCombination)
            return

        digit = digits[0]
        for char in digitMap[digits[0]]:
            self.generateCombinations(
                digits[1:], digitMap, currentCombination + char, result)
        return
