# Complexity (n = numRows)
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for curRow in range(1, numRows):
            row = []
            row.append(1)
            for k in range(0, curRow - 1):
                row.append(result[-1][k] + result[-1][k+1])
            row.append(1)
            result.append(row)
        return result