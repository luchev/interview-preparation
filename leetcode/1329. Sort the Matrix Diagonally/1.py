# Complexity (n = rows of the matrix, m = cols of the matrix)
# Time complexity: O(n * m)
# Space complexity: O(min(n, m))

from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        def sort_diag(mat, row, col):
            diag = []
            while row < rows and col < cols:
                diag.append(mat[row][col])
                row += 1
                col += 1
            
            diag.sort()
            while row > 0 and col > 0:
                row -= 1
                col -= 1
                mat[row][col] = diag.pop()
            
        for row in range(rows - 1):
            sort_diag(mat, row, 0)
        for col in range(1, cols - 1):
            sort_diag(mat, 0, col)

        return mat
