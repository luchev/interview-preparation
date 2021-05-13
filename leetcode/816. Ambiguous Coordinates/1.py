# Complexity (n = length of input string)
# Time complexity: O(n^3)
# Space complexity: O(n^3)

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        result = []
        digits = s[1:-1]
        for mid in range(1, len(digits)):
            left = digits[:mid]
            right = digits[mid:]
            for x in generateNumbers(left):
                for y in generateNumbers(right):
                    result.append('({}, {})'.format(x, y))
        return result

def generateNumbers(x: str) -> List[str]:
    result = []
    for i in range(1, len(x)):
        left = x[:i]
        right = x[i:]
        if str(int(left)) != left or right[-1] == '0':
            continue
        result.append('{}.{}'.format(left, right))
    if str(int(x)) == x:
        result.append(x)
    return result