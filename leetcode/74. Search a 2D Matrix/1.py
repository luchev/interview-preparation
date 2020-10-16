# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        cells = rows * cols

        start = 0
        end = cells - 1
        while start <= end:
            mid = (start + end) // 2
            row, col = convert_to_row_col(cols, mid)
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


def convert_to_row_col(cols: int, x) -> int:
    return (x // cols, x % cols)
