# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        balance = [0] * len(dominoes)

        b = 0
        for index, c in enumerate(dominoes):
            if c == 'R':
                b = n
            elif c == 'L':
                b = 0
            else:
                b = max(b - 1, 0)
            balance[index] += b

        b = 0
        for index, c in enumerate(reversed(dominoes)):
            index = -index - 1
            if c == 'R':
                b = 0
            elif c == 'L':
                b = n
            else:
                b = max(b - 1, 0)
            balance[index] -= b

        result = ['.'] * len(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] == 'R' or dominoes[i] == 'L':
                result[i] = dominoes[i]
            elif balance[i] > 0:
                result[i] = 'R'
            elif balance[i] < 0:
                result[i] = 'L'
        return ''.join(result)
